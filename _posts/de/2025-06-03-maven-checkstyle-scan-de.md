---
audio: false
generated: true
lang: de
layout: post
title: 'Maven Checkstyle: Scannen Fortsetzen'
translated: true
type: note
---

Um `mvn checkstyle:check` dazu zu bringen, alle Module weiter zu überprüfen, ohne frühzeitig bei Verstößen abzubrechen, müssen Sie das Checkstyle Maven Plugin so konfigurieren, dass die Option `failOnViolation` deaktiviert wird. Standardmäßig ist `failOnViolation` auf `true` gesetzt, was dazu führt, dass der Build stoppt, sobald Verstöße gefunden werden. Wenn Sie es auf `false` setzen, kann der Scan über alle Module hinweg abgeschlossen werden und meldet alle Verstöße, ohne den Build anzuhalten.

### Lösung
Aktualisieren Sie Ihre `pom.xml`, um das Checkstyle Plugin wie folgt zu konfigurieren:

```xml
<build>
  <plugins>
    <plugin>
      <groupId>org.apache.maven.plugins</groupId>
      <artifactId>maven-checkstyle-plugin</artifactId>
      <version>3.3.1</version> <!-- Verwenden Sie die neueste Version -->
      <configuration>
        <failOnViolation>false</failOnViolation>
        <logViolationsToConsole>true</logViolationsToConsole> <!-- Optional: Protokolliert Verstöße in der Konsole -->
      </configuration>
      <executions>
        <execution>
          <id>checkstyle</id>
          <phase>validate</phase> <!-- Oder Ihre bevorzugte Phase -->
          <goals>
            <goal>check</goal>
          </goals>
        </execution>
      </executions>
    </plugin>
  </plugins>
</build>
```

### Erklärung
- **`<failOnViolation>false</failOnViolation>`**: Diese Einstellung verhindert, dass der Build bei erkannten Checkstyle-Verstößen fehlschlägt, und ermöglicht so, dass die Überprüfung über alle Module hinweg fortgesetzt wird.
- **`<logViolationsToConsole>true</logViolationsToConsole>`**: (Optional) Stellt sicher, dass Verstöße zur besseren Sichtbarkeit in der Konsole ausgegeben werden, selbst wenn der Build nicht fehlschlägt.
- **Ausführungsphase**: Das `<phase>validate</phase>` bindet die Checkstyle-Überprüfung an die `validate`-Phase des Maven-Lebenszyklus. Passen Sie die Phase an (z.B. `compile`, `verify`), wenn Sie sie in einer anderen Phase ausführen möchten.

### Ausführen des Befehls
Führen Sie den Befehl erneut aus:
```bash
mvn checkstyle:check
```
Mit `failOnViolation` auf `false` gesetzt, wird Maven alle Module überprüfen, alle Verstöße melden und den Build abschließen, ohne vorzeitig anzuhalten.

### Hinweise
- Stellen Sie sicher, dass Sie eine aktuelle Version des `maven-checkstyle-plugin` verwenden (z.B. 3.3.1 wie gezeigt). Prüfen Sie bei Bedarf auf Maven Central auf die neueste Version.
- Wenn Sie in einem Multi-Modul-Projekt arbeiten, gilt diese Konfiguration für alle Module, sofern sie nicht in einer Kind-`pom.xml` überschrieben wird.
- Um einen Bericht der Verstöße zu generieren, ziehen Sie in Betracht, stattdessen `mvn checkstyle:checkstyle` auszuführen, was standardmäßig einen HTML-Bericht erzeugt, ohne den Build fehlschlagen zu lassen.

Wenn Sie spezifische Anforderungen haben (z.B. benutzerdefinierte Checkstyle-Regeln oder ein anderes Setup), lassen Sie es mich wissen, und ich kann die Lösung weiter anpassen!