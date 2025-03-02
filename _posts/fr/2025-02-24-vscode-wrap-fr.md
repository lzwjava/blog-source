---
audio: false
generated: true
lang: fr
layout: post
title: VSCode Envelopper les lignes
translated: true
---

Pour faire en sorte que VSCode enroule les lignes afin que vous puissiez facilement voir quand les lignes sont trop longues, vous pouvez configurer les paramètres d'enroulement des mots pour enrouler les lignes à une colonne spécifique. Voici comment faire :

### Étapes pour activer l'enroulement des lignes à une colonne spécifique

1. **Ouvrir les paramètres dans VSCode** :
   - Appuyez sur `Ctrl + ,` (ou `Cmd + ,` sur macOS) pour ouvrir le panneau des paramètres.
   - Alternativement, allez dans `Fichier` > `Préférences` > `Paramètres`.

2. **Rechercher les paramètres d'enroulement des mots** :
   - Dans le panneau des paramètres, tapez "word wrap" dans la barre de recherche.
   - Localisez le paramètre étiqueté **Editor: Word Wrap**.

3. **Définir l'enroulement des mots sur "wordWrapColumn"** :
   - Changez le paramètre **Editor: Word Wrap** en `"wordWrapColumn"`.
   - Cette option permet aux lignes de s'enrouler à une colonne spécifique.

4. **Spécifier la limite de colonne** :
   - Recherchez le paramètre **Editor: Word Wrap Column** (il apparaît lorsque "wordWrapColumn" est sélectionné).
   - Définissez-le sur votre limite de colonne préférée, par exemple, `80`.
   - Cela signifie que toute ligne plus longue que 80 caractères sera enroulée.

5. **(Facultatif) Ajouter une règle verticale pour une guidance visuelle** :
   - Recherchez "rulers" dans la barre de recherche des paramètres.
   - Trouvez le paramètre **Editor: Rulers**.
   - Ajoutez votre colonne préférée à la liste, par exemple, `[80]`.
   - Cela affichera une ligne verticale à la colonne 80, fournissant une indication visuelle de la limite de longueur de ligne.

6. **(Facultatif) Ajustez l'indentation de l'enroulement pour plus de clarté** :
   - Recherchez "wrapping indent" dans la barre de recherche des paramètres.
   - Trouvez le paramètre **Editor: Wrapping Indent**.
   - Définissez-le sur `"indent"` (ou une autre option comme `"deepIndent"`) pour indenter les lignes enroulées.
   - Cela aide à distinguer les lignes enroulées des nouvelles lignes, rendant plus clair qu'elles sont des continuations.

### Comment cela fonctionne

- Après avoir configuré ces paramètres, toute ligne dépassant la colonne spécifiée (par exemple, 80 caractères) sera enroulée et affichée sur plusieurs lignes visuelles.
- Les lignes enroulées sont indentées (si vous avez ajusté l'indentation de l'enroulement), ce qui permet de voir facilement qu'elles font partie de la même ligne logique.
- La règle verticale (si activée) montre une ligne à la colonne spécifiée, renforçant la limite visuelle.
- En remarquant qu'une ligne est enroulée, vous pouvez rapidement constater qu'elle est trop longue, car elle dépasse votre limite de colonne.

### Exemple

Supposons que vous avez une ligne de code qui fait 100 caractères de long :
- Avec **Editor: Word Wrap** défini sur `"wordWrapColumn"` et **Editor: Word Wrap Column** défini sur `80`, la ligne s'enroulera au 80ème caractère.
- La partie enroulée sera indentée, et la règle (si activée) montrera où se trouve la 80ème colonne.
- Cette configuration élimine le besoin de faire défiler horizontalement et rend clair que la ligne dépasse 80 caractères.

### Notes supplémentaires

- L'enroulement est purement visuel ; le code réel reste une seule ligne logique, donc cela n'affectera pas la manière dont votre code s'exécute ou est formaté.
- Si vous souhaitez imposer des limites de longueur de ligne strictes, envisagez d'utiliser des linteurs ou des formatteurs en plus de ces paramètres visuels.
- Pour des vérifications rapides, vous pouvez également vous référer à la barre d'état dans VSCode, qui affiche le numéro de ligne et de colonne actuel, mais l'enroulement et la règle devraient suffire pour l'identification visuelle.

En suivant ces étapes, vous pouvez facilement voir quand les lignes sont trop longues dans VSCode sans avoir à faire défiler horizontalement, car elles seront enroulées à votre limite de colonne spécifiée.