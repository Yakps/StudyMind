<img width="1454" height="774" alt="Ekran Resmi 2026-05-07 14 47 45" src="https://github.com/user-attachments/assets/d6bacb38-a7f3-458a-b58d-f3a2d17f289c" />

<img width="1469" height="830" alt="Ekran Resmi 2026-05-07 14 59 13" src="https://github.com/user-attachments/assets/d4ac073f-1259-4031-b0e9-ff91155c75d8" />
<img width="1470" height="829" alt="Ekran Resmi 2026-05-07 14 59 53" src="https://github.com/user-attachments/assets/1c4aec32-3e85-4c97-a23f-2542d1f38e49" />

#StudyMind

PDF veya DOCX dosyalarını yükle, ders notlarını yapıştır — GPT-4o otomatik olarak özet, flashcard ve sınav soruları üretsin.

-----------

## Özellikler

-Özet- Kısa, orta veya detaylı seçeneklerle metnin özeti
-Flashcard— 14–18 arası kart, tıklayınca cevap gösterir
-Sınav Soruları— Her seferinde 10 çoktan seçmeli soru
-Yeni Sorular Üret— Aynı metinden farklı sorular isteyebilirsin
-TR / EN— Sağ üstteki butonla arayüz dilini değiştirebilirsin
-Dosya Desteği— PDF ve DOCX formatları
-Tamamen Türkçe-çıktı

-----------

##Kurulum

### 1. Projeyi klonla

```bash
git clone https://github.com/kullanici/StudyMind.git
cd StudyMind
```

### 2. Sanal ortam oluştur ve aktif et

```bash
python -m venv .venv
source .venv/bin/activate      # Mac / Linux
.venv\Scripts\activate         # Windows
```

### 3. Bağımlılıkları yükle

```bash
pip install -r requirements.txt
```

### 4. API anahtarını ayarla

`settings_example.py` dosyasını kopyalayarak `settings.py` oluştur:

```bash
cp settings_example.py settings.py
```

Ardından `settings.py` dosyasını aç ve OpenAI API anahtarını gir:

```python
OPENAI_API_KEY = "sk-..."
```

> `settings.py` dosyası `.gitignore`'a eklenmiştir — anahtarın GitHub'a yüklenmez.
> API anahtarını `settings.py`'ye yazarsan arayüzde tekrar girmen gerekmez.

### 5. Uygulamayı başlat

```bash
python app.py
```

Tarayıcıda aç: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## Dosya Yapısı

```
StudyMind/
├── app.py                  # Flask backend
├── settings.py             # API anahtarı — GitHub'a yüklenMEZ
├── settings_example.py     # Örnek ayar dosyası — bunu kopyala
├── requirements.txt        # Python bağımlılıkları
├── .gitignore              # Git dışında tutulacak dosyalar
├── static/
│   └── style.css           # Arayüz stilleri
└── templates/
    └── index.html          # Arayüz
```

---

## settings.py Ayarları

| Değişken | Varsayılan | Açıklama |
|---|---|---|
| `OPENAI_API_KEY` | `"sk-..."` | OpenAI API anahtarın |
| `OPENAI_MODEL` | `"gpt-4o"` | Kullanılacak model |
| `SECRET_KEY` | `"gizli"` | Flask oturum anahtarı |
| `HOST` | `"127.0.0.1"` | Sunucu adresi |
| `PORT` | `5000` | Sunucu portu |
| `DEBUG` | `True` | Geliştirme modu |

---

## Gereksinimler

- Python 3.9+
- OpenAI API anahtarı ([platform.openai.com](https://platform.openai.com))

---

## Notlar

- Metin 100 karakterden kısa olursa analiz başlamaz
- Metinden ilk 6000 karakter işlenir
- Flashcard'a tıklayınca arka yüz (cevap) görünür
- Tüm sorulara cevap verilince skor gösterilir
- Sanal ortamı aktif etmeyi unutma: `source .venv/bin/activate`
