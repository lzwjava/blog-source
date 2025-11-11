---
audio: false
generated: true
lang: de
layout: post
title: Squirrel-Startskript
translated: true
type: note
---

Dieses Batch-Skript wird verwendet, um den SQuirreL SQL Client, ein Java-basiertes Datenbank-Administrationstool, zu starten. Im Folgenden finden Sie eine umfassende Erklärung des Skripts, die seinen Zweck, Aufbau und Funktionalität Schritt für Schritt aufschlüsselt.

---

### **Überblick**
Das Skript ist dazu entwickelt:
1. Die Java-Umgebung für den Betrieb des SQuirreL SQL Clients zu konfigurieren.
2. Die Java-Version-Kompatibilität zu überprüfen (erfordert Java 1.6 oder 1.7).
3. Nach Software-Updates zu suchen und diese bei Verfügbarkeit anzuwenden.
4. Den Classpath für SQuirreL und seine Bibliotheken zu erstellen.
5. Die SQuirreL SQL Client-Anwendung mit den entsprechenden Parametern zu starten.

Das Skript ist für Windows geschrieben (verwendet die `.bat`-Erweiterung) und nutzt die Batch-Skriptsprache der Windows-Eingabeaufforderung.

---

### **Zeilenweise Erklärung**

#### **1. `@echo off`**
- **Zweck**: Deaktiviert die Ausgabe von Befehlen in die Konsole, macht die Ausgabe des Skripts sauberer, indem nur die beabsichtigte Ausgabe angezeigt wird (z.B. Fehlermeldungen oder spezifische `echo`-Anweisungen).
- **Effekt**: Befehle, die im Skript ausgeführt werden, werden nicht angezeigt, es sei denn, sie werden explizit mit `echo` ausgegeben.

---

#### **2. `@rem IZPACK_JAVA is filtered in by the IzPack installer when this script is installed`**
- **Zweck**: Ein Kommentar (`@rem`), der anzeigt, dass die Variable `IZPACK_JAVA` vom IzPack-Installer während der Installation gesetzt wird.
- **Kontext**: IzPack ist ein Tool, das verwendet wird, um Installationsprogramme für Java-Anwendungen zu erstellen. Es setzt dynamisch die `JAVA_HOME`-Umgebungsvariable im Skript, um auf die während des Setups verwendete Java-Installation zu verweisen.

#### **3. `set IZPACK_JAVA=%JAVA_HOME`**
- **Zweck**: Weist den Wert der `JAVA_HOME`-Umgebungsvariable (gesetzt von IzPack) der Variable `IZPACK_JAVA` zu.
- **Erklärung**: Dies stellt sicher, dass das Skript weiß, wo sich die Java-Installation befindet. `JAVA_HOME` zeigt typischerweise auf das Stammverzeichnis eines Java Development Kit (JDK) oder Java Runtime Environment (JRE).

---

#### **4. Java-Erkennungslogik**
```bat
@rem We detect the java executable to use according to the following algorithm:
@rem 1. If the one used by the IzPack installer is available then use that; otherwise
@rem 2. Use the java that is in the command path.
if exist "%IZPACK_JAVA%\bin\javaw.exe" (
  set LOCAL_JAVA=%IZPACK_JAVA%\bin\javaw.exe
) else (
  set LOCAL_JAVA=javaw.exe
)
```
- **Zweck**: Bestimmt, welche Java-Executable für das Ausführen von SQuirreL SQL verwendet werden soll.
- **Logik**:
  1. **Prüfe auf IzPack Java**: Das Skript prüft, ob `javaw.exe` im `bin`-Verzeichnis der durch `IZPACK_JAVA` angegebenen Java-Installation existiert (d.h. `%IZPACK_JAVA%\bin\javaw.exe`).
     - `javaw.exe` ist eine Windows-spezifische Java-Executable, die Java-Anwendungen ohne das Öffnen eines Konsolenfensters ausführt (im Gegensatz zu `java.exe`).
     - Wenn gefunden, wird `LOCAL_JAVA` auf den vollständigen Pfad von `javaw.exe` gesetzt.
  2. **Fallback auf PATH**: Wenn `javaw.exe` nicht im `IZPACK_JAVA`-Verzeichnis gefunden wird, greift das Skript auf die Verwendung von `javaw.exe` aus der `PATH`-Umgebungsvariable des Systems zurück.
