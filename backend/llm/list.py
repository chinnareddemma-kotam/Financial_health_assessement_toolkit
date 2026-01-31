import os
import google.genai as genai
from dotenv import load_dotenv
load_dotenv()
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

models = client.models.list()

for m in models:
    print("MODEL NAME:", m.name)
    print("RAW MODEL DATA:", m)
    print("-" * 60)
