---
audio: false
generated: true
lang: es
layout: post
title: Criptografía en Java
translated: true
---

El paquete `javax.crypto` en Java proporciona un conjunto de clases y métodos para realizar operaciones criptográficas como cifrado, descifrado, generación de claves y autenticación de mensajes. A continuación se presenta una guía completa sobre cómo usar `javax.crypto`, incluyendo explicaciones y ejemplos prácticos para casos de uso comunes como el cifrado simétrico, el cifrado asimétrico y la autenticación de mensajes.

---

### **¿Qué es javax.crypto?**
El paquete `javax.crypto` forma parte de la Arquitectura de Criptografía de Java (JCA) y ofrece herramientas para implementar comunicación segura a través de la criptografía. Soporta:
- **Criptografía simétrica**: Utiliza la misma clave para cifrado y descifrado (por ejemplo, AES, DES).
- **Criptografía asimétrica**: Utiliza un par de claves públicas/privadas (por ejemplo, RSA).
- **Autenticación de mensajes**: Asegura la integridad y autenticidad de los datos (por ejemplo, HMAC).
- **Generación y gestión de claves**: Herramientas para crear y manejar claves criptográficas.

Para usar `javax.crypto`, debes:
1. Seleccionar un algoritmo criptográfico.
2. Generar o obtener las claves necesarias.
3. Usar las clases proporcionadas (por ejemplo, `Cipher`, `KeyGenerator`, `Mac`) para realizar operaciones.

A continuación se presentan ejemplos paso a paso para escenarios comunes.

---

### **1. Cifrado Simétrico con AES**
El cifrado simétrico utiliza una sola clave tanto para cifrar como para descifrar. Aquí se muestra cómo cifrar y descifrar una cadena usando AES (Advanced Encryption Standard) con la clase `Cipher` en modo CBC con relleno PKCS5.

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
        byte[] iv = new byte[16]; // El tamaño del bloque de AES es de 16 bytes
        random.nextBytes(iv);
        IvParameterSpec ivSpec = new IvParameterSpec(iv);

        // Paso 3: Crear e inicializar Cipher para cifrado
        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
        cipher.init(Cipher.ENCRYPT_MODE, secretKey, ivSpec);

        // Paso 4: Cifrar datos
        String plaintext = "¡Hola, Mundo!";
        byte[] plaintextBytes = plaintext.getBytes(StandardCharsets.UTF_8);
        byte[] ciphertext = cipher.doFinal(plaintextBytes);

        // Paso 5: Inicializar Cipher para descifrado con el mismo IV
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
- **Algoritmo**: `"AES/CBC/PKCS5Padding"` especifica AES con modo CBC y relleno para manejar datos que no sean múltiplos del tamaño del bloque.
- **IV**: El Vector de Inicialización debe ser aleatorio para el cifrado y reutilizado para el descifrado. Generalmente se prepende al texto cifrado o se transmite por separado.
- **Gestión de Claves**: En una aplicación real, comparte la `secretKey` de manera segura con el destinatario.

---

### **2. Cifrado Asimétrico con RSA**
El cifrado asimétrico utiliza una clave pública para cifrar y una clave privada para descifrar. Aquí hay un ejemplo usando RSA.

#### **Pasos**
- Generar un par de claves públicas/privadas.
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
        String plaintext = "Mensaje Secreto";
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
- **Límite de Tamaño**: RSA solo puede cifrar datos más pequeños que el tamaño de la clave (por ejemplo, ~245 bytes para una clave de 2048 bits). Para datos más grandes, usa cifrado híbrido (cifra los datos con una clave simétrica, luego cifra esa clave con RSA).
- **Distribución de Claves**: Comparte la clave pública de manera abierta; mantén la clave privada en secreto.

---

