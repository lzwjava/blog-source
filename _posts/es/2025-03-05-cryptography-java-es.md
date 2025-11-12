---
audio: false
generated: true
lang: es
layout: post
title: Criptografía en Java
translated: true
type: note
---

El paquete `javax.crypto` en Java proporciona un conjunto de clases y métodos para realizar operaciones criptográficas como cifrado, descifrado, generación de claves y autenticación de mensajes. A continuación se presenta una guía completa sobre cómo usar `javax.crypto`, incluyendo explicaciones y ejemplos prácticos para casos de uso comunes como cifrado simétrico, cifrado asimétrico y autenticación de mensajes.

---

### **¿Qué es javax.crypto?**
El paquete `javax.crypto` es parte de la Arquitectura de Criptografía de Java (JCA) y ofrece herramientas para implementar comunicación segura a través de criptografía. Soporta:
- **Criptografía simétrica**: Utiliza la misma clave para cifrar y descifrar (ej., AES, DES).
- **Criptografía asimétrica**: Utiliza un par de claves pública/privada (ej., RSA).
- **Autenticación de mensajes**: Garantiza la integridad y autenticidad de los datos (ej., HMAC).
- **Generación y gestión de claves**: Herramientas para crear y manejar claves criptográficas.

Para usar `javax.crypto`, necesitas:
1. Seleccionar un algoritmo criptográfico.
2. Generar u obtener las claves necesarias.
3. Usar las clases proporcionadas (ej., `Cipher`, `KeyGenerator`, `Mac`) para realizar las operaciones.

A continuación se presentan ejemplos paso a paso para escenarios comunes.

---

### **1. Cifrado Simétrico con AES**
El cifrado simétrico utiliza una única clave para cifrar y descifrar. Aquí se muestra cómo cifrar y descifrar una cadena usando AES (Advanced Encryption Standard) con la clase `Cipher` en modo CBC con relleno PKCS5.

#### **Pasos**
- Generar una clave secreta.
- Crear e inicializar una instancia de `Cipher`.
- Cifrar y descifrar los datos.

#### **Código de Ejemplo**
```java
import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import javax.crypto.spec.IvParameterSpec;
import java.security.SecureRandom;
import java.nio.charset.StandardCharsets;

public class SymmetricEncryptionExample {
    public static void main(String[] args) throws Exception {
        // Paso 1: Generar una clave secreta para AES
        KeyGenerator keyGen = KeyGenerator.getInstance("AES");
        keyGen.init(128); // Clave de 128 bits
        SecretKey secretKey = keyGen.generateKey();

        // Paso 2: Generar un Vector de Inicialización (IV) aleatorio
        SecureRandom random = new SecureRandom();
        byte[] iv = new byte[16]; // El tamaño de bloque de AES es de 16 bytes
        random.nextBytes(iv);
        IvParameterSpec ivSpec = new IvParameterSpec(iv);

        // Paso 3: Crear e inicializar Cipher para el cifrado
        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
        cipher.init(Cipher.ENCRYPT_MODE, secretKey, ivSpec);

        // Paso 4: Cifrar datos
        String plaintext = "Hello, World!";
        byte[] plaintextBytes = plaintext.getBytes(StandardCharsets.UTF_8);
        byte[] ciphertext = cipher.doFinal(plaintextBytes);

        // Paso 5: Inicializar Cipher para el descifrado con el mismo IV
        cipher.init(Cipher.DECRYPT_MODE, secretKey, ivSpec);
        byte[] decryptedBytes = cipher.doFinal(ciphertext);
        String decryptedText = new String(decryptedBytes, StandardCharsets.UTF_8);

        // Mostrar resultados
        System.out.println("Original: " + plaintext);
        System.out.println("Descifrado: " + decryptedText);
    }
}
```

#### **Puntos Clave**
- **Algoritmo**: `"AES/CBC/PKCS5Padding"` especifica AES con modo CBC y relleno para manejar datos que no son múltiplo del tamaño del bloque.
- **IV**: El Vector de Inicialización debe ser aleatorio para el cifrado y reutilizado para el descifrado. Normalmente se antepone al texto cifrado o se transmite por separado.
- **Gestión de Claves**: En una aplicación real, comparte la `secretKey` de forma segura con el destinatario.

