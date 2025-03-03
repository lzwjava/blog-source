---
audio: true
generated: true
lang: de
layout: post
title: Einen Schlüssel aus einem Namespace im Ausführungskontext abrufen
translated: true
---

Um einen Ausführungskontext zu verwenden, um einen Schlüssel aus einem Namensraum zu erhalten, hängt der Ansatz von dem spezifischen Framework oder System ab, mit dem Sie arbeiten, da "Ausführungskontext" und "Namensraum" je nach Kontext unterschiedliche Bedeutungen haben können. Da Sie kein bestimmtes Framework angegeben haben, werde ich eine allgemeine Anleitung bereitstellen, die Sie an Ihre Situation anpassen können, zusammen mit einem konkreten Beispiel, das eine gängige Szenario wie eine Java-basierte Anwendung (z.B. Spring) annimmt. Wenn dies nicht zu Ihrer Konfiguration passt, zögern Sie bitte nicht, weitere Details zu klären!

### Allgemeine Schritte zum Abrufen eines Schlüssels aus einem Namensraum in einem Ausführungskontext

Ein Ausführungskontext bezieht sich in der Regel auf ein Objekt oder eine Struktur, das/die Daten enthält, die für den aktuellen Ausführungsfluss relevant sind – wie z.B. ein Thread, eine Anfrage oder eine Transaktion. Ein Namensraum innerhalb dieses Kontextes ist eine Möglichkeit, Daten zu organisieren, oft als benannter Bereich oder als Sammlung von Schlüssel-Wert-Paaren. Hier ist, wie Sie dies angehen können:

1. **Zugreifen auf den aktuellen Ausführungskontext**
   - Ermitteln Sie, wie Sie den Ausführungskontext in Ihrer Anwendung erhalten. Dies könnte durch:
     - Eine statische Methode (z.B. `Context.getCurrent()`).
     - Eine thread-lokale Variable (z.B. `ThreadLocal<Context>`).
     - Abhängigkeitsinjektion, wenn Ihr Framework (wie Spring) den Kontext verwaltet.
   - Stellen Sie sicher, dass der Kontext in Ihrem aktuellen Ausführungsbereich verfügbar ist.

2. **Navigieren Sie zum Namensraum**
   - Sobald Sie den Kontext haben, identifizieren Sie, wie Namensräume dargestellt werden. Ein Namensraum könnte:
     - Ein spezifischer Methodenaufruf wie `context.getNamespace("myNamespace")`.
     - Eine verschachtelte Map oder Struktur innerhalb des Kontextes (z.B. `context.get("myNamespace")`, die eine `Map` zurückgibt).
     - Ein direkter Bereich, wenn Namensräume nicht explizit getrennt sind.
   - Überprüfen Sie die API Ihres Kontextes, um dessen Struktur zu verstehen.

3. **Abrufen des Wertes des Schlüssels**
   - Aus dem Namensraum verwenden Sie eine Methode wie `get("myKey")`, um den Wert abzurufen, der mit dem Schlüssel verbunden ist.
   - Behandeln Sie Fälle, in denen der Kontext oder Namensraum möglicherweise nicht verfügbar ist (z.B. Null-Überprüfungen).

### Beispiel: Verwendung eines benutzerdefinierten Ausführungskontextes in Plain Java

Angenommen, Sie arbeiten mit einer benutzerdefinierten `ExecutionContext`-Klasse in einer Java-Anwendung, bei der der Kontext statisch zugänglich ist und Namensräume als Schlüssel-Wert-Paar-Sammlungen enthält. Hier ist, wie Sie dies implementieren könnten:

