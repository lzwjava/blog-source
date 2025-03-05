---
audio: false
generated: true
lang: de
layout: post
title: Authentifizierung und Autorisierung in Java
translated: true
---

Um das `javax.security.auth`-Paket in Java zu verwenden, müssen Sie verstehen, dass es Teil des Java Authentication and Authorization Service (JAAS)-Frameworks ist. Dieses Paket stellt Klassen und Schnittstellen zur Authentifizierung von Benutzern (Überprüfung, wer sie sind) und zur Autorisierung (Bestimmung, was sie tun können) bereit. Im Folgenden finden Sie eine Schritt-für-Schritt-Anleitung zur Verwendung von `javax.security.auth` für ein grundlegendes Authentifizierungsszenario, wie z.B. die Authentifizierung eines Benutzers mit einem Benutzernamen und einem Passwort.

---

### **Übersicht der Schlüsselkonzepte**
Bevor wir zu den Schritten übergehen, hier eine kurze Erklärung der Kernkomponenten in `javax.security.auth`:

- **Subject**: Stellt eine Entität (z.B. einen Benutzer oder einen Dienst) dar, die authentifiziert wird. Es kann mehrere Identitäten (Principals) und Anmeldeinformationen (z.B. Passwörter oder Zertifikate) haben.
- **Principal**: Eine Identität oder Rolle, die einem Subject zugeordnet ist, wie z.B. ein Benutzername oder eine Gruppenmitgliedschaft.
- **Credential**: Informationen, die zur Authentifizierung eines Subjects verwendet werden, wie z.B. ein Passwort oder ein kryptografischer Schlüssel.
- **LoginModule**: Eine Plug-in-Komponente, die die Authentifizierungslogik durchführt (z.B. Überprüfung eines Benutzernamens und Passworts in einer Datenbank).
- **LoginContext**: Die zentrale Klasse, die den Authentifizierungsprozess mit einem oder mehreren LoginModules koordiniert.
- **CallbackHandler**: Eine Schnittstelle zur Interaktion mit dem Benutzer, wie z.B. das Auffordern eines Benutzernamens und Passworts.

Mit diesen Konzepten im Hinterkopf, erkunden wir, wie man das Paket verwendet.

---

### **Schritte zur Verwendung von `javax.security.auth`**

#### **1. Einrichten einer JAAS-Konfiguration**
Der Authentifizierungsprozess basiert auf einer Konfiguration, die angibt, welche `LoginModule`(s) verwendet werden sollen. Dies kann in einer Konfigurationsdatei oder programmgesteuert definiert werden.

Erstellen Sie beispielsweise eine Datei mit dem Namen `jaas.config` mit folgendem Inhalt:

```
MyApp {
    com.example.MyLoginModule required;
};
```

- **`MyApp`**: Der Name der Anwendung oder des Kontexts, auf den Sie in Ihrem Code verweisen werden.
- **`com.example.MyLoginModule`**: Der vollständige qualifizierte Name Ihres benutzerdefinierten `LoginModule` (Sie implementieren dies später).
- **`required`**: Ein Flag, das angibt, dass dieses Modul erfolgreich sein muss, damit die Authentifizierung erfolgreich ist. Weitere Flags sind `requisite`, `sufficient` und `optional`, die komplexere Logik mit mehreren Modulen ermöglichen.

Setzen Sie die Systemeigenschaft, um auf diese Datei zu verweisen:

```java
System.setProperty("java.security.auth.login.config", "jaas.config");
```

Alternativ können Sie die Konfiguration programmgesteuert setzen, aber eine Datei ist für die meisten Fälle einfacher.

#### **2. Implementieren eines CallbackHandlers**
Ein `CallbackHandler` sammelt Eingaben vom Benutzer, wie z.B. einen Benutzernamen und ein Passwort. Hier ist eine einfache Implementierung unter Verwendung der Konsole:

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

- **NameCallback**: Fordert und erhält den Benutzernamen an.
- **PasswordCallback**: Fordert und erhält das Passwort (als `char[]` für die Sicherheit gespeichert).

#### **3. Implementieren eines LoginModules**
Ein `LoginModule` definiert die Authentifizierungslogik. Hier ist ein grundlegendes Beispiel, das gegen einen hartcodierten Benutzernamen und ein Passwort überprüft (in der Praxis würden Sie eine Datenbank oder einen externen Dienst verwenden):

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

    // Initialisieren Sie das Modul
    public void initialize(Subject subject, CallbackHandler callbackHandler,
                           Map<String, ?> sharedState, Map<String, ?> options) {
        this.subject = subject;
        this.callbackHandler = callbackHandler;
    }

    // Authentifizierung durchführen
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

            // Hartcodierte Überprüfung (ersetzen Sie durch echte Logik in der Praxis)
            if ("myuser".equals(username) && "mypassword".equals(new String(password))) {
                succeeded = true;
                return true;
            } else {
                succeeded = false;
                throw new FailedLoginException("Authentifizierung fehlgeschlagen");
            }
        } catch (Exception e) {
            throw new LoginException("Login-Fehler: " + e.getMessage());
        }
    }

    // Authentifizierung bestätigen (Principals zum Subject hinzufügen)
    public boolean commit() throws LoginException {
        if (succeeded) {
            subject.getPrincipals().add(new MyPrincipal("myuser"));
            return true;
        }
        return false;
    }

    // Authentifizierungsprozess abbrechen
    public boolean abort() throws LoginException {
        succeeded = false;
        return true;
    }

    // Subject abmelden
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

