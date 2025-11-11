---
audio: false
generated: true
lang: fr
layout: post
title: Téléchargement VSIX de VS Code
translated: true
type: note
---

Pour télécharger manuellement un fichier `.vsix` pour une extension Visual Studio Code (VS Code), vous pouvez utiliser le Visual Studio Marketplace, qui héberge toutes les extensions officielles. Le fichier `.vsix` est le format empaqueté pour les extensions VS Code, et bien que le Marketplace ne fournisse pas toujours un bouton de téléchargement direct, vous pouvez construire l'URL de téléchargement ou utiliser des méthodes alternatives. Voici comment procéder étape par étape :

### Étapes pour télécharger manuellement un fichier `.vsix`

1. **Trouver l'extension sur le Visual Studio Marketplace**  
   - Allez sur le [Visual Studio Marketplace](https://marketplace.visualstudio.com/vscode) dans votre navigateur web.
   - Recherchez l'extension que vous voulez (par exemple, "Python" par Microsoft, "Prettier - Code formatter", etc.).
   - Ouvrez la page de l'extension. Par exemple, l'URL de l'extension Python pourrait ressembler à :  
     `https://marketplace.visualstudio.com/items?itemName=ms-python.python`.

2. **Identifier l'éditeur et le nom de l'extension**  
   - Sur la page de l'extension, notez l'**éditeur** et l'**identifiant de l'extension**. Ceux-ci font partie de l'URL ou sont affichés sur la page.
   - Par exemple, dans `ms-python.python`, `ms-python` est l'éditeur, et `python` est le nom de l'extension.

3. **Construire l'URL de téléchargement**  
   - Le fichier `.vsix` peut être téléchargé directement en utilisant un modèle d'URL spécifique fourni par le Marketplace. Le format général est :  
     ```
     https://<publisher>.gallery.vsassets.io/_apis/public/gallery/publisher/<publisher>/extension/<extension-name>/latest/assetbyname/Microsoft.VisualStudio.Services.VSIXPackage
     ```
   - Remplacez `<publisher>` par le nom de l'éditeur et `<extension-name>` par le nom de l'extension.
   - Pour l'extension Python (`ms-python.python`), l'URL serait :  
     ```
     https://ms-python.gallery.vsassets.io/_apis/public/gallery/publisher/ms-python/extension/python/latest/assetbyname/Microsoft.VisualStudio.Services.VSIXPackage
     ```
   - Collez cette URL dans votre navigateur, et cela déclenchera le téléchargement du fichier `.vsix`.

4. **Alternative : Utiliser le lien "Télécharger l'extension" sur la page du Marketplace (s'il est disponible)**  
   - Certaines pages d'extension incluent un lien "Télécharger l'extension" dans la section **Resources** ou ailleurs. S'il est présent, cliquez dessus pour télécharger le fichier `.vsix` directement. Cependant, cela est moins courant, donc la méthode par URL est plus fiable.

5. **Vérifier le téléchargement**  
   - Le fichier téléchargé aura une extension `.vsix` (par exemple, `ms-python.python-<version>.vsix`).
   - Vérifiez la taille et le nom du fichier pour vous assurer qu'il correspond à l'extension et à la version attendues.

6. **Installer le fichier `.vsix` dans VS Code (Optionnel)**  
   - Ouvrez VS Code.
   - Allez dans la vue Extensions (`Ctrl+Shift+X` ou `Cmd+Shift+X` sur macOS).
   - Cliquez sur le menu à trois points (`...`) en haut à droite du volet Extensions.
   - Sélectionnez **Install from VSIX**, puis naviguez et sélectionnez le fichier `.vsix` téléchargé.

### Exemple détaillé
Disons que vous voulez l'extension **ESLint** par Dirk Baeumer :
- URL du Marketplace : `https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint`
- Éditeur : `dbaeumer`
- Nom de l'extension : `vscode-eslint`
- URL de téléchargement :  
  ```
  https://dbaeumer.gallery.vsassets.io/_apis/public/gallery/publisher/dbaeumer/extension/vscode-eslint/latest/assetbyname/Microsoft.VisualStudio.Services.VSIXPackage
  ```
- Ouvrez cette URL dans votre navigateur, et le fichier `.vsix` (par exemple, `dbaeumer.vscode-eslint-<version>.vsix`) sera téléchargé.

### Notes
- **Version** : La partie `/latest/` de l'URL garantit que vous obtenez la version la plus récente. Si vous avez besoin d'une version spécifique, vous auriez généralement besoin d'accéder au numéro de version (visible dans l'onglet "Version History" du Marketplace) et pourriez avoir besoin d'ajuster l'URL ou d'utiliser un outil comme `ovsx` (voir ci-dessous), bien que l'API du Marketplace n'expose pas toujours facilement les anciennes versions via une URL directe.
- **Téléchargements bloqués** : Si l'URL ne fonctionne pas, l'éditeur pourrait restreindre l'accès direct, ou votre navigateur/réseau pourrait le bloquer. Dans de tels cas, essayez un autre navigateur ou un gestionnaire de téléchargement.
- **Outils alternatifs** : Vous pouvez utiliser un outil en ligne de commande comme `ovsx` (du registre Open VSX) pour télécharger des extensions. Installez-le via npm (`npm install -g ovsx`), puis exécutez :  
  ```
  ovsx download ms-python.python
  ```
  Cela télécharge le fichier `.vsix` de manière programmatique.

### Pour résumer
Pour télécharger manuellement un fichier `.vsix` pour une extension VS Code :
1. Allez sur la page de l'extension sur le [Visual Studio Marketplace](https://marketplace.visualstudio.com/vscode).
2. Identifiez l'éditeur et le nom de l'extension (par exemple, `ms-python.python`).
3. Utilisez ce format d'URL dans votre navigateur :  
   ```
   https://<publisher>.gallery.vsassets.io/_apis/public/gallery/publisher/<publisher>/extension/<extension-name>/latest/assetbyname/Microsoft.VisualStudio.Services.VSIXPackage
   ```
4. Téléchargez le fichier `.vsix` et installez-le optionnellement dans VS Code.