---
audio: false
generated: true
image: false
lang: es
layout: post
title: Corrección de Estimación de Carga de Batería
translated: true
type: note
---

El error `Cannot estimate time to full charge (sysfs files not found)` indica que el script no pudo encontrar los archivos de información de la batería esperados en `/sys/class/power_supply/BAT0/`. Esto puede suceder si:
1. La batería tiene un nombre diferente a `BAT0` (por ejemplo, `BAT1` u otro nombre).
2. Los archivos específicos (`charge_now`, `charge_full`, `current_now`) no están disponibles o tienen nombres diferentes en tu laptop Lenovo.
3. El usuario que ejecuta el script no tiene permiso para acceder a estos archivos.

Aquí tienes un script de Python corregido que detecta dinámicamente el nombre de la batería y maneja variaciones en los nombres de archivos sysfs (por ejemplo, `energy_now` en lugar de `charge_now` para algunos sistemas). También incluye un mejor manejo de errores y comprobaciones de permisos:

```python
import psutil
import os
import glob

def find_battery_path():
    """Encuentra el directorio de la batería en /sys/class/power_supply."""
    battery_paths = glob.glob('/sys/class/power_supply/BAT*')
    if not battery_paths:
        return None
    return battery_paths[0]  # Retorna la primera batería encontrada (ej. BAT0 o BAT1)

def get_battery_info():
    try:
        # Obtener información de la batería usando psutil
        battery = psutil.sensors_battery()
        
        if battery is None:
            print("No se detectó ninguna batería.")
            return

        # Porcentaje de la batería
        percent = battery.percent
        print(f"Porcentaje de Batería: {percent:.2f}%")

        # Verificar si la batería se está cargando
        is_charging = battery.power_plugged
        status = "Cargando" if is_charging else "Descargando"
        print(f"Estado: {status}")

        # Estimar tiempo restante (solo cuando se está descargando)
        if not is_charging and battery.secsleft != psutil.POWER_TIME_UNLIMITED:
            remaining_secs = battery.secsleft
            hours = remaining_secs // 3600
            minutes = (remaining_secs % 3600) // 60
            print(f"Tiempo Restante Estimado: {hours} horas, {minutes} minutos")
        elif is_charging:
            # Intentar estimar el tiempo hasta la carga completa usando sysfs
            battery_path = find_battery_path()
            if not battery_path:
                print("No se puede estimar el tiempo hasta la carga completa (no se encontró batería en sysfs).")
                return

            try:
                # Verificar archivos basados en carga o energía
                charge_now_file = os.path.join(battery_path, 'charge_now')
                energy_now_file = os.path.join(battery_path, 'energy_now')
                charge_full_file = os.path.join(battery_path, 'charge_full')
                energy_full_file = os.path.join(battery_path, 'charge_full_design')
                current_now_file = os.path.join(battery_path, 'current_now')

                # Determinar qué archivos usar (carga o energía)
                if os.path.exists(charge_now_file) and os.path.exists(charge_full_file):
                    now_file, full_file = charge_now_file, charge_full_file
                elif os.path.exists(energy_now_file) and os.path.exists(energy_full_file):
                    now_file, full_file = energy_now_file, energy_full_file
                else:
                    print("No se puede estimar el tiempo hasta la carga completa (archivos de carga/energía no encontrados).")
                    return

                # Leer datos de la batería
                with open(now_file, 'r') as f:
                    charge_now = int(f.read().strip())
                with open(full_file, 'r') as f:
                    charge_full = int(f.read().strip())
                with open(current_now_file, 'r') as f:
                    current_now = int(f.read().strip())

                if current_now > 0:
                    charge_remaining = charge_full - charge_now
                    seconds_to_full = (charge_remaining / current_now) * 3600
                    hours = int(seconds_to_full // 3600)
                    minutes = int((seconds_to_full % 3600) // 60)
                    print(f"Tiempo Estimado hasta Carga Completa: {hours} horas, {minutes} minutos")
                else:
                    print("No se puede estimar el tiempo hasta la carga completa (current_now es 0).")
            except PermissionError:
                print("No se puede estimar el tiempo hasta la carga completa (permiso denegado). Intenta ejecutar con sudo.")
            except FileNotFoundError:
                print(f"No se puede estimar el tiempo hasta la carga completa (archivos sysfs no encontrados en {battery_path}).")
            except Exception as e:
                print(f"Error al estimar el tiempo hasta la carga completa: {e}")
        else:
            print("No hay estimación de tiempo restante disponible.")

    except Exception as e:
        print(f"Error al recuperar la información de la batería: {e}")

if __name__ == "__main__":
    get_battery_info()
```

