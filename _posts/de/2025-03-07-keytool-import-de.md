---
audio: false
generated: true
lang: de
layout: post
title: Zertifikate mit Keytool importieren
translated: true
type: note
---

Um Ihre Frage zur Verwendung des Befehls `keytool -importcert` zum Importieren eines Zertifikats in die Datei `jre/lib/security/cacerts` und dem Auftreten eines Fehlers "password verification failed" mit einer `java.security.UnrecoverableException` zu beantworten, lassen Sie uns das Problem Schritt für Schritt aufschlüsseln, um es zu verstehen, es zu beheben und herauszufinden, was das mögliche Passwort sein könnte.

### Das Problem verstehen

Das Dienstprogramm `keytool` ist ein Kommandozeilen-Tool, das im Java Development Kit (JDK) enthalten ist und zur Verwaltung von Keystores verwendet wird. Ein Keystore ist eine Datei, die kryptografische Schlüssel und Zertifikate speichert, oft zur Absicherung von Netzwerkkommunikation wie SSL/TLS. Die Datei `cacerts`, die sich in `jre/lib/security` befindet, ist ein spezieller Keystore, der mit der Java Runtime Environment (JRE) ausgeliefert wird. Sie enthält eine Sammlung vertrauenswürdiger Stammzertifikate von bekannten Zertifizierungsstellen (CAs), die Java-Anwendungen standardmäßig zur Überprüfung sicherer Verbindungen verwenden.

Wenn Sie den Befehl `keytool -importcert` ausführen, um ein neues Zertifikat zur `cacerts`-Datei hinzuzufügen, müssen Sie das korrekte Passwort für den Keystore angeben. Die Fehlermeldung, die Sie sehen – "password verification failed" gefolgt von `java.security.UnrecoverableException` – zeigt an, dass das von Ihnen eingegebene Passwort (oder das, das Sie nicht korrekt übermittelt haben) nicht mit dem Keystore-Passwort übereinstimmt. Diese Exception tritt typischerweise auf, wenn das angegebene Passwort falsch ist und `keytool` dadurch am Zugriff auf oder an der Änderung des Keystores gehindert wird.

### Der betreffende Befehl

Der Befehl, den Sie wahrscheinlich verwenden, sieht in etwa so aus:

```
keytool -importcert -file mycert.crt -keystore /pfad/zu/jre/lib/security/cacerts -alias myalias
```

- `-file mycert.crt`: Spezifiziert die Zertifikatsdatei, die Sie importieren möchten.
- `-keystore /pfad/zu/jre/lib/security/cacerts`: Zeigt auf den `cacerts`-Keystore.
- `-alias myalias`: Weist dem Zertifikat im Keystore einen eindeutigen Namen (Alias) zu.

Wenn Sie diesen Befehl ausführen, fordert `keytool` Sie zur Eingabe des Keystore-Passworts auf. Wenn das eingegebene Passwort falsch ist, erhalten Sie den beschriebenen Fehler.

### Das mögliche Passwort identifizieren

Für die `cacerts`-Datei in einer standardmäßigen JRE-Installation (wie z.B. von Oracle oder OpenJDK) ist das **Standardpasswort** **"changeit"**. Dies ist eine gut dokumentierte Standardeinstellung über Java-Versionen und Distributionen hinweg. Der Name "changeit" dient als Erinnerung daran, dass Administratoren es aus Sicherheitsgründen ändern sollten, aber in den meisten standardmäßigen, unveränderten Installationen bleibt es unverändert.

Da Ihr Befehl mit einem Passwortverifizierungsfehler fehlschlägt, ist die wahrscheinlichste Ursache, dass entweder:
1. Sie "changeit" nicht korrekt eingegeben haben (z.B. Tippfehler oder falsche Groß-/Kleinschreibung – Passwörter sind case-sensitive).
2. Die Passwortabfrage nicht korrekt behandelt wurde.
3. In Ihrer spezifischen Umgebung das Standardpasswort geändert wurde (was jedoch für `cacerts` weniger üblich ist, es sei denn, es wurde explizit von einem Systemadministrator geändert).

Da Ihre Anfrage kein benutzerdefiniertes Setup anzeigt, gehen wir von einer standardmäßigen JRE-Installation aus, bei der "changeit" gelten sollte.

### Wie das Problem behoben wird

So können Sie das Problem beheben:

