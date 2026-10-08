import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if not cap.isOpened():
    raise SystemExit("Kamera acilamadi. Baska bir uygulama kullaniyor olabilir.")

for _ in range(15):
    cap.read()

ok, frame = cap.read()
cap.release()

if not ok:
    raise SystemExit("Kare alinamadi.")

cv2.imwrite("test_kare.jpg", frame)
print("Kaydedildi: test_kare.jpg", frame.shape)
