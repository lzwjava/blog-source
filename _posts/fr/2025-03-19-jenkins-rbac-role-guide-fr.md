---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Guide RBAC Jenkins avec le plugin Rôle
translated: true
type: note
---

Dans Jenkins, le **contrôle d'accès basé sur les rôles (RBAC)** consiste à définir qui peut faire quoi, et où. Par défaut, Jenkins n'a qu'un modèle basique utilisateur/administrateur, mais avec le **plugin Role-Based Strategy** (ou des stratégies d'autorisation similaires), vous pouvez définir un accès granulaire.

---

### Concepts de Base du RBAC dans Jenkins

1. **Rôles Globaux**
   Ils s'appliquent à l'ensemble de l'instance Jenkins. Exemples :

   * **Admin** : contrôle total.
   * **Lecture seule** : peut visualiser les jobs mais pas les exécuter.
   * **Développeur** : peut créer et configurer des jobs.

2. **Rôles de Projet/Job**
   Vous pouvez accorder des permissions par job ou par dossier. Par exemple :

   * L'Utilisateur A peut builder *le Projet X* mais pas voir *le Projet Y*.
   * Les prestataires peuvent déclencher des builds mais ne peuvent pas modifier les configurations.

3. **Permissions de Build**
   Les permissions peuvent être divisées :

   * `Job/Lire` (voir la définition du job et l'historique des builds)
   * `Job/Build` (déclencher des builds)
   * `Job/Configurer` (modifier le pipeline ou les paramètres)
   * `Job/Supprimer` (supprimer des jobs ou des builds)
   * `Job/Annuler` (interrompre les builds en cours d'exécution)

---

### Comment Gérer les Droits d'Accès aux Jobs ou aux Builds

1. **Installer le Plugin Role-Based Strategy**

   * Allez dans **Gérer Jenkins → Plugins → Plugins disponibles → Role-based Authorization Strategy**.
   * Après l'installation, sélectionnez-le dans **Gérer Jenkins → Configurer la sécurité globale → Autorisation**.

2. **Définir les Rôles**

   * Allez dans **Gérer Jenkins → Gérer et Attribuer les Rôles**.
   * Créez des rôles globaux (comme *admin*, *viewer*, *developer*) et des rôles de projet (comme *projectX-builder*).
   * Attribuez à chaque rôle les permissions nécessaires (`Job/Build`, `Job/Configurer`, etc.).

3. **Attribuer les Rôles aux Utilisateurs/Groupes**

   * Toujours dans **Gérer et Attribuer les Rôles**, associez vos utilisateurs Jenkins (ou groupes LDAP si intégré) aux rôles.
   * Par exemple :

     * Associez *alice* → `developer`
     * Associez *bob* → `viewer`
     * Associez *qa-team* → `projectX-builder`

4. **Utiliser les Dossiers pour une Meilleure Granularité**

   * Organisez les jobs dans des **Dossiers** (via le *Folders Plugin*).
   * Appliquez des restrictions de rôle au niveau du dossier afin que seule la bonne équipe puisse voir/builder/modifier les jobs à l'intérieur.

---

### Exemples de Scénarios

* **Développeurs** : Peuvent builder et configurer les jobs de leur équipe, mais ne peuvent pas toucher aux paramètres d'administration.
* **Équipe QA** : Ne peut que déclencher des builds (pas reconfigurer les pipelines).
* **Utilisateurs Externes** : Peuvent voir le statut des jobs mais pas les modifier ou déclencher des builds.

---

👉 En pratique : vous gardez **peu d'administrateurs**, donnez aux **développeurs un accès configurer + builder** à leurs propres jobs, et accordez des **droits en lecture seule ou builder uniquement** aux autres. Cela assure la cohérence, réduit les erreurs et protège les jobs sensibles.

---

Souhaitez-vous que je vous montre un **exemple de configuration étape par étape** (avec les rôles, les permissions et le mappage des jobs) qui corresponde à une configuration d'entreprise typique ?