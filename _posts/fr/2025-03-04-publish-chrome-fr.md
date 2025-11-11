---
audio: false
generated: true
lang: fr
layout: post
title: Publication d'une Extension Chrome
translated: true
type: note
---

Publier une extension Chrome sur le Chrome Web Store est un processus simple si vous suivez attentivement les étapes nécessaires. Voici un guide complet, étape par étape, pour vous aider à mettre votre extension en ligne sur le Chrome Web Store.

---

### Étape 1 : Préparer votre extension Chrome
Avant de commencer le processus de publication, assurez-vous que votre extension est prête pour le public :

- **Testez minutieusement** : Testez votre extension sur différentes versions de Chrome pour confirmer son bon fonctionnement. Utilisez la fonctionnalité "Charger l'extension non empaquetée" (accessible via `chrome://extensions/`) pour la tester localement.
- **Nettoyez le code** : Supprimez tout code de débogage, instructions `console.log` ou commentaires inutiles qui pourraient exposer des informations sensibles ou affecter les performances.
- **Vérifiez les performances** : Assurez-vous que votre extension ne ralentit pas le navigateur ou n'utilise pas de ressources excessives.
- **Vérifiez le fichier manifest.json** : Ce fichier est l'épine dorsale de votre extension. Assurez-vous qu'il inclut :
  - Un `name` descriptif.
  - Un numéro de `version` (par exemple, "1.0.0" pour votre première version).
  - Les `permissions` requises (par exemple, "activeTab", "storage"), en les maintenant minimales et justifiées.
  - Un champ `icons` pointant vers votre fichier d'icône (par exemple, une `icon.png` de 128x128 pixels).
  - Tous les autres champs nécessaires comme `background`, `content_scripts` ou `action` selon les fonctionnalités de votre extension.

---

### Étape 2 : Empaqueter votre extension
Pour télécharger votre extension sur le Chrome Web Store, vous devez l'empaqueter correctement :

- **Rassemblez les fichiers** : Assurez-vous que votre répertoire d'extension contient tous les fichiers nécessaires :
  - `manifest.json`
  - Les fichiers HTML, CSS, JavaScript
  - Les images (y compris votre icône)
- **Créez un fichier ZIP** : Compressez l'intégralité du répertoire de l'extension dans un fichier `.zip`. Ne téléchargez pas un fichier `.crx`, car le Chrome Web Store accepte désormais directement les fichiers `.zip`.

---

### Étape 3 : Configurer un compte développeur
Vous avez besoin d'un compte développeur Chrome Web Store pour publier votre extension :

