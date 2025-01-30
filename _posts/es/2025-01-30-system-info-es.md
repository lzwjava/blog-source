---
audio: false
lang: es
layout: post
title: Información del sistema en macOS
translated: true
---

Para obtener información del sistema en tu macOS, puedes usar varias herramientas y comandos integrados. Aquí tienes algunos métodos para obtener diferentes tipos de información del sistema:

### 1. **Utilidad de Información del Sistema**
La aplicación Información del Sistema proporciona una visión general completa del hardware y software de tu Mac.

- Abre **Búsqueda de Spotlight** presionando `Cmd + Space` y escribe "Información del Sistema", luego presiona Enter.
- Alternativamente, puedes abrirla desde el **menú de Apple** > **Acerca de este Mac** > **Informe del Sistema**.

### 2. **Acerca de este Mac**
Esto proporciona una visión general rápida de las especificaciones de tu Mac.

- Haz clic en el **menú de Apple** en la esquina superior izquierda de la pantalla.
- Selecciona **Acerca de este Mac**. Esto mostrará información básica como la versión de macOS, el procesador, la memoria y el número de serie.

### 3. **Comandos de Terminal**
Puedes usar el Terminal para obtener información detallada del sistema utilizando diversos comandos.

- Abre **Terminal** desde `Aplicaciones` > `Utilidades` > `Terminal` o buscándolo en Spotlight.

#### Información Básica del Sistema
```sh
system_profiler SPHardwareDataType
```

#### Información Detallada del Sistema
```sh
system_profiler
```

#### Información del CPU
```sh
sysctl -n machdep.cpu.brand_string
```

#### Información de Memoria
```sh
sysctl hw.memsize
```

#### Uso de Disco
```sh
df -h
```

#### Información de Red
```sh
ifconfig
```

#### Información de la Batería (para laptops)
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

#### Lista de Paquetes Instalados de Brew
```sh
brew list
```

#### Lista de Paquetes Instalados de Pip
```sh
pip list
```

#### Lista de Paquetes Instalados de Gem
```sh
gem list
```

### 4. **Monitor de Actividad**
Esta aplicación proporciona información en tiempo real sobre el uso de CPU, memoria, energía, disco y red de tu Mac.

- Abre **Monitor de Actividad** desde `Aplicaciones` > `Utilidades` > `Monitor de Actividad` o buscándolo en Spotlight.

### 5. **Utilidad de Discos**
Esta aplicación proporciona información sobre tus dispositivos de almacenamiento.

- Abre **Utilidad de Discos** desde `Aplicaciones` > `Utilidades` > `Utilidad de Discos` o buscándolo en Spotlight.

### 6. **Herramientas de Terceros**
También hay aplicaciones de terceros como **iStat Menus** y **CoconutBattery** que proporcionan información detallada y capacidades de monitoreo del sistema.

Usando estos métodos, puedes recopilar una amplia gama de información del sistema en tu macOS.