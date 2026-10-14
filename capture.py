import cv2
import config


def capture_frame():
    """Kameradan bir kare alir, kucultur, JPEG bayt olarak dondurur."""
    cap = cv2.VideoCapture(config.CAMERA_INDEX, cv2.CAP_DSHOW)
    if not cap.isOpened():
        raise RuntimeError("Kamera acilamadi. Baska bir uygulama kullaniyor olabilir.")
    try:
        for _ in range(config.WARMUP_FRAMES):
            cap.read()
        ok, frame = cap.read()
    finally:
        cap.release()

    if not ok:
        raise RuntimeError("Kare alinamadi.")

    h, w = frame.shape[:2]
    if w > config.FRAME_WIDTH:
        new_h = int(h * config.FRAME_WIDTH / w)
        frame = cv2.resize(frame, (config.FRAME_WIDTH, new_h))

    ok, buf = cv2.imencode(".jpg", frame, [cv2.IMWRITE_JPEG_QUALITY, config.JPEG_QUALITY])
    if not ok:
        raise RuntimeError("JPEG'e cevrilemedi.")
    return buf.tobytes()


if __name__ == "__main__":
    # Dogrudan calistirilirsa test eder: python capture.py
    data = capture_frame()
    with open("capture_test.jpg", "wb") as f:
        f.write(data)
    print(f"Tamam: capture_test.jpg ({len(data) // 1024} KB)")
