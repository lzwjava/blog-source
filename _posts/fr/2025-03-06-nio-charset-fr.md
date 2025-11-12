---
audio: false
generated: true
lang: fr
layout: post
title: Encodage et décodage des caractères en Java
translated: true
type: note
---

Le package `java.nio.charset` en Java fournit des outils pour gérer l'encodage et le décodage des caractères, ce qui est essentiel lors du travail avec des données texte dans différents formats ou à travers divers systèmes. Voici un guide complet sur la façon d'utiliser efficacement ce package.

---

#### **Qu'est-ce que `java.nio.charset` ?**
Le package `java.nio.charset` contient des classes qui gèrent les jeux de caractères (charsets), qui définissent comment les caractères sont encodés en octets et décodés en caractères. Ceci est crucial pour des tâches comme la lecture et l'écriture de fichiers, la communication réseau ou le traitement de texte dans différentes langues, où des encodages comme UTF-8, ISO-8859-1 ou d'autres peuvent être utilisés.

La classe principale de ce package est `Charset`, soutenue par des classes supplémentaires comme `CharsetEncoder` et `CharsetDecoder` pour des cas d'utilisation plus avancés.

---

#### **Classes principales dans `java.nio.charset`**
1. **`Charset`**  
   Représente un encodage de caractères (par exemple, UTF-8, ISO-8859-1). Vous utilisez cette classe pour spécifier l'encodage pour les conversions entre les octets et les caractères.

2. **`StandardCharsets`**  
   Une classe utilitaire fournissant des constantes pour les jeux de caractères couramment utilisés, tels que `StandardCharsets.UTF_8` ou `StandardCharsets.ISO_8859_1`. Elle élimine le besoin de rechercher manuellement les noms de jeux de caractères.

3. **`CharsetEncoder` et `CharsetDecoder`**  
   Ces classes offrent un contrôle granulaire sur l'encodage (caractères vers octets) et le décodage (octets vers caractères), généralement utilisées avec les buffers NIO comme `ByteBuffer` et `CharBuffer`.

---

#### **Comment utiliser `java.nio.charset`**

##### **1. Obtenir une instance de `Charset`**
Pour commencer à utiliser `java.nio.charset`, vous avez besoin d'un objet `Charset`. Il y a deux principales façons d'en obtenir un :

- **Utiliser `StandardCharsets`** (Recommandé pour les jeux de caractères courants) :
  ```java
  import java.nio.charset.StandardCharsets;

  Charset charset = StandardCharsets.UTF_8; // Jeu de caractères UTF-8 prédéfini
  ```

- **Utiliser `Charset.forName()`** (Pour tout jeu de caractères pris en charge) :
  ```java
  import java.nio.charset.Charset;

  Charset charset = Charset.forName("UTF-8"); // Jeu de caractères UTF-8
  ```
  Remarque : Si le nom du jeu de caractères est invalide, cela lance une `UnsupportedCharsetException`, donc gérez-la de manière appropriée :
  ```java
  try {
      Charset charset = Charset.forName("UTF-8");
  } catch (UnsupportedCharsetException e) {
      System.err.println("Jeu de caractères non supporté : " + e.getMessage());
  }
  ```

---

##### **2. Utilisation basique : Conversion entre les chaînes et les octets**
Pour la plupart des applications, vous pouvez utiliser un `Charset` avec la classe `String` pour encoder ou décoder du texte.

- **Décoder des octets en une chaîne** :
  Convertir un tableau d'octets en une `String` en utilisant un jeu de caractères spécifique :
  ```java
  byte[] bytes = {72, 101, 108, 108, 111}; // "Hello" en UTF-8
  Charset charset = StandardCharsets.UTF_8;
  String text = new String(bytes, charset);
  System.out.println(text); // Affiche : Hello
  ```

- **Encoder une chaîne en octets** :
  Convertir une `String` en un tableau d'octets en utilisant un jeu de caractères spécifique :
  ```java
  String text = "Hello, world!";
  Charset charset = StandardCharsets.UTF_8;
  byte[] bytes = text.getBytes(charset);
  ```

Ces méthodes sont simples et suffisantes pour la plupart des cas d'utilisation, tels que les E/S de fichiers ou le traitement de texte basique.

---

##### **3. Utilisation des Readers et Writers**
Lorsque vous travaillez avec des flux (par exemple, `InputStream` ou `OutputStream`), vous pouvez utiliser `InputStreamReader` et `OutputStreamWriter` avec un `Charset` pour gérer les données texte.

- **Lire depuis un InputStream** :
  ```java
  import java.io.*;
  import java.nio.charset.StandardCharsets;

  InputStream inputStream = new FileInputStream("file.txt");
  InputStreamReader reader = new InputStreamReader(inputStream, StandardCharsets.UTF_8);
  int data;
  while ((data = reader.read()) != -1) {
      System.out.print((char) data);
  }
  reader.close();
  ```

