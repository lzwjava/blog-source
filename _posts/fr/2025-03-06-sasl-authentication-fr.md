---
audio: false
generated: true
lang: fr
layout: post
title: Authentification SASL en Java
translated: true
type: note
---

Pour utiliser le package `javax.security.sasl` en Java, vous devez exploiter ses classes et interfaces pour implémenter les mécanismes SASL (Simple Authentication and Security Layer) pour l'authentification et, optionnellement, la sécurité des données dans les applications client-serveur. Les classes principales impliquées sont `Sasl`, `SaslClient` et `SaslServer`. Voici un guide complet sur l'utilisation de ce package, incluant les étapes et un exemple de code pour les implémentations client et serveur.

---

### **Aperçu de javax.security.sasl**
Le package `javax.security.sasl` fournit un framework pour l'authentification SASL, couramment utilisé dans des protocoles comme LDAP, IMAP ou des applications personnalisées. Il inclut :
- **`Sasl`** : Une classe utilitaire avec des méthodes statiques pour créer des instances de `SaslClient` et `SaslServer`.
- **`SaslClient`** : Représente le côté client du processus d'authentification SASL.
- **`SaslServer`** : Représente le côté serveur du processus d'authentification SASL.
- **`CallbackHandler`** : Une interface que vous implémentez pour gérer les callbacks d'authentification (par exemple, fournir des noms d'utilisateur ou des mots de passe).

Le processus implique la création d'un `SaslClient` ou d'un `SaslServer`, la fourniture d'un gestionnaire de rappels (callback handler) pour gérer les données d'authentification et la participation à un échange défi-réponse jusqu'à la fin de l'authentification.

---

### **Étapes pour utiliser javax.security.sasl**

#### **1. Déterminer votre rôle (Client ou Serveur)**
Déterminez si votre application agit comme un client (s'authentifiant auprès d'un serveur) ou comme un serveur (authentifiant un client). Cela détermine si vous utiliserez `SaslClient` ou `SaslServer`.

#### **2. Choisir un mécanisme SASL**
SASL prend en charge divers mécanismes, tels que :
- `PLAIN` : Authentification simple par nom d'utilisateur/mot de passe (sans chiffrement).
- `DIGEST-MD5` : Basé sur un mot de passe avec défi-réponse.
- `GSSAPI` : Authentification basée sur Kerberos.

Sélectionnez un mécanisme pris en charge à la fois par le client et le serveur. Pour plus de simplicité, ce guide utilise le mécanisme `PLAIN` comme exemple.

#### **3. Implémenter un CallbackHandler**
Un `CallbackHandler` est requis pour fournir ou vérifier les informations d'authentification. Vous devrez implémenter l'interface `javax.security.auth.callback.CallbackHandler`.

- **Pour un Client** : Fournissez des informations d'identification comme le nom d'utilisateur et le mot de passe.
- **Pour un Serveur** : Vérifiez les informations d'identification du client ou fournissez les données d'authentification côté serveur.

Voici un exemple de `CallbackHandler` côté client pour le mécanisme `PLAIN` :

```java
import javax.security.auth.callback.*;
import java.io.IOException;

public class ClientCallbackHandler implements CallbackHandler {
    private final String username;
    private final String password;

    public ClientCallbackHandler(String username, String password) {
        this.username = username;
        this.password = password;
    }

    @Override
    public void handle(Callback[] callbacks) throws IOException, UnsupportedCallbackException {
        for (Callback callback : callbacks) {
            if (callback instanceof NameCallback) {
                ((NameCallback) callback).setName(username);
            } else if (callback instanceof PasswordCallback) {
                ((PasswordCallback) callback).setPassword(password.toCharArray());
            } else {
                throw new UnsupportedCallbackException(callback, "Callback non supporté");
            }
        }
    }
}
```

Pour le serveur, vous pourriez vérifier les informations d'identification par rapport à une base de données :

```java
public class ServerCallbackHandler implements CallbackHandler {
    @Override
    public void handle(Callback[] callbacks) throws IOException, UnsupportedCallbackException {
        for (Callback callback : callbacks) {
            if (callback instanceof NameCallback) {
                String username = ((NameCallback) callback).getName();
                // Récupérer le mot de passe attendu pour le nom d'utilisateur depuis une base de données
            } else if (callback instanceof PasswordCallback) {
                // Définir le mot de passe attendu pour vérification
                ((PasswordCallback) callback).setPassword("expectedPassword".toCharArray());
            } else if (callback instanceof AuthorizeCallback) {
                AuthorizeCallback ac = (AuthorizeCallback) callback;
                ac.setAuthorized(ac.getAuthenticationID().equals(ac.getAuthorizationID()));
            }
        }
    }
}
```

#### **4. Implémentation Côté Client**
Pour s'authentifier en tant que client :

