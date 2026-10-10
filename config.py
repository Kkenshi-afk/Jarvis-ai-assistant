# Ayarlar tek yerde. Bir sey degisirse sadece burayi duzelt.

# --- Asistan adi ---
ASSISTANT_NAME = "Robin"

# --- Model ---
MODEL = "gemini-3.8-flash"   # Model adi eskirse list_models.py ile guncelini bul

# --- Kamera ---
CAMERA_INDEX = 0             # Yanlis kamera acilirsa 1 yap
WARMUP_FRAMES = 10           # Ilk karanlik kareleri atlamak icin
FRAME_WIDTH = 640            # Gemini'ye gonderilecek karenin genisligi (px)
JPEG_QUALITY = 85            # 1-100, dusuk = kucuk dosya

# --- Asistan kisiligi ---
SYSTEM_PROMPT = (
    f"Sen Robin adli bir gorsel asistansin. "
    "Kullanicinin kamerasindan gelen goruntuye bakarak "
    "Turkce, kisa ve dogal cevap ver."
)
