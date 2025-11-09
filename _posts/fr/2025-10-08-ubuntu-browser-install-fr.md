---
audio: false
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Guide d'installation du navigateur Ubuntu 24.04
translated: true
type: note
---

En dehors de **Firefox** et de **Chromium**, il existe plusieurs bons navigateurs que vous pouvez installer sur **Ubuntu 24.04** — en fonction de vos priorités (vitesse, vie privée, compatibilité, utilisation des ressources, etc.). Voici une liste catégorisée avec des notes :

---

### 🧠 Navigateurs grand public

**1. Google Chrome**

* Basé sur Chromium mais inclut la synchronisation Google, les codecs et des fonctionnalités propriétaires.
* Excellente compatibilité avec les applications web (comme Google Docs, Meet, etc.).
* Installez via le fichier `.deb` depuis le site officiel de Google.

**2. Microsoft Edge (version Linux)**

* Basé sur Chromium, interface soignée, intègre les services Microsoft.
* Souvent plus rapide que Chrome en gestion de la mémoire.
* Paquet `.deb` disponible sur le site de Microsoft.

---

### 🔒 Navigateurs axés sur la vie privée

**3. Brave**

* Construit sur Chromium mais avec un bloqueur de publicités intégré, un blocage des traqueurs et un mode fenêtre Tor.
* Maintient la compatibilité avec les extensions Chrome.
* Installation :

  ```bash
  sudo apt install apt-transport-https curl
  sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg
  echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg] https://brave-browser-apt-release.s3.brave.com/ stable main" | sudo tee /etc/apt/sources.list.d/brave-browser-release.list
  sudo apt update
  sudo apt install brave-browser
  ```

**4. Vivaldi**

* Également basé sur Chromium, mais hautement personnalisable (mosaïque d'onglets, raccourcis clavier, outils de la barre latérale).
* Plus riche en fonctionnalités que Chrome ou Edge.
* Téléchargez le fichier `.deb` sur [vivaldi.com](https://vivaldi.com).

**5. Tor Browser**

* Axé sur l'anonymat et le contournement de la censure.
* Basé sur Firefox ESR, route le trafic via le réseau Tor.
* Installation via :

  ```bash
  sudo apt install torbrowser-launcher
  ```

---

### 🪶 Navigateurs légers

**6. Falkon (Qt WebEngine)**

* Léger, interface minimale, s'intègre bien avec les systèmes KDE/Qt.
* Installation :

  ```bash
  sudo apt install falkon
  ```

**7. Midori**

* Un projet plus ancien relancé pour sa simplicité et sa faible utilisation des ressources.
* Correct pour une navigation simple, pas idéal pour les applications web lourdes.
* Installation :

  ```bash
  sudo apt install midori
  ```

**8. Epiphany (GNOME Web)**

* Le navigateur par défaut de GNOME, basé sur WebKit (et non Chromium).
* Simple, léger, s'intègre parfaitement dans l'environnement GNOME.
* Installation :

  ```bash
  sudo apt install epiphany-browser
  ```

---

### 🧪 Navigateurs pour développeurs / de niche

**9. Ungoogled Chromium**

* Chromium débarrassé de tout suivi Google et des dépendances d'API associées.
* Configuration manuelle mais bon pour une vie privée stricte.
* Souvent disponible via un paquet `.deb` communautaire ou Flatpak.

**10. Floorp**

* Un fork moderne de Firefox avec une vie privée et une personnalisation améliorées.
* Créé par des développeurs japonais ; devient assez populaire.
* Flatpak disponible sur Flathub.

---

Souhaitez-vous que je recommande une combinaison (par exemple, *un axé sur la vie privée, un léger, un complet*) qui correspond à votre flux de travail sur cette installation Ubuntu ?