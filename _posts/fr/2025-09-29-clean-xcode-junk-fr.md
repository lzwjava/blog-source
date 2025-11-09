---
audio: false
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Libérer de l'espace disque en nettoyant les fichiers inutiles de Xcode
translated: true
type: note
---

Bonne question 👍 Xcode (et le simulateur iOS) peuvent accumuler *beaucoup* de déchets au fil du temps — cache de build, données dérivées, appareils simulés, fichiers de support des appareils, logs, etc. Les nettoyer permet de libérer des gigaoctets. Voici une approche structurée :

---

### 1. Effacer les données dérivées (Cache de build)

Cela supprime les anciens produits de build, les fichiers intermédiaires et les index.

* Depuis **l'interface Xcode** :
  `Xcode → Settings → Locations → Derived Data → cliquez sur la flèche → supprimez les dossiers.`
* Depuis le **Terminal** :

  ```bash
  rm -rf ~/Library/Developer/Xcode/DerivedData/*
  ```

---

### 2. Nettoyer les données du simulateur

* Réinitialiser ou supprimer le contenu du simulateur :

  ```bash
  xcrun simctl erase all
  ```

  (efface les applications et les données, mais conserve les définitions des appareils)

* Pour supprimer tous les appareils simulés inutilisés (si vous avez accumulé d'anciennes versions d'iOS) :

  ```bash
  xcrun simctl delete unavailable
  ```

* Pour supprimer tous les appareils simulés (attention, cela supprimera tout) :

  ```bash
  xcrun simctl delete all
  ```

* Supprimer manuellement les répertoires lourds :

  ```bash
  rm -rf ~/Library/Developer/CoreSimulator/Devices/*
  ```

---

### 3. Supprimer les anciens fichiers de support d'appareil

Lorsque vous connectez de vrais appareils, Xcode télécharge les symboles de débogage pour chaque version d'iOS. Ils s'accumulent.

```bash
rm -rf ~/Library/Developer/Xcode/iOS\ DeviceSupport/*
```

---

### 4. Nettoyer les archives

Les archives d'applications de "Product → Archive" consomment beaucoup d'espace.

* Depuis l'Organiseur dans Xcode → Archives → supprimez les anciennes.
* Ou via le Terminal :

  ```bash
  rm -rf ~/Library/Developer/Xcode/Archives/*
  ```

---

### 5. Nettoyer les logs

```bash
rm -rf ~/Library/Developer/Xcode/DocumentationCache/*
rm -rf ~/Library/Developer/Xcode/ios device logs/*
rm -rf ~/Library/Logs/CoreSimulator/*
```

---

### 6. Nettoyer les index dérivés et le cache des modules

```bash
rm -rf ~/Library/Developer/Xcode/DerivedDataModuleCache/*
```

---

### 7. Optionnel : Réinitialisation complète

Si vous souhaitez réinitialiser complètement les caches liés à Xcode :

```bash
rm -rf ~/Library/Developer/Xcode/*
rm -rf ~/Library/Developer/CoreSimulator/*
```

(Cela supprime tout : simulateurs, archives, données dérivées, etc. Le prochain lancement de Xcode donnera une impression de "nouvelle installation".)

---

⚠️ **Conseils**

* Quittez toujours Xcode et le Simulateur avant d'exécuter ces commandes.
* Utilisez `du -sh ~/Library/Developer/*` pour voir quels dossiers sont les plus volumineux.
* Parfois, `Clean Build Folder` (`⇧⌘K`) dans Xcode suffit, mais un nettoyage en profondeur permet d'économiser plus d'espace.

---

Souhaitez-vous que je vous fournisse un **script unique** que vous pouvez exécuter pour nettoyer tous les déchets courants en une seule fois (avec des options facultatives) ?