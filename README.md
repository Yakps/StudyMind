<img width="1454" height="774" alt="Ekran Resmi 2026-05-07 14 47 45" src="https://github.com/user-attachments/assets/d6bacb38-a7f3-458a-b58d-f3a2d17f289c" />

<img width="1469" height="830" alt="Ekran Resmi 2026-05-07 14 59 13" src="https://github.com/user-attachments/assets/d4ac073f-1259-4031-b0e9-ff91155c75d8" />
<img width="1470" height="829" alt="Ekran Resmi 2026-05-07 14 59 53" src="https://github.com/user-attachments/assets/1c4aec32-3e85-4c97-a23f-2542d1f38e49" />
# StudyMind

Upload PDF or DOCX files, paste your lecture notes — GPT-4o automatically generates summaries, flashcards, and quiz questions.

---

## Features

- **Summary** — Summarize text with short, medium, or detailed options
- **Flashcards** — 14–18 cards that reveal the answer on click
- **Quiz Questions** — 10 multiple-choice questions generated each time
- **New Questions** — Request different questions from the same text
- **TR / EN** — Switch the interface language using the button in the top right
- **File Support** — PDF and DOCX formats
- **Fully Turkish output**

---

## Installation

### 1. Clone the project
```bash
git clone https://github.com/kullanici/StudyMind.git
cd StudyMind
```

### 2. Create and activate a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate      # Mac / Linux
.venv\Scripts\activate         # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up your API key

Copy `settings_example.py` to create `settings.py`:
```bash
cp settings_example.py settings.py
```

Then open `settings.py` and enter your OpenAI API key:
```python
OPENAI_API_KEY = "sk-..."
```

> `settings.py` is listed in `.gitignore` — your key will never be pushed to GitHub.  
> If you add the key to `settings.py`, you won't need to enter it again in the interface.

### 5. Start the app
```bash
python app.py
```

Open in your browser: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## File Structure

```
StudyMind/
├── app.py                  # Flask backend
├── settings.py             # API key — NOT pushed to GitHub
├── settings_example.py     # Example config file — copy this
├── requirements.txt        # Python dependencies
├── .gitignore              # Files excluded from Git
├── static/
│   └── style.css           # Interface styles
└── templates/
    └── index.html          # Interface
```

---

## settings.py Options

| Variable | Default | Description |
|---|---|---|
| `OPENAI_API_KEY` | `"sk-..."` | Your OpenAI API key |
| `OPENAI_MODEL` | `"gpt-4o"` | Model to use |
| `SECRET_KEY` | `"secret"` | Flask session key |
| `HOST` | `"127.0.0.1"` | Server address |
| `PORT` | `5000` | Server port |
| `DEBUG` | `True` | Development mode |

---

## Requirements

- Python 3.9+
- OpenAI API key ([platform.openai.com](https://platform.openai.com))

---

## Notes

- Analysis won't start if the text is shorter than 100 characters
- Only the first 6,000 characters of the text are processed
- Click a flashcard to reveal the back side (answer)
- Your score is shown once all questions are answered
- Don't forget to activate the virtual environment: `source .venv/bin/activate`


--------------


#StudyMind(Türkçe)

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
