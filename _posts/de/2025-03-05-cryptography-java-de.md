---
audio: false
generated: true
lang: de
layout: post
title: Kryptographie in Java
translated: true
---

Das `javax.crypto`-Paket in Java bietet eine Reihe von Klassen und Methoden zur Durchführung kryptographischer Operationen wie Verschlüsselung, Entschlüsselung, Schlüsselgenerierung und Nachrichtenauthentifizierung. Im Folgenden finden Sie eine umfassende Anleitung zur Verwendung von `javax.crypto`, einschließlich Erklärungen und praktischer Beispiele für häufige Anwendungsfälle wie symmetrische Verschlüsselung, asymmetrische Verschlüsselung und Nachrichtenauthentifizierung.

---

### **Was ist javax.crypto?**
Das `javax.crypto`-Paket ist Teil der Java Cryptography Architecture (JCA) und bietet Werkzeuge zur Implementierung sicherer Kommunikation durch Kryptographie. Es unterstützt:
- **Symmetrische Kryptographie**: Verwendet denselben Schlüssel für Verschlüsselung und Entschlüsselung (z.B. AES, DES).
- **Asymmetrische Kryptographie**: Verwendet ein öffentliches/privates Schlüsselpaar (z.B. RSA).
- **Nachrichtenauthentifizierung**: Stellt die Datenintegrität und Authentizität sicher (z.B. HMAC).
- **Schlüsselgenerierung und -verwaltung**: Werkzeuge zur Erstellung und Verwaltung kryptographischer Schlüssel.

Um `javax.crypto` zu verwenden, müssen Sie:
1. Einen kryptographischen Algorithmus auswählen.
2. Die erforderlichen Schlüssel generieren oder erhalten.
3. Die bereitgestellten Klassen (z.B. `Cipher`, `KeyGenerator`, `Mac`) verwenden, um Operationen durchzuführen.

Im Folgenden finden Sie Schritt-für-Schritt-Beispiele für häufige Szenarien.

---

### **1. Symmetrische Verschlüsselung mit AES**
Symmetrische Verschlüsselung verwendet einen einzigen Schlüssel für sowohl Verschlüsselung als auch Entschlüsselung. Hier erfahren Sie, wie Sie eine Zeichenkette mit AES (Advanced Encryption Standard) und der `Cipher`-Klasse im CBC-Modus mit PKCS5-Padding verschlüsseln und entschlüsseln.

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
        // Schritt 1: Generieren Sie einen geheimen Schlüssel für AES
        KeyGenerator keyGen = KeyGenerator.getInstance("AES");
        keyGen.init(128); // 128-Bit-Schlüssel
        SecretKey secretKey = keyGen.generateKey();

        // Schritt 2: Generieren Sie einen zufälligen Initialisierungsvektor (IV)
        SecureRandom random = new SecureRandom();
        byte[] iv = new byte[16]; // AES-Blockgröße beträgt 16 Bytes
        random.nextBytes(iv);
        IvParameterSpec ivSpec = new IvParameterSpec(iv);

        // Schritt 3: Erstellen und initialisieren Sie Cipher für die Verschlüsselung
        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
        cipher.init(Cipher.ENCRYPT_MODE, secretKey, ivSpec);

        // Schritt 4: Verschlüsseln Sie die Daten
        String plaintext = "Hello, World!";
        byte[] plaintextBytes = plaintext.getBytes(StandardCharsets.UTF_8);
        byte[] ciphertext = cipher.doFinal(plaintextBytes);

        // Schritt 5: Initialisieren Sie Cipher für die Entschlüsselung mit dem gleichen IV
        cipher.init(Cipher.DECRYPT_MODE, secretKey, ivSpec);
        byte[] decryptedBytes = cipher.doFinal(ciphertext);
        String decryptedText = new String(decryptedBytes, StandardCharsets.UTF_8);

        // Ausgabe der Ergebnisse
        System.out.println("Original: " + plaintext);
        System.out.println("Entschlüsselt: " + decryptedText);
    }
}
```

#### **Wichtige Punkte**
- **Algorithmus**: `"AES/CBC/PKCS5Padding"` gibt AES mit CBC-Modus und Padding an, um Daten zu verarbeiten, die kein Vielfaches der Blockgröße sind.
- **IV**: Der Initialisierungsvektor muss für die Verschlüsselung zufällig und für die Entschlüsselung wiederverwendet werden. Er wird normalerweise dem Chiffretext vorangestellt oder getrennt übertragen.
- **Schlüsselverwaltung**: In einer echten Anwendung müssen Sie den `secretKey` sicher mit dem Empfänger teilen.

---

### **2. Asymmetrische Verschlüsselung mit RSA**
Asymmetrische Verschlüsselung verwendet einen öffentlichen Schlüssel zur Verschlüsselung und einen privaten Schlüssel zur Entschlüsselung. Hier ist ein Beispiel mit RSA.

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
        // Schritt 1: Generieren Sie ein RSA-Schlüsselpaar
        KeyPairGenerator keyPairGen = KeyPairGenerator.getInstance("RSA");
        keyPairGen.initialize(2048); // 2048-Bit-Schlüssel
        KeyPair keyPair = keyPairGen.generateKeyPair();
        PublicKey publicKey = keyPair.getPublic();
        PrivateKey privateKey = keyPair.getPrivate();

        // Schritt 2: Verschlüsseln Sie mit dem öffentlichen Schlüssel
        Cipher cipher = Cipher.getInstance("RSA");
        cipher.init(Cipher.ENCRYPT_MODE, publicKey);
        String plaintext = "Geheime Nachricht";
        byte[] plaintextBytes = plaintext.getBytes(StandardCharsets.UTF_8);
        byte[] ciphertext = cipher.doFinal(plaintextBytes);

        // Schritt 3: Entschlüsseln Sie mit dem privaten Schlüssel
        cipher.init(Cipher.DECRYPT_MODE, privateKey);
        byte[] decryptedBytes = cipher.doFinal(ciphertext);
        String decryptedText = new String(decryptedBytes, StandardCharsets.UTF_8);

        // Ausgabe der Ergebnisse
        System.out.println("Original: " + plaintext);
        System.out.println("Entschlüsselt: " + decryptedText);
    }
}
```

