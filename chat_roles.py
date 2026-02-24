import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# 1. Configuración de entorno
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# 2. Inicialización del cliente
client = genai.Client(api_key=API_KEY)

# 3. Configuración del modelo
configuration = types.GenerateContentConfig(
    max_output_tokens=2048,
    system_instruction=(
        "Eres un asistente de estudio especializado en Inteligencia Artificial. "
        "Tus respuestas deben ser concisas, educativas para un estudiante de Ingeniería de Sistemas. "
        "Si la pregunta no es de IA, di que no puedes responder."
    )
)

# 4. Interacción
text = input("Escribe tu pregunta sobre Inteligencia Artificial: ")

# 5. Ejecución y manejo de errores
print("\n--- Respuesta del Asistente ---")
try:
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=configuration,
        contents=text
    )
    # Si todo sale bien, imprimimos aquí
    print(response.text)

except Exception as e:
    # Si hay error, informamos al usuario de forma limpia
    if "429" in str(e):
        print("🔴 Error: Has agotado tu cuota gratuita (429). Espera 60 segundos o revisa tu API Key en AI Studio.")
    else:
        print(f"🔴 Ocurrió un error inesperado: {e}")

# Ya no necesitamos el 'print(response.text)' aquí afuera porque ya lo manejamos arriba.