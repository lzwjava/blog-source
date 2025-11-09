---
audio: false
date: 2025-09-11
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Comportement du Fichier d'Exécution Runtime JaCoCo
translated: true
type: note
---

Lorsque vous exécutez **WebSphere Liberty Profile** avec l'**agent JaCoCo** en mode `exec`, l'agent JaCoCo **ne modifie pas** le fichier `.exec` original pendant l'exécution. Voici ce qui se passe :

---

### Fonctionnement de JaCoCo en mode `exec`
- **Objectif** : L'agent JaCoCo collecte les **données de couverture de code** pendant l'exécution de votre application.
- **Sortie** : Il écrit les données de couverture dans le fichier `.exec` (par exemple, `jacoco.exec`).
- **Comportement du fichier** :
  - Si le fichier **n'existe pas**, JaCoCo le crée.
  - Si le fichier **existe déjà**, JaCoCo **ajoute** les nouvelles données de couverture (il ne remplace pas ni ne modifie les données existantes, sauf si vous réinitialisez ou fusionnez explicitement le fichier).
  - Le fichier `.exec` original **n'est pas altéré** d'une manière qui pourrait casser ou changer sa structure—il s'enrichit uniquement avec de nouvelles données.

---

### Le fichier `.exec` sera-t-il modifié ?
- **Oui, mais uniquement par ajout de données** : Le fichier sera mis à jour avec de nouvelles informations de couverture chaque fois que vous exécutez votre application avec l'agent JaCoCo.
- **Aucun changement structurel** : Le format du fichier `.exec` reste le même ; c'est un fichier binaire contenant des données de couverture.

---

### Bonnes pratiques
- **Fusionner ou Réinitialiser** : Si vous souhaitez recommencer à zéro, supprimez ou renommez le fichier `.exec` avant de relancer votre application.
- **Fusionner des Exécutions Multiples** : Utilisez le goal `jacoco:merge` (dans Maven) ou la classe `org.jacoco.agent.rt.RT` pour fusionner plusieurs fichiers `.exec` si nécessaire.

---

### Exemple de Configuration Liberty
Dans votre `server.env` ou `jvm.options` pour Liberty, vous pourriez voir :
```bash
-javaagent:/chemin/vers/jacocoagent.jar=destfile=/chemin/vers/jacoco.exec,append=true
```
- `append=true` garantit que les nouvelles données sont ajoutées au fichier existant.

---