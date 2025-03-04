---
audio: false
generated: true
lang: fr
layout: post
title: Publier une application iOS sur l'App Store
translated: true
---

Pour utiliser le programme Apple Developer pour télécharger une application iOS, que ce soit pour un usage personnel ou corporatif, vous devez vous inscrire au programme, préparer et emballer votre application, la télécharger et gérer les mises à jour. Voici un guide étape par étape abordant tous les aspects de votre demande, y compris l'exigence de numéro D-U-N-S (Dun & Bradstreet) pour un usage corporatif, l'emballage de l'application, le téléchargement de l'archive et la mise à jour des applications via le site d'Apple.

---

### 1. Inscription au programme Apple Developer

#### Pour les particuliers (usage personnel)
- **Créer un identifiant Apple** :
  Si vous n'en avez pas, allez sur [appleid.apple.com](https://appleid.apple.com) et inscrivez-vous en utilisant une adresse e-mail personnelle.
- **S'inscrire au programme** :
  - Rendez-vous sur [developer.apple.com/programs/](https://developer.apple.com/programs/) et cliquez sur "S'inscrire".
  - Connectez-vous avec votre identifiant Apple.
  - Acceptez les conditions, fournissez votre nom légal personnel et votre adresse, et payez le frais annuel de 99 USD.
- **Note importante** : Votre nom personnel apparaîtra comme vendeur sur l'App Store.

#### Pour les entreprises (usage organisationnel)
- **Obtenir un numéro D-U-N-S** :
  - Un numéro D-U-N-S est un identifiant unique à neuf chiffres attribué par Dun & Bradstreet pour vérifier le statut d'entité légale de votre organisation. Apple le requiert pour les comptes d'entreprise.
  - Vérifiez si votre organisation en possède déjà un sur [dnb.com](https://www.dnb.com). Si ce n'est pas le cas, demandez-le gratuitement via leur site web — le traitement peut prendre jusqu'à deux semaines.
- **S'inscrire au programme** :
  - Utilisez un identifiant Apple lié à votre organisation (par exemple, une adresse e-mail professionnelle).
  - Rendez-vous sur [developer.apple.com/programs/](https://developer.apple.com/programs/) et cliquez sur "S'inscrire".
  - Sélectionnez "Organisation" et fournissez :
    - Nom de l'entité légale
    - Adresse du siège social
    - Numéro D-U-N-S
  - La personne s'inscrivant doit avoir l'autorité légale pour accepter les conditions d'Apple au nom de l'organisation.
  - Payez le frais annuel de 99 USD.
- **Note importante** : Le nom de votre organisation apparaîtra comme vendeur sur l'App Store.

---

### 2. Préparation et emballage de l'application
- **Développez votre application dans Xcode** :
  - Utilisez Xcode, l'outil de développement officiel d'Apple, pour créer votre application iOS.
  - Assurez-vous qu'elle respecte les [directives de révision de l'App Store](https://developer.apple.com/app-store/review/guidelines/).
  - Définissez la cible de déploiement et mettez à jour les numéros de version et de build de l'application dans les paramètres du projet.
- **Archiver l'application** :
  - Ouvrez votre projet dans Xcode.
  - Sélectionnez "Generic iOS Device" (ou tout autre simulateur) comme cible de build.
  - Allez dans **Product** > **Archive** dans la barre de menu.
  - Xcode compilera votre application et créera une archive, qui est une version empaquetée prête pour la distribution, incluant le code, les ressources et les informations de signature.

---

### 3. Téléchargement de l'archive de l'application
- **Utilisation de Xcode** :
  - Après l'archivage, la fenêtre Organizer s'ouvre automatiquement dans Xcode.
  - Sélectionnez votre archive et cliquez sur **Distribute App**.
  - Choisissez **App Store Connect** comme méthode de distribution.
  - Suivez les instructions pour valider et télécharger l'archive sur App Store Connect.
- **Utilisation de Transporter (alternative)** :
  - Téléchargez l'application [Transporter](https://apps.apple.com/us/app/transporter/id1450874784) depuis le Mac App Store.
  - Connectez-vous avec votre identifiant Apple.
  - Ajoutez le fichier d'application archivé (exporté sous forme de fichier `.ipa` depuis Xcode) et téléchargez-le sur App Store Connect.
  - Cette option est utile pour les utilisateurs avancés ou les téléchargements en masse.

---

### 4. Mise à jour des applications via le site d'Apple (App Store Connect)
- **Accéder à App Store Connect** :
  - Rendez-vous sur [appstoreconnect.apple.com](https://appstoreconnect.apple.com) et connectez-vous avec votre identifiant Apple.
- **Gérer votre application** :
  - Sélectionnez votre application à partir du tableau de bord.
  - Accédez à l'onglet **App Store**.
  - Mettez à jour les métadonnées (par exemple, la description de l'application, les captures d'écran, les mots-clés).
  - Sous "Versions", sélectionnez la nouvelle build que vous avez téléchargée.
- **Soumettre pour révision** :
  - Cliquez sur **Submit for Review** pour envoyer la mise à jour à l'équipe de révision d'Apple.
  - Après approbation, vous pouvez la publier manuellement ou planifier une publication automatique.

---

### Notes supplémentaires
- **Détails spécifiques aux entreprises** :
  - Assurez-vous que votre numéro D-U-N-S et les informations organisationnelles sont exacts pour éviter les retards d'inscription.
  - Vous pouvez inviter des membres de l'équipe (par exemple, des développeurs, des testeurs) à votre compte via App Store Connect et leur attribuer des rôles comme "Développeur" ou "Admin".
- **Défis courants et conseils** :
  - **Problèmes de signature de code** : Vérifiez vos certificats et profils de provisionnement dans Xcode sous **Signing & Capabilities**. Utilisez l'option "Automatically manage signing" si vous n'êtes pas sûr.
  - **Rejets de révision d'application** : Testez votre application de manière approfondie pour respecter les directives d'Apple et éviter les retards.
  - **Retards de D-U-N-S** : Demandez votre numéro D-U-N-S à l'avance si vous êtes une entreprise, car c'est une condition préalable à l'inscription.

---

Avec ces étapes, vous pouvez utiliser le programme Apple Developer pour télécharger et mettre à jour votre application iOS, que vous soyez un particulier ou une entreprise. Pour plus de détails, consultez la documentation officielle d'Apple sur [developer.apple.com](https://developer.apple.com).