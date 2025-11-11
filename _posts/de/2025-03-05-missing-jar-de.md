---
audio: false
generated: true
lang: de
layout: post
title: Fehlende JAR-Dateien in WebSphere Liberty
translated: true
type: note
---

In WebSphere Liberty sind Ihnen Warnungen in der `console.log`-Datei aufgefallen, die so aussehen: *"the manifest class path: grpc-protobuf.jar cannot be found in jar file ..ear/war or its parent"*. Diese Warnungen zeigen an, dass der Server die Datei `grpc-protobuf.jar` nicht finden kann, die im Manifest-Classpath einer EAR- oder WAR-Datei Ihrer Anwendung referenziert wird. Im Folgenden gehe ich auf Ihre Fragen ein: ob diese Warnungen von Bedeutung sind, ob sie die Ausführung Ihrer Anwendung beeinträchtigen und wie Sie sie entfernen können.

---

### Sind diese Warnungen von Bedeutung?

Ja und nein – es hängt davon ab, ob die fehlende JAR-Datei von Ihrer Anwendung benötigt wird:

- **Falls die JAR-Datei erforderlich ist:**  
  Wenn `grpc-protobuf.jar` Klassen oder Ressourcen enthält, die Ihre Anwendung zur Laufzeit benötigt, ist diese Warnung bedeutsam. Ohne die JAR-Datei könnte Ihre Anwendung Laufzeitfehler wie `ClassNotFoundException` verursachen, was dazu führen könnte, dass Teile davon fehlschlagen oder sich falsch verhalten.

- **Falls die JAR-Datei nicht benötigt wird:**  
  Wenn die JAR-Datei tatsächlich nicht erforderlich ist – vielleicht ist es eine übriggebliebene Referenz aus einer alten Konfiguration oder eine optionale Abhängigkeit – ist die Warnung harmlos und beeinträchtigt die Funktionalität Ihrer Anwendung nicht. Sie wird jedoch weiterhin Ihre Logs überfluten.

Kurz gesagt, diese Warnungen sind wichtig, wenn die fehlende JAR-Datei für Ihre Anwendung kritisch ist. Sie müssen untersuchen, um ihre Bedeutung zu bestimmen.

---

### Wird es die Ausführung der Anwendung beeinträchtigen?

Die Auswirkung auf die Laufzeit Ihrer Anwendung hängt von der Rolle der fehlenden JAR-Datei ab:

- **Ja, falls die JAR-Datei erforderlich ist:**  
  Wenn Ihre Anwendung versucht, Klassen oder Ressourcen aus `grpc-protobuf.jar` zu verwenden, und diese fehlt, werden Sie wahrscheinlich Laufzeitfehler sehen. Dies könnte verhindern, dass Ihre Anwendung korrekt funktioniert, oder dazu führen, dass sie vollständig fehlschlägt.

- **Nein, falls die JAR-Datei unnötig ist:**  
  Wenn die JAR-Datei nicht benötigt wird, läuft Ihre Anwendung trotz der Warnung einwandfrei. Die Meldung bleibt einfach als Störfaktor in den Logs.

Um dies zu bestätigen, überprüfen Sie das Verhalten Ihrer Anwendung und die Logs auf Fehler, die über die Warnung selbst hinausgehen. Wenn alles wie erwartet funktioniert, ist die JAR-Datei möglicherweise nicht essenziell.

---

### Wie entfernt man die Warnung?

Um die Warnung zu beseitigen, müssen Sie entweder sicherstellen, dass die JAR-Datei korrekt in Ihrer Anwendung enthalten ist, oder die unnötige Referenz darauf entfernen. Hier ist ein schrittweiser Ansatz:

1. **Überprüfen, ob die JAR-Datei benötigt wird:**  
   - Prüfen Sie die Dokumentation, den Quellcode oder die Abhängigkeitsliste Ihrer Anwendung (z.B. `pom.xml` bei Verwendung von Maven), um festzustellen, ob `grpc-protobuf.jar` erforderlich ist.  
   - Wenn sie nicht benötigt wird, fahren Sie mit Schritt 3 fort, um die Referenz zu entfernen. Wenn sie benötigt wird, fahren Sie mit Schritt 2 fort.

2. **Korrigieren Sie das Packaging (falls die JAR-Datei benötigt wird):**  
   - Stellen Sie sicher, dass `grpc-protobuf.jar` am richtigen Ort innerhalb Ihres Anwendungspackages enthalten ist:  
     - **Für eine WAR-Datei:** Platzieren Sie sie im `WEB-INF/lib`-Verzeichnis.  
     - **Für eine EAR-Datei:** Platzieren Sie sie im Stammverzeichnis der EAR oder in einem designated library directory (z.B. `lib/`).  
   - Bauen Sie Ihre Anwendung neu und deployen Sie sie erneut, um zu bestätigen, dass die JAR-Datei nun von WebSphere Liberty gefunden wird.  
   - Überprüfen Sie die `console.log`, um zu sehen, ob die Warnung verschwindet.

