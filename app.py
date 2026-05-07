from flask import Flask, request, jsonify, render_template
import openai
import pdfplumber
import docx
import json
import io

try:
    import settings
    _API_KEY = getattr(settings, "OPENAI_API_KEY", "")
    _MODEL   = getattr(settings, "OPENAI_MODEL", "gpt-4o")
    _SECRET  = getattr(settings, "SECRET_KEY", "gizli")
    _HOST    = getattr(settings, "HOST", "127.0.0.1")
    _PORT    = getattr(settings, "PORT", 5000)
    _DEBUG   = getattr(settings, "DEBUG", True)
except ImportError:
    _API_KEY = ""
    _MODEL   = "gpt-4o"
    _SECRET  = "gizli"
    _HOST    = "127.0.0.1"
    _PORT    = 5000
    _DEBUG   = True

app = Flask(__name__)
app.secret_key = _SECRET


def pdf_oku(dosya_bytes: bytes) -> str:
    metin = ""
    with pdfplumber.open(io.BytesIO(dosya_bytes)) as pdf:
        for sayfa in pdf.pages:
            icerik = sayfa.extract_text()
            if icerik:
                metin += icerik + "\n"
    return metin.strip()


def docx_oku(dosya_bytes: bytes) -> str:
    doc = docx.Document(io.BytesIO(dosya_bytes))
    return "\n".join([p.text for p in doc.paragraphs if p.text.strip()])


def gpt_analiz(metin: str, api_key: str, model: str, ozet_uzunlugu: str) -> dict:
    client = openai.OpenAI(api_key=api_key)
    uzunluk_map = {
        "kisa":    "3-5 cumle",
        "orta":    "1 paragraf (8-10 cumle)",
        "detayli": "2-3 paragraf",
    }
    uzunluk = uzunluk_map.get(ozet_uzunlugu, "1 paragraf")

    prompt = f"""
Asagidaki metni analiz et ve JSON formatinda yanit ver.
Turkce yanit ver. Yanitinin SADECE gecerli JSON olmasi gerekiyor, baska hicbir sey ekleme.

Sema:
{{
  "ozet": "Metnin {uzunluk} ozeti",
  "flashcardlar": [
    {{"soru": "...", "cevap": "..."}},
    ...
  ],
  "sinav_sorulari": [
    {{"soru": "...", "secenekler": ["A) ...", "B) ...", "C) ...", "D) ..."], "dogru": "A"}},
    ...
  ]
}}

Kurallar:
- En az 14, en fazla 18 flashcard uret
- Tam olarak 10 sinav sorusu uret (coktan secmeli, 4 sik)
- Flashcard sorulari kisa ve net olsun
- Sinav sorulari birbirinden farkli konulari test etsin
- Her sinav sorusunun dogru cevabi A, B, C veya D siklarindan biri olsun

Metin:
\"\"\"
{metin[:6000]}
\"\"\"
"""

    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,
        max_tokens=4500,
    )
    raw = response.choices[0].message.content.strip()
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
    return json.loads(raw.strip())


def gpt_yeni_sorular(metin: str, api_key: str, model: str) -> dict:
    client = openai.OpenAI(api_key=api_key)

    prompt = f"""
Asagidaki metinden YENI ve FARKLI coktan secmeli sinav sorulari uret.
Turkce yanit ver. Yanitinin SADECE gecerli JSON olmasi gerekiyor.

Sema:
{{
  "sinav_sorulari": [
    {{"soru": "...", "secenekler": ["A) ...", "B) ...", "C) ...", "D) ..."], "dogru": "A"}},
    ...
  ]
}}

Kurallar:
- Tam olarak 10 FARKLI soru uret
- Daha once sorulmus olabilecek sorulardan kacin, farkli acılardan sor
- Her sorunun dogru cevabi A, B, C veya D siklarindan biri olsun
- Sorular metnin farkli bolumlerini test etsin

Metin:
\"\"\"
{metin[:6000]}
\"\"\"
"""

    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.85,
        max_tokens=3500,
    )
    raw = response.choices[0].message.content.strip()
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
    return json.loads(raw.strip())


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/analiz", methods=["POST"])
def analiz():
    try:
        api_key = _API_KEY or request.form.get("api_key", "").strip()
        model   = _MODEL
        ozet_uzunlugu = request.form.get("ozet_uzunlugu", "orta")
        manuel_metin  = request.form.get("metin", "").strip()

        if not api_key:
            return jsonify({"hata": "API anahtari bulunamadi. settings.py dosyasini kontrol edin."}), 400

        metin = ""
        if "dosya" in request.files and request.files["dosya"].filename:
            dosya = request.files["dosya"]
            icerik = dosya.read()
            if dosya.filename.endswith(".pdf"):
                metin = pdf_oku(icerik)
            elif dosya.filename.endswith(".docx"):
                metin = docx_oku(icerik)
        elif manuel_metin:
            metin = manuel_metin

        if not metin or len(metin) < 100:
            return jsonify({"hata": "Metin cok kisa veya okunamadi."}), 400

        sonuc = gpt_analiz(metin, api_key, model, ozet_uzunlugu)
        sonuc["_metin"] = metin[:6000]
        return jsonify(sonuc)

    except json.JSONDecodeError:
        return jsonify({"hata": "API yaniti islenemedi. Tekrar dene."}), 500
    except Exception as e:
        return jsonify({"hata": str(e)}), 500


@app.route("/yeni-sorular", methods=["POST"])
def yeni_sorular():
    try:
        data    = request.get_json()
        api_key = _API_KEY or data.get("api_key", "").strip()
        metin   = data.get("metin", "").strip()

        if not api_key:
            return jsonify({"hata": "API anahtari bulunamadi."}), 400
        if not metin:
            return jsonify({"hata": "Metin bulunamadi."}), 400

        sonuc = gpt_yeni_sorular(metin, api_key, _MODEL)
        return jsonify(sonuc)

    except json.JSONDecodeError:
        return jsonify({"hata": "API yaniti islenemedi. Tekrar dene."}), 500
    except Exception as e:
        return jsonify({"hata": str(e)}), 500


if __name__ == "__main__":
    app.run(host=_HOST, port=_PORT, debug=_DEBUG)