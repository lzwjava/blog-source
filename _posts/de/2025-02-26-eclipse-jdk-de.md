---
audio: false
generated: true
lang: de
layout: post
title: Behebung von Eclipse JDK-Problemen
translated: true
type: note
---

Wenn Sie Eclipse 4.6.3 durch Klicken auf `eclipse.exe` starten und den Fehler "Java was started but returned exit code" mit einem Verweis auf `Oracle\Java\javapath\javaw.exe` erhalten, bedeutet dies, dass Eclipse versucht, eine Java Virtual Machine (JVM) zu verwenden, die entweder inkompatibel oder falsch konfiguriert ist. Der Pfad `Oracle\Java\javapath\javaw.exe` zeigt an, dass Eclipse standardmäßig auf eine JVM zurückgreift, die in der PATH-Umgebungsvariable Ihres Systems definiert ist und möglicherweise nicht für Eclipse 4.6.3 geeignet ist. Um das Problem zu beheben, müssen Sie die korrekte Java-Installation für Eclipse festlegen, indem Sie es so konfigurieren, dass es eine kompatible JVM verwendet. So gehen Sie vor:

### Schritt-für-Schritt-Lösung

1. **Anforderung verstehen**  
   Eclipse 4.6.3 (Neon) benötigt mindestens Java 8, um ordnungsgemäß zu funktionieren. Der Fehler deutet darauf hin, dass die aktuelle JVM (von `Oracle\Java\javapath`) diese Anforderung möglicherweise nicht erfüllt oder Konfigurationsprobleme aufweist. Sie müssen Eclipse auf eine kompatible Java-Installation verweisen, z.B. ein Java 8 JDK.

2. **Ihre Java-Installation finden**  
   Stellen Sie fest, wo eine kompatible Java-Version (z.B. JDK 1.8.0) auf Ihrem System installiert ist. Häufige Speicherorte unter Windows sind:  
   - `C:\Program Files\Java\jdk1.8.0_XXX` (für 64-Bit-Java)  
   - `C:\Program Files (x86)\Java\jdk1.8.0_XXX` (für 32-Bit-Java)  
   Ersetzen Sie `XXX` durch die spezifische Update-Version (z.B. `231` für JDK 1.8.0_231). In diesem Verzeichnis befindet sich die Datei `javaw.exe` im Unterverzeichnis `bin` (z.B. `C:\Program Files\Java\jdk1.8.0_XXX\bin\javaw.exe`).

   **Tipp**: Um die Version und Architektur zu bestätigen, öffnen Sie eine Eingabeaufforderung, navigieren Sie in das `bin`-Verzeichnis (z.B. `cd C:\Program Files\Java\jdk1.8.0_XXX\bin`) und führen Sie aus:
   ```
   java -version
   ```
   Suchen Sie in der Ausgabe nach "64-Bit" oder "32-Bit", um die Architektur zu überprüfen. Stellen Sie sicher, dass sie mit Ihrer Eclipse-Version übereinstimmt (wahrscheinlich 64-Bit, wenn sie kürzlich heruntergeladen wurde).

3. **Die Datei `eclipse.ini` finden**  
   Die Datei `eclipse.ini` ist eine Konfigurationsdatei, die sich im selben Verzeichnis wie `eclipse.exe` befindet. Wenn Eclipse beispielsweise in `C:\eclipse` installiert ist, befindet sich die Datei unter `C:\eclipse\eclipse.ini`. Diese Datei ermöglicht es Ihnen, die JVM festzulegen, die Eclipse verwenden soll.

