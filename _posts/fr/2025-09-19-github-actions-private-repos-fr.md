---
audio: false
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Guide des GitHub Actions pour les dépôts privés
translated: true
type: note
---

Oui, les dépôts privés peuvent également utiliser GitHub Actions. Cependant, il existe quelques différences par rapport aux dépôts publics :

1. **Limites d'utilisation** :

   * **Offre gratuite** : Pour les dépôts privés, GitHub fournit un nombre limité de minutes pour Actions dans l'offre gratuite, selon le type de compte (par exemple, individuel ou organisation). Vous pouvez utiliser GitHub Actions gratuitement avec certaines limitations d'utilisation.
   * **Comptes payants** : Les formules payantes, telles que GitHub Pro, GitHub Team ou GitHub Enterprise, fournissent des minutes supplémentaires pour Actions.

2. **Gestion des secrets** :

   * Vous pouvez utiliser GitHub Actions avec des **secrets** dans les dépôts privés (pour des éléments comme des clés API, des jetons, etc.). Les secrets sont chiffrés et peuvent être utilisés en toute sécurité dans vos workflows.

3. **Dépendances externes** :

   * Certaines actions ou intégrations (comme des workflows externes ou des actions du marketplace GitHub) peuvent nécessiter des autorisations ou un accès supplémentaires, qui peuvent être gérés pour les dépôts privés.

4. **Actions publiques vs privées** :

   * Vous pouvez toujours créer des **actions privées** au sein de votre organisation, mais vous devrez peut-être vous assurer que les autorisations nécessaires sont configurées, en particulier pour les workflows collaboratifs ou en équipe.

En résumé, les dépôts privés peuvent utiliser GitHub Actions sans restrictions autres que les limites d'utilisation basées sur votre forfait. L'essentiel est de s'assurer que les secrets et les workflows sont correctement configurés.