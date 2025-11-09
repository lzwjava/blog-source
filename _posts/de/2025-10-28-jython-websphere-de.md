---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Jython im WebSphere Application Server
translated: true
type: note
---

### Verwendung von Jython im IBM WebSphere Application Server

Hinweis: "jPython" bezieht sich auf Jython, eine Implementierung von Python, die auf der Java Virtual Machine (JVM) läuft. Es wird häufig in WebSphere für administrative Skripting-Aufgaben verwendet und kann auch in bereitgestellte Anwendungen integriert werden. Der WebSphere Application Server (WAS) enthält Jython (typischerweise Version 2.1 oder höher, abhängig von der WAS-Version) unter `<WAS_HOME>/optionalLibraries/jython`, sodass in der Regel keine separate Installation erforderlich ist. Im Folgenden werden die beiden primären Anwendungsfälle behandelt: administrative Aufgaben und Laufzeitnutzung in Anwendungen.

#### 1. Administratives Skripting mit wsadmin
Die gebräuchlichste Art, Jython in WebSphere zu verwenden, ist die Serververwaltung, wie das Bereitstellen von Anwendungen, das Starten/Stoppen von Servern, das Konfigurieren von Ressourcen und das Auflisten installierter Apps. Dies geschieht über das Tool `wsadmin`, das Jython als bevorzugte Skriptsprache unterstützt (anstelle der veralteten Sprache Jacl).

**Voraussetzungen:**
- Stellen Sie sicher, dass der WebSphere-Server läuft.
- Suchen Sie `wsadmin` in `<WAS_HOME>/bin/wsadmin.sh` (Linux/Unix) oder `wsadmin.bat` (Windows).
- Jython ist vorinstalliert; für neuere Funktionen (z.B. Python 2.5+ Syntax) kann ein Upgrade über einen benutzerdefinierten Classpath erforderlich sein (siehe fortgeschrittene Hinweise unten).

**Grundlegende Schritte zum Ausführen eines Jython-Skripts:**
1. Erstellen Sie eine Jython-Skriptdatei (z.B. `example.py`) mit Ihrem Code. Verwenden Sie die Objekte AdminConfig, AdminControl und AdminApp für WebSphere-spezifische Operationen.
   
   Beispielskript zum Auflisten aller installierten Anwendungen (`listApps.py`):
   ```
   # Alle Anwendungen auflisten
   apps = AdminApp.list()
   print("Installierte Anwendungen:")
   for app in apps.splitlines():
       if app.strip():
           print(app.strip())
   AdminConfig.save()  # Optional: Konfigurationsänderungen speichern
   ```

2. Führen Sie das Skript mit `wsadmin` aus:
   - Verbindung über SOAP (Standard für Remote):
     ```
     wsadmin.sh -lang jython -f listApps.py -host <hostname> -port <soap_port> -user <admin_user> -password <admin_pass>
     ```
   - Für lokal (ohne Host/Port):
     ```
     wsadmin.sh -lang jython -f listApps.py
     ```
   - Beispielausgabe: Listet Apps wie `DefaultApplication`.

3. Für den interaktiven Modus (REPL):
   ```
   wsadmin.sh -lang jython
   ```
   Geben Sie dann Jython-Befehle direkt ein, z.B. `print AdminApp.list()`.

**Häufige Beispiele:**
- **EAR/WAR bereitstellen:** Erstellen Sie `deployApp.py`:
  ```
  appName = 'MyApp'
  earPath = '/pfad/zu/MyApp.ear'
  AdminApp.install(earPath, '[-appname ' + appName + ' -server server1]')
  AdminConfig.save()
  print('Bereitgestellt ' + appName)
  ```
  Ausführung: `wsadmin.sh -lang jython -f deployApp.py`.

- **Server starten/stoppen:**
  ```
  server = AdminControl.completeObjectName('type=Server,process=server1,*')
  AdminControl.invoke(server, 'start')  # Oder 'stop'
  ```

- **Jython-Version angeben (falls benötigt):** Für Jython 2.1 explizit:
  `wsadmin.sh -usejython21 true -f script.py`. Für benutzerdefinierte Versionen, zum Classpath hinzufügen: `-wsadmin_classpath /pfad/zu/jython.jar`.

**Tipps:**
- Verwenden Sie `AdminConfig.help('object_type')` für Befehls-Hilfe.
- Skripte können in CI/CD (z.B. Jenkins) automatisiert werden, indem `wsadmin` in Batch-Dateien aufgerufen wird.
- Für Thin Client (ohne vollständige WAS-Installation): Laden Sie Client-JARs von IBM herunter und setzen Sie den Classpath.

#### 2. Verwendung von Jython in bereitgestellten Anwendungen
Um Jython-Code innerhalb einer Java-Anwendung (z.B. Servlet oder EJB), die auf WebSphere läuft, auszuführen, binden Sie die Jython-Laufzeitumgebung (jython.jar) in den Classpath der Anwendung ein. Dies ermöglicht das Einbetten von Python-Skripten oder die Verwendung von Jython als Skript-Engine. Laden Sie die neueste jython.jar von der offiziellen Jython-Website herunter, falls die gebündelte Version veraltet ist.

