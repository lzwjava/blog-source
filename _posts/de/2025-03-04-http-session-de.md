---
audio: false
generated: true
lang: de
layout: post
title: HTTP-Sitzungen in Java Servlets
translated: true
type: note
---

Lassen Sie mich Ihre Frage dazu beantworten, wie `HttpSession` im `javax.servlet`-Paket funktioniert, wie man einen Sitzungswert setzt und wie man ihn abruft. Ich nehme an, dass "HTTPSession" in Ihrer Frage ein Tippfehler ist und Sie `HttpSession` meinten, da dies der korrekte Klassenname im `javax.servlet`-Paket ist.

---

### **Wie funktioniert HttpSession?**

`HttpSession` ist ein Interface im `javax.servlet.http`-Paket, das State-Management in Java-Webanwendungen ermöglicht. HTTP ist von Natur aus zustandslos – jede Anfrage eines Clients (z.B. eines Browsers) an einen Server ist unabhängig und hat kein Gedächtnis für vorherige Interaktionen. Um diese Einschränkung zu überwinden und benutzerspezifische Daten über mehrere Anfragen hinweg zu verfolgen (z.B. während eines Benutzerbesuchs auf einer Website), bietet `HttpSession` einen Mechanismus zur Aufrechterhaltung einer "Sitzung".

So funktioniert es:

1.  **Sitzungserstellung**: Wenn ein Benutzer zum ersten Mal auf ein Servlet in einer Webanwendung zugreift, erstellt der Servlet-Container (z.B. Tomcat) ein neues `HttpSession`-Objekt. Dieser Sitzung wird eine eindeutige Kennung, die **Session-ID**, zugewiesen.

2.  **Session-ID-Übertragung**: Die Session-ID wird an den Browser des Clients gesendet, typischerweise als Cookie mit dem Namen `JSESSIONID`. Bei nachfolgenden Anfragen fügt der Browser diese Session-ID hinzu, sodass der Server die Anfrage der bestehenden Sitzung zuordnen kann.

3.  **Fallback-Mechanismus**: Wenn Cookies im Browser deaktiviert sind, kann der Servlet-Container **URL Rewriting** als Fallback verwenden. In diesem Fall wird die Session-ID an die URLs angehängt (z.B. `http://example.com/page;jsessionid=abc123`), was jedoch explizite Unterstützung im Anwendungscode erfordert.

4.  **Serverseitige Speicherung**: Die eigentlichen Sitzungsdaten (Attribute) werden auf dem Server gespeichert, nicht auf dem Client. Der Client hält nur die Session-ID, was Sitzungen für die Speicherung sensibler Informationen sicherer macht als Cookies. Die Daten werden typischerweise im Server-Speicher gehalten, können aber in erweiterten Konfigurationen auf der Festplatte oder in einer Datenbank persistiert werden.

5.  **Sitzungslebensdauer**: Sitzungen haben eine Timeout-Periode (z.B. standardmäßig 30 Minuten, konfigurierbar via `web.xml` oder programmatisch). Wenn der Benutzer länger als diese Zeit inaktiv ist, läuft die Sitzung ab und ihre Daten werden verworfen. Sie können eine Sitzung auch manuell beenden, z.B. während des Logouts.

Dieser Mechanismus ermöglicht es dem Server, benutzerspezifische Informationen wie Login-Status oder Warenkorbinhalte über mehrere Anfragen hinweg "zu merken".

---

### **Wie setzt man einen Sitzungswert?**

Um Daten in einer `HttpSession` zu speichern, verwenden Sie die Methode `setAttribute`. Diese Methode verknüpft einen Schlüssel (einen `String`) mit einem Wert (ein beliebiges Java-Objekt). So geht's:

1.  **HttpSession-Objekt beschaffen**: Holen Sie in einem Servlet die `HttpSession` aus dem `HttpServletRequest`-Objekt mit `request.getSession()`. Diese Methode erstellt eine neue Sitzung, falls keine existiert, oder gibt die bestehende Sitzung zurück.

2.  **Attribut setzen**: Rufen Sie `setAttribute(key, value)` auf dem `HttpSession`-Objekt auf.

Hier ein Beispiel in einem Servlet:

