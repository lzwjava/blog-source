---
audio: false
generated: true
lang: fr
layout: post
title: Comment utiliser une demande de modification
translated: true
type: note
---

Pour ajouter un groupe à une demande de changement (Change Request) dans ServiceNow, vous devez attribuer un groupe au champ **Groupe d'affectation** (Assignment group) dans le formulaire de demande de changement. Voici un guide détaillé, étape par étape, pour vous accompagner dans ce processus.

---

### Guide Étape par Étape

1. **Accéder au Module des Demandes de Changement**  
   - Connectez-vous à votre instance ServiceNow.  
   - Dans le volet de navigation de gauche, tapez "Change" dans le filtre de navigation.  
   - Sélectionnez **Change > Tous** (All) pour afficher la liste de toutes les demandes de changement.

2. **Ouvrir la Demande de Changement**  
   - Localisez la demande de changement spécifique à laquelle vous souhaitez attribuer un groupe. Vous pouvez utiliser la barre de recherche ou les filtres (par exemple, par numéro de demande de changement ou description courte).  
   - Cliquez sur la demande de changement pour ouvrir son formulaire.

3. **Localiser le Champ Groupe d'Affectation**  
   - Dans le formulaire de demande de changement, trouvez le champ **Groupe d'affectation** (Assignment group). Il se trouve généralement dans la section "Planification" (Planning) ou "Affectation" (Assignment), selon la configuration de votre instance.

4. **Sélectionner le Groupe**  
   - Cliquez sur l'icône en forme de loupe (recherche de référence) à côté du champ **Groupe d'affectation**.  
   - Une fenêtre pop-up affichera une liste des groupes disponibles.  
   - Tapez le nom du groupe dans la zone de recherche pour filtrer la liste, puis sélectionnez le groupe souhaité en cliquant dessus.  
   - Si vous connaissez le nom exact du groupe, vous pouvez également commencer à le taper directement dans le champ, et ServiceNow suggérera les groupes correspondants.

5. **Sauvegarder les Modifications**  
   - Après avoir sélectionné le groupe, cliquez sur **Mettre à jour** (Update) ou **Sauvegarder** (Save) (généralement en haut ou en bas du formulaire) pour enregistrer vos modifications sur la demande de changement.

---

### Considérations Importantes

- **Type de Groupe**  
   Assurez-vous que le groupe que vous souhaitez attribuer est configuré avec un type de groupe approprié (par exemple, "Change" ou "ITIL"). Certaines instances ServiceNow restreignent les groupes disponibles dans le champ **Groupe d'affectation** en fonction de leur type. Pour vérifier ou mettre à jour le type d'un groupe :  
   - Allez dans **Administration des utilisateurs > Groupes** (User Administration > Groups), trouvez le groupe et vérifiez son champ "Type".

- **Permissions**  
   Vous avez besoin de permissions suffisantes pour attribuer des groupes à une demande de changement. Généralement, des rôles comme `change_manager` ou équivalents sont requis. Si vous ne pouvez pas attribuer un groupe, contactez votre administrateur ServiceNow pour confirmer votre accès.

- **Qualificateurs de Référence**  
   Le champ **Groupe d'affectation** peut avoir des filtres (qualificateurs de référence) qui limitent les groupes affichés. Si le groupe que vous voulez n'apparaît pas dans la liste, cela peut être dû à une configuration dans les paramètres du dictionnaire du champ. Un administrateur peut vérifier cela sous **Définition du système > Dictionnaire** (System Definition > Dictionary).

- **Affectation Automatisée (Optionnel)**  
   Bien que ce guide couvre l'affectation manuelle, notez que les groupes peuvent également être attribués automatiquement à l'aide de workflows ou de règles d'affectation configurés par votre organisation.

---

### Dépannage
- **Le Groupe n'Apparaît Pas ?**  
   - Vérifiez que le groupe existe dans **Administration des utilisateurs > Groupes**.  
   - Vérifiez son type de groupe et les éventuels qualificateurs de référence sur le champ **Groupe d'affectation**.  
- **Pas d'Autorisation pour Sauvegarder ?**  
   - Assurez-vous d'avoir le rôle nécessaire pour modifier les demandes de changement.

