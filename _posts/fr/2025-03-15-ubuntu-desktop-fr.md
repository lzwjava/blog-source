---
audio: false
generated: true
lang: fr
layout: post
title: Installation d'un environnement de bureau sur Ubuntu
translated: true
type: note
---

Il semble que votre système Ubuntu n’ait peut-être pas d’interface utilisateur graphique (GUI) installée, ce qui expliquerait pourquoi vous ne voyez pas de navigateur de fichiers (souvent appelé gestionnaire de fichiers sous Linux) ou quelconque outil de type « finder ». Cela peut arriver si vous avez installé une version serveur d'Ubuntu, choisi une installation minimale, ou s'il y a un problème empêchant le chargement de l'interface graphique. Ne vous inquiétez pas—nous pouvons résoudre ceci en installant une interface graphique comme GNOME (l'environnement de bureau par défaut d'Ubuntu) ou une autre option si vous préférez. Voici comment procéder étape par étape.

### Étape 1 : Mettre à jour votre système
Avant d'installer quoi que ce soit, il est conseillé de s'assurer que vos listes de paquets sont à jour et que votre système est entièrement mis à niveau. Ouvrez un terminal et exécutez ces commandes :

```bash
sudo apt update
```
Cette commande actualise la liste des paquets disponibles.

```bash
sudo apt upgrade
```
Cette commande met à jour tous les paquets actuellement installés vers leurs dernières versions. Si vous y êtes invité, appuyez sur `Y` pour confirmer.

### Étape 2 : Installer l'environnement de bureau GNOME
Puisque vous avez mentionné vouloir une interface graphique « comme GNOME ou autre », commençons par GNOME, car c'est l'environnement par défaut pour Ubuntu Desktop et il inclut un gestionnaire de fichiers appelé Nautilus. Pour l'installer, exécutez :

```bash
sudo apt install ubuntu-desktop
```
Cette commande installe l'environnement de bureau GNOME complet, ainsi que les applications standard comme un gestionnaire de fichiers, un navigateur web, et plus encore. L'installation peut prendre quelques minutes, selon votre vitesse de connexion et votre système. Si on vous demande de choisir un gestionnaire d'affichage (par exemple, GDM ou LightDM), vous pouvez généralement conserver l'option par défaut (GDM pour GNOME) en appuyant sur Entrée.

### Étape 3 : Redémarrer votre système
Une fois l'installation terminée, redémarrez votre système pour lancer l'interface graphique :

```bash
sudo reboot
```
Une fois votre système redémarré, vous devriez voir un écran de connexion graphique. Connectez-vous, et vous aurez un bureau entièrement fonctionnel avec un gestionnaire de fichiers (Nautilus) qui vous permettra de parcourir vos fichiers.

### Et si cela ne fonctionne pas ?
Si vous ne voyez toujours pas d'interface graphique après le redémarrage, il est possible qu'il y ait un problème avec le gestionnaire d'affichage ou les pilotes graphiques. Vous pouvez essayer de démarrer le gestionnaire d'affichage manuellement pour tester :

```bash
sudo systemctl start gdm
```
Si cela affiche un écran de connexion, parfait ! Pour vous assurer qu'il démarre automatiquement à chaque démarrage, exécutez :

```bash
sudo systemctl enable gdm
```
Si l'interface graphique n'apparaît toujours pas, vérifiez les erreurs en consultant les journaux système avec :

```bash
journalctl -b
```
Recherchez les messages liés à `gdm`, `Xorg` ou aux pilotes graphiques, et n'hésitez pas à demander de l'aide supplémentaire en fournissant ces détails.

### Options alternatives d'interface graphique
Si vous préférez une interface graphique différente de GNOME, voici quelques alternatives populaires :
- **KDE Plasma** (élégant et personnalisable) :
  ```bash
  sudo apt install kubuntu-desktop
  ```
- **XFCE** (léger et rapide) :
  ```bash
  sudo apt install xubuntu-desktop
  ```
- **LXDE** (très léger, adapté aux anciens matériels) :
  ```bash
  sudo apt install lubuntu-desktop
  ```
Après avoir installé l'une de ces alternatives, redémarrez avec `sudo reboot`, et vous obtiendrez un environnement de bureau avec un gestionnaire de fichiers (par exemple, Dolphin pour KDE, Thunar pour XFCE).

### Pourquoi n'avais-je pas d'interface graphique ?
Il est possible que vous n'ayez pas eu d'interface graphique parce que :
- Vous avez installé Ubuntu Server, qui n'inclut pas de bureau par défaut.
- Vous avez choisi une installation minimale lors de la configuration, ignorant l'interface graphique.
- Il est rare, mais possible, que l'interface graphique soit installée mais ne démarre pas en raison d'un problème de configuration ou matériel.

Installer `ubuntu-desktop` comme décrit ci-dessus devrait résoudre le problème s'il s'agit d'une interface graphique manquante. Si vous soupçonnez un problème avec une interface graphique existante, faites-le-moi savoir, et nous pourrons approfondir le dépannage !

### Résumé
Pour installer GNOME et obtenir un navigateur de fichiers sur votre système Ubuntu :
1. `sudo apt update`
2. `sudo apt upgrade`
3. `sudo apt install ubuntu-desktop`
4. `sudo reboot`

Vous aurez bientôt une interface graphique avec un gestionnaire de fichiers prêt à l'emploi. Profitez de votre bureau Ubuntu !