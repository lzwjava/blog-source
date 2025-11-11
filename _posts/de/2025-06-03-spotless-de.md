---
audio: false
generated: true
lang: de
layout: post
title: Formatieren von Code mit Spotless
translated: true
type: note
---

Es gibt keinen `mvn checkstyle:format`-Befehl im Maven Checkstyle Plugin. Das Plugin ist in erster Linie dafür konzipiert, Code anhand einer Checkstyle-Konfiguration zu prüfen und Verstöße zu melden, nicht um Code automatisch zu formatieren. Sie können jedoch eine Codeformatierung basierend auf einer Checkstyle-Konfiguration mit anderen Tools wie Spotless oder dem Maven Formatter Plugin erreichen, die so konfiguriert werden können, dass sie mit Ihren Checkstyle-Regeln übereinstimmen.

Im Folgenden werde ich erklären, wie Sie Code basierend auf Ihrer Checkstyle-Konfiguration mit dem **Spotless Maven Plugin** formatieren können, da es eine beliebte Wahl für diesen Zweck ist und sich in Checkstyle-Regeln integrieren lässt.

### Lösung: Verwendung von Spotless mit Checkstyle-Konfiguration

Das Spotless Maven Plugin kann Java-Code gemäß einer Checkstyle-Konfigurationsdatei (z.B. `checkstyle.xml`) formatieren. So richten Sie es ein:

#### 1. Spotless zu Ihrer `pom.xml` hinzufügen
Fügen Sie das Spotless Plugin zu Ihrer `pom.xml` hinzu und konfigurieren Sie es so, dass es Ihre Checkstyle-Konfigurationsdatei verwendet.

```xml
<build>
  <plugins>
    <plugin>
      <groupId>com.diffplug.spotless</groupId>
      <artifactId>spotless-maven-plugin</artifactId>
      <version>2.43.0</version> <!-- Verwenden Sie die neueste Version -->
      <configuration>
        <java>
          <!-- Zeigen Sie auf Ihre Checkstyle-Konfigurationsdatei -->
          <googleJavaFormat>
            <version>1.22.0</version> <!-- Optional: Verwenden Sie eine bestimmte Version -->
            <style>GOOGLE</style> <!-- Oder AOSP, oder weglassen für Standard -->
          </googleJavaFormat>
          <formatAnnotations>
            <!-- Checkstyle-Konfiguration für die Formatierung verwenden -->
            <checkstyle>
              <file>${project.basedir}/checkstyle.xml</file> <!-- Pfad zu Ihrer Checkstyle-Konfig -->
              <version>10.17.0</version> <!-- Stimmen Sie Ihre Checkstyle-Version ab -->
            </checkstyle>
          </formatAnnotations>
        </java>
      </configuration>
      <executions>
        <execution>
          <goals>
            <goal>apply</goal> <!-- Formatiert den Code automatisch -->
          </goals>
          <phase>process-sources</phase> <!-- Optional: An eine Phase binden -->
        </execution>
      </executions>
    </plugin>
  </plugins>
</build>
```

#### 2. Sicherstellen, dass Ihre Checkstyle-Konfiguration existiert
Stellen Sie sicher, dass Sie eine `checkstyle.xml`-Datei in Ihrem Projekt haben (z.B. im Stammverzeichnis oder einem Unterverzeichnis). Diese Datei definiert die Codierungsstandards (z.B. Einrückung, Leerzeichen usw.), die Spotless zur Formatierung Ihres Codes verwendet. Wenn Sie einen Standard wie Google Java Format verwenden, können Sie darauf verweisen oder eine benutzerdefinierte Checkstyle-Konfiguration verwenden, die auf Ihr Projekt zugeschnitten ist.

Beispielhafter `checkstyle.xml`-Ausschnitt für grundlegende Formatierungsregeln:
```xml
<?xml version="1.0"?>
<!DOCTYPE module PUBLIC "-//Checkstyle//DTD Checkstyle Configuration 1.3//EN" "https://checkstyle.sourceforge.io/dtds/configuration_1_3.dtd">
<module name="Checker">
  <module name="TreeWalker">
    <module name="Indentation">
      <property name="basicOffset" value="2"/>
      <property name="braceAdjustment" value="0"/>
    </module>
  </module>
</module>
```