```java
// Hypothetische ExecutionContext-Klasse
public class ExecutionContext {
    private Map<String, Map<String, Object>> namespaces = new HashMap<>();

    // Statische Methode, um den aktuellen Kontext zu erhalten (könnte in der Praxis ThreadLocal-basiert sein)
    private static ExecutionContext current = new ExecutionContext();
    public static ExecutionContext getCurrent() {
        return current;
    }

    // Methode, um einen Namensraum zu erhalten
    public Map<String, Object> getNamespace(String namespaceName) {
        return namespaces.getOrDefault(namespaceName, new HashMap<>());
    }

    // Zu Einrichtungszwecken (nicht Teil des Abrufs)
    public void setValue(String namespaceName, String key, Object value) {
        namespaces.computeIfAbsent(namespaceName, k -> new HashMap<>()).put(key, value);
    }
}

// Verwendungsbeispiel
public class MyClass {
    public void retrieveKeyFromNamespace() {
        // Schritt 1: Zugreifen auf den aktuellen Ausführungskontext
        ExecutionContext context = ExecutionContext.getCurrent();

        if (context != null) {
            // Schritt 2: Erhalten des Namensraums
            Map<String, Object> ns = context.getNamespace("myNamespace");

            // Schritt 3: Abrufen des Wertes für den Schlüssel
            Object value = ns.get("myKey");

            if (value != null) {
                System.out.println("Wert: " + value);
            } else {
                System.out.println("Schlüssel 'myKey' nicht im Namensraum 'myNamespace' gefunden");
            }
        } else {
            System.out.println("Ausführungskontext ist nicht verfügbar");
        }
    }

    public static void main(String[] args) {
        // Einrichtung zur Demonstration
        ExecutionContext.getCurrent().setValue("myNamespace", "myKey", "Hello, World!");

        new MyClass().retrieveKeyFromNamespace();
    }
}
```

**Ausgabe:**
```
Wert: Hello, World!
```

#### Erklärung:
- **Schritt 1:** `ExecutionContext.getCurrent()` liefert den aktuellen Kontext. In einer echten Anwendung könnte dies `ThreadLocal` verwenden, um sicherzustellen, dass Kontexte thread-spezifisch sind.
- **Schritt 2:** `getNamespace("myNamespace")` ruft eine `Map` ab, die den Namensraum darstellt.
- **Schritt 3:** `ns.get("myKey")` holt den Wert, der mit `"myKey"` verbunden ist.

### Alternatives Beispiel: Spring Web-Anwendung

Wenn Sie in einer Spring Web-Anwendung arbeiten, könnte der "Ausführungskontext" sich auf den Anfrage- oder Sitzungsbereich beziehen, und der "Namensraum" könnten die Attribute sein, die in diesen Bereichen gespeichert sind. Hier ist, wie Sie auf einen Schlüssel zugreifen können:

```java
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.ServletRequestAttributes;
import javax.servlet.http.HttpServletRequest;

public class MyClass {
    public Object getKeyFromRequestScope(String key) {
        // Schritt 1: Zugreifen auf den aktuellen Ausführungskontext (Anfrageattribute)
        ServletRequestAttributes attributes = (ServletRequestAttributes) RequestContextHolder.getRequestAttributes();

        if (attributes != null) {
            HttpServletRequest request = attributes.getRequest();

            // Schritt 2: Der Namensraum ist der Anforderungsbereich selbst
            // Schritt 3: Abrufen des Schlüssels
            return request.getAttribute(key);
        }
        return null; // Kontext nicht verfügbar
    }
}
```

- **Namensraum:** Hier dient der Anforderungsbereich als Namensraum.
- **Schlüsselabruf:** `request.getAttribute(key)` holt den Wert.

Für den Sitzungsbereich ersetzen Sie `request.getAttribute(key)` durch `request.getSession().getAttribute(key)`.

### Wichtige Überlegungen
- **Framework-spezifische APIs:** Die genaue Methode zum Zugriff auf den Kontext und den Namensraum hängt von Ihrem Framework ab. Zum Beispiel:
  - In Spring verwenden Sie `ApplicationContext`, `RequestContextHolder` oder `Environment` für verschiedene Kontexte.
  - In einem benutzerdefinierten System beziehen Sie sich auf dessen Dokumentation.
- **Null-Handling:** Überprüfen Sie immer auf Null-Werte, um Laufzeitfehler zu vermeiden.
- **Thread-Sicherheit:** Wenn der Kontext über Threads hinweg geteilt wird, stellen Sie sicher, dass eine ordnungsgemäße Synchronisation oder eine thread-lokale Speicherung erfolgt.

Wenn Sie ein bestimmtes Framework verwenden oder eine andere Definition von "Ausführungskontext" und "Namensraum" im Sinn haben, geben Sie bitte weitere Details an, und ich kann die Antwort weiter anpassen! Für den Moment sollte dieser allgemeine Ansatz Ihnen helfen, einen Schlüssel aus einem Namensraum innerhalb eines Ausführungskontextes abzurufen.