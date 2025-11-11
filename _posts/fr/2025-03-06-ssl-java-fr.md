---
audio: false
generated: true
lang: fr
layout: post
title: Connexions sécurisées en Java
translated: true
type: note
---

Pour utiliser le package `javax.net.ssl` en Java, vous devez exploiter ses classes pour établir une communication sécurisée sur le réseau en utilisant les protocoles SSL (Secure Sockets Layer) ou TLS (Transport Layer Security). Ce package est essentiel pour créer des connexions sécurisées, comme celles utilisées dans la communication HTTPS. Ci-dessous, je vais expliquer comment l'utiliser pour les applications côté client et côté serveur, y compris des exemples de base et des considérations clés.

---

### **Aperçu de `javax.net.ssl`**
Le package `javax.net.ssl` fournit des outils pour la communication sécurisée par socket. Il inclut :
- **`SSLSocket`** : Un socket côté client pour la communication sécurisée.
- **`SSLServerSocket`** : Un socket côté serveur pour accepter les connexions sécurisées.
- **`SSLSocketFactory`** : Une usine pour créer des instances de `SSLSocket`.
- **`SSLServerSocketFactory`** : Une usine pour créer des instances de `SSLServerSocket`.
- **`SSLContext`** : Une classe pour configurer le protocole SSL/TLS, permettant la personnalisation des paramètres de sécurité.
- **`KeyManager` et `TrustManager`** : Des classes pour gérer les certificats et les décisions de confiance.

Ces composants permettent l'échange de données chiffrées, garantissant la confidentialité et l'intégrité entre un client et un serveur.

---

### **Utilisation de `javax.net.ssl` en tant que Client**
Pour une application cliente se connectant à un serveur sécurisé (par exemple, un serveur HTTPS), vous utilisez généralement `SSLSocketFactory` pour créer un `SSLSocket`. Voici comment :

#### **Étapes**
1. **Obtenir une `SSLSocketFactory`** :
   Utilisez l'usine par défaut fournie par Java, qui s'appuie sur les paramètres SSL/TLS par défaut du système et le truststore (un dépôt de certificats de confiance).

   ```java
   import javax.net.ssl.SSLSocketFactory;
   SSLSocketFactory factory = (SSLSocketFactory) SSLSocketFactory.getDefault();
   ```

2. **Créer un `SSLSocket`** :
   Utilisez l'usine pour vous connecter à un serveur en spécifiant le nom d'hôte et le port (par exemple, 443 pour HTTPS).

   ```java
   import javax.net.ssl.SSLSocket;
   SSLSocket socket = (SSLSocket) factory.createSocket("example.com", 443);
   ```

3. **Communiquer via le Socket** :
   Utilisez les flux d'entrée et de sortie du socket pour envoyer et recevoir des données. Le handshake SSL/TLS (qui établit la connexion sécurisée) se produit automatiquement lorsque vous lisez ou écrivez sur le socket pour la première fois.

#### **Exemple : Envoi d'une requête HTTP GET**
Voici un exemple complet qui se connecte à un serveur et récupère une page web :

```java
import javax.net.ssl.SSLSocket;
import javax.net.ssl.SSLSocketFactory;
import java.io.*;

public class SSLClientExample {
    public static void main(String[] args) {
        try {
            // Obtenir la SSLSocketFactory par défaut
            SSLSocketFactory factory = (SSLSocketFactory) SSLSocketFactory.getDefault();
            // Créer un SSLSocket vers example.com sur le port 443
            SSLSocket socket = (SSLSocket) factory.createSocket("example.com", 443);

            // Obtenir les flux d'entrée et de sortie
            OutputStream out = socket.getOutputStream();
            InputStream in = socket.getInputStream();

            // Envoyer une simple requête HTTP GET
            String request = "GET / HTTP/1.1\r\nHost: example.com\r\n\r\n";
            out.write(request.getBytes());
            out.flush();

            // Lire et afficher la réponse
            BufferedReader reader = new BufferedReader(new InputStreamReader(in));
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }

            // Fermer le socket
            socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

#### **Notes importantes**
- **Handshake** : Le handshake SSL/TLS est géré automatiquement lorsque vous utilisez le socket.
- **Confiance** : Par défaut, Java fait confiance aux certificats signés par des Autorités de Certification (CA) bien connues stockées dans son truststore. Si le certificat du serveur n'est pas approuvé, vous devrez configurer un truststore personnalisé (nous en reparlerons plus tard).
- **Vérification du nom d'hôte** : `SSLSocket` n'effectue pas de vérification du nom d'hôte par défaut (contrairement à `HttpsURLConnection`). Pour l'activer, utilisez `SSLParameters` :

   ```java
   import javax.net.ssl.SSLParameters;
   SSLParameters params = new SSLParameters();
   params.setEndpointIdentificationAlgorithm("HTTPS");
   socket.setSSLParameters(params);
   ```

   Cela garantit que le certificat du serveur correspond au nom d'hôte, empêchant les attaques de type man-in-the-middle.

---

### **Utilisation de `javax.net.ssl` en tant que Serveur**
Pour un serveur acceptant des connexions sécurisées, vous utilisez `SSLServerSocketFactory` pour créer un `SSLServerSocket`. Le serveur doit fournir un certificat, généralement stocké dans un keystore.

#### **Étapes**
1. **Configurer un Keystore** :
   Créez un keystore contenant la clé privée et le certificat du serveur (par exemple, en utilisant l'outil `keytool` de Java pour générer un fichier `.jks`).

2. **Initialiser un `SSLContext`** :
   Utilisez le keystore pour configurer un `SSLContext` avec un `KeyManager`.

   ```java
   import javax.net.ssl.*;
   import java.io.FileInputStream;
   import java.security.KeyStore;

   KeyStore ks = KeyStore.getInstance("JKS");
   ks.load(new FileInputStream("keystore.jks"), "password".toCharArray());

   KeyManagerFactory kmf = KeyManagerFactory.getInstance("SunX509");
   kmf.init(ks, "password".toCharArray());

   SSLContext context = SSLContext.getInstance("TLS");
   context.init(kmf.getKeyManagers(), null, null);
   ```

3. **Créer un `SSLServerSocket`** :
   Utilisez la `SSLServerSocketFactory` du `SSLContext` pour créer un socket serveur.

   ```java
   SSLServerSocketFactory factory = context.getServerSocketFactory();
   SSLServerSocket serverSocket = (SSLServerSocket) factory.createServerSocket(8443);
   ```

4. **Accepter les Connexions** :
   Acceptez les connexions des clients et communiquez via le `SSLSocket` résultant.

#### **Exemple : Serveur SSL Simple**
```java
import javax.net.ssl.*;
import java.io.*;
import java.security.KeyStore;

