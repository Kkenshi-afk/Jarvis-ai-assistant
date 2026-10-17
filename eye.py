import os
import time
from google import genai
from google.genai import types

import config
from capture import capture_frame

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])


def ask(question):
    """Kare cek, Gemini'ye sor, (cevap, sureler) dondur."""
    t0 = time.perf_counter()
    img = capture_frame()
    t1 = time.perf_counter()

    resp = client.models.generate_content(
        model=config.MODEL,
        contents=[
            types.Part.from_bytes(data=img, mime_type="image/jpeg"),
            question,
        ],
        config=types.GenerateContentConfig(
            system_instruction=config.SYSTEM_PROMPT,
        ),
    )
    t2 = time.perf_counter()
    return resp.text, t1 - t0, t2 - t1


def main():
    print(f"{config.ASSISTANT_NAME} hazir. Cikmak icin bos birak.")
    while True:
        q = input("\nSoru: ").strip()
        if not q:
            break
        try:
            text, t_cam, t_llm = ask(q)
            print(f"\n{config.ASSISTANT_NAME}: {text}")
            print(f"[kare: {t_cam:.2f} sn | gemini: {t_llm:.2f} sn]")
        except Exception as e:
            print("HATA:", type(e).__name__)
            print(str(e)[:300])


if __name__ == "__main__":
    main()
