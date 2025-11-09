---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Manejo de Zonas Horarias en Python con pytz
translated: true
type: note
---

### Instalación de pytz
pytz es una librería de terceros para Python que maneja objetos datetime conscientes de la zona horaria. Ten en cuenta que a partir de Python 3.9+, se prefiere el módulo incorporado `zoneinfo` para código nuevo (está en la librería estándar y maneja las actualizaciones automáticamente), pero pytz sigue siendo ampliamente utilizado.

Para instalar pytz, usa pip:
```
pip install pytz
```

### Uso Básico con pytz
pytz funciona con el módulo `datetime` de Python. Conceptos clave:
- **Objetos de zona horaria**: Usa `pytz.timezone()` para crear objetos conscientes de la zona horaria (por ejemplo, para "UTC" o "America/New_York").
- **Localización**: Adjunta una zona horaria a un objeto `datetime` naive usando `.localize()`.
- **Conversión**: Usa `.astimezone()` para convertir entre zonas horarias.
- **Peligros**: Evita usar los constructores de `pytz` directamente en objetos `datetime`; siempre localiza primero para manejar correctamente el horario de verano (DST).

Importa los módulos requeridos:
```python
import datetime
import pytz
```

### Ejemplos

#### 1. Obtener la Hora Actual en una Zona Horaria Específica
Usa `pytz.utc` o zonas horarias específicas. Siempre trabaja internamente con UTC para seguir las mejores prácticas.

```python
# Obtener la hora UTC actual
utc_now = datetime.datetime.now(pytz.utc)
print(utc_now)  # ej., 2023-10-15 14:30:00+00:00

# Obtener la hora actual en la hora del Este de EE. UU.
eastern = pytz.timezone('US/Eastern')
eastern_now = datetime.datetime.now(eastern)
print(eastern_now)  # ej., 2023-10-15 10:30:00-04:00 (se ajusta para DST)
```

#### 2. Localizar un Datetime Naive
Convertir un datetime naive (sin conciencia de zona horaria) a uno consciente de la zona horaria.

```python
# Crear un datetime naive (ej., 15 de octubre de 2023, 12:00)
naive_dt = datetime.datetime(2023, 10, 15, 12, 0)
print(naive_dt)  # 2023-10-15 12:00:00

# Localizar a la hora del Este de EE. UU.
eastern = pytz.timezone('US/Eastern')
aware_dt = eastern.localize(naive_dt)
print(aware_dt)  # 2023-10-15 12:00:00-04:00
```

#### 3. Convertir entre Zonas Horarias
Primero localiza un datetime, luego convierte.

```python
# Comenzar con la hora UTC
utc_dt = pytz.utc.localize(datetime.datetime(2023, 10, 15, 14, 0))
print(utc_dt)  # 2023-10-15 14:00:00+00:00

# Convertir a la hora del Pacífico
pacific = pytz.timezone('US/Pacific')
pacific_dt = utc_dt.astimezone(pacific)
print(pacific_dt)  # 2023-10-15 07:00:00-07:00
```

#### 4. Manejar Listas de Zonas Horarias
pytz soporta nombres comunes de zonas horarias de la base de datos Olson.

```python
# Listar zonas horarias disponibles
print(pytz.all_timezones[:10])  # Muestra: ['Africa/Abidjan', 'Africa/Accra', ...]

# O específicas por país
print(pytz.country_timezones['US'])  # ['America/New_York', 'America/Los_Angeles', ...]
```

### Migración a zoneinfo (Recomendado para Python 3.9+)
Para versiones más recientes de Python, usa el módulo incorporado `zoneinfo` en lugar de pytz por simplicidad:
```python
from zoneinfo import ZoneInfo
import datetime

# Equivalente a los ejemplos de pytz
eastern_now = datetime.datetime.now(ZoneInfo('US/Eastern'))
aware_dt = datetime.datetime(2023, 10, 15, 12, 0).replace(tzinfo=ZoneInfo('US/Eastern'))
```

### Problemas Comunes y Consejos
- **Tiempos ambiguos**: Durante las transiciones de DST, usa `is_dst` en `.localize()` (ej., `eastern.localize(naive_dt, is_dst=False)`).
- **Normalización UTC**: Convierte a UTC antes de hacer operaciones aritméticas para evitar errores.
- **Actualizar pytz**: Utiliza IANA tzdata; manténlo actualizado via pip.
- Para más información, consulta la [documentación de pytz](https://pythonhosted.org/pytz/). Si encuentras errores, pega fragmentos de código para obtener ayuda con la depuración.