3. **Aktualisieren Sie das Manifest (falls die JAR-Datei nicht benötigt wird):**  
   - Öffnen Sie die Datei `MANIFEST.MF` in Ihrer EAR oder WAR, die sich im `META-INF/`-Verzeichnis befindet.  
   - Suchen Sie nach dem Attribut `Class-Path`, das in etwa so aussehen könnte:  
     ```
     Class-Path: grpc-protobuf.jar some-other-lib.jar
     ```  
   - Entfernen Sie die Referenz auf `grpc-protobuf.jar`, sodass sie nicht mehr in der Liste erscheint.  
   - Speichern Sie die Datei, bauen Sie Ihre Anwendung neu und deployen Sie sie. Die Warnung sollte nicht mehr auftauchen.

4. **Überprüfen Sie die Classpath-Konfiguration:**  
   - Wenn Ihre Anwendung shared libraries oder benutzerdefinierte Classloader in WebSphere Liberty verwendet, vergewissern Sie sich, dass die Konfiguration des Servers (z.B. `server.xml`) die notwendigen JAR-Dateien enthält oder nicht fälschlicherweise auf `grpc-protobuf.jar` verweist.  
   - Passen Sie die Konfiguration bei Bedarf an und starten Sie den Server neu.

---

### Allgemeiner Rat

- **Warnungen untersuchen:** Selbst wenn die Anwendung einwandfrei zu laufen scheint, ist es eine gute Praxis, die Ursache von Warnungen zu verstehen, um später Überraschungen zu vermeiden.  
- **Nach Änderungen testen:** Nachdem Sie die JAR-Datei hinzugefügt oder das Manifest aktualisiert haben, testen Sie Ihre Anwendung gründlich, um sicherzustellen, dass sie sich wie erwartet verhält.  
- **Logs sauber halten:** Das Beheben unnötiger Warnungen hält Ihre Logs klar und erleichtert es, echte Probleme in der Zukunft zu erkennen.

Indem Sie diese Schritte befolgen, können Sie feststellen, ob die `grpc-protobuf.jar`-Warnung kritisch ist, potenzielle Laufzeitauswirkungen adressieren und die Warnung aus Ihrer `console.log` in WebSphere Liberty entfernen.

---

Wenn Sie `mvn package` ausführen, um eine EAR-Datei zu erstellen, und auf Warnungen über fehlende JAR-Dateien (wie `grpc-protobuf.jar`) im Manifest-Classpath stoßen, ist es unwahrscheinlich, dass das Problem von fehlenden Kommandozeilenargumenten herrührt. Der Befehl `mvn package` selbst ist ausreichend, um den Maven-Build-Lifecycle bis zur `package`-Phase auszulösen, die das Kompilieren, Testen und Packen Ihrer EAR umfasst. Die Warnung deutet jedoch eher auf ein Konfigurationsproblem in Ihrem Maven-Projekt hin als auf ein Problem mit dem Befehl oder seinen Argumenten. Lassen Sie uns das Schritt für Schritt untersuchen.

---

### Was bedeutet die Warnung?

Die Warnung zeigt an, dass die Datei `MANIFEST.MF` in Ihrer EAR `grpc-protobuf.jar` in ihrem `Class-Path`-Attribut referenziert, diese JAR-Datei jedoch nicht am erwarteten Ort innerhalb der EAR (z.B. im `lib/`-Verzeichnis) gefunden wird. Das `Class-Path`-Attribut listet JAR-Dateien auf, die Ihre Anwendung zur Laufzeit benötigt, und eine fehlende JAR-Datei könnte zu Laufzeitfehlern wie `ClassNotFoundException` führen.

---

### Liegt es an fehlenden Argumenten?

Nein, Sie benötigen keine zusätzlichen Argumente bei `mvn package`, um dies zu beheben. Maven verlässt sich auf die `pom.xml`-Dateien Ihres Projekts und Plugin-Konfigurationen (wie das `maven-ear-plugin`), um zu bestimmen, was in die EAR aufgenommen wird und wie das Manifest generiert wird. Das Hinzufügen von Argumenten wie `-DskipTests` oder `-U` könnte den Build-Prozess anpassen, aber sie adressieren diese Warnung nicht direkt. Die Grundursache liegt in Ihrem Projekt-Setup, nicht im Befehl selbst.

---

### Häufige Ursachen der Warnung

Hier sind die wahrscheinlichen Gründe für die Warnung:

1. **Fehlende Dependency-Deklaration**  
   Wenn `grpc-protobuf.jar` von Ihrer Anwendung benötigt wird, ist sie möglicherweise nicht als Dependency in der `pom.xml` Ihres EAR-Moduls oder seiner Submodule (z.B. eines WAR- oder JAR-Moduls) deklariert.

2. **Falscher Dependency-Scope**  
   Wenn `grpc-protobuf.jar` mit einem Scope wie `provided` deklariert ist, geht Maven davon aus, dass sie von der Laufzeitumgebung (z.B. WebSphere Liberty) bereitgestellt wird, und wird sie nicht in der EAR packagen.

