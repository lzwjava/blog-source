---
audio: false
generated: true
image: false
lang: de
layout: post
title: MacOS-Shellbefehle
translated: true
type: note
---

Hier sind 200 häufig verwendete macOS Shell-Befehle, kategorisiert für einen einfacheren Überblick. Diese Befehle sind nützlich für die Navigation im Dateisystem, die Dateiverwaltung, Systemüberwachung und mehr.

### Dateisystem-Navigation
- `ls` - Inhalt eines Verzeichnisses auflisten.
- `cd` - Das aktuelle Verzeichnis wechseln.
- `pwd` - Das aktuelle Arbeitsverzeichnis anzeigen.
- `tree` - Verzeichnisse als Baumstruktur anzeigen (falls installiert).

### Dateioperationen
- `cp` - Dateien oder Verzeichnisse kopieren.
- `mv` - Dateien oder Verzeichnisse verschieben oder umbenennen.
- `rm` - Dateien oder Verzeichnisse entfernen.
- `touch` - Eine leere Datei erstellen oder den Zeitstempel aktualisieren.
- `mkdir` - Ein neues Verzeichnis erstellen.
- `rmdir` - Ein leeres Verzeichnis entfernen.
- `ln` - Hard- und symbolische Links erstellen.
- `chmod` - Dateiberechtigungen ändern.
- `chown` - Dateibesitzer und Gruppe ändern.
- `cat` - Dateiinhalte anzeigen und verketten.
- `less` - Dateiinhalte seitenweise anzeigen.
- `more` - Dateiinhalte seitenweise anzeigen.
- `head` - Die ersten Zeilen einer Datei anzeigen.
- `tail` - Die letzten Zeilen einer Datei anzeigen.
- `nano` - Textdateien bearbeiten.
- `vi` - Textdateien bearbeiten.
- `vim` - Textdateien bearbeiten (erweiterte Version von `vi`).
- `find` - Dateien in einer Verzeichnishierarchie suchen.
- `locate` - Dateien schnell nach Namen finden.
- `grep` - Text mit Mustern durchsuchen.
- `diff` - Dateien zeilenweise vergleichen.
- `file` - Den Dateityp bestimmen.
- `stat` - Status einer Datei oder eines Dateisystems anzeigen.
- `du` - Speicherplatzverwendung einer Datei schätzen.
- `df` - Speicherplatzbelegung des Dateisystems anzeigen.
- `dd` - Eine Datei konvertieren und kopieren.
- `tar` - Dateien in einem Archiv speichern, auflisten oder extrahieren.
- `gzip` - Dateien komprimieren oder dekomprimieren.
- `gunzip` - Mit gzip komprimierte Dateien dekomprimieren.
- `zip` - Dateien packen und komprimieren.
- `unzip` - Komprimierte Dateien aus einem ZIP-Archiv extrahieren.
- `rsync` - Remote-Datei- und Verzeichnissynchronisation.
- `scp` - Dateien sicher zwischen Hosts kopieren.
- `curl` - Daten von oder zu einem Server übertragen.
- `wget` - Dateien aus dem Internet herunterladen.

### Systeminformationen
- `uname` - Systeminformationen anzeigen.
- `top` - Systemprozesse anzeigen.
- `htop` - Interaktiver Prozess-Viewer (falls installiert).
- `ps` - Eine Momentaufnahme der aktuellen Prozesse anzeigen.
- `kill` - Ein Signal an einen Prozess senden.
- `killall` - Prozesse nach Namen beenden.
- `bg` - Jobs im Hintergrund ausführen.
- `fg` - Jobs im Vordergrund ausführen.
- `jobs` - Aktive Jobs auflisten.
- `nice` - Ein Programm mit geänderter Scheduling-Priorität ausführen.
- `renice` - Priorität laufender Prozesse ändern.
- `time` - Die Ausführungszeit eines Befehls messen.
- `uptime` - Anzeigen, wie lange das System bereits läuft.
- `who` - Anzeigen, wer eingeloggt ist.
- `w` - Anzeigen, wer eingeloggt ist und was er tut.
- `whoami` - Den aktuellen Benutzernamen anzeigen.
- `id` - Benutzer- und Gruppeninformationen anzeigen.
- `groups` - Die Gruppen eines Benutzers anzeigen.
- `passwd` - Benutzerpasswort ändern.
- `sudo` - Einen Befehl als anderer Benutzer ausführen.
- `su` - Benutzer wechseln.
- `chroot` - Einen Befehl mit einem anderen Root-Verzeichnis ausführen.
- `hostname` - Den Hostnamen des Systems anzeigen oder setzen.
- `ifconfig` - Eine Netzwerkschnittstelle konfigurieren.
- `ping` - ICMP ECHO_REQUEST an Netzwerk-Hosts senden.
- `traceroute` - Die Route zu einem Netzwerk-Host verfolgen.
- `netstat` - Netzwerkstatistiken.
- `route` - Die IP-Routing-Tabelle anzeigen oder manipulieren.
- `dig` - DNS-Lookup-Dienstprogramm.
- `nslookup` - Interaktiv Internet-Nameserver abfragen.
- `host` - DNS-Lookup-Dienstprogramm.
- `ftp` - Internet-Dateiübertragungsprogramm.
- `ssh` - OpenSSH SSH-Client.
- `telnet` - Benutzeroberfläche für das TELNET-Protokoll.
- `nc` - Netcat, beliebige TCP- und UDP-Verbindungen und Listener.
- `iftop` - Bandbreitennutzung auf einer Schnittstelle anzeigen (falls installiert).
- `nmap` - Netzwerkerkundungstool und Security-/Port-Scanner (falls installiert).

