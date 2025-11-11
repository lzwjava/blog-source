---
audio: false
generated: true
lang: de
layout: post
title: Kryptografie in Java
translated: true
type: note
---

Das `javax.crypto`-Paket in Java bietet eine Reihe von Klassen und Methoden zur Durchführung kryptografischer Operationen wie Verschlüsselung, Entschlüsselung, Schlüsselgenerierung und Nachrichtenauthentifizierung. Nachfolgend finden Sie eine umfassende Anleitung zur Verwendung von `javax.crypto`, einschließlich Erklärungen und praktischer Beispiele für gängige Anwendungsfälle wie symmetrische Verschlüsselung, asymmetrische Verschlüsselung und Nachrichtenauthentifizierung.

---

### **Was ist javax.crypto?**
Das `javax.crypto`-Paket ist Teil der Java Cryptography Architecture (JCA) und bietet Werkzeuge zur Implementierung sicherer Kommunikation durch Kryptografie. Es unterstützt:
- **Symmetrische Kryptografie**: Verwendet denselben Schlüssel für Ver- und Entschlüsselung (z.B. AES, DES).
- **Asymmetrische Kryptografie**: Verwendet ein öffentliches/privates Schlüsselpaar (z.B. RSA).
- **Nachrichtenauthentifizierung**: Stellt Datenintegrität und Authentizität sicher (z.B. HMAC).
- **Schlüsselgenerierung und -verwaltung**: Werkzeuge zum Erstellen und Handhaben kryptografischer Schlüssel.

Um `javax.crypto` zu verwenden, müssen Sie:
1. Einen kryptografischen Algorithmus auswählen.
2. Die notwendigen Schlüssel generieren oder beschaffen.
3. Die bereitgestellten Klassen (z.B. `Cipher`, `KeyGenerator`, `Mac`) verwenden, um Operationen durchzuführen.

Nachfolgend finden Sie Schritt-für-Schritt-Beispiele für gängige Szenarien.

---

### **1. Symmetrische Verschlüsselung mit AES**
Symmetrische Verschlüsselung verwendet einen einzelnen Schlüssel für Ver- und Entschlüsselung. So verschlüsseln und entschlüsseln Sie einen String mit AES (Advanced Encryption Standard) unter Verwendung der `Cipher`-Klasse im CBC-Modus mit PKCS5-Padding.

#### **Schritte**
- Generieren Sie einen geheimen Schlüssel.
- Erstellen und initialisieren Sie eine `Cipher`-Instanz.
- Verschlüsseln und entschlüsseln Sie die Daten.

#### **Beispielcode**
```java
import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import javax.crypto.spec.IvParameterSpec;
import java.security.SecureRandom;
import java.nio.charset.StandardCharsets;

public class SymmetricEncryptionExample {
    public static void main(String[] args) throws Exception {
        // Schritt 1: Generieren eines geheimen Schlüssels für AES
        KeyGenerator keyGen = KeyGenerator.getInstance("AES");
        keyGen.init(128); // 128-Bit-Schlüssel
        SecretKey secretKey = keyGen.generateKey();

        // Schritt 2: Generieren eines zufälligen Initialisierungsvektors (IV)
        SecureRandom random = new SecureRandom();
        byte[] iv = new byte[16]; // AES-Blockgröße ist 16 Bytes
        random.nextBytes(iv);
        IvParameterSpec ivSpec = new IvParameterSpec(iv);

        // Schritt 3: Erstellen und Initialisieren des Cipher für die Verschlüsselung
        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
        cipher.init(Cipher.ENCRYPT_MODE, secretKey, ivSpec);

        // Schritt 4: Daten verschlüsseln
        String plaintext = "Hello, World!";
        byte[] plaintextBytes = plaintext.getBytes(StandardCharsets.UTF_8);
        byte[] ciphertext = cipher.doFinal(plaintextBytes);

        // Schritt 5: Initialisieren des Cipher für die Entschlüsselung mit demselben IV
        cipher.init(Cipher.DECRYPT_MODE, secretKey, ivSpec);
        byte[] decryptedBytes = cipher.doFinal(ciphertext);
        String decryptedText = new String(decryptedBytes, StandardCharsets.UTF_8);

        // Ergebnisse ausgeben
        System.out.println("Original: " + plaintext);
        System.out.println("Entschlüsselt: " + decryptedText);
    }
}
```

