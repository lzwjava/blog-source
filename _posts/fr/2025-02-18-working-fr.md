---
audio: true
lang: fr
layout: post
title: Travail
translated: true
---

- Avant d'accéder au dépôt de code, demandez à vos collègues le fichier `pom.xml` et essayez de télécharger les dépendances Nexus.

- Sans le code réel mais avec les bibliothèques Nexus, nous pouvons effectivement décompiler le JAR ou expérimenter avec les bibliothèques. Nous pouvons faire beaucoup de choses. Pensez en dehors de la boîte.

- Il est préférable de configurer les jetons utilisateur dans le dépôt Sonatype Nexus Repository dans `settings.yaml`.

- Ne vous attendez pas à l'approbation des tickets de demande d'accès. Avant d'avoir les droits d'accès, pensez à ce que vous pouvez faire.

- Beaucoup du travail peut être fait avant de commencer à travailler. On peut se familiariser avec presque tout à l'avance. Tout a un code ou des matériaux de substitution open-source.

- Un travail implique souvent des paramètres spécifiques, une logique de code légèrement différente et des droits d'accès ou des mots de passe pour faire les choses.

- Prévoyez la prochaine phase du projet. Pensez à la manière dont le projet actuel progressera et à ce que les utilisateurs auront besoin ou attendront.

- Pensez à toutes les façons possibles de faire le travail, de faire des progrès et de vous préparer autant que possible avant d'obtenir les droits d'accès ou les matériaux que les autres fourniront.

- Ne vous contentez pas de faire les choses; faites-les et automatisez autant que possible.

- Utilisez la bibliothèque Python `requests` pour remplacer Postman.

- Windows et PowerShell sont également des options viables. Les commandes couramment utilisées sont limitées à quelques dizaines. Apprenez-les bien.

- Pensez à la manière dont un ingénieur pourrait travailler sur ce projet pendant 5 ou 10 ans, et réfléchissez à la manière d'atteindre une efficacité similaire rapidement.

- Utilisez les répertoires de notes et de journaux. Copiez soigneusement les journaux de la console ou des pages frontend pour une analyse détaillée.

- Pensez à la manière de transmettre cette connaissance aux nouveaux membres de l'équipe.

- Pensez à ce que nous pouvons accomplir si tout le monde fait de son mieux et que nous avons 50 ingénieurs de ce type.

- Les bibliothèques qui peuvent être facilement téléchargées à partir des dépôts Nexus internes peuvent être téléchargées manuellement et placées dans le dépôt `.m2`.

- Lisez le fichier `pom.xml` pour déterminer la cible de compilation Maven et la version JDK requise pour le projet.

- Au lieu de rechercher dans Jira ou Confluence, construisez directement une URL pour accéder au profil et localiser les pages.

- Si nous rencontrons un bug, par exemple si `npm run build` a des problèmes dans un grand pipeline de construction, nous pouvons l'exécuter séparément pour nous assurer qu'il fonctionne avant d'exécuter l'ensemble du pipeline. Cela rend le cycle de débogage plus rapide et plus petit.