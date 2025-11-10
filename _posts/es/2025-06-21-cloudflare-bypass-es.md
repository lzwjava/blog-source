---
audio: false
generated: true
lang: es
layout: post
title: Script de Selenium para Omitir Cloudflare
translated: true
type: note
---

Tu script de Selenium está diseñado para interactuar con "https://grok.com" usando Firefox y un perfil específico, pero se está encontrando con un desafío de detección de bots de Cloudflare, específicamente la casilla de verificación "Verify you are human". Incluso después de hacer clic en la casilla de verificación, el script parece tener problemas para omitir la verificación, lo que impide el acceso al contenido principal (por ejemplo, el área de texto `textarea`). Cloudflare emplea métodos sofisticados para detectar navegadores automatizados, como análisis de cabeceras HTTP, fingerprinting TLS y comprobaciones de comportamiento, lo que puede hacer que omitir este desafío sea complicado usando solo Selenium. Sin embargo, hay estrategias que puedes probar para pasar la prueba de Cloudflare manteniéndote dentro de tu configuración actual basada en Firefox. A continuación, se presentan dos enfoques prácticos adaptados a tu script, seguidos de consideraciones adicionales si estos no son suficientes.

---

### **Método 1: Completar el Desafío Manualmente con Reutilización del Perfil**
Dado que tu script utiliza un perfil específico de Firefox (`/home/lzw/.mozilla/firefox/wzfodx6v.default`), puedes aprovechar esto para almacenar datos de la sesión después de pasar manualmente el desafío de Cloudflare. Así es cómo hacerlo:

1. **Abrir Firefox Manualmente con el Perfil**:
   - Inicia Firefox usando el mismo perfil especificado en tu script. Puedes hacerlo mediante la línea de comandos:
     ```bash
     firefox --profile "/home/lzw/.mozilla/firefox/wzfodx6v.default"
     ```
   - Alternativamente, usa el administrador de perfiles de Firefox (`firefox --ProfileManager`) para seleccionar `wzfodx6v.default`.

2. **Navegar y Pasar el Desafío**:
   - Ve a "https://grok.com" en el navegador.
   - Cuando aparezca la casilla de verificación "Verify you are human" de Cloudflare, haz clic en ella y completa cualquier paso de verificación adicional si aparece.
   - Espera hasta que llegues a la página principal (por ejemplo, donde el `textarea` con `aria-label="Ask Grok anything"` es visible).

3. **Cerrar el Navegador**:
   - Cierra Firefox para asegurarte de que el perfil guarda las cookies de la sesión, incluyendo cualquier token de autorización de Cloudflare (como `cf_clearance`).

4. **Ejecutar Tu Script de Selenium**:
   - Ejecuta tu script tal cual. Dado que utiliza el mismo perfil, debería heredar las cookies y los datos de la sesión almacenados, lo que potencialmente le permitiría omitir el desafío.

**Por Qué Esto Podría Funcionar**: Cloudflare a menudo depende de cookies para recordar que un navegador ha pasado su prueba. Al preautenticar el perfil manualmente, tu sesión automatizada puede aparecer como una continuación de una visita verificada.

**Limitaciones**: Si Cloudflare realiza comprobaciones adicionales en cada carga de página (por ejemplo, detectando los fingerprints de automatización de Selenium), este método podría fallar. En ese caso, prueba el siguiente enfoque.

---

### **Método 2: Extraer y Establecer Cookies en el Script**
Si reutilizar el perfil no funciona, puedes extraer manualmente las cookies después de pasar el desafío e inyectarlas en tu controlador de Selenium. Este es el proceso paso a paso:

1. **Pasar el Desafío Manualmente**:
   - Sigue los pasos 1 y 2 del Método 1 para llegar a la página principal de "https://grok.com".

2. **Extraer las Cookies**:
   - Abre las Developer Tools de Firefox (F12 o clic derecho > Inspeccionar).
   - Ve a la pestaña **Storage** (o pestaña **Network**, luego recarga la página para inspeccionar las cookies).
   - Busca las cookies asociadas con `.grok.com`, especialmente `cf_clearance` (la cookie de verificación de Cloudflare).
   - Anota el `name`, `value` y `domain` de cada cookie relevante. Por ejemplo:
     - Nombre: `cf_clearance`, Valor: `abc123...`, Dominio: `.grok.com`
     - También podrían estar presentes otras cookies como `__cfduid` o las específicas de la sesión.

