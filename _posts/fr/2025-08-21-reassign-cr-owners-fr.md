---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Comment réassigner les propriétaires de demandes de changement
translated: true
type: note
---

Changer le propriétaire d’une **Demande de changement (CR)** dépend de l’outil ou du système de flux de travail que vous utilisez (par exemple, ServiceNow, Jira, HP ALM, ou un outil ITSM personnalisé). Mais le processus général est généralement similaire sur toutes les plateformes :

---

### 1. Localiser la Demande de Changement

* Accédez à la section **Gestion des changements** ou **Demandes** de votre outil ITSM.
* Recherchez la CR par ID, titre ou d’autres filtres.
* Ouvrez la page de détails de la CR.

---

### 2. Trouver le champ « Propriétaire » ou « Assigné à »

* La plupart des systèmes ont un champ comme **Propriétaire du changement**, **Assigné à** ou **Personne responsable**.
* Ce champ contrôle qui est responsable de la CR.
* Si vous ne le voyez pas immédiatement, vérifiez sous les onglets **Assignation** ou **Propriété**.

---

### 3. Mettre à jour le propriétaire

* Cliquez sur **Modifier** la CR.
* Changez la valeur du champ **Propriétaire** (ou « Assigné à ») pour la nouvelle personne.
* Cela se fait généralement en sélectionnant un nom dans une liste déroulante d'utilisateurs.
* Enregistrez ou soumettez la mise à jour.

---

### 4. Vérifier les exigences de Rôle/Permission

* Certains systèmes restreignent les changements de propriétaire à des rôles spécifiques (par exemple, **Change Manager**, **Admin**).
* Si vous n'avez pas la permission, vous devrez demander à un Change Manager ou à un Administrateur de la mettre à jour pour vous.

---

### 5. Notifier les Parties Prenantes

* Bonne pratique : ajoutez un **commentaire** ou une **note de travail** dans la CR expliquant pourquoi la propriété a changé.
* Notifiez le nouveau propriétaire afin qu'il soit conscient de la responsabilité.

---

✅ **Exemple (ServiceNow)**

1. Ouvrez la Demande de Changement.
2. Dans le champ « Assigné à », sélectionnez le nouvel utilisateur.
3. Enregistrez l'enregistrement.

✅ **Exemple (Jira)**

1. Ouvrez le ticket de la Demande de Changement.
2. Cliquez sur le champ « Assigné à ».
3. Sélectionnez le nouveau propriétaire.

---

Souhaitez-vous que je vous donne **des instructions étape par étape pour un système spécifique** (comme ServiceNow, Jira ou HP ALM) ?