---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Aplicar intervalo de construcción de 30 minutos
translated: true
type: note
---

### Modificar el flujo de trabajo para imponer un intervalo de 30 minutos entre builds

Para asegurar que tu flujo de trabajo de despliegue de Jekyll no se ejecute con demasiada frecuencia (es decir, al menos un intervalo de 30 minutos entre ejecuciones consecutivas), puedes agregar un paso condicional al principio del trabajo `build`. Este paso consultará la API de GitHub para obtener la marca de tiempo de la ejecución exitosa más reciente de este flujo de trabajo. Si el activador actual se produce dentro de los 30 minutos posteriores a la finalización de esa ejecución, el trabajo finalizará anticipadamente con un mensaje (omitirá el build).

Este enfoque:
- Utiliza la API REST de GitHub (no se necesitan herramientas externas).
- Solo verifica las ejecuciones previas **exitosas** (estado: "completed", conclusión: "success").
- Calcula la diferencia de tiempo en segundos y la compara con 1800 (30 minutos).
- Funciona con tus activadores `push` y `workflow_dispatch` existentes.
- No interfiere con la configuración de concurrencia (que maneja las ejecuciones superpuestas).

#### Fragmento de YAML actualizado
Inserta este nuevo paso justo después del paso "Checkout Repository" en tu trabajo `build`. El resto del flujo de trabajo permanece sin cambios.

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    environment: github-pages
    env:
      GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      TELEGRAM_BOT_API_KEY: ${{ secrets.TELEGRAM_BOT_API_KEY }}
      OPENROUTER_API_KEY: ${{ secrets.OPENROUTER_API_KEY }}

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 5

      - name: Imponer intervalo de 30 minutos entre builds
        id: cooldown
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          # Obtener la ejecución exitosa más reciente de este flujo de trabajo
          RUNS_RESPONSE=$(curl -s -H "Authorization: token $GITHUB_TOKEN" \
            -H "Accept: application/vnd.github.v3+json" \
            "https://api.github.com/repos/${{ github.repository }}/actions/workflows/${{ github.workflow_ref }}/runs?status=completed&conclusion=success&per_page=1&sort=timestamp&direction=desc")

          # Extraer la marca de tiempo completed_at de la última ejecución exitosa (formato ISO 8601)
          LAST_COMPLETED_AT=$(echo "$RUNS_RESPONSE" | jq -r '.[0].completed_at // empty')
          
          if [ -z "$LAST_COMPLETED_AT" ] || [ "$LAST_COMPLETED_AT" = "null" ]; then
            echo "No se encontraron ejecuciones exitosas previas. Procediendo con el build."
            echo "skip_build=false" >> $GITHUB_OUTPUT
            exit 0
          fi

          # Convertir las marcas de tiempo a segundos Unix para la comparación
          CURRENT_TIME=$(date -u +%s)
          LAST_TIME=$(date -d "$LAST_COMPLETED_AT" +%s)
          TIME_DIFF=$((CURRENT_TIME - LAST_TIME))

          echo "La última ejecución exitosa finalizó a las: $LAST_COMPLETED_AT (diferencia: ${TIME_DIFF}s)"

          if [ $TIME_DIFF -lt 1800 ]; then  # 1800 segundos = 30 minutos
            echo "Build omitido: Menos de 30 minutos desde la última ejecución exitosa."
            echo "skip_build=true" >> $GITHUB_OUTPUT
            exit 0
          else
            echo "Intervalo de tiempo suficiente. Procediendo con el build."
            echo "skip_build=false" >> $GITHUB_OUTPUT
            exit 0
          fi

      # Omitir todo el build si la verificación del intervalo falla (agregar esta condición a los pasos siguientes o envolver el build en un if)
      - name: Configurar Python 3.13.2
        if: steps.cooldown.outputs.skip_build != 'true'
        uses: actions/setup-python@v4
        with:
          python-version: "3.13.2"

      # ... (repetir la condición 'if: steps.cooldown.outputs.skip_build != 'true'' en TODOS los pasos restantes después de este)
```

#### Cambios clave explicados
1. **Consulta a la API**:
   - Utiliza `curl` para acceder al endpoint de la API de GitHub Actions para las ejecuciones del flujo de trabajo.
   - Filtra por `status=completed` y `conclusion=success` para obtener solo las ejecuciones finalizadas y exitosas.
   - Limita a `per_page=1` y ordena por `timestamp desc` para obtener la más reciente.
   - Extrae `completed_at` (el tiempo exacto de finalización de la ejecución anterior).

2. **Cálculo del tiempo**:
   - Convierte tanto la hora actual como la última hora de finalización a marcas de tiempo Unix usando `date`.
   - Calcula la diferencia en segundos.
   - Si es `< 1800` segundos, establece `skip_build=true` y sale del paso anticipadamente.

3. **Ejecución condicional**:
   - Agrega `if: steps.cooldown.outputs.skip_build != 'true'` a **cada paso posterior** (por ejemplo, Configurar Python, Instalar Dependencias, hasta Sincronizar el sitio construido).
   - Esto asegura que el trabajo se reporte como "omitido" en la interfaz de usuario de GitHub si se activa el intervalo, pero aún así registra la razón.

4. **Casos extremos manejados**:
   - Sin ejecuciones previas: Procede (primer build).
   - Ejecuciones previas fallidas/en progreso: Las ignora y procede.
   - Errores de la API: Recurre a proceder (valor predeterminado seguro).
   - `jq` está preinstalado en `ubuntu-latest`, por lo que no se necesita configuración adicional.

#### Probar el cambio
- Confirma esto en tu rama `main` (activará el flujo de trabajo).
- Activa múltiples pushes/dispatches rápidos: El segundo dentro de 30 min debería omitirse.
- Monitorea los registros del trabajo para ver el mensaje "Build skipped".
- Si deseas ajustar el intervalo (por ejemplo, 1 hora), cambia `1800` a `3600`.

#### Alternativas
- **Activador Programado**: Si quieres builds *periódicos* cada 30 min (independientemente de los pushes), agrega esto a la sección `on:`:
  ```yaml
  schedule:
    - cron: '*/30 * * * *'  # Cada 30 minutos
  ```
  Pero esto no impone un intervalo en los activadores push—úsalo junto con el paso de intervalo si es necesario.
- **Acción Personalizada**: Para reutilización, envuelve la lógica del intervalo en un flujo de trabajo reutilizable o una acción compuesta.
- **Limitaciones**: Esto verifica el tiempo de finalización de la ejecución, no el tiempo de inicio. Si una ejecución anterior aún se está ejecutando >30 min, la concurrencia la cancelará de todos modos.

Si esto no se ajusta a tu intención exacta (por ejemplo, querías programar *al menos* cada 30 min), ¡proporciona más detalles!