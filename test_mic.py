import sounddevice as sd
import numpy as np
import wave

print(sd.query_devices())
print("\nVarsayilan giris cihazi:", sd.default.device[0])

SR = 16000  # Whisper icin standart ornekleme hizi
print("\n5 saniye kayit basliyor, konus...")
rec = sd.rec(int(5 * SR), samplerate=SR, channels=1, dtype="int16")
sd.wait()
print("Kayit bitti. Ses seviyesi (maks):", int(np.abs(rec).max()))

with wave.open("test_ses.wav", "wb") as f:
    f.setnchannels(1)
    f.setsampwidth(2)
    f.setframerate(SR)
    f.writeframes(rec.tobytes())

print("Simdi kaydi calıyorum...")
sd.play(rec, SR)
sd.wait()
