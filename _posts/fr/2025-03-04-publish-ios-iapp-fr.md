---
audio: false
generated: true
lang: fr
layout: post
title: Publication d'une application iOS sur l'App Store
translated: true
type: note
---

Pour utiliser le programme pour développeurs Apple afin de télécharger une application iOS, que ce soit pour un usage personnel ou professionnel, vous devez vous inscrire au programme, préparer et empaqueter votre application, la télécharger et gérer les mises à jour. Voici un guide étape par étape abordant tous les aspects de votre demande, y compris l'exigence du numéro Dun & Bradstreet (D-U-N-S) pour un usage professionnel, l'empaquetage de l'application, le téléchargement de l'archive et la mise à jour des applications via le site d'Apple.

---

### 1. S'inscrire au Programme pour Développeurs Apple

#### Pour les particuliers (Usage personnel)
- **Créer un Apple ID** :  
  Si vous n'en avez pas, allez sur [appleid.apple.com](https://appleid.apple.com) et inscrivez-vous en utilisant une adresse e-mail personnelle.
- **S'inscrire au Programme** :  
  - Rendez-vous sur [developer.apple.com/programs/](https://developer.apple.com/programs/) et cliquez sur "S'inscrire".
  - Connectez-vous avec votre Apple ID.
  - Acceptez les conditions, fournissez votre nom légal personnel et votre adresse, et payez les frais annuels de 99 USD.
- **Note importante** : Votre nom personnel apparaîtra comme vendeur sur l'App Store.

#### Pour les entreprises (Usage organisationnel)
- **Obtenir un numéro D-U-N-S** :  
  - Un numéro D-U-N-S est un identifiant unique à neuf chiffres attribué par Dun & Bradstreet pour vérifier le statut de l'entité légale de votre organisation. Apple l'exige pour les comptes professionnels.
  - Vérifiez si votre organisation en possède déjà un sur [dnb.com](https://www.dnb.com). Sinon, demandez-le gratuitement via leur site web — le traitement peut prendre jusqu'à deux semaines.
- **S'inscrire au Programme** :  
  - Utilisez un Apple ID lié à votre organisation (par exemple, une adresse e-mail professionnelle).
  - Allez sur [developer.apple.com/programs/](https://developer.apple.com/programs/) et cliquez sur "S'inscrire".
  - Sélectionnez "Organisation" et fournissez :
    - Le nom de l'entité légale
    - L'adresse du siège social
    - Le numéro D-U-N-S
  - La personne qui s'inscrit doit avoir l'autorité légale pour accepter les conditions d'Apple au nom de l'organisation.
  - Payez les frais annuels de 99 USD.
- **Note importante** : Le nom de votre organisation apparaîtra comme vendeur sur l'App Store.

---

### 2. Préparer et empaqueter l'application
- **Développer votre application dans Xcode** :  
  - Utilisez Xcode, l'outil de développement officiel d'Apple, pour créer votre application iOS.
  - Assurez-vous qu'elle respecte les [Règles de vérification de l'App Store](https://developer.apple.com/app-store/review/guidelines/).
  - Définissez la cible de déploiement et mettez à jour la version de l'application et les numéros de build dans les paramètres du projet.
- **Archiver l'application** :  
  - Ouvrez votre projet dans Xcode.
  - Sélectionnez "Generic iOS Device" (ou tout simulateur) comme cible de build.
  - Allez dans **Product** > **Archive** dans la barre de menus.
  - Xcode compilera votre application et créera une archive, qui est une version empaquetée prête pour la distribution, incluant le code, les ressources et les informations de signature.

---

### 3. Télécharger l'archive de l'application
- **Utilisation de Xcode** :  
  - Après l'archivage, la fenêtre Organizer s'ouvre automatiquement dans Xcode.
  - Sélectionnez votre archive et cliquez sur **Distribute App**.
  - Choisissez **App Store Connect** comme méthode de distribution.
  - Suivez les invites pour valider et télécharger l'archive vers App Store Connect.
- **Utilisation de Transporter (Alternative)** :  
  - Téléchargez l'application [Transporter](https://apps.apple.com/us/app/transporter/id1450874784) depuis le Mac App Store.
  - Connectez-vous avec votre Apple ID.
  - Ajoutez le fichier de l'application archivée (exporté en tant que fichier `.ipa` depuis Xcode) et téléchargez-le vers App Store Connect.
  - Cette option est utile pour les utilisateurs avancés ou les téléchargements en masse.

---

### 4. Mettre à jour les applications en utilisant le site d'Apple (App Store Connect)
- **Accéder à App Store Connect** :  
  - Allez sur [appstoreconnect.apple.com](https://appstoreconnect.apple.com) et connectez-vous avec votre Apple ID.
- **Gérer votre application** :  
  - Sélectionnez votre application depuis le tableau de bord.
  - Naviguez vers l'onglet **App Store**.
  - Mettez à jour les métadonnées (par exemple, la description de l'application, les captures d'écran, les mots-clés).
  - Sous "Versions", sélectionnez la nouvelle version que vous avez téléchargée.
- **Soumettre pour vérification** :  
  - Cliquez sur **Submit for Review** pour envoyer la mise à jour à l'équipe de vérification d'Apple.
  - Après approbation, vous pouvez la publier manuellement ou planifier une publication automatique.

---

### Notes supplémentaires
- **Détails spécifiques aux entreprises** :  
  - Assurez-vous que votre numéro D-U-N-S et les informations de votre organisation sont exacts pour éviter les retards d'inscription.
  - Vous pouvez inviter des membres de l'équipe (par exemple, des développeurs, des testeurs) à votre compte via App Store Connect et leur attribuer des rôles comme "Developer" ou "Admin".
- **Défis courants et conseils** :  
  - **Problèmes de signature de code** : Vérifiez vos certificats et profils d'approvisionnement dans Xcode sous **Signing & Capabilities**. Utilisez l'option "Automatically manage signing" si vous n'êtes pas sûr.
  - **Rejets lors de la vérification de l'application** : Testez votre application minutieusement pour vous conformer aux règles d'Apple et éviter les retards.
  - **Retards liés au numéro D-U-N-S** : Demandez votre numéro D-U-N-S à l'avance si vous êtes une entreprise, car c'est un prérequis pour l'inscription.

---

Avec ces étapes, vous pouvez utiliser avec succès le Programme pour Développeurs Apple pour télécharger et mettre à jour votre application iOS, que vous soyez un particulier ou une entreprise. Pour plus de détails, consultez la documentation officielle d'Apple sur [developer.apple.com](https://developer.apple.com).