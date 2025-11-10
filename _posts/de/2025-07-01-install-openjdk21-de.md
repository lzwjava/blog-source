---
audio: false
generated: true
lang: de
layout: post
title: Aktualisierung auf OpenJDK 21 unter macOS
translated: true
type: note
---

Da Sie derzeit OpenJDK 17 über Homebrew auf Ihrem macOS-System installiert haben, finden Sie hier eine kurze Anleitung zur Installation von OpenJDK 21, welches zum aktuellen Datum, dem 1. Juli 2025, die neueste Long-Term-Support (LTS)-Version ist. Sie können OpenJDK 21 parallel zu OpenJDK 17 installieren und bei Bedarf zwischen ihnen wechseln. Die einfachste Methode ist die Verwendung von Homebrew, aber ich werde auch eine Option für die manuelle Installation bereitstellen.

### Methode 1: OpenJDK 21 mit Homebrew installieren (Empfohlen)
Homebrew ist, wie Ihre aktuelle Java-Version anzeigt, bereits auf Ihrem System installiert. Dies ist der einfachste und wartungsfreundlichste Ansatz.

1. **Homebrew aktualisieren**:
   Stellen Sie sicher, dass Homebrew auf dem neuesten Stand ist, um die neuesten Pakete zu erhalten:
   ```bash
   brew update
   ```

2. **OpenJDK 21 installieren**:
   Homebrew bietet eine spezifische Formel für OpenJDK 21. Führen Sie den folgenden Befehl aus:
   ```bash
   brew install openjdk@21
   ```
   Dies installiert OpenJDK 21 auf eine "keg-only" Weise, was bedeutet, dass es nicht in `/usr/local/bin` symbolisch verlinkt wird, um Konflikte mit anderen Java-Versionen zu vermeiden.

3. **OpenJDK 21 zu Ihrem Pfad (PATH) hinzufügen**:
   Um OpenJDK 21 zu verwenden, müssen Sie es zum SYSTEM-PATH Ihres Systems hinzufügen. Homebrew gibt nach der Installation Anweisungen aus, aber typischerweise können Sie es temporär oder permanent verlinken:
   - **Temporär (für die aktuelle Sitzung)**:
     ```bash
     export PATH="/opt/homebrew/opt/openjdk@21/bin:$PATH"
     ```
   - **Permanent (zur Shell-Konfigurationsdatei hinzufügen)**:
     Öffnen Sie Ihre Shell-Konfigurationsdatei (wahrscheinlich `~/.zshrc`, da macOS standardmäßig Zsh verwendet):
     ```bash
     nano ~/.zshrc
     ```
     Fügen Sie die folgende Zeile hinzu:
     ```bash
     export PATH="/opt/homebrew/opt/openjdk@21/bin:$PATH"
     ```
     Speichern und schließen Sie die Datei, und wenden Sie die Änderungen an:
     ```bash
     source ~/.zshrc
     ```

4. **JAVA_HOME setzen**:
   Um sicherzustellen, dass Java-Anwendungen OpenJDK 21 finden können, setzen Sie die `JAVA_HOME`-Umgebungsvariable:
   ```bash
   export JAVA_HOME=$(/usr/libexec/java_home -v 21)
   ```
   Fügen Sie dies für eine dauerhafte Lösung Ihrer `~/.zshrc` hinzu:
   ```bash
   echo 'export JAVA_HOME=$(/usr/libexec/java_home -v 21)' >> ~/.zshrc
   source ~/.zshrc
   ```

5. **Installation überprüfen**:
   Überprüfen Sie, ob OpenJDK 21 installiert und aktiv ist:
   ```bash
   java -version
   ```
   Sie sollten eine Ausgabe ähnlich der folgenden sehen:
   ```
   openjdk 21.0.1 2023-10-17
   OpenJDK Runtime Environment (build 21.0.1+12)
   OpenJDK 64-Bit Server VM (build 21.0.1+12, mixed mode, sharing)
   ```

