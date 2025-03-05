---
audio: false
generated: true
lang: fr
layout: post
title: Authentification et Autorisation en Java
translated: true
---

Pour utiliser le package `javax.security.auth` en Java, il est important de comprendre qu'il fait partie du cadre Java Authentication and Authorization Service (JAAS). Ce package fournit des classes et des interfaces pour authentifier les utilisateurs (vérifier qui ils sont) et les autoriser (déterminer ce qu'ils peuvent faire). Voici un guide étape par étape pour utiliser `javax.security.auth` dans un scénario d'authentification de base, tel que l'authentification d'un utilisateur avec un nom d'utilisateur et un mot de passe.

---

### **Aperçu des Concepts Clés**
Avant de plonger dans les étapes, voici une brève explication des composants principaux dans `javax.security.auth` :

- **Subject** : Représente une entité (par exemple, un utilisateur ou un service) en cours d'authentification. Il peut avoir plusieurs identités (Principals) et justificatifs d'identité (par exemple, des mots de passe ou des certificats).
- **Principal** : Une identité ou un rôle associé à un Subject, tel qu'un nom d'utilisateur ou une appartenance à un groupe.
- **Credential** : Information utilisée pour authentifier un Subject, telle qu'un mot de passe ou une clé cryptographique.
- **LoginModule** : Un composant pluggable qui effectue la logique d'authentification (par exemple, vérifier un nom d'utilisateur et un mot de passe contre une base de données).
- **LoginContext** : La classe centrale qui coordonne le processus d'authentification en utilisant un ou plusieurs LoginModules.
- **CallbackHandler** : Une interface pour interagir avec l'utilisateur, telle que la demande d'un nom d'utilisateur et d'un mot de passe.

Avec ces concepts en tête, explorons comment utiliser le package.

---

### **Étapes pour Utiliser `javax.security.auth`**

#### **1. Configurer un JAAS**
Le processus d'authentification repose sur une configuration qui spécifie quel(s) `LoginModule`(s) utiliser. Cela peut être défini dans un fichier de configuration ou de manière programmatique.

Par exemple, créez un fichier nommé `jaas.config` avec le contenu suivant :

```
MyApp {
    com.example.MyLoginModule required;
};
```

