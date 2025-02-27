---
audio: true
lang: es
layout: post
title: Información del sistema en macOS
translated: true
---

Para obtener información del sistema en tu macOS, puedes usar varias herramientas y comandos integrados. Aquí tienes algunos métodos para obtener diversos tipos de información del sistema:

### 1. **Utilidad de Información del Sistema**
La aplicación Información del Sistema proporciona una visión general completa del hardware y software de tu Mac.

- Abre **Búsqueda de Spotlight** presionando `Cmd + Space` y escribe "Información del Sistema", luego presiona Enter.
- Alternativamente, puedes abrirla desde el **menú Apple** > **Acerca de este Mac** > **Información del Sistema**.

### 2. **Acerca de este Mac**
Esto proporciona una visión general rápida de las especificaciones de tu Mac.

- Haz clic en el **menú Apple** en la esquina superior izquierda de la pantalla.
- Selecciona **Acerca de este Mac**. Esto mostrará información básica como la versión de macOS, el procesador, la memoria y el número de serie.

### 3. **Comandos de Terminal**
Puedes usar el Terminal para obtener información detallada del sistema utilizando varios comandos.

- Abre **Terminal** desde `Aplicaciones` > `Utilidades` > `Terminal` o buscándolo en Spotlight.

#### Información Básica del Sistema
```sh
system_profiler SPHardwareDataType
```

#### Información Detallada del Sistema
```sh
system_profiler
```

#### Información de la CPU
```sh
sysctl -n machdep.cpu.brand_string
```

#### Información de la Memoria
```sh
sysctl hw.memsize
```

#### Uso del Disco
```sh
df -h
```

#### Información de la Red
```sh
ifconfig
```

#### Información de la Batería (para portátiles)
```sh
pmset -g batt
```

#### Lista de Software Instalado
```sh
ls /Applications
```

#### Versión de macOS
```sh
sw_vers
```

#### Información del Usuario
```sh
id
```

#### Lista de Procesos en Ejecución
```sh
ps aux
```

#### Lista de Paquetes de Brew Instalados
```sh
brew list
```

#### Lista de Paquetes de Pip Instalados
```sh
pip list
```

#### Lista de Paquetes de Gem Instalados
```sh
gem list
```

### 4. **Monitor de Actividad**
Esta aplicación proporciona información en tiempo real sobre el uso de la CPU, memoria, energía, disco y red de tu Mac.

- Abre **Monitor de Actividad** desde `Aplicaciones` > `Utilidades` > `Monitor de Actividad` o buscándolo en Spotlight.

### 5. **Utilidad de Disco**
Esta aplicación proporciona información sobre tus dispositivos de almacenamiento.

- Abre **Utilidad de Disco** desde `Aplicaciones` > `Utilidades` > `Utilidad de Disco` o buscándolo en Spotlight.

### 6. **Herramientas de Terceros**
También hay aplicaciones de terceros como **iStat Menus** y **CoconutBattery** que proporcionan información detallada del sistema y capacidades de monitoreo.

Usando estos métodos, puedes recopilar una amplia gama de información del sistema en tu macOS.