---
audio: false
generated: true
image: false
lang: es
layout: post
model: anthropic/claude-sonnet-4
title: Guía de Automatización en Línea de Comandos de Xdotool
translated: true
type: note
---

## ¿Qué es xdotool?

xdotool es una herramienta de automatización de línea de comandos para X11 (entornos de escritorio Linux) que te permite:
- Controlar movimientos y clics del ratón
- Enviar pulsaciones de teclas a aplicaciones
- Manipular ventanas (mover, redimensionar, enfocar)
- Buscar ventanas por varios criterios
- Automatizar interacciones del escritorio de forma programática

## Instalación

```bash
# Ubuntu/Debian
sudo apt install xdotool

# Fedora/RHEL/CentOS
sudo dnf install xdotool

# Arch Linux
sudo pacman -S xdotool

# Desde el código fuente
git clone https://github.com/jordansissel/xdotool
cd xdotool
make
sudo make install
```

## Comandos Principales

### Comandos de Información de Ventana

#### `getactivewindow`
Obtiene el ID de la ventana actualmente activa/enfocada.
```bash
xdotool getactivewindow
# Salida: 52428807 (ID de ventana)

# Obtener el título de la ventana activa
xdotool getactivewindow getwindowname
```

#### `getwindowfocus`
Similar a getactivewindow pero puede comportarse diferente en algunos gestores de ventanas.
```bash
xdotool getwindowfocus
```

#### `getwindowname`
Obtiene el título/nombre de una ventana.
```bash
# Obtener nombre de la ventana activa
xdotool getactivewindow getwindowname

# Obtener nombre de un ID de ventana específico
xdotool getwindowname 52428807
```

#### `getwindowpid`
Obtiene el ID de proceso (PID) asociado con una ventana.
```bash
xdotool getactivewindow getwindowpid
```

#### `getwindowgeometry`
Obtiene información de posición y tamaño de una ventana.
```bash
xdotool getactivewindow getwindowgeometry
# Salida: Window 52428807
#   Position: 100,50 (screen: 0)
#   Geometry: 800x600
```

#### `getdisplaygeometry`
Obtiene las dimensiones de la pantalla/monitor.
```bash
xdotool getdisplaygeometry
# Salida: 1920x1080
```

### Búsqueda y Selección de Ventanas

#### `search`
Buscar ventanas por varios criterios.
```bash
# Buscar por nombre/título de ventana
xdotool search --name "Firefox"
xdotool search --name "Terminal"

# Buscar por nombre de clase
xdotool search --class "firefox"

# Búsqueda sin distinguir mayúsculas/minúsculas
xdotool search --name --onlyvisible --maxdepth 1 "terminal"

# Opciones comunes de búsqueda:
# --name: buscar títulos de ventanas
# --class: buscar nombres de clase de ventanas
# --classname: buscar nombres de instancia de clase de ventanas
# --onlyvisible: solo ventanas visibles
# --maxdepth N: limitar profundidad de búsqueda
# --limit N: limitar número de resultados
# --desktop N: buscar escritorio/área de trabajo específica
```

#### `selectwindow`
Selección interactiva de ventanas (hacer clic para seleccionar).
```bash
xdotool selectwindow
# Haz clic en cualquier ventana para obtener su ID
```

### Control del Ratón

#### `click`
Simular clics del ratón.
```bash
# Clic izquierdo en la posición actual
xdotool click 1

# Clic derecho
xdotool click 3

# Clic central
xdotool click 2

# Doble clic
xdotool click --repeat 2 1

# Clic en coordenadas específicas
xdotool mousemove 500 300 click 1

# Clic con retraso
xdotool click --delay 500 1
```

#### `getmouselocation`
Obtener la posición actual del cursor del ratón.
```bash
xdotool getmouselocation
# Salida: x:500 y:300 screen:0 window:52428807

# Obtener solo coordenadas
xdotool getmouselocation --shell
# Salida: X=500 Y=300 SCREEN=0 WINDOW=52428807
```

#### Movimiento del Ratón
```bash
# Mover ratón a posición absoluta
xdotool mousemove 500 300

# Mover ratón relativo a la posición actual
xdotool mousemove_relative 10 -20

# Mover y hacer clic en un comando
xdotool mousemove 500 300 click 1
```

