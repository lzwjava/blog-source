---
audio: false
generated: true
lang: es
layout: post
title: Configuración de Simultaneidad de GitHub Actions
translated: true
type: note
---

Tu configuración actual de GitHub Actions ya tiene `cancel-in-progress: false`, lo que significa que *no debería* cancelar los jobs en progreso para el grupo de concurrencia `gh-pages`. Si los jobs aún se están cancelando, podría haber otro problema o una mala configuración causando este comportamiento. A continuación, se detallan los pasos para verificar y solucionar el problema:

### 1. **Confirmar la Configuración de Concurrencia**
Tu configuración parece correcta para prevenir cancelaciones de jobs:

```yaml
concurrency:
  group: 'gh-pages'
  cancel-in-progress: false
```

- **Qué hace esto**: La clave `concurrency` con `cancel-in-progress: false` asegura que múltiples ejecuciones del workflow para el mismo grupo `gh-pages` puedan ejecutarse simultáneamente sin cancelarse entre sí.
- **Dónde colocarlo**: Asegúrate de que este bloque `concurrency` esté definido en el **nivel del workflow** (nivel superior del archivo YAML, no dentro de un job o step). Por ejemplo:

```yaml
name: Desplegar a GitHub Pages
on:
  push:
    branches: [ main ]
concurrency:
  group: 'gh-pages'
  cancel-in-progress: false
jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      # Tus steps aquí
```

Si el bloque `concurrency` está mal ubicado (por ejemplo, dentro de un job), no funcionará como se espera. Muévelo al nivel superior si es necesario.

### 2. **Verificar Configuraciones de Concurrencia Conflictivas**
- **Múltiples workflows**: Si tienes múltiples workflows (por ejemplo, archivos YAML separados) que interactúan con la rama `gh-pages`, asegúrate de que *todos* los workflows relevantes tengan `cancel-in-progress: false`. Un solo workflow con `cancel-in-progress: true` (o sin `concurrency`) podría cancelar jobs de otros workflows.
- **Configuraciones del repositorio**: Verifica si alguna configuración a nivel de repositorio o GitHub Actions de terceros está forzando cancelaciones. Por ejemplo, algunas integraciones de CI/CD o acciones personalizadas podrían anular el comportamiento de concurrencia.

### 3. **Verificar los Disparadores del Workflow**
Los jobs pueden parecer "cancelados" si los disparadores están mal configurados o si hay condiciones de carrera. Revisa la sección `on` de tu workflow:
- Asegúrate de que el workflow se dispare solo cuando sea intencionado (por ejemplo, `on: push: branches: [ main ]` o `on: pull_request`).
- Si se definen múltiples disparadores (por ejemplo, `push` y `pull_request`), podrían crear ejecuciones superpuestas. Usa nombres únicos de `concurrency.group` para diferentes disparadores si es necesario, como:

```yaml
concurrency:
  group: 'gh-pages-${{ github.event_name }}'
  cancel-in-progress: false
```

Esto crea grupos de concurrencia separados para eventos `push` y `pull_request`, evitando que interfieran entre sí.

### 4. **Revisar los Registros de GitHub Actions**
- Ve a la pestaña **Actions** en tu repositorio de GitHub y revisa los registros de los jobs cancelados.
- Busca mensajes que indiquen por qué se canceló el job (por ejemplo, "Canceled due to concurrency" u otras razones como timeouts, cancelación manual o fallos).
- Si los registros mencionan concurrencia, verifica dos veces que *todos* los workflows que tocan la rama `gh-pages` tengan `cancel-in-progress: false`.

### 5. **Manejar Cancelaciones Manuales**
Si alguien cancela manualmente una ejecución del workflow a través de la UI de GitHub, esto detendrá todos los jobs en esa ejecución, independientemente de `cancel-in-progress: false`. Asegúrate de que tu equipo sepa no cancelar ejecuciones manualmente a menos que sea necesario.

### 6. **Considerar las Dependencias del Workflow**
Si los jobs se cancelan debido a dependencias o fallos en steps anteriores:
- Busca palabras clave `needs` en tu workflow. Si un job falla, los jobs dependientes pueden ser omitidos o cancelados.
- Usa `if: always()` para asegurar que los jobs subsiguientes se ejecuten incluso si los anteriores fallan:

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      # Pasos de build
  deploy:
    needs: build
    if: always()
    runs-on: ubuntu-latest
    steps:
      # Pasos de deploy
```

### 7. **Probar con un Workflow Mínimo**
Si el problema persiste, crea un workflow de prueba mínimo para aislar el problema:

```yaml
name: Probar Concurrencia
on:
  push:
    branches: [ main ]
concurrency:
  group: 'gh-pages'
  cancel-in-progress: false
jobs:
  test-job:
    runs-on: ubuntu-latest
    steps:
      - name: Sleep para simular job largo
        run: sleep 60
      - name: Imprimir mensaje
        run: echo "¡Job completado!"
```

Haz múltiples commits para disparar ejecuciones concurrentes y verifica si los jobs se completan sin cancelación.

### 8. **Verificar el Estado de GitHub Actions**
En raras ocasiones, GitHub Actions puede tener problemas a nivel de plataforma. Consulta la [página de Estado de GitHub](https://www.githubstatus.com/) o publicaciones recientes en X sobre interrupciones de GitHub Actions.

### 9. **Consejos para Depuración**
- Añade un step para registrar el ID de ejecución del workflow y el grupo de concurrencia para depurar:

```yaml
steps:
  - name: Registrar detalles de la ejecución
    run: echo "Run ID: ${{ github.run_id }}, Grupo de Concurrencia: ${{ github.workflow }}-${{ github.event_name }}"
```

- Usa la API de GitHub Actions para inspeccionar los workflows en ejecución programáticamente si es necesario (requiere configuración avanzada).

### Si Todavía No Funciona
Si los jobs aún se cancelan:
- Comparte el archivo YAML completo del workflow y una captura de pantalla o descripción del mensaje de cancelación de los registros de GitHub Actions.
- Déjame saber si estás usando acciones específicas (por ejemplo, `actions/checkout`, `peaceiris/actions-gh-pages`) o si tienes múltiples workflows interactuando con `gh-pages`.

Esto ayudará a identificar el problema exacto. ¡Avísame si puedo ayudar en algo más!