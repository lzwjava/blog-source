---
audio: false
generated: true
lang: es
layout: post
title: Copiar Archivos con Estructura de Directorios
translated: true
type: note
---

Dada la salida de tu comando `find`, quieres copiar todos los archivos `.log` a `/Users/lzwjava/projects/logs` preservando su estructura de directorios. Por ejemplo, un archivo como `./CoreSimulator/FC275C39-59CC-4483-A64E-5D459D7A1D57/system.log` debería terminar como `/Users/lzwjava/projects/logs/CoreSimulator/FC275C39-59CC-4483-A64E-5D459D7A1D57/system.log`. Te mostraré cómo lograr esto usando `find` combinado con `cp` o `rsync`, asegurando que se mantenga la jerarquía de directorios.

---

### **Solución 1: Usar `find` con `cp`**
Puedes usar `find` para localizar los archivos `.log` y `cp` con la opción `--parents` para copiarlos preservando su estructura de directorios.

#### **Comando**
```bash
find . -name "*.log" -exec cp --parents {} /Users/lzwjava/projects/logs \;
```

#### **Explicación**
- **`find . -name "*.log"`**: Localiza todos los archivos `.log` en el directorio actual y subdirectorios (como en tu ejemplo).
- **`-exec cp --parents {} /Users/lzwjava/projects/logs \;`**:
  - `cp --parents`: Copia el archivo y recrea su ruta de directorio relativa al origen (`.`).
  - `{}`: Marcador de posición para cada archivo encontrado por `find`.
  - `/Users/lzwjava/projects/logs`: Directorio de destino.
  - `\;`: Termina el comando `-exec`.

#### **Resultado**
- `./CoreSimulator/FC275C39-59CC-4483-A64E-5D459D7A1D57/system.log` → `/Users/lzwjava/projects/logs/CoreSimulator/FC275C39-59CC-4483-A64E-5D459D7A1D57/system.log`
- La estructura de directorios bajo `CoreSimulator` se preserva.

#### **Antes de Ejecutar**
- Asegúrate de que `/Users/lzwjava/projects/logs` existe:
  ```bash
  mkdir -p /Users/lzwjava/projects/logs
  ```

---

### **Solución 2: Usar `rsync`**
`rsync` es otra herramienta potente que puede copiar archivos preservando la estructura de directorios, y a menudo es más eficiente para operaciones masivas.

#### **Comando**
```bash
find . -name "*.log" -exec rsync -R -a {} /Users/lzwjava/projects/logs \;
```

#### **Explicación**
- **`-R`**: Usa rutas relativas, preservando la estructura de directorios desde el origen (`.`).
- **`-a`**: Modo archivo (preserva marcas de tiempo, permisos, etc.).
- `{}`: Cada archivo `.log` encontrado.
- `/Users/lzwjava/projects/logs`: Directorio objetivo.

#### **Resultado**
Igual que antes: los archivos se copian con sus rutas relativas completas intactas.

#### **Antes de Ejecutar**
- Crea el directorio de destino si no existe:
  ```bash
  mkdir -p /Users/lzwjava/projects/logs
  ```

---

### **Verificando la Copia**
Después de ejecutar cualquiera de los comandos, verifica el destino:
```bash
ls -R /Users/lzwjava/projects/logs
```
Deberías ver:
```
/Users/lzwjava/projects/logs:
CoreSimulator

/Users/lzwjava/projects/logs/CoreSimulator:
CoreSimulator.log  FC275C39-59CC-4483-A64E-5D459D7A1D57  Simulator.log

/Users/lzwjava/projects/logs/CoreSimulator/FC275C39-59CC-4483-A64E-5D459D7A1D57:
com.apple.itunesstored  system.log

/Users/lzwjava/projects/logs/CoreSimulator/FC275C39-59CC-4483-A64E-5D459D7A1D57/com.apple.itunesstored:
itunesstored.log
```

---

### **Notas Clave**
- **Permisos:** Asegúrate de tener acceso de escritura a `/Users/lzwjava/projects/logs`. Si no, usa `sudo` (ej., `sudo cp ...`) o ajusta los permisos:
  ```bash
  chmod -R u+w /Users/lzwjava/projects/logs
  ```
- **Sobrescribir:** Si los archivos ya existen en el destino:
  - `cp` sobrescribirá sin advertencia.
  - `rsync -a` también sobrescribirá, pero puedes añadir `--ignore-existing` para omitir archivos existentes:
    ```bash
    find . -name "*.log" -exec rsync -R -a --ignore-existing {} /Users/lzwjava/projects/logs \;
    ```
- **Prueba en Seco (Probar Primero):**
  - Para `cp`, añade `echo` para previsualizar:
    ```bash
    find . -name "*.log" -exec echo cp --parents {} /Users/lzwjava/projects/logs \;
    ```
  - Para `rsync`, usa `--dry-run`:
    ```bash
    find . -name "*.log" -exec rsync -R -a --dry-run {} /Users/lzwjava/projects/logs \;
    ```

---

### **¿Cuál Elegir?**
- **`cp`**: Más simple, no necesita herramientas extra (disponible en todos los sistemas tipo Unix).
- **`rsync`**: Más flexible (ej., para sincronizar, omitir duplicados), pero requiere que `rsync` esté instalado (estándar en la mayoría de sistemas).

Ambos funcionarán para tu caso. Recomiendo empezar con `cp --parents` por simplicidad.

---

### **Comando Final (Recomendado)**
```bash
mkdir -p /Users/lzwjava/projects/logs
find . -name "*.log" -exec cp --parents {} /Users/lzwjava/projects/logs \;
```

Ejecuta esto desde tu directorio `Logs` (`lzwjava@anonymous Logs %`), ¡y listo! Avísame si encuentras algún problema o quieres ajustar el comportamiento (ej., aplanar la estructura en lugar de preservarla).