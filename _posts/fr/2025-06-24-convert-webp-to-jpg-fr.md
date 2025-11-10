---
audio: false
generated: true
lang: fr
layout: post
title: Conversion de WebP en JPG sous Ubuntu
translated: true
type: note
---

Vous disposez de plusieurs excellentes options pour convertir WebP en JPG sous Ubuntu, que ce soit en ligne de commande ou avec des outils graphiques.

## Outils en ligne de commande

Ces outils sont généralement les plus flexibles et efficaces pour convertir des fichiers individuels ou par lots.

### 1. ImageMagick

ImageMagick est une suite d'outils en ligne de commande puissante pour la manipulation d'images, et elle est très répandue.

*   **Installation :**
    ```bash
    sudo apt update
    sudo apt install imagemagick
    ```
*   **Convertir un fichier unique :**
    ```bash
    convert input.webp output.jpg
    ```
    Ou, en utilisant `magick` pour ImageMagick v7+ :
    ```bash
    magick input.webp output.jpg
    ```
*   **Convertir plusieurs fichiers (conversion par lot) dans le répertoire courant :**
    ```bash
    mogrify -format JPEG *.webp
    ```
    Cette commande convertira tous les fichiers `.webp` du répertoire courant en `.jpeg` (ou `.jpg`) avec le même nom de fichier. Si vous souhaitez que les fichiers convertis soient placés dans un répertoire séparé :
    ```bash
    mkdir output_jpgs # Créer un répertoire pour la sortie
    mogrify -format JPEG -path output_jpgs *.webp
    ```

### 2. `dwebp` (du paquet `libwebp`)

`dwebp` est un outil dédié au décodage des images WebP.

*   **Installation :**
    ```bash
    sudo apt update
    sudo apt install webp
    ```
*   **Convertir un fichier unique :**
    ```bash
    dwebp input.webp -o output.jpg
    ```
    Bien que vous spécifiiez `.jpg` comme sortie, `dwebp` sort souvent au format PPM et nécessite un autre outil comme ImageMagick pour une conversion correcte en JPEG. Cependant, certaines sources suggèrent que l'utilisation directe de `.jpg` comme sortie fonctionne pour les cas simples. Si vous rencontrez des problèmes, convertissez d'abord en PNG, puis en JPG :
    ```bash
    dwebp input.webp -o output.png
    convert output.png output.jpg
    ```

### 3. `ffmpeg`

`ffmpeg` est principalement conçu pour la vidéo et l'audio, mais il est aussi très compétent avec les formats d'image.

*   **Installation :**
    ```bash
    sudo apt update
    sudo apt install ffmpeg
    ```
*   **Convertir un fichier unique :**
    ```bash
    ffmpeg -i input.webp output.jpg
    ```
*   **Convertir plusieurs fichiers (conversion par lot) :**
    ```bash
    for file in *.webp; do ffmpeg -i "$file" "${file%.*}.jpg"; done
    ```
    Cette commande parcourt tous les fichiers `.webp` du répertoire courant et les convertit en `.jpg` avec le même nom (par exemple, `image.webp` devient `image.jpg`).

## Outils graphiques

Si vous préférez une interface graphique, voici quelques options :

### 1. GIMP (GNU Image Manipulation Program)

GIMP est un éditeur d'image open-source puissant qui prend en charge WebP.

*   **Installation :**
    ```bash
    sudo apt update
    sudo apt install gimp
    ```
*   **Comment convertir :**
    1.  Ouvrez l'image WebP dans GIMP (Fichier > Ouvrir).
    2.  Allez dans Fichier > Exporter sous.
    3.  Dans la boîte de dialogue "Exporter l'image", choisissez "Image JPEG" dans le menu déroulant "Sélectionner le type de fichier (par extension)".
    4.  Cliquez sur "Exporter" et ajustez les paramètres de qualité si nécessaire.

### 2. XnView MP / XnConvert

Ce sont des visionneuses et convertisseurs par lot d'images multiplateformes avec une prise en charge complète des formats, y compris WebP.

*   **Installation :**
    Vous devrez peut-être télécharger le paquet `.deb` depuis leur site web officiel et l'installer en utilisant `sudo dpkg -i <nom_du_paquet.deb>` ou via un installateur de paquets graphique.
*   **Comment convertir (généralement) :**
    1.  Ouvrez XnView MP ou XnConvert.
    2.  Ajoutez les images WebP que vous souhaitez convertir.
    3.  Choisissez JPG comme format de sortie.
    4.  Ajustez les paramètres (qualité, redimensionnement, etc.).
    5.  Lancez la conversion.

### 3. Converseen

Converseen est un convertisseur d'images par lot gratuit qui prend en charge WebP.

*   **Installation :** Vous pouvez généralement le trouver dans le Logithèque Ubuntu ou l'installer via apt s'il est disponible dans vos dépôts.
*   **Comment convertir :** Il dispose d'une interface graphique simple pour ajouter des images, sélectionner le format de sortie et convertir.

## Quelle méthode choisir ?

*   **Pour des conversions rapides de fichiers uniques ou pour automatiser des tâches via des scripts :** Utilisez `ffmpeg` ou `ImageMagick` en ligne de commande. Ils sont très efficaces.
*   **Pour des conversions occasionnelles où vous souhaitez une interface visuelle et plus de contrôle sur l'édition d'image :** GIMP est un excellent choix.
*   **Pour convertir de nombreuses images par lot avec une interface graphique et diverses options :** XnView MP/XnConvert ou Converseen sont excellents.

Quelle que soit la méthode que vous choisissiez, assurez-vous d'abord d'installer les paquets nécessaires.