### Cambios Realizados
1. **Detección Dinámica de la Batería**:
   - Usa `glob.glob('/sys/class/power_supply/BAT*')` para encontrar el directorio de la batería (ej. `BAT0`, `BAT1`) en lugar de codificar `BAT0`.
   - Retorna la primera batería encontrada o `None` si no se detecta ninguna.

2. **Soporte para Archivos de Carga y Energía**:
   - Verifica tanto los archivos `charge_now`/`charge_full` como `energy_now`/`energy_full`, ya que algunos sistemas usan métricas basadas en energía (en vatios-hora) en lugar de carga (en microamperios-hora).
   - Selecciona el par de archivos apropiado basándose en la disponibilidad.

3. **Manejo de Errores Mejorado**:
   - Maneja `PermissionError` por separado para sugerir ejecutar con `sudo` si el acceso es denegado.
   - Proporciona retroalimentación específica si los archivos sysfs no se encuentran o si `current_now` es cero.

4. **Salida Formateada**:
   - Limita el porcentaje de la batería a dos decimales (`{percent:.2f}`) para una salida más limpia.

### Cómo Usarlo
1. **Instalar `psutil` (si no está instalado)**:
   ```bash
   sudo pip3 install psutil
   ```

2. **Guardar el Script**:
   - Guarda el script actualizado como, por ejemplo, `battery_info.py`.

3. **Ejecutar el Script**:
   - Ejecuta en una terminal:
     ```bash
     python3 battery_info.py
     ```
   - Si obtienes un error de "permiso denegado", intenta ejecutar con privilegios elevados:
     ```bash
     sudo python3 battery_info.py
     ```

4. **Verificar la Ruta de la Batería**:
   - Para verificar el nombre de la batería y los archivos disponibles, ejecuta:
     ```bash
     ls /sys/class/power_supply
     ```
     Luego, revisa los contenidos del directorio de la batería (ej. `BAT0` o `BAT1`):
     ```bash
     ls /sys/class/power_supply/BAT0
     ```
   - Busca archivos como `charge_now`, `charge_full`, `energy_now`, `energy_full`, o `current_now`. Si son diferentes (ej. `energy_full_design` en lugar de `charge_full`), el script debería manejarlo, pero avísame si necesitas más ajustes.

### Consejos para Depuración
- Si el script aún reporta "archivos sysfs no encontrados", verifica los nombres exactos de los archivos en `/sys/class/power_supply/BAT*`. Algunas laptops Lenovo pueden usar nombres no estándar o tener soporte sysfs limitado.
- Si ves "permiso denegado", ejecutar con `sudo` debería resolverlo, pero ten cuidado con los privilegios elevados.
- Si la batería es detectada pero no se proporciona ninguna estimación de tiempo, podría deberse a que `current_now` es cero (común cuando el sistema no reporta activamente la corriente de carga). En este caso, el script indicará que no hay estimación disponible.

### Ejemplo de Salida
En tu sistema (Lenovo XiaoXin-14-IAH8), podrías ver algo como:
```
Porcentaje de Batería: 49.62%
Estado: Cargando
Tiempo Estimado hasta Carga Completa: 1 horas, 45 minutos
```
O, si los archivos aún faltan:
```
Porcentaje de Batería: 49.62%
Estado: Cargando
No se puede estimar el tiempo hasta la carga completa (archivos sysfs no encontrados en /sys/class/power_supply/BAT0).
```

### Si los Problemas Persisten
Si el script aún falla al encontrar los archivos sysfs, por favor comparte la salida de:
```bash
ls -l /sys/class/power_supply
ls -l /sys/class/power_supply/BAT*/*
```
Esto ayudará a identificar los nombres exactos de los archivos y los permisos. Luego puedo ajustar el script aún más para que coincida con la configuración de tu sistema.

[Documentación de psutil](https://psutil.readthedocs.io/en/latest/)  
[Linux sysfs Power Supply](https://www.kernel.org/doc/html/latest/power/power_supply_class.html)