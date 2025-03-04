---
audio: false
generated: true
lang: fr
layout: post
title: Publier une extension Chrome
translated: true
---

Publier une extension Chrome (plugin) sur le Chrome Web Store est un processus simple si vous suivez les étapes nécessaires avec soin. Voici un guide complet, étape par étape, pour vous aider à rendre votre extension disponible sur le Chrome Web Store.

---

### Étape 1 : Préparer votre extension Chrome
Avant de commencer le processus de publication, assurez-vous que votre extension est prête pour le public :

- **Tester soigneusement** : Testez votre extension sur différentes versions de Chrome pour confirmer qu'elle fonctionne comme prévu. Utilisez la fonctionnalité "Charger non empaqueté" de Chrome (trouvée dans `chrome://extensions/`) pour la tester localement.
- **Nettoyer le code** : Supprimez tout code de débogage, les instructions `console.log` ou les commentaires inutiles qui pourraient exposer des informations sensibles ou affecter les performances.
- **Vérifier les performances** : Assurez-vous que votre extension ne ralentit pas le navigateur ou n'utilise pas trop de ressources.
- **Vérifier le fichier manifest.json** : Ce fichier est le socle de votre extension. Assurez-vous qu'il inclut :
  - Un `nom` descriptif.
  - Un numéro de `version` (par exemple, "1.0.0" pour votre première version).
  - Les `permissions` requises (par exemple, "activeTab", "storage"), en les gardant minimales et justifiées.
  - Un champ `icons` pointant vers votre fichier d'icône (par exemple, un `icon.png` de 128x128 pixels).
  - Tous les autres champs nécessaires comme `background`, `content_scripts`, ou `action` en fonction de la fonctionnalité de votre extension.

---

### Étape 2 : Emballer votre extension
Pour télécharger votre extension sur le Chrome Web Store, vous devez l'emballer correctement :

- **Rassembler les fichiers** : Assurez-vous que votre répertoire d'extension contient tous les fichiers requis :
  - `manifest.json`
  - Fichiers HTML, CSS, JavaScript
  - Images (y compris votre icône)
- **Créer un fichier ZIP** : Compressez l'ensemble du répertoire de l'extension en un fichier `.zip`. Ne téléchargez pas un fichier `.crx`, car le Chrome Web Store accepte désormais directement les fichiers `.zip`.

---

### Étape 3 : Configurer un compte développeur
Vous avez besoin d'un compte développeur Chrome Web Store pour publier votre extension :

