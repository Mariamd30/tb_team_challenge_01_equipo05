import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai

env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError(f"No se encontró GEMINI_API_KEY (buscando en {env_path})")

client = genai.Client(api_key=API_KEY)
MODEL = "gemini-flash-latest"