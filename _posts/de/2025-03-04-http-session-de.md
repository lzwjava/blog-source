---
audio: false
generated: true
lang: de
layout: post
title: HTTP-Sitzungen in Java-Servlets
translated: true
---

Lassen Sie mich Ihre Anfrage bezüglich der Funktionsweise von `HttpSession` im `javax.servlet`-Paket, wie man einen Sessionswert setzt und wie man ihn abruft, beantworten. Ich werde annehmen, dass "HTTPSession" in Ihrer Frage ein Tippfehler ist und dass Sie `HttpSession` meinen, da dies der korrekte Klassenname im `javax.servlet`-Paket ist.

---

### **Wie funktioniert HttpSession?**

`HttpSession` ist eine Schnittstelle im `javax.servlet.http`-Paket, die die Zustandsverwaltung in Java-Webanwendungen ermöglicht. HTTP ist von Natur aus zustandslos – jede Anfrage von einem Client (z. B. einem Browser) an einen Server ist unabhängig und hat keine Erinnerung an vorherige Interaktionen. Um diese Einschränkung zu überwinden und benutzerbezogene Daten über mehrere Anfragen hinweg zu verfolgen (z. B. während eines Benutzerbesuchs auf einer Website), stellt `HttpSession` einen Mechanismus bereit, um eine "Session" aufrechtzuerhalten.

Hier ist, wie es funktioniert:

1. **Sessionserstellung**: Wenn ein Benutzer erstmals auf einen Servlet in einer Webanwendung zugreift, erstellt der Servlet-Container (z. B. Tomcat) ein neues `HttpSession`-Objekt. Diese Session wird eine eindeutige Kennung namens **Session-ID** zugewiesen.

2. **Übertragung der Session-ID**: Die Session-ID wird an den Browser des Clients gesendet, normalerweise als ein Cookie mit dem Namen `JSESSIONID`. Bei nachfolgenden Anfragen fügt der Browser diese Session-ID hinzu, sodass der Server die Anfrage der bestehenden Session zuordnen kann.

3. **Fallback-Mechanismus**: Wenn Cookies im Browser deaktiviert sind, kann der Servlet-Container **URL-Umschreibung** als Fallback verwenden. In diesem Fall wird die Session-ID an URLs angehängt (z. B. `http://example.com/page;jsessionid=abc123`), was jedoch eine explizite Unterstützung im Anwendungscode erfordert.

4. **Serverseitige Speicherung**: Die eigentlichen Sessionsdaten (Attribute) werden auf dem Server gespeichert, nicht auf dem Client. Der Client hält nur die Session-ID, was Sessions sicherer macht als Cookies für die Speicherung sensibler Informationen. Die Daten werden normalerweise im Speicher des Servers gehalten, können aber in erweiterten Konfigurationen auf Festplatte oder in einer Datenbank persistiert werden.

5. **Sessionslebensdauer**: Sessions haben eine Timeout-Periode (z. B. 30 Minuten standardmäßig, konfigurierbar über `web.xml` oder programmgesteuert). Wenn der Benutzer länger als diese Zeit inaktiv ist, läuft die Session ab und ihre Daten werden verworfen. Sie können eine Session auch manuell beenden, z. B. beim Abmelden.

Dieser Mechanismus ermöglicht es dem Server, benutzerbezogene Informationen wie den Anmeldezustand oder den Inhalt eines Einkaufswagens über mehrere Anfragen hinweg "zu erinnern".

---

### **Wie man einen Sessionswert setzt**

Um Daten in einer `HttpSession` zu speichern, verwenden Sie die Methode `setAttribute`. Diese Methode ordnet einen Schlüssel (ein `String`) einem Wert (einem beliebigen Java-Objekt) zu. Hier ist, wie man es macht:

1. **HttpSession-Objekt erhalten**: In einem Servlet erhalten Sie die `HttpSession` aus dem `HttpServletRequest`-Objekt mit `request.getSession()`. Diese Methode erstellt eine neue Session, wenn keine existiert, oder gibt die bestehende Session zurück.

2. **Attribut setzen**: Rufen Sie `setAttribute(key, value)` auf dem `HttpSession`-Objekt auf.

Hier ist ein Beispiel in einem Servlet:

```java
import javax.servlet.http.*;
import java.io.*;

public class SetSessionServlet extends HttpServlet {
    public void doGet(HttpServletRequest request, HttpServletResponse response)
            throws IOException {
        // Session erhalten (erstellt eine neue, falls keine existiert)
        HttpSession session = request.getSession();

        // Ein Sessionsattribut setzen
        session.setAttribute("username", "Alice");

        // Antwort an den Client
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        out.println("Sessionswert gesetzt: username = Alice");
    }
}
```

