---
audio: false
generated: true
lang: fr
layout: post
title: Cryptographie en Java
translated: true
type: note
---

Le package `javax.crypto` en Java fournit un ensemble de classes et de méthodes pour effectuer des opérations cryptographiques telles que le chiffrement, le déchiffrement, la génération de clés et l'authentification de messages. Voici un guide complet sur l'utilisation de `javax.crypto`, incluant des explications et des exemples pratiques pour des cas d'usage courants comme le chiffrement symétrique, le chiffrement asymétrique et l'authentification de messages.

---

### **Qu'est-ce que javax.crypto ?**
Le package `javax.crypto` fait partie de l'Architecture de Cryptographie Java (JCA) et offre des outils pour implémenter une communication sécurisée via la cryptographie. Il prend en charge :
- **La cryptographie symétrique** : Utilise la même clé pour le chiffrement et le déchiffrement (ex. : AES, DES).
- **La cryptographie asymétrique** : Utilise une paire de clés publique/privée (ex. : RSA).
- **L'authentification de messages** : Garantit l'intégrité et l'authenticité des données (ex. : HMAC).
- **La génération et la gestion de clés** : Outils pour créer et manipuler les clés cryptographiques.

Pour utiliser `javax.crypto`, vous devez :
1. Sélectionner un algorithme cryptographique.
2. Générer ou obtenir les clés nécessaires.
3. Utiliser les classes fournies (ex. : `Cipher`, `KeyGenerator`, `Mac`) pour effectuer les opérations.

Vous trouverez ci-dessous des exemples étape par étape pour des scénarios courants.

---

### **1. Chiffrement symétrique avec AES**
Le chiffrement symétrique utilise une seule clé pour le chiffrement et le déchiffrement. Voici comment chiffrer et déchiffrer une chaîne en utilisant AES (Advanced Encryption Standard) avec la classe `Cipher` en mode CBC avec remplissage PKCS5.

#### **Étapes**
- Générer une clé secrète.
- Créer et initialiser une instance de `Cipher`.
- Chiffrer et déchiffrer les données.

#### **Exemple de code**
```java
import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import javax.crypto.spec.IvParameterSpec;
import java.security.SecureRandom;
import java.nio.charset.StandardCharsets;

public class SymmetricEncryptionExample {
    public static void main(String[] args) throws Exception {
        // Étape 1 : Générer une clé secrète pour AES
        KeyGenerator keyGen = KeyGenerator.getInstance("AES");
        keyGen.init(128); // Clé 128 bits
        SecretKey secretKey = keyGen.generateKey();

        // Étape 2 : Générer un Vecteur d'Initialisation (IV) aléatoire
        SecureRandom random = new SecureRandom();
        byte[] iv = new byte[16]; // La taille de bloc AES est de 16 octets
        random.nextBytes(iv);
        IvParameterSpec ivSpec = new IvParameterSpec(iv);

        // Étape 3 : Créer et initialiser Cipher pour le chiffrement
        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
        cipher.init(Cipher.ENCRYPT_MODE, secretKey, ivSpec);

        // Étape 4 : Chiffrer les données
        String plaintext = "Hello, World!";
        byte[] plaintextBytes = plaintext.getBytes(StandardCharsets.UTF_8);
        byte[] ciphertext = cipher.doFinal(plaintextBytes);

        // Étape 5 : Initialiser Cipher pour le déchiffrement avec le même IV
        cipher.init(Cipher.DECRYPT_MODE, secretKey, ivSpec);
        byte[] decryptedBytes = cipher.doFinal(ciphertext);
        String decryptedText = new String(decryptedBytes, StandardCharsets.UTF_8);

        // Afficher les résultats
        System.out.println("Original : " + plaintext);
        System.out.println("Déchiffré : " + decryptedText);
    }
}
```

#### **Points clés**
- **Algorithme** : `"AES/CBC/PKCS5Padding"` spécifie AES avec le mode CBC et un remplissage pour gérer les données qui ne sont pas un multiple de la taille de bloc.
- **IV** : Le Vecteur d'Initialisation doit être aléatoire pour le chiffrement et réutilisé pour le déchiffrement. Il est généralement préfixé au texte chiffré ou transmis séparément.
- **Gestion des clés** : Dans une application réelle, partagez la `secretKey` de manière sécurisée avec le destinataire.

---

### **2. Chiffrement asymétrique avec RSA**
Le chiffrement asymétrique utilise une clé publique pour chiffrer et une clé privée pour déchiffrer. Voici un exemple utilisant RSA.

