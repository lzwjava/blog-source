---
audio: false
generated: false
image: false
lang: fr
layout: post
title: Configuration de streaming en direct avec OBS, SRS et FFmpeg
translated: true
---

*Cet article de blog a été rédigé avec l'assistance de ChatGPT-4o.*

---

La diffusion en direct est devenue une composante essentielle de la communication en ligne, avec des applications allant des émissions professionnelles aux blogs vidéo personnels. La mise en place d'une solution de diffusion en direct robuste nécessite une compréhension approfondie de divers outils et protocoles. Ce guide vous accompagnera étape par étape pour configurer une diffusion en direct en utilisant OBS, SRS et FFmpeg.

### Les composants clés du streaming en direct

**1. OBS（Open Broadcaster Software）**
OBS est un logiciel open source puissant utilisé pour l'enregistrement vidéo et le streaming en direct. Il offre des fonctionnalités de capture en temps réel de sources et de périphériques, de composition de scènes, d'encodage, d'enregistrement et de diffusion.

**2. SRS（Simple Realtime Server）**
SRS est un serveur de streaming haute performance prenant en charge RTMP, HLS et HTTP-FLV. Il supporte un grand nombre de connexions simultanées et est hautement configurable.

**3. FFmpeg**
FFmpeg est un cadre multimédia complet capable de décoder, encoder, transcoder, multiplexer, démultiplexer, diffuser, filtrer et lire presque tout ce qui est créé par les humains et les machines. Il est largement utilisé dans les configurations de streaming et est très apprécié pour sa polyvalence et sa fiabilité.

### Configuration de votre environnement de streaming en direct

#### Configuration d'OBS

1. **Installer OBS** : Téléchargez et installez OBS depuis le site officiel.
2. **Configurer les paramètres** : Ouvrez OBS, allez dans `Paramètres > Diffusion`, et configurez le type de diffusion sur `Personnalisé...`. Entrez l'URL de votre serveur de streaming (par exemple, `rtmp://votre_ip_serveur/live`).
3. **Ajouter des sources** : Ajoutez des sources vidéo et audio dans OBS pour créer une scène. Cela peut inclure la capture d'écran, une webcam, des images, du texte, etc.

#### Configuration du serveur SRS

1. **Installer SRS** : Clonez le dépôt SRS depuis GitHub et compilez-le pour prendre en charge SSL.
    ```sh
    git clone https://github.com/ossrs/srs.git
    cd srs/trunk
    ./configure --disable-all --with-ssl
    make
    ```
2. **Configurer SRS** : Modifiez le fichier `conf/rtmp.conf` pour configurer vos paramètres RTMP.
    ```sh
    listen 1935;
    max_connections 1000;
    vhost __defaultVhost__ { }
    ```
3. **Démarrer SRS** : Exécutez le serveur SRS avec votre fichier de configuration.
    ```sh
    ./objs/srs -c conf/rtmp.conf
    ```

#### Utilisation de FFmpeg pour le streaming

1. **Installer FFmpeg** : Installez FFmpeg depuis le site officiel ou via un gestionnaire de paquets.
2. **Utiliser FFmpeg pour la diffusion en continu** : Utilisez FFmpeg pour pousser un flux vidéo vers votre serveur SRS.
    ```sh
    ffmpeg -re -i input_video.flv -vcodec copy -acodec copy -f flv rtmp://your_server_ip/live/stream_key
    ```
3. **Automatiser la diffusion en continu** : Créez un script pour diffuser en continu des fichiers vidéo de manière continue.
    ```sh
    for ((;;)); do 
        ffmpeg -re -i input_video.flv -vcodec copy -acodec copy -f flv rtmp://your_server_ip/live/stream_key;
        sleep 1;
    done
    ```

### Protocoles et formats

**RTMP (Real-Time Messaging Protocol)**
- RTMP est largement utilisé pour la diffusion en direct en raison de sa faible latence et de sa transmission fiable.
- Il utilise TCP, ce qui permet de maintenir une connexion persistante, assurant ainsi une diffusion fluide.

**HLS (HTTP Live Streaming)**
- HLS divise le flux vidéo en petits segments basés sur HTTP, ce qui facilite la transmission via des serveurs web standard.
- Bien qu'il introduise une certaine latence, il est hautement compatible avec une variété d'appareils et de plateformes.

**HTTP-FLV**
- Combine le format FLV avec le transport HTTP pour une diffusion en continu à faible latence.
- Convient pour la diffusion en continu basée sur le navigateur, car il utilise l'infrastructure HTTP existante.

### Applications Pratiques

**Diffusion en continu sur iOS et Android**
- Utilisation de bibliothèques telles que VideoCore et Ijkplayer pour la diffusion RTMP sur les appareils mobiles.
- Intégration de FFmpeg pour les tâches d'encodage et de décodage afin d'améliorer la compatibilité et les performances.

**Diffusion en continu basée sur le Web**
- Utilisation de l'élément vidéo HTML5 pour la lecture de vidéos sur une page web, prenant en charge HLS ou HTTP-FLV.
- Exploitation de WebRTC pour la communication en temps réel et les interactions à faible latence.

### Outils et Ressources

- **VLC** : Un lecteur multimédia polyvalent prenant en charge les protocoles de streaming comme RTMP et HLS.
- **SRS Player** : Un lecteur en ligne pour tester les flux SRS.
- **Documentation FFmpeg** : Fournit une documentation détaillée pour diverses tâches multimédias.

### Conclusion

La mise en place d'une solution de streaming en direct fiable nécessite la compréhension et la configuration de plusieurs outils et protocoles. OBS, SRS et FFmpeg sont des composants puissants qui, combinés, permettent de créer une configuration de streaming robuste. Que ce soit pour iOS, Android ou le Web, ces outils offrent la flexibilité et les performances nécessaires pour réaliser des diffusions en direct de haute qualité.

Pour des informations plus détaillées et des configurations avancées, veuillez consulter la documentation officielle de chaque outil et explorer d'autres astuces et supports sur les forums communautaires. Bonne chance pour votre diffusion en direct !