---

### **2. Cifrado Asimétrico con RSA**
El cifrado asimétrico utiliza una clave pública para cifrar y una clave privada para descifrar. Aquí hay un ejemplo usando RSA.

#### **Pasos**
- Generar un par de claves pública/privada.
- Cifrar con la clave pública.
- Descifrar con la clave privada.

#### **Código de Ejemplo**
```java
import javax.crypto.Cipher;
import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.PrivateKey;
import java.security.PublicKey;
import java.nio.charset.StandardCharsets;

public class AsymmetricEncryptionExample {
    public static void main(String[] args) throws Exception {
        // Paso 1: Generar un par de claves RSA
        KeyPairGenerator keyPairGen = KeyPairGenerator.getInstance("RSA");
        keyPairGen.initialize(2048); // Clave de 2048 bits
        KeyPair keyPair = keyPairGen.generateKeyPair();
        PublicKey publicKey = keyPair.getPublic();
        PrivateKey privateKey = keyPair.getPrivate();

        // Paso 2: Cifrar con la clave pública
        Cipher cipher = Cipher.getInstance("RSA");
        cipher.init(Cipher.ENCRYPT_MODE, publicKey);
        String plaintext = "Secret Message";
        byte[] plaintextBytes = plaintext.getBytes(StandardCharsets.UTF_8);
        byte[] ciphertext = cipher.doFinal(plaintextBytes);

        // Paso 3: Descifrar con la clave privada
        cipher.init(Cipher.DECRYPT_MODE, privateKey);
        byte[] decryptedBytes = cipher.doFinal(ciphertext);
        String decryptedText = new String(decryptedBytes, StandardCharsets.UTF_8);

        // Mostrar resultados
        System.out.println("Original: " + plaintext);
        System.out.println("Descifrado: " + decryptedText);
    }
}
```

#### **Puntos Clave**
- **Límite de Tamaño**: RSA solo puede cifrar datos más pequeños que el tamaño de la clave (ej., ~245 bytes para una clave de 2048 bits). Para datos más grandes, usa cifrado híbrido (cifra los datos con una clave simétrica, luego cifra esa clave con RSA).
- **Distribución de Claves**: Comparte la clave pública abiertamente; mantén la clave privada en secreto.

---

### **3. Autenticación de Mensajes con HMAC**
Un Código de Autenticación de Mensajes (MAC) garantiza la integridad y autenticidad de los datos. Aquí se muestra cómo usar `Mac` con HMAC-SHA256.

#### **Código de Ejemplo**
```java
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import java.nio.charset.StandardCharsets;
import java.util.Base64;

public class MacExample {
    public static void main(String[] args) throws Exception {
        // Paso 1: Crear una clave secreta
        String secret = "mysecretkey";
        SecretKeySpec secretKey = new SecretKeySpec(secret.getBytes(StandardCharsets.UTF_8), "HmacSHA256");

        // Paso 2: Inicializar Mac con la clave
        Mac mac = Mac.getInstance("HmacSHA256");
        mac.init(secretKey);

        // Paso 3: Calcular el MAC para los datos
        String data = "Data to authenticate";
        byte[] macValue = mac.doFinal(data.getBytes(StandardCharsets.UTF_8));
        String macBase64 = Base64.getEncoder().encodeToString(macValue);

        // Mostrar resultado
        System.out.println("MAC: " + macBase64);
    }
}
```

#### **Puntos Clave**
- **Verificación**: El destinatario recalcula el MAC con la misma clave y datos; si coincide, los datos son auténticos y no han sido alterados.
- **Clave**: Usa una clave secreta compartida, distribuida de forma segura de antemano.

---

### **4. Cifrado/Descifrado de Flujos**
Para datos grandes (ej., archivos), usa `CipherInputStream` o `CipherOutputStream`.

