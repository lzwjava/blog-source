---
audio: false
generated: true
lang: de
layout: post
title: Fehlende JAR-Dateien in WebSphere Liberty
translated: true
---

In WebSphere Liberty haben Sie möglicherweise Warnungen in der `console.log`-Datei bemerkt, die so aussehen: *"the manifest class path: grpc-protobuf.jar cannot be found in jar file ..ear/war or its parent"*. Diese Warnungen deuten darauf hin, dass der Server die Datei `grpc-protobuf.jar` nicht finden kann, die im Manifest-Pfad einer EAR- oder WAR-Datei Ihrer Anwendung referenziert wird. Im Folgenden werde ich Ihre Fragen beantworten: ob diese Warnungen wichtig sind, ob sie den Betrieb Ihrer Anwendung beeinflussen und wie Sie sie entfernen können.

---

### Sind diese Warnungen wichtig?

Ja und nein – das hängt davon ab, ob die fehlende JAR-Datei von Ihrer Anwendung benötigt wird:

- **Wenn die JAR-Datei erforderlich ist:**
  Wenn `grpc-protobuf.jar` Klassen oder Ressourcen enthält, die Ihre Anwendung zur Laufzeit benötigt, ist diese Warnung bedeutend. Ohne die JAR-Datei könnte Ihre Anwendung Laufzeitfehler wie `ClassNotFoundException` erleiden, was dazu führen könnte, dass Teile davon fehlschlagen oder falsch funktionieren.

- **Wenn die JAR-Datei nicht benötigt wird:**
  Wenn die JAR-Datei nicht tatsächlich benötigt wird – vielleicht handelt es sich um einen veralteten Verweis aus einer alten Konfiguration oder eine optionale Abhängigkeit – ist die Warnung harmlos und beeinträchtigt die Funktionalität Ihrer Anwendung nicht. Sie wird jedoch weiterhin Ihre Protokolle verstopfen.

Kurz gesagt, diese Warnungen sind wichtig, wenn die fehlende JAR-Datei für Ihre Anwendung kritisch ist. Sie müssen ermitteln, ob sie wichtig ist.

---

### Wird es den Betrieb der Anwendung beeinflussen?

Die Auswirkungen auf die Laufzeit Ihrer Anwendung hängen von der Rolle der fehlenden JAR-Datei ab:

- **Ja, wenn die JAR-Datei erforderlich ist:**
  Wenn Ihre Anwendung versucht, Klassen oder Ressourcen aus `grpc-protobuf.jar` zu verwenden und diese fehlt, werden Sie wahrscheinlich Laufzeitfehler sehen. Dies könnte verhindern, dass Ihre Anwendung korrekt funktioniert oder sie vollständig fehlschlägt.

- **Nein, wenn die JAR-Datei nicht erforderlich ist:**
  Wenn die JAR-Datei nicht benötigt wird, wird Ihre Anwendung trotz der Warnung einwandfrei laufen. Die Nachricht wird einfach als Ärgernis in den Protokollen verbleiben.

Um dies zu bestätigen, überprüfen Sie das Verhalten Ihrer Anwendung und die Protokolle auf Fehler, die über die Warnung hinausgehen. Wenn alles wie erwartet funktioniert, ist die JAR-Datei möglicherweise nicht wesentlich.

---

### Wie kann man die Warnung entfernen?

Um die Warnung zu beseitigen, müssen Sie sicherstellen, dass die JAR-Datei ordnungsgemäß in Ihrer Anwendung enthalten ist oder den unnötigen Verweis darauf entfernen. Hier ist ein Schritt-für-Schritt-Ansatz:

1. **Überprüfen Sie, ob die JAR-Datei benötigt wird:**
   - Überprüfen Sie die Dokumentation, den Quellcode oder die Abhängigkeitsliste Ihrer Anwendung (z. B. `pom.xml`, wenn Maven verwendet wird), um festzustellen, ob `grpc-protobuf.jar` erforderlich ist.
   - Wenn sie nicht benötigt wird, fahren Sie mit Schritt 3 fort, um den Verweis zu entfernen. Wenn sie benötigt wird, fahren Sie mit Schritt 2 fort.

2. **Korrektur der Verpackung (wenn die JAR-Datei benötigt wird):**
   - Stellen Sie sicher, dass `grpc-protobuf.jar` an der richtigen Stelle innerhalb Ihres Anwendungs-Pakets enthalten ist:
     - **Für eine WAR-Datei:** Platzieren Sie sie im Verzeichnis `WEB-INF/lib`.
     - **Für eine EAR-Datei:** Platzieren Sie sie im Stammverzeichnis der EAR oder einem bestimmten Bibliotheksverzeichnis (z. B. `lib/`).
   - Bauen Sie Ihre Anwendung neu und deployen Sie sie erneut, um zu bestätigen, dass die JAR-Datei nun von WebSphere Liberty gefunden wird.
   - Überprüfen Sie die `console.log`, um zu sehen, ob die Warnung verschwindet.

