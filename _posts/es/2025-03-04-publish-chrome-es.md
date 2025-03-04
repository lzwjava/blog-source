---
audio: false
generated: true
lang: es
layout: post
title: Publicar una extensión de Chrome
translated: true
---

Publicar una extensión de Chrome en la Chrome Web Store es un proceso sencillo si sigues los pasos necesarios con cuidado. A continuación se presenta una guía completa paso a paso para ayudarte a poner tu extensión en línea en la Chrome Web Store.

---

### Paso 1: Preparar tu extensión de Chrome
Antes de comenzar el proceso de publicación, asegúrate de que tu extensión esté lista para el público:

- **Probar a fondo**: Prueba tu extensión en diferentes versiones de Chrome para confirmar que funciona como se espera. Utiliza la función "Cargar sin empaquetar" de Chrome (encontrada en `chrome://extensions/`) para probarla localmente.
- **Limpiar el código**: Elimina cualquier código de depuración, declaraciones `console.log` o comentarios innecesarios que puedan exponer información sensible o afectar el rendimiento.
- **Verificar el rendimiento**: Asegúrate de que tu extensión no ralentice el navegador ni utilice recursos excesivos.
- **Verificar `manifest.json`**: Este archivo es el núcleo de tu extensión. Asegúrate de que incluya:
  - Un `nombre` descriptivo.
  - Un número de `versión` (por ejemplo, "1.0.0" para tu primer lanzamiento).
  - `Permisos` requeridos (por ejemplo, "activeTab", "storage"), manteniéndolos mínimos y justificados.
  - Un campo `icons` que apunte a tu archivo de icono (por ejemplo, un `icon.png` de 128x128 píxeles).
  - Todos los demás campos necesarios como `background`, `content_scripts` o `action` dependiendo de la funcionalidad de tu extensión.

---

### Paso 2: Empaquetar tu extensión
Para subir tu extensión a la Chrome Web Store, necesitas empaquetarla correctamente:

- **Recopilar archivos**: Asegúrate de que tu directorio de extensión contenga todos los archivos necesarios:
  - `manifest.json`
  - Archivos HTML, CSS, JavaScript
  - Imágenes (incluyendo tu icono)
- **Crear un archivo ZIP**: Comprime todo el directorio de la extensión en un archivo `.zip`. No subas un archivo `.crx`, ya que la Chrome Web Store ahora acepta archivos `.zip` directamente.

---

### Paso 3: Configurar una cuenta de desarrollador
Necesitas una cuenta de desarrollador de la Chrome Web Store para publicar tu extensión:

- **Iniciar sesión**: Ve al [Panel de control del desarrollador de Chrome](https://chrome.google.com/webstore/devconsole) e inicia sesión con tu cuenta de Google.
- **Pagar la tarifa**: Si no te has registrado antes, paga una tarifa de registro de desarrollador de $5. Esta es una tarifa única, no por extensión.

---

### Paso 4: Preparar los activos de la lista de la tienda
La lista de tu extensión en la tienda requiere activos específicos e información para atraer a los usuarios:

- **Icono**: Un icono de 128x128 píxeles (por ejemplo, `icon.png`) especificado en tu `manifest.json`. Este aparece en la barra de herramientas de Chrome y en la lista de la tienda.
- **Capturas de pantalla**: Al menos una captura de pantalla mostrando tu extensión en acción. Los tamaños recomendados son 1280x800 o 640x400 píxeles. Cuantas más capturas de pantalla, mejor para mostrar la funcionalidad.
- **Imágenes promocionales opcionales**: Una imagen de marquesina (1400x560 píxeles) puede mejorar tu lista, aunque no es obligatoria.
- **Descripción**:
  - **Descripción corta**: Un resumen conciso (por ejemplo, "Una herramienta sencilla para [el propósito de tu extensión]").
  - **Descripción detallada**: Una explicación más larga de qué hace tu extensión, sus características clave y por qué los usuarios deberían instalarla. Evita errores de ortografía o gramática.
- **Política de privacidad** (si aplica): Si tu extensión recopila datos personales o sensibles del usuario, crea una política de privacidad y alójala en línea (por ejemplo, en un sitio web personal o en una página de GitHub). Enlázala en tu lista. Si no recopila datos, una declaración sencilla como "Esta extensión no recopila ni transmite datos personales del usuario" puede generar confianza.

---

### Paso 5: Subir tu extensión
Ahora estás listo para enviar tu extensión:

1. **Acceder al panel de control**: Inicia sesión en el [Panel de control del desarrollador de Chrome](https://chrome.google.com/webstore/devconsole).
2. **Agregar nuevo elemento**: Haz clic en "Agregar nuevo elemento" o un botón similar para comenzar el proceso de carga.
3. **Subir el ZIP**: Selecciona y sube tu archivo `.zip`.
4. **Rellenar la lista**:
   - Introduce tus descripciones corta y detallada.
   - Sube tu icono, capturas de pantalla e imágenes promocionales opcionales.
   - Selecciona las **categorías** adecuadas (por ejemplo, "Productividad") y añade **etiquetas** (por ejemplo, "gestión del tiempo") para mejorar la descubribilidad.
   - Enlaza tu política de privacidad (si aplica).
   - Establece la **visibilidad**: Elige publicar inmediatamente después de la aprobación o programar una fecha posterior. Para tu primer lanzamiento, "publicar después de la aprobación" es típico.
5. **Precios**: Decide si tu extensión es gratuita (recomendado para un primer lanzamiento) o de pago. La mayoría de las extensiones de Chrome son gratuitas, con monetización posible más tarde a través de compras dentro de la aplicación o suscripciones (aunque esto requiere una configuración adicional).

---

### Paso 6: Enviar para revisión
- **Enviar**: Una vez que todos los campos estén completos, envía tu extensión para su revisión.
- **Proceso de revisión**: El equipo de la Chrome Web Store revisará tu extensión para verificar su cumplimiento con sus [Políticas del programa](https://developer.chrome.com/docs/webstore/program-policies/). Esto generalmente toma unas pocas horas a unos pocos días.
- **Cumplimiento de políticas**:
  - Asegúrate de que tu extensión tenga un solo propósito claro.
  - Justifica todos los permisos en tu descripción (por ejemplo, por qué se necesita "activeTab" o "storage").
  - Evita comportamientos prohibidos como malware, recolección excesiva de datos o afirmaciones engañosas.

---

### Paso 7: Después de la aprobación
- **Ir en vivo**: Una vez aprobada, tu extensión estará disponible en la Chrome Web Store para que los usuarios la instalen.
- **Monitorear comentarios**: Revisa las reseñas y calificaciones de los usuarios en el Panel de control del desarrollador para abordar problemas o sugerencias.
- **Actualizaciones**: Para futuras actualizaciones, incrementa la `versión` en `manifest.json`, crea un nuevo `.zip` y súbelo a través del Panel de control. Volverá a pasar por la revisión antes de actualizarse para los usuarios.

---

### Consejos adicionales
- **Elige un nombre único**: Busca en la Chrome Web Store para asegurarte de que el nombre de tu extensión no esté ya tomado. Hazlo descriptivo y atractivo.
- **Empieza sencillo**: Para tu primer lanzamiento, manténlo gratuito e inglés. Puedes añadir características de pago o traducciones más tarde.
- **Promociona**: Comparte tu extensión en redes sociales u otras plataformas para aumentar la visibilidad (opcional).

---

Siguiendo estos pasos—preparar tu extensión, empaquetarla, configurar una cuenta de desarrollador, crear una lista de tienda atractiva y enviarla para su revisión—publicarás con éxito tu extensión de Chrome en la Chrome Web Store. ¡Buena suerte con tu lanzamiento!