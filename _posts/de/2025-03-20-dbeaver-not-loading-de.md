---
audio: false
generated: true
lang: de
layout: post
title: Lösung zur Behebung von DBeaver, die keine Schemas lädt
translated: true
type: note
---

Wenn Sie Schemas in einer IBM DB2-Datenbank mit Squirrel SQL unter Windows anzeigen können, aber DBeaver bei "loading item 0%" hängen bleibt, liegt das Problem wahrscheinlich daran, wie DBeaver Metadaten im Vergleich zu Squirrel SQL abruft. Im Folgenden finden Sie eine Schritt-für-Schritt-Anleitung zur Fehlerbehebung und Lösung dieses Problems:

---

#### 1. Überprüfen Sie den DB2-Treiber in DBeaver
DBeaver benötigt den korrekten Treiber, um eine Verbindung zu Ihrer IBM DB2-Datenbank herzustellen. Die Verwendung des falschen Treibers (z.B. "Db2 for LUW" vs. "Db2 for z/OS") kann Probleme beim Laden der Schemas verursachen.

- **Schritte**:
  1. Öffnen Sie DBeaver und klicken Sie mit der rechten Maustaste auf Ihre DB2-Verbindung im Database Navigator.
  2. Wählen Sie **Edit Connection**.
  3. Vergewissern Sie sich im Abschnitt "Driver", dass der ausgewählte Treiber Ihrer DB2-Umgebung entspricht (z.B. "Db2 for LUW" für Linux/Unix/Windows oder "Db2 for z/OS" für Mainframe).
  4. Wenn Sie unsicher sind, konsultieren Sie Ihren Datenbankadministrator oder die Dokumentation, um sicherzustellen, dass der richtige Treiber ausgewählt ist.
  5. Klicken Sie auf **Test Connection**, um zu überprüfen, ob die Verbindung funktioniert.

---

#### 2. Passen Sie die Eigenschaft "Metadata Source" an
DBeaver verwendet eine Eigenschaft namens "metadata source", um zu steuern, wie Schema- und Tabelleninformationen abgerufen werden. Für DB2 kann eine Anpassung dieser Einstellung Probleme beim Laden der Schemas beheben.

- **Schritte**:
  1. Öffnen Sie Ihre DB2-Verbindungseinstellungen in DBeaver (Rechtsklick auf die Verbindung > **Edit Connection**).
  2. Gehen Sie zum Tab **Driver Properties**.
  3. Suchen Sie die Eigenschaft "metadata source" (oder fügen Sie sie hinzu, falls sie nicht aufgeführt ist).
  4. Setzen Sie deren Wert auf `0`.
  5. Klicken Sie auf **OK**, um die Änderungen zu speichern.
  6. Verbinden Sie sich erneut mit der Datenbank und prüfen Sie, ob die Schemas geladen werden.

- **Warum das funktioniert**: Das Setzen von "metadata source" auf `0` vereinfacht, wie DBeaver Metadaten abruft, was Probleme speziell beim DB2-Schema-Abruf umgehen kann.

---

#### 3. Überprüfen Sie die Benutzerberechtigungen
Obwohl Squirrel SQL die Schemas anzeigt, könnte DBeaver die Datenbank anders abfragen und spezifische Berechtigungen für den Zugriff auf Metadaten benötigen.

- **Schritte**:
  1. Bestätigen Sie mit Ihrem Datenbankadministrator, dass Ihr Benutzerkonto Berechtigungen zum Anzeigen von Schemas und Metadaten in DB2 hat (z.B. `SELECT` auf Systemkatalogtabellen wie `SYSCAT.SCHEMATA`).
  2. Wenn die Berechtigungen nicht ausreichen, bitten Sie Ihren DBA, die notwendigen Rechte zu erteilen.
  3. Testen Sie die Verbindung erneut in DBeaver.

---

#### 4. Schließen Sie Netzwerk- oder Firewall-Probleme aus
Eine Netzwerkeinschränkung oder Firewall könnte verhindern, dass DBeaver die Schemadaten vollständig abrufen kann, selbst wenn Squirrel SQL funktioniert.

- **Schritte**:
  1. Stellen Sie sicher, dass der DB2-Server von Ihrem Windows-Rechner aus erreichbar ist (z.B. durch einen Ping auf den Server oder einen Test des Ports).
  2. Klären Sie mit Ihrem Netzwerkteam, ob keine Firewall-Regeln die DBeaver-Verbindung blockieren.
  3. Testen Sie, wenn möglich, DBeaver von einem anderen Rechner aus, um das Problem einzugrenzen.

---

#### 5. Aktualisieren Sie DBeaver auf die neueste Version
Ältere Versionen von DBeaver könnten Bugs enthalten, die das Laden von DB2-Schemas beeinträchtigen.

- **Schritte**:
  1. Gehen Sie in DBeaver zu **Help** > **Check for Updates**.
  2. Installieren Sie alle verfügbaren Updates.
  3. Starten Sie DBeaver neu und verbinden Sie sich erneut mit der Datenbank.

- **Alternative**: Laden Sie die neueste Version von der [DBeaver-Website](https://dbeaver.io/) herunter und installieren Sie sie neu, falls keine Updates verfügbar sind.

---

#### 6. Aktivieren Sie die Debug-Protokollierung für weitere Fehlerbehebung
Wenn die oben genannten Schritte das Problem nicht beheben, aktivieren Sie die Debug-Protokollierung, um spezifische Fehler während des Ladevorgangs der Schemas zu identifizieren.

- **Schritte**:
  1. Gehen Sie zu **Window** > **Preferences** > **DBeaver** > **Logging**.
  2. Aktivieren Sie die detaillierte Protokollierung und speichern Sie die Einstellungen.
  3. Verbinden Sie sich erneut mit der Datenbank und versuchen Sie, die Schemas zu laden.
  4. Überprüfen Sie die Protokolldateien (normalerweise im DBeaver-Workspace-Ordner) auf Fehlermeldungen bezüglich des DB2-Schema-Abrufs.
  5. Teilen Sie die Protokolle bei Bedarf mit dem DBeaver-Support oder einem Forum für weitere Unterstützung.

---

### Warum das passiert
- **DBeaver vs. Squirrel SQL**: DBeaver ist ein funktionsreicheres Tool und ruft zusätzliche Metadaten im Vergleich zum einfacheren Ansatz von Squirrel SQL ab. Dies kann zu Kompatibilitätsproblemen mit DB2 führen, wenn die Einstellungen nicht optimiert sind.
- **Gängige Lösung**: Das Anpassen von "metadata source" auf `0` ist eine bekannte Problemumgehung für DB2-Schema-Ladeprobleme in DBeaver.

---

### Nächste Schritte
Beginnen Sie mit den Schritten 1 und 2 (Treiberüberprüfung und Anpassung der Metadatenquelle), da dies die wahrscheinlichsten Lösungen sind. Wenn das Problem weiterhin besteht, fahren Sie mit den restlichen Schritten fort. Wenn keine der Maßnahmen funktioniert, erwägen Sie, Ihre Debug-Protokolle in der [DBeaver-Community](https://github.com/dbeaver/dbeaver/issues) zu veröffentlichen, um zusätzliche Hilfe zu erhalten.

Dies sollte das Problem "loading item 0%" beheben und es Ihnen ermöglichen, Schemas in DBeaver so anzuzeigen, wie Sie es in Squirrel SQL tun!