3. **Aktualisieren Sie das Manifest (wenn die JAR-Datei nicht benötigt wird):**
   - Öffnen Sie die `MANIFEST.MF`-Datei in Ihrer EAR oder WAR, die sich im Verzeichnis `META-INF/` befindet.
   - Suchen Sie nach dem Attribut `Class-Path`, das etwa so aussehen könnte:
     ```
     Class-Path: grpc-protobuf.jar some-other-lib.jar
     ```
   - Entfernen Sie den Verweis auf `grpc-protobuf.jar`, sodass er nicht mehr in der Liste erscheint.
   - Speichern Sie die Datei, bauen Sie Ihre Anwendung neu und deployen Sie sie. Die Warnung sollte nicht mehr erscheinen.

4. **Überprüfen Sie die Classpath-Konfiguration:**
   - Wenn Ihre Anwendung gemeinsam genutzte Bibliotheken oder benutzerdefinierte Classloader in WebSphere Liberty verwendet, stellen Sie sicher, dass die Serverkonfiguration (z. B. `server.xml`) die erforderlichen JARs enthält oder `grpc-protobuf.jar` nicht falsch referenziert.
   - Passen Sie die Konfiguration bei Bedarf an und starten Sie den Server neu.

---

### Allgemeiner Rat

- **Untersuchen Sie Warnungen:** Selbst wenn die Anwendung scheinbar einwandfrei läuft, ist es eine gute Praxis, die Ursache von Warnungen zu verstehen, um später Überraschungen zu vermeiden.
- **Testen Sie nach Änderungen:** Nach dem Hinzufügen der JAR-Datei oder dem Aktualisieren des Manifests testen Sie Ihre Anwendung gründlich, um sicherzustellen, dass sie wie erwartet funktioniert.
- **Halten Sie die Protokolle sauber:** Das Beheben unnötiger Warnungen hält Ihre Protokolle klar, sodass Sie zukünftig echte Probleme leichter erkennen können.

Durch die Befolgung dieser Schritte können Sie feststellen, ob die Warnung `grpc-protobuf.jar` kritisch ist, mögliche Laufzeitauswirkungen beheben und die Warnung aus Ihrer `console.log` in WebSphere Liberty entfernen.

---

Wenn Sie `mvn package` ausführen, um eine EAR-Datei zu erstellen, und Warnungen über fehlende JARs (wie `grpc-protobuf.jar`) im Manifest-Pfad erhalten, ist es unwahrscheinlich, dass das Problem von fehlenden Befehlszeilenargumenten stammt. Der Befehl `mvn package` selbst ist ausreichend, um den Maven-Build-Lebenszyklus bis zur `package`-Phase auszulösen, die das Kompilieren, Testen und Verpacken Ihrer EAR umfasst. Die Warnung deutet jedoch auf ein Konfigurationsproblem in Ihrem Maven-Projekt hin und nicht auf ein Problem mit dem Befehl oder seinen Argumenten. Lassen Sie uns dies Schritt für Schritt untersuchen.

---

### Was bedeutet die Warnung?

Die Warnung deutet darauf hin, dass die `MANIFEST.MF`-Datei in Ihrer EAR `grpc-protobuf.jar` im Attribut `Class-Path` referenziert, diese JAR-Datei jedoch nicht an der erwarteten Stelle innerhalb der EAR (z. B. im Verzeichnis `lib/`) gefunden wird. Das Attribut `Class-Path` listet JARs auf, die Ihre Anwendung zur Laufzeit benötigt, und eine fehlende JAR-Datei könnte zu Laufzeitfehlern wie `ClassNotFoundException` führen.

---

### Geht es um fehlende Argumente?

Nein, Sie benötigen keine zusätzlichen Argumente mit `mvn package`, um dieses Problem zu beheben. Maven verlässt sich auf Ihre Projektdateien `pom.xml` und Plugin-Konfigurationen (wie das `maven-ear-plugin`), um zu bestimmen, was in die EAR aufgenommen wird und wie das Manifest generiert wird. Das Hinzufügen von Argumenten wie `-DskipTests` oder `-U` könnte den Build-Prozess anpassen, aber sie werden dieses Problem nicht direkt beheben. Die Ursache liegt in Ihrer Projektkonfiguration, nicht im Befehl selbst.

---

### Häufige Ursachen der Warnung

Hier sind die wahrscheinlichsten Ursachen für die Warnung:

1. **Fehlende Abhängigkeitserklärung**
   Wenn `grpc-protobuf.jar` von Ihrer Anwendung benötigt wird, könnte sie möglicherweise nicht als Abhängigkeit im `pom.xml` des EAR-Moduls oder seiner Submodule (z. B. ein WAR- oder JAR-Modul) deklariert sein.

2. **Falscher Abhängigkeitsscope**
   Wenn `grpc-protobuf.jar` mit einem Scope wie `provided` deklariert ist, geht Maven davon aus, dass es von der Laufzeitumgebung (z. B. WebSphere Liberty) bereitgestellt wird und es nicht in der EAR verpackt.

3. **Unerwünschter Manifest-Eintrag**
   Das `maven-ear-plugin` könnte so konfiguriert sein, dass es `grpc-protobuf.jar` zum `Class-Path` im Manifest hinzufügt, obwohl es nicht in der EAR enthalten ist.

