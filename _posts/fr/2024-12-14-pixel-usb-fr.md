---
audio: false
generated: false
lang: fr
layout: post
title: Options USB de Pixel
translated: true
---

<div style="text-align: center;">  
    <img class="responsive" src="/assets/images/pixel/pixel.jpg" alt="Pixel" width="50%" />  
</div>

Pixel propose plusieurs options USB, et une fonctionnalité particulièrement intéressante est sa capacité à fonctionner comme une webcam. Sur macOS, QuickTime peut accéder à la webcam Android comme source vidéo, offrant ainsi une solution simple et efficace.

Pour configurer cela :

1. Accédez à "À propos du téléphone" dans les paramètres et appuyez sept fois sur "Numéro de build" pour activer le mode Développeur.  
2. Ouvrez les "Options pour développeurs" et activez le "Débogage USB".  
3. Connectez votre Pixel à votre ordinateur via USB et exécutez la commande suivante dans un terminal pour vérifier la connexion :  
   ```bash
   adb devices
   ```