#### **Wichtige Punkte**
- **Algorithmus**: `"AES/CBC/PKCS5Padding"` spezifiziert AES mit CBC-Modus und Padding, um Daten zu verarbeiten, die kein Vielfaches der Blockgröße sind.
- **IV**: Der Initialisierungsvektor muss für die Verschlüsselung zufällig sein und für die Entschlüsselung wiederverwendet werden. Er wird typischerweise dem Chiffretext vorangestellt oder separat übertragen.
- **Schlüsselverwaltung**: In einer echten Anwendung teilen Sie den `secretKey` sicher mit dem Empfänger.

---

### **2. Asymmetrische Verschlüsselung mit RSA**
Asymmetrische Verschlüsselung verwendet einen öffentlichen Schlüssel zum Verschlüsseln und einen privaten Schlüssel zum Entschlüsseln. Hier ist ein Beispiel mit RSA.

#### **Schritte**
- Generieren Sie ein öffentliches/privates Schlüsselpaar.
- Verschlüsseln Sie mit dem öffentlichen Schlüssel.
- Entschlüsseln Sie mit dem privaten Schlüssel.

#### **Beispielcode**
```java
import javax.crypto.Cipher;
import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.PrivateKey;
import java.security.PublicKey;
import java.nio.charset.StandardCharsets;

public class AsymmetricEncryptionExample {
    public static void main(String[] args) throws Exception {
        // Schritt 1: Generieren eines RSA-Schlüsselpaars
        KeyPairGenerator keyPairGen = KeyPairGenerator.getInstance("RSA");
        keyPairGen.initialize(2048); // 2048-Bit-Schlüssel
        KeyPair keyPair = keyPairGen.generateKeyPair();
        PublicKey publicKey = keyPair.getPublic();
        PrivateKey privateKey = keyPair.getPrivate();

        // Schritt 2: Verschlüsseln mit dem öffentlichen Schlüssel
        Cipher cipher = Cipher.getInstance("RSA");
        cipher.init(Cipher.ENCRYPT_MODE, publicKey);
        String plaintext = "Secret Message";
        byte[] plaintextBytes = plaintext.getBytes(StandardCharsets.UTF_8);
        byte[] ciphertext = cipher.doFinal(plaintextBytes);

        // Schritt 3: Entschlüsseln mit dem privaten Schlüssel
        cipher.init(Cipher.DECRYPT_MODE, privateKey);
        byte[] decryptedBytes = cipher.doFinal(ciphertext);
        String decryptedText = new String(decryptedBytes, StandardCharsets.UTF_8);

        // Ergebnisse ausgeben
        System.out.println("Original: " + plaintext);
        System.out.println("Entschlüsselt: " + decryptedText);
    }
}
```

#### **Wichtige Punkte**
- **Größenbeschränkung**: RSA kann nur Daten verschlüsseln, die kleiner als die Schlüsselgröße sind (z.B. ~245 Bytes für einen 2048-Bit-Schlüssel). Für größere Daten verwenden Sie hybride Verschlüsselung (Verschlüsseln der Daten mit einem symmetrischen Schlüssel, dann Verschlüsseln dieses Schlüssels mit RSA).
- **Schlüsselverteilung**: Teilen Sie den öffentlichen Schlüssel offen; halten Sie den privaten Schlüssel geheim.

---

### **3. Nachrichtenauthentifizierung mit HMAC**
Ein Message Authentication Code (MAC) stellt Datenintegrität und Authentizität sicher. So verwenden Sie `Mac` mit HMAC-SHA256.

#### **Beispielcode**
```java
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import java.nio.charset.StandardCharsets;
import java.util.Base64;

public class MacExample {
    public static void main(String[] args) throws Exception {
        // Schritt 1: Erstellen eines geheimen Schlüssels
        String secret = "mysecretkey";
        SecretKeySpec secretKey = new SecretKeySpec(secret.getBytes(StandardCharsets.UTF_8), "HmacSHA256");

        // Schritt 2: Initialisieren von Mac mit dem Schlüssel
        Mac mac = Mac.getInstance("HmacSHA256");
        mac.init(secretKey);

        // Schritt 3: Berechnen des MAC für die Daten
        String data = "Data to authenticate";
        byte[] macValue = mac.doFinal(data.getBytes(StandardCharsets.UTF_8));
        String macBase64 = Base64.getEncoder().encodeToString(macValue);

        // Ergebnis ausgeben
        System.out.println("MAC: " + macBase64);
    }
}
```

#### **Wichtige Punkte**
- **Verifikation**: Der Empfänger berechnet den MAC mit demselben Schlüssel und denselben Daten neu; wenn er übereinstimmt, sind die Daten authentisch und unverändert.
- **Schlüssel**: Verwenden Sie einen gemeinsamen geheimen Schlüssel, der vorab sicher verteilt wurde.

---

### **4. Ver-/Entschlüsseln von Streams**
Für große Datenmengen (z.B. Dateien) verwenden Sie `CipherInputStream` oder `CipherOutputStream`.