- **Connectez-vous** : Allez sur le [Tableau de bord du développeur Chrome](https://chrome.google.com/webstore/devconsole) et connectez-vous avec votre compte Google.
- **Payez les frais** : Si vous n'êtes pas encore enregistré, payez les frais d'inscription unique de 5 $. Il s'agit d'un coût unique, et non par extension.

---

### Étape 4 : Préparer les éléments de la page de présentation
La page de présentation de votre extension nécessite des éléments et des informations spécifiques pour attirer les utilisateurs :

- **Icône** : Une icône de 128x128 pixels (par exemple, `icon.png`) spécifiée dans votre `manifest.json`. Elle apparaît dans la barre d'outils Chrome et sur la page de présentation.
- **Captures d'écran** : Au moins une capture d'écran montrant votre extension en action. Les tailles recommandées sont 1280x800 ou 640x400 pixels. Plusieurs captures d'écran sont préférables pour mettre en valeur les fonctionnalités.
- **Images promotionnelles (optionnelles)** : Une image bannière (1400x560 pixels) peut améliorer votre page de présentation, bien que non obligatoire.
- **Description** :
  - **Description courte** : Un résumé concis (par exemple, "Un outil simple pour [l'objectif de votre extension]").
  - **Description détaillée** : Une explication plus longue de ce que fait votre extension, ses principales fonctionnalités et pourquoi les utilisateurs devraient l'installer. Évitez les fautes d'orthographe ou de grammaire.
- **Politique de confidentialité** (le cas échéant) : Si votre extension collecte des données utilisateur personnelles ou sensibles, créez une politique de confidentialité et hébergez-la en ligne (par exemple, sur un site web personnel ou une page GitHub). Liez-la dans votre page de présentation. Si elle ne collecte aucune donnée, une simple déclaration comme "Cette extension ne collecte ni ne transmet de données utilisateur personnelles" peut instaurer la confiance.

---

### Étape 5 : Télécharger votre extension
Vous êtes maintenant prêt à soumettre votre extension :

1. **Accédez au Tableau de bord** : Connectez-vous au [Tableau de bord du développeur Chrome](https://chrome.google.com/webstore/devconsole).
2. **Ajouter un nouvel élément** : Cliquez sur "Ajouter un nouvel élément" ou un bouton similaire pour lancer le processus de téléchargement.
3. **Téléchargez le ZIP** : Sélectionnez et téléchargez votre fichier `.zip`.
4. **Remplissez la page de présentation** :
   - Saisissez vos descriptions courte et détaillée.
   - Téléchargez votre icône, vos captures d'écran et vos images promotionnelles optionnelles.
   - Sélectionnez les **catégories** appropriées (par exemple, "Productivité") et ajoutez des **tags** (par exemple, "gestion du temps") pour améliorer la découvrabilité.
   - Liez votre politique de confidentialité (le cas échéant).
   - Définissez la **visibilité** : Choisissez de publier immédiatement après approbation ou de planifier une date ultérieure. Pour votre première version, "publier après approbation" est typique.
5. **Tarification** : Décidez si votre extension est gratuite (recommandé pour une première version) ou payante. La plupart des extensions Chrome sont gratuites, une monétisation étant possible ultérieurement via des achats intégrés ou des abonnements (bien que cela nécessite une configuration supplémentaire).

---

### Étape 6 : Soumettre pour examen
- **Soumettez** : Une fois tous les champs remplis, soumettez votre extension pour examen.
- **Processus d'examen** : L'équipe du Chrome Web Store vérifiera la conformité de votre extension avec ses [Politiques du programme](https://developer.chrome.com/docs/webstore/program-policies/). Cela prend généralement quelques heures à quelques jours.
- **Conformité aux politiques** :
  - Assurez-vous que votre extension a un objectif unique et clair.
  - Justifiez toutes les permissions dans votre description (par exemple, pourquoi "activeTab" ou "storage" est nécessaire).
  - Évitez les comportements interdits comme les logiciels malveillants, la collecte excessive de données ou les affirmations trompeuses.

---

### Étape 7 : Après l'approbation
- **Mise en ligne** : Une fois approuvée, votre extension sera disponible sur le Chrome Web Store pour que les utilisateurs puissent l'installer.
- **Surveillez les retours** : Consultez les avis et les notations des utilisateurs dans le Tableau de bord du développeur pour traiter les problèmes ou suggestions.
- **Mises à jour** : Pour les futures mises à jour, incrémentez le numéro de `version` dans `manifest.json`, créez un nouveau fichier `.zip` et téléchargez-le via le Tableau de bord. Elle passera à nouveau par un examen avant d'être mise à jour pour les utilisateurs.

---

### Conseils supplémentaires
- **Choisissez un nom unique** : Recherchez sur le Chrome Web Store pour vous assurer que le nom de votre extension n'est pas déjà pris. Rendez-le descriptif et accrocheur.
- **Restez simple** : Pour votre première version, gardez-la gratuite et en anglais uniquement. Vous pourrez ajouter des fonctionnalités payantes ou des traductions plus tard.
- **Promouvez** : Partagez votre extension sur les réseaux sociaux ou d'autres plateformes pour augmenter sa visibilité (optionnel).

---

En suivant ces étapes—préparer votre extension, l'empaqueter, configurer un compte développeur, créer une page de présentation attrayante et la soumettre pour examen—vous publierez avec succès votre extension Chrome sur le Chrome Web Store. Bonne chance pour votre lancement !