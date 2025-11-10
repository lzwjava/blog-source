---
audio: false
generated: true
lang: es
layout: post
title: Instalación de Selenium GeckoDriver en Ubuntu
translated: true
type: note
---

Para instalar el controlador de Firefox para Selenium (geckodriver) en Ubuntu, sigue estos pasos:

1. **Instalar Firefox** (si aún no está instalado):
   ```bash
   sudo apt update
   sudo apt install firefox
   ```

2. **Descargar geckodriver**:
   - Visita la [página de lanzamientos de geckodriver](https://github.com/mozilla/geckodriver/releases).
   - Elige la última versión compatible con tu versión de Firefox. Para Ubuntu, descarga la versión Linux de 64 bits (por ejemplo, `geckodriver-vX.XX.X-linux64.tar.gz`).
   - Comando de ejemplo para descargar (reemplaza `X.XX.X` con la última versión):
     ```bash
     wget https://github.com/mozilla/geckodriver/releases/download/vX.XX.X/geckodriver-vX.XX.X-linux64.tar.gz
     ```

3. **Extraer el archivo descargado**:
   ```bash
   tar -xvzf geckodriver-vX.XX.X-linux64.tar.gz
   ```

4. **Mover geckodriver a una ruta del sistema**:
   - Mueve el archivo `geckodriver` extraído a `/usr/local/bin` para que sea accesible en todo el sistema:
     ```bash
     sudo mv geckodriver /usr/local/bin/
     ```
   - Hazlo ejecutable:
     ```bash
     sudo chmod +x /usr/local/bin/geckodriver
     ```

5. **Instalar Selenium para Python** (si usas Python):
   ```bash
   pip install selenium
   ```

6. **Verificar la instalación**:
   - Comprueba la versión de geckodriver:
     ```bash
     geckodriver --version
     ```
   - Prueba con un script simple de Python:
     ```python
     from selenium import webdriver

     driver = webdriver.Firefox()
     driver.get("https://www.example.com")
     print(driver.title)
     driver.quit()
     ```

**Notas**:
- Asegúrate de que tu versión de Firefox sea compatible con la versión de geckodriver (consulta las notas de la versión en la página de GitHub de geckodriver).
- Si encuentras problemas, asegúrate de que `python3-pip` esté instalado:
  ```bash
  sudo apt install python3-pip
  ```
- Si no se encuentra geckodriver, añade `/usr/local/bin` a tu variable `PATH`:
  ```bash
  export PATH=$PATH:/usr/local/bin
  ```

Esto debería configurar el controlador de Firefox para Selenium en Ubuntu. ¡Avísame si tienes algún problema!

---

La diferencia entre `geckodriver-v0.36.0-linux-aarch64.tar.gz` y `geckodriver-v0.36.0-linux64.tar.gz` radica en la arquitectura de CPU objetivo:

- **linux-aarch64**: Este es para arquitecturas ARM de 64 bits (por ejemplo, ARMv8-A), comúnmente utilizadas en dispositivos como Raspberry Pi, algunos servidores o sistemas Linux modernos basados en ARM. "aarch64" significa arquitectura ARM de 64 bits.

- **linux64**: Este es para arquitecturas x86 de 64 bits (también conocidas como x86_64 o AMD64), que son estándar para la mayoría de las PC de escritorio y servidores que ejecutan Linux.

**Puntos clave**:
- Elige `linux-aarch64` si tu sistema tiene un procesador ARM de 64 bits.
- Elige `linux64` si tu sistema tiene un procesador x86 de 64 bits.
- Puedes verificar la arquitectura de tu sistema en Linux ejecutando `uname -m`. Si muestra `aarch64`, usa la versión ARM; si muestra `x86_64`, usa la versión linux64.

Los archivos `.asc` son firmas GPG para verificar la integridad y autenticidad de los archivos `.tar.gz` correspondientes.