---
audio: false
generated: true
lang: de
layout: post
title: Maven-Kompilierung vor Git-Commit
translated: true
type: note
---

Ja, Sie können `mvn compile` in einem lokalen Git-Repository ausführen, bevor Sie `git commit` ausführen. Hier ist eine kurze Erklärung und die Schritte:

1. **Stellen Sie sicher, dass Maven installiert ist**: Vergewissern Sie sich, dass Maven auf Ihrem System installiert und konfiguriert ist (überprüfen Sie mit `mvn -version`).

2. **Navigieren Sie zu Ihrem Git-Repository**: Verwenden Sie `cd pfad/zu/ihrem/repo`, um zu Ihrem lokalen Git-Repository mit dem Maven-Projekt (mit einer `pom.xml`-Datei) zu gelangen.

3. **Führen Sie Maven Compile aus**: Führen Sie `mvn compile` aus, um Ihren Java-Code zu kompilieren. Dies wird:
   - Den Quellcode in `src/main/java` kompilieren.
   - Die kompilierten Klassen in `target/classes` ablegen.
   - Etwaige Kompilierungsfehler melden.

4. **Überprüfen Sie den Kompilierungsstatus**:
   - Wenn `mvn compile` erfolgreich ist (endet mit `BUILD SUCCESS`), können Sie mit den Git-Operationen fortfahren.
   - Wenn es fehlschlägt (z.B. aufgrund von Syntaxfehlern), beheben Sie den Code, bevor Sie committen.

5. **Git-Workflow**:
   - Änderungen vorbereiten (stagen): `git add .` (oder bestimmte Dateien).
   - Änderungen committen: `git commit -m "Ihr Commit-Kommentar"`.

### Optional: Automatisieren mit Git Hooks
Um sicherzustellen, dass `mvn compile` vor jedem `git commit` ausgeführt wird, können Sie einen Git Pre-Commit Hook verwenden:
1. Navigieren Sie zu `.git/hooks` in Ihrem Repository.
2. Erstellen oder bearbeiten Sie die Datei `pre-commit` (ohne Dateierweiterung).
3. Fügen Sie ein Skript wie folgt hinzu:
   ```bash
   #!/bin/sh
   mvn compile
   if [ $? -ne 0 ]; then
       echo "Kompilierung fehlgeschlagen, Commit abgebrochen."
       exit 1
   fi
   ```
4. Machen Sie es ausführbar: `chmod +x .git/hooks/pre-commit`.
   - Jetzt wird `git commit` nur fortgesetzt, wenn `mvn compile` erfolgreich ist.

### Hinweise
- **Abhängigkeiten**: Stellen Sie sicher, dass `pom.xml` korrekt konfiguriert ist und die Abhängigkeiten heruntergeladen wurden (verwenden Sie bei Bedarf `mvn dependency:resolve`).
- **Leistung**: Das Ausführen von `mvn compile` vor jedem Commit stellt die Codequalität sicher, kann aber Ihren Workflow bei großen Projekten verlangsamen.
- **Alternative Befehle**: Wenn Sie Tests einbeziehen möchten, verwenden Sie `mvn test` anstelle von `mvn compile`, um den Code zu kompilieren und Unit-Tests auszuführen.

Dieser Ansatz stellt sicher, dass Ihr Code erfolgreich kompiliert, bevor Sie ihn in das Git-Repository committen.