#### **Étapes**
- Générer une paire de clés publique/privée.
- Chiffrer avec la clé publique.
- Déchiffrer avec la clé privée.

#### **Exemple de code**
```java
import javax.crypto.Cipher;
import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.PrivateKey;
import java.security.PublicKey;
import java.nio.charset.StandardCharsets;

public class AsymmetricEncryptionExample {
    public static void main(String[] args) throws Exception {
        // Étape 1 : Générer une paire de clés RSA
        KeyPairGenerator keyPairGen = KeyPairGenerator.getInstance("RSA");
        keyPairGen.initialize(2048); // Clé 2048 bits
        KeyPair keyPair = keyPairGen.generateKeyPair();
        PublicKey publicKey = keyPair.getPublic();
        PrivateKey privateKey = keyPair.getPrivate();

        // Étape 2 : Chiffrer avec la clé publique
        Cipher cipher = Cipher.getInstance("RSA");
        cipher.init(Cipher.ENCRYPT_MODE, publicKey);
        String plaintext = "Secret Message";
        byte[] plaintextBytes = plaintext.getBytes(StandardCharsets.UTF_8);
        byte[] ciphertext = cipher.doFinal(plaintextBytes);

        // Étape 3 : Déchiffrer avec la clé privée
        cipher.init(Cipher.DECRYPT_MODE, privateKey);
        byte[] decryptedBytes = cipher.doFinal(ciphertext);
        String decryptedText = new String(decryptedBytes, StandardCharsets.UTF_8);

        // Afficher les résultats
        System.out.println("Original : " + plaintext);
        System.out.println("Déchiffré : " + decryptedText);
    }
}
```

#### **Points clés**
- **Limite de taille** : RSA ne peut chiffrer que des données plus petites que la taille de la clé (ex. : ~245 octets pour une clé de 2048 bits). Pour des données plus volumineuses, utilisez le chiffrement hybride (chiffrez les données avec une clé symétrique, puis chiffrez cette clé avec RSA).
- **Distribution des clés** : Partagez la clé publique ouvertement ; gardez la clé privée secrète.

---

### **3. Authentification de messages avec HMAC**
Un Code d'Authentification de Message (MAC) garantit l'intégrité et l'authenticité des données. Voici comment utiliser `Mac` avec HMAC-SHA256.

#### **Exemple de code**
```java
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import java.nio.charset.StandardCharsets;
import java.util.Base64;

public class MacExample {
    public static void main(String[] args) throws Exception {
        // Étape 1 : Créer une clé secrète
        String secret = "mysecretkey";
        SecretKeySpec secretKey = new SecretKeySpec(secret.getBytes(StandardCharsets.UTF_8), "HmacSHA256");

        // Étape 2 : Initialiser Mac avec la clé
        Mac mac = Mac.getInstance("HmacSHA256");
        mac.init(secretKey);

        // Étape 3 : Calculer le MAC pour les données
        String data = "Data to authenticate";
        byte[] macValue = mac.doFinal(data.getBytes(StandardCharsets.UTF_8));
        String macBase64 = Base64.getEncoder().encodeToString(macValue);

        // Afficher le résultat
        System.out.println("MAC : " + macBase64);
    }
}
```

#### **Points clés**
- **Vérification** : Le destinataire recalcule le MAC avec la même clé et les mêmes données ; s'il correspond, les données sont authentiques et non altérées.
- **Clé** : Utilisez une clé secrète partagée, distribuée de manière sécurisée au préalable.

---

### **4. Chiffrement/Déchiffrement de flux**
Pour les données volumineuses (ex. : fichiers), utilisez `CipherInputStream` ou `CipherOutputStream`.

#### **Exemple de code (Chiffrement d'un fichier)**
```java
import javax.crypto.Cipher;
import javax.crypto.CipherOutputStream;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import javax.crypto.spec.IvParameterSpec;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.security.SecureRandom;

public class StreamEncryptionExample {
    public static void main(String[] args) throws Exception {
        // Générer la clé et l'IV
        KeyGenerator keyGen = KeyGenerator.getInstance("AES");
        keyGen.init(128);
        SecretKey secretKey = keyGen.generateKey();
        byte[] iv = new byte[16];
        new SecureRandom().nextBytes(iv);
        IvParameterSpec ivSpec = new IvParameterSpec(iv);

        // Initialiser Cipher
        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
        cipher.init(Cipher.ENCRYPT_MODE, secretKey, ivSpec);

        // Chiffrer le fichier
        try (FileInputStream fis = new FileInputStream("input.txt");
             FileOutputStream fos = new FileOutputStream("encrypted.txt");
             CipherOutputStream cos = new CipherOutputStream(fos, cipher)) {
            byte[] buffer = new byte[1024];
            int bytesRead;
            while ((bytesRead = fis.read(buffer)) != -1) {
                cos.write(buffer, 0, bytesRead);
            }
        }
    }
}
```

