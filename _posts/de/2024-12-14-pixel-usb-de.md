---
audio: false
generated: false
image: true
lang: de
layout: post
title: Pixel's USB-Optionen
translated: true
---

<div style="text-align: center;">  
    <img class="responsive" src="/assets/images/pixel/pixel.jpg" alt="Pixel" width="50%" />  
</div>

Pixel bietet mehrere USB-Optionen, und eine besonders interessante Funktion ist seine Fähigkeit, als Webcam zu fungieren. Auf macOS kann QuickTime die Android-Webcam als Videoquelle nutzen, was eine einfache und effektive Lösung bietet.

Um dies einzurichten:

1. Navigieren Sie in den Einstellungen zu „Über das Telefon“ und tippen Sie sieben Mal auf die Build-Nummer, um den Entwicklermodus zu aktivieren.  
2. Öffnen Sie die Entwickleroptionen und aktivieren Sie USB-Debugging.  
3. Verbinden Sie Ihr Pixel über USB mit Ihrem Computer und führen Sie den folgenden Befehl in einem Terminal aus, um die Verbindung zu überprüfen:  
   ```bash
   adb devices
   ```