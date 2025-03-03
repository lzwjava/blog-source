---
audio: false
generated: true
lang: de
layout: post
title: Maven Release Plugin
translated: true
---

Hier ist eine umfassende Anleitung zur Verwendung des **Maven Release Plugins**, um den Release-Prozess für Ihr Maven-Projekt zu verwalten und zu automatisieren.

---

### Was ist das Maven Release Plugin?

Das **Maven Release Plugin** ist ein Werkzeug, das den Prozess des Releases eines Maven-Projekts automatisiert. Es übernimmt Aufgaben wie:

- Aktualisieren der Versionsnummern in den POM-Dateien Ihres Projekts.
- Committen von Änderungen in Ihrem Versionskontrollsystem (VCS), wie z.B. Git.
- Erstellen eines Tags für den Release im VCS.
- Bauen und Bereitstellen der Release-Artifakte.
- Vorbereiten des Projekts für den nächsten Entwicklungszyklus durch erneutes Aktualisieren der Versionsnummern.

Die beiden Hauptziele des Plugins sind:

- **`release:prepare`**: Bereitet das Projekt für einen Release vor, indem es Versionen aktualisiert, Änderungen committet und den Release im VCS taggt.
- **`release:perform`**: Baut und stellt die freigegebene Version unter Verwendung des getaggten Codes aus dem VCS bereit.

---

### Schritt-für-Schritt-Anleitung zur Verwendung des Maven Release Plugins

#### 1. Fügen Sie das Maven Release Plugin zu Ihrer POM-Datei hinzu

Um das Plugin zu verwenden, müssen Sie es in Ihrer `pom.xml` Ihres Projekts einbinden. Fügen Sie es unter dem `<build><plugins>`-Abschnitt wie folgt hinzu:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-release-plugin</artifactId>
            <version>2.5.3</version> <!-- Verwenden Sie die neueste stabile Version -->
        </plugin>
    </plugins>
</build>
```

**Hinweis**: Überprüfen Sie die [offizielle Seite des Maven Release Plugins](https://maven.apache.org/maven-release/maven-release-plugin/) auf die neueste Version und ersetzen Sie `2.5.3` entsprechend.

#### 2. Konfigurieren Sie den SCM (Source Control Management) Abschnitt

Das Plugin interagiert mit Ihrem VCS (z.B. Git), um Änderungen zu committen und Tags zu erstellen. Sie müssen Ihre VCS-Details im `<scm>`-Abschnitt Ihrer `pom.xml` angeben. Für ein Git-Repository, das auf GitHub gehostet wird, könnte es so aussehen:

```xml
<scm>
    <connection>scm:git:git://github.com/username/project.git</connection>
    <developerConnection>scm:git:git@github.com:username/project.git</developerConnection>
    <url>https://github.com/username/project</url>
</scm>
```

- Ersetzen Sie `username` und `project` durch Ihren tatsächlichen GitHub-Benutzernamen und den Repository-Namen.
- Passen Sie die URLs an, wenn Sie einen anderen Git-Hosting-Dienst verwenden (z.B. GitLab, Bitbucket).
- Stellen Sie sicher, dass Sie die notwendigen Anmeldeinformationen (z.B. SSH-Schlüssel oder ein persönlicher Zugriffstoken) konfiguriert haben, um Änderungen an das Repository zu pushen.

#### 3. Bereiten Sie Ihr Projekt für den Release vor

Stellen Sie sicher, dass Ihr Projekt vor dem Ausführen der Release-Befehle bereit ist:

- Alle Tests sind erfolgreich (`mvn test`).
- Es gibt keine uncommited Änderungen in Ihrem Arbeitsverzeichnis (führen Sie `git status` aus, um dies zu überprüfen).
- Sie befinden sich auf dem richtigen Branch (z.B. `master` oder `main`) für den Release.

#### 4. Führen Sie `release:prepare` aus

Das Ziel `release:prepare` bereitet Ihr Projekt für den Release vor. Führen Sie den folgenden Befehl in Ihrem Terminal aus:

```bash
mvn release:prepare
```

**Was passiert während `release:prepare`**:

- **Überprüfen auf uncommited Änderungen**: Stellt sicher, dass Ihr Arbeitsverzeichnis sauber ist.
- **Abfragen der Versionen**: Fragt nach der Release-Version und der nächsten Entwicklungsversion.
  - Beispiel: Wenn Ihre aktuelle Version `1.0-SNAPSHOT` ist, könnte es `1.0` für den Release und `1.1-SNAPSHOT` für die nächste Entwicklungsversion vorschlagen. Sie können die Standardeinstellungen akzeptieren oder benutzerdefinierte Versionen eingeben (z.B. `1.0.1` für ein Patch-Release).
- **Aktualisieren der POM-Dateien**: Ändert die Version zur Release-Version (z.B. `1.0`), committet die Änderung und taggt sie im VCS (z.B. `project-1.0`).
- **Vorbereiten für den nächsten Zyklus**: Aktualisiert die POM zur nächsten Entwicklungsversion (z.B. `1.1-SNAPSHOT`) und committet sie.

**Optionaler Trockenlauf**: Um den Prozess zu testen, ohne Änderungen vorzunehmen, verwenden Sie:

```bash
mvn release:prepare -DdryRun=true
```

Dies simuliert die Vorbereitungsschritte, ohne zu committen oder zu taggen.

#### 5. Führen Sie `release:perform` aus

Nach der Vorbereitung des Releases bauen und stellen Sie ihn mit folgendem Befehl bereit:

```bash
mvn release:perform
```

**Was passiert während `release:perform`**:

- Checkt die getaggte Version aus dem VCS aus.
- Baut das Projekt.
- Stellt die Artefakte im Repository bereit, das in Ihrem POM unter `<distributionManagement>` angegeben ist.

**Konfigurieren Sie `<distributionManagement>`** (wenn Sie an ein Remote-Repository bereitstellen):

```xml
<distributionManagement>
    <repository>
        <id>releases</id>
        <url>http://my-repository-manager/releases</url>
    </repository>
    <snapshotRepository>
        <id>snapshots</id>
        <url>http://my-repository-manager/snapshots</url>
    </snapshotRepository>
