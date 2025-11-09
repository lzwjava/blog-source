---
audio: false
date: 2025-09-11
generated: true
image: false
lang: de
layout: post
model: mistralai/mistral-medium-3.1
title: IBM-Pakete in JaCoCo ausschließen
translated: true
type: note
---

Um **`com.ibm`**-Pakete (oder andere Pakete) von der JaCoCo-Abdeckung in einer **WebSphere Liberty Profile**-Umgebung auszuschließen, können Sie die Ausschlüsse in Ihrer **`pom.xml`**-Datei konfigurieren. Dies wird typischerweise in der Konfiguration des **JaCoCo Maven Plugins** durchgeführt.

---

### **So schließen Sie `com.ibm`-Pakete in `pom.xml` aus**

Sie können das Tag `<excludes>` in der Konfiguration des JaCoCo Plugins verwenden, um anzugeben, welche Klassen oder Pakete von der Coverage-Berichterstattung ausgeschlossen werden sollen.

#### **Beispielkonfiguration:**

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.jacoco</groupId>
            <artifactId>jacoco-maven-plugin</artifactId>
            <version>0.8.11</version> <!-- Verwenden Sie die neueste Version -->
            <executions>
                <execution>
                    <goals>
                        <goal>prepare-agent</goal>
                    </goals>
                </execution>
                <execution>
                    <id>report</id>
                    <phase>test</phase>
                    <goals>
                        <goal>report</goal>
                    </goals>
                    <configuration>
                        <outputDirectory>${project.reporting.outputDirectory}/jacoco</outputDirectory>
                        <excludes>
                            <!-- Schließt alle com.ibm-Pakete aus -->
                            <exclude>com/ibm/**</exclude>
                        </excludes>
                    </configuration>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```

---

### **Erklärung:**
- **`<excludes>`**: Dieser Abschnitt gibt an, welche Klassen oder Pakete von der Coverage-Berichterstattung ausgeschlossen werden sollen.
- **`<exclude>com/ibm/**</exclude>`**: Dies schließt alle Klassen unter dem Paket `com.ibm` und seinen Unterpaketen aus.

---

### **Zusätzliche Hinweise:**
- Wenn Sie mehrere Pakete ausschließen möchten, fügen Sie weitere `<exclude>`-Einträge hinzu:
  ```xml
  <excludes>
      <exclude>com/ibm/**</exclude>
      <exclude>org/apache/**</exclude>
  </excludes>
  ```
- Wenn Sie **JaCoCo mit WebSphere Liberty** verwenden, stellen Sie sicher, dass der JaCoCo Agent korrekt in Ihrer `server.env`- oder `jvm.options`-Datei konfiguriert ist und dass die Ausschlüsse in der `pom.xml` Ihren Anforderungen entsprechen.

---

### **Best Practice:**
- Überprüfen Sie die Ausschlüsse immer, indem Sie einen Coverage-Bericht ausführen und prüfen, ob die ausgeschlossenen Pakete nicht in den Ergebnissen enthalten sind.
- Wenn Sie Pakete zur Laufzeit ausschließen müssen (z. B. in den JaCoCo Agent-Argumenten), können Sie den `excludes`-Parameter in den Agent-Argumenten verwenden:
  ```plaintext
  -javaagent:/pfad/zum/jacocoagent.jar=destfile=/pfad/zum/jacoco.exec,excludes=com.ibm.*
  ```