En suivant ces étapes et en tenant compte des points ci-dessus, vous devriez pouvoir ajouter avec succès un groupe à une demande de changement dans ServiceNow. Si vous rencontrez des problèmes, consultez votre administrateur ServiceNow pour une assistance adaptée à la configuration de votre instance.

---

Pour résoudre votre problème où votre demande de changement dans ServiceNow apparaît vide—avec des sections comme les liens associés, la planification, les CI affectés, les approbateurs et la liste des demandes de changement n'affichant aucune donnée—vous devez renseigner ces zones avec les informations nécessaires. Il semble que bien que le formulaire de demande de changement existe lui-même, ses listes associées et ses champs manquent de données. Voici un guide étape par étape pour vous aider à remplir les détails requis et les listes associées.

---

### Étape 1 : Vérifier et Remplir les Informations de Base
Même si votre demande de changement existe, elle peut manquer de détails essentiels. Commencez par vous assurer que les champs fondamentaux sont complétés :

- **Ouvrir la Demande de Changement** : Accédez à la demande de changement spécifique dans ServiceNow (par exemple, via le module Change > Tous ou en recherchant son numéro).
- **Vérifier les Champs Obligatoires** :
  - **Description Courte** (Short Description) : Ajoutez un bref résumé du changement (par exemple, "Mise à niveau de la mémoire du serveur").
  - **Description** (Description) : Fournissez une explication détaillée de ce que le changement implique.
  - **Demandeur** (Requester) : Spécifiez qui demande le changement (cela peut être vous par défaut si vous l'avez créée).
  - **Groupe d'Affectation** (Assignment Group) : Attribuez l'équipe responsable du changement (par exemple, "Équipe Serveur").
  - **Assigné à** (Assigned To) : Optionnellement, assignez un individu spécifique au sein du groupe.
- **Sauvegarder le Formulaire** : Cliquez sur **Sauvegarder** (Save) ou **Mettre à jour** (Update) pour vous assurer que ces détails sont enregistrés. Certains champs peuvent être obligatoires (marqués d'un astérisque rouge), et la sauvegarde pourrait être impossible tant qu'ils ne sont pas remplis.

---

### Étape 2 : Compléter les Détails de Planification
La section "planification" que vous avez mentionnée fait probablement référence aux champs qui définissent la portée et le calendrier du changement. Renseignez-les pour fournir du contexte :

- **Type de Changement** (Change Type) : Sélectionnez le type (par exemple, Normal, Urgent, Standard).
- **Catégorie** (Category) : Choisissez une catégorie appropriée (par exemple, Matériel, Logiciel, Réseau).
- **Priorité** (Priority) : Définissez-la en fonction de l'urgence et de l'impact (par exemple, Faible, Moyenne, Élevée).
- **Risque et Impact** (Risk and Impact) : Évaluez et saisissez les niveaux de risque et d'impact potentiels.
- **Dates de Début et de Fin Prévues** (Planned Start and End Dates) : Spécifiez quand le changement commencera et se terminera.
- **Sauvegarder les Modifications** : Assurez-vous que ces champs sont sauvegardés pour mettre à jour la demande de changement.

---

### Étape 3 : Ajouter les CI Affectés
La liste des "CI affectés" est vide car aucun Élément de Configuration (CI) n'a encore été lié. Voici comment la renseigner :

- **Localiser la Liste Associée** : Descendez jusqu'à la section **CI Affectés** (Affected CIs) en bas du formulaire.
- **Ajouter des CIs** :
  - Cliquez sur **Modifier** (Edit) ou **Nouveau** (New) (selon la configuration de votre instance).
  - Une fenêtre de sélection apparaîtra, vous permettant de rechercher et de sélectionner des CIs dans la Base de Données de Gestion de Configuration (CMDB).
  - Choisissez les CIs pertinents (par exemple, serveurs, applications) impactés par le changement.
- **Sauvegarder** : Cliquez sur **Sauvegarder** pour lier ces CIs à la demande de changement.

---

### Étape 4 : Gérer les Approbateurs
La liste des "approbateurs" est vide car aucun enregistrement d'approbation n'existe encore. Selon le processus de votre organisation, les approbateurs peuvent être ajoutés automatiquement ou manuellement :

- **Vérifier le Processus d'Approbaion** :
  - Cherchez un bouton **Demander une Approbation** (Request Approval) ou une action UI sur le formulaire. Cliquer dessus peut déclencher un workflow d'approbation basé sur des règles prédéfinies (par exemple, le type de changement ou le niveau de risque).
- **Ajouter Manuellement des Approbateurs** (si nécessaire) :
  - Allez dans la liste associée **Approbations** (Approvals).
  - Cliquez sur **Nouveau** (New) pour créer un enregistrement d'approbation.
  - Sélectionnez l'approbateur (par exemple, un manager ou un membre du Comité Consultatif des Changements) et sauvegardez.
- **Surveiller le Statut** : Une fois ajoutés, les approbateurs devront approuver ou rejeter le changement.

---

### Étape 5 : Remplir la Liste des Demandes de Changement (Changements Enfants ou Tâches)
Vous avez mentionné qu'une "liste des demandes de changement" était vide, ce qui pourrait faire référence à des demandes de changement enfants ou à des **Tâches de Changement** (Change Tasks). Voici comment résoudre ce problème :

- **Tâches de Changement** (plus probable) :
  - Descendez jusqu'à la liste associée **Tâches de Changement** (Change Tasks).
  - Cliquez sur **Nouveau** pour créer une tâche.
  - Remplissez les détails comme la description de la tâche, le groupe d'affectation, la personne assignée et la date d'échéance.
  - Sauvegardez la tâche. Répétez l'opération pour toutes les tâches requises.
- **Demandes de Changement Enfants** (si applicable) :
  - Si votre organisation utilise des demandes de changement parent-enfant, cherchez une liste associée comme **Changements Enfants** (Child Changes).
  - Cliquez sur **Nouveau** pour créer une demande de changement liée et remplissez ses détails.
- **Sauvegarder les Modifications** : Assurez-vous que toutes les tâches ou demandes enfants sont sauvegardées.

---

### Étape 6 : Traiter les "Liens Associés"
Vous avez mentionné que les "liens associés" étaient vides. Il pourrait s'agir d'une confusion avec les listes associées (comme les incidents ou problèmes) plutôt qu'avec la section de l'interface utilisateur "Liens Associés" (Related Links). Pour renseigner les enregistrements associés :

- **Lier les Enregistrements Associés** :
  - Vérifiez les listes associées comme **Incidents Associés** (Related Incidents), **Problèmes Associés** (Related Problems) ou **Causé par le Changement** (Caused by Change).
  - Cliquez sur **Modifier** ou **Nouveau** dans ces listes.
  - Recherchez et liez les enregistrements pertinents (par exemple, un incident ayant déclenché ce changement).
- **Sauvegarder** : Mettez à jour le formulaire après avoir ajouté ces liens.

---

### Étape 7 : Faire Progresser la Demande de Changement
Une fois les informations de base et les listes associées renseignées, faites passer la demande de changement à l'étape suivante :

- **Vérifier l'État** (State) : Vérifiez l'état actuel (probablement "Nouveau" - New).
- **Passer à l'État Suivant** : Utilisez la liste déroulante **État** ou les actions UI (par exemple, **Évaluer** - Assess, **Autoriser** - Authorize) pour la faire avancer. Certains champs ou listes peuvent ne devenir pertinents que dans des états ultérieurs (par exemple, les dates réelles dans "Implémenter" - Implement).
- **Suivre le Workflow** : Le workflow de votre instance guidera le processus—complétez les champs requis à chaque étape.

---

### Notes Importantes
- **Permissions** : Assurez-vous d'avoir l'accès nécessaire (par exemple, le rôle `change_manager`) pour modifier ces champs et listes. Sinon, contactez votre administrateur ServiceNow.
- **Configuration Personnalisée** : Votre instance peut utiliser des modèles, des modèles de changement ou des workflows automatisés qui pré-remplissent certaines données. Vérifiez auprès de votre administrateur si les champs ne se comportent pas comme prévu.
- **Visibilité** : Certaines sections peuvent être masquées ou verrouillées en fonction de l'état ou de vos permissions—faire avancer l'état peut révéler plus d'options.

En suivant ces étapes, vous transformerez votre demande de changement vide en un enregistrement entièrement renseigné, prêt à être traité. Si les problèmes persistent, fournissez à votre administrateur ServiceNow les détails (par exemple, le numéro de la demande de changement) pour une investigation plus poussée.