### Festplattenverwaltung
- `mount` - Ein Dateisystem einhängen.
- `umount` - Ein Dateisystem aushängen.
- `fdisk` - Partitionstabellen-Manipulator für Linux.
- `mkfs` - Ein Linux-Dateisystem erstellen.
- `fsck` - Ein Linux-Dateisystem überprüfen und reparieren.
- `df` - Speicherplatzbelegung des Dateisystems anzeigen.
- `du` - Speicherplatzverwendung einer Datei schätzen.
- `sync` - Zwischengespeicherte Schreibvorgänge auf den persistenten Speicher synchronisieren.
- `dd` - Eine Datei konvertieren und kopieren.
- `hdparm` - Festplattenparameter abrufen/setzen.
- `smartctl` - SMART-fähige ATA/SCSI-3-Laufwerke steuern und überwachen (falls installiert).

### Paketverwaltung
- `brew` - Homebrew Paketmanager (falls installiert).
- `port` - MacPorts Paketmanager (falls installiert).
- `gem` - RubyGems Paketmanager.
- `pip` - Python Paketinstaller.
- `npm` - Node.js Paketmanager.
- `cpan` - Perl Paketmanager.

### Textverarbeitung
- `awk` - Mustererkennungs- und Verarbeitungssprache.
- `sed` - Stream-Editor zum Filtern und Transformieren von Text.
- `sort` - Zeilen von Textdateien sortieren.
- `uniq` - Doppelte Zeilen melden oder auslassen.
- `cut` - Abschnitte aus jeder Zeile von Dateien entfernen.
- `paste` - Zeilen von Dateien zusammenführen.
- `join` - Zeilen zweier Dateien an einem gemeinsamen Feld verbinden.
- `tr` - Zeichen übersetzen oder löschen.
- `iconv` - Text von einer Kodierung in eine andere konvertieren.
- `strings` - Druckbare Zeichenketten in Dateien finden.
- `wc` - Zeilen-, Wort- und Byte-Anzahl für jede Datei anzeigen.
- `nl` - Zeilen in Dateien nummerieren.
- `od` - Dateien in verschiedenen Formaten ausgeben.
- `xxd` - Einen Hexdump erstellen oder umgekehrt.

### Shell-Scripting
- `echo` - Eine Textzeile anzeigen.
- `printf` - Daten formatieren und ausgeben.
- `test` - Einen Ausdruck auswerten.
- `expr` - Ausdrücke auswerten.
- `read` - Eine Zeile von der Standardeingabe lesen.
- `export` - Eine Umgebungsvariable setzen.
- `unset` - Werte und Attribute von Shell-Variablen und -Funktionen aufheben.
- `alias` - Einen Alias für einen Befehl erstellen.
- `unalias` - Einen Alias entfernen.
- `source` - Befehle aus einer Datei in der aktuellen Shell ausführen.
- `exec` - Einen Befehl ausführen.
- `trap` - Signale und andere Ereignisse abfangen.
- `set` - Shell-Optionen und Positionsparameter setzen oder aufheben.
- `shift` - Positionsparameter verschieben.
- `getopts` - Positionsparameter parsen.
- `type` - Einen Befehl beschreiben.
- `which` - Einen Befehl lokalisieren.
- `whereis` - Die Binär-, Quell- und Handbuchseitendateien für einen Befehl lokalisieren.

