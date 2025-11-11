---
audio: false
generated: true
lang: de
layout: post
title: Installationsquelle von npm-Paketen
translated: true
type: note
---

Um die Installationsquelle des Pakets `@ngx-formly/bootstrap` von einer lokalen `.tgz`-Datei auf die npm-Registry zu ändern, befolgen Sie diese Schritte:

### 1. Deinstallieren Sie das lokal installierte Paket
Da Sie `@ngx-formly/bootstrap` zuvor von einer lokalen `.tgz`-Datei installiert haben, befindet es sich derzeit in Ihrem `node_modules`-Verzeichnis des Projekts. Um es zu entfernen, führen Sie den folgenden Befehl in Ihrem Terminal aus:

```bash
npm uninstall @ngx-formly/bootstrap
```

Dieser Befehl entfernt das Paket aus `node_modules`. Wenn das Paket manuell zu Ihrer `package.json`-Datei unter `dependencies` oder `devDependencies` hinzugefügt wurde, wird es auch von dort entfernt. Wenn es nicht in `package.json` aufgeführt war (was häufig der Fall ist, wenn es von einer `.tgz`-Datei ohne Speichern installiert wird), wird es dennoch aus Ihrem Projekt entfernt.

### 2. Installieren Sie das Paket aus der npm-Registry
Installieren Sie nun das Paket aus der npm-Registry, indem Sie ausführen:

```bash
npm install @ngx-formly/bootstrap
```

Dieser Befehl holt die neueste Version von `@ngx-formly/bootstrap` aus der npm-Registry (typischerweise `https://registry.npmjs.org/`, es sei denn, Sie haben eine andere Registry konfiguriert) und installiert es in Ihr `node_modules`-Verzeichnis. Es wird das Paket auch standardmäßig (in neueren npm-Versionen) zu Ihrer `package.json`-Datei unter `dependencies` hinzufügen, um sicherzustellen, dass es als Teil Ihres Projekts verfolgt wird.

### Optional: Überprüfen Sie die Registry (falls nötig)
Wenn Sie Ihre npm-Registry zuvor geändert haben und sicherstellen möchten, dass sie auf die Standard-npm-Registry eingestellt ist, können Sie dies mit folgendem Befehl überprüfen:

```bash
npm config get registry
```

Wenn die Ausgabe `https://registry.npmjs.org/` lautet, verwenden Sie die Standard-Registry und der `npm install`-Befehl funktioniert wie erwartet. Wenn sie auf eine andere Registry eingestellt ist und Sie zur Standard-Registry zurückkehren möchten, führen Sie aus:

```bash
npm config set registry https://registry.npmjs.org/
```

Da Sie jedoch bereits erwähnt haben, dass Sie Ihre Registry konfiguriert haben, ist dieser Schritt möglicherweise nicht notwendig.

### Hinweise
- **Versionskontrolle**: Wenn Sie die gleiche Version wie die in Ihrer `.tgz`-Datei benötigen, überprüfen Sie die Versionsnummer in `node_modules/@ngx-formly/bootstrap/package.json` vor der Deinstallation. Installieren Sie dann diese spezifische Version mit:
  ```bash
  npm install @ngx-formly/bootstrap@<Version>
  ```
  Wenn Sie keine Version angeben, wird die neueste Version aus der Registry installiert.
- **Abhängigkeitstyp**: Wenn Sie das Paket als Entwicklungsabhängigkeit anstelle einer regulären Abhängigkeit wünschen, verwenden Sie:
  ```bash
  npm install @ngx-formly/bootstrap --save-dev
  ```

Indem Sie diese Schritte befolgen, wechseln Sie `@ngx-formly/bootstrap` erfolgreich von einer Installation über eine lokale `.tgz`-Datei zu einer Installation aus der npm-Registry.