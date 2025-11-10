---
audio: false
generated: true
image: false
lang: es
layout: post
title: Instalar la extensión CLI de GitHub Copilot
translated: true
type: note
---

El comando `gh extension install github/gh-copilot` instala la extensión GitHub Copilot para GitHub CLI, permitiendo funciones de Copilot como sugerencias y explicaciones en la línea de comandos. Para usuarios empresariales, si este comando aplica depende de condiciones específicas:

- **Configuración Empresarial**: Los usuarios empresariales pueden usar la extensión Copilot CLI si su organización o empresa tiene una suscripción GitHub Copilot Business o Copilot Enterprise y la función CLI está habilitada por los administradores. Si el propietario de la organización o el administrador de la empresa ha deshabilitado Copilot en la CLI, la extensión no se puede usar, incluso si está instalada.[](https://docs.github.com/fr/enterprise-cloud%40latest/copilot/how-tos/set-up/install-copilot-in-the-cli)[](https://docs.github.com/en/enterprise-cloud%40latest/copilot/how-tos/set-up/install-copilot-in-the-cli)
- **Autenticación**: Los usuarios empresariales deben autenticarse en GitHub CLI con una cuenta de GitHub que tenga asignada una licencia de Copilot. Para las cuentas de usuario gestionadas en GitHub Enterprise Cloud (GHE.com), puede ser necesaria una configuración adicional, como actualizar la configuración antes de iniciar sesión.[](https://docs.github.com/en/enterprise-cloud%40latest/copilot/how-tos/set-up/install-copilot-extension)
- **Requisitos de Instalación**: GitHub CLI debe estar instalado antes de ejecutar el comando. El proceso de instalación en sí es el mismo para usuarios empresariales e individuales, pero las políticas empresariales pueden restringir el uso.[](https://docs.github.com/en/enterprise-cloud%40latest/copilot/how-tos/set-up/install-copilot-in-the-cli)

**Pasos para Usuarios Empresariales**:
1. Asegúrate de que GitHub CLI esté instalado (consulta el [repositorio de GitHub CLI](https://github.com/cli/cli) para obtener instrucciones).
2. Verifica con el administrador de tu empresa que Copilot CLI esté habilitado para tu organización.
3. Ejecuta `gh extension install github/gh-copilot` en tu terminal.
4. Autentícate usando `gh auth login` con tu cuenta de GitHub asignada por la empresa.
5. Si usas una cuenta de usuario gestionada en GHE.com, sigue los pasos de configuración adicionales descritos en [Usar GitHub Copilot con una cuenta en GHE.com](https://docs.github.com/en/enterprise-cloud@latest/copilot/configuring-github-copilot-in-your-environment/using-github-copilot-with-an-account-on-ghecom).[](https://docs.github.com/en/enterprise-cloud%40latest/copilot/how-tos/set-up/install-copilot-extension)

Si tu empresa restringe el acceso a la CLI o no ha habilitado Copilot, la extensión podría instalarse pero no funcionará. Consulta con tu administrador los detalles de la política.

[Instalar GitHub Copilot en la CLI](https://docs.github.com/en/enterprise-cloud@latest/copilot/installing-github-copilot-in-the-cli)[](https://docs.github.com/en/enterprise-cloud%40latest/copilot/how-tos/set-up/install-copilot-in-the-cli)
[Configurar GitHub Copilot para tu empresa](https://docs.github.com/en/enterprise-cloud@latest/copilot/setting-up-github-copilot-for-your-enterprise)[](https://docs.github.com/en/enterprise-cloud%40latest/copilot/how-tos/set-up/set-up-for-enterprise)