- **Écrire dans un OutputStream** :
  ```java
  import java.io.*;
  import java.nio.charset.StandardCharsets;

  OutputStream outputStream = new FileOutputStream("file.txt");
  OutputStreamWriter writer = new OutputStreamWriter(outputStream, StandardCharsets.UTF_8);
  writer.write("Hello, world!");
  writer.close();
  ```

Remarque : Ces classes acceptent soit un nom de jeu de caractères (par exemple, `"UTF-8"`), soit un objet `Charset`.

---

##### **4. Opérations de fichiers simplifiées avec `java.nio.file.Files`**
Depuis Java 7, le package `java.nio.file` fournit des méthodes pratiques pour lire et écrire des fichiers en utilisant un `Charset` :

- **Lire un fichier dans une chaîne** :
  ```java
  import java.nio.file.*;
  import java.nio.charset.StandardCharsets;

  Path path = Paths.get("file.txt");
  String content = Files.readString(path, StandardCharsets.UTF_8);
  System.out.println(content);
  ```

- **Écrire une chaîne dans un fichier** :
  ```java
  import java.nio.file.*;
  import java.nio.charset.StandardCharsets;

  Path path = Paths.get("file.txt");
  String content = "Hello, world!";
  Files.writeString(path, content, StandardCharsets.UTF_8);
  ```

Ces méthodes gèrent l'encodage et le décodage en interne, ce qui les rend idéales pour les opérations de fichiers simples.

---

##### **5. Utilisation avancée : `CharsetEncoder` et `CharsetDecoder`**
Pour les scénarios nécessitant plus de contrôle (par exemple, travailler avec des canaux NIO ou traiter des données partielles), utilisez `CharsetEncoder` et `CharsetDecoder`.

- **Encoder avec `CharsetEncoder`** :
  Convertir des caractères en octets en utilisant les buffers NIO :
  ```java
  import java.nio.*;
  import java.nio.charset.*;

  Charset charset = StandardCharsets.UTF_8;
  CharsetEncoder encoder = charset.newEncoder();
  CharBuffer charBuffer = CharBuffer.wrap("Hello");
  ByteBuffer byteBuffer = encoder.encode(charBuffer);
  byte[] bytes = byteBuffer.array();
  ```

- **Décoder avec `CharsetDecoder`** :
  Convertir des octets en caractères :
  ```java
  import java.nio.*;
  import java.nio.charset.*;

  Charset charset = StandardCharsets.UTF_8;
  CharsetDecoder decoder = charset.newDecoder();
  ByteBuffer byteBuffer = ByteBuffer.wrap(new byte[]{72, 101, 108, 108, 111});
  CharBuffer charBuffer = decoder.decode(byteBuffer);
  String text = charBuffer.toString();
  System.out.println(text); // Affiche : Hello
  ```

Ces classes sont utiles lorsque vous travaillez avec `SocketChannel`, `FileChannel` ou d'autres composants NIO où les données arrivent par morceaux.

---

#### **Bonnes pratiques**
- **Toujours spécifier le Charset** : Évitez de vous fier à `Charset.defaultCharset()`, car la valeur par défaut varie selon la plateforme (par exemple, UTF-8 sur Linux, windows-1252 sur Windows). Spécifier explicitement le jeu de caractères assure un comportement cohérent :
  ```java
  // À éviter :
  byte[] bytes = "Hello".getBytes(); // Utilise le jeu de caractères par défaut de la plateforme

  // Faire ceci :
  byte[] bytes = "Hello".getBytes(StandardCharsets.UTF_8);
  ```

- **Utiliser `StandardCharsets`** : C'est plus propre et évite les exceptions d'exécution dues à des noms de jeux de caractères invalides.

- **Gérer les exceptions** : Lors de l'utilisation de `Charset.forName()`, interceptez `UnsupportedCharsetException` pour les jeux de caractères non supportés.

---

#### **Résumé**
Pour utiliser `java.nio.charset` :
1. **Obtenez un `Charset`** en utilisant `StandardCharsets` ou `Charset.forName()`.
2. **Effectuez les conversions** :
   - Utilisez les méthodes de `String` (`getBytes()`, constructeur) pour les conversions simples octets-caractères.
   - Utilisez `InputStreamReader`/`OutputStreamWriter` pour les flux.
   - Utilisez `Files.readString()`/`writeString()` pour les opérations sur les fichiers.
   - Utilisez `CharsetEncoder`/`CharsetDecoder` pour les scénarios NIO avancés.
3. **Assurez la portabilité** en spécifiant explicitement les jeux de caractères.

Ce package fournit des outils flexibles et puissants pour gérer l'encodage des caractères, rendant vos applications Java robustes et compatibles avec des données texte diverses.