#### **Wichtige Punkte**
- **Größenbegrenzung**: RSA kann nur Daten verschlüsseln, die kleiner als die Schlüsselgröße sind (z.B. ~245 Bytes für einen 2048-Bit-Schlüssel). Für größere Daten verwenden Sie eine hybride Verschlüsselung (verschlüsseln Sie die Daten mit einem symmetrischen Schlüssel und dann diesen Schlüssel mit RSA).
- **Schlüsselverteilung**: Teilen Sie den öffentlichen Schlüssel offen; behalten Sie den privaten Schlüssel geheim.

---

### **3. Nachrichtenauthentifizierung mit HMAC**
Ein Message Authentication Code (MAC) stellt die Datenintegrität und Authentizität sicher. Hier erfahren Sie, wie Sie `Mac` mit HMAC-SHA256 verwenden.

#### **Beispielcode**
```java
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import java.nio.charset.StandardCharsets;
import java.util.Base64;

public class MacExample {
    public static void main(String[] args) throws Exception {
        // Schritt 1: Erstellen Sie einen geheimen Schlüssel
        String secret = "mysecretkey";
        SecretKeySpec secretKey = new SecretKeySpec(secret.getBytes(StandardCharsets.UTF_8), "HmacSHA256");

        // Schritt 2: Initialisieren Sie Mac mit dem Schlüssel
        Mac mac = Mac.getInstance("HmacSHA256");
        mac.init(secretKey);

        // Schritt 3: Berechnen Sie den MAC für die Daten
        String data = "Zu authentifizierende Daten";
        byte[] macValue = mac.doFinal(data.getBytes(StandardCharsets.UTF_8));
        String macBase64 = Base64.getEncoder().encodeToString(macValue);

        // Ausgabe des Ergebnisses
        System.out.println("MAC: " + macBase64);
    }
}
```

