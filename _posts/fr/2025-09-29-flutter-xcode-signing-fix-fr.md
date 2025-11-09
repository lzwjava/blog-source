---
audio: false
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Corriger l'Échec de Signature de Code Flutter dans Xcode
translated: true
type: note
---

Vous rencontrez l'erreur classique de signature de code Flutter / Xcode : Xcode/`security` n'a trouvé aucune identité de signature valide, donc `flutter run` ne peut pas signer l'application pour un appareil physique. Ci-dessous, je vais vous donner une série de corrections et de commandes de dépannage claires et ordonnées — choisissez l'option que vous souhaitez (exécuter dans le Simulateur maintenant, ou configurer la signature pour exécuter sur un vrai appareil). Je ne demanderai pas plus d'informations — je suppose que vous voulez corriger ce problème maintenant.

---

# Options rapides (choisissez-en une)

**A — Exécuter sur le simulateur (aucune signature de code requise)**
Si vous voulez simplement exécuter rapidement sans gérer les certificats :

1. Ouvrez le Simulateur : `open -a Simulator`
2. Exécutez Flutter en ciblant le simulateur :
   `flutter run -d "$(xcrun simctl list devices | grep -m1 -o "iPhone.*(Simulator)" | sed 's/ (Simulator)//')"`
   Ou plus simplement : `flutter run -d iPhone-14` (remplacez par un nom de simulateur disponible affiché par `xcrun simctl list`).

**B — Corriger la signature pour déployer sur un appareil réel (recommandé pour les tests sur appareil)**
Suivez les étapes ci-dessous dans l'ordre.

---

# Étapes pour corriger la signature pour le déploiement sur appareil

## 1) Confirmer l'environnement et les vérifications de base

Exécutez ces commandes et notez le résultat :

```bash
flutter doctor -v
xcode-select --print-path
xcodebuild -version
security find-identity -p codesigning -v
xcrun simctl list devices
```

`security find-identity -p codesigning -v` devrait afficher au moins une identité. La vôtre a affiché `0 valid identities found` — c'est pourquoi cela échoue.

## 2) Utiliser la signature automatique de Xcode (le plus simple)

1. Ouvrez l'espace de travail :
   `open ios/Runner.xcworkspace`
2. Dans Xcode : sélectionnez le projet `Runner` → la cible `Runner` → **Signing & Capabilities**.
3. Définissez **Team** sur votre identifiant Apple / compte Apple Developer. Si votre identifiant Apple n'est pas ajouté :

   * Xcode → Preferences → Accounts → `+` → ajoutez l'identifiant Apple.
4. Cochez **Automatically manage signing**.
5. Assurez-vous que le **Bundle Identifier** est unique (style DNS inversé, par exemple `com.votrenom.votreapp`).
6. Xcode tentera de créer un certificat de développement et un profil d'approvisionnement ; si vous voyez des invites, autorisez Xcode à les gérer.

> Remarque : Pour un déploiement complet sur un appareil arbitraire, vous avez besoin d'un abonnement Apple Developer (99 $/an). Xcode peut utiliser un identifiant Apple gratuit pour le "free provisioning", mais il est limité (nombre d'appareils, pas certains droits).

## 3) Enregistrer votre appareil (si nécessaire)

Si Xcode ne peut pas enregistrer automatiquement votre appareil, allez sur le portail Apple Developer → Certificates, IDs & Profiles → Devices → ajoutez l'UDID de l'appareil. Vous pouvez obtenir l'UDID de l'appareil en le connectant et en le sélectionnant dans la fenêtre Devices and Simulators de Xcode.

## 4) Générer/importer un certificat manuellement (si vous avez déjà un p12)

Si vous avez un certificat `.p12` et une clé privée :

```bash
security import /chemin/vers/certificate.p12 -k ~/Library/Keychains/login.keychain-db -P "P12_PASSWORD" -T /usr/bin/codesign
```

Puis réexécutez `security find-identity -p codesigning -v` pour confirmer son apparition.

## 5) Si vous préférez que Xcode crée les certificats pour vous

Dans Xcode → Accounts → Sélectionnez votre identifiant Apple → Manage Certificates → `+` → ajoutez **iOS Development**. Cela crée un certificat dans votre trousseau et il apparaît dans `security find-identity`.

## 6) Vérifier que les Command Line Tools sont définies

```bash
sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer
```

Puis acceptez la licence si nécessaire :

```bash
sudo xcodebuild -license accept
```

## 7) Une fois la signature configurée, exécutez depuis le terminal

Depuis la racine du projet :

```bash
flutter clean
flutter pub get
flutter run
```

Si plusieurs appareils, spécifiez `-d <device-id>`.

---

# Conseils de dépannage et pièges courants

* **"0 valid identities found" persiste** — confirmez que la clé privée du certificat est dans le trousseau de connexion (ouvrez Keychain Access → login). Si vous avez importé le certificat mais pas la clé privée, la signature échoue.
* **Incompatibilité du Bundle ID** — l'App ID dans le portail Developer doit correspondre exactement à l'identifiant de bundle dans Xcode (les caractères génériques sont autorisés dans certains cas).
* **Équipe non sélectionnée** — Xcode affiche "No account" — ajoutez l'identifiant Apple dans Xcode Preferences → Accounts.
* **Profil d'approvisionnement expiré** — vérifiez le portail Developer et régénérez le profil d'approvisionnement.
* **Limitations du free provisioning** — si vous utilisez un identifiant Apple gratuit, vous devrez peut-être réapprovisionner tous les 7 jours et le nombre d'appareils est limité.
* **CI / automatisation** — utilisez `fastlane match` ou les APIs App Store Connect pour gérer les certificats et profils de manière centralisée.
* **Erreurs de permission Codesign** — assurez-vous que l'élément Keychain accorde l'accès à codesign ; parfois, vous devez autoriser manuellement `/usr/bin/codesign` à accéder à la clé privée dans le trousseau.
* **Si `flutter run` échoue toujours**, exécutez la build Xcode pour voir une erreur plus détaillée : ouvrez l'espace de travail et appuyez sur Run dans Xcode ; vérifiez les erreurs Signing & Capabilities dans l'interface utilisateur.

---

# Commandes utiles à copier-coller

Lister les identités de signature de code :

```bash
security find-identity -p codesigning -v
```

Importer un `.p12` :

```bash
security import /chemin/vers/yourcert.p12 -k ~/Library/Keychains/login.keychain-db -P "P12PASSWORD" -T /usr/bin/codesign
```

Définir les outils en ligne de commande Xcode :

```bash
sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer
```

Ouvrir l'espace de travail iOS :

```bash
open ios/Runner.xcworkspace
```

---

# Si vous voulez, je peux

* donner la séquence exacte de clics dans Xcode pour créer un certificat/profil étape par étape (j'ai déjà inclus les étapes principales), ou
* fournir des exemples de commandes `fastlane`/`match` si vous voulez de l'automatisation pour plusieurs machines/CI, ou
* aider à interpréter toute nouvelle erreur après avoir essayé la méthode de signature automatique de Xcode.

Dites-moi quelle option vous avez choisie (Simulateur maintenant / Xcode automatique / import manuel p12 / CI) et collez toute nouvelle erreur si cela échoue encore — je vous donnerai les prochaines étapes.