#### **Código de Ejemplo (Cifrando un Archivo)**
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
        // Generar clave e IV
        KeyGenerator keyGen = KeyGenerator.getInstance("AES");
        keyGen.init(128);
        SecretKey secretKey = keyGen.generateKey();
        byte[] iv = new byte[16];
        new SecureRandom().nextBytes(iv);
        IvParameterSpec ivSpec = new IvParameterSpec(iv);

        // Inicializar Cipher
        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
        cipher.init(Cipher.ENCRYPT_MODE, secretKey, ivSpec);

        // Cifrar archivo
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

#### **Puntos Clave**
- **Flujos**: Usa `CipherOutputStream` para cifrar y `CipherInputStream` para descifrar y procesar datos de forma incremental.
- **Manejo del IV**: Almacena el IV con el archivo cifrado (ej., anteponiéndolo).

---

### **5. Cifrado Basado en Contraseñas (PBE)**
Deriva una clave a partir de una contraseña usando `SecretKeyFactory`.

#### **Código de Ejemplo**
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
        // Contraseña y salt
        char[] password = "mysecretpassword".toCharArray();
        byte[] salt = new byte[16];
        new SecureRandom().nextBytes(salt);

        // Derivar clave a partir de la contraseña
        PBEKeySpec pbeKeySpec = new PBEKeySpec(password, salt, 10000, 256); // Clave de 256 bits
        SecretKeyFactory factory = SecretKeyFactory.getInstance("PBKDF2WithHmacSHA256");
        SecretKey tempKey = factory.generateSecret(pbeKeySpec);
        SecretKey secretKey = new SecretKeySpec(tempKey.getEncoded(), "AES");

        // Cifrar con la clave derivada
        Cipher cipher = Cipher.getInstance("AES");
        cipher.init(Cipher.ENCRYPT_MODE, secretKey);
        String plaintext = "Hello from PBE";
        byte[] ciphertext = cipher.doFinal(plaintext.getBytes(StandardCharsets.UTF_8));

        System.out.println("Cifrado: " + Base64.getEncoder().encodeToString(ciphertext));
    }
}
```

#### **Puntos Clave**
- **Salt**: Aleatoriza la derivación de la clave; almacénalo con los datos cifrados.
- **Iteraciones**: Aumenta el coste computacional para frustrar ataques de fuerza bruta (ej., 10,000).

---

### **Claves Principales en javax.crypto**
- **`Cipher`**: Realiza cifrado y descifrado.
- **`KeyGenerator`**: Genera claves simétricas (ej., AES).
- **`KeyPairGenerator`**: Genera pares de claves asimétricas (ej., RSA).
- **`Mac`**: Calcula códigos de autenticación de mensajes.
- **`SecretKeyFactory`**: Deriva claves (ej., a partir de contraseñas).
- **`SecureRandom`**: Genera números aleatorios criptográficamente seguros.

---

### **Mejores Prácticas**
- **Manejo de Excepciones**: Envuelve el código en bloques try-catch para excepciones como `NoSuchAlgorithmException`, `InvalidKeyException`, etc.
- **Gestión de Claves**: Almacena las claves de forma segura (ej., en un `KeyStore`) y nunca las codifiques directamente en el código.
- **Elección de Algoritmo**: Usa algoritmos seguros (ej., AES-256, RSA-2048) y modos (ej., CBC con IV).
- **Proveedores**: El proveedor por defecto SunJCE es suficiente, pero puedes usar otros (ej., BouncyCastle) mediante `Cipher.getInstance("AES", "BC")`.

---

### **Conclusión**
Para usar `javax.crypto`, selecciona el algoritmo criptográfico apropiado para tus necesidades, genera u obtén las claves, y aprovecha clases como `Cipher`, `KeyGenerator` y `Mac` para realizar las operaciones. Ya sea cifrando datos simétricamente con AES, asimétricamente con RSA, o garantizando la integridad con HMAC, `javax.crypto` proporciona las herramientas—combinadas con una inicialización adecuada y una gestión segura de claves—para implementar criptografía robusta en Java.