3. **Unerwünschter Manifest-Eintrag**  
   Das `maven-ear-plugin` könnte so konfiguriert sein, dass es `grpc-protobuf.jar` zum `Class-Path` im Manifest hinzufügt, obwohl es nicht in der EAR enthalten ist.

4. **Problem mit transitiver Abhängigkeit**  
   Die JAR-Datei könnte eine transitive Abhängigkeit (eine Abhängigkeit einer anderen Abhängigkeit) sein, die entweder excluded ist oder nicht korrekt in der EAR enthalten ist.

---

### Wie man untersucht

Um das Problem einzugrenzen, versuchen Sie diese Schritte:

1. **Überprüfen Sie die Manifest-Datei**  
   Nachdem Sie `mvn package` ausgeführt haben, entpacken Sie die generierte EAR und sehen Sie sich `META-INF/MANIFEST.MF` an. Prüfen Sie, ob `grpc-protobuf.jar` im `Class-Path` aufgeführt ist. Dies bestätigt, ob die Warnung mit dem Inhalt des Manifests übereinstimmt.

2. **Überprüfen Sie die `pom.xml` der EAR**  
   Sehen Sie sich die Konfiguration des `maven-ear-plugin` an. Zum Beispiel:
   ```xml
   <plugin>
       <groupId>org.apache.maven.plugins</groupId>
       <artifactId>maven-ear-plugin</artifactId>
       <version>3.2.0</version>
       <configuration>
           <version>7</version> <!-- Passen Sie dies an Ihre Java EE Version an -->
           <defaultLibBundleDir>lib</defaultLibBundleDir>
       </configuration>
   </plugin>
   ```
   Stellen Sie sicher, dass es so eingerichtet ist, dass Dependencies im `lib/`-Verzeichnis (oder wo auch immer Ihre JAR-Dateien hingehen sollen) enthalten sind.

3. **Inspizieren Sie die Dependencies**  
   Führen Sie `mvn dependency:tree` in Ihrem EAR-Modul aus, um zu sehen, ob `grpc-protobuf.jar` auftaucht. Wenn es fehlt, ist es nirgendwo in Ihrem Dependency-Baum deklariert.

4. **Sehen Sie sich Submodule an**  
   Wenn Ihre EAR WARs oder JARs enthält, überprüfen Sie deren `pom.xml`-Dateien auf Dependencies von `grpc-protobuf.jar`.

---

### Wie man es behebt

Je nachdem, was Sie finden, wenden Sie eine dieser Lösungen an:

1. **Falls die JAR-Datei benötigt wird**  
   Fügen Sie `grpc-protobuf.jar` als Dependency in der `pom.xml` Ihrer EAR hinzu:
   ```xml
   <dependency>
       <groupId>io.grpc</groupId>
       <artifactId>grpc-protobuf</artifactId>
       <version>1.39.0</version> <!-- Verwenden Sie die korrekte Version -->
   </dependency>
   ```
   Stellen Sie sicher, dass das `maven-ear-plugin` sie in der EAR (z.B. im `lib/`-Verzeichnis) einschließt.

2. **Falls der Scope falsch ist**  
   Wenn sie als `<scope>provided</scope>` deklariert ist, aber gepackaged werden muss, ändern Sie sie zu `<scope>compile</scope>` (dem Standard-Scope).

3. **Falls die JAR-Datei nicht benötigt wird**  
   Wenn `grpc-protobuf.jar` nicht im Manifest sein sollte, prüfen Sie auf benutzerdefinierte Manifest-Konfigurationen im `maven-ear-plugin`:
   ```xml
   <configuration>
       <manifestFile>META-INF/MANIFEST.MF</manifestFile>
   </configuration>
   ```
   Entfernen Sie alle manuellen Einträge für `grpc-protobuf.jar`, oder lassen Sie Maven das Manifest automatisch generieren.

4. **Behandeln Sie transitive Dependencies**  
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

5. **Neu bauen und verifizieren**  
   Führen Sie `mvn clean package` aus, um die EAR neu zu bauen, und prüfen Sie dann die ausgegebene EAR-Datei, um sicherzustellen, dass die Warnung verschwunden ist und die Struktur korrekt ist.

---

### Schlussfolgerung

Der Befehl `mvn package` selbst erfordert keine zusätzlichen Argumente, um diese Warnung zu beheben. Stattdessen ist das Problem wahrscheinlich auf eine Fehlkonfiguration in Ihrer `pom.xml` oder im `maven-ear-plugin` zurückzuführen. Indem Sie sicherstellen, dass `grpc-protobuf.jar` entweder korrekt eingebunden (falls benötigt) oder aus dem Manifest entfernt (falls nicht benötigt) wird, können Sie die Warnung beseitigen. Beginnen Sie damit, Ihr Manifest und Ihre Dependencies zu inspizieren, und passen Sie dann Ihre Konfiguration entsprechend an. Dies sollte das Problem beheben, ohne dass Sie Ihren Build-Befehl ändern müssen.