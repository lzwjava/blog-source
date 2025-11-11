---
audio: false
generated: true
lang: de
layout: post
title: Deaktivieren von Javadoc-Prüfungen in Checkstyle
translated: true
type: note
---

Um Checkstyle so zu konfigurieren, dass es alle Javadoc-bezogenen Prüfungen ignoriert und sie als keine Verstöße behandelt, müssen Sie Ihre Checkstyle-Konfigurationsdatei (typischerweise `checkstyle.xml`) so ändern, dass Sie Javadoc-bezogene Module entweder deaktivieren oder unterdrücken. So können Sie vorgehen:

### Option 1: Javadoc-bezogene Prüfungen deaktivieren
Checkstyle hat mehrere Javadoc-bezogene Module, wie z.B. `JavadocMethod`, `JavadocType`, `JavadocVariable`, `JavadocStyle` und `JavadocPackage`. Um diese zu deaktivieren, stellen Sie sicher, dass diese Module in Ihrer Konfigurationsdatei entfernt oder auskommentiert sind. Zum Beispiel:

```xml
<module name="Checker">
    <!-- Andere Module -->
    <!-- Javadoc-bezogene Prüfungen auskommentieren oder entfernen -->
    <!--
    <module name="JavadocMethod"/>
    <module name="JavadocType"/>
    <module name="JavadocVariable"/>
    <module name="JavadocStyle"/>
    <module name="JavadocPackage"/>
    -->
</module>
```

Wenn diese Module nicht in Ihrer Konfiguration vorhanden sind, erzwingt Checkstyle keine Javadoc-Prüfungen.

### Option 2: Javadoc-Prüfungen mit Suppression Filters unterdrücken
Sie können den `SuppressionFilter` von Checkstyle verwenden, um alle Javadoc-bezogenen Prüfungen in Ihrer Codebasis zu unterdrücken. Fügen Sie eine Unterdrückungsregel zu einer separaten Suppressions-Datei hinzu (z.B. `suppressions.xml`) und verweisen Sie in Ihrer Checkstyle-Konfiguration darauf.

1. **Erstellen Sie eine Suppressions-Datei** (z.B. `suppressions.xml`):
   ```xml
   <!DOCTYPE suppressions PUBLIC
       "-//Checkstyle//DTD Suppression DTD 1.0//EN"
       "https://checkstyle.org/dtds/suppressions_1_0.dtd">
   <suppressions>
       <!-- Unterdrücke alle Javadoc-bezogenen Prüfungen -->
       <suppress checks="Javadoc.*" files=".*"/>
   </suppressions>
   ```

   Das Muster `checks="Javadoc.*"` passt auf alle Prüfungen, die mit "Javadoc" beginnen (z.B. `JavadocMethod`, `JavadocType`, etc.), und `files=".*"` wendet die Unterdrückung auf alle Dateien an.

2. **Verweisen Sie in Ihrer Checkstyle-Konfiguration auf die Suppressions-Datei**:
   ```xml
   <module name="Checker">
       <module name="SuppressionFilter">
           <property name="file" value="suppressions.xml"/>
       </module>
       <!-- Andere Module -->
   </module>
   ```

### Option 3: `@SuppressWarnings` Annotations verwenden
Wenn Sie Javadoc-Prüfungen für bestimmte Klassen oder Methoden unterdrücken möchten, können Sie die Annotation `@SuppressWarnings("checkstyle:javadoc")` in Ihrem Java-Code verwenden. Zum Beispiel:

```java
@SuppressWarnings("checkstyle:javadoc")
public class MyClass {
    // Code ohne Javadoc löst keine Verstöße aus
}
```

Dieser Ansatz eignet sich für gezielte Unterdrückung, erfordert jedoch das Hinzufügen von Annotationen zum Code, was für die globale Deaktivierung von Javadoc-Prüfungen möglicherweise nicht ideal ist.

### Hinweise
- **Überprüfen Sie Ihre Konfiguration**: Nachdem Sie die Konfiguration geändert haben, führen Sie Checkstyle aus, um sicherzustellen, dass Javadoc-bezogene Verstöße nicht mehr gemeldet werden. Verwenden Sie zum Beispiel den Befehl:
  ```bash
  java -jar checkstyle.jar -c checkstyle.xml YourSourceFiles
  ```
- **Gängige Javadoc-Module**: Stellen Sie sicher, dass Sie alle relevanten Module behandeln, einschließlich `JavadocMethod`, `JavadocType`, `JavadocVariable`, `JavadocStyle`, `JavadocPackage`, `MissingJavadocMethod`, `MissingJavadocType` und `InvalidJavadocPosition`.
- **Checkstyle-Version**: Die genauen Modulnamen und die Syntax für die Unterdrückung können je nach Ihrer Checkstyle-Version leicht variieren. Die obigen Beispiele sind mit Checkstyle 8.x und höher kompatibel.
- **Globale Unterdrückung**: Der `SuppressionFilter`-Ansatz (Option 2) ist typischerweise der sauberste Weg, um alle Javadoc-Prüfungen zu deaktivieren, ohne die Kernkonfiguration umfangreich ändern zu müssen.

Wenn Sie ein bestimmtes Build-Tool wie Maven oder Gradle verwenden, lassen Sie es mich wissen, und ich kann zusätzliche Anleitung zur Integration der aktualisierten Checkstyle-Konfiguration geben!