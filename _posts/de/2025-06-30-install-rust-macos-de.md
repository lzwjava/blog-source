---
audio: false
generated: true
lang: de
layout: post
title: Rust unter macOS mit rustup installieren
translated: true
type: note
---

## Rust mit rustup installieren

1. **Terminal öffnen**  
    Sie finden Terminal unter **Programme > Dienstprogramme** oder suchen Sie danach mit Spotlight.

2. **rustup und Rust installieren**  
    Führen Sie den folgenden Befehl aus, um das rustup-Installationsskript herunterzuladen und auszuführen:

    ```sh
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
    ```

    Das Skript wird Sie zur Fortsetzung auffordern. Drücken Sie `1` für die Standardinstallation.

3. **Ihre Shell konfigurieren**  
    Nach der Installation müssen Sie Rust möglicherweise zum System-`PATH` hinzufügen. Der Installer bietet einen ähnlichen Befehl an:

    ```sh
    source $HOME/.cargo/env
    ```

    Fügen Sie diese Zeile zu Ihrer Shell-Konfigurationsdatei hinzu (z.B. `.zshrc`, `.bashrc` oder `.bash_profile`), um Rust in zukünftigen Sitzungen verfügbar zu machen.

4. **Installation überprüfen**  
    Überprüfen Sie, ob Rust korrekt installiert wurde:

    ```sh
    rustc --version
    ```

    Sie sollten die Version des Rust-Compilers sehen, wenn die Installation erfolgreich war.

---

## Rust mit Homebrew installieren

Alternativ können Sie [Homebrew](https://brew.sh/) verwenden, um Rust zu installieren, obwohl `rustup` generell für einfachere Updates und Versionsverwaltung empfohlen wird.

1. **Homebrew installieren** (falls noch nicht installiert):

    ```sh
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```

2. **Rust mit Homebrew installieren**:

    ```sh
    brew install rust
    ```

3. **Installation überprüfen**:

    ```sh
    rustc --version
    ```

---

## Rust-Code kompilieren

1. **Ein Rust-Programm schreiben**  
    Erstellen Sie eine Datei namens `main.rs` mit folgendem Inhalt:

    ```rust
    fn main() {
         println!("Hello, World!");
    }
    ```

2. **Das Programm kompilieren**  
    Navigieren Sie im Terminal zu dem Verzeichnis, das Ihre Datei enthält, und führen Sie aus:

    ```sh
    rustc main.rs
    ```

3. **Das kompilierte Programm ausführen**:

    ```sh
    ./main
    ```

---

Dieses Setup sollte Ihnen den Einstieg in die Rust-Entwicklung auf macOS ermöglichen. Wenn Sie Probleme haben, fragen Sie gerne!