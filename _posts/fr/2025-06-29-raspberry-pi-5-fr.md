---
audio: false
generated: true
lang: fr
layout: post
title: 'Raspberry Pi 5 : Puissant et Polyvalent'
translated: true
type: note
---

Le Raspberry Pi 5, sorti en octobre 2023 par la Raspberry Pi Foundation, est la dernière itération de la série populaire de nano-ordinateurs, conçue pour offrir haute performance, polyvalence et abordabilité aux amateurs, éducateurs et professionnels. S'appuyant sur le succès de ses prédécesseurs, le Raspberry Pi 5 introduit des améliorations significatives en matière de puissance de traitement, de connectivité et de fonctionnalités, le rendant adapté à un large éventail d'applications, des projets éducatifs à l'automatisation industrielle et aux tâches informatiques avancées. Voici une introduction complète au Raspberry Pi 5, couvrant son historique, ses spécifications, ses fonctionnalités, son installation, ses applications et plus encore.

---

### **Aperçu et Historique**
La série Raspberry Pi a commencé en 2012 avec pour mission de fournir une plateforme abordable et accessible pour apprendre la programmation et l'informatique. Initialement destiné aux étudiants et aux amateurs, le Raspberry Pi a rapidement gagné en popularité auprès des développeurs et des ingénieurs pour sa conception compacte, sa faible consommation d'énergie et sa polyvalence. Chaque itération a amélioré les performances et élargi les capacités, le Raspberry Pi 5 marquant un bond significatif par rapport au Raspberry Pi 4, sorti en 2019.

