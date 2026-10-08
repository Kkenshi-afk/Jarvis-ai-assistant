import os
from google import genai
from google.genai import types

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

with open("test_kare.jpg", "rb") as f:
    img = f.read()

while True:
    soru = input("\nSoru (cikmak icin bos birak): ").strip()
    if not soru:
        break
    resp = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=[
            types.Part.from_bytes(data=img, mime_type="image/jpeg"),
            soru + " Kisa Turkce cevap ver.",
        ],
    )
    print("Cevap:", resp.text)