3. **Modificar Tu Script**:
   - Añade las cookies a tu controlador de Selenium antes de navegar a la URL. Actualiza tu código así:
     ```python
     # ... (las importaciones y configuración existentes permanecen sin cambios)

     # Configurar el servicio de geckodriver
     service = Service(executable_path="/home/lzw/bin/geckodriver")
     driver = webdriver.Firefox(service=service, options=firefox_options)

     # Abre una página en blanco primero para establecer cookies (las cookies solo se pueden establecer después de cargar una página)
     driver.get("about:blank")

     # Añade las cookies que extrajiste
     cookies = [
         {"name": "cf_clearance", "value": "abc123...", "domain": ".grok.com"},
         # Añade otras cookies según sea necesario, por ejemplo:
         # {"name": "__cfduid", "value": "xyz789...", "domain": ".grok.com"},
     ]
     for cookie in cookies:
         driver.add_cookie(cookie)

     # Ahora navega a la URL objetivo
     driver.get("https://grok.com")

     # Imprime el título de la página
     print("Title of the page:", driver.title)

     # ... (el resto de tu script permanece igual)
     ```

4. **Probar el Script**:
   - Ejecuta el script modificado. Las cookies preestablecidas deberían indicar a Cloudflare que el navegador ya ha pasado el desafío.

**Por Qué Esto Podría Funcionar**: Establecer explícitamente la cookie `cf_clearance` imita una sesión verificada, lo que potencialmente omite la necesidad de interactuar con la casilla de verificación.

**Limitaciones**: Las cookies podrían estar vinculadas a fingerprints del navegador (por ejemplo, agente de usuario, IP o configuraciones TLS). Si el fingerprint de Selenium difiere de la sesión manual, Cloudflare podría rechazar las cookies o volver a desafiar al navegador.

---

### **Depuración y Mejoras Adicionales**
Si ningún método resuelve completamente el problema, considera estos ajustes en tu script para asegurarte de que está interactuando correctamente con el desafío de Cloudflare:

- **Comprobar Iframes**: La casilla de verificación "Verify you are human" podría estar dentro de un iframe. Modifica tu código de clic en la casilla para cambiar primero al iframe:
  ```python
  try:
      wait = WebDriverWait(driver, 20)
      iframe = wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[contains(@src, 'cloudflare')]")))
      driver.switch_to.frame(iframe)
      label = wait.until(EC.presence_of_element_located((By.XPATH, "//label[@class='cb-lb']")))
      checkbox = label.find_element(By.TAG_NAME, "input")
      print("Checkbox found:", checkbox.is_displayed())
      checkbox.click()
      driver.switch_to.default_content()  # Volver al contenido principal
      print("Checkbox clicked.")
  except Exception as e:
      print("Checkbox not found or not clickable:", e)
  ```

- **Mejorar la Lógica de Espera**: Después de hacer clic en la casilla de verificación, espera una señal clara de que el desafío ha sido superado (por ejemplo, que desaparezca la página de verificación):
  ```python
  try:
      wait.until(EC.invisibility_of_element_located((By.XPATH, "//*[contains(text(), 'Verify you are human')]")))
      print("Challenge passed.")
  except Exception as e:
      print("Challenge not passed:", e)
  ```

- **Enmascarar la Automatización**: Añade JavaScript para ocultar los rastros de automatización de Selenium:
  ```python
  driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
  ```

---

### **Si Todo lo Demás Falla: Enfoques Alternativos**
Si la detección de Cloudflare persiste, podría deberse a un fingerprinting avanzado que tu configuración actual no puede evadir. Aquí hay opciones de escalada, aunque se desvían de tu preferencia por Firefox:

- **Cambiar a Chrome con Undetected ChromeDriver**:
  - Instala: `pip install undetected-chromedriver`
  - Modifica la configuración:
    ```python
    import undetected_chromedriver as uc
    driver = uc.Chrome()
    driver.get("https://grok.com")
    ```
  - Esta biblioteca parchea Chrome para evitar métodos de detección comunes.

- **Usar un Proxy o un Solucionador de CAPTCHA**: Servicios como 2Captcha o proxies residenciales pueden manejar desafíos, pero añaden complejidad y costo.

---

### **Próximos Pasos Recomendados**
Comienza con el **Método 1** (reutilización del perfil) ya que es el más simple y se ajusta a la configuración de tu script. Si falla, prueba el **Método 2** (inyección de cookies) añadiendo la comprobación del iframe. Estos métodos maximizan tu configuración existente de Firefox sin requerir nuevas herramientas. Prueba cada enfoque y monitoriza la salida (por ejemplo, `driver.title` y los mensajes de excepción) para confirmar si el desafío se ha omitido. Si aún enfrentas problemas, considera los enfoques alternativos según la flexibilidad de tu proyecto.

¡Avísame si necesitas ayuda para implementar o solucionar problemas con estas soluciones!