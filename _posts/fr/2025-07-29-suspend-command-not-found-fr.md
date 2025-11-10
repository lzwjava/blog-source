---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Résoudre l'erreur de commande de suspension
translated: true
type: note
---

L'erreur `sudo: suspend: command not found` indique que la commande `suspend` n'est pas disponible sur votre système ou n'est pas installée. La commande `suspend` est généralement utilisée pour mettre un système Linux dans un état de suspension (veille), mais elle peut ne pas être présente par défaut ou avoir un nom différent selon votre distribution.

Voici comment résoudre ce problème :

### 1. **Utiliser la Bonne Commande**
Sur de nombreuses distributions Linux, la commande pour suspendre le système n'est pas `suspend` mais plutôt l'une des suivantes :

- **`systemctl suspend`** :
  C'est la commande standard sur les systèmes utilisant `systemd` (par exemple, Ubuntu, Debian, Fedora, etc.).
  ```bash
  sudo systemctl suspend
  ```

- **`pm-suspend`** :
  Si votre système utilise le paquet `pm-utils`, vous pouvez utiliser :
  ```bash
  sudo pm-suspend
  ```
  Remarque : Vous devrez peut-être installer `pm-utils` s'il n'est pas déjà installé :
  ```bash
  sudo apt-get install pm-utils  # Pour Debian/Ubuntu
  sudo dnf install pm-utils      # Pour Fedora
  ```

- **`echo mem > /sys/power/state`** :
  Pour une approche de bas niveau, vous pouvez écrire directement dans l'état d'alimentation du système :
  ```bash
  echo mem | sudo tee /sys/power/state
  ```
  Cela nécessite des privilèges root et peut ne pas fonctionner sur tous les systèmes selon la configuration du noyau.

### 2. **Vérifier si `systemd` est Disponible**
Puisque `systemctl suspend` est la méthode la plus courante sur les distributions Linux modernes, vérifiez si `systemd` est en cours d'exécution :
```bash
pidof systemd
```
Si cette commande retourne un PID, votre système utilise `systemd`, et `systemctl suspend` devrait fonctionner. Sinon, vous devrez peut-être utiliser `pm-suspend` ou une autre méthode.

### 3. **Installer les Outils Manquants**
Si ni `systemctl` ni `pm-suspend` n'est disponible, vous devrez peut-être installer le paquet approprié :
- Pour Ubuntu/Debian :
  ```bash
  sudo apt-get update
  sudo apt-get install pm-utils
  ```
- Pour Fedora :
  ```bash
  sudo dnf install pm-utils
  ```

### 4. **Vérifier les Permissions**
Assurez-vous d'avoir des privilèges suffisants. La commande `sudo` suggère que vous essayez de l'exécuter en tant qu'administrateur, mais vérifiez que votre utilisateur est bien dans le fichier `sudoers` :
```bash
sudo -l
```
Si vous n'avez pas les permissions, vous devrez peut-être contacter votre administrateur système.

### 5. **Alternative : Utiliser l'Environnement de Bureau**
Si vous utilisez un environnement de bureau graphique (par exemple, GNOME, KDE), vous pouvez suspendre le système via l'interface graphique (par exemple, en cliquant sur le menu d'alimentation et en sélectionnant "Suspendre"). Alternativement, utilisez :
- Pour GNOME :
  ```bash
  gnome-session-quit --power-off
  ```
- Pour KDE :
  ```bash
  qdbus org.kde.ksmserver /KSMServer org.kde.KSMServerInterface.logout 0 1 0
  ```

### 6. **Vérifier le Support Matériel**
Certains systèmes peuvent ne pas prendre en charge la suspension en raison de problèmes matériels ou de noyau. Vérifiez si la suspension est prise en charge :
```bash
cat /sys/power/state
```
Si `mem` est listé dans la sortie, la suspension est prise en charge. Sinon, vous devrez peut-être résoudre les problèmes matériels ou les paramètres du noyau.

### 7. **Si Vous Avez Spécifiquement Besoin de la Commande `suspend`**
Si vous recherchez une commande `suspend` spécifique (par exemple, faisant partie d'un script ou d'un paquet personnalisé), elle pourrait ne pas être installée. Recherchez-la :
```bash
sudo apt-cache search suspend
```
Ou vérifiez si elle fait partie d'un autre paquet. Si vous pensiez à un script ou alias personnalisé, vérifiez son emplacement et assurez-vous qu'il est exécutable :
```bash
which suspend
```

### Exemple de Procédure
Pour suspendre votre système sur une configuration Ubuntu typique :
```bash
sudo systemctl suspend
```
Cela devrait mettre votre système dans un état de veille à faible consommation. Lorsque vous reprenez, vous devrez peut-être déverrouiller votre session.

Si vous rencontrez toujours des problèmes, indiquez-moi votre distribution Linux et tout détail supplémentaire sur votre configuration, et je pourrai vous fournir des conseils plus adaptés.

[Documentation Ubuntu sur la Gestion de l'Alimentation](https://help.ubuntu.com/stable/ubuntu-help/power-suspend.html)
[Page de manuel systemd suspend](https://www.freedesktop.org/software/systemd/man/systemctl.html)