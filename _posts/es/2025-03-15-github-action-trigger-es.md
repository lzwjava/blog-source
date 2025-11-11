---
audio: false
generated: true
lang: es
layout: post
title: Activación de GitHub Actions
translated: true
type: note
---

Sí, una GitHub Action puede activar otra GitHub Action, aunque no directamente. Los flujos de trabajo de GitHub Actions normalmente se activan por eventos específicos como pushes, pull requests o programaciones, pero existen varios métodos indirectos para que un flujo de trabajo active a otro. A continuación se presentan las formas principales de lograr esto:

---

### 1. Usando el evento `workflow_dispatch`
Puedes activar un flujo de trabajo mediante programación usando el evento `workflow_dispatch` a través de la API de GitHub. Esto permite que un flujo de trabajo inicie otro que esté configurado para escuchar este evento.

- **Cómo funciona**: El primer flujo de trabajo realiza una llamada a la API para activar el segundo flujo de trabajo.
- **Ejemplo**:
  ```yaml
  name: Activar Otro Flujo de Trabajo
  on: [push]
  jobs:
    trigger:
      runs-on: ubuntu-latest
      steps:
        - name: Activar Flujo de Trabajo
          run: |
            curl -X POST \
              -H "Authorization: token ${{ secrets.GITHUB_TOKEN }}" \
              -H "Accept: application/vnd.github.v3+json" \
              https://api.github.com/repos/<owner>/<repo>/actions/workflows/<workflow_id>/dispatches \
              -d '{"ref": "main"}'
  ```
  Reemplaza `<owner>`, `<repo>`, y `<workflow_id>` con los detalles de tu repositorio y el ID del flujo de trabajo objetivo. El segundo flujo de trabajo debe incluir `on: [workflow_dispatch]` en su configuración.

---

### 2. Usando eventos Repository Dispatch
Un flujo de trabajo puede enviar un evento personalizado usando un repository dispatch, el cual otro flujo de trabajo puede escuchar y activarse.

- **Cómo funciona**: El primer flujo de trabajo envía un evento repository dispatch a través de la API de GitHub, y el segundo flujo de trabajo responde a ese evento.
- **Ejemplo**:
  - Primer flujo de trabajo (envía el evento):
    ```yaml
    name: Enviar Evento Dispatch
    on: [push]
    jobs:
      send-dispatch:
        runs-on: ubuntu-latest
        steps:
          - name: Enviar Dispatch
            run: |
              curl -X POST \
                -H "Authorization: token ${{ secrets.GITHUB_TOKEN }}" \
                -H "Accept: application/vnd.github.v3+json" \
                https://api.github.com/repos/<owner>/<repo>/dispatches \
                -d '{"event_type": "custom_event"}'
    ```
  - Segundo flujo de trabajo (activado por el evento):
    ```yaml
    name: Activado por Dispatch
    on:
      repository_dispatch:
        types: [custom_event]
    jobs:
      respond:
        runs-on: ubuntu-latest
        steps:
          - name: Responder al Evento
            run: echo "Activado por custom_event"
    ```

---

### 3. Activación mediante eventos Git
Un flujo de trabajo puede activar a otro generando un evento Git, como crear un commit o abrir un pull request, al cual el segundo flujo de trabajo está configurado para responder.

- **Cómo funciona**: El primer flujo de trabajo modifica el repositorio (por ejemplo, haciendo push de un commit), activando un segundo flujo de trabajo configurado para ese evento (por ejemplo, `on: [push]`).
- **Ejemplo**:
  ```yaml
  name: Crear Commit
  on: [push]
  jobs:
    create-commit:
      runs-on: ubuntu-latest
      steps:
        - name: Checkout
          uses: actions/checkout@v2
        - name: Crear Archivo
          run: echo "Nuevo archivo" > newfile.txt
        - name: Hacer Commit y Push
          run: |
            git config user.name "GitHub Action"
            git config user.email "action@github.com"
            git add newfile.txt
            git commit -m "Agregar nuevo archivo"
            git push
  ```
  Esto podría activar otro flujo de trabajo configurado para ejecutarse en eventos `push`.

---

### Consideraciones Clave
- **Permisos**: El token de GitHub utilizado en las llamadas a la API debe tener permisos suficientes para activar flujos de trabajo o enviar eventos dispatch.
- **Límites de Tasa**: Ten en cuenta los límites de tasa de la API de GitHub, especialmente para flujos de trabajo que se ejecutan con frecuencia.
- **Evitar Bucles**: Prevén bucles infinitos añadiendo condiciones para evitar que los flujos de trabajo se activen entre sí sin fin.
- **Configuración**: Asegúrate de que el flujo de trabajo objetivo esté configurado correctamente para escuchar el evento deseado.

---

### Conclusión
Si bien GitHub Actions no ofrece un mecanismo directo para que un flujo de trabajo llame a otro, puedes lograrlo indirectamente usando `workflow_dispatch`, eventos repository dispatch o eventos Git como commits o pull requests. Estos métodos te permiten encadenar o activar flujos de trabajo de manera efectiva según tus necesidades.