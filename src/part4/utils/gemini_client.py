import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai

<<<<<<< HEAD
=======
# Busca el .env en la MISMA carpeta que este archivo, sin importar
# desde dónde ejecutes el script. Evita el bug de rutas relativas.
>>>>>>> feature/Parte_4_extensiones_con_Gemini
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError(f"No se encontró GEMINI_API_KEY (buscando en {env_path})")

client = genai.Client(api_key=API_KEY)
<<<<<<< HEAD
=======

# gemini-flash-latest apunta siempre a la última versión estable de Flash,
# así no tienes que actualizar el string cada vez que Google libera un modelo nuevo.
>>>>>>> feature/Parte_4_extensiones_con_Gemini
MODEL = "gemini-flash-latest"