4. **Die Datei `eclipse.ini` bearbeiten**  
   Öffnen Sie `eclipse.ini` in einem Texteditor (z.B. Notepad) mit Administratorrechten. Sie werden sie ändern, um das `-vm`-Argument einzufügen, das Eclipse mitteilt, welche JVM es verwenden soll. Gehen Sie folgendermaßen vor:

   - **Vorhandenen Inhalt prüfen**: Suchen Sie nach einem `-vm`-Argument. Wenn es bereits vorhanden ist, folgt im nächsten Zeile ein Pfad (z.B. `-vm` gefolgt von `C:/some/path/bin/javaw.exe`). Wenn es auf den problematischen Pfad `Oracle\Java\javapath\javaw.exe` verweist, ersetzen Sie ihn. Wenn kein `-vm`-Argument existiert, fügen Sie es hinzu.
   - **Das `-vm`-Argument hinzufügen oder ändern**: Fügen Sie die folgenden zwei Zeilen vor dem `-vmargs`-Abschnitt (falls vorhanden) oder nahe dem Anfang der Datei nach den initialen Startparametern ein:
     ```
     -vm
     C:/Program Files/Java/jdk1.8.0_XXX/bin/javaw.exe
     ```
     - Verwenden Sie Vorwärtsschrägstriche (`/`) anstelle von Rückwärtsschrägstrichen (`\`), um Parsing-Probleme zu vermeiden.
     - Ersetzen Sie `C:/Program Files/Java/jdk1.8.0_XXX` mit dem tatsächlichen Pfad zu Ihrer Java-Installation.
   - **Korrekte Platzierung sicherstellen**: Das `-vm`-Argument muss vor dem `-vmargs`-Abschnitt erscheinen, der typischerweise mit `-vmargs` beginnt, gefolgt von JVM-Optionen wie `-Xms256m` oder `-Xmx1024m`. Nach der Bearbeitung könnte Ihre `eclipse.ini` beispielsweise so aussehen:
     ```
     -startup
     plugins/org.eclipse.equinox.launcher_1.3.201.v20161025-1711.jar
     --launcher.library
     plugins/org.eclipse.equinox.launcher.win32.win32.x86_64_1.1.401.v20161122-1740
     -vm
     C:/Program Files/Java/jdk1.8.0_XXX/bin/javaw.exe
     -vmargs
     -Dosgi.requiredJavaVersion=1.8
     -Xms256m
     -Xmx1024m
     ```
   - **Vermeiden Sie zusätzliche Leerzeichen oder Leerzeilen**: Stellen Sie sicher, dass sich keine unnötigen Leerzeichen oder Leerzeilen unmittelbar nach den `-vm`- oder Pfad-Zeilen befinden, da dies dazu führen kann, dass Eclipse die Konfiguration falsch interpretiert.

5. **Speichern und testen**  
   Speichern Sie die Datei `eclipse.ini` und doppelklicken Sie dann auf `eclipse.exe`, um Eclipse zu starten. Wenn es korrekt konfiguriert ist, sollte Eclipse ohne den Fehler "Java was started but returned exit code" starten.

### Zusätzliche Hinweise
- **Architekturübereinstimmung**: Stellen Sie sicher, dass die JVM-Architektur (32-Bit oder 64-Bit) mit Ihrer Eclipse-Installation übereinstimmt. Ein 64-Bit-Eclipse benötigt eine 64-Bit-JVM, die sich typischerweise in `C:\Program Files\Java` befindet, während ein 32-Bit-Eclipse eine 32-Bit-JVM aus `C:\Program Files (x86)\Java` benötigt.
- **Pfad überprüfen**: Überprüfen Sie nochmals, ob `javaw.exe` am angegebenen Speicherort existiert. Wenn der Pfad falsch ist, wird Eclipse nicht starten.
- **Fallback-Option**: Wenn dies nicht funktioniert, erwägen Sie, die Umgebungsvariable `JAVA_HOME` (z.B. `C:\Program Files\Java\jdk1.8.0_XXX`) zu setzen und den System-PATH so zu aktualisieren, dass `%JAVA_HOME%\bin` enthalten ist. Die Änderung der `eclipse.ini` ist jedoch die bevorzugte und zuverlässigere Methode für Eclipse.

Durch das Bearbeiten der `eclipse.ini`-Datei, um das `-vm`-Argument mit dem Pfad zu einer kompatiblen `javaw.exe` einzufügen, legen Sie effektiv das Java Home für Eclipse fest und stellen sicher, dass es die korrekte JVM zum Starten verwendet.