```java
import javax.servlet.http.*;
import java.io.*;

public class SetSessionServlet extends HttpServlet {
    public void doGet(HttpServletRequest request, HttpServletResponse response) 
            throws IOException {
        // Sitzung holen (erstellt eine neue, falls keine existiert)
        HttpSession session = request.getSession();
        
        // Ein Sitzungsattribut setzen
        session.setAttribute("username", "Alice");
        
        // Dem Client antworten
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        out.println("Session value set: username = Alice");
    }
}
```

In diesem Code:
- `request.getSession()` stellt sicher, dass eine Sitzung verfügbar ist.
- `session.setAttribute("username", "Alice")` speichert den String `"Alice"` unter dem Schlüssel `"username"`.

---

### **Wie ruft man einen Sitzungswert ab?**

Um einen Wert aus der Sitzung abzurufen, verwenden Sie die Methode `getAttribute`. Da sie ein `Object` zurückgibt, müssen Sie es in den entsprechenden Typ casten. So geht's:

1.  **HttpSession-Objekt beschaffen**: Verwenden Sie `request.getSession()` oder `request.getSession(false)` (letzteres gibt `null` zurück, falls keine Sitzung existiert, und vermeidet so die Erstellung einer neuen).

2.  **Attribut holen**: Rufen Sie `getAttribute(key)` auf und casten Sie das Ergebnis.

Hier ein Beispiel:

```java
import javax.servlet.http.*;
import java.io.*;

public class GetSessionServlet extends HttpServlet {
    public void doGet(HttpServletRequest request, HttpServletResponse response) 
            throws IOException {
        // Sitzung holen (gibt null zurück, falls keine Sitzung existiert)
        HttpSession session = request.getSession(false);
        
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        
        if (session != null) {
            // Das Sitzungsattribut abrufen
            String username = (String) session.getAttribute("username");
            
            if (username != null) {
                out.println("Session value retrieved: username = " + username);
            } else {
                out.println("No username found in session.");
            }
        } else {
            out.println("No active session.");
        }
    }
}
```

In diesem Code:
- `request.getSession(false)` ruft die bestehende Sitzung ab oder gibt `null` zurück.
- `session.getAttribute("username")` holt den Wert, gecastet zu `String`.
- Null-Checks verhindern Fehler, falls die Sitzung oder das Attribut nicht existiert.

---

### **Praktisches Beispiel**

Hier ein kombiniertes Beispiel, das das Setzen und Abrufen eines Sitzungswerts über mehrere Anfragen hinweg zeigt:

1.  **SetSessionServlet.java** (z.B. für Login):

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
        out.println("User set in session: Bob");
    }
}
```

2.  **GetSessionServlet.java** (z.B. für eine geschützte Seite):

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
            out.println("Welcome back, " + user);
        } else {
            out.println("Please log in first.");
        }
    }
}
```

Wenn ein Client auf `SetSessionServlet` zugreift, speichert die Sitzung `"Bob"`. Später ruft der Zugriff auf `GetSessionServlet` diesen Wert ab und zeigt ihn an, da die Sitzung über Anfragen hinweg bestehen bleibt.

---

### **Zusätzliche Hinweise**

-   **Sitzungs-Timeout**: Setzen via `session.setMaxInactiveInterval(seconds)` (z.B. `session.setMaxInactiveInterval(1800)` für 30 Minuten) oder in `web.xml`:

    ```xml
    <session-config>
        <session-timeout>30</session-timeout> <!-- in Minuten -->
    </session-config>
    ```
-   **Sitzung beenden**: Verwenden Sie `session.invalidate()` (z.B. für Logout).
-   **Sicherheit**: Verwenden Sie HTTPS, um die Session-ID vor Abfangen zu schützen. Vermeiden Sie das Speichern hochsensibler Daten ohne Verschlüsselung.
-   **Typumwandlung (Casting)**: Casten Sie die Ergebnisse von `getAttribute` immer, da es `Object` zurückgibt.

---

### **Zusammenfassung**

-   **Wie es funktioniert**: `HttpSession` verwaltet den Benutzerzustand mithilfe einer Session-ID (per Cookie oder URL Rewriting) und speichert Daten auf dem Server.
-   **Wert setzen**: `session.setAttribute("key", value)`.
-   **Wert abrufen**: `String value = (String) session.getAttribute("key")`.

Dies sollte Ihnen ein klares Verständnis von `HttpSession` in `javax.servlet` vermitteln. Lassen Sie mich wissen, wenn Sie weitere Erklärungen benötigen!