### Entrada de Teclado

#### `key`
Enviar pulsaciones de teclas a la ventana activa.
```bash
# Enviar tecla única
xdotool key Return
xdotool key Escape
xdotool key Tab

# Enviar combinaciones de teclas
xdotool key ctrl+c
xdotool key ctrl+alt+t
xdotool key shift+F10

# Enviar múltiples teclas en secuencia
xdotool key ctrl+l type "https://google.com" key Return

# Nombres de teclas comunes:
# - Letras: a, b, c, ... (minúsculas)
# - Números: 1, 2, 3, ...
# - Especiales: Return, Escape, Tab, space, BackSpace, Delete
# - Función: F1, F2, ... F12
# - Modificadores: ctrl, alt, shift, super (tecla Windows)
# - Flechas: Up, Down, Left, Right
```

#### Entrada de Texto
```bash
# Escribir texto (simula escribir cada carácter)
xdotool type "Hello World"

# Escribir con retraso entre caracteres
xdotool type --delay 100 "Slow typing"

# Limpiar retraso para escritura rápida
xdotool type --clearmodifiers --delay 0 "Fast text"
```

### Manipulación de Ventanas

```bash
# Enfocar/activar una ventana
xdotool windowactivate WINDOW_ID

# Minimizar ventana
xdotool windowminimize WINDOW_ID

# Maximizar ventana
xdotool windowmaximize WINDOW_ID

# Cerrar ventana
xdotool windowclose WINDOW_ID

# Mover ventana a posición
xdotool windowmove WINDOW_ID 100 50

# Redimensionar ventana
xdotool windowsize WINDOW_ID 800 600

# Mover ventana a escritorio específico
xdotool set_desktop_for_window WINDOW_ID 2

# Elevar ventana al frente
xdotool windowraise WINDOW_ID

# Mostrar ventana
xdotool windowmap WINDOW_ID

# Ocultar ventana
xdotool windowunmap WINDOW_ID
```

### Características Avanzadas

#### `behave`
Configurar comportamientos de eventos de ventana (disparadores).
```bash
# Ejecutar comando cuando la ventana gana foco
xdotool behave WINDOW_ID focus exec echo "Window focused"

# Ejecutar cuando se crea la ventana
xdotool behave WINDOW_ID create exec "notify-send 'New window'"

# Eventos disponibles: focus, unfocus, mouse-enter, mouse-leave, create, destroy
```

#### `behave_screen_edge`
Disparar acciones cuando el ratón alcanza los bordes de la pantalla.
```bash
# Ejecutar comando cuando el ratón toca el borde izquierdo
xdotool behave_screen_edge left exec "echo 'Left edge hit'"

# Bordes disponibles: left, right, top, bottom
```

## Ejemplos Prácticos

### Scripts Básicos de Automatización

#### Abrir Terminal y Ejecutar Comando
```bash
#!/bin/bash
# Abrir terminal y ejecutar comando ls
xdotool key ctrl+alt+t
sleep 1
xdotool type "ls -la"
xdotool key Return
```

#### Capturar Ventana Activa
```bash
#!/bin/bash
WINDOW=$(xdotool getactivewindow)
NAME=$(xdotool getwindowname $WINDOW | sed 's/[^a-zA-Z0-9]/_/g')
import -window $WINDOW "screenshot_${NAME}.png"
```

#### Enfocar Aplicación Específica
```bash
#!/bin/bash
# Enfocar Firefox o abrir si no está ejecutándose
WINDOW=$(xdotool search --onlyvisible --class "firefox" | head -1)
if [ -n "$WINDOW" ]; then
    xdotool windowactivate $WINDOW
else
    firefox &
fi
```

### Scripts de Gestión de Ventanas

#### Organizar Ventanas una al Lado de la Otra
```bash
#!/bin/bash
# Obtener geometría de la pantalla
eval $(xdotool getdisplaygeometry --shell)
HALF_WIDTH=$((WIDTH / 2))

# Obtener dos ventanas más recientes
WINDOWS=($(xdotool search --onlyvisible --maxdepth 1 "" | tail -2))

# Posicionar primera ventana a la izquierda
xdotool windowsize ${WINDOWS[0]} $HALF_WIDTH $HEIGHT
xdotool windowmove ${WINDOWS[0]} 0 0

# Posicionar segunda ventana a la derecha
xdotool windowsize ${WINDOWS[1]} $HALF_WIDTH $HEIGHT
xdotool windowmove ${WINDOWS[1]} $HALF_WIDTH 0
```