1. **Créer un SaslClient** :
   Utilisez `Sasl.createSaslClient` avec le mécanisme, le protocole, le nom du serveur, les propriétés et le gestionnaire de rappels.

   ```java
   import javax.security.sasl.Sasl;
   import javax.security.sasl.SaslClient;
   import java.util.HashMap;

   String[] mechanisms = {"PLAIN"};
   String authorizationId = null; // Optionnel ; null si identique à l'ID d'authentification
   String protocol = "ldap"; // par exemple, "ldap", "imap"
   String serverName = "myserver.example.com";
   HashMap<String, Object> props = null; // Propriétés optionnelles, par exemple, QoP
   CallbackHandler cbh = new ClientCallbackHandler("user", "pass");

   SaslClient sc = Sasl.createSaslClient(mechanisms, authorizationId, protocol, serverName, props, cbh);
   ```

2. **Gérer l'échange Défi-Réponse** :
   - Vérifiez la présence d'une réponse initiale (courant dans les mécanismes de type client d'abord comme `PLAIN`).
   - Envoyez les réponses au serveur et traitez les défis jusqu'à la fin de l'authentification.

   ```java
   byte[] response = sc.hasInitialResponse() ? sc.evaluateChallenge(new byte[0]) : null;
   if (response != null) {
       // Envoyer la réponse au serveur (spécifique au protocole, par exemple, via socket ou LDAP BindRequest)
   }

   // Recevoir le défi du serveur (spécifique au protocole)
   byte[] challenge = /* lire depuis le serveur */;
   while (!sc.isComplete()) {
       response = sc.evaluateChallenge(challenge);
       // Envoyer la réponse au serveur
       if (sc.isComplete()) break;
       challenge = /* lire le prochain défi depuis le serveur */;
   }

   // L'authentification est terminée ; vérifier le succès via des moyens spécifiques au protocole
   ```

   Pour `PLAIN`, le client envoie les informations d'identification dans la réponse initiale, et le serveur répond généralement par un succès ou un échec sans défis supplémentaires.

#### **5. Implémentation Côté Serveur**
Pour authentifier un client en tant que serveur :

1. **Créer un SaslServer** :
   Utilisez `Sasl.createSaslServer` avec le mécanisme, le protocole, le nom du serveur, les propriétés et le gestionnaire de rappels.

   ```java
   import javax.security.sasl.Sasl;
   import javax.security.sasl.SaslServer;
   import java.util.HashMap;

   String mechanism = "PLAIN";
   String protocol = "ldap";
   String serverName = "myserver.example.com";
   HashMap<String, Object> props = null;
   CallbackHandler cbh = new ServerCallbackHandler();

   SaslServer ss = Sasl.createSaslServer(mechanism, protocol, serverName, props, cbh);
   ```

2. **Gérer l'échange Défi-Réponse** :
   - Traitez la réponse initiale du client et générez des défis jusqu'à la fin de l'authentification.

   ```java
   byte[] response = /* lire la réponse initiale du client */;
   byte[] challenge = ss.evaluateResponse(response != null ? response : new byte[0]);
   // Envoyer le défi au client (spécifique au protocole)

   while (!ss.isComplete()) {
       response = /* lire la prochaine réponse du client */;
       challenge = ss.evaluateResponse(response);
       if (ss.isComplete()) {
           // Authentification terminée
           break;
       }
       // Envoyer le défi au client
   }

   if (ss.isComplete()) {
       String authorizedUser = ss.getAuthorizationID();
       // Poursuivre avec l'utilisateur autorisé
   }
   ```

   Pour `PLAIN`, le serveur vérifie les informations d'identification dans la réponse initiale et termine l'authentification sans défis supplémentaires.

#### **6. Optionnel : Utiliser les couches de sécurité**
Si le mécanisme (par exemple, `DIGEST-MD5`) prend en charge une couche de sécurité :
- Utilisez `sc.wrap()` et `sc.unwrap()` sur le client, ou `ss.wrap()` et `ss.unwrap()` sur le serveur, pour chiffrer/déchiffrer les messages après l'authentification.
- `PLAIN` ne prend pas en charge les couches de sécurité.

---

### **Points Clés**
- **Intégration** : Intégrez l'échange SASL dans le protocole de communication de votre application (par exemple, les requêtes LDAP Bind, les commandes IMAP AUTHENTICATE).
- **Gestion des erreurs** : Encadrez le code avec des blocs try-catch pour gérer `SaslException` et d'autres erreurs potentielles.
- **Propriétés** : Utilisez la map `props` pour configurer des options comme la qualité de la protection (`"javax.security.sasl.qop"`) si cela est pris en charge par le mécanisme.

---

### **Exemple d'utilisation**
Pour un client LDAP s'authentifiant avec `PLAIN` :
1. Créez un `SaslClient` avec le mécanisme `PLAIN`.
2. Envoyez une `BindRequest` LDAP avec le mécanisme et la réponse initiale (`sc.evaluateChallenge(new byte[0])`).
3. Traitez la `BindResponse` du serveur pour confirmer le succès.

Pour un protocole personnalisé, remplacez les étapes spécifiques à LDAP par les commandes d'authentification de votre protocole.

---

En suivant ces étapes, vous pouvez utiliser efficacement `javax.security.sasl` pour implémenter l'authentification SASL dans votre application Java, en adaptant le processus à votre mécanisme et protocole choisis.