---
audio: false
generated: true
image: false
lang: fr
layout: post
model: anthropic/claude-sonnet-4
title: Script d'identification de fenêtre Firefox active
translated: true
type: note
---

```python
#!/usr/bin/env python3
import gi
gi.require_version('Wnck', '3.0')
from gi.repository import Wnck

def obtenir_fenetres_firefox():
    screen = Wnck.Screen.get_default()
    screen.force_update()
    
    fenetres_firefox = []
    for window in screen.get_windows():
        if window.get_application():
            app_name = window.get_application().get_name().lower()
            window_name = window.get_name()
            
            if 'firefox' in app_name or 'firefox' in window_name.lower():
                fenetres_firefox.append({
                    'title': window_name,
                    'app_name': app_name,
                    'is_active': window.is_active(),
                    'pid': window.get_pid()
                })
    
    return fenetres_firefox

# Obtenir la fenêtre Firefox active
windows = obtenir_fenetres_firefox()
active_firefox = [w for w in windows if w['is_active']]
print("Fenêtre Firefox active :", active_firefox)
```