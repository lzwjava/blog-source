---
audio: false
generated: false
image: false
lang: es
layout: post
title: 'Herramienta de Código Abierto: Auto SS Config'
translated: true
---

Estoy emocionado de anunciar que he liberado el código de una herramienta llamada **Auto SS Config**. Esta herramienta genera y sube automáticamente URLs de suscripción de Shadowsocks o Clash a partir de URLs de Shadowsocks, facilitando la gestión y actualización de las configuraciones de tu servidor proxy.

Esta herramienta ha sido un cambio radical para mí, especialmente cuando mi servidor de Shadowsocks es bloqueado. Utilizo Outline Manager para crear un nuevo servidor, obtener una dirección fresca e importar esta URL directamente usando la aplicación de Mac para sortear las restricciones del Gran Cortafuegos (GFW). Ejecutar `python upload_configs.py` desde este proyecto actualiza mis URLs de suscripción, asegurando que todos mis dispositivos digitales mantengan conexiones de red funcionales.

## Características

- **Convierte URLs de Shadowsocks a configuración de Clash**: Cambia fácilmente entre diferentes configuraciones de proxy.
- **Admite múltiples servidores Shadowsocks**: Gestiona varios servidores con facilidad.
- **Sube automáticamente las configuraciones a Google Cloud Storage**: Mantén tus configuraciones seguras y accesibles.
- **Hace que las configuraciones sean accesibles públicamente**: Comparte tus configuraciones con otros.
- **Utiliza control de caché para actualizaciones inmediatas**: Asegura que tus configuraciones estén siempre actualizadas.

## Archivos

- `app_config_tmp.yaml`: Configuración de la aplicación (nombre del bucket, URLs de SS).
- `clash_config_tmp.yaml`: Archivo de configuración temporal de Clash.
- `upload_configs.py`: Script para generar la configuración de Clash y subir las configuraciones a Google Cloud Storage.
- `requirements.txt`: Dependencias de Python.

## Configuración

1. **Instalar dependencias**:
    ```bash
    pip install -r requirements.txt
    ```

2. **Configurar las credenciales de Google Cloud**:
    - Instala Google Cloud SDK.
    - Ejecuta `gcloud auth application-default login`.
    - O establece la variable de entorno `GOOGLE_APPLICATION_CREDENTIALS`.

3. **Copia `app_config_tmp.yaml` a `app_config.yaml` y configura**:
    ```yaml
    bucket_name: tu-nombre-de-bucket
    ss_urls:
        - ss://método:contraseña@servidor:puerto
    ```

## Uso

1. **Agrega tus URLs de Shadowsocks a la lista `ss_urls` en `app_config.yaml`**:
    ```yaml
    ss_urls:
        - ss://method:password@server:port
    ```

2. **Subir configuraciones**:
    ```bash
    python upload_configs.py
    ```

    El script generará las URLs públicas para ambas configuraciones.

## Desarrollo

- **Python 3.6+**
- Utiliza `ruamel.yaml` para el manejo de YAML.
- Utiliza `google-cloud-storage` para operaciones con GCS.

## Licencia

El Instituto Tecnológico de Massachusetts (MIT, por sus siglas en inglés) es una de las universidades más prestigiosas del mundo, conocida por su enfoque en la investigación, la innovación y la excelencia académica en campos como la ingeniería, las ciencias y la tecnología. Fundado en 1861, el MIT ha sido cuna de numerosos avances científicos y tecnológicos, así como de líderes en diversos sectores. Su lema, "Mens et Manus" (Mente y Mano), refleja su compromiso con la aplicación práctica del conocimiento.

---

¡No dudes en revisar el [repositorio](https://github.com/lzwjava/auto-ss-config) para más detalles y contribuir!