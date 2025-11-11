---
audio: false
generated: true
lang: fr
layout: post
title: Retour à la ligne dans VSCode
translated: true
type: note
---

Pour que VSCode effectue un retour à la ligne afin de visualiser facilement quand les lignes sont trop longues, vous pouvez configurer les paramètres de retour à la ligne pour qu'elles se coupent à une colonne spécifique. Voici comment procéder :

### Étapes pour activer le retour à la ligne à une colonne spécifique

1. **Ouvrir les Paramètres dans VSCode** :
   - Appuyez sur `Ctrl + ,` (ou `Cmd + ,` sur macOS) pour ouvrir le panneau des Paramètres.
   - Alternativement, allez dans `Fichier` > `Préférences` > `Paramètres`.

2. **Rechercher les paramètres de retour à la ligne** :
   - Dans le panneau des Paramètres, tapez "word wrap" dans la barre de recherche.
   - Localisez le paramètre intitulé **Editor: Word Wrap**.

3. **Définir le retour à la ligne sur "wordWrapColumn"** :
   - Modifiez le paramètre **Editor: Word Wrap** en le réglant sur `"wordWrapColumn"`.
   - Cette option permet aux lignes de se couper à une colonne spécifique.

4. **Spécifier la limite de colonne** :
   - Recherchez le paramètre **Editor: Word Wrap Column** (il apparaît lorsque "wordWrapColumn" est sélectionné).
   - Définissez-le sur votre limite de colonne préférée, par exemple, `80`.
   - Cela signifie que toute ligne dépassant 80 caractères sera coupée.

5. **(Optionnel) Ajouter une règle verticale pour un repère visuel** :
   - Recherchez "rulers" dans la barre de recherche des Paramètres.
   - Trouvez le paramètre **Editor: Rulers**.
   - Ajoutez votre colonne préférée à la liste, par exemple, `[80]`.
   - Cela affichera une ligne verticale à la colonne 80, fournissant un repère visuel pour la limite de longueur de ligne.

6. **(Optionnel) Ajuster l'indentation des lignes coupées pour plus de clarté** :
   - Recherchez "wrapping indent" dans la barre de recherche des Paramètres.
   - Trouvez le paramètre **Editor: Wrapping Indent**.
   - Définissez-le sur `"indent"` (ou une autre option comme `"deepIndent"`) pour indenter les lignes coupées.
   - Cela aide à distinguer les lignes coupées des nouvelles lignes, rendant plus clair le fait qu'elles sont des continuations.

### Comment cela fonctionne

- Après avoir configuré ces paramètres, toute ligne dépassant la colonne spécifiée (par exemple, 80 caractères) sera coupée et affichée sur plusieurs lignes visuelles.
- Les lignes coupées sont indentées (si vous avez ajusté l'indentation), ce qui permet de voir facilement qu'elles font partie de la même ligne logique.
- La règle verticale (si elle est activée) affiche une ligne à la colonne spécifiée, renforçant la limite visuelle.
- En remarquant qu'une ligne est coupée, vous pouvez rapidement identifier qu'elle est trop longue, car elle dépasse votre limite de colonne.

### Exemple

Supposons que vous ayez une ligne de code de 100 caractères :
- Avec **Editor: Word Wrap** réglé sur `"wordWrapColumn"` et **Editor: Word Wrap Column** réglé sur `80`, la ligne se coupera au 80ème caractère.
- La partie coupée sera indentée, et la règle (si elle est activée) montrera où se trouve la 80ème colonne.
- Cette configuration élimine le besoin de faire défiler horizontalement et rend clair le fait que la ligne dépasse 80 caractères.

### Notes supplémentaires

- Le retour à la ligne est purement visuel ; le code actuel reste une seule ligne logique, donc cela n'affectera pas l'exécution ou le formatage de votre code.
- Si vous souhaitez appliquer des limites strictes de longueur de ligne, envisagez d'utiliser des linters ou des formateurs en plus de ces paramètres visuels.
- Pour des vérifications rapides, vous pouvez également consulter la barre d'état dans VSCode, qui affiche le numéro de la ligne et de la colonne actuelles, mais le retour à la ligne et la règle devraient suffire pour une identification visuelle.

En suivant ces étapes, vous pouvez facilement voir quand les lignes sont trop longues dans VSCode sans avoir à faire défiler horizontalement, car elles seront coupées à votre limite de colonne spécifiée.