---
audio: false
generated: true
lang: de
layout: post
title: Erkennung von Einrückungen in Checkstyle
translated: true
type: note
---

Ich verstehe, dass du dich fragst, warum Checkstyle die fehlende Einrückung vor der `System.out.println`-Anweisung in deiner `logAfter`-Methode nicht erkennt. Lass uns das Schritt für Schritt aufschlüsseln, um das Problem zu identifizieren und zu beheben.

### Warum erkennt Checkstyle das Einrückungsproblem nicht?
Checkstyle verwendet bestimmte Module, um Coding-Standards durchzusetzen, und für die Einrückung ist es auf das `Indentation`-Modul angewiesen. Wenn dieses Modul nicht korrekt konfiguriert oder in deinem Checkstyle-Setup enthalten ist, wird es Einrückungsfehler wie den in deinem Code nicht erkennen.

Hier ist dein aktueller Code:

```java
package org.lzwjava;

import org.aspectj.lang.JoinPoint;
import org.aspectj.lang.annotation.After;
import org.aspectj.lang.annotation.Aspect;
import org.springframework.stereotype.Component;

@Aspect
@Component
public class DebugAspect {
    @After("execution(* org.lzwjava..*(..))")
    public void logAfter(JoinPoint joinPoint) {
    System.out.println("Method executed: " + joinPoint.getSignature());  // No indentation
    }
}
```

Nach standardmäßigen Java-Konventionen sollten Anweisungen innerhalb einer Methode (wie `System.out.println`) relativ zur Methodendeklaration eingerückt sein. In deinem Code hat die `System.out.println`-Zeile keine Einrückung, was Checkstyle als Fehler markieren sollte, wenn es korrekt konfiguriert ist. Hier sind die wahrscheinlichsten Gründe, warum es nicht erkannt wird:

1. **Das `Indentation`-Modul ist nicht enthalten** in deiner Checkstyle-Konfigurationsdatei (z.B. `checks.xml`).
2. **Das Modul ist enthalten, aber falsch konfiguriert**, sodass es die erwarteten Einrückungsregeln nicht durchsetzt.
3. **Deine Konfiguration schließt bestimmte Dateien oder Pakete aus**, was verhindert, dass die Prüfung für diesen Code ausgeführt wird.
4. **Es gibt ein Problem damit, wie Checkstyle ausgeführt wird** (z.B. durch Maven oder eine IDE), das das erwartete Verhalten überschreibt.

Lass uns diese Möglichkeiten angehen und es zum Laufen bringen.

---

### Schritt 1: Überprüfe das `Indentation`-Modul in deiner Konfiguration
Überprüfe zuerst deine Checkstyle-Konfigurationsdatei (wahrscheinlich `checks.xml`), um zu sehen, ob das `Indentation`-Modul enthalten ist. So geht's:

1. **Finde deine `checks.xml`-Datei**. Sie befindet sich typischerweise in deinem Projektverzeichnis (z.B. `/home/lzw/Projects/blog-server/checks.xml`, wenn du ein Setup wie dieses verwendest).
2. **Suche nach dem `Indentation`-Modul** im `TreeWalker`-Abschnitt. Es sollte so aussehen:

   ```xml
   <module name="TreeWalker">
       <!-- Other checks -->
       <module name="Indentation">
           <property name="basicOffset" value="4"/>  <!-- 4 Leerzeichen pro Einrückungsebene -->
           <property name="lineWrappingIndentation" value="4"/>  <!-- Optional: für umbrochene Zeilen -->
       </module>
       <!-- Other checks -->
   </module>
   ```

   - **Wenn du dieses Modul nicht siehst**, ist das das Problem – Checkstyle prüft die Einrückung überhaupt nicht.
   - **Wenn es da ist**, überprüfe, ob `basicOffset` auf einen sinnvollen Wert gesetzt ist (z.B. 4 Leerzeichen, was für Java Standard ist).

---

### Schritt 2: Füge das `Indentation`-Modul hinzu oder korrigiere es
Wenn das Modul fehlt oder nicht korrekt eingerichtet ist, kannst du es so beheben:

#### Wenn es fehlt: Füge das `Indentation`-Modul hinzu
Füge Folgendes im `TreeWalker`-Abschnitt deiner `checks.xml` hinzu:

