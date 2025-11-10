---
audio: false
generated: true
image: false
lang: es
layout: post
title: Corregir Error de Autenticación de Copilot Chat
translated: true
type: note
---

Ese error generalmente significa que **GitHub Copilot Chat** no pudo encontrar un token de autenticación válido, por lo que no puede comunicarse con el servicio de Copilot.
No es un error de código — es un problema de **autenticación/configuración**.

Aquí te mostramos cómo solucionarlo paso a paso dependiendo de dónde estés usando Copilot Chat:

---

### 1. Asegúrate de haber iniciado sesión con una cuenta habilitada para Copilot

* En **VS Code** o un IDE de **JetBrains**:

  1. Abre la Paleta de Comandos (**Ctrl+Shift+P** / **Cmd+Shift+P**).
  2. Busca **“GitHub: Sign in”**.
  3. Sigue el proceso de inicio de sesión (se abrirá un navegador para autorizar).
  4. Asegúrate de que la cuenta con la que iniciaste sesión tenga **una suscripción activa a GitHub Copilot**.
* En **Neovim CLI** (`copilot.vim` o `copilot.lua`):

  * Ejecuta `:Copilot sign in` y sigue el enlace en tu navegador.

---

### 2. Verifica que GitHub Copilot Chat esté habilitado

* En VS Code:

  * Ve a **Extensions** → busca “GitHub Copilot Chat” → asegúrate de que esté instalado y habilitado.
  * Configuración → busca “Copilot Chat: Enabled” → actívalo.

---

### 3. Actualiza el token de autenticación

A veces los tokens expiran o se pierden (especialmente si cambiaste de red, actualizaste el IDE o cambiaste de cuenta).

* VS Code:

  1. Paleta de Comandos → **“GitHub Copilot: Sign out”**.
  2. Luego **“GitHub Copilot: Sign in”** nuevamente.
* CLI:

  * Elimina el archivo del token (por ejemplo, `~/.config/github-copilot/hosts.json`) y vuelve a iniciar sesión.

---

### 4. Verifica restricciones de red / firewall

* Si estás en una VPN corporativa o detrás de un firewall, GitHub Copilot podría estar bloqueado para alcanzar su API.
* Permite el acceso a `github.com`, `api.githubcopilot.com` y `copilot-proxy.githubusercontent.com`.

---

### 5. Actualiza tu IDE y las extensiones de Copilot

* Las versiones desactualizadas de VS Code o de las extensiones de Copilot a veces causan este problema.
* Actualiza ambos y luego reinicia tu IDE.

---

💡 Si solucionas la autenticación pero aún ves errores, GitHub Copilot Chat también requiere **acceso a la función Copilot Chat** — algunas cuentas tienen Copilot para codificar pero **no Chat** a menos que esté explícitamente habilitado en la configuración.

---

Si quieres, puedo darte **la secuencia exacta de comandos de VS Code** para restablecer completamente la autenticación de Copilot Chat y que te lo solicite nuevamente desde cero. ¿Te gustaría que prepare eso?