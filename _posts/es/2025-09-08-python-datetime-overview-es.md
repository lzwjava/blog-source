---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Descripción General del Módulo Datetime de Python
translated: true
type: note
---

### Resumen del Módulo datetime de Python

El módulo `datetime` de Python proporciona clases para manipular fechas, horas y marcas de tiempo. Está en la biblioteca estándar, por lo que no requiere instalación. Las clases clave incluyen:
- `date`: Maneja fechas (año, mes, día).
- `time`: Maneja horas (hora, minuto, segundo, microsegundo).
- `datetime`: Combina fecha y hora.
- `timedelta`: Representa una duración (por ejemplo, para aritmética de fechas).

Es útil para tareas como registrar marcas de tiempo, calcular duraciones o formatear fechas para visualización/salida.

### Importar el Módulo

Importa el módulo completo o las clases específicas según sea necesario:

```python
import datetime  # Módulo completo

# O importa clases específicas
from datetime import datetime, date, time, timedelta
```

### Obtener la Fecha y Hora Actual

Usa `datetime.now()` para obtener la fecha y hora local actual como un objeto `datetime`.

```python
import datetime

now = datetime.datetime.now()
print(now)  # Salida: ej., 2023-10-05 14:30:45.123456
print(type(now))  # <class 'datetime.datetime'>
```

Para la hora UTC, usa `datetime.utcnow()` (aunque es preferible usar `datetime.now(timezone.utc)` con importaciones de `datetime.timezone` para manejo de zonas horarias).

### Crear Objetos de Fecha y Hora

Construye objetos manualmente con sus constructores.

```python
# Fecha: año, mes, día
d = datetime.date(2023, 10, 5)
print(d)  # 2023-10-05

# Hora: hora, minuto, segundo, microsegundo (opcional)
t = datetime.time(14, 30, 45)
print(t)  # 14:30:45

# Datetime: combina fecha y hora
dt = datetime.datetime(2023, 10, 5, 14, 30, 45)
print(dt)  # 2023-10-05 14:30:45
```

Omite las partes que no necesites (por ejemplo, `datetime.datetime(2023, 10, 5)` crea un datetime a la medianoche).

### Formatear Fechas (strftime)

Convierte fechas a cadenas usando `strftime` con códigos de formato (por ejemplo, `%Y` para año, `%m` para mes).

```python
now = datetime.datetime.now()
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)  # ej., 2023-10-05 14:30:45

# Formatos comunes:
# %A: Día de la semana completo (ej., Thursday)
# %B: Mes completo (ej., October)
# %Y-%m-%d: Fecha ISO
```

### Analizar Fechas desde Cadenas (strptime)

Convierte cadenas a objetos `datetime` usando `strptime` con formatos coincidentes.

```python
date_str = "2023-10-05 14:30:45"
parsed = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print(parsed)  # 2023-10-05 14:30:45
print(type(parsed))  # <class 'datetime.datetime'>
```

El formato debe coincidir exactamente, o se generará un `ValueError`.

### Aritmética de Fechas con timedelta

Suma o resta intervalos de tiempo usando `timedelta`.

```python
now = datetime.datetime.now()
one_day = datetime.timedelta(days=1)
tomorrow = now + one_day
print(tomorrow)  # Fecha actual + 1 día

# Restar
yesterday = now - one_day

# Partes: días, segundos, microsegundos, milisegundos, minutos, horas, semanas
one_week = datetime.timedelta(weeks=1)
```

Para diferencias entre fechas:

```python
date1 = datetime.datetime(2023, 10, 5)
date2 = datetime.datetime(2023, 10, 10)
delta = date2 - date1
print(delta.days)  # 5
```

### Zonas Horarias (Uso Avanzado)

Para operaciones con zonas horarias, usa `timezone` (Python 3.3+). El módulo no maneja conversiones de zona horaria de forma nativa; combínalo con la biblioteca `pytz` para un manejo robusto.

```python
from datetime import datetime, timezone

# Datetime ingenuo (sin zona horaria)
naive = datetime.now()

# UTC consciente
utc = datetime.now(timezone.utc)

# Zona horaria personalizada (requiere tzinfo)
import pytz  # Podría necesitar pip install pytz
eastern = pytz.timezone("US/Eastern")
eastern_time = naive.astimezone(eastern)
```

### Consejos Comunes y Problemas Frecuentes
- **Objetos inmutables**: Los objetos `datetime` no se pueden modificar directamente; las operaciones aritméticas crean nuevos.
- **Días del mes**: Usa 29 para febrero en años bisiestos; el módulo maneja esto con `calendar` o `dateutil` para comprobaciones de año bisiesto.
- **Rendimiento**: Evita llamadas frecuentes a `now()` en bucles; almacena el valor.
- **Errores**: Cuidado con fechas inválidas (por ejemplo, `date(2023, 2, 30)` genera `ValueError`).
- **Extensiones de biblioteca**: Para análisis avanzado, considera los paquetes `dateutil` o `arrow`.

Para la documentación completa, consulta la documentación oficial de Python en [docs.python.org](https://docs.python.org/3/library/datetime.html). Practica con estos ejemplos en un intérprete de Python.