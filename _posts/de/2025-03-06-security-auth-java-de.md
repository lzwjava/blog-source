---
audio: false
generated: true
lang: de
layout: post
title: Authentifizierung und Autorisierung in Java
translated: true
type: note
---

Um das `javax.security.auth`-Paket in Java zu verwenden, müssen Sie verstehen, dass es Teil des Java Authentication and Authorization Service (JAAS)-Frameworks ist. Dieses Paket stellt Klassen und Interfaces zur Authentifizierung von Benutzern (Überprüfung ihrer Identität) und Autorisierung (Bestimmung ihrer Berechtigungen) bereit. Im Folgenden finden Sie eine Schritt-für-Schritt-Anleitung zur Verwendung von `javax.security.auth` für ein grundlegendes Authentifizierungsszenario, wie z. B. die Authentifizierung eines Benutzers mit Benutzername und Passwort.

---

### **Überblick über Schlüsselkonzepte**
Bevor wir zu den Schritten kommen, hier eine kurze Erklärung der Kernkomponenten in `javax.security.auth`:

- **Subject**: Stellt eine Entität dar (z. B. einen Benutzer oder Dienst), die authentifiziert wird. Es kann mehrere Identitäten (Principals) und Anmeldeinformationen (Credentials, z. B. Passwörter oder Zertifikate) haben.
- **Principal**: Eine Identität oder Rolle, die einem Subject zugeordnet ist, wie ein Benutzername oder eine Gruppenmitgliedschaft.
- **Credential**: Informationen, die zur Authentifizierung eines Subjects verwendet werden, wie ein Passwort oder ein kryptografischer Schlüssel.
- **LoginModule**: Eine austauschbare Komponente, die die Authentifizierungslogik ausführt (z. B. Überprüfung eines Benutzernamens und Passworts gegen eine Datenbank).
- **LoginContext**: Die zentrale Klasse, die den Authentifizierungsprozess unter Verwendung eines oder mehrerer LoginModules koordiniert.
- **CallbackHandler**: Ein Interface zur Interaktion mit dem Benutzer, z. B. zur Abfrage von Benutzername und Passwort.

Mit diesen Konzepten im Hinterkopf wollen wir uns ansehen, wie das Paket verwendet wird.

---

### **Schritte zur Verwendung von `javax.security.auth`**

#### **1. Eine JAAS-Konfiguration einrichten**
Der Authentifizierungsprozess basiert auf einer Konfiguration, die angibt, welche `LoginModule(s)` verwendet werden sollen. Diese kann in einer Konfigurationsdatei oder programmatisch definiert werden.

Erstellen Sie beispielsweise eine Datei namens `jaas.config` mit folgendem Inhalt:

```
MyApp {
    com.example.MyLoginModule required;
};
```

- **`MyApp`**: Der Name der Anwendung oder des Kontexts, auf den Sie in Ihrem Code verweisen werden.
- **`com.example.MyLoginModule`**: Der vollständig qualifizierte Name Ihres benutzerdefinierten `LoginModule` (dies werden Sie später implementieren).
- **`required`**: Ein Flag, das angibt, dass dieses Modul erfolgreich sein muss, damit die Authentifizierung bestanden wird. Andere Flags sind `requisite`, `sufficient` und `optional`, die komplexere Logik mit mehreren Modulen ermöglichen.

Setzen Sie die Systemeigenschaft, um auf diese Datei zu verweisen:

```java
System.setProperty("java.security.auth.login.config", "jaas.config");
```

Alternativ können Sie die Konfiguration programmatisch setzen, aber eine Datei ist in den meisten Fällen einfacher.

#### **2. Einen CallbackHandler implementieren**
Ein `CallbackHandler` sammelt Eingaben vom Benutzer, wie z. B. einen Benutzernamen und ein Passwort. Hier ist eine einfache Implementierung unter Verwendung der Konsole:

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

- **NameCallback**: Fordert den Benutzernamen ab und ruft ihn ab.
- **PasswordCallback**: Fordert das Passwort ab und ruft es ab (aus Sicherheitsgründen als `char[]` gespeichert).

#### **3. Ein LoginModule implementieren**
Ein `LoginModule` definiert die Authentifizierungslogik. Im Folgenden finden Sie ein grundlegendes Beispiel, das gegen einen hartkodierten Benutzernamen und ein hartkodiertes Passwort prüft (in der Praxis würden Sie eine Datenbank oder einen externen Dienst verwenden):

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

    // Initialisiert das Modul
    public void initialize(Subject subject, CallbackHandler callbackHandler,
                           Map<String, ?> sharedState, Map<String, ?> options) {
        this.subject = subject;
        this.callbackHandler = callbackHandler;
    }

    // Führt die Authentifizierung durch
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

            // Hartkodierte Prüfung (in der Praxis durch echte Logik ersetzen)
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

    // Commit der Authentifizierung (fügt Principals zum Subject hinzu)
    public boolean commit() throws LoginException {
        if (succeeded) {
            subject.getPrincipals().add(new MyPrincipal("myuser"));
            return true;
        }
        return false;
    }

    // Bricht den Authentifizierungsprozess ab
    public boolean abort() throws LoginException {
        succeeded = false;
        return true;
    }

    // Meldet das Subject ab
    public boolean logout() throws LoginException {
        subject.getPrincipals().clear();
        subject.getPublicCredentials().clear();
        subject.getPrivateCredentials().clear();
        return true;
    }
}

