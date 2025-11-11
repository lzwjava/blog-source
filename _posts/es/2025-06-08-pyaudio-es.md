---
audio: false
generated: true
lang: es
layout: post
title: PortAudio y PyAudio
translated: true
type: note
---

El error ocurre porque **pyaudio** requiere los headers de desarrollo de PortAudio para compilar, los cuales faltan en tu sistema. Aquí se explica cómo solucionarlo:

### Solución Paso a Paso:

1. **Instalar los Headers de Desarrollo de PortAudio** (requeridos para pyaudio):
```bash
sudo apt update && sudo apt install portaudio19-dev
```

2. **Instalar las Herramientas de Desarrollo de Python** (si aún no están instaladas):
```bash
sudo apt install python3-dev
```

3. **Reintentar la Instalación**:
```bash
pip install -r requirements.local.txt
```

### Si Todavía Encuentras Problemas con pycrypto:
El paquete pycrypto está obsoleto y puede tener problemas de compatibilidad. Reemplázalo con **pycryptodome** modificando tu `requirements.local.txt`:

1. Abre el archivo de requisitos:
```bash
nano requirements.local.txt
```

2. Reemplaza `pycrypto` con:
```
pycryptodome
```

3. Guarda y vuelve a ejecutar la instalación:
```bash
pip install -r requirements.local.txt
```

### Por Qué Esto Funciona:
- `portaudio19-dev` proporciona los headers de PortAudio que faltan y son necesarios para compilar pyaudio
- `python3-dev` incluye los headers de desarrollo de Python necesarios
- `pycryptodome` es un reemplazo mantenido y compatible para el obsoleto pycrypto

### Alternativa para pycrypto (si debes mantenerlo):
Si específicamente necesitas pycrypto, instala primero las dependencias de compilación:
```bash
sudo apt install build-essential libgmp-dev
pip install pycrypto
```
Pero ten en cuenta que pycrypto tiene problemas de compatibilidad con versiones más recientes de Python.

Después de estos pasos, todos los paquetes deberían instalarse correctamente. Las advertencias de DEPRECATION sobre compilaciones legacy son informativas y no impedirán la instalación - indican que los paquetes necesitarán migración a compilaciones PEP 517 en el futuro.