public class SSLServerExample {
    public static void main(String[] args) {
        try {
            // Charger le keystore
            KeyStore ks = KeyStore.getInstance("JKS");
            ks.load(new FileInputStream("keystore.jks"), "password".toCharArray());

            // Initialiser KeyManagerFactory
            KeyManagerFactory kmf = KeyManagerFactory.getInstance("SunX509");
            kmf.init(ks, "password".toCharArray());

            // Initialiser SSLContext
            SSLContext context = SSLContext.getInstance("TLS");
            context.init(kmf.getKeyManagers(), null, null);

            // Créer le SSLServerSocket
            SSLServerSocketFactory factory = context.getServerSocketFactory();
            SSLServerSocket serverSocket = (SSLServerSocket) factory.createServerSocket(8443);

            System.out.println("Serveur démarré sur le port 8443...");
            while (true) {
                SSLSocket socket = (SSLSocket) serverSocket.accept();
                System.out.println("Client connecté.");

                // Gérer la communication avec le client
                BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
                out.println("Bonjour du serveur sécurisé !");
                socket.close();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

#### **Notes importantes**
- **Keystore** : Le serveur nécessite un certificat, généralement dans un fichier `.jks`, que vous devez générer et configurer.
- **Authentification du Client** : Si le serveur exige que les clients fournissent des certificats, initialisez le `SSLContext` avec un `TrustManager` et appelez `serverSocket.setNeedClientAuth(true)`.

---

### **Configuration Avancée**
Pour plus de contrôle sur le comportement SSL/TLS, vous pouvez personnaliser les éléments suivants :

#### **1. Truststore Personnalisé**
Si le certificat du serveur n'est pas signé par une CA de confiance, chargez un truststore personnalisé :

```java
KeyStore trustStore = KeyStore.getInstance("JKS");
trustStore.load(new FileInputStream("truststore.jks"), "password".toCharArray());

TrustManagerFactory tmf = TrustManagerFactory.getInstance("SunX509");
tmf.init(trustStore);

SSLContext context = SSLContext.getInstance("TLS");
context.init(null, tmf.getTrustManagers(), null);

SSLSocketFactory factory = context.getSocketFactory();
```

#### **2. Versions de Protocole**
Spécifiez des protocoles sécurisés (par exemple, TLS 1.2 ou 1.3) pour éviter les versions obsolètes et non sécurisées :

```java
socket.setEnabledProtocols(new String[] {"TLSv1.2", "TLSv1.3"});
```

#### **3. Suites de Chiffrement**
Restreignez les suites de chiffrement utilisées pour le chiffrement :

```java
socket.setEnabledCipherSuites(new String[] {"TLS_AES_128_GCM_SHA256"});
```

---

### **Résumé**
Pour utiliser `javax.net.ssl` :
- **Pour les Clients** : Utilisez `SSLSocketFactory` pour créer un `SSLSocket`, connectez-vous à un serveur et configurez éventuellement la vérification du nom d'hôte avec `SSLParameters`.
- **Pour les Serveurs** : Configurez un `SSLContext` avec un keystore et un `KeyManager`, puis utilisez `SSLServerSocketFactory` pour créer un `SSLServerSocket`.
- **Personnalisation** : Utilisez `SSLContext`, `KeyManager` et `TrustManager` pour une gestion avancée des certificats, et définissez les protocoles ou les suites de chiffrement selon les besoins.

Ce package fournit les bases de la communication sécurisée en Java, adaptée à la fois aux applications simples et complexes. Pour HTTPS spécifiquement, envisagez des API de plus haut niveau comme `HttpsURLConnection`, mais `javax.net.ssl` vous donne un contrôle direct sur les sockets SSL/TLS lorsque cela est nécessaire.