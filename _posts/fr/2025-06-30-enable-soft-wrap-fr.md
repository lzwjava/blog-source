---
audio: false
generated: true
lang: fr
layout: post
title: Activer le retour à la ligne automatique dans Zed
translated: true
type: note
---

Zed, comme de nombreux éditeurs de texte modernes, utilise le concept de « retour à la ligne automatique » (soft wrap) pour gérer les lignes longues. Cela signifie que les lignes apparaîtront comme étant renvoyées à la ligne dans l'éditeur, mais aucun caractère de nouvelle ligne n'est réellement inséré dans votre fichier.

Voici comment activer le retour à la ligne automatique dans Zed :

1.  **Ouvrez les Paramètres de Zed :**

      * Appuyez sur `Cmd + Maj + P` (macOS) ou `Ctrl + Maj + P` (Windows/Linux) pour ouvrir la Palette de commandes.
      * Tapez "local" et sélectionnez "zed: Open Local Settings". Ceci ouvrira votre fichier `settings.json`.

2.  **Ajoutez le paramètre `soft_wrap` :**

      * Dans votre fichier `settings.json`, ajoutez ou modifiez le paramètre `"soft_wrap"`. Vous avez plusieurs options :

          * **`"editor_width"` :** C'est l'option la plus courante et généralement recommandée. Elle renvoie les lignes à la ligne pour s'adapter à la largeur actuelle de votre fenêtre d'édition.
            ```json
            {
              "soft_wrap": "editor_width"
            }
            ```
          * **`"preferred_line_length"` :** Cette option renvoie les lignes à la ligne en fonction d'une `preferred_line_length` spécifiée (par exemple, 80 caractères). Vous devrez également définir `preferred_line_length`.
            ```json
            {
              "soft_wrap": "preferred_line_length",
              "preferred_line_length": 80
            }
            ```
          * **`"bounded"` :** Cette option offre un comportement de renvoi plus avancé, bien que `editor_width` ou `preferred_line_length` soient généralement suffisants pour la plupart des utilisateurs.
          * **`"none"` :** Cette option désactive le retour à la ligne automatique.

3.  **Enregistrez le fichier :**

      * Appuyez sur `Cmd + S` (macOS) ou `Ctrl + S` (Windows/Linux) pour enregistrer le fichier `settings.json`.

Zed devrait maintenant renvoyer les lignes à la ligne selon le paramètre que vous avez choisi.

**Notes importantes :**

  * **Paramètres au niveau du projet :** Vous pouvez également activer le retour à la ligne automatique au niveau du projet en créant un dossier `.zed` dans le répertoire de votre projet et en y plaçant un fichier `settings.json` avec la configuration `soft_wrap` souhaitée. Ceci remplacera vos paramètres globaux pour ce projet spécifique.
  * **Paramètres spécifiques à un langage :** Vous pouvez même configurer `soft_wrap` pour des langages spécifiques. Par exemple, pour définir le retour à la ligne automatique pour les fichiers Markdown :
    ```json
    {
      "languages": {
        "Markdown": {
          "soft_wrap": "editor_width"
        }
      }
    }
    ```
  * **Commande "Rewrap" :** Si vous recherchez une commande pour "renvoyer" le texte (insérer de véritables nouvelles lignes) plutôt que de simplement le renvoyer visuellement, Zed dispose également d'une commande "Rewrap" (souvent associée à `Alt-Q` ou `Alt-W`). C'est utile pour formater des commentaires ou de longues lignes de texte.