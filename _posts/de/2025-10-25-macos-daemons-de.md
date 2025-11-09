---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Standard-Daemon-Prozesse in macOS
translated: true
type: note
---

### Standard-Daemon-Prozesse in macOS

In macOS sind Daemon-Prozesse Hintergrunddienste, die ohne Benutzeroberfläche laufen und typischerweise beim Start oder bei Bedarf beginnen. Sie werden von **launchd** verwaltet, dem Init- und Dienstverwaltungssystem des Systems (PID 1). Daemons unterscheiden sich von Agents: Daemons laufen als root/systemweit (vor dem Login), während Agents benutzerspezifisch laufen (nach dem Login).

Standard-System-Daemons sind in Property-List-Dateien (.plist) definiert, die sich in `/System/Library/LaunchDaemons/` befinden. In einer Standardinstallation gibt es typischerweise etwa 300–350 davon (z. B. 339 unter macOS 10.14 Mojave), die alles von Netzwerkanbindung und Sicherheit bis hin zur Hardwareverwaltung abdecken. Vom Benutzer installierte oder Drittanbieter-Daemons befinden sich in `/Library/LaunchDaemons/`.

#### So zeigen Sie Standard-Daemons an
Um alle geladenen Daemons (und Agents) im Terminal aufzulisten:
- `sudo launchctl list` (zeigt systemweite Daemons und Agents an).
- `launchctl list` (zeigt nur benutzerspezifische Agents an).

Für ein vollständiges Verzeichnislisting: `ls /System/Library/LaunchDaemons/` (benötigt kein sudo, aber die Dateien sind schreibgeschützt).

Diese Befehle geben Spalten wie PID, Status und Label aus (z. B. `com.apple.timed`).

#### Der "timed"-Daemon
Sie haben speziell "timed" erwähnt, was sich auf **com.apple.timed** (den Time Sync Daemon) bezieht. Dies ist ein zentraler System-Daemon, der in macOS High Sierra (10.13) eingeführt wurde, um den älteren `ntpd`-Prozess zu ersetzen.

- **Zweck**: Er synchronisiert automatisch die Systemuhr des Macs mit NTP-Servern (Network Time Protocol) für Genauigkeit und fragt diese alle 15 Minuten ab. Dies gewährleistet präise Zeitmessung für Protokolle, Zertifikate und Netzwerkoperationen.
- **Funktionsweise**: Wird von launchd aus `/System/Library/LaunchDaemons/com.apple.timed.plist` gestartet und läuft als `_timed`-Benutzer (in den Gruppen `_timed` und `_sntpd`). Er verwendet den `settimeofday`-Systemaufruf, um die Uhr basierend auf Serverantworten anzupassen. Die Konfiguration befindet sich in `/etc/ntpd.conf` (NTP-Server) und der Zustand wird in `/var/db/timed/com.apple.timed.plist` zwischengespeichert.
- **Zusammenhang**: Verknüpft mit Systemeinstellungen > Allgemein > Datum & Uhrzeit > "Datum und Uhrzeit automatisch einstellen". Wenn dies deaktiviert ist, synchronisiert timed nicht. Für erweiterte Einrichtungen (z. B. Hochpräzisionsanforderungen) können Tools wie Chrony es ersetzen, aber dann muss timed deaktiviert werden.

Wenn Ihre Uhr abweicht, prüfen Sie auf Netzwerkprobleme oder Firewall-Blockaden für NTP (UDP-Port 123).

#### Andere häufige Standard-Daemons ("usw.")
Hier ist eine Tabelle einiger häufig laufender Standard-System-Daemons, gruppiert nach Funktion. Diese ist nicht vollständig (es gibt Hunderte), deckt aber die wesentlichen ab. Die Labels stammen aus den .plist-Dateinamen.

| Kategorie       | Daemon-Label                  | Beschreibung |
|----------------|-------------------------------|-------------|
| **Kernsystem** | `com.apple.launchd`          | Der launchd-Prozess selbst; startet alle anderen. |
| **Zeit & Sync** | `com.apple.timed`             | NTP-Zeitsynchronisation (wie oben). |
| **Benutzerverwaltung** | `com.apple.opendirectoryd`   | Verwaltet Benutzer-/Gruppenkonten und Verzeichnisdienste. |
| **Benutzerverwaltung** | `com.apple.accounts`         | Verwaltet Benutzerkonten und Authentifizierung. |
| **Netzwerk** | `com.apple.mDNSResponder`    | Bonjour/mDNS für die lokale Netzwerkerkennung (z. B. AirDrop). |
| **Netzwerk** | `com.apple.nesessionmanager` | Verwaltung von Netzwerkerweiterungen und VPN. |
| **Bluetooth/Drahtlos** | `com.apple.bluetoothd`      | Behandlung von Bluetooth-Geräten. |
| **iCloud/Sync** | `com.apple.cloudd`            | iCloud-Datensynchronisation und -Dienste. |
| **Sicherheit**   | `com.apple.securityd`        | Verwaltung von Keychain und Berechtigungsnachweisen (oft auch als Agent). |
| **Updates**    | `com.apple.softwareupdated`  | Bearbeitet Software-Updates und Katalogdownloads. |
| **Hardware**   | `com.apple.kextd`             | Laden und Verwaltung von Kernel-Erweiterungen. |
| **Protokollierung**    | `com.apple.systemnotificationd` | Systembenachrichtigungen und Protokollierung. |
| **MDM (falls aktiviert)** | `com.apple.mdmclient`     | Mobile Device Management-Client für Unternehmensumgebungen. |

Diese laufen kontinuierlich oder bei Auslösern, um macOS stabil zu halten. Falls einer fehlerhaft läuft (z. B. hohe CPU-Auslastung), können Sie ihn vorübergehend mit `sudo launchctl unload /System/Library/LaunchDaemons/com.apple.example.plist` entladen, aber vermeiden Sie Änderungen an Systemdateien.

Für eine vollständige, aktuelle Liste auf Ihrem Mac (Stand Oktober 2025, wahrscheinlich macOS 15 Sequoia oder später), führen Sie die oben genannten Befehle aus – die Versionen entwickeln sich mit Updates leicht weiter.

#### Referenzen
- [The macOS Process Journey — “timed” (Time Sync Daemon)](https://medium.com/@boutnaru/the-macos-process-journey-timed-time-sync-daemon-4898c8185b4b)
- [Daemons and Agents could be slowing down your Mac](https://appleinsider.com/inside/macos/tips/daemons-and-agents-could-be-slowing-down-your-mac)
- [What files are included in the /System/Library/LaunchAgents and /System/Library/LaunchDaemons](https://apple.stackexchange.com/questions/361029/what-files-are-included-in-the-system-library-launchagents-and-system-library)
- [Script management with launchd in Terminal on Mac](https://support.apple.com/guide/terminal/script-management-with-launchd-apdc6c1077b-5d5d-4d35-9c19-60f2397b2369/mac)
- [How to show all running launchctl daemons/agents?](https://apple.stackexchange.com/questions/134817/how-to-show-all-running-launchctl-daemons-agents)