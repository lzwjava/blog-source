---
audio: false
generated: true
lang: de
layout: post
title: Umgang mit nicht vertrauenswürdigen Zertifikaten in IntelliJ IDEA
translated: true
type: note
---

Der Dialog "Untrusted Server's Certificate" (Zertifikat des nicht vertrauenswürdigen Servers) in IntelliJ IDEA erscheint oft, wenn die IDE auf SSL-Zertifikate stößt, die nicht von ihrem Keystore (Zertifikatsspeicher) als vertrauenswürdig eingestuft werden, wie z. B. selbstsignierte oder benutzerdefinierte Unternehmenszertifikate. Da Sie den Keystore Ihres Unternehmens bereits in `/lib/cacerts` importiert haben, aber weiterhin die Aufforderung sehen, könnte das Problem darin liegen, dass IntelliJ diesen Keystore nicht verwendet oder dass zusätzliche Zertifikate den Dialog auslösen. So können Sie das Problem beheben und die Aufforderungen möglicherweise stoppen:

### Option 1: IntelliJ so konfigurieren, dass nicht vertrauenswürdige Zertifikate automatisch akzeptiert werden
Wenn Sie diese Option aktivieren, umgeht IntelliJ den Dialog für nicht vertrauenswürdige Zertifikate. Seien Sie jedoch vorsichtig, da dies die Sicherheit verringert, indem alle Zertifikate akzeptiert werden, was Sie potenziell Man-in-the-Middle-Angriffen aussetzen kann.

- **Windows/Linux**:
  1. Gehen Sie zu `File > Settings > Tools > Server Certificates`.
  2. Aktivieren Sie das Kontrollkästchen für **"Accept non-trusted certificates automatically"** (Nicht vertrauenswürdige Zertifikate automatisch akzeptieren).
  3. Klicken Sie auf **Apply** und **OK**.
- **macOS**:
  1. Gehen Sie zu `IntelliJ IDEA > Preferences > Tools > Server Certificates`.
  2. Aktivieren Sie **"Accept non-trusted certificates automatically"**.
  3. Klicken Sie auf **Apply** und **OK**.

**Hinweis**: Dies ist nicht empfehlenswert, es sei denn, Sie befinden sich in einem vertrauenswürdigen, isolierten Netzwerk (z. B. einer luftgekoppelten Unternehmensumgebung), da es Ihre IDE anfällig für unverifizierte Verbindungen machen kann.

### Option 2: Keystore-Konfiguration überprüfen und korrigieren
Da Sie den Unternehmens-Keystore in `/lib/cacerts` importiert haben, stellen Sie sicher, dass IntelliJ ihn korrekt verwendet. Das Problem könnte sein, dass IntelliJ immer noch auf seinen eigenen Truststore oder die falsche cacerts-Datei verweist.

1. **Keystore-Pfad überprüfen**:
   - IntelliJ verwendet oft seinen eigenen Truststore unter `~/.IntelliJIdea<version>/system/tasks/cacerts` oder den JetBrains Runtime (JBR)-Truststore unter `<IntelliJ Installation>/jbr/lib/security/cacerts`.
   - Wenn Sie `/lib/cacerts` im IntelliJ-Verzeichnis modifiziert haben, bestätigen Sie, dass es der korrekte Pfad für Ihre IDE-Version ist. Bei Installationen über die JetBrains Toolbox könnte der Pfad abweichen (z. B. `~/AppData/Local/JetBrains/Toolbox/apps/IDEA-U/ch-0/<version>/jbr/lib/security/cacerts` unter Windows).
   - Verwenden Sie den `keytool`-Befehl, um zu überprüfen, ob das Zertifikat in der cacerts-Datei vorhanden ist:
     ```bash
     keytool -list -keystore <path-to-cacerts> -storepass changeit
     ```
     Stellen Sie sicher, dass Ihr Corporate-CA-Zertifikat aufgeführt ist.

2. **IntelliJ auf den benutzerdefinierten Keystore verweisen**:
   - Wenn das Zertifikat korrekt importiert wurde, IntelliJ aber weiterhin auffordert, verwendet es möglicherweise nicht die modifizierte cacerts-Datei. Fügen Sie eine benutzerdefinierte VM-Option hinzu, um den Truststore anzugeben:
     1. Gehen Sie zu `Help > Edit Custom VM Options`.
     2. Fügen Sie hinzu:
        ```
        -Djavax.net.ssl.trustStore=<path-to-cacerts>
        -Djavax.net.ssl.trustStorePassword=changeit
        ```
        Ersetzen Sie `<path-to-cacerts>` durch den vollständigen Pfad zu Ihrer modifizierten `cacerts`-Datei.
     3. Starten Sie IntelliJ IDEA neu.

3. **Zertifikat erneut importieren**:
   - Wenn der Zertifikatsimport unvollständig oder fehlerhaft war, importieren Sie es erneut:
     ```bash
     keytool -import -trustcacerts -file <certificate-file>.cer -alias <alias> -keystore <path-to-cacerts> -storepass changeit
     ```
     Ersetzen Sie `<certificate-file>.cer` durch Ihr Corporate-CA-Zertifikat und `<path-to-cacerts>` durch den korrekten Pfad zur cacerts-Datei.

### Option 3: Zertifikate über die Server Certificates Einstellungen von IntelliJ hinzufügen
Anstatt die cacerts-Datei manuell zu ändern, können Sie Zertifikate über die Benutzeroberfläche von IntelliJ hinzufügen, die sie in ihrem internen Truststore speichert:

