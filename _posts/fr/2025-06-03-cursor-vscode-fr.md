---
audio: false
generated: true
lang: fr
layout: post
title: Curseur et VS Code
translated: true
type: note
---

Oui, il est légal pour Cursor de forker Visual Studio Code (VS Code) et de construire une entreprise autour, à condition de respecter les termes de la licence MIT sous laquelle le code source de VS Code est publié. La licence MIT est très permissive, permettant à quiconque d'utiliser, copier, modifier, fusionner, publier, distribuer, sous-licencier et vendre des copies du logiciel, à condition que l'avis de copyright original et l'avis d'autorisation soient inclus dans toutes les copies ou parties substantielles du logiciel.

Voici les points clés concernant la légalité du fork de Cursor :

1.  **Conformité à la Licence MIT** : Le code source de VS Code, disponible sur le dépôt GitHub `vscode`, est sous licence MIT. Cela permet à Cursor de forker le codebase, de le modifier et de l'utiliser à des fins commerciales, y compris pour créer un produit propriétaire, à condition d'inclure la licence MIT originale et l'avis de copyright dans leur distribution. La licence MIT n'exige pas que le projet forké reste open-source, Cursor peut donc légalement rendre son produit propriétaire.

2.  **Visual Studio Code vs. Code-OSS** : Il existe une distinction entre le dépôt open-source `vscode` (souvent appelé Code-OSS) et le produit Microsoft Visual Studio Code. Le VS Code de Microsoft inclut des ajouts propriétaires (par exemple, la télémétrie, l'intégration du marketplace) et est distribué sous une licence différente. Cependant, forker le dépôt open-source `vscode`, qui est sous licence MIT, est ce que Cursor et des projets similaires comme Windsurf ont fait. Ceci est explicitement autorisé, et ils peuvent construire leurs propres personnalisations par-dessus.

3.  **Restrictions du Visual Studio Marketplace** : Une limitation importante pour les forks comme Cursor est qu'ils ne peuvent pas accéder au Visual Studio Marketplace officiel en raison des Conditions d'Utilisation de Microsoft. Cela signifie que Cursor ne peut pas offrir le même écosystème d'extensions que VS Code, à moins de mettre en place un registre d'extensions alternatif (par exemple, OpenVSX) ou de développer le leur. De plus, certaines extensions propriétaires, comme GitHub Copilot ou les extensions C/C++ de Microsoft, sont restreintes aux builds officielles de VS Code de Microsoft, ce qui peut limiter la fonctionnalité des forks.

4.  **Préoccupations Éthiques et Communautaires** : Bien que forker soit légal sous la licence MIT, certains ont soulevé des préoccupations éthiques concernant des entreprises comme Cursor qui prennent un projet open-source, ajoutent des fonctionnalités et le vendent comme un produit propriétaire sans contribuer en retour à la communauté VS Code originale. Par exemple, des publications sur X ont exprimé des sentiments mitigés, certains utilisateurs se demandant s'il est juste que Cursor profite d'un code largement développé par l'équipe VS Code. Cependant, il s'agit d'un débat moral, et non légal, et la licence MIT autorise explicitement une telle utilisation.

5.  **La Réponse de Microsoft** : Microsoft a pris des mesures pour protéger son écosystème, telles que restreindre l'accès au marketplace et les extensions propriétaires pour les forks, comme on l'a vu avec des actions telles que la suppression du support des extensions C/C++ pour les builds non officielles. Cependant, ces restrictions n'affectent pas la légalité du fork du dépôt `vscode` lui-même, tant que le fork respecte la licence MIT.

En résumé, le fork de VS Code par Cursor est légal sous la licence MIT, car ils sont libres de modifier et de commercialiser le codebase, à condition d'inclure les avis de copyright et de licence requis. Les principaux défis auxquels ils sont confrontés sont pratiques - tels que le manque d'accès au VS Code Marketplace et à certaines extensions propriétaires - plutôt que des barrières légales. Si vous avez des inquiétudes concernant des aspects spécifiques de la mise en œuvre ou de la conformité de Cursor, consulter un professionnel du droit de votre juridiction est conseillé, car je ne suis pas avocat.