#### Centrar Ventana Activa
```bash
#!/bin/bash
WINDOW=$(xdotool getactivewindow)
eval $(xdotool getdisplaygeometry --shell)
eval $(xdotool getwindowgeometry --shell $WINDOW)

NEW_X=$(((WIDTH - WINDOW_WIDTH) / 2))
NEW_Y=$(((HEIGHT - WINDOW_HEIGHT) / 2))

xdotool windowmove $WINDOW $NEW_X $NEW_Y
```

### Automatización Específica de Aplicaciones

#### Automatización del Navegador
```bash
#!/bin/bash
# Abrir nueva pestaña y navegar
xdotool key ctrl+t
sleep 0.5
xdotool type "github.com"
xdotool key Return
```

#### Automatización del Editor de Texto
```bash
#!/bin/bash
# Seleccionar todo y copiar al portapapeles
xdotool key ctrl+a
sleep 0.1
xdotool key ctrl+c
```

## Consejos y Mejores Prácticas

### Temporización y Retrasos
```bash
# Añadir retrasos para aplicaciones lentas
xdotool key ctrl+alt+t
sleep 2  # Esperar a que se abra la terminal
xdotool type "echo hello"

# Usar retrasos incorporados de xdotool
xdotool key --delay 100 ctrl+alt+t
```

### Manejo de Errores
```bash
#!/bin/bash
# Verificar si la ventana existe antes de actuar sobre ella
WINDOW=$(xdotool search --name "MyApp" 2>/dev/null)
if [ -n "$WINDOW" ]; then
    xdotool windowactivate $WINDOW
else
    echo "Window not found"
    exit 1
fi
```

### Trabajar con Múltiples Ventanas
```bash
#!/bin/bash
# Actuar sobre todas las ventanas de una aplicación específica
xdotool search --name "Firefox" | while read WINDOW; do
    xdotool windowactivate $WINDOW
    xdotool key F5  # Actualizar
    sleep 0.5
done
```

### Depuración
```bash
# Habilitar salida detallada
xdotool --verbose key Return

# Obtener información detallada de ventana
xdotool search --name "Terminal" getwindowgeometry getwindowname getwindowpid
```

## Casos de Uso Comunes

1. **Gestión de Ventanas**: Enfocar, mover, redimensionar ventanas programáticamente
2. **Pruebas de Aplicaciones**: Automatizar escenarios de prueba de GUI
3. **Herramientas de Presentación**: Automatizar navegación de diapositivas y cambio de ventanas
4. **Macros para Juegos**: Automatizar tareas repetitivas en juegos
5. **Accesibilidad**: Crear métodos de entrada personalizados para usuarios con discapacidades
6. **Administración de Sistemas**: Automatizar tareas administrativas basadas en GUI
7. **Herramientas de Desarrollo**: Integrar con IDEs y flujos de trabajo de desarrollo

## Resolución de Problemas

### Problemas Comunes

- **Comandos no funcionan**: Asegurarse de que X11 esté ejecutándose (no Wayland)
- **Problemas de permisos**: Algunas operaciones pueden requerir permisos de usuario apropiados
- **Ventana no encontrada**: Usar `xdotool search` para verificar que la ventana existe y es visible
- **Problemas de temporización**: Añadir retrasos apropiados entre comandos
- **Caracteres especiales**: Usar escape apropiado para caracteres especiales en entrada de texto

### Consideraciones de Seguridad

- xdotool puede controlar cualquier aplicación, usar con precaución
- Evitar ejecutar scripts xdotool no confiables
- Tener cuidado con la automatización que maneja datos sensibles
- Considerar usar `xdotool` solo en entornos controlados

Esta guía cubre las características esenciales y avanzadas de xdotool. Experimenta con estos comandos para crear potentes scripts de automatización del escritorio adaptados a tus necesidades específicas.