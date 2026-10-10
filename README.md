# Robin

Gercek zamanli goruntu asistani (kamera + ses + Gemini).

## Durum
- [x] Asama 0: Kurulum, kamera, mikrofon, Gemini testleri
- [ ] Asama 1: Goz
- [ ] Asama 2: Kulak ve agiz
- [ ] Asama 3+: MVP, gercek zamanlilik, hafiza, arayuz

## Kurulum (Windows, Python 3.12)

    python -m venv venv
    source venv/Scripts/activate
    pip install -r requirements.txt

API anahtarini ortam degiskeni olarak tanimla (koda yazma):

    setx GEMINI_API_KEY "anahtarin"

## Calistirma

    python test_camera.py
    python ask_vision.py