// Einfache Principal-Implementierung
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

- **login()**: Verwendet den `CallbackHandler`, um Anmeldeinformationen zu erhalten und prüft sie.
- **commit()**: Wenn die Authentifizierung erfolgreich ist, wird ein `Principal` zum `Subject` hinzugefügt.
- **abort()** und **logout()**: Behandeln die Bereinigung oder den Abbruch.

#### **4. Authentifizierung mit LoginContext durchführen**
Verwenden Sie nun `LoginContext`, um die Authentifizierung in Ihrer Hauptanwendung durchzuführen:

```java
import javax.security.auth.login.*;
import java.security.Principal;

public class Main {
    public static void main(String[] args) {
        // Sicherstellen, dass die JAAS-Konfiguration gesetzt ist
        System.setProperty("java.security.auth.login.config", "jaas.config");

        try {
            // LoginContext mit dem Konfigurationsnamen und CallbackHandler erstellen
            LoginContext lc = new LoginContext("MyApp", new MyCallbackHandler());

            // Authentifizierung durchführen
            lc.login();

            // Das authentifizierte Subject abrufen
            Subject subject = lc.getSubject();
            System.out.println("Authenticated subject: " + subject);

            // Die Principals des Subjects ausgeben
            for (Principal p : subject.getPrincipals()) {
                System.out.println("Principal: " + p.getName());
            }

            // Abmelden, wenn fertig
            lc.logout();
        } catch (LoginException e) {
            System.err.println("Authentication failed: " + e.getMessage());
        }
    }
}
```

- **`LoginContext lc = new LoginContext("MyApp", new MyCallbackHandler())`**: Verknüpft mit der `"MyApp"`-Konfiguration und verwendet `MyCallbackHandler`.
- **`lc.login()`**: Löst den Authentifizierungsprozess aus.
- **`lc.getSubject()`**: Ruft das authentifizierte `Subject` ab.

#### **5. Autorisierte Aktionen durchführen (Optional)**
Sobald authentifiziert, können Sie das `Subject` verwenden, um Code mit seinen Berechtigungen unter Verwendung von `Subject.doAs()` auszuführen:

```java
import java.security.PrivilegedAction;

Subject.doAs(subject, new PrivilegedAction<Void>() {
    public Void run() {
        System.out.println("Running as: " + Subject.getSubject(java.security.AccessController.getContext()));
        // Führen Sie hier berechtigte Aktionen aus
        return null;
    }
});
```

Dies ist nützlich für die Autorisierung, bei der Aktionen basierend auf den `Principals` des `Subject` eingeschränkt werden.

---

### **Alles zusammengeführt**
1. **Konfiguration**: Definieren Sie `jaas.config` mit Ihrem `LoginModule`.
2. **CallbackHandler**: Implementieren Sie `MyCallbackHandler`, um Benutzereingaben zu sammeln.
3. **LoginModule**: Implementieren Sie `MyLoginModule` mit Ihrer Authentifizierungslogik.
4. **Hauptcode**: Verwenden Sie `LoginContext` zur Authentifizierung und zum Abrufen eines `Subject`.
5. **Autorisierung**: Verwenden Sie bei Bedarf `Subject.doAs()` für berechtigte Aktionen.

Wenn Sie die `Main`-Klasse ausführen, wird sie:
- Nach einem Benutzernamen und Passwort fragen.
- Unter Verwendung von `MyLoginModule` authentifizieren.
- Bei Erfolg das `Subject` und seine `Principals` ausgeben.

---

### **Zusätzliche Hinweise**
- **Echter Einsatz**: Ersetzen Sie die hartkodierten Anmeldeinformationen in `MyLoginModule` durch Prüfungen gegen eine Datenbank, LDAP oder einen anderen Dienst. Java bietet Standardmodule wie `Krb5LoginModule` (Kerberos) oder `JndiLoginModule` (LDAP) an, diese können jedoch zusätzliche Einrichtung erfordern.
- **Mehrere LoginModules**: Die Konfiguration kann mehrere Module mit Flags (`required`, `sufficient`, etc.) angeben, um komplexe Authentifizierungsabläufe zu erstellen.
- **Sicherheit**: Verwenden Sie sichere Praktiken, wie das Vermeiden von `String` für Passwörter (verwenden Sie `char[]`) und die Integration in bestehende Sicherheitsframeworks.

Diese Anleitung behandelt die Grundlagen der Verwendung von `javax.security.auth` für Authentifizierung und Autorisierung in Java!