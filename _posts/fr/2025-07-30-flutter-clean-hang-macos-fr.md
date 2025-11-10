---
audio: false
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Résoudre le blocage de Flutter Clean sur macOS
translated: true
type: note
---

Ah, je vois ce que tu veux dire 👍  
Parfois, `flutter clean` peut sembler "planter" sur macOS — surtout s'il y a beaucoup de fichiers générés, ou si les dossiers `DerivedData` de Xcode sont énormes.

---

### ✅ Essayez ces étapes

1. **Annulez la commande qui semble bloquée**
   Appuyez sur `CTRL + C`.

2. **Nettoyez manuellement (même effet que `flutter clean`)**  
   Vous pouvez supprimer vous-même ces dossiers de build/cache :
   ```bash
   rm -rf build/ .dart_tool/ ios/Pods ios/Podfile.lock ios/Flutter/Flutter.framework ios/Flutter/Flutter.podspec
   ```

   Si vous voulez aussi supprimer le cache de Xcode :
   ```bash
   rm -rf ~/Library/Developer/Xcode/DerivedData
   ```

3. **Récupérez à nouveau les dépendances**
   ```bash
   flutter pub get
   ```

4. **Réinstallez CocoaPods (pour iOS)**
   ```bash
   cd ios
   pod install --repo-update
   cd ..
   ```

5. **Recompilez et exécutez à nouveau**
   ```bash
   flutter run
   ```

---

⚡ **Astuce :** La première fois après le nettoyage peut prendre un peu plus de temps (puisque Flutter doit régénérer `.dart_tool`, `.pub-cache`, les Pods iOS, etc.), mais cela ne devrait pas rester bloqué indéfiniment. Si cela reste "bloqué", cela pourrait être lié à :

- **Un Flutter SDK obsolète** → Exécutez `flutter upgrade`
- **Un CocoaPods obsolète** → Exécutez `sudo gem install cocoapods`  
- **Problèmes liés à Rosetta / puce M1** : Si vous êtes sur Apple Silicon, il faut parfois exécuter `arch -x86_64 pod install` dans le dossier `ios`, selon votre configuration.

---

👉 Voulez-vous que je vous donne un **script en une ligne** qui efface les caches de build et réinitialise les Pods (en gros un "super clean") pour que vous n'ayez pas à déboguer un `flutter clean` bloqué ?