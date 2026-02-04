import os
from google import genai
from dotenv import load_dotenv


# Configuration
def cargar_configuracion():
    """Load environment variables and initialize API client."""
    load_dotenv()
    clave_api = os.getenv("GEMINI_API_KEY")
    if not clave_api:
        raise ValueError("GEMINI_API_KEY not found in environment variables")
    return genai.Client(api_key=clave_api)


# Main function
def ejecutar_consulta(client):
    """Execute a query to the Gemini API."""
    print("🚀 Conectando con el motor de Gemini ...\n")
    
    try:
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents="Eres un consejero experto de la agencia de viajes Dani Torres. "
                     "Tu rol es ayudar a los clientes a planificar sus viajes, "
                     "recomendando destinos, hoteles, actividades y paquetes turísticos. "
                     "Preséntate brevemente con profesionalismo y entusiasmo."
        )
        
        print("\n" + "="*50)
        print("✈️  RESPUESTA DE DANI TORRES AGENCIA DE VIAJES")
        print("="*50)
        print(response.text)
        print("="*50 + "\n")
        
    except Exception as e:
        print(f"❌ Ocurrió un error en la conexión: {e}")


if __name__ == "__main__":
    client = cargar_configuracion()
    ejecutar_consulta(client)
