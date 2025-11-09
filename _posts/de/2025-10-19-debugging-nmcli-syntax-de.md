---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Debugging von nmcli Syntax Fallstricken
translated: true
type: note
---

Ja, genau – Programmierung (besonders bei Shell-Befehlen, Subprozessen oder Tools wie `nmcli`) ist absolut voll von diesen pingeligen Syntax-Fallen. Es sind keine "Fehler" im Sinne eines kaputten Systems oder nicht behebbarer Bugs; es sind nur versionsspezifische Eigenarten oder undokumentierte Präferenzen in Kommandozeilenschnittstellen, die jeden irgendwann einmal zu Fall bringen. Tools entwickeln sich weiter, die Dokumentation hinkt hinterher und ein Buchstabe Unterschied (wie `iface` vs. `ifname`) kann alles stoppen. Es ist frustrierend, aber super häufig, und die Lösung ist normalerweise einfach, sobald man sie gefunden hat.

Aus der geteilten Ausgabe sieht es so aus, als ob das Skript genau auf dieses Problem bei mehreren Netzwerken gestoßen ist: `nmcli` hat `iface` als ungültiges Argument abgelehnt (was Sinn ergibt, da das offizielle Flag für die Angabe des Interface-Namens in Verbindungsbefehlen schon immer `ifname` war). Das Update, das du angewendet hast – der Wechsel zu `ifname {interface}` in Zeile 113 – sollte das Problem sauber beheben. Dieser Diff ist präzise und minimal, also kein Risiko, neue Nebenwirkungen einzuführen.

### Schneller Testvorschlag
Um die Korrektur zu überprüfen, ohne alle 35 Netzwerke erneut zu scannen, könntest du vorübergehend einen Debug-Print direkt nach dem `subprocess.run`-Aufruf in `test_wifi_connection` (ungefähr Zeile 114) hinzufügen:

```python
result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=timeout)
print(f"Debug: Ran '{cmd}' -> returncode: {result.returncode}, stdout: '{result.stdout}', stderr: '{result.stderr}'")  # Diese Zeile hinzufügen
```

Führe es nur für ein oder zwei SSIDs aus (z.B. durch temporäres Kürzen der Liste), und es sollte nun einen erfolgreichen Verbindungsversuch oder einen aussagekräftigeren Fehler (wie z.B. Authentifizierungsfehler) anzeigen, anstatt der Argument-Beschwerde.

Wenn du danach immer noch auf Probleme stößt (z.B. bei bestimmten Netzwerken wie "HONG GOR 1" oder den unbenannten mit `--`), poste die neue Ausgabe hier – es könnten Probleme mit der Passwortkodierung, versteckte Zeichen in den SSIDs oder sogar Treiber-Eigenarten auf deiner Hardware sein. Wir können von dort aus weiter iterieren. Wie sieht der nächste Durchlauf aus?