#### 3. Spotless ausführen, um Code zu formatieren
Um Ihren Code basierend auf der Checkstyle-Konfiguration zu formatieren, führen Sie aus:
```bash
mvn spotless:apply
```

Dieser Befehl formatiert alle Java-Dateien in Ihrem Projekt gemäß den Regeln, die in Ihrer Checkstyle-Konfiguration und etwaigen zusätzlichen Formatierungseinstellungen (z.B. Google Java Format) definiert sind.

#### 4. Formatierung mit Checkstyle überprüfen
Nach der Formatierung können Sie `mvn checkstyle:check` ausführen, um zu überprüfen, ob der formatierte Code Ihren Checkstyle-Regeln entspricht. Wenn Sie dem vorherigen Ratschlag gefolgt sind, `<failOnViolation>false</failOnViolation>` zu setzen, werden eventuell verbleibende Verstöße gemeldet, ohne den Build zu stoppen.

### Alternative: Maven Formatter Plugin
Wenn Sie Spotless nicht verwenden möchten, können Sie das **Maven Formatter Plugin** verwenden, das ebenfalls Formatierung basierend auf Regeln unterstützt, aber weniger häufig direkt mit Checkstyle-Konfigurationen verwendet wird. Hier ist eine grundlegende Einrichtung:

```xml
<build>
  <plugins>
    <plugin>
      <groupId>net.revelc.code.formatter</groupId>
      <artifactId>formatter-maven-plugin</artifactId>
      <version>2.23.0</version> <!-- Verwenden Sie die neueste Version -->
      <configuration>
        <configFile>${project.basedir}/checkstyle.xml</configFile> <!-- Pfad zur Checkstyle-Konfig -->
      </configuration>
      <executions>
        <execution>
          <goals>
            <goal>format</goal>
          </goals>
        </execution>
      </executions>
    </plugin>
  </plugins>
</build>
```

Führen Sie die Formatierung mit folgendem Befehl aus:
```bash
mvn formatter:format
```

### Hinweise
- **Kein direkter Checkstyle-Format-Befehl**: Das Checkstyle Maven Plugin bietet kein `format`-Goal. Tools wie Spotless oder das Formatter Plugin sind erforderlich, um Formatierung basierend auf Checkstyle-Regeln anzuwenden.
- **Checkstyle-Version-Kompatibilität**: Stellen Sie sicher, dass die in Spotless (oder Formatter) angegebene Checkstyle-Version mit der in Ihrem Checkstyle Plugin verwendeten Version übereinstimmt, um Regelinkonsistenzen zu vermeiden.
- **Benutzerdefinierte Checkstyle-Regeln**: Ihre `checkstyle.xml` muss formatierungsbezogene Regeln (z.B. `Indentation`, `WhitespaceAround` usw.) enthalten, damit Spotless sie korrekt anwenden kann.
- **Multi-Modul-Projekte**: In einem Multi-Modul Maven Projekt können Sie die Spotless/Formatter-Konfiguration in der übergeordneten `pom.xml` platzieren, um sie über alle Module hinweg anzuwenden, oder sie je Modul nach Bedarf konfigurieren.
- **Prüfung nach der Formatierung**: Führen Sie immer `mvn checkstyle:check` nach der Formatierung aus, um die Konformität zu bestätigen, insbesondere wenn Sie nicht-formatierungsbezogene Regeln (z.B. Methodenlänge, Komplexität) in Ihrer Checkstyle-Konfiguration haben.

Wenn Sie keine `checkstyle.xml` haben oder Hilfe bei der Erstellung benötigen, lassen Sie es mich wissen, und ich kann ein Beispiel bereitstellen oder Sie weiter anleiten! Wenn Sie ein anderes Tool bevorzugen oder spezifische Formatierungsanforderungen haben, teilen Sie diese bitte mit, und ich werde die Lösung entsprechend anpassen.