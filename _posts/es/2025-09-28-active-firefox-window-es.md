---
audio: false
generated: true
image: false
lang: es
layout: post
model: anthropic/claude-sonnet-4
title: Script de Identificación de Ventanas Activas de Firefox
translated: true
type: note
---

```python
#!/usr/bin/env python3
import gi
gi.require_version('Wnck', '3.0')
from gi.repository import Wnck

def obtener_ventanas_firefox():
    pantalla = Wnck.Screen.get_default()
    pantalla.force_update()
    
    ventanas_firefox = []
    for ventana in pantalla.get_windows():
        if ventana.get_application():
            nombre_app = ventana.get_application().get_name().lower()
            nombre_ventana = ventana.get_name()
            
            if 'firefox' in nombre_app or 'firefox' in nombre_ventana.lower():
                ventanas_firefox.append({
                    'titulo': nombre_ventana,
                    'nombre_app': nombre_app,
                    'esta_activa': ventana.is_active(),
                    'pid': ventana.get_pid()
                })
    
    return ventanas_firefox

# Obtener ventana activa de Firefox
ventanas = obtener_ventanas_firefox()
firefox_activo = [v for v in ventanas if v['esta_activa']]
print("Ventana activa de Firefox:", firefox_activo)
```