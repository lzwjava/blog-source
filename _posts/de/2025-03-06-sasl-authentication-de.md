---
audio: false
generated: true
lang: de
layout: post
title: SASL-Authentifizierung in Java
translated: true
---

Um das `javax.security.sasl`-Paket in Java zu verwenden, müssen Sie seine Klassen und Schnittstellen nutzen, um Mechanismen der Simple Authentication and Security Layer (SASL) für die Authentifizierung und optional für die Datensicherheit in Client-Server-Anwendungen zu implementieren. Die wichtigsten Klassen sind `Sasl`, `SaslClient` und `SaslServer`. Im Folgenden finden Sie eine umfassende Anleitung zur Verwendung dieses Pakets, einschließlich Schritte und Beispielcode für sowohl Client- als auch Server-Implementierungen.

---

### **Übersicht über javax.security.sasl**
Das `javax.security.sasl`-Paket bietet einen Rahmen für die SASL-Authentifizierung, die häufig in Protokollen wie LDAP, IMAP oder benutzerdefinierten Anwendungen verwendet wird. Es enthält:
- **`Sasl`**: Eine Hilfsklasse mit statischen Methoden zur Erstellung von `SaslClient`- und `SaslServer`-Instanzen.
- **`SaslClient`**: Repräsentiert die Client-Seite des SASL-Authentifizierungsprozesses.
- **`SaslServer`**: Repräsentiert die Server-Seite des SASL-Authentifizierungsprozesses.
- **`CallbackHandler`**: Eine Schnittstelle, die Sie implementieren, um Authentifizierungs-Callbacks zu verarbeiten (z. B. Benutzernamen oder Passwörter bereitstellen).

Der Prozess umfasst die Erstellung eines `SaslClient` oder `SaslServer`, die Bereitstellung eines Callback-Handlers zur Verwaltung der Authentifizierungsdaten und die Durchführung eines Challenge-Response-Austauschs, bis die Authentifizierung abgeschlossen ist.

---

### **Schritte zur Verwendung von javax.security.sasl**

#### **1. Bestimmen Sie Ihre Rolle (Client oder Server)**
Entscheiden Sie, ob Ihre Anwendung als Client (Authentifizierung bei einem Server) oder als Server (Authentifizierung eines Clients) agiert. Dies bestimmt, ob Sie `SaslClient` oder `SaslServer` verwenden.

#### **2. Wählen Sie einen SASL-Mechanismus**
SASL unterstützt verschiedene Mechanismen, wie z. B.:
- `PLAIN`: Einfache Benutzername/Passwort-Authentifizierung (keine Verschlüsselung).
- `DIGEST-MD5`: Passwortbasiert mit Challenge-Response.
- `GSSAPI`: Kerberos-basierte Authentifizierung.

Wählen Sie einen Mechanismus, der sowohl vom Client als auch vom Server unterstützt wird. Aus Gründen der Einfachheit verwendet diese Anleitung den `PLAIN`-Mechanismus als Beispiel.

#### **3. Implementieren Sie einen CallbackHandler**
Ein `CallbackHandler` ist erforderlich, um Authentifizierungsanmeldeinformationen bereitzustellen oder zu überprüfen. Sie müssen die `javax.security.auth.callback.CallbackHandler`-Schnittstelle implementieren.

- **Für einen Client**: Stellen Sie Anmeldeinformationen wie Benutzername und Passwort bereit.
- **Für einen Server**: Überprüfen Sie die Client-Anmeldeinformationen oder stellen Sie serverseitige Authentifizierungsdaten bereit.

