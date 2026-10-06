import os
from google import genai

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
resp = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Merhaba de, tek cumle.",
)
print(resp.text)