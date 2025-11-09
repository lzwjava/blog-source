---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Installation de Chromium sur Ubuntu 24.04
translated: true
type: note
---

Pour installer **Chromium** sur **Ubuntu 24.04**, vous avez plusieurs bonnes options — selon que vous voulez la **version Snap officielle**, la version **APT (paquet Debian)**, ou un **téléchargement manuel**. Voici un guide clair pour chaque méthode :

---

### 🧩 Option 1 : Installer via Snap (Méthode Ubuntu Officielle)

C'est la méthode **par défaut** et la plus stable.

```bash
sudo snap install chromium
```

Puis lancez-le avec :

```bash
chromium
```

✅ *Avantages :*

* Maintenu officiellement par Canonical.
* Se met à jour automatiquement.

⚠️ *Inconvénients :*

* Le démarrage peut être plus lent.
* Le sandboxing Snap peut causer des problèmes avec les proxys système ou l'accès aux fichiers.

---

### ⚙️ Option 2 : Installer via APT (Paquet Debian, Non-Snap)

Si vous **n'aimez pas Snap**, vous pouvez installer Chromium depuis un **dépôt tiers** tel que la build Debian officielle fournie par **ungoogled-chromium** ou **OBS**.

1. Ajoutez le dépôt OBS :

   ```bash
   sudo apt install wget gnupg
   wget -qO - https://download.opensuse.org/repositories/home:/ungoogled_chromium/Ubuntu_24.04/Release.key | sudo gpg --dearmor -o /usr/share/keyrings/ungoogled-chromium.gpg
   ```

2. Ajoutez le dépôt :

   ```bash
   echo "deb [signed-by=/usr/share/keyrings/ungoogled-chromium.gpg] https://download.opensuse.org/repositories/home:/ungoogled_chromium/Ubuntu_24.04/ /" | sudo tee /etc/apt/sources.list.d/ungoogled-chromium.list
   ```

3. Installez Chromium :

   ```bash
   sudo apt update
   sudo apt install ungoogled-chromium
   ```

Puis lancez-le avec :

```bash
ungoogled-chromium
```

✅ *Avantages :*

* Aucune dépendance à Snap.
* Version renforcée pour la confidentialité disponible.

⚠️ *Inconvénients :*

* Les mises à jour arrivent plus lentement qu'avec Snap.
* Certaines fonctionnalités (comme Google Sync) sont désactivées.

---

### 🧰 Option 3 : Installer depuis la Build Officielle de Chromium (Manuelle)

Si vous voulez la **dernière version de développement** :

```bash
sudo apt install chromium-browser
```

Si cela redirige vers Snap et que vous voulez l'éviter :

```bash
sudo apt purge chromium-browser
sudo apt install chromium
```

Ou, téléchargez manuellement un fichier `.deb` :

```bash
wget https://commondatastorage.googleapis.com/chromium-browser-snapshots/Linux_x64/LAST_CHANGE -O /tmp/LAST_CHANGE
LATEST=$(cat /tmp/LAST_CHANGE)
wget "https://commondatastorage.googleapis.com/chromium-browser-snapshots/Linux_x64/${LATEST}/chrome-linux.zip"
unzip chrome-linux.zip
./chrome-linux/chrome
```

---

### 🌍 Note sur les Paramètres de Proxy

Étant donné que votre système utilise :

```
HTTP_PROXY=http://127.0.0.1:7890
HTTPS_PROXY=http://127.0.0.1:7890
```

Assurez-vous que Snap et APT respectent votre proxy en les exportant dans `/etc/environment` ou votre profil shell :

```bash
export http_proxy=http://127.0.0.1:7890
export https_proxy=http://127.0.0.1:7890
```

---

Souhaitez-vous que je vous montre comment configurer Chromium pour qu'il utilise automatiquement ce proxy (afin qu'il se connecte toujours par son intermédiaire) ?