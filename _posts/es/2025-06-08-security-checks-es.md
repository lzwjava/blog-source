---
audio: false
generated: true
lang: es
layout: post
title: 'Géminis contra Grok: Verificaciones de Seguridad'
translated: true
type: note
---

* **Gemini (gemini.google.com):** Por lo general, Gemini de Google no presenta una "verificación humana de Cloudflare" (como un CAPTCHA o una página de "Verificando que eres humano") cuando accedes directamente a través de `gemini.google.com`. Google tiene sus propios mecanismos internos para la detección de bots y la verificación de usuarios.

* **Grok (grok.com):** Sí, Grok utiliza frecuentemente las medidas de seguridad de Cloudflare, incluyendo sus verificaciones de "Verifica que eres humano". Muchos usuarios han reportado encontrarse con Turnstile de Cloudflare (su alternativa al CAPTCHA) al intentar acceder a `grok.com`. Esta es una forma común para que los sitios web se protejan contra bots y abusos.