Hier ist ein Beispiel für einen clientseitigen `CallbackHandler` für den `PLAIN`-Mechanismus:

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
                throw new UnsupportedCallbackException(callback, "Unsupported callback");
            }
        }
    }
}
```

Für den Server könnten Sie Anmeldeinformationen gegen eine Datenbank überprüfen:

```java
public class ServerCallbackHandler implements CallbackHandler {
    @Override
    public void handle(Callback[] callbacks) throws IOException, UnsupportedCallbackException {
        for (Callback callback : callbacks) {
            if (callback instanceof NameCallback) {
                String username = ((NameCallback) callback).getName();
                // Rufen Sie das erwartete Passwort für den Benutzernamen aus einer Datenbank ab
            } else if (callback instanceof PasswordCallback) {
                // Setzen Sie das erwartete Passwort zur Überprüfung
                ((PasswordCallback) callback).setPassword("expectedPassword".toCharArray());
            } else if (callback instanceof AuthorizeCallback) {
                AuthorizeCallback ac = (AuthorizeCallback) callback;
                ac.setAuthorized(ac.getAuthenticationID().equals(ac.getAuthorizationID()));
            }
        }
    }
}
```

#### **4. Clientseitige Implementierung**
Um sich als Client zu authentifizieren:

1. **Erstellen Sie einen SaslClient**:
   Verwenden Sie `Sasl.createSaslClient` mit dem Mechanismus, dem Protokoll, dem Servernamen, den Eigenschaften und dem Callback-Handler.

   ```java
   import javax.security.sasl.Sasl;
   import javax.security.sasl.SaslClient;
   import java.util.HashMap;

   String[] mechanisms = {"PLAIN"};
   String authorizationId = null; // Optional; null, wenn gleich wie die Authentifizierungs-ID
   String protocol = "ldap"; // z. B. "ldap", "imap"
   String serverName = "myserver.example.com";
   HashMap<String, Object> props = null; // Optionale Eigenschaften, z. B. QoP
   CallbackHandler cbh = new ClientCallbackHandler("user", "pass");

   SaslClient sc = Sasl.createSaslClient(mechanisms, authorizationId, protocol, serverName, props, cbh);
   ```

2. **Verarbeiten Sie den Challenge-Response-Austausch**:
   - Überprüfen Sie auf eine initiale Antwort (häufig bei client-first-Mechanismen wie `PLAIN`).
   - Senden Sie Antworten an den Server und verarbeiten Sie Challenges, bis die Authentifizierung abgeschlossen ist.

   ```java
   byte[] response = sc.hasInitialResponse() ? sc.evaluateChallenge(new byte[0]) : null;
   if (response != null) {
       // Senden Sie die Antwort an den Server (protokollspezifisch, z. B. über Socket oder LDAP BindRequest)
   }

   // Empfangen Sie die Server-Challenge (protokollspezifisch)
   byte[] challenge = /* vom Server lesen */;
   while (!sc.isComplete()) {
       response = sc.evaluateChallenge(challenge);
       // Senden Sie die Antwort an den Server
       if (sc.isComplete()) break;
       challenge = /* nächste Challenge vom Server lesen */;
   }

   // Die Authentifizierung ist abgeschlossen; überprüfen Sie den Erfolg über protokollspezifische Mittel
   ```

   Für `PLAIN` sendet der Client die Anmeldeinformationen in der initialen Antwort, und der Server antwortet in der Regel mit Erfolg oder Fehlschlag ohne weitere Challenges.

#### **5. Serverseitige Implementierung**
Um einen Client als Server zu authentifizieren:

1. **Erstellen Sie einen SaslServer**:
   Verwenden Sie `Sasl.createSaslServer` mit dem Mechanismus, dem Protokoll, dem Servernamen, den Eigenschaften und dem Callback-Handler.

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

2. **Verarbeiten Sie den Challenge-Response-Austausch**:
   - Verarbeiten Sie die initiale Antwort des Clients und generieren Sie Challenges, bis die Authentifizierung abgeschlossen ist.

   ```java
   byte[] response = /* initiale Antwort vom Client lesen */;
   byte[] challenge = ss.evaluateResponse(response != null ? response : new byte[0]);
   // Senden Sie die Challenge an den Client (protokollspezifisch)

   while (!ss.isComplete()) {
       response = /* nächste Antwort vom Client lesen */;
       challenge = ss.evaluateResponse(response);
       if (ss.isComplete()) {
           // Authentifizierung abgeschlossen
           break;
       }
       // Senden Sie die Challenge an den Client
   }

   if (ss.isComplete()) {
       String authorizedUser = ss.getAuthorizationID();
       // Fortfahren mit dem autorisierten Benutzer
   }
   ```

   Für `PLAIN` überprüft der Server die Anmeldeinformationen in der initialen Antwort und schließt die Authentifizierung ohne zusätzliche Challenges ab.

#### **6. Optional: Verwenden Sie Sicherheitslagen**
Wenn der Mechanismus (z. B. `DIGEST-MD5`) eine Sicherheitslage unterstützt:
- Verwenden Sie `sc.wrap()` und `sc.unwrap()` auf der Client-Seite oder `ss.wrap()` und `ss.unwrap()` auf der Server-Seite, um Nachrichten nach der Authentifizierung zu verschlüsseln/entschlüsseln.
- `PLAIN` unterstützt keine Sicherheitslagen.

---

### **Wichtige Punkte**
- **Integration**: Integrieren Sie den SASL-Austausch in das Kommunikationsprotokoll Ihrer Anwendung (z. B. LDAP Bind-Anfragen, IMAP AUTHENTICATE-Befehle).
- **Fehlerbehandlung**: Umfassen Sie den Code in try-catch-Blöcke, um `SaslException` und andere potenzielle Fehler zu behandeln.
- **Eigenschaften**: Verwenden Sie die `props`-Map, um Optionen wie die Qualität des Schutzes (`"javax.security.sasl.qop"`) zu konfigurieren, falls sie vom Mechanismus unterstützt werden.

---

### **Beispielanwendung**
Für einen LDAP-Client, der sich mit `PLAIN` authentifiziert:
1. Erstellen Sie einen `SaslClient` mit dem `PLAIN`-Mechanismus.
2. Senden Sie eine LDAP `BindRequest` mit dem Mechanismus und der initialen Antwort (`sc.evaluateChallenge(new byte[0])`).
3. Verarbeiten Sie die `BindResponse` des Servers, um den Erfolg zu bestätigen.

Für ein benutzerdefiniertes Protokoll ersetzen Sie die LDAP-spezifischen Schritte durch die Authentifizierungsbefehle Ihres Protokolls.

---

Durch die Befolgung dieser Schritte können Sie `javax.security.sasl` effektiv verwenden, um SASL-Authentifizierung in Ihrer Java-Anwendung zu implementieren und den Prozess an Ihren gewählten Mechanismus und Ihr Protokoll anzupassen.