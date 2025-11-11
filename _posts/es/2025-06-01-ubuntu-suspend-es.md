---
audio: false
generated: true
lang: es
layout: post
title: Guía de Suspensión de Ubuntu
translated: true
type: note
---

En Ubuntu, puedes poner tu sistema en suspensión o hibernación usando varios métodos:

## Métodos Gráficos:
- **Esquina superior derecha**: Haz clic en el icono de encendido/ajustes en el panel superior, luego selecciona "Suspender" o "Hibernar" si está disponible
- **Menú de Actividades**: Presiona la tecla Super, escribe "power" o "suspend", y selecciona las opciones de energía

## Métodos de Línea de Comandos:
```bash
# Para suspender
systemctl suspend

# Para hibernar
systemctl hibernate

# Para suspensión híbrida (combinación de ambos)
systemctl hybrid-sleep
```

## Atajos de Teclado:
- Muchos sistemas Ubuntu usan **Fn + Tecla de suspensión** o **Ctrl + Alt + Fin** por defecto
- Puedes personalizarlos en Configuración > Teclado > Atajos

## Notas Importantes:
- **Suspensión/Suspender**: Mantiene la RAM encendida, despertado rápido pero consume algo de batería
- **Hibernación**: Guarda todo en el disco y se apaga, despertado más lento pero sin consumo de energía
- La hibernación podría no estar habilitada por defecto en versiones nuevas de Ubuntu debido a posibles problemas con algún hardware

Si la hibernación no funciona, puede que necesites habilitarla primero configurando el espacio de swap y editando la configuración del sistema. La suspensión debería funcionar inmediatamente en la mayoría de los sistemas.