---
audio: false
generated: true
lang: fr
layout: post
title: 'Xvfb : Serveur d''affichage X11 sans tête'
translated: true
type: note
---

### Qu'est-ce que Xvfb ?

Xvfb (X Virtual Framebuffer) est un serveur d'affichage X11 qui exécute des applications graphiques sans avoir besoin d'un affichage physique ou d'une accélération graphique matérielle. Il s'agit essentiellement d'un serveur X « headless » qui simule un affichage en mémoire, permettant à des programmes nécessitant un environnement graphique (comme des navigateurs, des tests d'interface utilisateur ou des outils de rendu) de s'exécuter sur des serveurs ou dans des environnements sans moniteur, clavier ou souris.

Il est couramment utilisé dans les tests automatisés (par exemple, avec Selenium pour le web scraping ou les tests d'interface utilisateur), les pipelines d'intégration et de déploiement continus (CI/CD), ou tout scénario où vous devez exécuter des applications basées sur X11 en arrière-plan sans rien afficher à l'écran.

### Comment fonctionne Xvfb ?

1. **Création d'un affichage virtuel** :
   - Lorsque vous démarrez Xvfb, il crée un affichage virtuel (par exemple, `:99` ou un autre numéro d'affichage) qui existe entièrement dans la RAM. Cet affichage a une résolution, une profondeur de couleur et d'autres paramètres que vous définissez au lancement.
   - Exemple de commande : `Xvfb :99 -screen 0 1024x768x24` (démarre un affichage virtuel à une résolution de 1024x768 avec une couleur 24 bits).

2. **Gestion des opérations graphiques** :
   - Xvfb intercepte les requêtes du protocole X11 provenant des applications (comme le dessin de fenêtres, le rendu d'images ou la gestion d'événements).
   - Au lieu d'envoyer la sortie vers un écran physique, il effectue toutes les opérations dans un tampon mémoire (le « framebuffer »). Ce tampon agit comme un écran virtuel où les pixels sont écrits mais jamais affichés.
   - Il prend en charge les fonctionnalités de base de X11 mais ne dispose pas d'accélération matérielle, il n'est donc pas adapté aux graphiques haute performance comme les jeux — il est plutôt destiné au rendu simple ou aux tests.

3. **Simulation d'événements** :
   - Xvfb peut simuler des événements d'entrée (par exemple, souris/clavier) si nécessaire, mais généralement, les applications s'exécutent comme si elles étaient sur un véritable affichage.
   - La sortie n'est pas visible, mais vous pouvez capturer des captures d'écran ou vider le framebuffer dans des fichiers (en utilisant des outils comme `xwd` ou `import` d'ImageMagick) pour vérification.

4. **Intégration avec des outils** :
   - Des bibliothèques comme pyvirtualdisplay (comme dans votre trace d'erreur) encapsulent Xvfb pour faciliter son démarrage/arrêt depuis le code. Par exemple, en Python :
     ```python
     from pyvirtualdisplay import Display
     display = Display(visible=0, size=(1024, 768))
     display.start()
     # Exécutez votre application graphique ici
     display.stop()
     ```
   - Il s'exécute en arrière-plan, et votre application définit la variable d'environnement `DISPLAY` (par exemple, `export DISPLAY=:99`) pour pointer vers le serveur virtuel.

5. **Limitations** :
   - Aucune interaction matérielle réelle, donc pas de support GPU ou de sortie vidéo directe.
   - L'utilisation de la mémoire peut augmenter avec des résolutions plus importantes ou des sessions de longue durée.
   - Il fait partie du projet X.org et est disponible sur les systèmes Linux/Unix ; il n'est pas natif sur macOS ou Windows (bien qu'il existe des alternatives comme Xming pour Windows).

Concernant l'erreur que vous avez collée : Il semble que Xvfb ne soit pas installé sur votre système (le `FileNotFoundError` pour 'Xvfb'). Sur macOS (d'après vos chemins Homebrew), vous pouvez l'installer via `brew install --cask xvfb` ou similaire, mais vérifiez qu'il est dans votre PATH. pyvirtualdisplay dépend de sa disponibilité en tant qu'exécutable.

[Page de manuel de Xvfb](https://www.x.org/releases/X11R7.7/doc/man/man1/Xvfb.1.xhtml)
[Wikipedia : Xvfb](https://en.wikipedia.org/wiki/Xvfb)
[Comment utiliser Xvfb pour les tests headless](https://www.browserstack.com/guide/what-is-xvfb)