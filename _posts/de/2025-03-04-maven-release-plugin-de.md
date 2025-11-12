---
audio: false
generated: true
lang: de
layout: post
title: Maven Release Plugin
translated: true
type: note
---

Hier ist eine umfassende Anleitung zur Verwendung des **Maven Release Plugins**, um den Release-Prozess für Ihr Maven-Projekt zu verwalten und zu automatisieren.

---

### Was ist das Maven Release Plugin?

Das **Maven Release Plugin** ist ein Tool, das den Prozess der Veröffentlichung eines Maven-Projekts automatisiert. Es übernimmt Aufgaben wie:

- Aktualisieren von Versionsnummern in der POM-Datei Ihres Projekts.
- Committen von Änderungen in Ihrem Versionskontrollsystem (VCS), wie z. B. Git.
- Erstellen eines Tags für das Release im VCS.
- Bauen und Bereitstellen der Release-Artefakte.
- Vorbereiten des Projekts für den nächsten Entwicklungszyklus durch erneutes Aktualisieren der Versionsnummern.

Die beiden primären Ziele des Plugins sind:

- **`release:prepare`**: Bereitet das Projekt auf ein Release vor, indem Versionen aktualisiert, Änderungen committet und das Release im VCS getaggt wird.
- **`release:perform`**: Baut die freigegebene Version und stellt sie bereit, indem der getaggte Code aus dem VCS verwendet wird.

---

### Schritt-für-Schritt-Anleitung zur Verwendung des Maven Release Plugins

#### 1. Fügen Sie das Maven Release Plugin zu Ihrer POM-Datei hinzu

Um das Plugin zu verwenden, müssen Sie es im Abschnitt `<build><plugins>` Ihrer `pom.xml` hinzufügen:

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

