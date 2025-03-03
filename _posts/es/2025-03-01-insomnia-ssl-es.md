---
audio: true
generated: true
lang: es
layout: post
title: Validación de Certificados SSL en Insomnia
translated: true
---

Para solucionar el error "SSL peer certificate or SSH remote key was not OK" en Insomnia, este error generalmente ocurre cuando Insomnia no puede verificar el certificado SSL del servidor al que intentas conectarte. A continuación se presentan soluciones paso a paso para resolver este problema:

### 1. **Desactivar la validación del certificado SSL (Solo para desarrollo local)**
Si estás trabajando con un servidor de desarrollo local que utiliza un certificado SSL autofirmado o inválido, puedes desactivar la validación del certificado en Insomnia:
- Abre Insomnia y ve a **Aplicación** > **Preferencias**.
- Navega a la sección **Solicitud / Respuesta**.
- Desmarca la casilla etiquetada como **Validar certificados**.
- Vuelve a intentar tu solicitud.

**Importante**: Esta opción omite las comprobaciones de seguridad y solo debe **usarse para pruebas o desarrollo local**. No la uses en entornos de producción, ya que hace que tu conexión sea vulnerable.

---

### 2. **Verificar el certificado SSL del servidor**
El error puede indicar un problema con el certificado SSL del servidor (por ejemplo, expirado, autofirmado o con discrepancia en el nombre del host). Para verificar:
- Abre la URL del servidor en un navegador web.
- Haz clic en el icono del candado en la barra de direcciones para ver los detalles del certificado.
- Asegúrate de que el certificado sea válido, no esté expirado y coincida con el nombre del dominio.
- Si el certificado es inválido o está mal configurado, contacta al administrador del servidor para que lo arregle.

---

### 3. **Importar un certificado de cliente (si es necesario)**
Si el servidor requiere un certificado de cliente para la autenticación, deberás configurarlo en Insomnia:
- En Insomnia, ve a **Certificados de cliente** (accesible desde el tablero principal o preferencias).
- Haz clic en **Agregar certificado**.
- Importa tu archivo de certificado (los formatos soportados incluyen PFX o PEM).
- Asígnalo al dominio o nombre de host específico al que te estás conectando.
- Vuelve a probar la solicitud.

---

### 4. **Actualizar Insomnia**
Los problemas relacionados con SSL pueden deberse a un error en una versión anterior de Insomnia. Para asegurarte de estar en la última versión:
- Busca actualizaciones en **Aplicación** > **Acerca de** o descarga la última versión desde el sitio web oficial de Insomnia.
- Instala la actualización y vuelve a intentar tu solicitud.

---

### 5. **Probar con Curl**
Si los pasos anteriores no resuelven el problema, prueba la solicitud fuera de Insomnia para aislar el problema:
- Abre una terminal y usa el comando `curl` con la misma URL y parámetros (por ejemplo, `curl -v https://example.com`).
- Si `curl` también falla, el problema probablemente esté en la configuración del servidor en lugar de en Insomnia.
- Si `curl` tiene éxito, puede indicar un problema específico con Insomnia, y puedes informar a su equipo de soporte.

---

### Resumen
Comienza desactivando la validación SSL si es un servidor local, luego verifica el certificado del servidor o configura un certificado de cliente si es necesario. Asegúrate de que Insomnia esté actualizado y usa `curl` para solucionar problemas adicionales si es necesario. Estos pasos deberían resolver la mayoría de los casos del error "SSL peer certificate or SSH remote key was not OK".

Si el problema persiste, puede deberse a una configuración incorrecta en el servidor o a un error raro en Insomnia. ¡Hazme saber si necesitas más asistencia!