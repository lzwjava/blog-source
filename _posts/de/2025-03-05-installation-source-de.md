---
audio: false
generated: true
lang: de
layout: post
title: Installationsquelle von npm-Paketen
translated: true
---

Um die Installationsquelle des `@ngx-formly/bootstrap`-Pakets von einer lokalen `.tgz`-Datei auf das npm-Repository zu ändern, befolgen Sie diese Schritte:

### 1. Lokales Paket deinstallieren
Da Sie `@ngx-formly/bootstrap` zuvor aus einer lokalen `.tgz`-Datei installiert haben, befindet es sich derzeit im `node_modules`-Verzeichnis Ihres Projekts. Um es zu entfernen, führen Sie den folgenden Befehl in Ihrem Terminal aus:

```bash
npm uninstall @ngx-formly/bootstrap
```

Dieser Befehl entfernt das Paket aus `node_modules`. Wenn das Paket manuell zu Ihrer `package.json`-Datei unter `dependencies` oder `devDependencies` hinzugefügt wurde, wird es auch von dort entfernt. Wenn es nicht in `package.json` aufgelistet war (häufig, wenn es aus einer `.tgz`-Datei ohne Speichern installiert wurde), wird es dennoch aus Ihrem Projekt entfernt.

### 2. Paket aus dem npm-Repository installieren
Installieren Sie nun das Paket aus dem npm-Repository, indem Sie Folgendes ausführen:

```bash
npm install @ngx-formly/bootstrap
```

Dieser Befehl lädt die neueste Version von `@ngx-formly/bootstrap` aus dem npm-Repository (normalerweise `https://registry.npmjs.org/` es sei denn, Sie haben ein anderes Repository konfiguriert) und installiert es in Ihr `node_modules`-Verzeichnis. Es wird auch das Paket zu Ihrer `package.json`-Datei unter `dependencies` hinzufügen (standardmäßig in neueren npm-Versionen), sodass es als Teil Ihres Projekts verfolgt wird.

### Optional: Registry überprüfen (falls erforderlich)
Wenn Sie zuvor Ihr npm-Repository geändert haben und sicherstellen möchten, dass es auf das Standard-npm-Repository gesetzt ist, können Sie dies mit Folgendem überprüfen:

```bash
npm config get registry
```

Wenn die Ausgabe `https://registry.npmjs.org/` lautet, verwenden Sie das Standard-Repository und der `npm install`-Befehl wird wie erwartet funktionieren. Wenn es auf ein anderes Repository gesetzt ist und Sie es auf das Standard-Repository zurücksetzen möchten, führen Sie Folgendes aus:

```bash
npm config set registry https://registry.npmjs.org/
```

Da Sie jedoch erwähnt haben, dass Sie Ihr Repository bereits konfiguriert haben, ist dieser Schritt möglicherweise nicht erforderlich.

### Hinweise
- **Versionskontrolle**: Wenn Sie die gleiche Version wie die in Ihrer `.tgz`-Datei benötigen, überprüfen Sie die Versionsnummer in `node_modules/@ngx-formly/bootstrap/package.json` vor dem Deinstallieren. Installieren Sie dann diese spezifische Version mit:
  ```bash
  npm install @ngx-formly/bootstrap@<version>
  ```
  Wenn Sie keine Version angeben, wird die neueste Version aus dem Repository installiert.
- **Abhängigkeitstyp**: Wenn Sie das Paket als Entwicklungsabhängigkeit anstelle einer regulären Abhängigkeit möchten, verwenden Sie:
  ```bash
  npm install @ngx-formly/bootstrap --save-dev
  ```

Durch die Befolgung dieser Schritte wechseln Sie `@ngx-formly/bootstrap` erfolgreich von der Installation über eine lokale `.tgz`-Datei zur Installation aus dem npm-Repository.