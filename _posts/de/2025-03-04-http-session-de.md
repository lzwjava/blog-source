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

`HttpSession` ist eine Schnittstelle im `javax.servlet.http`-Paket, die die Zustandsverwaltung in Java-Webanwendungen ermöglicht. HTTP ist von Natur aus zustandslos – jede Anfrage von einem Client (z. B. einem Browser) an einen Server ist unabhängig und hat keine Erinnerung an vorherige Interaktionen. Um diese Einschränkung zu überwinden und benutzerbezogene Daten über mehrere Anfragen hinweg zu verfolgen (z. B. während eines Benutzerbesuchs auf einer Website), stellt `HttpSession` einen Mechanismus zur Verfügung, um eine "Sitzung" aufrechtzuerhalten.

Hier ist, wie es funktioniert:

1. **Sitzungserstellung**: Wenn ein Benutzer erstmals auf einen Servlet in einer Webanwendung zugreift, erstellt der Servlet-Container (z. B. Tomcat) ein neues `HttpSession`-Objekt. Diese Sitzung wird eine eindeutige Kennung namens **Sitzungs-ID** zugewiesen.

2. **Übertragung der Sitzungs-ID**: Die Sitzungs-ID wird an den Browser des Clients gesendet, normalerweise als ein Cookie mit dem Namen `JSESSIONID`. Bei nachfolgenden Anfragen fügt der Browser diese Sitzungs-ID hinzu, sodass der Server die Anfrage der bestehenden Sitzung zuordnen kann.

3. **Fallback-Mechanismus**: Wenn Cookies im Browser deaktiviert sind, kann der Servlet-Container **URL-Umschreibung** als Fallback verwenden. In diesem Fall wird die Sitzungs-ID an URLs angehängt (z. B. `http://example.com/page;jsessionid=abc123`), was jedoch eine explizite Unterstützung im Anwendungscode erfordert.

4. **Serverseitige Speicherung**: Die tatsächlichen Sitzungsdaten (Attribute) werden auf dem Server gespeichert, nicht auf dem Client. Der Client hält nur die Sitzungs-ID, was Sitzungen sicherer macht als Cookies für die Speicherung sensibler Informationen. Die Daten werden normalerweise im Speicher des Servers gehalten, können aber in fortgeschrittenen Konfigurationen auf Festplatte oder in einer Datenbank persistiert werden.

5. **Sitzungslebensdauer**: Sitzungen haben eine Timeout-Periode (z. B. 30 Minuten standardmäßig, konfigurierbar über `web.xml` oder programmgesteuert). Wenn der Benutzer länger als diese Zeit inaktiv ist, läuft die Sitzung ab und ihre Daten werden verworfen. Sie können eine Sitzung auch manuell beenden, z. B. beim Abmelden.

Dieser Mechanismus ermöglicht es dem Server, benutzerbezogene Informationen wie den Anmeldestatus oder den Inhalt eines Warenkorbs über mehrere Anfragen hinweg "zu erinnern".

---

### **Wie man einen Sitzungswert setzt**

Um Daten in einer `HttpSession` zu speichern, verwenden Sie die Methode `setAttribute`. Diese Methode ordnet einen Schlüssel (ein `String`) einem Wert (einem beliebigen Java-Objekt) zu. Hier ist, wie es geht:

1. **Erhalten Sie das HttpSession-Objekt**: In einem Servlet erhalten Sie die `HttpSession` aus dem `HttpServletRequest`-Objekt mit `request.getSession()`. Diese Methode erstellt eine neue Sitzung, wenn keine existiert, oder gibt die bestehende Sitzung zurück.

2. **Setzen Sie das Attribut**: Rufen Sie `setAttribute(key, value)` auf dem `HttpSession`-Objekt auf.

Hier ist ein Beispiel in einem Servlet:

```java
import javax.servlet.http.*;
import java.io.*;

public class SetSessionServlet extends HttpServlet {
    public void doGet(HttpServletRequest request, HttpServletResponse response)
            throws IOException {
        // Holen Sie sich die Sitzung (erstellt eine neue, wenn keine existiert)
        HttpSession session = request.getSession();

        // Setzen Sie ein Sitzungsattribut
        session.setAttribute("username", "Alice");

        // Antworten Sie dem Client
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        out.println("Sitzungswert gesetzt: username = Alice");
    }
}
```

