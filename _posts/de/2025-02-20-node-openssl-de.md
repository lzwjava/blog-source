---
audio: false
generated: false
lang: de
layout: post
title: Node.js OpenSSL-Kompatibilität
translated: true
type: note
---

Beim Ausführen von `ng build` mit **Node.js 22.9.0** und **npm 10.8.3** tritt folgender Fehler auf:

```
error 0308010C digital envelope routines::unsupported
```

Dieser Fehler tritt typischerweise aufgrund eines Kompatibilitätsproblems zwischen neueren Node.js-Versionen (wie 22.9.0, die OpenSSL 3.0 oder höher verwendet) und bestimmten kryptographischen Algorithmen auf, die von Tools wie Webpack (das Angular intern verwendet) genutzt werden. Nachfolgend finden Sie eine Schritt-für-Schritt-Anleitung zur Behebung des Problems.

---

### Lösung

#### Schritt 1: OpenSSL Legacy Provider aktivieren
Die einfachste und schnellste Lösung ist die Aktivierung des OpenSSL Legacy Providers durch Setzen der Umgebungsvariable `NODE_OPTIONS`. Dies erlaubt es Node.js, ältere kryptographische Algorithmen zu verwenden, die in OpenSSL 3.0+ standardmäßig möglicherweise nicht mehr unterstützt werden.

- **Für macOS/Linux**:
  Öffnen Sie Ihr Terminal und führen Sie aus:
  ```bash
  export NODE_OPTIONS=--openssl-legacy-provider
  ng build
  ```

- **Für Windows (Command Prompt)**:
  Öffnen Sie die Eingabeaufforderung und führen Sie aus:
  ```cmd
  set NODE_OPTIONS=--openssl-legacy-provider
  ng build
  ```

- **Für Windows (PowerShell)**:
  Öffnen Sie PowerShell und führen Sie aus:
  ```powershell
  $env:NODE_OPTIONS="--openssl-legacy-provider"
  ng build
  ```

Nachdem Sie die Umgebungsvariable gesetzt haben, führen Sie `ng build` erneut aus. Dies sollte den Fehler in den meisten Fällen beheben, indem Node.js in die Lage versetzt wird, die nicht unterstützten Routinen zu verarbeiten.

---

#### Schritt 2: Angular CLI überprüfen und aktualisieren (falls nötig)
Wenn der Fehler nach Schritt 1 weiterhin besteht, ist Ihre Version der Angular CLI möglicherweise nicht vollständig mit Node.js 22.9.0 kompatibel. Ein Update auf die neueste Version kann helfen.

- Überprüfen Sie Ihre aktuelle Angular CLI-Version:
  ```bash
  ng --version
  ```

- Aktualisieren Sie die Angular CLI global:
  ```bash
  npm install -g @angular/cli
  ```

- Versuchen Sie anschließend, `ng build` erneut auszuführen.

---

#### Schritt 3: Projektabhängigkeiten überprüfen und aktualisieren (Optional)
Wenn das Problem immer noch nicht behoben ist, könnten veraltete Abhängigkeiten in Ihrem Projekt die Ursache sein. Gehen Sie wie folgt vor:

- Öffnen Sie Ihre `package.json`-Datei und überprüfen Sie die Versionen Ihrer Abhängigkeiten (z.B. `@angular/core`, `@angular/cli`, etc.).
- Aktualisieren Sie diese sorgfältig auf ihre neuesten kompatiblen Versionen:
  ```bash
  npm install
  ```
  oder, wenn Sie alle Abhängigkeiten aktualisieren möchten:
  ```bash
  npm update
  ```

- Führen Sie `ng build` erneut aus, um zu testen.

*Hinweis*: Seien Sie vorsichtig bei Updates, da diese Breaking Changes einführen könnten. Testen Sie Ihre Anwendung anschließend gründlich.

---

#### Schritt 4: Node.js downgraden (Letzter Ausweg)
Wenn keine der oben genannten Lösungen funktioniert, wird Node.js 22.9.0 von der aktuellen Konfiguration Ihres Projekts möglicherweise noch nicht vollständig unterstützt. Ein Downgrade auf eine Long-Term Support (LTS) Version von Node.js, wie **20.x** oder **18.x**, könnte das Problem lösen.

- Deinstallieren Sie Ihre aktuelle Node.js-Version.
- Laden Sie eine LTS-Version von der [offiziellen Node.js-Website](https://nodejs.org/) herunter und installieren Sie sie.
- Überprüfen Sie die installierte Version:
  ```bash
  node -v
  ```
- Installieren Sie Ihre Projektabhängigkeiten neu:
  ```bash
  npm install
  ```
- Führen Sie `ng build` erneut aus.

---

### Empfohlener Ansatz
Beginnen Sie mit **Schritt 1** (Setzen von `NODE_OPTIONS`), da dies die schnellste Lösung ist und Ihnen erlaubt, Node.js 22.9.0 weiterzuverwenden. Falls das nicht funktioniert, fahren Sie mit **Schritt 2** und **Schritt 3** fort. Verwenden Sie **Schritt 4** nur bei Bedarf, da ein Downgrade von Node.js den Zugriff auf neuere Funktionen einschränken könnte.

Dies sollte den Fehler "error 0308010C digital envelope routines::unsupported" beheben und Ihren `ng build`-Befehl wieder zum Laufen bringen!