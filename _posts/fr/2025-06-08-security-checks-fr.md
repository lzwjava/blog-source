---
audio: false
generated: true
lang: fr
layout: post
title: 'Gemini contre Grok : Vérifications de sécurité'
translated: true
type: note
---

* **Gemini (gemini.google.com) :** En général, Gemini de Google ne présente pas de "vérification humaine Cloudflare" (comme un CAPTCHA ou une page "Vérification que vous êtes un humain") lorsque vous y accédez directement via `gemini.google.com`. Google dispose de ses propres mécanismes internes pour la détection des bots et la vérification des utilisateurs.

* **Grok (grok.com) :** Oui, Grok utilise souvent les mesures de sécurité de Cloudflare, y compris leurs vérifications "Vérifiez que vous êtes un humain". De nombreux utilisateurs ont signalé avoir rencontré le système Turnstile de Cloudflare (leur alternative au CAPTCHA) en essayant d'accéder à `grok.com`. C'est une méthode courante pour les sites web de se protéger contre les bots et les abus.