### **3. Autenticación de Mensajes con HMAC**
Un Código de Autenticación de Mensajes (MAC) asegura la integridad y autenticidad de los datos. Aquí se muestra cómo usar `Mac` con HMAC-SHA256.

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

        // Paso 3: Computar MAC para los datos
        String data = "Datos para autenticar";
        byte[] macValue = mac.doFinal(data.getBytes(StandardCharsets.UTF_8));
        String macBase64 = Base64.getEncoder().encodeToString(macValue);

        // Mostrar resultado
        System.out.println("MAC: " + macBase64);
    }
}
```

#### **Puntos Clave**
- **Verificación**: El destinatario recomputa el MAC con la misma clave y datos; si coincide, los datos son auténticos e inalterados.
- **Clave**: Usa una clave secreta compartida, distribuida de manera segura con antelación.

---

### **4. Cifrando/Descifrando Flujos**
Para datos grandes (por ejemplo, archivos), usa `CipherInputStream` o `CipherOutputStream`.

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
- **Flujos**: Usa `CipherOutputStream` para cifrado y `CipherInputStream` para descifrado para procesar datos de manera incremental.
- **Manejo de IV**: Almacena el IV con el archivo cifrado (por ejemplo, préndelo).

---

### **5. Cifrado Basado en Contraseñas (PBE)**
Deriva una clave de una contraseña usando `SecretKeyFactory`.

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
        // Contraseña y sal
        char[] password = "mysecretpassword".toCharArray();
        byte[] salt = new byte[16];
        new SecureRandom().nextBytes(salt);

        // Derivar clave de la contraseña
        PBEKeySpec pbeKeySpec = new PBEKeySpec(password, salt, 10000, 256); // Clave de 256 bits
        SecretKeyFactory factory = SecretKeyFactory.getInstance("PBKDF2WithHmacSHA256");
        SecretKey tempKey = factory.generateSecret(pbeKeySpec);
        SecretKey secretKey = new SecretKeySpec(tempKey.getEncoded(), "AES");

        // Cifrar con clave derivada
        Cipher cipher = Cipher.getInstance("AES");
        cipher.init(Cipher.ENCRYPT_MODE, secretKey);
        String plaintext = "Hola desde PBE";
        byte[] ciphertext = cipher.doFinal(plaintext.getBytes(StandardCharsets.UTF_8));

        System.out.println("Cifrado: " + Base64.getEncoder().encodeToString(ciphertext));
    }
}
```

#### **Puntos Clave**
- **Sal**: Aleatoriza la derivación de la clave; almacénala con los datos cifrados.
- **Iteraciones**: Aumenta el costo computacional para contrarrestar ataques de fuerza bruta (por ejemplo, 10,000).

---

### **Clases Clave en javax.crypto**
- **`Cipher`**: Realiza cifrado y descifrado.
- **`KeyGenerator`**: Genera claves simétricas (por ejemplo, AES).
- **`KeyPairGenerator`**: Genera pares de claves asimétricas (por ejemplo, RSA).
- **`Mac`**: Computa códigos de autenticación de mensajes.
- **`SecretKeyFactory`**: Deriva claves (por ejemplo, de contraseñas).
- **`SecureRandom`**: Genera números aleatorios criptográficamente seguros.

---

### **Mejores Prácticas**
- **Manejo de Excepciones**: Envuelve el código en bloques try-catch para excepciones como `NoSuchAlgorithmException`, `InvalidKeyException`, etc.
- **Gestión de Claves**: Almacena las claves de manera segura (por ejemplo, en un `KeyStore`) y nunca las codifiques de manera fija.
- **Elección del Algoritmo**: Usa algoritmos seguros (por ejemplo, AES-256, RSA-2048) y modos (por ejemplo, CBC con IV).
- **Proveedores**: El proveedor SunJCE predeterminado es suficiente, pero puedes usar otros (por ejemplo, BouncyCastle) a través de `Cipher.getInstance("AES", "BC")`.

---

### **Conclusión**
Para usar `javax.crypto`, selecciona el algoritmo criptográfico adecuado para tus necesidades, genera o obtiene claves y aprovecha clases como `Cipher`, `KeyGenerator` y `Mac` para realizar operaciones. Ya sea cifrando datos simétricamente con AES, asimétricamente con RSA o asegurando la integridad con HMAC, `javax.crypto` proporciona las herramientas—emparejadas con una inicialización adecuada y una gestión segura de claves—para implementar criptografía robusta en Java.