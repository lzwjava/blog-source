---
audio: false
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: Einrichtung des Remote-Debuggings in IntelliJ
translated: true
type: note
---

Kurze Antwort: ja – wenn Sie den Build und die laufende JVM synchron halten, wird sich der IntelliJ-Remote-Debugger sauber verbinden. Hier ist eine solide, unkomplizierte Methode, die sowohl lokal mit Liberty als auch mit Cloud Foundry funktioniert.

## 1) Verhindern Sie "Class Mismatch", bevor Sie sich verbinden

* Immer JDKs abstimmen: Die von der Maven-Kompilierung, der Liberty-JVM und (falls auf CF) dem JDK des Java Buildpacks verwendeten JDKs müssen in der Hauptversion übereinstimmen. In Maven können Sie es mit dem `maven-compiler-plugin` (`release` oder `source/target`) festlegen und sicherstellen, dass Liberty/CF dasselbe verwendet.
* Bereinigen Sie veralteten Bytecode beim Wechsel von Branches oder beim (De-)Aktivieren von Modulen: `mvn clean package -DskipTests` ist die einfachste Absicherung.
* Führen Sie in IntelliJ auch einmal "Rebuild Project" aus, wenn Sie zuvor IDE-Build und Maven-Build gemischt haben.

## 2) Automatischen Neubuild nur bei Bedarf (30-Minuten-Regel)

Wenn Sie nur dann neu bauen möchten, wenn kompilierte Klassen älter als 30 Minuten sind, können Sie Maven in eine kleine Prüfung einwickeln.

### Bash (macOS/Linux)

```bash
#!/usr/bin/env bash
set -euo pipefail

CLASSES_DIR="target/classes"
THRESHOLD_MIN=30

needs_build() {
  # no classes yet?
  [[ ! -d "$CLASSES_DIR" ]] && return 0
  # latest class mtime older than threshold?
  last_mod_epoch=$(find "$CLASSES_DIR" -type f -name '*.class' -printf '%T@\n' 2>/dev/null | sort -n | tail -1)
  [[ -z "${last_mod_epoch:-}" ]] && return 0
  now_epoch=$(date +%s)
  diff_min=$(( ( now_epoch - ${last_mod_epoch%.*} ) / 60 ))
  (( diff_min >= THRESHOLD_MIN ))
}

if needs_build; then
  echo "Classes are old (>= ${THRESHOLD_MIN}m) or missing — building…"
  mvn clean package -DskipTests
else
  echo "Classes are fresh (< ${THRESHOLD_MIN}m) — skipping build."
fi
```

### PowerShell (Windows)

```powershell
$classes = "target\classes"
$thresholdMin = 30

function Needs-Build {
  if (-not (Test-Path $classes)) { return $true }
  $last = Get-ChildItem $classes -Recurse -Filter *.class |
          Sort-Object LastWriteTime -Descending |
          Select-Object -First 1
  if (-not $last) { return $true }
  $age = (New-TimeSpan -Start $last.LastWriteTime -End (Get-Date)).TotalMinutes
  return ($age -ge $thresholdMin)
}

if (Needs-Build) {
  Write-Host "Classes are old (>= $thresholdMin m) or missing — building…"
  mvn clean package -DskipTests
} else {
  Write-Host "Classes are fresh (< $thresholdMin m) — skipping build."
}
```

## 3) Liberty (lokal) – Start im Debug-Modus und Verbindung von IntelliJ

Sie haben zwei einfache Möglichkeiten:

**A. Einmaliger Debug-Start**

```bash
server debug myServer   # default JDWP auf Port 7777
```

**B. Permanente Konfiguration**

* In `wlp/usr/servers/myServer/jvm.options`:

```
-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=*:7777
```

* Oder per Environment Variable:

```
WLP_DEBUG_ADDRESS=7777
WLP_DEBUG_SUSPEND=false
```

**IntelliJ-Verbindung**

* Run → "Edit Configurations…" → "Remote JVM Debug".
* Host: `localhost`, Port: `7777`.
* Debug drücken; Sie sollten "Connected to the target VM…" sehen und Breakpoints sollten binden.

> Tipp: Nach einem Rebuild lädt Liberty aktualisierte Klassen für die meisten Features via Hot Swap. Wenn sich eine Methodensignatur oder die Klassenstruktur geändert hat, benötigen Sie einen Server-Neustart, damit diese Änderungen geladen werden.

## 4) Cloud Foundry (PCF) – Was ist realistisch

CF führt Apps hinter seinem Routing Layer aus; Sie können typischerweise keinen JDWP-Port direkt exponieren. Sie haben zwei praktikable Ansätze:

**Option 1: Buildpack-Debugging + SSH-Tunnel (nur für Dev/Staging)**

1.  JVM-Debugging im Java Buildpack aktivieren:

    * Setzen Sie die Environment Variable vor dem Push (Namen variieren je nach Buildpack-Version):

    ```
    cf set-env <APP> JBP_CONFIG_DEBUG '{enabled: true, port: 7777}'
    ```
2.  Restagen:

    ```
    cf restage <APP>
    ```
3.  SSH-Tunnel öffnen:

    ```
    cf ssh -N -L 7777:localhost:7777 <APP>
    ```
4.  In IntelliJ, Verbindung zu `localhost:7777` herstellen.

**Option 2: Verwenden Sie CF SSH JMX/Diagnostics anstelle von JDWP**

* Wenn direkter JDWP-Zugriff nicht erlaubt ist, verlassen Sie sich auf:

  * App-Logs + gezielte Logger,
  * Thread/Heap-Dumps via `cf ssh` + `jcmd`/`jmap` (falls vorhanden),
  * Feature Flags wie Liberty's Trace und Health Endpoints.

> Realitätscheck: Viele CF-Orgs deaktivieren Debug-Ports in Prod. Betrachten Sie Remote-JDWP auf CF als einen Pfad nur für Debug-Zwecke in Non-Prod-Spaces. Falls Ihr Platform-Team dies blockiert, fallen Sie auf Logs + SSH-Diagnostics zurück.

## 5) Häufige Ursachen für "couldn't bind breakpoints" (und Lösungen)

* **Class File Mismatch**: Clean Rebuild; verifizieren Sie, dass nur eine Kopie der Klasse im Runtime-Classpath vorhanden ist (Achtung vor Fat JARs oder duplizierten Modulen).
* **Falscher JDWP-Port**: Bestätigen Sie, dass Liberty tatsächlich lauscht (`server debug` Logs oder `netstat` lokal; für CF muss die SSH-Tunnel-Zeile übereinstimmen).
* **Unterschiedliche JDK-Hauptversion**: Stellen Sie sicher, dass die Maven/Liberty/CF-JDKs identisch sind (z.B. alle Java 17).
* **Compiler-Debug-Info entfernt**: Stellen Sie sicher, dass `maven-compiler-plugin` nicht `-g:none` verwendet. Der Default ist in Ordnung; bei Anpassungen `-g` einschließen.
* **Reload erforderlich**: Nach Signaturänderungen, Liberty neu starten (oder auf CF restagen).

---

Wenn Sie es wie oben beschrieben einrichten – entweder immer `mvn clean package` oder den "30-Minuten-Frische"-Wrapper – wird sich der IntelliJ-Remote-Debugger zuverlässig mit Liberty verbinden, und es kann auf CF via SSH-Tunnel in Non-Prod funktionieren.