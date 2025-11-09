---
audio: false
generated: true
image: false
lang: es
layout: post
model: openai/gpt-5
title: Guía de Token de Acceso Personal de GitHub
translated: true
type: note
---

Un **Personal Access Token (PAT)** de GitHub es como una contraseña que generas tú mismo para acceder de forma segura a las APIs y recursos de GitHub. Se usa ampliamente porque es más flexible y seguro que escribir tu contraseña de GitHub en todas partes.

Aquí te explicamos cómo usarlo de forma **inteligente** y cuáles son sus **funciones principales**:

---

## Funciones principales de un PAT

1. **Autenticación para Comandos Git**
   En lugar de introducir tu nombre de usuario y contraseña de GitHub al hacer push/pull, usas un PAT. Esto es especialmente importante desde que GitHub deshabilitó la autenticación por contraseña para Git sobre HTTPS.

2. **Acceso a la API**
   Si escribes scripts, herramientas o pipelines de CI/CD que llaman a la API de GitHub, un PAT te permite autenticarte de forma segura y hacer peticiones (como crear issues, obtener repos o gestionar workflows).

3. **Control de Acceso con Scopes**
   Tú decides exactamente lo que el token puede hacer (por ejemplo, acceso de solo lectura a los repos, o acceso de escritura para subir código). Esto ayuda a minimizar el daño si el token se filtra.

4. **Automatización e Integraciones**
   Herramientas como GitHub Actions, Jenkins o scripts locales pueden usar PATs para obtener dependencias, publicar paquetes o actualizar repos.

5. **Alternativa a SSH**
   Algunas personas prefieren usar PATs en lugar de configurar claves SSH—es más simple de compartir entre scripts o entornos.

---

## Cómo usar un PAT de forma inteligente

* **Limita los Scopes**: Solo concédele los permisos que realmente necesitas. Por ejemplo, si solo necesitas hacer pull de repos privados, no le des acceso de escritura.
* **Establece una Caducidad**: Usa tokens de corta duración (por ejemplo, 30 o 90 días) para la mayoría de tareas. Renuévalos en lugar de mantener uno para siempre.
* **Almacénalo de Forma Segura**: No incluyas tu PAT directamente en los scripts ni lo subas a GitHub. Usa variables de entorno, archivos `.gitignore` o gestores de secretos (por ejemplo, GitHub Actions Secrets, 1Password, AWS Secrets Manager).
* **Rota los Tokens Regularmente**: Revoca los tokens antiguos que ya no uses. Esto mantiene una buena higiene de seguridad.
* **Usa Tokens de Granularidad Fina (Más Nuevos)**: GitHub ahora recomienda PATs de granularidad fina donde puedes controlar el acceso repositorio por repositorio en lugar de un acceso global amplio.
* **Prefiere SSH para el Trabajo Diario**: Los PATs son mejores para la automatización y el uso de la API. Para programar en tu propio portátil, las claves SSH suelen ser más seguras y fáciles a largo plazo.

---

👉 Un buen modelo mental:

* **PAT = contraseña que puedes personalizar y revocar en cualquier momento.**
* **Clave SSH = credencial para tu propia estación de trabajo.**
* Usa **PATs para scripts, CI o integraciones**, y **claves SSH para tu desarrollo local diario**.

---

¿Quieres que también te muestre un **ejemplo paso a paso** de cómo configurar un PAT para `git push` con HTTPS, o estás más interesado en cómo usarlo en **automatización (por ejemplo, GitHub Actions, scripts)**?