In diesem Code:
- `request.getSession()` stellt sicher, dass eine Session verfügbar ist.
- `session.setAttribute("username", "Alice")` speichert die Zeichenkette `"Alice"` unter dem Schlüssel `"username"`.

---

### **Wie man einen Sessionswert abruft**

Um einen Wert aus der Session abzurufen, verwenden Sie die Methode `getAttribute`. Da sie ein `Object` zurückgibt, müssen Sie es in den entsprechenden Typ umwandeln. Hier ist der Prozess:

1. **HttpSession-Objekt erhalten**: Verwenden Sie `request.getSession()` oder `request.getSession(false)` (der Letztere gibt `null` zurück, wenn keine Session existiert, und vermeidet die Erstellung einer neuen).

2. **Attribut abrufen**: Rufen Sie `getAttribute(key)` auf und wandeln Sie das Ergebnis um.

Hier ist ein Beispiel:

```java
import javax.servlet.http.*;
import java.io.*;

public class GetSessionServlet extends HttpServlet {
    public void doGet(HttpServletRequest request, HttpServletResponse response)
            throws IOException {
        // Session erhalten (gibt null zurück, wenn keine Session existiert)
        HttpSession session = request.getSession(false);

        response.setContentType("text/html");
        PrintWriter out = response.getWriter();

        if (session != null) {
            // Sessionsattribut abrufen
            String username = (String) session.getAttribute("username");

            if (username != null) {
                out.println("Sessionswert abgerufen: username = " + username);
            } else {
                out.println("Kein Benutzername in der Session gefunden.");
            }
        } else {
            out.println("Keine aktive Session.");
        }
    }
}
```

In diesem Code:
- `request.getSession(false)` ruft die bestehende Session ab oder gibt `null` zurück.
- `session.getAttribute("username")` holt den Wert, der in `String` umgewandelt wird.
- Null-Überprüfungen verhindern Fehler, falls die Session oder das Attribut nicht existiert.

---

### **Praktisches Beispiel**

Hier ist ein kombiniertes Beispiel, das das Setzen und Abrufen eines Sessionswerts über Anfragen zeigt:

1. **SetSessionServlet.java** (z. B. für die Anmeldung):
```java
import javax.servlet.http.*;
import java.io.*;

public class SetSessionServlet extends HttpServlet {
    public void doGet(HttpServletRequest request, HttpServletResponse response)
            throws IOException {
        HttpSession session = request.getSession();
        session.setAttribute("user", "Bob");

        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        out.println("Benutzer in der Session gesetzt: Bob");
    }
}
```

2. **GetSessionServlet.java** (z. B. für eine geschützte Seite):
```java
import javax.servlet.http.*;
import java.io.*;

public class GetSessionServlet extends HttpServlet {
    public void doGet(HttpServletRequest request, HttpServletResponse response)
            throws IOException {
        HttpSession session = request.getSession(false);

        response.setContentType("text/html");
        PrintWriter out = response.getWriter();

        if (session != null && session.getAttribute("user") != null) {
            String user = (String) session.getAttribute("user");
            out.println("Willkommen zurück, " + user);
        } else {
            out.println("Bitte melden Sie sich zuerst an.");
        }
    }
}
```

Wenn ein Client auf `SetSessionServlet` zugreift, speichert die Session `"Bob"`. Später, wenn `GetSessionServlet` aufgerufen wird, wird es abgerufen und angezeigt, da die Session über Anfragen hinweg besteht.

---

### **Zusätzliche Hinweise**

- **Session-Timeout**: Setzen Sie dies über `session.setMaxInactiveInterval(seconds)` (z. B. `session.setMaxInactiveInterval(1800)` für 30 Minuten) oder in `web.xml`:
  ```xml
  <session-config>
      <session-timeout>30</session-timeout> <!-- in Minuten -->
  </session-config>
  ```
- **Beenden einer Session**: Verwenden Sie `session.invalidate()` (z. B. für das Abmelden).
- **Sicherheit**: Verwenden Sie HTTPS, um die Session-ID vor Abfangen zu schützen. Vermeiden Sie das Speichern hochsensibler Daten ohne Verschlüsselung.
- **Typumwandlung**: Wandeln Sie immer das Ergebnis von `getAttribute` um, da es `Object` zurückgibt.

---

### **Zusammenfassung**

- **Wie es funktioniert**: `HttpSession` hält den Benutzerzustand mit einer Session-ID (über Cookies oder URL-Umschreibung) und speichert Daten auf dem Server.
- **Wert setzen**: `session.setAttribute("key", value)`.
- **Wert abrufen**: `String value = (String) session.getAttribute("key")`.

Das sollte Ihnen ein klares Verständnis von `HttpSession` in `javax.servlet` geben. Lassen Sie mich wissen, wenn Sie weitere Klarstellungen benötigen!