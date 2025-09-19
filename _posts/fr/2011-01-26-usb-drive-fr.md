---
audio: false
generated: false
image: false
lang: fr
layout: post
title: Personnalisez votre clé USB avec un fond d'écran et une icône
translated: true
---

Ce message a initialement été rédigé en chinois et publié sur Qzone.

---

**I. Personnaliser l'icône de la clé USB :**

1. Choisissez d'abord une icône qui vous plaît. L'extension du fichier de l'icône doit être `.ico`.
2. Copiez le fichier icône sur votre clé USB et créez un nouveau document texte sur la clé USB.
3. Dans le document texte, écrivez ce qui suit :
   ```
   [autorun]
   ICON=\xxx.ico,0
   ```
   Où `xxx.ico` est le nom de votre fichier icône (y compris l'extension).
4. Enregistrez le fichier texte sous le nom `autorun.inf`.
   **Note :** Il est crucial de changer l'extension en `.inf`, et non en `.txt`. Si l'icône du fichier change en une avec un engrenage jaune, vous l'avez fait correctement.
   Déconnectez la clé USB et reconnectez-la. Vous verrez que l'icône de la clé USB a changé pour celle que vous avez sélectionnée.
   Cette méthode peut également être utilisée pour les disques durs externes ou le gravage de CD/DVD.

**II. Personnaliser l'arrière-plan :**

1. Choisissez d'abord une image d'arrière-plan que vous aimez et copiez-la sur votre clé USB.
2. Créez un nouveau fichier texte et copiez ce qui suit à l'intérieur :
   ```
   [ExtShellFolderViews]
   {BE098140-A513-11D0-A3A4-00C04FD706EC}={BE098140-A513-11D0-A3A4-00C04FD706EC}
   [{BE098140-A513-11D0-A3A4-00C04FD706EC}]
   Attributes=1
   IconArea_Image=aaa.jpg
   IconArea_Text=0x00FFFFFF
   [.ShellClassInfo]
   ConfirmFileOp=0
   ```
   Ce code signifie :

   Où `aaa.jpg` est le nom de votre fichier d'image choisi (y compris l'extension).

   `IconArea_Text=0x00FFFFFF`  Cette ligne change la couleur du texte sur la clé USB.

   Les codes de couleur sont :

   *   Rouge : `0x000000FF`
   *   Jaune : `0x0000FFFF`
   *   Bleu : `0x00FF0000`
   *   Gris : `0x00808080`
   *   Vert lime : `0x006BDEC7`
   *   Noir : `0x00000000`
   *   Couleur de fond Excel : `0x00848284`
   *   Blanc : `0x00FFFFFF`
   *   Vert : `0x00008000`
   *   Violet : `0x00C000C0`

   Choisissez une couleur qui vous plaît (qui complemende votre arrière-plan) et remplacez le code de couleur existant.

   Vous pouvez changer la couleur après `IconArea_Text=` en votre couleur préférée.

3. Enregistrez le fichier texte sous le nom `Desktop.ini`. La modification est terminée.
   Rafraîchissez la clé USB et vous devriez voir les modifications.
   Tous les quatre fichiers mentionnés ci-dessus peuvent être cachés pour éviter une suppression accidentelle.
   Après avoir changé l'icône, vous devez déconnecter et reconnecter la clé USB pour voir l'effet.
   Après avoir changé l'arrière-plan, rafraîchissez la clé USB pour voir les changements.