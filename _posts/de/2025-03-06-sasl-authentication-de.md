---
audio: false
generated: true
lang: de
layout: post
title: SASL-Authentifizierung in Java
translated: true
type: note
---

Um das `javax.security.sasl`-Paket in Java zu verwenden, müssen Sie seine Klassen und Schnittstellen nutzen, um Simple Authentication and Security Layer (SASL)-Mechanismen für die Authentifizierung und optional für Datensicherheit in Client-Server-Anwendungen zu implementieren. Die Hauptklassen sind `Sasl`, `SaslClient` und `SaslServer`. Nachfolgend finden Sie eine umfassende Anleitung zur Verwendung dieses Pakets, einschließlich Schritten und Beispielcode für Client- und Server-Implementierungen.

---

### **Überblick über javax.security.sasl**
Das `javax.security.sasl`-Paket bietet einen Rahmen für die SASL-Authentifizierung, die häufig in Protokollen wie LDAP, IMAP oder benutzerdefinierten Anwendungen verwendet wird. Es beinhaltet:
- **`Sasl`**: Eine Utility-Klasse mit statischen Methoden zum Erstellen von `SaslClient`- und `SaslServer`-Instanzen.
- **`SaslClient`**: Stellt die Client-Seite des SASL-Authentifizierungsprozesses dar.
- **`SaslServer`**: Stellt die Server-Seite des SASL-Authentifizierungsprozesses dar.
- **`CallbackHandler`**: Eine Schnittstelle, die Sie implementieren, um Authentifizierungs-Callbacks zu behandeln (z.B. zur Bereitstellung von Benutzernamen oder Passwörtern).

Der Prozess umfasst das Erstellen eines `SaslClient` oder `SaslServer`, das Bereitstellen eines Callback-Handlers zur Verwaltung von Authentifizierungsdaten und den Austausch von Challenge-Response, bis die Authentifizierung abgeschlossen ist.

---

### **Schritte zur Verwendung von javax.security.sasl**

#### **1. Bestimmen Sie Ihre Rolle (Client oder Server)**
Entscheiden Sie, ob Ihre Anwendung als Client (authentifiziert sich bei einem Server) oder als Server (authentifiziert einen Client) agiert. Dies bestimmt, ob Sie `SaslClient` oder `SaslServer` verwenden.

#### **2. Wählen Sie einen SASL-Mechanismus**
SASL unterstützt verschiedene Mechanismen, wie z.B.:
- `PLAIN`: Einfache Benutzername/Passwort-Authentifizierung (keine Verschlüsselung).
- `DIGEST-MD5`: Passwortbasiert mit Challenge-Response.
- `GSSAPI`: Kerberos-basierte Authentifizierung.

Wählen Sie einen Mechanismus, der sowohl vom Client als auch vom Server unterstützt wird. Der Einfachheit halber wird in dieser Anleitung der `PLAIN`-Mechanismus als Beispiel verwendet.

#### **3. Implementieren Sie einen CallbackHandler**
Ein `CallbackHandler` ist erforderlich, um Authentifizierungsanmeldedaten bereitzustellen oder zu überprüfen. Sie müssen die Schnittstelle `javax.security.auth.callback.CallbackHandler` implementieren.

- **Für einen Client**: Stellen Sie Anmeldedaten wie Benutzername und Passwort bereit.
- **Für einen Server**: Überprüfen Sie Client-Anmeldedaten oder stellen Sie serverseitige Authentifizierungsdaten bereit.

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

Für den Server könnten Sie Anmeldedaten gegen eine Datenbank überprüfen:

```java
public class ServerCallbackHandler implements CallbackHandler {
    @Override
    public void handle(Callback[] callbacks) throws IOException, UnsupportedCallbackException {
        for (Callback callback : callbacks) {
            if (callback instanceof NameCallback) {
                String username = ((NameCallback) callback).getName();
                // Erwartetes Passwort für Benutzernamen aus einer Datenbank abrufen
            } else if (callback instanceof PasswordCallback) {
                // Setze das erwartete Passwort zur Überprüfung
                ((PasswordCallback) callback).setPassword("expectedPassword".toCharArray());
            } else if (callback instanceof AuthorizeCallback) {
                AuthorizeCallback ac = (AuthorizeCallback) callback;
                ac.setAuthorized(ac.getAuthenticationID().equals(ac.getAuthorizationID()));
            }
        }
    }
}
```

#### **4. Client-Seitige Implementierung**
So authentifizieren Sie sich als Client:

1. **Erstellen Sie einen SaslClient**:
   Verwenden Sie `Sasl.createSaslClient` mit dem Mechanismus, Protokoll, Servernamen, Eigenschaften und dem Callback-Handler.

   ```java
   import javax.security.sasl.Sasl;
   import javax.security.sasl.SaslClient;
   import java.util.HashMap;

   String[] mechanisms = {"PLAIN"};
   String authorizationId = null; // Optional; null, falls identisch mit Authentication ID
   String protocol = "ldap"; // z.B. "ldap", "imap"
   String serverName = "myserver.example.com";
   HashMap<String, Object> props = null; // Optionale Eigenschaften, z.B. QoP
   CallbackHandler cbh = new ClientCallbackHandler("user", "pass");

   SaslClient sc = Sasl.createSaslClient(mechanisms, authorizationId, protocol, serverName, props, cbh);
   ```