6. **Zwischen Java-Versionen wechseln**:
   Da Sie OpenJDK 17 installiert haben, können Sie mit `/usr/libexec/java_home` zwischen den Versionen wechseln. Zum Beispiel:
   - Um OpenJDK 17 zu verwenden:
     ```bash
     export JAVA_HOME=$(/usr/libexec/java_home -v 17)
     ```
   - Um OpenJDK 21 zu verwenden:
     ```bash
     export JAVA_HOME=$(/usr/libexec/java_home -v 21)
     ```
   Alternativ können Sie zur einfacheren Verwaltung einen Versionsmanager wie `jenv` verwenden (Installation via `brew install jenv`):
   ```bash
   jenv add /Library/Java/JavaVirtualMachines/openjdk-21.jdk/Contents/Home
   jenv add /Library/Java/JavaVirtualMachines/openjdk-17.jdk/Contents/Home
   jenv enable-plugin export
   jenv global 21
   ```

### Methode 2: Manuelle Installation
Wenn Sie Homebrew nicht verwenden möchten, können Sie OpenJDK 21 manuell installieren.

1. **OpenJDK 21 herunterladen**:
   - Besuchen Sie die offizielle OpenJDK-Website (jdk.java.net/21) oder einen vertrauenswürdigen Anbieter wie Oracle, Azul oder Adoptium.
   - Für Apple Silicon (M1/M2) laden Sie die `macOS/AArch64` tar.gz-Datei herunter. Für Intel-basierte Macs wählen Sie `macOS/x64`.
   - Beispiel: Von Oracles JDK 21 Download-Seite wählen Sie die ARM64 oder x64 tar.gz-Datei.

2. **Download überprüfen**:
   Überprüfen Sie die Integrität der heruntergeladenen Datei mit ihrem SHA256-Prüfsumme:
   ```bash
   shasum -a 256 openjdk-21.0.1_macos-aarch64_bin.tar.gz
   ```
   Vergleichen Sie die Ausgabe mit der auf der Download-Seite angegebenen Prüfsumme.

3. **Datei entpacken**:
   Entpacken Sie die tar.gz-Datei in ein gewünschtes Verzeichnis, zum Beispiel Ihr Home-Verzeichnis:
   ```bash
   tar -xf openjdk-21.0.1_macos-aarch64_bin.tar.gz -C ~/OpenJDK
   ```
   Das JDK wird nach `~/OpenJDK/jdk-21.0.1.jdk/Contents/Home` extrahiert.

4. **In Systemverzeichnis verschieben** (Optional):
   Der Konsistenz halber können Sie das JDK in das standardmäßige macOS-Java-Verzeichnis verschieben:
   ```bash
   sudo mv ~/OpenJDK/jdk-21.0.1.jdk /Library/Java/JavaVirtualMachines/
   ```

5. **JAVA_HOME und PATH setzen**:
   Aktualisieren Sie Ihre `~/.zshrc` mit:
   ```bash
   export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk-21.0.1.jdk/Contents/Home
   export PATH=$JAVA_HOME/bin:$PATH
   ```
   Wenden Sie die Änderungen an:
   ```bash
   source ~/.zshrc
   ```

6. **Installation überprüfen**:
   Bestätigen Sie die Installation:
   ```bash
   java -version
   ```
   Stellen Sie sicher, dass OpenJDK 21 angezeigt wird.

### Hinweise
- **Apple Silicon Kompatibilität**: Stellen Sie sicher, dass Sie den AArch64 Build für M1/M2 Macs herunterladen, um Leistungsprobleme zu vermeiden. Homebrew wählt automatisch die richtige Architektur aus.
- **Mehrere JDKs**: macOS unterstützt mehrere JDKs in `/Library/Java/JavaVirtualMachines/`. Verwenden Sie `/usr/libexec/java_home -v <version>`, um zwischen ihnen zu wechseln.
- **Vorteil von Homebrew**: Homebrew vereinfacht Updates (`brew upgrade openjd@21`) und gewährleistet die Kompatibilität mit Ihrem System.
- **Alternative Anbieter**: Sie können auch Azul Zulu oder Eclipse Temurin Builds von OpenJDK 21 verwenden, die auf deren jeweiligen Websites verfügbar sind (z.B. azul.com oder adoptium.net).

Wenn Sie auf Probleme stoßen, lassen Sie es mich wissen, und ich kann bei der Fehlerbehebung helfen.