---
audio: false
generated: true
lang: fr
layout: post
title: Cryptographie en Java
translated: true
---

Le package `javax.crypto` en Java fournit un ensemble de classes et de méthodes pour effectuer des opérations cryptographiques telles que le chiffrement, le déchiffrement, la génération de clés et l'authentification de messages. Voici un guide complet sur l'utilisation de `javax.crypto`, y compris des explications et des exemples pratiques pour des cas d'utilisation courants comme le chiffrement symétrique, le chiffrement asymétrique et l'authentification de messages.

---

### **Qu'est-ce que javax.crypto ?**
Le package `javax.crypto` fait partie de l'architecture de cryptographie Java (JCA) et offre des outils pour mettre en œuvre une communication sécurisée par le biais de la cryptographie. Il prend en charge :
- **Cryptographie symétrique** : Utilise la même clé pour le chiffrement et le déchiffrement (par exemple, AES, DES).
- **Cryptographie asymétrique** : Utilise une paire de clés publique/privée (par exemple, RSA).
- **Authentification de messages** : Assure l'intégrité et l'authenticité des données (par exemple, HMAC).
- **Génération et gestion de clés** : Outils pour créer et gérer des clés cryptographiques.

Pour utiliser `javax.crypto`, vous devez :
1. Sélectionner un algorithme cryptographique.
2. Générer ou obtenir les clés nécessaires.
3. Utiliser les classes fournies (par exemple, `Cipher`, `KeyGenerator`, `Mac`) pour effectuer des opérations.

Voici des exemples étape par étape pour des scénarios courants.

---

### **1. Chiffrement symétrique avec AES**
Le chiffrement symétrique utilise une seule clé pour le chiffrement et le déchiffrement. Voici comment chiffrer et déchiffrer une chaîne en utilisant AES (Advanced Encryption Standard) avec la classe `Cipher` en mode CBC avec un remplissage PKCS5.

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
        keyGen.init(128); // Clé de 128 bits
        SecretKey secretKey = keyGen.generateKey();

        // Étape 2 : Générer un vecteur d'initialisation aléatoire (IV)
        SecureRandom random = new SecureRandom();
        byte[] iv = new byte[16]; // La taille du bloc AES est de 16 octets
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
        System.out.println("Original: " + plaintext);
        System.out.println("Déchiffré: " + decryptedText);
    }
}
```

#### **Points clés**
- **Algorithme** : `"AES/CBC/PKCS5Padding"` spécifie AES avec le mode CBC et un remplissage pour gérer les données qui ne sont pas un multiple de la taille du bloc.
- **IV** : Le vecteur d'initialisation doit être aléatoire pour le chiffrement et réutilisé pour le déchiffrement. Il est généralement préfixé au texte chiffré ou transmis séparément.
- **Gestion des clés** : Dans une application réelle, partager la `secretKey` de manière sécurisée avec le destinataire.

---

### **2. Chiffrement asymétrique avec RSA**
Le chiffrement asymétrique utilise une clé publique pour le chiffrement et une clé privée pour le déchiffrement. Voici un exemple utilisant RSA.

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
        keyPairGen.initialize(2048); // Clé de 2048 bits
        KeyPair keyPair = keyPairGen.generateKeyPair();
        PublicKey publicKey = keyPair.getPublic();
        PrivateKey privateKey = keyPair.getPrivate();

        // Étape 2 : Chiffrer avec la clé publique
        Cipher cipher = Cipher.getInstance("RSA");
        cipher.init(Cipher.ENCRYPT_MODE, publicKey);
        String plaintext = "Message secret";
        byte[] plaintextBytes = plaintext.getBytes(StandardCharsets.UTF_8);
        byte[] ciphertext = cipher.doFinal(plaintextBytes);

        // Étape 3 : Déchiffrer avec la clé privée
        cipher.init(Cipher.DECRYPT_MODE, privateKey);
        byte[] decryptedBytes = cipher.doFinal(ciphertext);
        String decryptedText = new String(decryptedBytes, StandardCharsets.UTF_8);

        // Afficher les résultats
        System.out.println("Original: " + plaintext);
        System.out.println("Déchiffré: " + decryptedText);
    }
}
```

#### **Points clés**
- **Limite de taille** : RSA ne peut chiffrer que des données plus petites que la taille de la clé (par exemple, ~245 octets pour une clé de 2048 bits). Pour des données plus grandes, utilisez un chiffrement hybride (chiffrez les données avec une clé symétrique, puis chiffrez cette clé avec RSA).
- **Distribution des clés** : Partagez la clé publique ouvertement ; gardez la clé privée secrète.

