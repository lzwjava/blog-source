---
audio: false
generated: true
lang: fr
layout: post
title: Connexion d'un iPad à un moniteur HDMI
translated: true
type: note
---

Pour connecter votre iPad à un moniteur en utilisant HDMI et l'utiliser pour regarder des films (par exemple, en streamant depuis le serveur Nginx de votre ordinateur portable Ubuntu avec une application comme Infuse), vous aurez besoin du bon adaptateur et d'une configuration simple. Les iPad n'ont pas de port HDMI natif, mais Apple propose des adaptateurs officiels, et il existe aussi des options tierces. Voici comment procéder étape par étape, adapté à votre objectif de regarder des films sans tracas sur votre moniteur.

### Ce dont vous aurez besoin
1.  **iPad avec port Lightning ou USB-C**
    *   Vérifiez le modèle de votre iPad : Les anciens iPad (par exemple, iPad Air 2, iPad Mini 4) utilisent des ports Lightning, tandis que les modèles plus récents (par exemple, iPad Pro 2018+, iPad Air 4ème génération+) utilisent l'USB-C.
    *   Vous n'avez pas spécifié votre modèle d'iPad, je vais donc couvrir les deux possibilités.

2.  **Adaptateur HDMI**
    *   Pour les **iPad Lightning** : L'**Adaptateur Lightning vers HDMI** d'Apple (officiellement "Lightning Digital AV Adapter", ~49 $ USD).
    *   Pour les **iPad USB-C** : L'**Adaptateur Multiport AV Numérique USB-C** d'Apple (~69 $ USD) ou un adaptateur USB-C vers HDMI tiers (assurez-vous qu'il prend en charge la sortie vidéo, ~15-30 $ USD).
    *   Les adaptateurs tiers fonctionnent mais peuvent ne pas prendre en charge toutes les fonctionnalités (comme le HDR ou les taux de rafraîchissement élevés) ; ceux d'Apple sont plus fiables pour le plug-and-play.

3.  **Câble HDMI**
    *   N'importe quel câble HDMI standard (par exemple, HDMI 2.0 pour la 4K, si votre moniteur et votre iPad le supportent). La longueur dépend de votre configuration - 1,5 à 3 mètres est typique pour les connexions à proximité.

4.  **Moniteur avec entrée HDMI**
    *   Vous en avez déjà un, assurez-vous qu'il est allumé et réglé sur la bonne entrée HDMI.

5.  **Optionnel : Source d'alimentation**
    *   Les adaptateurs Apple ont souvent un port supplémentaire (Lightning ou USB-C) pour la charge. Si vous regardez de longs métrages, connectez le chargeur de votre iPad pour le garder sous tension.

### Étapes pour connecter votre iPad au moniteur
1.  **Obtenez le bon adaptateur**
    *   iPad Lightning : Branchez l'Adaptateur Lightning Digital AV dans le port Lightning de votre iPad.
    *   iPad USB-C : Branchez l'Adaptateur Multiport AV Numérique USB-C (ou un adaptateur USB-C vers HDMI) dans le port USB-C de votre iPad.

2.  **Connectez le câble HDMI**
    *   Branchez une extrémité du câble HDMI dans le port HDMI de l'adaptateur.
    *   Branchez l'autre extrémité dans le port d'entrée HDMI de votre moniteur.

3.  **Alimentez (Optionnel)**
    *   Pour les longues sessions, connectez votre chargeur iPad au port supplémentaire de l'adaptateur (Lightning ou USB-C) et branchez-le sur une prise électrique. Cela évite la décharge de la batterie.

4.  **Allumez le moniteur**
    *   Allumez votre moniteur et utilisez son bouton d'entrée/source pour sélectionner le port HDMI auquel vous êtes connecté (par exemple, HDMI 1 ou HDMI 2).

5.  **Miroir l'écran de l'iPad**
    *   Une fois connecté, l'écran de votre iPad devrait automatiquement se refléter sur le moniteur. Vous verrez l'écran d'accueil de l'iPad sur le moniteur.
    *   S'il ne se reflète pas automatiquement :
        *   Faites un glissement vers le bas depuis le coin supérieur droit (sur les iPad avec Face ID) ou vers le haut depuis le bas (sur les anciens iPad avec bouton Home) pour ouvrir le **Centre de Contrôle**.
        *   Appuyez sur l'icône **Miroir l'écran** (deux rectangles qui se chevauchent).
        *   Sélectionnez l'adaptateur (il pourrait apparaître comme "Apple AV Adapter" ou similaire). Le miroir devrait commencer.

6.  **Ajustez les paramètres d'affichage (Optionnel)**
    *   Sur votre iPad, allez dans **Réglages > Affichage et Luminosité**.
        *   Si le moniteur prend en charge des résolutions plus élevées (par exemple, 1080p ou 4K), l'iPad s'ajuste automatiquement, mais vous pouvez modifier le zoom ou la luminosité ici.
        *   La plupart des contenus (comme les films) s'adapteront à l'aspect ratio du moniteur.

7.  **Lisez vos films**
    *   Ouvrez une application comme **Infuse** (ou n'importe quel lecteur vidéo) sur votre iPad.
    *   Si vous utilisez Infuse pour streamer depuis votre serveur Nginx Ubuntu :
        *   Configurez Infuse pour se connecter à votre serveur (par exemple, `http://<ip-ordinateur>:80/films`, où `<ip-ordinateur>` est l'adresse IP de votre machine Ubuntu, comme `192.168.1.100`).
        *   Sélectionnez un film, appuyez sur lecture, et il s'affichera sur le moniteur en plein écran.
    *   Faites pivoter votre iPad en mode paysage ou appuyez sur l'icône plein écran dans l'application pour une meilleure expérience de visionnage.

### Considérations audio
*   **Moniteur avec haut-parleurs** : L'audio devrait passer par les haut-parleurs du moniteur via HDMI (si pris en charge).
*   **Pas de haut-parleurs sur le moniteur** : Utilisez les haut-parleurs de l'iPad, ou connectez des écouteurs filaires au port Lightning/USB-C de l'adaptateur (peut nécessiter un dongle pour les prises jack 3,5mm) ou associez des écouteurs Bluetooth à l'iPad.

### Conseils pour votre configuration
*   **Prise en charge de la résolution** : Les adaptateurs Lightning prennent en charge jusqu'à 1080p ; les adaptateurs USB-C prennent en charge jusqu'à 4K (en fonction de votre iPad et de votre moniteur). Vérifiez la résolution maximale de votre moniteur et la qualité des fichiers vidéo.
*   **Contrôle** : Vous contrôlerez la lecture directement sur l'écran tactile de l'iPad. Comme Infuse n'offre pas de contrôle à distance sur le réseau (comme noté précédemment), vous devrez interagir avec l'iPad lui-même - gardez-le à proximité ou utilisez un support.
*   **Accès au serveur Nginx** : Assurez-vous que votre ordinateur portable Ubuntu et votre iPad sont sur le même réseau Wi-Fi. Testez le serveur Nginx en ouvrant un navigateur sur l'iPad et en accédant à `http://<ip-ordinateur>` - vous devriez voir vos fichiers de films s'ils sont correctement configurés.

### Dépannage
*   **Pas de vidéo** : Assurez-vous que toutes les connexions sont sécurisées, que le moniteur est sur la bonne entrée et que l'adaptateur est compatible (certains adaptateurs tiers bon marché peuvent échouer).
*   **Décalage ou saccades** : Si vous streamer depuis Nginx, vérifiez la force du signal Wi-Fi ou la taille du fichier vidéo - les gros fichiers 4K peuvent nécessiter une connexion plus forte.
*   **Barres noires** : Si le film ne remplit pas l'écran, c'est dû à des différences d'aspect ratio (par exemple, un film 16:9 sur un moniteur 4:3). Utilisez les options de zoom d'Infuse pour ajuster.

### Dernières réflexions
Cette configuration permet à votre iPad d'agir comme un appareil de lecture, streamant depuis votre ordinateur portable Ubuntu et sortant le signal vers le moniteur via HDMI. C'est simple une fois connecté - il suffit de brancher, de sélectionner votre film dans Infuse et de regarder. Comme vous vouliez un minimum de tracas et pas de périphériques supplémentaires comme une Fire TV Stick, cela utilise efficacement votre iPad et votre moniteur existants. Si votre iPad est ancien ou manque de stockage pour les métadonnées d'Infuse, le streaming direct depuis Nginx garde tout léger. Profitez bien de vos films !