2. **Behandeln Sie den Challenge-Response-Austausch**:
   - Prüfen Sie auf eine initiale Antwort (üblich bei client-initiierten Mechanismen wie `PLAIN`).
   - Senden Sie Antworten an den Server und verarbeiten Sie Challenges, bis die Authentifizierung abgeschlossen ist.

   ```java
   byte[] response = sc.hasInitialResponse() ? sc.evaluateChallenge(new byte[0]) : null;
   if (response != null) {
       // Sende Antwort an Server (protokollspezifisch, z.B. via Socket oder LDAP BindRequest)
   }

   // Empfange Server-Challenge (protokollspezifisch)
   byte[] challenge = /* vom Server lesen */;
   while (!sc.isComplete()) {
       response = sc.evaluateChallenge(challenge);
       // Sende Antwort an Server
       if (sc.isComplete()) break;
       challenge = /* lese nächste Challenge vom Server */;
   }

   // Authentifizierung ist abgeschlossen; Erfolg protokollspezifisch prüfen
   ```

   Bei `PLAIN` sendet der Client die Anmeldedaten in der initialen Antwort, und der Server antwortet typischerweise mit Erfolg oder Misserfolg ohne weitere Challenges.

#### **5. Server-Seitige Implementierung**
So authentifizieren Sie einen Client als Server:

1. **Erstellen Sie einen SaslServer**:
   Verwenden Sie `Sasl.createSaslServer` mit dem Mechanismus, Protokoll, Servernamen, Eigenschaften und dem Callback-Handler.

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

2. **Behandeln Sie den Challenge-Response-Austausch**:
   - Verarbeiten Sie die initiale Antwort des Clients und generieren Sie Challenges, bis die Authentifizierung abgeschlossen ist.

   ```java
   byte[] response = /* initiale Antwort vom Client lesen */;
   byte[] challenge = ss.evaluateResponse(response != null ? response : new byte[0]);
   // Sende Challenge an Client (protokollspezifisch)

   while (!ss.isComplete()) {
       response = /* lese nächste Antwort vom Client */;
       challenge = ss.evaluateResponse(response);
       if (ss.isComplete()) {
           // Authentifizierung abgeschlossen
           break;
       }
       // Sende Challenge an Client
   }

   if (ss.isComplete()) {
       String authorizedUser = ss.getAuthorizationID();
       // Fahre mit autorisiertem Benutzer fort
   }
   ```

   Bei `PLAIN` überprüft der Server die Anmeldedaten in der initialen Antwort und schließt die Authentifizierung ohne zusätzliche Challenges ab.

#### **6. Optional: Verwenden Sie Sicherheitsebenen**
Falls der Mechanismus (z.B. `DIGEST-MD5`) eine Sicherheitsebene unterstützt:
- Verwenden Sie `sc.wrap()` und `sc.unwrap()` auf dem Client oder `ss.wrap()` und `ss.unwrap()` auf dem Server, um Nachrichten nach der Authentifizierung zu verschlüsseln/entschlüsseln.
- `PLAIN` unterstützt keine Sicherheitsebenen.

---

### **Wichtige Punkte**
- **Integration**: Betten Sie den SASL-Austausch in das Kommunikationsprotokoll Ihrer Anwendung ein (z.B. LDAP Bind requests, IMAP AUTHENTICATE commands).
- **Fehlerbehandlung**: Umschließen Sie den Code mit try-catch-Blöcken, um `SaslException` und andere potenzielle Fehler zu behandeln.
- **Eigenschaften**: Verwenden Sie die `props`-Map, um Optionen wie Quality of Protection (`"javax.security.sasl.qop"`) zu konfigurieren, sofern dies vom Mechanismus unterstützt wird.

---

### **Beispiel-Anwendungsfall**
Für einen LDAP-Client, der sich mit `PLAIN` authentifiziert:
1. Erstellen Sie einen `SaslClient` mit dem `PLAIN`-Mechanismus.
2. Senden Sie eine LDAP `BindRequest` mit dem Mechanismus und der initialen Antwort (`sc.evaluateChallenge(new byte[0])`).
3. Verarbeiten Sie die `BindResponse` des Servers, um den Erfolg zu bestätigen.

Für ein benutzerdefiniertes Protokoll ersetzen Sie die LDAP-spezifischen Schritte durch die Authentifizierungsbefehle Ihres Protokolls.

---

Indem Sie diese Schritte befolgen, können Sie `javax.security.sasl` effektiv verwenden, um SASL-Authentifizierung in Ihrer Java-Anwendung zu implementieren und den Prozess an Ihren gewählten Mechanismus und Ihr Protokoll anzupassen.