---

### **3. Authentification de messages avec HMAC**
Un code d'authentification de message (MAC) assure l'intégrité et l'authenticité des données. Voici comment utiliser `Mac` avec HMAC-SHA256.

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
        String data = "Données à authentifier";
        byte[] macValue = mac.doFinal(data.getBytes(StandardCharsets.UTF_8));
        String macBase64 = Base64.getEncoder().encodeToString(macValue);

        // Afficher le résultat
        System.out.println("MAC: " + macBase64);
    }
}
```

#### **Points clés**
- **Vérification** : Le destinataire recalcule le MAC avec la même clé et les mêmes données ; s'il correspond, les données sont authentiques et non altérées.
- **Clé** : Utilisez une clé secrète partagée, distribuée de manière sécurisée au préalable.

---

### **4. Chiffrement/Déchiffrement de flux**
Pour de grandes données (par exemple, des fichiers), utilisez `CipherInputStream` ou `CipherOutputStream`.

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
- **Flux** : Utilisez `CipherOutputStream` pour le chiffrement et `CipherInputStream` pour le déchiffrement pour traiter les données par incréments.
- **Gestion de l'IV** : Stockez l'IV avec le fichier chiffré (par exemple, préfixez-le).

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
        PBEKeySpec pbeKeySpec = new PBEKeySpec(password, salt, 10000, 256); // Clé de 256 bits
        SecretKeyFactory factory = SecretKeyFactory.getInstance("PBKDF2WithHmacSHA256");
        SecretKey tempKey = factory.generateSecret(pbeKeySpec);
        SecretKey secretKey = new SecretKeySpec(tempKey.getEncoded(), "AES");

        // Chiffrer avec la clé dérivée
        Cipher cipher = Cipher.getInstance("AES");
        cipher.init(Cipher.ENCRYPT_MODE, secretKey);
        String plaintext = "Hello from PBE";
        byte[] ciphertext = cipher.doFinal(plaintext.getBytes(StandardCharsets.UTF_8));

        System.out.println("Chiffré: " + Base64.getEncoder().encodeToString(ciphertext));
    }
}
```

#### **Points clés**
- **Sel** : Randomisez la dérivation de la clé ; stockez-le avec les données chiffrées.
- **Itérations** : Augmentez le coût computationnel pour contrer les attaques par force brute (par exemple, 10 000).

---

### **Classes clés dans javax.crypto**
- **`Cipher`** : Effectue le chiffrement et le déchiffrement.
- **`KeyGenerator`** : Génère des clés symétriques (par exemple, AES).
- **`KeyPairGenerator`** : Génère des paires de clés asymétriques (par exemple, RSA).
- **`Mac`** : Calcule les codes d'authentification de messages.
- **`SecretKeyFactory`** : Dérive des clés (par exemple, à partir de mots de passe).
- **`SecureRandom`** : Génère des nombres aléatoires cryptographiquement sécurisés.

---

### **Bonnes pratiques**
- **Gestion des exceptions** : Enveloppez le code dans des blocs try-catch pour les exceptions comme `NoSuchAlgorithmException`, `InvalidKeyException`, etc.
- **Gestion des clés** : Stockez les clés de manière sécurisée (par exemple, dans un `KeyStore`) et ne les codez jamais en dur.
- **Choix de l'algorithme** : Utilisez des algorithmes sécurisés (par exemple, AES-256, RSA-2048) et des modes (par exemple, CBC avec IV).
- **Fournisseurs** : Le fournisseur SunJCE par défaut suffit, mais vous pouvez utiliser d'autres (par exemple, BouncyCastle) via `Cipher.getInstance("AES", "BC")`.

---

### **Conclusion**
Pour utiliser `javax.crypto`, sélectionnez l'algorithme cryptographique approprié pour vos besoins, générez ou obtenez des clés, et utilisez des classes comme `Cipher`, `KeyGenerator` et `Mac` pour effectuer des opérations. Que vous chiffriez des données de manière symétrique avec AES, de manière asymétrique avec RSA, ou que vous assuriez l'intégrité avec HMAC, `javax.crypto` fournit les outils—associés à une initialisation appropriée et à une gestion sécurisée des clés—pour mettre en œuvre une cryptographie robuste en Java.