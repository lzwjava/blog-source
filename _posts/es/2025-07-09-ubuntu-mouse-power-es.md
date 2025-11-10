---
audio: false
generated: true
lang: es
layout: post
title: Gestión de Batería del Ratón en Ubuntu
translated: true
type: note
---

Ubuntu tiene varias funciones integradas que ayudan a gestionar la energía del ratón y proporcionan notificaciones de batería baja:

## Gestión de Energía del Ratón en Ubuntu

**Monitorización de la Batería:**
- El sistema de gestión de energía de Ubuntu monitoriza los niveles de la batería del ratón inalámbrico a través de conexiones Bluetooth o por receptor USB
- El sistema lee los datos de la batería del firmware del ratón cuando están disponibles
- Las notificaciones de energía aparecen en la bandeja del sistema cuando la batería cae por debajo de ciertos umbrales (normalmente alrededor del 20% y 10%)

**Cómo Funciona el Sistema de Notificaciones:**
- **Demonio UPower** - Monitoriza los estados de energía de los dispositivos conectados, incluidos los ratones inalámbricos
- **GNOME Power Manager** - Maneja las notificaciones reales y los ajustes de energía
- **Pila Bluetooth** - Para ratones Bluetooth, la información de la batería se transmite a través de protocolos Bluetooth estándar
- **USB HID** - Para ratones inalámbricos con dongles USB, los datos de la batería llegan a través de informes HID (Human Interface Device)

**Características de Ahorro de Energía:**
- Modo de suspensión automático del ratón cuando está inactivo
- Tasas de sondeo reducidas durante periodos de baja actividad
- Ajustes de tiempo de espera de conexión para preservar la batería
- Opción para desactivar el despertar del ratón desde el modo de suspensión

**Comprobación de la Batería del Ratón:**
Puedes comprobar el estado de la batería del ratón a través de:
- Configuración del Sistema → Energía (muestra los dispositivos conectados)
- Línea de comandos: `upower -i /org/freedesktop/UPower/devices/mouse_*`
- Indicador de batería en el panel superior (si el ratón lo admite)

El sistema funciona sondeando constantemente los dispositivos conectados para conocer su estado de energía y utilizando servicios de notificación del escritorio para alertar a los usuarios cuando se necesita intervención. Esto ayuda a prevenir desconexiones inesperadas durante trabajos importantes.