Es gibt zwei Hauptmethoden: **Classpath** (serverweit) oder **Shared Library** (wiederverwendbar über Apps hinweg).

**Methode 1: Classpath (Direktes Hinzufügen zur JVM)**
1. Speichern Sie `jython.jar` in einem zugänglichen Pfad auf dem WebSphere-Host (z.B. `/opt/IBM/WebSphere/AppServer/profiles/AppSrv01/mylibs/jython.jar`).
2. Melden Sie sich bei der WebSphere Admin Console an.
3. Navigieren Sie zu **Server > Servertypen > WebSphere-Anwendungsserver > [Ihr Server]**.
4. Gehen Sie zu **Java- und Prozessverwaltung > Prozessdefinition > Java Virtual Machine > Classpath**.
5. Fügen Sie den vollständigen Pfad zu `jython.jar` hinzu (z.B. `/opt/.../jython.jar`).
6. Fügen Sie in **Generische JVM-Argumente** den Python-Pfad hinzu:
   `-Dpython.path=/opt/.../jython.jar/Lib` (zeigt auf Jythons Standardbibliothek).
7. Klicken Sie auf **OK**, speichern Sie die Konfiguration und starten Sie den Server neu.
8. Synchronisieren Sie die Knoten in einer geclusterten Umgebung (über **Systemverwaltung > Knoten > Synchronisieren**).
9. Verwenden Sie in Ihrem Java-Code `org.python.util.PythonInterpreter`, um Jython-Skripte auszuführen:
   ```
   import org.python.util.PythonInterpreter;
   PythonInterpreter interpreter = new PythonInterpreter();
   interpreter.exec("print('Hallo von Jython in WebSphere!')");
   ```

**Methode 2: Shared Library (Empfohlen für mehrere Apps)**
1. Platzieren Sie `jython.jar` in einem freigegebenen Verzeichnis (z.B. `/shared/libs/jython.jar`).
2. In der Admin Console: **Umgebung > Shared Libraries > [Bereich: Server oder Zelle] > Neu**.
3. Geben Sie einen Namen ein (z.B. `JythonLib`), aktivieren Sie **Use a native library directory** und setzen Sie **Classpath** auf `/shared/libs/jython.jar`.
4. Speichern.
5. Für eine bestimmte Anwendung: **Anwendungen > Anwendungstypen > WebSphere-Unternehmensanwendungen > [Ihre App] > Shared Libraries referenzieren**.
6. Klicken Sie unter **Shared Library References** auf **Hinzufügen**, wählen Sie `JythonLib` aus und setzen Sie **Classpath** entsprechend.
7. Speichern, aktualisieren Sie die App (neu starten falls nötig) und synchronisieren Sie die Knoten.
8. Referenzieren Sie im Code wie in der Classpath-Methode.

**Tipps für Apps:**
- Für Servlet-basierte Jython-Apps verwenden Sie PyServlet (in Jython enthalten) für Python-Handler.
- Testen Sie in einer Entwicklungsumgebung; überwachen Sie die Logs auf Classpath-Probleme.
- Bei Verwendung einer neueren Jython-Version (z.B. 2.7) stellen Sie Java 8+ Kompatibilität sicher.

#### Fortgeschrittene Hinweise
- **Versionskompatibilität:** WAS 9.x verwendet Jython 2.7+. Für Upgrades ersetzen Sie die gebündelte JAR-Datei, testen Sie jedoch gründlich.
- **Fehlerbehandlung:** Verwenden Sie in Skripten `try: ... except Exception as e: print(e)`.
- **IDE-Unterstützung:** Verwenden Sie IBM Rational Application Developer (RAD) oder Eclipse mit WebSphere-Plugins zum Debuggen von Jython/wsadmin-Skripten.
- **Ressourcen:** Für vollständige Tutorials siehe das Buch *WebSphere Application Server Administration Using Jython* oder die IBM wsadmin-Dokumentation.

Wenn dies nicht genau auf Ihr Szenario zutrifft (z.B. spezifische WAS-Version oder Anwendungsfall), geben Sie weitere Details für eine maßgeschneiderte Beratung an.

**Referenzen:**
- [Using wsadmin scripting with Jython (IBM Docs)](https://www.ibm.com/docs/en/was/9.0.5?topic=scripting-using-wsadmin-jython)
- [Deploying Jython on WebSphere (Oracle Guide)](https://docs.oracle.com/en/applications/jd-edwards/cross-product/9.2/eotos/deploying-jython-on-ais-server-on-ibm-websphere-application.html)
- [WebSphere Jython Integration (Stack Overflow)](https://stackoverflow.com/questions/25187577/will-the-ibm-websphere-application-server-run-the-python-jython-script-without-p)
- [Jython Wiki on WebSphere](https://wiki.python.org/jython/WebSphere)
- [Deploy App with Jython Example](https://jobhunterssite.wordpress.com/2016/05/12/deploy-an-application-in-websphere-using-jython-automation/)