- **`MyApp`** : Le nom de l'application ou du contexte, que vous référencerez dans votre code.
- **`com.example.MyLoginModule`** : Le nom qualifié complet de votre `LoginModule` personnalisé (vous l'implémenterez plus tard).
- **`required`** : Un indicateur indiquant que ce module doit réussir pour que l'authentification passe. D'autres indicateurs incluent `requisite`, `sufficient`, et `optional`, qui permettent une logique plus complexe avec plusieurs modules.

Définissez la propriété système pour pointer vers ce fichier :

```java
System.setProperty("java.security.auth.login.config", "jaas.config");
```

Alternativement, vous pouvez définir la configuration de manière programmatique, mais un fichier est plus simple pour la plupart des cas.

#### **2. Implémenter un CallbackHandler**
Un `CallbackHandler` collecte les entrées de l'utilisateur, telles qu'un nom d'utilisateur et un mot de passe. Voici une implémentation simple utilisant la console :

```java
import javax.security.auth.callback.*;
import java.io.*;

public class MyCallbackHandler implements CallbackHandler {
    public void handle(Callback[] callbacks) throws IOException, UnsupportedCallbackException {
        for (Callback callback : callbacks) {
            if (callback instanceof NameCallback) {
                NameCallback nc = (NameCallback) callback;
                System.out.print(nc.getPrompt());
                nc.setName(System.console().readLine());
            } else if (callback instanceof PasswordCallback) {
                PasswordCallback pc = (PasswordCallback) callback;
                System.out.print(pc.getPrompt());
                pc.setPassword(System.console().readPassword());
            } else {
                throw new UnsupportedCallbackException(callback, "Unsupported callback");
            }
        }
    }
}
```

- **NameCallback** : Demande et récupère le nom d'utilisateur.
- **PasswordCallback** : Demande et récupère le mot de passe (stocker sous forme de `char[]` pour des raisons de sécurité).

#### **3. Implémenter un LoginModule**
Un `LoginModule` définit la logique d'authentification. Voici un exemple de base qui vérifie contre un nom d'utilisateur et un mot de passe codés en dur (en pratique, vous utiliseriez une base de données ou un service externe) :

```java
import javax.security.auth.*;
import javax.security.auth.callback.*;
import javax.security.auth.login.*;
import javax.security.auth.spi.*;
import java.security.Principal;
import java.util.*;

public class MyLoginModule implements LoginModule {
    private Subject subject;
    private CallbackHandler callbackHandler;
    private boolean succeeded = false;

    // Initialiser le module
    public void initialize(Subject subject, CallbackHandler callbackHandler,
                           Map<String, ?> sharedState, Map<String, ?> options) {
        this.subject = subject;
        this.callbackHandler = callbackHandler;
    }

    // Effectuer l'authentification
    public boolean login() throws LoginException {
        if (callbackHandler == null) {
            throw new LoginException("No callback handler provided");
        }

        try {
            NameCallback nameCallback = new NameCallback("Username: ");
            PasswordCallback passwordCallback = new PasswordCallback("Password: ", false);
            callbackHandler.handle(new Callback[]{nameCallback, passwordCallback});

            String username = nameCallback.getName();
            char[] password = passwordCallback.getPassword();

            // Vérification codée en dur (remplacer par une logique réelle en pratique)
            if ("myuser".equals(username) && "mypassword".equals(new String(password))) {
                succeeded = true;
                return true;
            } else {
                succeeded = false;
                throw new FailedLoginException("Authentication failed");
            }
        } catch (Exception e) {
            throw new LoginException("Login error: " + e.getMessage());
        }
    }

    // Valider l'authentification (ajouter des Principals au Subject)
    public boolean commit() throws LoginException {
        if (succeeded) {
            subject.getPrincipals().add(new MyPrincipal("myuser"));
            return true;
        }
        return false;
    }

    // Annuler le processus d'authentification
    public boolean abort() throws LoginException {
        succeeded = false;
        return true;
    }

    // Déconnecter le Subject
    public boolean logout() throws LoginException {
        subject.getPrincipals().clear();
        subject.getPublicCredentials().clear();
        subject.getPrivateCredentials().clear();
        return true;
    }
}

// Implémentation simple de Principal
class MyPrincipal implements Principal {
    private String name;

    public MyPrincipal(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }
}
```

- **login()** : Utilise le `CallbackHandler` pour obtenir les justificatifs d'identité et les vérifier.
- **commit()** : Si l'authentification réussit, ajoute un `Principal` au `Subject`.
- **abort()** et **logout()** : Gèrent le nettoyage ou l'annulation.

#### **4. Authentifier en Utilisant LoginContext**
Maintenant, utilisez `LoginContext` pour effectuer l'authentification dans votre application principale :

```java
import javax.security.auth.login.*;
import java.security.Principal;

public class Main {
    public static void main(String[] args) {
        // Assurez-vous que la configuration JAAS est définie
        System.setProperty("java.security.auth.login.config", "jaas.config");

        try {
            // Créer LoginContext avec le nom de la configuration et CallbackHandler
            LoginContext lc = new LoginContext("MyApp", new MyCallbackHandler());

            // Effectuer l'authentification
            lc.login();

            // Obtenir le Subject authentifié
            Subject subject = lc.getSubject();
            System.out.println("Subject authentifié : " + subject);

            // Afficher les Principals du Subject
            for (Principal p : subject.getPrincipals()) {
                System.out.println("Principal : " + p.getName());
            }

            // Déconnecter lorsque terminé
            lc.logout();
        } catch (LoginException e) {
            System.err.println("Authentication failed: " + e.getMessage());
        }
    }
}
```

- **`LoginContext lc = new LoginContext("MyApp", new MyCallbackHandler())`** : Lie à la configuration `"MyApp"` et utilise `MyCallbackHandler`.
- **`lc.login()`** : Déclenche le processus d'authentification.
- **`lc.getSubject()`** : Récupère le `Subject` authentifié.

#### **5. Effectuer des Actions Autorisées (Optionnel)**
Une fois authentifié, vous pouvez utiliser le `Subject` pour exécuter du code avec ses privilèges en utilisant `Subject.doAs()` :

```java
import java.security.PrivilegedAction;

Subject.doAs(subject, new PrivilegedAction<Void>() {
    public Void run() {
        System.out.println("Running as: " + Subject.getSubject(java.security.AccessController.getContext()));
        // Effectuer des actions privilégiées ici
        return null;
    }
});
```

Cela est utile pour l'autorisation, où les actions sont restreintes en fonction des `Principals` du `Subject`.

---

### **Tout Assembler**
1. **Configuration** : Définir `jaas.config` avec votre `LoginModule`.
2. **CallbackHandler** : Implémenter `MyCallbackHandler` pour collecter les entrées de l'utilisateur.
3. **LoginModule** : Implémenter `MyLoginModule` avec votre logique d'authentification.
4. **Code Principal** : Utiliser `LoginContext` pour authentifier et récupérer un `Subject`.
5. **Autorisation** : Utiliser `Subject.doAs()` pour des actions privilégiées si nécessaire.

Lorsque vous exécutez la classe `Main`, elle :
- Demande un nom d'utilisateur et un mot de passe.
- Authentifie en utilisant `MyLoginModule`.
- Affiche le `Subject` et ses `Principals` en cas de succès.

---

### **Notes Supplémentaires**
- **Utilisation dans le Monde Réel** : Remplacez les justificatifs d'identité codés en dur dans `MyLoginModule` par des vérifications contre une base de données, LDAP, ou un autre service. Java fournit des modules standard comme `Krb5LoginModule` (Kerberos) ou `JndiLoginModule` (LDAP), mais ils peuvent nécessiter une configuration supplémentaire.
- **Multiples LoginModules** : La configuration peut spécifier plusieurs modules avec des indicateurs (`required`, `sufficient`, etc.) pour créer des flux d'authentification complexes.
- **Sécurité** : Utilisez des pratiques sécurisées, telles qu'éviter `String` pour les mots de passe (utilisez `char[]`) et intégrer avec des frameworks de sécurité existants.

Ce guide couvre les bases de l'utilisation de `javax.security.auth` pour l'authentification et l'autorisation en Java !