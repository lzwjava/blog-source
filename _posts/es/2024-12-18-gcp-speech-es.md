---
audio: false
generated: false
image: false
lang: es
layout: post
title: Introducción a la API de Texto a Voz de Google
translated: true
type: post
---

Planeo convertir algunos de los artículos de Yin Wang en audio utilizando la API de Google Text-to-Speech. A continuación, te dejo una guía paso a paso, junto con algunos tutoriales útiles proporcionados por ChatGPT. Una vez que todo esté listo, subiré el audio aquí para que puedas escucharlo.

---

### Paso 1: Configurar una cuenta de Google Cloud

1. Crea una cuenta en Google Cloud  
   Si no tienes una, regístrate en la [Consola de Google Cloud](https://console.cloud.google.com/).

2. Crear un Nuevo Proyecto  
   - En la Consola de Cloud, haz clic en el menú desplegable de proyectos (en la parte superior izquierda).  
   - Selecciona "Nuevo Proyecto", asígnale un nombre y crea el proyecto.

3. Habilitar la API de Text-to-Speech  
   - Visita la [página de la API de Text-to-Speech de Google Cloud](https://cloud.google.com/text-to-speech).  
   - Haz clic en "Habilitar" para activar la API en tu proyecto.

4. Crear Credenciales de API  
   - Navega a APIs y Servicios > Credenciales en la Consola de Cloud.
   - Haz clic en Crear Credenciales, luego selecciona Cuenta de Servicio.
   - Sigue las indicaciones para crear la cuenta de servicio y descarga el archivo de clave privada en formato JSON.  
   - Mantén este archivo JSON seguro, ya que se utiliza para autenticar tus solicitudes de API.

---

### Paso 2: Instalar Google Cloud SDK y la Biblioteca del Cliente

1. Instala Google Cloud SDK  
   Si aún no lo has hecho, sigue las instrucciones para instalar el [Google Cloud SDK](https://cloud.google.com/sdk/docs/install) en tu sistema operativo.

2. Instala la Biblioteca de Cliente de Python  
   Si estás usando Python, instala la biblioteca `google-cloud-texttospeech` con:

```bash
pip install google-cloud-texttospeech
```

---

### Paso 3: Configurar la Autenticación

Antes de usar la API, necesitas autenticarte con tus credenciales. Configura la variable de entorno con la ruta de tu archivo de credenciales:

```bash
export GOOGLE_APPLICATION_CREDENTIALS="/ruta/a/tu/archivo-de-cuenta-de-servicio.json"
```

Reemplaza la ruta con la ubicación real de tu archivo JSON descargado.

---

### Paso 4: Implementar la Conversión de Texto a Voz

Aquí tienes un ejemplo en Python para convertir texto en voz utilizando la API de Google Cloud Text-to-Speech:

```python
from google.cloud import texttospeech
```

```python
def text_to_speech(text, output_filename):
    # Inicializa el cliente de Text-to-Speech
    client = texttospeech.TextToSpeechClient()
```

    # Configurar la entrada de síntesis
    synthesis_input = texttospeech.SynthesisInput(text=text)

    # Configurar parámetros de voz (usando 'en-US-Journey-D')
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",  # Inglés (Estados Unidos)
        name="en-US-Journey-D"  # Modelo de voz específico (Journey)
    )

    # Configurar la configuración de audio
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,  # Formato MP3
        effects_profile_id=["small-bluetooth-speaker-class-device"],  # Optimizado para altavoces Bluetooth
        pitch=0.0,  # Sin modificación de tono
        speaking_rate=0.9,  # Velocidad de habla ajustada (se puede modificar según sea necesario)
        volume_gain_db=5.0  # Volumen más alto
    )

    # Realizar la solicitud de texto a voz
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # Escribir el contenido de audio en un archivo
    with open(output_filename, "wb") as out:
        out.write(response.audio_content)

    print(f"Contenido de audio escrito en {output_filename}")

# Ejemplo de uso
article_text = "Películas, oh Dios mío, simplemente las amo. Son como máquinas del tiempo que te llevan a diferentes mundos y paisajes, y no puedo tener suficiente de eso."
output_file = "output_audio.mp3"  # Salida en formato MP3

# Convertir texto a voz
text_to_speech(article_text, output_file)
```

---

### Paso 5: Ejecutar el Script

1. Guarda el script como `text_to_speech.py`.
2. Ejecuta el script con:

```bash
   python text_to_speech.py
   ```

Esto generará un archivo de audio (`output_audio.mp3`) a partir del texto proporcionado.

---

### Paso 6: Clave de la Cuenta de Servicio

La clave JSON de tu cuenta de servicio debería verse similar a esto:

```json
{
  "type": "service_account",
  "project_id": "tu-id-de-proyecto",
  "private_key_id": "tu-id-de-clave-privada",
  "private_key": "tu-clave-privada",
  "client_email": "tu-correo-de-cuenta-de-servicio@tu-id-de-proyecto.iam.gserviceaccount.com",
  "client_id": "tu-id-de-cliente",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "tu-url-de-certificado-de-cliente"
}
```

---

### ¿Por qué elegir Journey?

Google Cloud Text-to-Speech ofrece varias voces, pero Journey destaca por su sonido natural y similar al humano. A diferencia de otros modelos que suelen sonar robóticos, Journey sobresale en expresividad y una entrega realista. Es especialmente adecuado para contenido de larga duración, como podcasts, audiolibros o cualquier aplicación que requiera un tono más conversacional.

Características clave de Journey:
- Habla natural: Suena más cercano a una voz humana.
- Expresividad: Ajusta el tono y la inflexión según el contexto.
- Ideal para contenido de larga duración: Perfecto para podcasts y narraciones.

Para obtener más detalles sobre los beneficios de Google Cloud Text-to-Speech, consulta la [descripción general de Google Cloud](https://cloud.google.com/text-to-speech#benefits).

---

### Paso 7: Generar una nueva clave de cuenta de servicio (si es necesario)

Si la clave de tu cuenta de servicio no coincide con el ejemplo anterior, puedes generar una nueva desde la Consola de Google Cloud.

Para generar una nueva clave:
1. Ve a la [Consola de Google Cloud](https://console.cloud.google.com/).
2. Navega a IAM y Administración > Cuentas de servicio.
3. Crea una nueva cuenta de servicio:
   - Haz clic en Crear cuenta de servicio y asigna los roles apropiados.
   - Haz clic en Crear.
4. Genera una clave:
   - Después de crear la cuenta de servicio, haz clic en ella.
   - Ve a la pestaña Claves, haz clic en Agregar clave y elige JSON. Luego descarga la clave.

---

### Ejemplo de Salida de Audio

Una vez que todo esté configurado, puedes generar un archivo de audio, que estará disponible aquí:  
[Descargar el archivo de audio](assets/audios/output-audio.mp3).

---

### Conclusión

La API de Google Cloud Text-to-Speech facilita la conversión de texto en voz con sonido natural. Ya sea que estés desarrollando una aplicación que requiera salida de voz o simplemente experimentando con la conversión de texto a voz, esta API ofrece funciones potentes y opciones de personalización. Explora la documentación completa para acceder a más selecciones de voces, idiomas y funciones avanzadas.