Le Raspberry Pi 5, annoncé le 28 septembre 2023 et disponible en précommande peu après, est le premier à intégrer une puce conçue en interne (le contrôleur E/S RP1) et introduit des fonctionnalités avancées comme le support PCIe pour des options de stockage plus rapides. Prizé à 60 $ pour le modèle 4 Go, 80 $ pour le modèle 8 Go, 50 $ pour le modèle 2 Go (introduit en août 2024) et 120 $ pour le modèle 16 Go (introduit en janvier 2025), il reste une solution informatique abordable mais puissante.[](https://www.raspberrypi.com/products/raspberry-pi-5/)[](https://www.raspberrypi.com/news/introducing-raspberry-pi-5/)

---

### **Spécifications Clés**
Le Raspberry Pi 5 est alimenté par un ensemble robuste de composants matériels, offrant une augmentation de performance de 2 à 3 fois par rapport au Raspberry Pi 4. Voici ses spécifications principales :

- **Processeur** : Broadcom BCM2712, un CPU quadricœur 64 bits ARM Cortex-A76 à 2,4 GHz avec des extensions de cryptographie, des caches L2 de 512 Ko par cœur et un cache L3 partagé de 2 Mo. Ce CPU est nettement plus rapide que le Cortex-A72 du Raspberry Pi 4, permettant de meilleures performances pour les tâches exigeantes comme l'informatique de bureau et l'émulation.[](https://www.raspberrypi.com/products/raspberry-pi-5/)[](https://www.zimaspace.com/blog/raspberry-pi-5-everything-you-need-to-know.html)
- **GPU** : GPU VideoCore VII, prenant en charge OpenGL ES 3.1 et Vulkan 1.2, capable de piloter deux écrans 4K à 60 Hz via des ports micro HDMI.[](https://www.linkedin.com/pulse/introduction-raspberry-pi-5-specs-harshvardhan-mishra-wkbmf)
- **RAM** : Disponible en variantes de 2 Go, 4 Go, 8 Go et 16 Go LPDDR4X-4267 SDRAM, offrant une bande passante mémoire plus rapide que le Raspberry Pi 4.[](https://wagnerstechtalk.com/rpi5/)[](https://www.raspberrypi.com/products/raspberry-pi-5/)
- **Stockage** :
  - Slot pour carte MicroSD avec support du mode haute vitesse SDR104 (recommandé : 32 Go ou plus pour Raspberry Pi OS, 16 Go pour Lite). Les capacités supérieures à 2 To ne sont pas prises en charge en raison des limitations MBR.
  - Interface PCIe pour les SSD NVMe M.2 via des HATs optionnels, permettant un démarrage et un transfert de données plus rapides.[](https://www.raspberrypi.com/documentation/computers/getting-started.html)[](https://www.raspberrypi.com/products/raspberry-pi-5/)
- **Connectivité** :
  - Wi-Fi double bande 2,4 GHz et 5 GHz 802.11ac.
  - Bluetooth 5.0 et Bluetooth Low Energy (BLE).
  - Ethernet Gigabit avec support Power over Ethernet (PoE) (nécessite un PoE+ HAT).
  - 2 ports USB 3.0 (fonctionnement simultané à 5 Gbps) et 2 ports USB 2.0.
  - Connecteur GPIO 40 broches pour l'interfaçage avec des capteurs, écrans et autres périphériques.
  - 2 ports micro HDMI pour une sortie double 4K@60Hz.
  - 2 transcepteurs MIPI caméra/display à 4 voies (interchangeables pour une caméra et un écran ou deux du même type).
  - Connecteur UART dédié pour le débogage (921 600 bps).[](https://www.linkedin.com/pulse/introduction-raspberry-pi-5-specs-harshvardhan-mishra-wkbmf)[](https://www.waveshare.com/wiki/Raspberry_Pi_5)
- **Alimentation** : Nécessite une alimentation USB-C 5V/5A (par exemple, l'Alimentation USB-C 27W Raspberry Pi). Des alimentations inadéquates peuvent causer une instabilité.[](https://www.raspberrypi.com/products/raspberry-pi-5/)
- **Horloge Temps Réel (RTC)** : RTC intégrée avec un connecteur pour batterie de secours (J5), éliminant le besoin de modules d'horloge externes lorsqu'elle est hors tension.[](https://en.wikipedia.org/wiki/Raspberry_Pi)
- **Autres Fonctionnalités** :
  - Contrôleur E/S RP1, une puce personnalisée conçue par Raspberry Pi pour des performances E/S améliorées.
  - Bouton marche/arrêt, une première pour la série.
  - Compatibilité avec le M.2 HAT+ pour les SSD NVMe et autres périphériques PCIe.[](https://www.tomshardware.com/reviews/raspberry-pi-5)[](https://www.raspberrypi.com/news/introducing-raspberry-pi-5/)

---

### **Conception Physique**
Le Raspberry Pi 5 conserve le facteur de forme de la taille d'une carte de crédit (85 mm x 56 mm) des modèles phares précédents, garantissant la compatibilité avec de nombreuses configurations existantes. Cependant, il nécessite un nouveau boîtier en raison des changements de disposition et des exigences thermiques accrues. Le boîtier officiel Raspberry Pi 5 (10 $) inclut un ventilateur intégré pour le refroidissement actif, et le Refroidisseur Actif (5 $) est recommandé pour les charges de travail lourdes pour éviter le throttling thermique. La carte présente également des bords plus nets grâce à des processus de fabrication améliorés comme le refusion intrusive pour les connecteurs et la séparation par panneau routé.[](https://www.raspberrypi.com/products/raspberry-pi-5/)[](https://www.raspberrypi.com/news/introducing-raspberry-pi-5/)

---

### **Système d'Exploitation et Logiciel**
Le système d'exploitation recommandé est **Raspberry Pi OS** (basé sur Debian Bookworm), optimisé pour le matériel du Raspberry Pi 5. Il est disponible en :
- **Complet** : Inclut un environnement de bureau et des logiciels préinstallés pour un usage général.
- **Standard** : Environnement de bureau avec un minimum de logiciels.
- **Léger** : Ligne de commande uniquement, idéal pour les configurations sans tête ou les applications légères.

Les autres systèmes d'exploitation pris en charge incluent :
- **Ubuntu** : Distribution Linux robuste pour les utilisations bureau et serveur.
- **Arch Linux ARM** : Minimaliste et hautement personnalisable.
- **LibreELEC** : OS léger pour exécuter le centre média Kodi.
- **Batocera/Recalbox** : Pour le rétrogaming.
- **Windows 10/11** : Support expérimental pour une utilisation bureau (non officiellement recommandé).[](https://www.jaycon.com/ultimate-guide-to-raspberry-pi/)[](https://wagnerstechtalk.com/rpi5/)

Le **Raspberry Pi Imager** est l'outil officiel pour installer les systèmes d'exploitation sur des cartes microSD ou des SSD. Il simplifie le processus d'installation en permettant aux utilisateurs de sélectionner et de configurer le système d'exploitation, y compris la préconfiguration du nom d'hôte, des comptes utilisateur et du SSH pour un fonctionnement sans tête.[](https://wagnerstechtalk.com/rpi5/)[](https://www.scribd.com/document/693937166/Bash-A-Getting-started-with-Raspberry-Pi-5-A-beginners-Guide-2023)

---

### **Processus d'Installation**
Configurer un Raspberry Pi 5 est simple mais nécessite une préparation matérielle et logicielle spécifique. Voici un guide étape par étape :

1. **Rassembler le Matériel** :
   - Raspberry Pi 5 (variante 2 Go, 4 Go, 8 Go ou 16 Go).
   - Carte microSD (32 Go+ recommandé, Classe 10 pour les performances).
   - Alimentation USB-C 5V/5A.
   - Câble micro HDMI vers HDMI pour l'affichage.
   - Clavier et souris USB (ou alternatives Bluetooth).
   - Optionnel : Moniteur, câble Ethernet, SSD M.2 avec HAT, boîtier avec refroidissement.[](https://robocraze.com/blogs/post/how-to-setup-your-raspberry-pi-5)

2. **Préparer la Carte MicroSD** :
   - Téléchargez le Raspberry Pi Imager depuis le site officiel de Raspberry Pi.
   - Formatez la carte microSD à l'aide d'un outil comme SDFormatter.
   - Utilisez l'Imager pour sélectionner et écrire Raspberry Pi OS (Bookworm) sur la carte.[](https://www.waveshare.com/wiki/Raspberry_Pi_5)

3. **Connecter les Péripériques** :
   - Insérez la carte microSD dans le Raspberry Pi 5.
   - Connectez le moniteur au port HDMI0 (si vous utilisez deux écrans, utilisez les deux ports micro HDMI).
   - Branchez le clavier, la souris et l'Ethernet (si vous n'utilisez pas le Wi-Fi).
   - Branchez l'alimentation USB-C.[](https://www.raspberrypi.com/documentation/computers/getting-started.html)

4. **Démarrer et Configurer** :
   - Allumez le Raspberry Pi 5. La LED d'alimentation rouge doit rester allumée et la LED ACT verte clignotera pendant le démarrage.
   - Suivez les invites à l'écran pour configurer Raspberry Pi OS, y compris le réglage du fuseau horaire, du Wi-Fi et des identifiants utilisateur.
   - Pour les configurations sans tête, activez le SSH via l'Imager ou connectez-vous via UART pour le débogage.[](https://www.waveshare.com/wiki/Raspberry_Pi_5)

5. **Accessoires Optionnels** :
   - Installez un SSD M.2 en utilisant le M.2 HAT+ pour un stockage plus rapide.
   - Ajoutez une batterie au connecteur RTC pour la gestion du temps lorsqu'il est hors tension.
   - Utilisez un boîtier avec refroidissement actif pour les tâches intensives.[](https://www.theengineeringprojects.com/2023/10/introduction-to-raspberry-pi-5.html)[](https://www.raspberrypi.com/products/raspberry-pi-5/)

---

### **Fonctionnalités et Améliorations Clés**
Le Raspberry Pi 5 introduit plusieurs avancées par rapport au Raspberry Pi 4 :
- **Performances** : Le CPU Cortex-A76 et le GPU VideoCore VII offrent un traitement et des graphismes 2 à 3 fois plus rapides, adaptés à des tâches comme l'émulation PS2, l'informatique de bureau et les charges de travail IA. Le CPU peut être overclocké à 3 GHz avec un refroidissement approprié.[](https://wagnerstechtalk.com/rpi5/)[](https://www.tomshardware.com/reviews/raspberry-pi-5)
- **Support PCIe** : L'ajout d'une interface PCIe permet l'utilisation de SSD NVMe et d'autres périphériques haute vitesse, améliorant considérablement les vitesses de démarrage et de transfert de données.[](https://www.raspberrypi.com/news/introducing-raspberry-pi-5/)
- **Contrôleur E/S RP1** : Cette puce personnalisée améliore la bande passante USB 3.0, la connectivité caméra/écran et les performances E/S globales.[](https://www.raspberrypi.com/products/raspberry-pi-5/)
- **Support Double Affichage 4K** : Deux ports micro HDMI permettent une sortie simultanée 4K@60Hz, idéale pour les configurations multimédias et de productivité.[](https://www.linkedin.com/pulse/introduction-raspberry-pi-5-specs-harshvardhan-mishra-wkbmf)
- **RTC Intégrée** : L'horloge temps réel intégrée avec batterie de secours assure une gestion du temps précise sans connexion internet.[](https://en.wikipedia.org/wiki/Raspberry_Pi)
- **Bouton d'Alimentation** : Un bouton marche/arrêt dédié simplifie la gestion de l'alimentation.[](https://www.tomshardware.com/reviews/raspberry-pi-5)
- **Thermique Améliorée** : Le processus de fabrication en 40 nm et le Refroidisseur Actif optionnel améliorent l'efficacité thermique, bien qu'un refroidissement actif soit recommandé pour des performances élevées soutenues.[](https://robocraze.com/blogs/post/how-to-setup-your-raspberry-pi-5)

---

### **Applications**
Les capacités améliorées du Raspberry Pi 5 le rendent adapté à un large éventail de projets :
- **Éducation** : Apprendre la programmation (Python, C++, Java) et l'électronique en utilisant le connecteur GPIO 40 broches pour les capteurs, LED et la robotique.[](https://www.rs-online.com/designspark/introduction-to-raspberry-pi-5-specifications-and-features)
- **Domotique** : Contrôler les appareils domestiques intelligents comme les lumières, serrures et caméras en utilisant des frameworks IoT.[](https://www.rs-online.com/designspark/introduction-to-raspberry-pi-5-specifications-and-features)
- **Centres Médias** : Exécuter Kodi via LibreELEC pour la diffusion et la lecture multimédia sur des écrans doubles 4K.[](https://www.jaycon.com/ultimate-guide-to-raspberry-pi/)
- **Rétrogaming** : Utiliser Batocera ou Recalbox pour émuler des consoles jusqu'à la PS2.[](https://wagnerstechtalk.com/rpi5/)
- **Serveurs** : Héberger des serveurs web légers, des VPN ou des hubs domotiques (par exemple, HomeBridge).[](https://arstechnica.com/gadgets/2024/01/what-i-learned-from-using-a-raspberry-pi-5-as-my-main-computer-for-two-weeks/)
- **Systèmes Industriels et Embarqués** : Le Compute Module 5, basé sur le Raspberry Pi 5, est idéal pour les applications embarquées personnalisées.
- **IA et Apprentissage Automatique** : Tirer parti du CPU/GPU amélioré pour les projets d'IA de périphérie, tels que le traitement d'image ou la reconnaissance vocale, avec des HATs IA compatibles.[](https://www.jaycon.com/ultimate-guide-to-raspberry-pi/)[](https://www.raspberrypi.com/documentation/)
- **Informatique de Bureau** : Utiliser comme un bureau peu coûteux et écoénergétique pour la navigation, le traitement de texte et les tâches de productivité légères.[](https://arstechnica.com/gadgets/2024/01/what-i-learned-from-using-a-raspberry-pi-5-as-my-main-computer-for-two-weeks/)

---

### **Compatibilité et Défis**
Bien que le Raspberry Pi 5 offre des améliorations significatives, certains problèmes de compatibilité surviennent :
- **Boîtiers** : Le Raspberry Pi 5 ne s'adapte pas aux boîtiers Raspberry Pi 4 en raison des changements de disposition. Utilisez le boîtier officiel Raspberry Pi 5 ou des options tierces compatibles.[](https://www.raspberrypi.com/products/raspberry-pi-5/)
- **HATs et Modules d'Extension** : Certains anciens HATs peuvent manquer de support logiciel pour le Raspberry Pi 5, nécessitant des mises à jour communautaires. La programmation GPIO peut également nécessiter des ajustements.[](https://www.dfrobot.com/blog-13550.html)
- **Alimentation** : Une alimentation USB-C 5V/5A est requise pour éviter l'instabilité, contrairement au 5V/3A utilisé pour le Raspberry Pi 4.[](https://www.waveshare.com/wiki/Raspberry_Pi_5)
- **Système d'Exploitation** : Seul le dernier Raspberry Pi OS (Bookworm) est entièrement optimisé. Les anciennes versions du système d'exploitation peuvent ne pas prendre en charge les nouvelles fonctionnalités comme le PCIe.[](https://www.waveshare.com/wiki/Raspberry_Pi_5)

La communauté Raspberry Pi aborde activement ces défis, partageant des solutions et des mises à jour du firmware pour améliorer la compatibilité.[](https://www.dfrobot.com/blog-13550.html)

---

### **Accessoires et Écosystème**
Le Raspberry Pi 5 est soutenu par un riche écosystème d'accessoires :
- **Accessoires Officiels** :
  - Boîtier Raspberry Pi 5 (10 $) avec ventilateur intégré.
  - Refroidisseur Actif (5 $) pour les charges de travail lourdes.
  - Alimentation USB-C 27W (12 $).
  - M.2 HAT+ pour les SSD NVMe (10–20 $).
  - SSD NVME de marque Raspberry Pi (256 Go ou 512 Go).[](https://www.theengineeringprojects.com/2023/10/introduction-to-raspberry-pi-5.html)[](https://www.raspberrypi.com/products/raspberry-pi-5/)
- **Accessoires Tiers** : Des entreprises comme CanaKit, Pimoroni et Pineboards proposent des kits, HATs et solutions de stockage conçus pour le Raspberry Pi 5.[](https://wagnerstechtalk.com/rpi5/)[](https://www.tomshardware.com/reviews/raspberry-pi-5)
- **Documentation et Ressources** :
  - Le Guide du Débutant Officiel Raspberry Pi (5e édition) par Gareth Halfacree couvre l'installation, la programmation et les projets. Un PDF gratuit est disponible via l'application Raspberry Pi Bookshelf.[](https://www.raspberrypi.com/news/available-now-the-official-raspberry-pi-beginners-guide-5th-edition/)
  - Les ressources communautaires comme Wagner’s TechTalk et le subreddit Raspberry Pi fournissent des tutoriels et des idées de projets.[](https://wagnerstechtalk.com/rpi5/)[](https://www.reddit.com/r/RASPBERRY_PI_PROJECTS/comments/16upxc0/total_beginner_with_raspberry_pi_where_do_i_start/)

---

### **Performances et Cas d'Utilisation**
Les performances du Raspberry Pi 5 en font une alternative viable aux mini-PC basse consommation basés sur ARM. Lors des tests, il a été utilisé avec succès comme bureau général pour la navigation web, l'édition de documents et le multitâche léger, bien qu'il puisse avoir des difficultés avec des charges de travail de navigateur lourdes (par exemple, plusieurs onglets Chrome). Sa capacité à exécuter l'émulation PS2 et à gérer des écrans doubles 4K en fait un favori pour le rétrogaming et les centres multimédias. L'overclocking à 3 GHz et le GPU à 1,1 GHz boostent encore les performances, bien qu'un refroidissement actif soit essentiel.[](https://arstechnica.com/gadgets/2024/01/what-i-learned-from-using-a-raspberry-pi-5-as-my-main-computer-for-two-weeks/)[](https://www.tomshardware.com/reviews/raspberry-pi-5)

Pour les applications professionnelles, le modèle 16 Go supporte des tâches plus exigeantes comme le développement logiciel et l'hébergement de serveurs. Le Compute Module 5 et le Raspberry Pi 500 (une version intégrée au clavier) répondent aux besoins des systèmes embarqués et de l'informatique tout-en-un.[](https://www.jaycon.com/ultimate-guide-to-raspberry-pi/)[](https://en.wikipedia.org/wiki/Raspberry_Pi)

---

### **Communauté et Support**
La communauté Raspberry Pi est un atout clé, avec des forums, des subreddits et des sites web comme raspberrypi.org offrant un support étendu. La Raspberry Pi Foundation fournit des mises à jour régulières du firmware, comme celles permettant le support double lecteur NVMe et l'overclocking amélioré. Le magazine MagPi et la documentation officielle offrent des idées de projets et des détails techniques.[](https://www.linkedin.com/pulse/introduction-raspberry-pi-5-specs-harshvardhan-mishra-wkbmf)[](https://www.raspberrypi.com/documentation/)

---

### **Conclusion**
Le Raspberry Pi 5 est un nano-ordinateur puissant, polyvalent et abordable qui s'appuie sur l'héritage de ses prédécesseurs tout en introduisant des fonctionnalités de pointe comme le support PCIe, une puce RP1 personnalisée et une RTC intégrée. Avec des options de RAM allant jusqu'à 16 Go, le support d'affichage double 4K et une augmentation de performance de 2 à 3 fois, il est idéal pour l'éducation, les projets amateurs, la domotique, le rétrogaming et les applications industrielles. Bien que des défis de compatibilité existent, la communauté active et les mises à jour régulières assurent une expérience fluide. Que vous soyez un débutant apprenant le Python ou un ingénieur construisant des systèmes IoT, le Raspberry Pi 5 offre des possibilités infinies à un prix qui démocratise l'informatique.[](https://www.zimaspace.com/blog/raspberry-pi-5-everything-you-need-to-know.html)[](https://www.rs-online.com/designspark/introduction-to-raspberry-pi-5-specifications-and-features)

Pour plus de détails, visitez le site officiel de Raspberry Pi (raspberrypi.com) ou explorez les ressources communautaires comme Wagner’s TechTalk et le magazine The MagPi.[](https://wagnerstechtalk.com/rpi5/)[](https://www.linkedin.com/pulse/introduction-raspberry-pi-5-specs-harshvardhan-mishra-wkbmf)