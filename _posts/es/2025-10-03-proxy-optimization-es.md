---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Optimización del Rendimiento en la Selección de Proxy de Clash
translated: true
type: note
---

### Resumen de la Optimización: Scripts de Selección de Proxies para Clash

Optimicé los scripts de selección de proxies para Clash para evitar probar proxies que no serán seleccionados, mejorando significativamente el rendimiento al minimizar las pruebas de velocidad innecesarias.

#### Qué se Optimizó

El código original seguía este flujo de trabajo ineficiente:
1.  Probar la velocidad de todos los proxies disponibles.
2.  Luego filtrar para seleccionar solo los proxies SG/TW (o HK).
3.  Esto resultaba en una pérdida de tiempo probando proxies que serían descartados.

#### La Solución

Modifiqué la función `get_top_proxies()` en `speed.py` para que acepte un parámetro `name_filter` y aplique el filtrado antes de la prueba de velocidad:

```python
def get_top_proxies(num_results=5, name_filter=None):
    """
    Tests Clash proxy speeds concurrently and returns the top N fastest individual proxies.

    Args:
        num_results (int): Number of top proxies to return (default: 5)
        name_filter (list): List of strings to filter proxy names. Only proxies containing
                           any of these strings in their name will be tested.
    """
```

#### Beneficios de Rendimiento

-   **Solicitudes de red reducidas**: Solo prueba los proxies que realmente tienes la intención de usar.
-   **Ejecución más rápida**: Elimina el tiempo innecesario dedicado a proxies irrelevantes.
-   **Registros más claros**: Muestra exactamente cuántos proxies fueron filtrados, mejorando la transparencia.

#### Configuración Simplificada

Se eliminó el flag `--hk`. El script ahora siempre prueba solo los proxies SG y TW por defecto para lograr la máxima concentración y simplicidad.

#### Resultados

La optimización redujo drásticamente el tiempo de ejecución, ya que la mayoría de los proxies no contienen "SG" o "TW" en sus nombres. Esto hace que la fase de prueba de velocidad sea mucho más eficiente, entregando resultados más rápido sin comprometer la funcionalidad.