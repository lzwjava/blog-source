---
layout: post  
title: "Pixel's USB Options"  
---

<div style="text-align: center;">  
    <img class="responsive" src="/assets/images/pixel/pixel.jpg" alt="Pixel" width="50%" />  
</div>

Pixel offers several USB options, and one particularly interesting feature is its ability to function as a webcam. On macOS, QuickTime can access the Android webcam as a video source, providing a simple and effective solution.

To set this up:  

1. Navigate to About Phone in the settings and tap Build Number seven times to enable Developer Mode.  
2. Open Developer Options and enable USB Debugging.  
3. Connect your Pixel to your computer via USB and run the following command in a terminal to verify the connection:  
   ```bash
   adb devices
   ```  