**Hinweis**: Überprüfen Sie die [offizielle Maven Release Plugin Seite](https://maven.apache.org/maven-release/maven-release-plugin/) auf die neueste Version und ersetzen Sie `2.5.3` entsprechend.

#### 2. Konfigurieren Sie den SCM-Abschnitt (Source Control Management)

Das Plugin interagiert mit Ihrem VCS (z. B. Git), um Änderungen zu committen und Tags zu erstellen. Sie müssen Ihre VCS-Details im `<scm>`-Abschnitt Ihrer `pom.xml` angeben. Für ein Git-Repository, das auf GitHub gehostet wird, könnte dies wie folgt aussehen:

```xml
<scm>
    <connection>scm:git:git://github.com/username/project.git</connection>
    <developerConnection>scm:git:git@github.com:username/project.git</developerConnection>
    <url>https://github.com/username/project</url>
</scm>
```

- Ersetzen Sie `username` und `project` durch Ihren tatsächlichen GitHub-Benutzernamen und Repository-Namen.
- Passen Sie die URLs an, wenn Sie einen anderen Git-Hosting-Dienst verwenden (z. B. GitLab, Bitbucket).
- Stellen Sie sicher, dass die notwendigen Anmeldeinformationen (z. B. SSH-Schlüssel oder ein persönlicher Zugriffstoken) konfiguriert sind, um Änderungen an das Repository zu pushen.

#### 3. Bereiten Sie Ihr Projekt auf das Release vor

Bevor Sie die Release-Befehle ausführen, stellen Sie sicher, dass Ihr Projekt bereit ist:

- Alle Tests sind erfolgreich (`mvn test`).
- Es gibt keine uncommitteten Änderungen in Ihrem Arbeitsverzeichnis (führen Sie `git status` aus, um dies zu überprüfen).
- Sie befinden sich auf dem korrekten Branch (z. B. `master` oder `main`) für das Release.

#### 4. Führen Sie `release:prepare` aus

Das `release:prepare`-Ziel bereitet Ihr Projekt auf das Release vor. Führen Sie den folgenden Befehl in Ihrem Terminal aus:

```bash
mvn release:prepare
```

**Was passiert während `release:prepare`**:

- **Prüfung auf uncommittete Änderungen**: Stellt sicher, dass Ihr Arbeitsverzeichnis sauber ist.
- **Abfrage der Versionen**: Fragt nach der Release-Version und der nächsten Entwicklungsversion.
  - Beispiel: Wenn Ihre aktuelle Version `1.0-SNAPSHOT` ist, schlägt es möglicherweise `1.0` für das Release und `1.1-SNAPSHOT` für die nächste Entwicklungsversion vor. Sie können die Standardwerte akzeptieren oder benutzerdefinierte Versionen eingeben (z. B. `1.0.1` für ein Patch-Release).
- **Aktualisiert POM-Dateien**: Ändert die Version auf die Release-Version (z. B. `1.0`), committet die Änderung und taggt sie im VCS (z. B. `project-1.0`).
- **Bereitet den nächsten Zyklus vor**: Aktualisiert die POM auf die nächste Entwicklungsversion (z. B. `1.1-SNAPSHOT`) und committet sie.

**Optionaler Probelauf**: Um den Prozess zu testen, ohne Änderungen vorzunehmen, verwenden Sie:

```bash
mvn release:prepare -DdryRun=true
```

Dies simuliert die Vorbereitungsschritte ohne Commit oder Tag.

#### 5. Führen Sie `release:perform` aus

Nachdem das Release vorbereitet wurde, bauen und stellen Sie es mit folgendem Befehl bereit:

```bash
mvn release:perform
```

**Was passiert während `release:perform`**:

- Checkout der getaggten Version aus dem VCS.
- Baut das Projekt.
- Stellt die Artefakte in dem Repository bereit, das im `<distributionManagement>`-Abschnitt Ihrer POM angegeben ist.

**Konfigurieren Sie `<distributionManagement>`** (falls die Bereitstellung in einem Remote-Repository erfolgt):

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

- Ersetzen Sie die URLs durch die Adressen Ihres Repository-Managers (z. B. Nexus, Artifactory).
- Stellen Sie sicher, dass die Anmeldeinformationen in Ihrer `~/.m2/settings.xml`-Datei unter `<servers>` mit den entsprechenden `id`s eingerichtet sind.

#### 6. Überprüfen Sie das Release

Überprüfen Sie nach `release:perform` das Release:

- Prüfen Sie in Ihrem Repository-Manager, ob die Artefakte (z. B. JARs, Quellcode) bereitgestellt wurden.
- Testen Sie die freigegebene Version in einem anderen Projekt, indem Sie sie als Abhängigkeit in dessen POM hinzufügen.

---

### Zusätzliche Konfiguration und Tipps

#### Umgang mit Fehlern

- **Bereinigung**: Wenn der Release-Prozess fehlschlägt, verwenden Sie:
  ```bash
  mvn release:clean
  ```
  um die vom Plugin erstellten temporären Dateien zu entfernen.
- **Rückgängig machen**: Um die durch `release:prepare` vorgenommenen Änderungen rückgängig zu machen:
  ```bash
  mvn release:rollback
  ```
  Seien Sie vorsichtig und überprüfen Sie, welche Änderungen rückgängig gemacht werden.

#### Multi-Modul-Projekte

Für Multi-Modul-Projekte aktualisiert das Plugin standardmäßig konsistent die Versionen über alle Module hinweg. Stellen Sie sicher, dass die Parent-POM das Plugin und die SCM-Konfiguration enthält.

#### Batch-Modus für Automatisierung

Um das Release nicht-interaktiv auszuführen (z. B. in einer CI/CD-Pipeline), verwenden Sie das `-B`-Flag und geben Sie die Versionen an:

```bash
mvn release:prepare -B -DreleaseVersion=1.0 -DdevelopmentVersion=1.1-SNAPSHOT
mvn release:perform -B
```

#### Häufige Probleme und Lösungen

- **VCS-Fehler**: Stellen Sie sicher, dass Git-Befehle (z. B. `git commit`, `git push`) manuell funktionieren. Überprüfen Sie die Authentifizierung (SSH-Schlüssel, Tokens).
- **Build-Fehler**: Verifizieren Sie, dass der Build lokal erfolgreich ist (`mvn clean install`) und Abhängigkeiten korrekt aufgelöst werden.
- **Versionsstrategie**: Passen Sie die Versionen während der Abfragen oder über Eigenschaften an, wenn die Standardwerte nicht Ihren Anforderungen entsprechen.

---

### Befehlsübersicht

1. **Release vorbereiten**:
   ```bash
   mvn release:prepare
   ```
2. **Release durchführen**:
   ```bash
   mvn release:perform
   ```
3. **Optionaler Probelauf**:
   ```bash
   mvn release:prepare -DdryRun=true
   ```
4. **Bereinigung oder Rückgängigmachen bei Bedarf**:
   ```bash
   mvn release:clean
   mvn release:rollback
   ```

---

### Schlussfolgerung

Das Maven Release Plugin vereinfacht den Release-Prozess durch die Automatisierung von Versionsverwaltung, VCS-Interaktionen und Bereitstellung. Indem Sie das Plugin zu Ihrer POM hinzufügen, Ihren SCM konfigurieren und die Schritte `release:prepare` und `release:perform` befolgen, können Sie Ihre Maven-Projekte effizient veröffentlichen. Testen Sie Ihre Konfiguration immer mit einem Probelauf und überprüfen Sie die Ergebnisse, um einen reibungslosen Release-Prozess zu gewährleisten.