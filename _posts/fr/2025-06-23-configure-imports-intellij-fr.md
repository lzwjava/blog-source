---
audio: false
generated: true
lang: fr
layout: post
title: Configuration des importations à classe unique dans IntelliJ IDEA
translated: true
type: note
---

IntelliJ IDEA propose des paramètres pour contrôler la façon dont il gère les imports, y compris pour empêcher l'utilisation des wildcards. Voici comment vous pouvez le configurer pour qu'il utilise toujours des imports de classe unique :

1.  **Ouvrir les Paramètres/Préférences :**
    * **Windows/Linux :** `Ctrl + Alt + S`
    * **macOS :** `Cmd + ,` (Virgule)

2.  **Accéder à Code Style pour Java :**
    * Dans le panneau de gauche de la boîte de dialogue Paramètres, naviguez vers :
        `Editor` -> `Code Style` -> `Java`

3.  **Aller dans l'onglet "Imports" :**
    * Sur le côté droit, sélectionnez l'onglet `Imports`.

4.  **Configurer les paramètres d'import :**
    Vous verrez quelques paramètres importants ici :

    * **`Use single class import`** : **Cochez cette case.** C'est le paramètre principal qui indique à IntelliJ de préférer les imports de classe individuels aux imports avec wildcard.

    * **`Class count to use import with '*'`** : Ce paramètre détermine le nombre de classes d'un même package qui doivent être importées avant qu'IntelliJ ne passe automatiquement à un import avec wildcard (par exemple, `java.util.*`). Pour désactiver efficacement les imports avec wildcard, **définissez ceci sur un nombre très élevé**, comme `999` ou `9999`. Cela garantit que vous n'atteindrez presque jamais le seuil pour un import avec wildcard.

    * **`Names count to use static import with '*'`** : Ceci est similaire au paramètre ci-dessus mais pour les imports statiques. Définissez-le également sur un nombre élevé (par exemple, `999` ou `9999`) pour empêcher les imports statiques avec wildcard.

    * **`Packages to Use Imports with '*'`** : Ce tableau liste les packages pour lesquels IntelliJ utilisera *toujours* des imports avec wildcard, indépendamment des autres paramètres. **Assurez-vous que ce tableau est vide** si vous voulez éviter complètement les imports avec wildcard. Si vous voyez des entrées comme `java.util.*` ou `java.awt.*`, supprimez-les.

5.  **Appliquer les modifications :**
    * Cliquez sur `Apply` puis sur `OK` pour enregistrer vos modifications.

**Après avoir effectué ces changements :**

* Lorsque vous utilisez la fonctionnalité "Auto Import" (par exemple, en appuyant sur `Alt + Entrée` sur une classe non résolue), IntelliJ insérera désormais des imports de classe individuels au lieu de wildcards.
* Si vous avez des fichiers existants avec des imports avec wildcard, vous pouvez utiliser l'action "Optimize Imports" (`Ctrl + Alt + O` sur Windows/Linux, `Cmd + Option + O` sur macOS) pour les convertir en imports de classe unique selon vos nouveaux paramètres.

En suivant ces étapes, vous pouvez empêcher efficacement IntelliJ IDEA d'utiliser des imports avec wildcard pour les fichiers Java.