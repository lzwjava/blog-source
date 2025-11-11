---
audio: false
generated: true
lang: es
layout: post
title: Eliminación de Dependabot
translated: true
type: note
---

Para eliminar Dependabot de GitHub Actions, necesitas desactivar su capacidad para crear pull requests que activen flujos de trabajo y, opcionalmente, eliminar cualquier flujo de trabajo personalizado específicamente vinculado a Dependabot. A continuación se detallan los pasos para lograrlo. Nota: asumo que "dependant bot" en tu consulta se refiere a "Dependabot", una herramienta común en GitHub para la gestión de dependencias.

---

### Paso 1: Desactivar las actualizaciones de versión de Dependabot
Las actualizaciones de versión de Dependabot crean automáticamente pull requests para mantener tus dependencias actualizadas. Estos pull requests pueden activar flujos de trabajo de GitHub Actions. Para desactivar esta función:

- **Localiza el archivo de configuración**: Revisa tu repositorio en busca de un archivo llamado `dependabot.yml` en el directorio `.github`.
- **Elimina el archivo**: Si existe, elimina el archivo `dependabot.yml` y confirma este cambio. Esto detiene a Dependabot de crear pull requests para actualizaciones de versión.
- **Verifica**: Si no existe un archivo `dependabot.yml`, las actualizaciones de versión ya están desactivadas.

---

### Paso 2: Desactivar las actualizaciones de seguridad de Dependabot
Las actualizaciones de seguridad de Dependabot generan pull requests para corregir vulnerabilidades en tus dependencias, lo que también puede activar flujos de trabajo de GitHub Actions. Para desactivarlas:

- **Ve a la Configuración del Repositorio**: En tu repositorio de GitHub, haz clic en la pestaña **Settings**.
- **Navega a la Configuración de Seguridad**: Desplázate hasta **Security & analysis** (o **Code security and analysis**, dependiendo de tu interfaz de GitHub).
- **Desactiva las Actualizaciones de Seguridad**: Encuentra **Dependabot security updates** y haz clic en **Disable**.

Esto evita que Dependabot cree pull requests para correcciones de seguridad.

---

### Paso 3: (Opcional) Eliminar flujos de trabajo personalizados relacionados con Dependabot
Si has configurado flujos de trabajo de GitHub Actions específicamente para manejar los pull requests de Dependabot (por ejemplo, fusión automática, etiquetado o uso de metadatos de Dependabot), es posible que desees limpiarlos:

- **Revisa los archivos de flujo de trabajo**: Busca en el directorio `.github/workflows` los archivos YAML.
- **Identifica la lógica de Dependabot**: Busca condiciones como `if: github.event.pull_request.user.login == 'dependabot[bot]'` o acciones como `dependabot/fetch-metadata`.
- **Elimina o modifica**: Elimina estos flujos de trabajo o ajústalos para eliminar la lógica específica de Dependabot, luego confirma los cambios.

Este paso es opcional porque desactivar Dependabot en los Pasos 1 y 2 evitará que cree nuevos pull requests, lo que significa que los flujos de trabajo existentes ya no serán activados por Dependabot. Sin embargo, eliminar estos flujos de trabajo garantiza una limpieza completa.

---

### Notas Adicionales
- **Pull Requests Existentes**: Desactivar Dependabot no cierra los pull requests existentes que haya creado. Estos aún pueden activar flujos de trabajo si se actualizan. Puedes cerrarlos manualmente si es necesario.
- **Alertas de Dependabot**: Si también deseas detener las notificaciones de vulnerabilidades (no directamente vinculadas a GitHub Actions), ve a **Settings > Security & analysis** y desactiva **Dependabot alerts**. Esto es opcional y no está relacionado con los activadores de flujos de trabajo.

---

### Resultado
Al completar los Pasos 1 y 2, Dependabot ya no creará pull requests en tu repositorio, eliminando efectivamente su influencia en GitHub Actions. Si has personalizado flujos de trabajo para Dependabot, el Paso 3 garantiza que toda la automatización relacionada desaparezca. Tus GitHub Actions ahora solo se ejecutarán en base a otros eventos, sin verse afectadas por Dependabot.