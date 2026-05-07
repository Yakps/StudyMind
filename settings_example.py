# ─────────────────────────────────────────────
#  settings_example.py
#  Bu dosyayı kopyalayıp settings.py olarak kaydet,
#  ardından kendi bilgilerini gir.
#
#  cp settings_example.py settings.py
# ─────────────────────────────────────────────

# OpenAI API anahtarın (platform.openai.com)
OPENAI_API_KEY = "sk-..."

# Kullanılacak model
OPENAI_MODEL = "gpt-4o"

# Flask gizli anahtarı — rastgele güçlü bir şey yaz
SECRET_KEY = "buraya-gizli-bir-sey-yaz"

# Sunucu ayarları
HOST  = "127.0.0.1"
PORT  = 5000
DEBUG = True