#### **Wichtige Punkte**
- **Verifikation**: Der Empfänger berechnet den MAC erneut mit dem gleichen Schlüssel und den Daten; wenn er übereinstimmt, sind die Daten authentisch und unverändert.
- **Schlüssel**: Verwenden Sie einen gemeinsam genutzten geheimen Schlüssel, der vorher sicher verteilt wurde.

---

### **4. Verschlüsseln/Entschlüsseln von Streams**
Für große Daten (z.B. Dateien) verwenden Sie `CipherInputStream` oder `CipherOutputStream`.

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
        // Generieren Sie Schlüssel und IV
        KeyGenerator keyGen = KeyGenerator.getInstance("AES");
        keyGen.init(128);
        SecretKey secretKey = keyGen.generateKey();
        byte[] iv = new byte[16];
        new SecureRandom().nextBytes(iv);
        IvParameterSpec ivSpec = new IvParameterSpec(iv);

        // Initialisieren Sie Cipher
        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
        cipher.init(Cipher.ENCRYPT_MODE, secretKey, ivSpec);

        // Verschlüsseln Sie die Datei
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
- **Streams**: Verwenden Sie `CipherOutputStream` für die Verschlüsselung und `CipherInputStream` für die Entschlüsselung, um Daten schrittweise zu verarbeiten.
- **IV-Verarbeitung**: Speichern Sie den IV mit der verschlüsselten Datei (z.B. voranstellen).

---

### **5. Passwortbasierte Verschlüsselung (PBE)**
Leiten Sie einen Schlüssel von einem Passwort mit `SecretKeyFactory` ab.

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

        // Leiten Sie den Schlüssel vom Passwort ab
        PBEKeySpec pbeKeySpec = new PBEKeySpec(password, salt, 10000, 256); // 256-Bit-Schlüssel
        SecretKeyFactory factory = SecretKeyFactory.getInstance("PBKDF2WithHmacSHA256");
        SecretKey tempKey = factory.generateSecret(pbeKeySpec);
        SecretKey secretKey = new SecretKeySpec(tempKey.getEncoded(), "AES");

        // Verschlüsseln Sie mit dem abgeleiteten Schlüssel
        Cipher cipher = Cipher.getInstance("AES");
        cipher.init(Cipher.ENCRYPT_MODE, secretKey);
        String plaintext = "Hallo von PBE";
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
- **`Cipher`**: Führt Verschlüsselung und Entschlüsselung durch.
- **`KeyGenerator`**: Generiert symmetrische Schlüssel (z.B. AES).
- **`KeyPairGenerator`**: Generiert asymmetrische Schlüsselpaare (z.B. RSA).
- **`Mac`**: Berechnet Message Authentication Codes.
- **`SecretKeyFactory`**: Leitet Schlüssel ab (z.B. aus Passwörtern).
- **`SecureRandom`**: Generiert kryptographisch sichere Zufallszahlen.

---

### **Best Practices**
- **Fehlerbehandlung**: Umfassen Sie den Code in try-catch-Blöcke für Ausnahmen wie `NoSuchAlgorithmException`, `InvalidKeyException` usw.
- **Schlüsselverwaltung**: Speichern Sie Schlüssel sicher (z.B. in einem `KeyStore`) und codieren Sie sie niemals fest.
- **Algorithmusauswahl**: Verwenden Sie sichere Algorithmen (z.B. AES-256, RSA-2048) und Modi (z.B. CBC mit IV).
- **Provider**: Der Standard-SunJCE-Provider reicht aus, aber Sie können andere (z.B. BouncyCastle) verwenden, indem Sie `Cipher.getInstance("AES", "BC")` verwenden.

---

### **Fazit**
Um `javax.crypto` zu verwenden, wählen Sie den geeigneten kryptographischen Algorithmus für Ihre Anforderungen aus, generieren oder erhalten Sie Schlüssel und nutzen Sie Klassen wie `Cipher`, `KeyGenerator` und `Mac`, um Operationen durchzuführen. Ob Sie Daten symmetrisch mit AES, asymmetrisch mit RSA verschlüsseln oder die Integrität mit HMAC sicherstellen, `javax.crypto` bietet die Werkzeuge – gepaart mit der richtigen Initialisierung und sicheren Schlüsselverwaltung – um robuste Kryptographie in Java zu implementieren.