- **Warum `javaw.exe`?**: Die Verwendung von `javaw.exe` stellt sicher, dass die Anwendung ohne ein persistentes Befehlsfenster läuft und so ein saubereres Benutzererlebnis bietet.

#### **5. `echo Using java: %LOCAL_JAVA%`**
- **Zweck**: Gibt den Pfad der verwendeten Java-Executable zu Debugging- oder Informationszwecken auf der Konsole aus.
- **Beispielausgabe**: Wenn `LOCAL_JAVA` `C:\Program Files\Java\jre1.6.0_45\bin\javaw.exe` ist, wird angezeigt:
  ```
  Using java: C:\Program Files\Java\jre1.6.0_45\bin\javaw.exe
  ```

---

#### **6. Bestimmen des SQuirreL SQL Home-Verzeichnisses**
```bat
set basedir=%~f0
:strip
set removed=%basedir:~-1%
set basedir=%basedir:~0,-1%
if NOT "%removed%"=="\" goto strip
set SQUIRREL_SQL_HOME=%basedir%
```
- **Zweck**: Bestimmt das Verzeichnis, in dem SQuirreL SQL installiert ist (`SQUIRREL_SQL_HOME`).
- **Erklärung**:
  - `%~f0`: Dies erweitert sich zum vollständigen Pfad des Batch-Skripts selbst (z.B. `C:\Program Files\SQuirreL\squirrel-sql.bat`).
  - **`:strip` Schleife**: Das Skript entfernt iterativ das letzte Zeichen von `basedir`, bis es auf einen Backslash (`\`) trifft, und entfernt so effektiv den Dateinamen des Skripts, um den Verzeichnispfad zu erhalten.
  - **Ergebnis**: `SQUIRREL_SQL_HOME` wird auf das Verzeichnis gesetzt, das das Skript enthält (z.B. `C:\Program Files\SQuirreL`).
- **Warum dieser Ansatz?**: Dies stellt sicher, dass das Skript sein eigenes Installationsverzeichnis dynamisch bestimmen kann, was es portabel über verschiedene Systeme hinweg macht.

---

#### **7. Java-Version-Prüfung**
```bat
"%LOCAL_JAVA%" -cp "%SQUIRREL_SQL_HOME%\lib\versioncheck.jar" JavaVersionChecker 1.6 1.7
if ErrorLevel 1 goto ExitForWrongJavaVersion
```
- **Zweck**: Überprüft, ob die Java-Version mit SQuirreL SQL kompatibel ist (erfordert Java 1.6 oder 1.7).
- **Erklärung**:
  - Das Skript führt die Klasse `JavaVersionChecker` aus `versioncheck.jar` aus, die sich im `lib`-Verzeichnis von SQuirreL SQL befindet.
  - **`-cp`**: Spezifiziert den Classpath und verweist auf `versioncheck.jar`.
  - **Argumente**: `1.6 1.7` gibt an, dass die Java-Version 1.6 oder 1.7 sein muss.
  - **Hinweis**: `versioncheck.jar` ist mit Java 1.2.2-Kompatibilität kompiliert, um sicherzustellen, dass es auf älteren JVMs laufen kann, um die Versionsprüfung durchzuführen.
  - **Fehlerbehandlung**: Wenn die Java-Version inkompatibel ist, wird `ErrorLevel` auf 1 gesetzt und das Skript springt zum Label `:ExitForWrongJavaVersion`, wodurch die Ausführung beendet wird.
- **Warum diese Prüfung?**: SQuirreL SQL erfordert bestimmte Java-Versionen, um korrekt zu funktionieren, und dies verhindert das Ausführen der Anwendung auf nicht unterstützten JVMs.

---

#### **8. Software-Update-Prüfung**
```bat
if not exist "%SQUIRREL_SQL_HOME%\update\changeList.xml" goto launchsquirrel
SET TMP_CP="%SQUIRREL_SQL_HOME%\update\downloads\core\squirrel-sql.jar"
if not exist %TMP_CP% goto launchsquirrel
dir /b "%SQUIRREL_SQL_HOME%\update\downloads\core\*.*" > %TEMP%\update-lib.tmp
FOR /F %%I IN (%TEMP%\update-lib.tmp) DO CALL "%SQUIRREL_SQL_HOME%\addpath.bat" "%SQUIRREL_SQL_HOME%\update\downloads\core\%%I"
SET UPDATE_CP=%TMP_CP%
SET UPDATE_PARMS=--log-config-file "%SQUIRREL_SQL_HOME%\update-log4j.properties" --squirrel-home "%SQUIRREL_SQL_HOME%" %1 %2 %3 %4 %5 %6 %7 %8 %9
"%LOCAL_JAVA%" -cp %UPDATE_CP% -Dlog4j.defaultInitOverride=true -Dprompt=true net.sourceforge.squirrel_sql.client.update.gui.installer.PreLaunchUpdateApplication %UPDATE_PARAMS%
```
- **Zweck**: Prüft auf Software-Updates und wendet diese vor dem Start der Hauptanwendung an.
- **Erklärung**:
  1. **Prüfe auf Update-Dateien**:
     - Das Skript prüft, ob `changeList.xml` im `update`-Verzeichnis existiert. Diese Datei wird von der Software-Update-Funktion von SQuirreL erstellt, um Updates zu verfolgen.
     - Wenn `changeList.xml` nicht existiert, überspringt das Skript den Update-Prozess und springt zu `:launchsquirrel`.
     - Es prüft auch auf die aktualisierte `squirrel-sql.jar` im Verzeichnis `update\downloads\core`. Wenn sie nicht existiert, springt das Skript zu `:launchsquirrel`.
  2. **Update-Classpath erstellen**:
     - Der Befehl `dir /b` listet alle Dateien im Verzeichnis `update\downloads\core` auf und schreibt sie in eine temporäre Datei (`%TEMP%\update-lib.tmp`).
     - Die `FOR /F`-Schleife iteriert über die Dateien in `update-lib.tmp` und ruft `addpath.bat` auf, um jede Datei an den in `TMP_CP` gespeicherten Classpath anzuhängen.
     - `UPDATE_CP` wird auf den Classpath gesetzt, beginnend mit `squirrel-sql.jar` aus dem Update-Verzeichnis.
  3. **Update-Parameter setzen**:
     - `UPDATE_PARMS` beinhaltet:
       - `--log-config-file`: Spezifiziert die Log4j-Konfigurationsdatei für die Protokollierung während des Update-Prozesses.
       - `--squirrel-home`: Übergibt das SQuirreL-Installationsverzeichnis.
       - `%1 %2 %3 ... %9`: Übergibt alle Befehlszeilenargumente, die dem Skript bereitgestellt wurden.
  4. **Update-Anwendung ausführen**:
     - Das Skript startet `PreLaunchUpdateApplication` (eine Java-Klasse in `squirrel-sql.jar`), um Updates anzuwenden.
     - **`-Dlog4j.defaultInitOverride=true`**: Überschreibt die Standard-Log4j-Konfiguration.
     - **`-Dprompt=true`**: Aktiviert wahrscheinlich interaktive Aufforderungen während des Update-Prozesses.
- **Warum dieser Schritt?**: SQuirreL SQL unterstützt automatische Updates, und dieser Abschnitt stellt sicher, dass alle heruntergeladenen Updates angewendet werden, bevor die Hauptanwendung gestartet wird.

---

#### **9. SQuirreL SQL starten**
```bat
:launchsquirrel
@rem build SQuirreL's classpath
set TMP_CP="%SQUIRREL_SQL_HOME%\squirrel-sql.jar"
dir /b "%SQUIRREL_SQL_HOME%\lib\*.*" > %TEMP%\squirrel-lib.tmp
FOR /F %%I IN (%TEMP%\squirrel-lib.tmp) DO CALL "%SQUIRREL_SQL_HOME%\addpath.bat" "%SQUIRREL_SQL_HOME%\lib\%%I"
SET SQUIRREL_CP=%TMP_CP%
echo "SQUIRREL_CP=%SQUIRREL_CP%"
```
- **Zweck**: Erstellt den Classpath für die Haupt-SQuirreL SQL-Anwendung und bereitet deren Start vor.
- **Erklärung**:
  1. **Classpath initialisieren**:
     - `TMP_CP` wird mit dem Pfad zu `squirrel-sql.jar` im SQuirreL-Installationsverzeichnis initialisiert.
  2. **Bibliotheks-Jars hinzufügen**:
     - Der Befehl `dir /b` listet alle Dateien im `lib`-Verzeichnis auf und schreibt sie in `squirrel-lib.tmp`.
     - Die `FOR /F`-Schleife iteriert über die Dateien und ruft `addpath.bat` auf, um jede Bibliotheksdatei (z.B. `.jar`-Dateien) an den `TMP_CP`-Classpath anzuhängen.
  3. **Finalen Classpath setzen**:
     - `SQUIRREL_CP` wird auf den fertigen Classpath gesetzt.
  4. **Debug-Ausgabe**:
     - Das Skript gibt den finalen Classpath (`SQUIRREL_CP`) zu Debugging-Zwecken aus.

---

#### **10. Startparameter setzen**
```bat
SET TMP_PARMS=--log-config-file "%SQUIRREL_SQL_HOME%\log4j.properties" --squirrel-home "%SQUIRREL_SQL_HOME%" %1 %2 %3 %4 %5 %6 %7 %8 %9
```
- **Zweck**: Definiert die Parameter, die an die SQuirreL SQL-Anwendung übergeben werden sollen.
- **Erklärung**:
  - `--log-config-file`: Spezifiziert die Log4j-Konfigurationsdatei für die Hauptanwendung.
  - `--squirrel-home`: Übergibt das SQuirreL-Installationsverzeichnis.
  - `%1 %2 ... %9`: Übergibt alle Befehlszeilenargumente, die dem Skript bereitgestellt wurden.

---

#### **11. Anwendung starten**
```bat
@rem -Dsun.java2d.noddraw=true prevents performance problems on Win32 systems.
start "SQuirreL SQL Client" /B "%LOCAL_JAVA%" -Xmx256m -Dsun.java2d.noddraw=true -cp %SQUIRREL_CP% -splash:"%SQUIRREL_SQL_HOME%/icons/splash.jpg" net.sourceforge.squirrel_sql.client.Main %TMP_PARMS%
```
- **Zweck**: Startet die SQuirreL SQL Client-Anwendung.
- **Erklärung**:
  - **`start "SQuirreL SQL Client" /B`**: Führt den Befehl in einem neuen Prozess aus, ohne ein neues Konsolenfenster zu öffnen (`/B` unterdrückt das Fenster).
  - **`%LOCAL_JAVA%`**: Spezifiziert die zu verwendende Java-Executable.
  - **`-Xmx256m`**: Setzt die maximale Java-Heap-Größe auf 256 MB, um die Speichernutzung zu begrenzen.
  - **`-Dsun.java2d.noddraw=true`**: Deaktiviert DirectDraw für Java 2D-Grafiken, um Leistungsprobleme auf Windows-Systemen zu vermeiden.
  - **`-cp %SQUIRREL_CP%`**: Spezifiziert den Classpath für die Anwendung.
  - **`-splash:"%SQUIRREL_SQL_HOME%/icons/splash.jpg"`**: Zeigt einen Splash Screen (ein Bild) an, wenn die Anwendung startet.
  - **`net.sourceforge.squirrel_sql.client.Main`**: Die auszuführende Haupt-Java-Klasse.
  - **`%TMP_PARMS%`**: Übergibt die zuvor definierten Parameter.

---

#### **12. Beenden bei falscher Java-Version**
```bat
:ExitForWrongJavaVersion
```
- **Zweck**: Ein Label, das als Ausstiegspunkt verwendet wird, wenn die Java-Version-Prüfung fehlschlägt.
- **Erklärung**: Wenn die Java-Version nicht 1.6 oder 1.7 ist, springt das Skript hierher und beendet sich, ohne die Anwendung zu starten.

---

### **Wichtige Komponenten und Konzepte**
1. **Classpath-Konstruktion**:
   - Das Skript erstellt dynamisch den Classpath für sowohl den Update-Prozess (`UPDATE_CP`) als auch die Hauptanwendung (`SQUIRREL_CP`), indem es `squirrel-sql.jar` und alle `.jar`-Dateien in den Verzeichnissen `lib` oder `update\downloads\core` einbindet.
   - Das Skript `addpath.bat` (nicht gezeigt) wird angenommen, um jede Datei an die Classpath-Variable anzuhängen.

2. **Log4j-Konfiguration**:
   - Log4j ist ein Protokollierungs-Framework, das von SQuirreL SQL verwendet wird. Das Skript spezifiziert separate Log4j-Konfigurationsdateien für den Update-Prozess (`update-log4j.properties`) und die Hauptanwendung (`log4j.properties`).

3. **Software-Update-Mechanismus**:
   - SQuirreL SQL unterstützt automatische Updates, die von der Klasse `PreLaunchUpdateApplication` verwaltet werden. Das Skript prüft auf Update-Dateien und führt den Update-Prozess bei Bedarf aus.

4. **Java-Version-Kompatibilität**:
   - Das Skript erzwingt strikte Kompatibilität mit Java 1.6 oder 1.7, wahrscheinlich aufgrund von Abhängigkeiten oder features, die spezifisch für diese Versionen sind.

5. **Portabilität**:
   - Das Skript ist portabel gestaltet, indem es das Installationsverzeichnis und den Speicherort der Java-Executable dynamisch bestimmt.

---

### **Potenzielle Probleme und Überlegungen**
1. **Java-Version-Beschränkung**:
   - Das Skript erlaubt nur Java 1.6 oder 1.7, die veraltet sind (veröffentlicht 2006 bzw. 2011). Moderne Systeme können neuere Java-Versionen haben, was dazu führt, dass das Skript fehlschlägt, es sei denn, eine ältere JRE ist installiert.
   - **Workaround**: Benutzer müssen möglicherweise eine kompatible JRE installieren oder das Skript modifizieren, um neuere Versionen zu unterstützen (falls SQuirreL SQL kompatibel ist).

2. **Fest codierte Pfade**:
   - Das Skript nimmt an, dass bestimmte Dateien (z.B. `squirrel-sql.jar`, `versioncheck.jar`, `addpath.bat`) in bestimmten, relativ zu `SQUIRREL_SQL_HOME` liegenden Verzeichnissen existieren. Wenn diese fehlen oder verschoben wurden, schlägt das Skript fehl.

3. **Windows-Spezifisch**:
   - Das Skript verwendet Windows-spezifische Befehle (`dir /b`, `FOR /F`, `start /B`) und `javaw.exe`, was es ohne Modifikation inkompatibel mit Nicht-Windows-Systemen macht.

4. **Fehlerbehandlung**:
   - Das Skript behandelt Java-Versionsfehler, bietet aber keine detaillierten Fehlermeldungen für andere Fehler (z.B. fehlende `squirrel-sql.jar` oder ungültiger Classpath).

5. **Speicherlimit**:
   - Das Flag `-Xmx256m` begrenzt die JVM auf 256 MB Speicher, was für große Datenbanken oder komplexe Abfragen unzureichend sein kann und potenziell `OutOfMemoryError` verursacht.

---

### **Zusammenfassung**
Dieses Batch-Skript ist ein Launcher für den SQuirreL SQL Client und führt die folgenden Aufgaben durch:
- Erkennt und konfiguriert die Java-Executable.
- Überprüft die Java-Version-Kompatibilität (1.6 oder 1.7).
- Prüft auf Software-Updates und wendet diese bei Verfügbarkeit an.
- Erstellt den Classpath für die Anwendung.
- Startet SQuirreL SQL mit den entsprechenden Parametern, inklusive eines Splash Screens und Speichereinstellungen.

Das Skript ist für seinen Zweck gut strukturiert, aber auf eine spezifische Umgebung zugeschnitten (Windows, Java 1.6/1.7) und erfordert möglicherweise Anpassungen, um moderne Systeme oder neuere Java-Versionen zu unterstützen.

Wenn Sie weitere Fragen haben oder Hilfe bei der Modifikation des Skripts benötigen (z.B. zur Unterstützung neuerer Java-Versionen), lassen Sie es mich wissen!