1. **Stellen Sie die korrekte Passworteingabe in der Abfrage sicher**
   Führen Sie den Befehl erneut aus:

   ```
   keytool -importcert -file mycert.crt -keystore /pfad/zu/jre/lib/security/cacerts -alias myalias
   ```

   Wenn Sie zur Eingabe des Passworts aufgefordert werden, tippen Sie sorgfältig **"changeit"** (alles klein geschrieben, ohne Leerzeichen) ein und drücken Sie Enter. Überprüfen Sie die Eingabe auf Tippfehler oder Probleme mit der Tastaturbelegung.

2. **Geben Sie das Passwort in der Kommandozeile an**
   Um Probleme mit der interaktiven Abfrage zu vermeiden (z.B. bei Skripting oder Terminalproblemen), können Sie das Passwort direkt mit der Option `-storepass` angeben:

   ```
   keytool -importcert -file mycert.crt -keystore /pfad/zu/jre/lib/security/cacerts -alias myalias -storepass changeit
   ```

   Dies übergibt explizit "changeit" als Passwort und umgeht die Abfrage. Wenn dies ohne Fehler funktioniert, lag das Problem wahrscheinlich an der vorherigen Passworteingabe.

3. **Überprüfen Sie die Berechtigungen**
   Da `cacerts` im JRE-Verzeichnis residiert (z.B. `/usr/lib/jvm/java-11-openjdk/lib/security/cacerts` unter Linux oder ein ähnlicher Pfad unter Windows), stellen Sie sicher, dass Sie Schreibberechtigungen haben. Führen Sie den Befehl bei Bedarf mit Administratorrechten aus:
   - Unter Linux/Mac: `sudo keytool ...`
   - Unter Windows: Führen Sie die Eingabeaufforderung als Administrator aus.

   Da Ihr Fehler jedoch von der Passwortverifizierung und nicht vom Dateizugriff handelt, ist dies wahrscheinlich nicht die Kernursache – aber es ist gut, dies zu überprüfen.

4. **Verifizieren Sie das Passwort**
   Wenn "changeit" weiterhin fehlschlägt, könnte das Passwort in Ihrer Umgebung geändert worden sein. Um das Passwort zu testen, ohne den Keystore zu ändern, versuchen Sie, dessen Inhalt aufzulisten:

   ```
   keytool -list -keystore /pfad/zu/jre/lib/security/cacerts
   ```

   Geben Sie "changeit" ein, wenn Sie dazu aufgefordert werden. Wenn es Zertifikate auflistet, ist das Passwort korrekt. Wenn Sie denselben Fehler erhalten, unterscheidet sich das Passwort vom Standard.

### Was, wenn "changeit" nicht das Passwort ist?

Wenn "changeit" nicht funktioniert, ziehen Sie diese Möglichkeiten in Betracht:
- **Benutzerdefiniertes Passwort**: In seltenen Fällen könnte ein Systemadministrator das `cacerts`-Passwort geändert haben. Sie müssten Ihre Systemdokumentation oder Ihren Administrator konsultieren, um es zu erhalten. Es gibt keine Möglichkeit, ein verlorenes Keystore-Passwort direkt wiederherzustellen; wenn es wirklich unbekannt ist, müssen Sie möglicherweise die `cacerts`-Datei durch eine neue Kopie aus einer neuen JRE-Installation ersetzen (was es auf "changeit" zurücksetzt).
- **Umgebungsspezifische Standardeinstellungen**: Einige nicht standardmäßige Java-Distributionen (z.B. IBM JDK) könnten einen anderen Standard verwenden, aber dies ist unüblich, und Ihre Anfrage deutet auf ein typisches Setup hin.

Ohne weiteren Kontext bleibt "changeit" das wahrscheinlichste Passwort in einer standardmäßigen JRE.

### Endgültige Lösung

Um Ihr Problem zu beheben:
- Verwenden Sie diesen Befehl, unter der Annahme einer standardmäßigen JRE:

  ```
  keytool -importcert -file mycert.crt -keystore /pfad/zu/jre/lib/security/cacerts -alias myalias -storepass changeit
  ```

- Wenn es fehlschlägt, verifizieren Sie das Passwort mit dem `-list`-Befehl oder prüfen Sie bei Ihrem Systemadministrator nach.

Das **mögliche Passwort** in diesem Szenario, basierend auf Standard-Java-Konventionen, ist **"changeit"**. Dies sollte die `java.security.UnrecoverableException` beheben, wenn es korrekt eingegeben wurde und die `cacerts`-Datei nicht angepasst wurde.