#### **Beispielcode (Verschlüsseln einer Datei)**
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
        // Schlüssel und IV generieren
        KeyGenerator keyGen = KeyGenerator.getInstance("AES");
        keyGen.init(128);
        SecretKey secretKey = keyGen.generateKey();
        byte[] iv = new byte[16];
        new SecureRandom().nextBytes(iv);
        IvParameterSpec ivSpec = new IvParameterSpec(iv);

        // Cipher initialisieren
        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
        cipher.init(Cipher.ENCRYPT_MODE, secretKey, ivSpec);

        // Datei verschlüsseln
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

#### **Wichtige Punkte**
- **Streams**: Verwenden Sie `CipherOutputStream` für die Verschlüsselung und `CipherInputStream` für die Entschlüsselung, um Daten inkrementell zu verarbeiten.
- **IV-Behandlung**: Speichern Sie den IV mit der verschlüsselten Datei (z.B. stellen Sie ihn voran).

---

### **5. Passwortbasierte Verschlüsselung (PBE)**
Leiten Sie einen Schlüssel aus einem Passwort mit `SecretKeyFactory` ab.

#### **Beispielcode**
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
        // Passwort und Salt
        char[] password = "mysecretpassword".toCharArray();
        byte[] salt = new byte[16];
        new SecureRandom().nextBytes(salt);

        // Schlüssel aus Passwort ableiten
        PBEKeySpec pbeKeySpec = new PBEKeySpec(password, salt, 10000, 256); // 256-Bit-Schlüssel
        SecretKeyFactory factory = SecretKeyFactory.getInstance("PBKDF2WithHmacSHA256");
        SecretKey tempKey = factory.generateSecret(pbeKeySpec);
        SecretKey secretKey = new SecretKeySpec(tempKey.getEncoded(), "AES");

        // Mit abgeleitetem Schlüssel verschlüsseln
        Cipher cipher = Cipher.getInstance("AES");
        cipher.init(Cipher.ENCRYPT_MODE, secretKey);
        String plaintext = "Hello from PBE";
        byte[] ciphertext = cipher.doFinal(plaintext.getBytes(StandardCharsets.UTF_8));

        System.out.println("Verschlüsselt: " + Base64.getEncoder().encodeToString(ciphertext));
    }
}
```

#### **Wichtige Punkte**
- **Salt**: Randomisieren Sie die Schlüsselableitung; speichern Sie es mit den verschlüsselten Daten.
- **Iterationen**: Erhöhen Sie den Rechenaufwand, um Brute-Force-Angriffe zu erschweren (z.B. 10.000).

---

### **Wichtige Klassen in javax.crypto**
- **`Cipher`**: Führt Ver- und Entschlüsselung durch.
- **`KeyGenerator`**: Generiert symmetrische Schlüssel (z.B. AES).
- **`KeyPairGenerator`**: Generiert asymmetrische Schlüsselpaare (z.B. RSA).
- **`Mac`**: Berechnet Message Authentication Codes.
- **`SecretKeyFactory`**: Leitet Schlüssel ab (z.B. aus Passwörtern).
- **`SecureRandom`**: Generiert kryptografisch sichere Zufallszahlen.

---

### **Best Practices**
- **Ausnahmebehandlung**: Umschließen Sie Code mit try-catch-Blöcken für Ausnahmen wie `NoSuchAlgorithmException`, `InvalidKeyException` usw.
- **Schlüsselverwaltung**: Speichern Sie Schlüssel sicher (z.B. in einem `KeyStore`) und hardcodieren Sie sie niemals.
- **Algorithmusauswahl**: Verwenden Sie sichere Algorithmen (z.B. AES-256, RSA-2048) und Modi (z.B. CBC mit IV).
- **Provider**: Der Standard-SunJCE-Provider genügt, aber Sie können andere (z.B. BouncyCastle) über `Cipher.getInstance("AES", "BC")` verwenden.

---

### **Schlussfolgerung**
Um `javax.crypto` zu verwenden, wählen Sie den geeigneten kryptografischen Algorithmus für Ihre Anforderungen, generieren oder beschaffen Sie Schlüssel und nutzen Sie Klassen wie `Cipher`, `KeyGenerator` und `Mac`, um Operationen durchzuführen. Egal, ob Sie Daten symmetrisch mit AES verschlüsseln, asymmetrisch mit RSA oder die Integrität mit HMAC sicherstellen – `javax.crypto` bietet die Werkzeuge, die – gepaart mit korrekter Initialisierung und sicherer Schlüsselverwaltung – die Implementierung robuster Kryptografie in Java ermöglichen.