1. Gehen Sie zu `File > Settings > Tools > Server Certificates` (oder `IntelliJ IDEA > Preferences` auf macOS).
2. Klicken Sie auf die Schaltfläche **"+"**, um ein neues Zertifikat hinzuzufügen.
3. Navigieren Sie zu Ihrer Corporate-CA-Zertifikatsdatei (im Format `.cer` oder `.pem`) und importieren Sie sie.
4. Starten Sie IntelliJ neu, um sicherzustellen, dass das Zertifikat erkannt wird.

### Option 4: Auf Proxy- oder Antivirenprogramm-Interferenz prüfen
Unternehmensumgebungen verwenden oft Proxys oder Antivirensoftware (z. B. Zscaler, Forcepoint), die Man-in-the-Middle-SSL-Inspektionen durchführen und dabei dynamisch neue Zertifikate generieren. Dies kann zu wiederholten Aufforderungen führen, wenn sich die Zertifikate häufig ändern (z. B. täglich, wie bei McAfee Endpoint Security).

- **Proxy-/Antiviren-CA-Zertifikat importieren**:
  - Beschaffen Sie sich das Root-CA-Zertifikat von Ihrer Proxy- oder Antivirensoftware (fragen Sie Ihr IT-Team).
  - Importieren Sie es in IntelliJs Truststore über `Settings > Tools > Server Certificates` oder in die cacerts-Datei mit dem oben genannten `keytool`-Befehl.
- **SSL-Inspektion deaktivieren (falls möglich)**:
  - Wenn Ihr Proxy es zulässt, konfigurieren Sie ihn so, dass die SSL-Inspektion für IntelliJ-bezogene Domains umgangen wird (z. B. `plugins.jetbrains.com`, `repo.maven.apache.org`).

### Option 5: Problematiche Zertifikate debuggen und identifizieren
Wenn das Problem weiterhin besteht, identifizieren Sie, welcher Server oder welches Zertifikat die Aufforderung verursacht:

1. Ausführliche SSL-Protokollierung aktivieren:
   - Gehen Sie zu `Help > Edit Custom VM Options` und fügen Sie hinzu:
     ```
     -Djavax.net.debug=ssl:handshake:verbose
     ```
   - Starten Sie IntelliJ neu und überprüfen Sie die `idea.log`-Datei (zu finden unter `~/.IntelliJIdea<version>/system/log/`) auf SSL-Fehler, wie z. B. `PKIX path building failed`. Dies zeigt den problematischen Server oder das problematische Zertifikat an.

2. Auf bestimmte Plugins oder Integrationen prüfen:
   - Plugins wie Maven, Gradle oder Versionskontrollsysteme (z. B. Git, SVN) verbinden sich möglicherweise mit Servern, die unterschiedliche Zertifikate verwenden. Deaktivieren Sie Plugins temporär, um das Problem einzugrenzen.
   - Stellen Sie für Maven sicher, dass das in `File > Settings > Build, Execution, Deployment > Build Tools > Maven > Runner` konfigurierte JDK die aktualisierte cacerts-Datei verwendet.

### Zusätzliche Hinweise
- **Sicherheitswarnung**: Das automatische Akzeptieren nicht vertrauenswürdiger Zertifikate ist bequem, aber in nicht-isolierten Netzwerken riskant. Verwenden Sie dies nur in vertrauenswürdigen Umgebungen.
- **Systemzeitsynchronisation**: Stellen Sie sicher, dass Ihre Systemuhr synchronisiert ist, da eine Abweichung Zertifikatsvalidierungsprobleme verursachen kann.
- **JetBrains Runtime (JBR)**: IntelliJ läuft auf seiner eigenen JBR, die möglicherweise nicht den Truststore des System-Java verwendet. Änderungen am `$JAVA_HOME/lib/security/cacerts` des Systems wirken sich nicht auf IntelliJ aus, es sei denn, sie sind explizit konfiguriert.
- **Anhaltende Aufforderungen**: Wenn die Aufforderungen nach dem Import des Zertifikats weiterhin bestehen, könnte dies an einem Plugin oder Dienst (z. B. JFrog, SonarQube) liegen, der einen anderen Truststore verwendet. Überprüfen Sie die Plugineinstellungen oder wenden Sie sich an Ihr IT-Team, um die vollständige Zertifikatskette zu erhalten.

### Empfohlener Ansatz
1. Versuchen Sie zuerst **Option 3** (Zertifikate über die IntelliJ-Benutzeroberfläche hinzufügen), da dies die sicherste und unkomplizierteste Methode ist.
2. Wenn das fehlschlägt, überprüfen Sie den Keystore-Pfad und die Konfiguration mit **Option 2**.
3. Verwenden Sie **Option 1** (automatisches Akzeptieren) nur als letzten Ausweg in einer vertrauenswürdigen Umgebung.
4. Wenn das Problem einen Proxy oder ein Antivirenprogramm betrifft, arbeiten Sie mit Ihrem IT-Team zusammen, um die korrekten CA-Zertifikate zu beschaffen und zu importieren.

Wenn Sie weiterhin Probleme haben, teilen Sie Details zum Zertifikat (z. B. Aussteller, Domain) oder alle Fehlermeldungen aus der `idea.log`-Datei mit, damit ich helfen kann, die Ursache weiter einzugrenzen.