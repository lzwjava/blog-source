---
audio: false
generated: true
lang: de
layout: post
title: Ubuntu Ruhezustand Anleitung
translated: true
type: note
---

In Ubuntu können Sie Ihr System auf verschiedene Weise in den Schlaf- oder Ruhemodus versetzen:

## GUI-Methoden:
- **Obere rechte Ecke**: Klicken Sie auf das Energie-/Einstellungs-Symbol in der oberen Panel-Leiste und wählen Sie dann "Suspend" (Schlafmodus) oder "Hibernate" (Ruhemodus), falls verfügbar
- **Aktivitäten-Menü**: Drücken Sie die Super-Taste, geben Sie "power" oder "suspend" ein und wählen Sie die Energieoptionen

## Befehlszeilen-Methoden:
```bash
# Zum Suspendieren (Schlafmodus)
systemctl suspend

# Für Ruhemodus
systemctl hibernate

# Für Hybrid-Schlaf (Kombination aus beiden)
systemctl hybrid-sleep
```

## Tastaturkürzel:
- Viele Ubuntu-Systeme verwenden standardmäßig **Fn + Sleep-Taste** oder **Strg + Alt + Ende**
- Sie können diese anpassen unter Einstellungen > Tastatur > Shortcuts

## Wichtige Hinweise:
- **Sleep/Suspend**: Hält den RAM unter Strom, schnelles Aufwachen, verbraucht aber etwas Batterie
- **Hibernate**: Speichert alles auf die Festplatte und fährt herunter, langsameres Aufwachen, aber kein Stromverbrauch
- Hibernate ist möglicherweise auf neueren Ubuntu-Versionen aufgrund potenzieller Probleme mit einiger Hardware nicht standardmäßig aktiviert

Falls Hibernate nicht funktioniert, müssen Sie es möglicherweise zuerst aktivieren, indem Sie den Swap-Space konfigurieren und Systemeinstellungen bearbeiten. Sleep/Suspend sollte auf den meisten Systemen sofort funktionieren.