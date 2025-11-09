---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Configuration de l'assistant de smileys CodeIgniter
translated: true
type: note
---

### Aperçu
Il s'agit d'un fichier de configuration PHP du framework web CodeIgniter, spécifiquement pour son **helper emoticônes/smileys**. CodeIgniter est un framework PHP MVC pour créer des applications web. Ce fichier définit un ensemble de mappages de smileys/émoticônes utilisés par le `smiley_helper` du framework pour remplacer automatiquement les émoticônes textuelles (comme `:-)`) par des balises HTML `<img>` qui affichent les images GIF correspondantes.

Le fichier bloque l'accès direct via `defined('BASEPATH') OR exit('No direct script access allowed');`, une mesure de sécurité dans CodeIgniter pour empêcher l'exécution directe non autorisée de scripts.

### Composants principaux
- **Objectif** : Convertit les émoticônes en texte brut dans le contenu généré par les utilisateurs (par exemple, les messages de forum ou les commentaires) en images visuelles pour une meilleure expérience utilisateur.
- **Structure de données** : `$smileys` est un tableau associatif PHP avec la structure formelle :
  ```
  $smileys = array(
      'smiley_code' => array('image_file', 'width', 'height', 'alt_text'),
      // ...
  );
  ```
  - **smiley_code** : Le motif textuel à correspondre (par exemple, `:-)`, `:lol:`, `>:(`).
  - **image_file** : Nom de l'image GIF dans le répertoire des smileys (par défaut `application/views/smileys/` dans CodeIgniter).
  - **width/height** : Dimensions en pixels pour la balise `<img>` (toutes sont `'19'` ici, indiquant des GIFs de 19x19px).
  - **alt_text** : Texte alternatif pour l'accessibilité/les lecteurs d'écran, décrivant l'émotion.

- **Utilisation dans CodeIgniter** : Chargez le helper avec `$this->load->helper('smiley');`, puis appelez des fonctions comme `parse_smileys($text)` sur les chaînes contenant les codes d'émoticônes. Cela remplace les codes par des balises `<img>`, par exemple :
  - Entrée : `I'm happy :)`
    Sortie : `I'm happy <img src="http://example.com/smileys/smile.gif" width="19" height="19" alt="smile">`

### Détail des entrées
Le tableau comprend plus de 40 mappages groupés par type d'émotion. La plupart des images sont des GIFs de 19x19px. Voici une vue résumée (avec des exemples) :

| Code(s) Smiley | Image | Texte Alt | Notes |
|---------------|-------|----------|-------|
| `:-)`, `:)` | grin.gif, smile.gif | grin, smile | Sourires et sourires positifs. |
| `:lol:`, `:cheese:` | lol.gif, cheese.gif | LOL, cheese | Rire/pouce levé, sourire en coin. |
| `;-)`, `;)` | wink.gif | wink | Clin d'œil. |
| `:smirk:`, `:roll:` | smirk.gif, rolleyes.gif | smirk, rolleyes | Sarcasme/hochement de tête sage. |
| `:-S`, `:wow:`, `:bug:` | confused.gif, surprise.gif, bigsurprise.gif | confused, surprised, big surprise | Confusion/surprise. |
| `:-P`, `%-P`, `;-P`, `:P` | tongue_laugh.gif, etc. | tongue laugh, etc. | Variantes avec la langue tirée (riant, clin d'œil, framboise). |
| `:blank:`, `:long:`, `:ohh:`, `:grrr:`, `:gulp:`, `8-/` | Divers | blank stare, long face, ohh, grrr, gulp, oh oh | Expressions neutres ou agacées. |
| `:down:`, `:red:`, `:sick:`, `:shut:` | Divers | downer, red face, sick, shut eye | Triste, embarrassé, malade. |
| `:-/`, `>:(` (`:mad:`), `>:-(` (`:angry:`) | hmm.gif, mad.gif, angry.gif | hmmm, mad, angry | Confus, fâché, en colère. |
| `:zip:`, `:kiss:` | zip.gif, kiss.gif | zipper, kiss | Bouche fermée à clé, bisou. |
| `:ahhh:`, `:coolsmile:`, `-:coolsmirk:`, `:coolgrin:`, `:coolhmm:`, `:coolmad:`, `:coolcheese:` | shock.gif, shade_smile.gif, etc. | shock, cool smile, cool smirk, cool grin, cool hmm, cool mad, cool cheese | Variantes choquées ou "cool"/lunettes de soleil. |
| `:vampire:`, `:snake:` | vampire.gif, snake.gif | vampire, snake | Émoticônes à thème. |
| `:exclaim:`, `:question:` | exclaim.gif, question.gif | exclaim, question | Équivalents de ponctuation (!, ?). |

### Extension et personnalisation
- **Ajouter des Smileys** : Ajoutez de nouvelles entrées, par exemple, `':fire:' => array('fire.gif', '19', '19', 'fire');`.
- **Changer les images** : Mettez à jour les noms de fichiers si vous remplacez les GIFs par des PNGs/JPGs (ajustez la largeur et la hauteur en conséquence).
- **Répertoire** : Assurez-vous que les images existent dans le chemin des smileys de CodeIgniter.
- **Limitations** : Toutes les images ici ont la même taille ; les implémentations réelles peuvent varier. Ce tableau ne définit que les mappages—la logique de remplacement se trouve dans le helper lui-même.

Si vous avez une question spécifique sur la personnalisation ou l'utilisation de ceci dans CodeIgniter, fournissez plus de détails !