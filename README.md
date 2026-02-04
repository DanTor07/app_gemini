# Gemini API - Agencia de Viajes Dani Torres 🚀

Este proyecto implementa una aplicación que se conecta con la API de Google Gemini para proporcionar asesoramiento de viajes a través de la agencia **Dani Torres**.

## 📋 Requisitos Previos

- **Python 3.9** instalado
- Acceso a internet
- Clave API de Google Gemini (obtenerla en [Google AI Studio](https://aistudio.google.com/apikey))

---

## 🔧 Instalación y Configuración

### Paso 1: Crear el Entorno Virtual

El entorno virtual aísla las dependencias del proyecto. Sigue los pasos según tu sistema operativo:

#### Windows (CMD)

```powershell
# Abrir CMD en la carpeta del proyecto
python -m venv env
```

#### macOS / Linux

```bash
# Abrir Terminal en la carpeta del proyecto
python3 -m venv env
```

---

### Paso 2: Activar el Entorno Virtual

Después de crear el entorno, debes activarlo:

#### Windows (CMD)

```powershell
.\env\Scripts\Activate.ps1
```

**Nota:** Si obtienes un error de permisos, ejecuta:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Indicador de activación:** Verás `(env)` al inicio de tu línea de terminal.

---

### Paso 3: Verificar la Configuración del Entorno

Ejecuta el script de validación para asegurarte de que todo está correctamente configurado:

```bash
python prueba_entorno.py
```

#### Salida esperada:

```
--- Verificación de Entorno Virtual ---
✅ Estado: Entorno Virtual ACTIVO.
📍 Ruta de Python: C:\Users\Windows\Documentos\gemini-api\env\Scripts\python.exe
🌐 Conexión a internet: OK (Google es alcanzable).
```

---

### Paso 4: Instalar las Dependencias

Con el entorno virtual activado, instala todos los paquetes requeridos:

```bash
pip install -r requirements.txt
```

#### Dependencias incluidas:

- **google-genai** - Cliente oficial de Google Gemini API
- **python-dotenv** - Manejo seguro de variables de entorno
- **requests** - Librería HTTP
- **pydantic** - Validación de datos
- Y otras dependencias de soporte

#### Verificar instalación:

```bash
pip list
```

---

### Paso 5: Configurar la Clave API

Crea un archivo `.env` en la raíz del proyecto:

**Contenido del archivo `.env`:**

```
GEMINI_API_KEY=tu_clave_api_aqui
```

**⚠️ IMPORTANTE:** Reemplaza `tu_clave_api_aqui` con tu clave real de Google Gemini.

**Seguridad:** El archivo `.env` está incluido en `.gitignore` para proteger tus credenciales.

---

## 🚀 Ejecutar la Aplicación

Con todo configurado, ejecuta la aplicación principal:

```bash
python app_gemini.py
```

---

## 📊 Evidencia de Ejecución

### Salida esperada en terminal:


```bash
🚀 Conectando con el motor de Gemini ...

GEMINI_API_KEY=tu_clave_api_aqui

```
<img width="1836" height="921" alt="evidence" src="https://github.com/user-attachments/assets/3946a7a5-26c2-425d-9476-bec0f6567190" />

---

## 📁 Estructura del Proyecto

```
gemini-api/
├── README.md                 # Este archivo
├── app_gemini.py            # Script principal de la aplicación
├── prueba_entorno.py        # Script de validación del entorno
├── requirements.txt         # Dependencias del proyecto
├── .env                     # Variables de entorno
├── .gitignore              # Archivos a ignorar en Git
└── env/                    # Entorno virtual
    ├── Scripts/            # (Windows) Ejecutables del env
    └── bin/               # (macOS/Linux) Ejecutables del env
```

---

## 📝 Flujo Completo de Uso

1. **Clonar o descargar** el proyecto
2. **Crear el entorno virtual** (`python -m venv env`)
3. **Activar el entorno** (`.\env\Scripts\Activate.ps1` en Windows o `source env/bin/activate` en macOS)
4. **Validar configuración** (`python prueba_entorno.py`)
5. **Instalar dependencias** (`pip install -r requirements.txt`)
6. **Configurar `.env`** con tu clave API
7. **Ejecutar la aplicación** (`python app_gemini.py`)

---

## 👨‍💻 Desarrollado por

**Semestre VIII - DESARROLLO DE APLICACIONES CON IA**  
Fundación Universitaria Konrad Lorenz - Daniel Torres

---

## 📄 Licencia

Este proyecto es de uso educativo.

---

**Última actualización:** Febrero 3, 2026