- **Se connecter** : Allez sur le [Tableau de bord des développeurs Chrome](https://chrome.google.com/webstore/devconsole) et connectez-vous avec votre compte Google.
- **Payer les frais** : Si vous ne vous êtes pas encore inscrit, payez un frais d'inscription unique de 5 $ pour les développeurs. Ce coût est unique, pas par extension.

---

### Étape 4 : Préparer les actifs de la liste de la boutique
La liste de votre extension dans la boutique nécessite des actifs et des informations spécifiques pour attirer les utilisateurs :

- **Icône** : Une icône de 128x128 pixels (par exemple, `icon.png`) spécifiée dans votre `manifest.json`. Elle apparaît dans la barre d'outils Chrome et dans la liste de la boutique.
- **Captures d'écran** : Au moins une capture d'écran montrant votre extension en action. Les tailles recommandées sont 1280x800 ou 640x400 pixels. Plusieurs captures d'écran sont meilleures pour montrer la fonctionnalité.
- **Images promotionnelles optionnelles** : Une image de marque (1400x560 pixels) peut améliorer votre liste, bien qu'elle ne soit pas obligatoire.
- **Description** :
  - **Description courte** : Un résumé concis (par exemple, "Un outil simple pour [le but de votre extension]").
  - **Description détaillée** : Une explication plus longue de ce que fait votre extension, de ses principales fonctionnalités et de pourquoi les utilisateurs devraient l'installer. Évitez les fautes d'orthographe ou de grammaire.
- **Politique de confidentialité** (si applicable) : Si votre extension collecte des données personnelles ou sensibles des utilisateurs, créez une politique de confidentialité et hébergez-la en ligne (par exemple, sur un site web personnel ou une page GitHub). Liez-la dans votre liste. Si elle ne collecte pas de données, une simple déclaration comme "Cette extension ne collecte ni ne transmet de données personnelles des utilisateurs" peut inspirer confiance.

---

### Étape 5 : Télécharger votre extension
Vous êtes maintenant prêt à soumettre votre extension :

1. **Accéder au tableau de bord** : Connectez-vous au [Tableau de bord des développeurs Chrome](https://chrome.google.com/webstore/devconsole).
2. **Ajouter un nouvel élément** : Cliquez sur "Ajouter un nouvel élément" ou un bouton similaire pour commencer le processus de téléchargement.
3. **Télécharger le fichier ZIP** : Sélectionnez et téléchargez votre fichier `.zip`.
4. **Remplir la liste** :
   - Entrez vos descriptions courte et détaillée.
   - Téléchargez votre icône, vos captures d'écran et vos images promotionnelles optionnelles.
   - Sélectionnez des **catégories** appropriées (par exemple, "Productivité") et ajoutez des **mots-clés** (par exemple, "gestion du temps") pour améliorer la découverte.
   - Liez votre politique de confidentialité (si applicable).
   - Définissez la **visibilité** : Choisissez de publier immédiatement après l'approbation ou de planifier une date ultérieure. Pour votre première version, "publier après l'approbation" est typique.
5. **Tarification** : Décidez si votre extension est gratuite (recommandé pour une première version) ou payante. La plupart des extensions Chrome sont gratuites, avec une monétisation possible plus tard via des achats intégrés ou des abonnements (ce qui nécessite une configuration supplémentaire).

---

### Étape 6 : Soumettre pour examen
- **Soumettre** : Une fois tous les champs remplis, soumettez votre extension pour examen.
- **Processus d'examen** : L'équipe du Chrome Web Store vérifiera votre extension pour s'assurer qu'elle respecte leurs [Politiques du programme](https://developer.chrome.com/docs/webstore/program-policies/). Cela prend généralement quelques heures à quelques jours.
- **Conformité aux politiques** :
  - Assurez-vous que votre extension a un seul but clair.
  - Justifiez toutes les permissions dans votre description (par exemple, pourquoi "activeTab" ou "storage" est nécessaire).
  - Évitez les comportements interdits comme les logiciels malveillants, la collecte excessive de données ou les allégations trompeuses.

---

### Étape 7 : Après l'approbation
- **Mise en ligne** : Une fois approuvée, votre extension sera disponible sur le Chrome Web Store pour les utilisateurs à installer.
- **Surveiller les retours** : Vérifiez les avis et les évaluations des utilisateurs dans le tableau de bord des développeurs pour résoudre les problèmes ou les suggestions.
- **Mises à jour** : Pour les futures mises à jour, incrémentez la `version` dans `manifest.json`, créez un nouveau `.zip` et téléchargez-le via le tableau de bord. Il passera à nouveau par l'examen avant d'être mis à jour pour les utilisateurs.

---

### Conseils supplémentaires
- **Choisir un nom unique** : Recherchez le Chrome Web Store pour vous assurer que le nom de votre extension n'est pas déjà pris. Rendez-le descriptif et accrocheur.
- **Commencer simplement** : Pour votre première version, gardez-la gratuite et en anglais uniquement. Vous pouvez ajouter des fonctionnalités payantes ou des traductions plus tard.
- **Promouvoir** : Partagez votre extension sur les réseaux sociaux ou d'autres plateformes pour augmenter la visibilité (optionnel).

---

En suivant ces étapes—préparer votre extension, l'emballer, configurer un compte développeur, créer une liste de boutique attrayante et la soumettre pour examen—vous publierez avec succès votre plugin Chrome sur le Chrome Web Store. Bonne chance pour votre lancement !