### Entwicklungstools
- `gcc` - GNU Projekt C und C++ Compiler.
- `make` - Verzeichnisorientierter Makefile-Prozessor.
- `cmake` - Plattformübergreifender Makefile-Generator.
- `autoconf` - Configure-Skripte generieren.
- `automake` - Makefile.in-Dateien generieren.
- `ld` - Der GNU Linker.
- `ar` - Archive erstellen, modifizieren und daraus extrahieren.
- `nm` - Symbole aus Objektdateien auflisten.
- `objdump` - Informationen aus Objektdateien anzeigen.
- `strip` - Symbole aus Objektdateien entfernen.
- `ranlib` - Index für ein Archiv generieren.
- `gdb` - Der GNU Debugger.
- `lldb` - Der LLVM Debugger.
- `valgrind` - Instrumentierungs-Framework für den Bau dynamischer Analysetools (falls installiert).
- `strace` - Systemaufrufe und Signale verfolgen (falls installiert).
- `ltrace` - Bibliotheksaufrufe verfolgen (falls installiert).
- `perf` - Leistungsanalysetools für Linux.
- `time` - Die Ausführungszeit eines Befehls messen.
- `xargs` - Befehlszeilen aus der Standardeingabe erstellen und ausführen.
- `m4` - Makroprozessor.
- `cpp` - Der C-Präprozessor.
- `flex` - Fast Lexical Analyzer Generator.
- `bison` - Yacc-kompatibler Parser-Generator.
- `bc` - Eine Sprache für Berechnungen mit beliebiger Genauigkeit.
- `dc` - Ein Rechner mit beliebiger Genauigkeit.

### Versionskontrolle
- `git` - Verteiltes Versionskontrollsystem.
- `svn` - Subversion Versionskontrollsystem.
- `hg` - Mercurial verteiltes Versionskontrollsystem.
- `cvs` - Concurrent Versions System.

### Verschiedenes
- `man` - Die Online-Handbuchseiten formatieren und anzeigen.
- `info` - Info-Dokumente lesen.
- `apropos` - Die Handbuchseitennamen und -beschreibungen durchsuchen.
- `whatis` - Einzeilige Handbuchseitenbeschreibungen anzeigen.
- `history` - Die History-Liste anzeigen oder manipulieren.
- `yes` - Eine Zeichenkette wiederholt ausgeben, bis beendet.
- `cal` - Einen Kalender anzeigen.
- `date` - Das Datum und die Uhrzeit anzeigen oder setzen.
- `sleep` - Für eine bestimmte Zeit verzögern.
- `watch` - Ein Programm periodisch ausführen und die Ausgabe im Vollbildmodus anzeigen.
- `xargs` - Befehlszeilen aus der Standardeingabe erstellen und ausführen.
- `seq` - Eine Zahlenfolge ausgeben.
- `shuf` - Zufällige Permutationen generieren.
- `tee` - Von der Standardeingabe lesen und in die Standardausgabe und Dateien schreiben.
- `tput` - Ein Terminal initialisieren oder die terminfo-Datenbank abfragen.
- `stty` - Terminal-Zeileneinstellungen ändern und anzeigen.
- `clear` - Den Terminalbildschirm löschen.
- `reset` - Das Terminal in einen stabilen Zustand zurücksetzen.
- `script` - Ein Protokoll einer Terminalsitzung erstellen.
- `wall` - Eine Nachricht an alle Benutzer schreiben.
- `write` - Eine Nachricht an einen anderen Benutzer senden.
- `mesg` - Schreibzugriff auf Ihr Terminal steuern.
- `talk` - Mit einem anderen Benutzer sprechen.
- `ytalk` - Noch ein weiteres Talk-Programm (falls installiert).
- `crontab` - Crontab-Dateien für einzelne Benutzer verwalten.
- `at` - Befehle planen, die einmal zu einem späteren Zeitpunkt ausgeführt werden.
- `batch` - Befehle planen, die in einer Batch-Warteschlange ausgeführt werden.
- `nice` - Ein Programm mit geänderter Scheduling-Priorität ausführen.
- `renice` - Priorität laufender Prozesse ändern.
- `time` - Die Ausführungszeit eines Befehls messen.
- `ulimit` - Benutzerressourcenlimits setzen oder melden.
- `pr` - Textdateien für den Druck konvertieren.
- `lp` - Dateien an einen Drucker senden.
- `lpr` - Dateien drucken.
- `lpq` - Druckerwarteschlangenstatus anzeigen.
- `lprm` - Jobs aus der Druckerwarteschlange entfernen.
- `enscript` - Text zu PostScript, HTML oder RTF mit Syntax-Hervorhebung konvertieren (falls installiert).
- `a2ps` - Any to PostScript Filter.
- `ps2pdf` - PostScript zu PDF konvertieren.
- `pdf2ps` - PDF zu PostScript konvertieren.
- `gs` - Ghostscript Interpreter.
- `convert` - Zwischen Bildformaten konvertieren (falls installiert).
- `mogrify` - Bilder in der Größe ändern, drehen und transformieren (falls installiert).
- `exiftool` - Metadaten in Dateien lesen, schreiben und bearbeiten (falls installiert).
- `jpegoptim` - JPEG-Dateien optimieren (falls installiert).
- `optipng` - PNG-Dateien optimieren (falls installiert).

Diese Befehle decken ein breites Spektrum an Funktionalitäten ab und sind essenziell für Benutzer, die ihr macOS-System effizient über das Terminal verwalten und damit interagieren möchten.