</distributionManagement>
```

- Ersetzen Sie die URLs durch die Adressen Ihres Repository-Managers (z.B. Nexus, Artifactory).
- Stellen Sie sicher, dass die Anmeldeinformationen in Ihrer `~/.m2/settings.xml`-Datei unter `<servers>` mit den entsprechenden `id`s eingerichtet sind.

#### 6. Überprüfen Sie den Release

Nach `release:perform` überprüfen Sie den Release:

- Überprüfen Sie Ihren Repository-Manager, um sicherzustellen, dass die Artefakte (z.B. JARs, Quellen) bereitgestellt wurden.
- Testen Sie die freigegebene Version in einem anderen Projekt, indem Sie sie als Abhängigkeit in dessen POM hinzufügen.

---

### Zusätzliche Konfiguration und Tipps

#### Fehlerbehebung

- **Bereinigung**: Wenn der Release-Prozess fehlschlägt, verwenden Sie:
  ```bash
  mvn release:clean
  ```
  um temporäre Dateien zu entfernen, die vom Plugin erstellt wurden.
- **Rückgängigmachen**: Um Änderungen rückgängig zu machen, die von `release:prepare` vorgenommen wurden:
  ```bash
  mvn release:rollback
  ```
  Seien Sie vorsichtig und überprüfen Sie, welche Änderungen rückgängig gemacht werden.

#### Mehrmodulprojekte

Für Mehrmodulprojekte aktualisiert das Plugin die Versionen in allen Modulen konsistent. Stellen Sie sicher, dass die Eltern-POM das Plugin und die SCM-Konfiguration enthält.

#### Batch-Modus für die Automatisierung

Um den Release nicht interaktiv (z.B. in einer CI/CD-Pipeline) auszuführen, verwenden Sie die `-B`-Flag und geben Sie die Versionen an:

```bash
mvn release:prepare -B -DreleaseVersion=1.0 -DdevelopmentVersion=1.1-SNAPSHOT
mvn release:perform -B
```

#### Häufige Probleme und Lösungen

- **VCS-Fehler**: Stellen Sie sicher, dass Git-Befehle (z.B. `git commit`, `git push`) manuell funktionieren. Überprüfen Sie die Authentifizierung (SSH-Schlüssel, Tokens).
- **Build-Fehler**: Stellen Sie sicher, dass der Build lokal erfolgreich ist (`mvn clean install`) und die Abhängigkeiten korrekt aufgelöst werden.
- **Versionsstrategie**: Passen Sie die Versionen während der Abfragen oder über Eigenschaften an, wenn die Standardeinstellungen nicht Ihren Anforderungen entsprechen.

---

### Zusammenfassung der Befehle

1. **Bereiten Sie den Release vor**:
   ```bash
   mvn release:prepare
   ```
2. **Führen Sie den Release durch**:
   ```bash
   mvn release:perform
   ```
3. **Optionaler Trockenlauf**:
   ```bash
   mvn release:prepare -DdryRun=true
   ```
4. **Bereinigung oder Rückgängigmachen bei Bedarf**:
   ```bash
   mvn release:clean
   mvn release:rollback
   ```

---

### Fazit

Das Maven Release Plugin vereinfacht den Release-Prozess, indem es die Versionsverwaltung, die VCS-Interaktionen und die Bereitstellung automatisiert. Durch Hinzufügen des Plugins zu Ihrer POM, Konfigurieren Ihres SCM und Folgen der `release:prepare` und `release:perform` Schritte können Sie Ihre Maven-Projekte effizient freigeben. Testen Sie Ihre Konfiguration immer mit einem Trockenlauf und überprüfen Sie die Ergebnisse, um einen reibungslosen Release-Prozess zu gewährleisten.