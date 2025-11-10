---
audio: false
generated: true
lang: es
layout: post
title: Conversión de WebP a JPG en Ubuntu
translated: true
type: note
---

Tienes varias opciones excelentes para convertir WebP a JPG en Ubuntu, tanto desde la línea de comandos como con herramientas gráficas.

## Herramientas de Línea de Comandos

Estas son generalmente las más flexibles y eficientes para archivos individuales o conversiones por lotes.

### 1. ImageMagick

ImageMagick es un conjunto de herramientas de línea de comandos muy potente para la manipulación de imágenes, y está ampliamente disponible.

*   **Instalación:**
    ```bash
    sudo apt update
    sudo apt install imagemagick
    ```
*   **Convertir un solo archivo:**
    ```bash
    convert input.webp output.jpg
    ```
    O, usando `magick` para ImageMagick v7+:
    ```bash
    magick input.webp output.jpg
    ```
*   **Convertir múltiples archivos (conversión por lotes) en el directorio actual:**
    ```bash
    mogrify -format JPEG *.webp
    ```
    Esto convertirá todos los archivos `.webp` en el directorio actual a `.jpeg` (o `.jpg`) con el mismo nombre de archivo. Si quieres los archivos convertidos en un directorio separado:
    ```bash
    mkdir output_jpgs # Crear un directorio para la salida
    mogrify -format JPEG -path output_jpgs *.webp
    ```

### 2. `dwebp` (del paquete `libwebp`)

`dwebp` es una herramienta dedicada para decodificar imágenes WebP.

*   **Instalación:**
    ```bash
    sudo apt update
    sudo apt install webp
    ```
*   **Convertir un solo archivo:**
    ```bash
    dwebp input.webp -o output.jpg
    ```
    Aunque especifiques `.jpg` como salida, `dwebp` a menudo genera archivos en formato PPM y requiere otra herramienta como ImageMagick para convertirlos a un JPEG adecuado. Sin embargo, algunas fuentes sugieren que usar `.jpg` como salida funciona para casos simples. Si encuentras problemas, convierte primero a PNG y luego a JPG:
    ```bash
    dwebp input.webp -o output.png
    convert output.png output.jpg
    ```

### 3. `ffmpeg`

`ffmpeg` es principalmente para video y audio, pero también es muy capaz con formatos de imagen.

*   **Instalación:**
    ```bash
    sudo apt update
    sudo apt install ffmpeg
    ```
*   **Convertir un solo archivo:**
    ```bash
    ffmpeg -i input.webp output.jpg
    ```
*   **Convertir múltiples archivos (conversión por lotes):**
    ```bash
    for file in *.webp; do ffmpeg -i "$file" "${file%.*}.jpg"; done
    ```
    Este comando itera a través de todos los archivos `.webp` en el directorio actual y los convierte a `.jpg` con el mismo nombre (por ejemplo, `image.webp` se convierte en `image.jpg`).

## Herramientas Gráficas

Si prefieres una interfaz gráfica, aquí hay un par de opciones:

### 1. GIMP (GNU Image Manipulation Program)

GIMP es un editor de imágenes de código abierto muy potente que soporta WebP.

*   **Instalación:**
    ```bash
    sudo apt update
    sudo apt install gimp
    ```
*   **Cómo convertir:**
    1.  Abre la imagen WebP en GIMP (Archivo > Abrir).
    2.  Ve a Archivo > Exportar como.
    3.  En el cuadro de diálogo "Exportar imagen", elige "Imagen JPEG" del menú desplegable "Seleccionar tipo de archivo (Por extensión)".
    4.  Haz clic en "Exportar" y ajusta la configuración de calidad si lo deseas.

### 2. XnView MP / XnConvert

Estos son visores de imágenes y convertidores por lotes multiplataforma con soporte integral de formatos, incluyendo WebP.

*   **Instalación:**
    Es posible que necesites descargar el paquete `.deb` desde su sitio web oficial e instalarlo usando `sudo dpkg -i <nombre_del_paquete.deb>` o a través de un instalador de paquetes gráfico.
*   **Cómo convertir (generalmente):**
    1.  Abre XnView MP o XnConvert.
    2.  Añade las imágenes WebP que quieras convertir.
    3.  Elige JPG como formato de salida.
    4.  Ajusta cualquier configuración (calidad, redimensionar, etc.).
    5.  Inicia la conversión.

### 3. Converseen

Converseen es un convertidor de imágenes por lotes gratuito que soporta WebP.

*   **Instalación:** Normalmente lo puedes encontrar en el Centro de Software de Ubuntu o instalarlo vía apt si está disponible en tus repositorios.
*   **Cómo convertir:** Tiene una interfaz gráfica sencilla para añadir imágenes, seleccionar el formato de salida y convertir.

## ¿Qué método elegir?

*   **Para conversiones rápidas de un solo archivo o para automatizar tareas con scripts:** Usa `ffmpeg` o `ImageMagick` desde la línea de comandos. Son muy eficientes.
*   **Para conversiones ocasionales donde quieres una interfaz visual y más control sobre la edición de la imagen:** GIMP es una gran elección.
*   **Para convertir por lotes muchas imágenes con una interfaz gráfica y varias opciones:** XnView MP/XnConvert o Converseen son excelentes.

No importa qué método elijas, asegúrate de instalar primero los paquetes necesarios.