```xml
<module name="Indentation">
    <property name="basicOffset" value="4"/>  <!-- 4 Leerzeichen ist typisch -->
    <property name="lineWrappingIndentation" value="4"/>
</module>
```

#### Wenn es vorhanden ist: Überprüfe die Einstellungen
Stelle sicher:
- `basicOffset` ist auf die Anzahl der Leerzeichen gesetzt, die du für die Einrückung erwartest (z.B. 4).
- Keine Eigenschaften die Prüfung deaktivieren oder überschreiben, sodass dein Code übersprungen wird.

Speichere die Datei nach den Änderungen.

---

### Schritt 3: Prüfe auf Ausschlüsse
Manchmal schließen Checkstyle-Konfigurationen bestimmte Dateien oder Pakete aus. Suche in deiner `checks.xml` nach:
- Einem `SuppressionFilter` oder `SuppressionCommentFilter`, der möglicherweise das Paket `org.lzwjava` oder diese spezifische Datei überspringt.
- Irgendwelchen Patterns, die `.java`-Dateien oder bestimmte Verzeichnisse ausschließen.

Wenn du einen solchen Ausschluss findest, der deinen Code betrifft, entferne oder passe ihn an, sodass `DebugAspect.java` geprüft wird.

---

### Schritt 4: Teste die Korrektur
Nachdem du deine Konfiguration aktualisiert hast, führe Checkstyle erneut aus. Wenn du z.B. Maven verwendest:

```bash
mvn clean checkstyle:check
```

Überprüfe die Ausgabe. Du solltest einen Fehler wie diesen sehen:

```
[ERROR] DebugAspect.java:13: 'System.out.println' sollte um +4 Leerzeichen relativ zu seinem umschließenden Block eingerückt sein.
```

Dies würde anzeigen, dass Checkstyle jetzt die fehlende Einrückung erkennt. Zur Referenz, so sollte dein Code *mit* korrekter Einrückung aussehen:

```java
@Aspect
@Component
public class DebugAspect {
    @After("execution(* org.lzwjava..*(..))")
    public void logAfter(JoinPoint joinPoint) {
        System.out.println("Method executed: " + joinPoint.getSignature());  // 4 Leerzeichen Einrückung
    }
}
```

---

### Schritt 5: Fehlerbehebung, falls es immer noch nicht funktioniert
Wenn Checkstyle das Problem immer noch nicht meldet:
- **Führe es mit Debug-Ausgabe aus**: Verwende einen ausführlichen Befehl, um zu sehen, was Checkstyle tut:
  ```bash
  mvn -X checkstyle:check
  ```
  Achte auf Nachrichten über das `Indentation`-Modul oder übersprungene Dateien.
- **Teste mit einer minimalen Konfiguration**: Erstelle eine temporäre `checks.xml` nur mit der `Indentation`-Prüfung:
  ```xml
  <?xml version="1.0"?>
  <!DOCTYPE module PUBLIC
      "-//Checkstyle//DTD Checkstyle Configuration 1.3//EN"
      "https://checkstyle.org/dtds/configuration_1_3.dtd">
  <module name="Checker">
      <module name="TreeWalker">
          <module name="Indentation">
              <property name="basicOffset" value="4"/>
          </module>
      </module>
  </module>
  ```
  Weise Checkstyle diese Datei zu und teste erneut, um das Problem zu isolieren.
- **Überprüfe dein Setup**: Wenn du Checkstyle über eine IDE (wie IntelliJ oder Eclipse) ausführst, stelle sicher, dass die IDE die aktualisierte `checks.xml` verwendet und nicht eine alte oder separate Konfiguration.

---

### Fazit
Checkstyle erkennt die fehlende Einrückung nicht, weil das `Indentation`-Modul wahrscheinlich in deiner `checks.xml` fehlt oder falsch konfiguriert ist. Indem du dieses Modul hinzufügst oder korrigierst und sicherstellst, dass keine Ausschlüsse gelten, sollte Checkstyle das Fehlen der Einrückung vor `System.out.println` melden. Aktualisiere deine Konfiguration wie gezeigt, führe Checkstyle erneut aus und du solltest den Fehler wie erwartet gemeldet sehen. Lass mich wissen, wenn du Hilfe mit den nächsten Schritten benötigst!