In diesem Code:
- `request.getSession()` stellt sicher, dass eine Sitzung verfügbar ist.
- `session.setAttribute("username", "Alice")` speichert die Zeichenkette `"Alice"` unter dem Schlüssel `"username"`.

---

### **Wie man einen Sitzungswert abruft**

Um einen Wert aus der Sitzung abzurufen, verwenden Sie die Methode `getAttribute`. Da sie ein `Object` zurückgibt, müssen Sie es in den entsprechenden Typ umwandeln. Hier ist der Prozess:

1. **Erhalten Sie das HttpSession-Objekt**: Verwenden Sie `request.getSession()` oder `request.getSession(false)` (letzteres gibt `null` zurück, wenn keine Sitzung existiert, und vermeidet die Erstellung einer neuen).

2. **Holen Sie sich das Attribut**: Rufen Sie `getAttribute(key)` auf und wandeln Sie das Ergebnis um.

Hier ist ein Beispiel:

```java
import javax.servlet.http.*;
import java.io.*;

public class GetSessionServlet extends HttpServlet {
    public void doGet(HttpServletRequest request, HttpServletResponse response)
            throws IOException {
        // Holen Sie sich die Sitzung (gibt null zurück, wenn keine Sitzung existiert)
        HttpSession session = request.getSession(false);

        response.setContentType("text/html");
        PrintWriter out = response.getWriter();

        if (session != null) {
            // Holen Sie sich das Sitzungsattribut
            String username = (String) session.getAttribute("username");

            if (username != null) {
                out.println("Sitzungswert abgerufen: username = " + username);
            } else {
                out.println("Kein Benutzername in der Sitzung gefunden.");
            }
        } else {
            out.println("Keine aktive Sitzung.");
        }
    }
}
```

In diesem Code:
- `request.getSession(false)` ruft die bestehende Sitzung ab oder gibt `null` zurück.
- `session.getAttribute("username")` holt den Wert, der in `String` umgewandelt wird.
- Null-Überprüfungen verhindern Fehler, wenn die Sitzung oder das Attribut nicht existiert.

---

### **Praktisches Beispiel**

Hier ist ein kombiniertes Beispiel, das das Setzen und Abrufen eines Sitzungswerts über Anfragen zeigt:

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
        out.println("Benutzer in der Sitzung gesetzt: Bob");
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

Wenn ein Client auf `SetSessionServlet` zugreift, speichert die Sitzung `"Bob"`. Später, wenn `GetSessionServlet` aufgerufen wird, wird es abgerufen und angezeigt, da die Sitzung über Anfragen hinweg besteht.

---

### **Zusätzliche Hinweise**

- **Sitzungs-Timeout**: Setzen Sie dies mit `session.setMaxInactiveInterval(seconds)` (z. B. `session.setMaxInactiveInterval(1800)` für 30 Minuten) oder in `web.xml`:

  ```xml
  <session-config>
      <session-timeout>30</session-timeout> <!-- in Minuten -->
  </session-config>
  ```
- **Beenden einer Sitzung**: Verwenden Sie `session.invalidate()` (z. B. zum Abmelden).
- **Sicherheit**: Verwenden Sie HTTPS, um die Sitzungs-ID vor Abfangen zu schützen. Vermeiden Sie das Speichern hochsensibler Daten ohne Verschlüsselung.
- **Typumwandlung**: Wandeln Sie immer `getAttribute`-Ergebnisse um, da es `Object` zurückgibt.

---

### **Zusammenfassung**

- **Wie es funktioniert**: `HttpSession` hält den Benutzerzustand mit einer Sitzungs-ID (über Cookies oder URL-Umschreibung) aufrecht und speichert Daten auf dem Server.
- **Setzen eines Werts**: `session.setAttribute("key", value)`.
- **Abrufen eines Werts**: `String value = (String) session.getAttribute("key")`.

Das sollte Ihnen ein klares Verständnis von `HttpSession` in `javax.servlet` geben. Lassen Sie mich wissen, wenn Sie weitere Klarstellungen benötigen!