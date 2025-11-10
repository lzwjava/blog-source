---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Renommer des Fichiers avec PyCharm en Toute Sécurité et Intelligemment
translated: true
type: note
---

Oui — si vous utilisez **la fonction de refactoring de PyCharm** (clic droit sur le fichier → Refactor → Rename, ou appuyez sur `Shift+F6` sur le nom du fichier), cela ne renommera pas seulement le fichier sur le disque mais mettra également à jour **toutes les références et les instructions d'importation** qui pointent vers lui, tant qu'elles sont résolvables à l'intérieur du projet.

Quelques détails importants à garder à l'esprit :

* **Portée du refactoring** : PyCharm analyse l'ensemble de votre projet, donc les imports dans d'autres fichiers Python du projet seront mis à jour automatiquement.
* **Imports non résolus / dynamiques** : Si certains imports sont construits dynamiquement (par exemple en utilisant `__import__`, `importlib`, ou des chemins de modules basés sur des chaînes de caractères), PyCharm ne les détectera pas, donc ils ne seront pas mis à jour.
* **Racines multiples / scripts externes** : Si d'autres scripts sont en dehors du projet PyCharm ou ne sont pas indexés (par exemple, pas dans vos racines sources du projet), PyCharm ne les capturera pas non plus.
* **Tests et imports relatifs** : Si vous utilisez des imports relatifs (`from . import something`) et que la structure des dossiers change, vous devrez peut-être vérifier cela séparément.

Ainsi, pour les cas normaux de `import mymodule.something` à l'intérieur de votre projet, le renommage avec le refactoring de PyCharm maintiendra tout cohérent.

Voulez-vous que j'explique également **comment tester en toute sécurité après un renommage** pour être sûr que rien n'a été cassé ?