- **login()**: Verwendet den `CallbackHandler`, um Anmeldeinformationen zu erhalten und überprüft sie.
- **commit()**: Wenn die Authentifizierung erfolgreich ist, fügt ein `Principal` zum `Subject` hinzu.
- **abort()** und **logout()**: Behandeln die Bereinigung oder Abbruch.

#### **4. Authentifizieren mit LoginContext**
Verwenden Sie nun `LoginContext`, um die Authentifizierung in Ihrer Hauptanwendung durchzuführen:

```java
import javax.security.auth.login.*;
import java.security.Principal;

public class Main {
    public static void main(String[] args) {
        // Stellen Sie sicher, dass die JAAS-Konfiguration gesetzt ist
        System.setProperty("java.security.auth.login.config", "jaas.config");

        try {
            // Erstellen Sie LoginContext mit dem Konfigurationsnamen und CallbackHandler
            LoginContext lc = new LoginContext("MyApp", new MyCallbackHandler());

            // Authentifizierung durchführen
            lc.login();

            // Erhalten Sie das authentifizierte Subject
            Subject subject = lc.getSubject();
            System.out.println("Authentifiziertes Subject: " + subject);

            // Drucken Sie die Principals des Subjects
            for (Principal p : subject.getPrincipals()) {
                System.out.println("Principal: " + p.getName());
            }

            // Melden Sie sich ab, wenn Sie fertig sind
            lc.logout();
        } catch (LoginException e) {
            System.err.println("Authentifizierung fehlgeschlagen: " + e.getMessage());
        }
    }
}
```

- **`LoginContext lc = new LoginContext("MyApp", new MyCallbackHandler())`**: Verknüpft mit der `"MyApp"`-Konfiguration und verwendet `MyCallbackHandler`.
- **`lc.login()`**: Löst den Authentifizierungsprozess aus.
- **`lc.getSubject()`**: Ruft das authentifizierte `Subject` ab.

#### **5. Durchführen autorisierter Aktionen (optional)**
Nach der Authentifizierung können Sie das `Subject` verwenden, um Code mit seinen Berechtigungen auszuführen, indem Sie `Subject.doAs()` verwenden:

```java
import java.security.PrivilegedAction;

Subject.doAs(subject, new PrivilegedAction<Void>() {
    public Void run() {
        System.out.println("Ausführen als: " + Subject.getSubject(java.security.AccessController.getContext()));
        // Führen Sie hier privilegierte Aktionen aus
        return null;
    }
});
```

Dies ist nützlich für die Autorisierung, bei der Aktionen basierend auf den `Principals` des `Subject` eingeschränkt werden.

---

### **Alles zusammenfassen**
1. **Konfiguration**: Definieren Sie `jaas.config` mit Ihrem `LoginModule`.
2. **CallbackHandler**: Implementieren Sie `MyCallbackHandler`, um Benutzereingaben zu sammeln.
3. **LoginModule**: Implementieren Sie `MyLoginModule` mit Ihrer Authentifizierungslogik.
4. **Hauptcode**: Verwenden Sie `LoginContext`, um zu authentifizieren und ein `Subject` abzurufen.
5. **Autorisierung**: Verwenden Sie `Subject.doAs()` für privilegierte Aktionen, falls erforderlich.

Wenn Sie die `Main`-Klasse ausführen, wird sie:
- Nach einem Benutzernamen und Passwort fragen.
- Authentifizierung mit `MyLoginModule` durchführen.
- Das `Subject` und seine `Principals` drucken, wenn erfolgreich.

---

### **Zusätzliche Hinweise**
- **Einsatz in der Praxis**: Ersetzen Sie die hartcodierten Anmeldeinformationen in `MyLoginModule` durch Überprüfungen gegen eine Datenbank, LDAP oder einen anderen Dienst. Java bietet Standardmodule wie `Krb5LoginModule` (Kerberos) oder `JndiLoginModule` (LDAP), diese erfordern jedoch möglicherweise zusätzliche Einstellungen.
- **Mehrere LoginModules**: Die Konfiguration kann mehrere Module mit Flags (`required`, `sufficient` usw.) angeben, um komplexe Authentifizierungsabläufe zu erstellen.
- **Sicherheit**: Verwenden Sie sichere Praktiken, wie das Vermeiden von `String` für Passwörter (verwenden Sie `char[]`) und die Integration in bestehende Sicherheitsframeworks.

Diese Anleitung deckt die Grundlagen der Verwendung von `javax.security.auth` für Authentifizierung und Autorisierung in Java ab!