4. **Transitives Abhängigkeitsproblem**
   Die JAR-Datei könnte eine transitive Abhängigkeit (eine Abhängigkeit einer anderen Abhängigkeit) sein, die entweder ausgeschlossen oder nicht ordnungsgemäß in die EAR aufgenommen wird.

---

### Wie kann man es untersuchen?

Um das Problem zu lokalisieren, versuchen Sie diese Schritte:

1. **Überprüfen Sie die Manifest-Datei**
   Nach dem Ausführen von `mvn package` entpacken Sie die generierte EAR und sehen Sie sich `META-INF/MANIFEST.MF` an. Überprüfen Sie, ob `grpc-protobuf.jar` im `Class-Path` aufgeführt ist. Dies bestätigt, ob die Warnung mit dem Inhalt des Manifests übereinstimmt.

2. **Überprüfen Sie das `pom.xml` der EAR**
   Sehen Sie sich die Konfiguration des `maven-ear-plugin` an. Zum Beispiel:
   ```xml
   <plugin>
       <groupId>org.apache.maven.plugins</groupId>
       <artifactId>maven-ear-plugin</artifactId>
       <version>3.2.0</version>
       <configuration>
           <version>7</version> <!-- Passen Sie Ihre Java EE-Version an -->
           <defaultLibBundleDir>lib</defaultLibBundleDir>
       </configuration>
   </plugin>
   ```
   Stellen Sie sicher, dass es so konfiguriert ist, dass Abhängigkeiten im Verzeichnis `lib/` (oder wo Ihre JARs hingehen sollen) enthalten sind.

3. **Überprüfen Sie die Abhängigkeiten**
   Führen Sie `mvn dependency:tree` auf Ihrem EAR-Modul aus, um zu sehen, ob `grpc-protobuf.jar` erscheint. Wenn es fehlt, ist es nirgends in Ihrem Abhängigkeitbaum deklariert.

4. **Überprüfen Sie die Submodule**
   Wenn Ihre EAR WARs oder JARs enthält, überprüfen Sie deren `pom.xml`-Dateien auf Abhängigkeiten von `grpc-protobuf.jar`.

---

### Wie kann man es beheben?

Abhängig davon, was Sie finden, wenden Sie eine dieser Lösungen an:

1. **Wenn die JAR-Datei benötigt wird**
   Fügen Sie `grpc-protobuf.jar` als Abhängigkeit im `pom.xml` der EAR hinzu:
   ```xml
   <dependency>
       <groupId>io.grpc</groupId>
       <artifactId>grpc-protobuf</artifactId>
       <version>1.39.0</version> <!-- Verwenden Sie die richtige Version -->
   </dependency>
   ```
   Stellen Sie sicher, dass das `maven-ear-plugin` es in der EAR enthält (z. B. im Verzeichnis `lib/`).

2. **Wenn der Scope falsch ist**
   Wenn es als `<scope>provided</scope>` deklariert ist, aber verpackt werden muss, ändern Sie es in `<scope>compile</scope>` (der Standard-Scope).

3. **Wenn die JAR-Datei nicht benötigt wird**
   Wenn `grpc-protobuf.jar` nicht im Manifest sein sollte, überprüfen Sie benutzerdefinierte Manifest-Konfigurationen im `maven-ear-plugin`:
   ```xml
   <configuration>
       <manifestFile>META-INF/MANIFEST.MF</manifestFile>
   </configuration>
   ```
   Entfernen Sie alle manuellen Einträge für `grpc-protobuf.jar` oder lassen Sie Maven das Manifest automatisch generieren.

4. **Transitive Abhängigkeiten behandeln**
   Wenn es sich um eine transitive Abhängigkeit handelt, die Sie nicht benötigen, schließen Sie sie aus:
   ```xml
   <dependency>
       <groupId>some.group</groupId>
       <artifactId>some-artifact</artifactId>
       <exclusions>
           <exclusion>
               <groupId>io.grpc</groupId>
               <artifactId>grpc-protobuf</artifactId>
           </exclusion>
       </exclusions>
   </dependency>
   ```

5. **Neu bauen und überprüfen**
   Führen Sie `mvn clean package` aus, um die EAR neu zu erstellen, und überprüfen Sie die ausgegebene EAR-Datei, um sicherzustellen, dass die Warnung verschwunden ist und die Struktur korrekt ist.

---

### Schlussfolgerung

Der Befehl `mvn package` selbst benötigt keine zusätzlichen Argumente, um diese Warnung zu beheben. Stattdessen ist das Problem wahrscheinlich auf eine falsche Konfiguration in Ihrem `pom.xml` oder dem `maven-ear-plugin` zurückzuführen. Durch das Sicherstellen, dass `grpc-protobuf.jar` entweder ordnungsgemäß enthalten (wenn benötigt) oder aus dem Manifest entfernt (wenn nicht benötigt) wird, können Sie die Warnung beseitigen. Beginnen Sie mit der Untersuchung Ihres Manifests und Ihrer Abhängigkeiten und passen Sie Ihre Konfiguration entsprechend an. Dies sollte das Problem ohne Änderung Ihres Build-Befehls beheben.