#### **Points clés**
- **Flux** : Utilisez `CipherOutputStream` pour le chiffrement et `CipherInputStream` pour le déchiffrement afin de traiter les données de manière incrémentale.
- **Gestion de l'IV** : Stockez l'IV avec le fichier chiffré (ex. : en le préfixant).

---

### **5. Chiffrement basé sur un mot de passe (PBE)**
Dérivez une clé à partir d'un mot de passe en utilisant `SecretKeyFactory`.

#### **Exemple de code**
```java
import javax.crypto.Cipher;
import javax.crypto.SecretKey;
import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.PBEKeySpec;
import javax.crypto.spec.SecretKeySpec;
import java.security.SecureRandom;
import java.nio.charset.StandardCharsets;

public class PBEExample {
    public static void main(String[] args) throws Exception {
        // Mot de passe et sel
        char[] password = "mysecretpassword".toCharArray();
        byte[] salt = new byte[16];
        new SecureRandom().nextBytes(salt);

        // Dériver la clé à partir du mot de passe
        PBEKeySpec pbeKeySpec = new PBEKeySpec(password, salt, 10000, 256); // Clé 256 bits
        SecretKeyFactory factory = SecretKeyFactory.getInstance("PBKDF2WithHmacSHA256");
        SecretKey tempKey = factory.generateSecret(pbeKeySpec);
        SecretKey secretKey = new SecretKeySpec(tempKey.getEncoded(), "AES");

        // Chiffrer avec la clé dérivée
        Cipher cipher = Cipher.getInstance("AES");
        cipher.init(Cipher.ENCRYPT_MODE, secretKey);
        String plaintext = "Hello from PBE";
        byte[] ciphertext = cipher.doFinal(plaintext.getBytes(StandardCharsets.UTF_8));

        System.out.println("Chiffré : " + Base64.getEncoder().encodeToString(ciphertext));
    }
}
```

#### **Points clés**
- **Sel** : Randomise la dérivation de clé ; stockez-le avec les données chiffrées.
- **Itérations** : Augmentez le coût computationnel pour contrer les attaques par force brute (ex. : 10 000).

---

### **Classes clés dans javax.crypto**
- **`Cipher`** : Effectue le chiffrement et le déchiffrement.
- **`KeyGenerator`** : Génère des clés symétriques (ex. : AES).
- **`KeyPairGenerator`** : Génère des paires de clés asymétriques (ex. : RSA).
- **`Mac`** : Calcule les codes d'authentification de messages.
- **`SecretKeyFactory`** : Dérive des clés (ex. : à partir de mots de passe).
- **`SecureRandom`** : Génère des nombres aléatoires cryptographiquement sûrs.

---

### **Bonnes pratiques**
- **Gestion des exceptions** : Encapsulez le code dans des blocs try-catch pour les exceptions comme `NoSuchAlgorithmException`, `InvalidKeyException`, etc.
- **Gestion des clés** : Stockez les clés de manière sécurisée (ex. : dans un `KeyStore`) et ne les codez jamais en dur.
- **Choix de l'algorithme** : Utilisez des algorithmes sécurisés (ex. : AES-256, RSA-2048) et des modes sûrs (ex. : CBC avec IV).
- **Fournisseurs** : Le fournisseur par défaut SunJCE suffit, mais vous pouvez en utiliser d'autres (ex. : BouncyCastle) via `Cipher.getInstance("AES", "BC")`.

---

### **Conclusion**
Pour utiliser `javax.crypto`, sélectionnez l'algorithme cryptographique approprié à vos besoins, générez ou obtenez les clés, et utilisez des classes comme `Cipher`, `KeyGenerator` et `Mac` pour effectuer les opérations. Que vous chiffriez des données symétriquement avec AES, asymétriquement avec RSA, ou assuriez l'intégrité avec HMAC, `javax.crypto` fournit les outils—associés à une initialisation correcte et une gestion sécurisée des clés—pour implémenter une cryptographie robuste en Java.