---
audio: false
generated: true
lang: es
layout: post
title: Publicar una extensión de Chrome
translated: true
type: note
---

Publicar un plugin (extensión) de Chrome en Chrome Web Store es un proceso sencillo si sigues los pasos necesarios cuidadosamente. A continuación, una guía completa paso a paso para ayudarte a que tu extensión esté disponible en Chrome Web Store.

---

### Paso 1: Prepara tu Extensión de Chrome
Antes de comenzar el proceso de publicación, asegúrate de que tu extensión esté lista para el público:

- **Prueba a Fondo**: Prueba tu extensión en diferentes versiones de Chrome para confirmar que funciona como se espera. Usa la función "Cargar descomprimida" de Chrome (se encuentra en `chrome://extensions/`) para probarla localmente.
- **Limpia el Código**: Elimina cualquier código de depuración, declaraciones `console.log` o comentarios innecesarios que puedan exponer información sensible o afectar el rendimiento.
- **Verifica el Rendimiento**: Asegúrate de que tu extensión no ralentice el navegador o use recursos excesivos.
- **Verifica el manifest.json**: Este archivo es la columna vertebral de tu extensión. Asegúrate de que incluya:
  - Un `name` descriptivo.
  - Un número de `version` (ej. "1.0.0" para tu primera versión).
  - Los `permissions` requeridos (ej. "activeTab", "storage"), manteniéndolos mínimos y justificados.
  - Un campo `icons` que apunte a tu archivo de icono (ej. un `icon.png` de 128x128 píxeles).
  - Todos los demás campos necesarios como `background`, `content_scripts` o `action` dependiendo de la funcionalidad de tu extensión.

---

### Paso 2: Empaqueta tu Extensión
Para subir tu extensión a Chrome Web Store, necesitas empaquetarla correctamente:

- **Reúne los Archivos**: Asegúrate de que el directorio de tu extensión contenga todos los archivos requeridos:
  - `manifest.json`
  - Archivos HTML, CSS, JavaScript
  - Imágenes (incluyendo tu icono)
- **Crea un Archivo ZIP**: Comprime todo el directorio de la extensión en un archivo `.zip`. No subas un archivo `.crx`, ya que Chrome Web Store ahora acepta archivos `.zip` directamente.

---

### Paso 3: Configura una Cuenta de Desarrollador
Necesitas una cuenta de desarrollador de Chrome Web Store para publicar tu extensión:

- **Inicia Sesión**: Ve al [Chrome Developer Dashboard](https://chrome.google.com/webstore/devconsole) e inicia sesión con tu cuenta de Google.
- **Paga la Tarifa**: Si no te has registrado antes, paga la tarifa única de registro de desarrollador de $5. Este es un costo único, no por extensión.

---

### Paso 4: Prepara los Recursos para el Listado en la Tienda
El listado de tu extensión en la tienda requiere recursos e información específicos para atraer usuarios:

- **Icono**: Un icono de 128x128 píxeles (ej. `icon.png`) especificado en tu `manifest.json`. Este aparece en la barra de herramientas de Chrome y en el listado de la tienda.
- **Capturas de Pantalla**: Al menos una captura de pantalla que muestre tu extensión en acción. Los tamaños recomendados son 1280x800 o 640x400 píxeles. Múltiples capturas de pantalla son mejores para mostrar la funcionalidad.
- **Imágenes Promocionales Opcionales**: Una imagen marquesina (1400x560 píxeles) puede mejorar tu listado, aunque no es obligatoria.
- **Descripción**:
  - **Descripción Corta**: Un resumen conciso (ej. "Una herramienta simple para [el propósito de tu extensión]").
  - **Descripción Detallada**: Una explicación más larga de lo que hace tu extensión, sus características clave y por qué los usuarios deberían instalarla. Evita errores de ortografía o gramática.
- **Política de Privacidad** (si aplica): Si tu extensión recopila datos personales o sensibles del usuario, crea una política de privacidad y alójala en línea (ej. en un sitio web personal o página de GitHub). Enlázala en tu listado. Si no recopila datos, una declaración simple como "Esta extensión no recopila ni transmite datos personales del usuario" puede generar confianza.

---

### Paso 5: Sube tu Extensión
Ahora estás listo para enviar tu extensión:

1. **Accede al Dashboard**: Inicia sesión en el [Chrome Developer Dashboard](https://chrome.google.com/webstore/devconsole).
2. **Añade un Nuevo Elemento**: Haz clic en "Add new item" o un botón similar para comenzar el proceso de carga.
3. **Sube el ZIP**: Selecciona y sube tu archivo `.zip`.
4. **Completa el Listado**:
   - Ingresa tus descripciones corta y detallada.
   - Sube tu icono, capturas de pantalla e imágenes promocionales opcionales.
   - Selecciona **categorías** apropiadas (ej. "Productividad") y añade **etiquetas** (ej. "gestión del tiempo") para mejorar la visibilidad.
   - Enlaza tu política de privacidad (si aplica).
   - Establece la **visibilidad**: Elige publicar inmediatamente después de la aprobación o programa una fecha posterior. Para tu primera versión, lo típico es "publicar después de la aprobación".
5. **Precio**: Decide si tu extensión es gratuita (recomendado para una primera versión) o de pago. La mayoría de las extensiones de Chrome son gratuitas, siendo posible la monetización posteriormente mediante compras dentro de la aplicación o suscripciones (aunque esto requiere configuración adicional).

---

### Paso 6: Envía para Revisión
- **Envía**: Una vez que todos los campos estén completos, envía tu extensión para revisión.
- **Proceso de Revisión**: El equipo de Chrome Web Store verificará que tu extensión cumple con sus [Program Policies](https://developer.chrome.com/docs/webstore/program-policies/). Esto típicamente toma desde unas horas hasta unos días.
- **Cumplimiento de Políticas**:
  - Asegúrate de que tu extensión tenga un único propósito claro.
  - Justifica todos los permisos en tu descripción (ej. por qué se necesita "activeTab" o "storage").
  - Evita comportamientos prohibidos como malware, recopilación excesiva de datos o afirmaciones engañosas.

---

### Paso 7: Después de la Aprobación
- **Se Hace Pública**: Una vez aprobada, tu extensión estará disponible en Chrome Web Store para que los usuarios la instalen.
- **Monitorea los Comentarios**: Revisa las reseñas y calificaciones de los usuarios en el Developer Dashboard para abordar problemas o sugerencias.
- **Actualizaciones**: Para futuras actualizaciones, incrementa el `version` en `manifest.json`, crea un nuevo `.zip` y súbelo a través del Dashboard. Pasará por revisión nuevamente antes de actualizarse para los usuarios.

---

### Consejos Adicionales
- **Elige un Nombre Único**: Busca en Chrome Web Store para asegurarte de que el nombre de tu extensión no esté ya en uso. Hazlo descriptivo y atractivo.
- **Comienza de Forma Sencilla**: Para tu primera versión, mantenla gratuita y solo en inglés. Puedes añadir funciones de pago o traducciones más tarde.
- **Promociona**: Comparte tu extensión en redes sociales u otras plataformas para aumentar la visibilidad (opcional).

---

Siguiendo estos pasos—preparando tu extensión, empaquetándola, configurando una cuenta de desarrollador, creando un listado atractivo en la tienda y enviándola para revisión—publicarás con éxito tu plugin de Chrome en Chrome Web Store. ¡Buena suerte con tu lanzamiento!