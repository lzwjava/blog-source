---
audio: false
lang: de
layout: post
title: macOS Shell-Befehle
translated: true
---

Hier sind 200 häufig verwendete macOS-Shell-Befehle, kategorisiert für eine einfachere Referenz. Diese Befehle sind nützlich für die Navigation im Dateisystem, das Verwalten von Dateien, die Systemüberwachung und mehr.

### Dateisystem-Navigation
- `ls` - Liste den Inhalt eines Verzeichnisses.
- `cd` - Wechselt das aktuelle Verzeichnis.
- `pwd` - Gibt das aktuelle Arbeitsverzeichnis aus.
- `tree` - Zeigt Verzeichnisse als Bäume an (wenn installiert).

### Dateioperationen
- `cp` - Kopiert Dateien oder Verzeichnisse.
- `mv` - Verschiebt oder benennt Dateien oder Verzeichnisse um.
- `rm` - Entfernt Dateien oder Verzeichnisse.
- `touch` - Erstellt eine leere Datei oder aktualisiert den Zeitstempel.
- `mkdir` - Erstellt ein neues Verzeichnis.
- `rmdir` - Entfernt ein leeres Verzeichnis.
- `ln` - Erstellt harte und symbolische Links.
- `chmod` - Ändert Dateiberechtigungen.
- `chown` - Ändert den Besitzer und die Gruppe einer Datei.
- `cat` - Fügt Dateiinhalte zusammen und zeigt sie an.
- `less` - Zeigt Dateiinhalte Seite für Seite an.
- `more` - Zeigt Dateiinhalte Seite für Seite an.
- `head` - Zeigt die ersten Zeilen einer Datei an.
- `tail` - Zeigt die letzten Zeilen einer Datei an.
- `nano` - Bearbeitet Textdateien.
- `vi` - Bearbeitet Textdateien.
- `vim` - Bearbeitet Textdateien (erweiterte Version von `vi`).
- `find` - Sucht nach Dateien in einer Verzeichnisstruktur.
- `locate` - Findet Dateien schnell nach Namen.
- `grep` - Sucht Text mit Mustern.
- `diff` - Vergleicht Dateien Zeile für Zeile.
- `file` - Bestimmt den Dateityp.
- `stat` - Zeigt den Status einer Datei oder eines Dateisystems an.
- `du` - Schätzt den Dateispeicherplatz.
- `df` - Berichtet über die Dateisystem-Diskplatznutzung.
- `dd` - Konvertiert und kopiert eine Datei.
- `tar` - Speichert, listet oder extrahiert Dateien in einem Archiv.
- `gzip` - Komprimiert oder dekomprimiert Dateien.
- `gunzip` - Dekomprimiert Dateien, die mit gzip komprimiert wurden.
- `zip` - Verpackt und komprimiert Dateien.
- `unzip` - Extrahiert komprimierte Dateien in einem ZIP-Archiv.
- `rsync` - Fernkopie und Synchronisation von Dateien und Verzeichnissen.
- `scp` - Sicheres Kopieren von Dateien zwischen Hosts.
- `curl` - Übertragt Daten von oder zu einem Server.
- `wget` - Lädt Dateien aus dem Web herunter.

### Systeminformationen
- `uname` - Gibt Systeminformationen aus.
- `top` - Zeigt Systemprozesse an.
- `htop` - Interaktiver Prozessbetrachter (wenn installiert).
- `ps` - Berichtet über einen Momentaufnahme der aktuellen Prozesse.
- `kill` - Sendet ein Signal an einen Prozess.
- `killall` - Tötet Prozesse nach Namen.
- `bg` - Führt Jobs im Hintergrund aus.
- `fg` - Führt Jobs im Vordergrund aus.
- `jobs` - Listet aktive Jobs auf.
- `nice` - Führt ein Programm mit geänderter Planungspriorität aus.
- `renice` - Ändert die Priorität laufender Prozesse.
- `time` - Zeitmessung der Ausführung eines Befehls.
- `uptime` - Zeigt an, wie lange das System läuft.
- `who` - Zeigt an, wer angemeldet ist.
- `w` - Zeigt an, wer angemeldet ist und was sie tun.
- `whoami` - Gibt den aktuellen Benutzernamen aus.
- `id` - Gibt Benutzer- und Gruppeninformationen aus.
- `groups` - Gibt die Gruppen an, in denen sich ein Benutzer befindet.
- `passwd` - Ändert das Benutzerpasswort.
- `sudo` - Führt einen Befehl als anderer Benutzer aus.
- `su` - Wechselt den Benutzer.
- `chroot` - Führt einen Befehl mit einem anderen Stammverzeichnis aus.
- `hostname` - Zeigt oder setzt den Hostnamen des Systems.
- `ifconfig` - Konfiguriert eine Netzwerkschnittstelle.
- `ping` - Sendet ICMP ECHO_REQUEST an Netzwerkhosts.
- `traceroute` - Verfolgt den Weg zu einem Netzwerkhost.
- `netstat` - Netzwerkstatistiken.
- `route` - Zeigt oder manipuliert die IP-Routing-Tabelle.
- `dig` - DNS-Abfrage-Tool.
- `nslookup` - Abfragen von Internet-Namensservern interaktiv.
- `host` - DNS-Abfrage-Tool.
- `ftp` - Internet-Dateiübertragungsprogramm.
- `ssh` - OpenSSH SSH-Client.
- `telnet` - Benutzeroberfläche für das TELNET-Protokoll.
- `nc` - Netcat, beliebige TCP- und UDP-Verbindungen und -Hörer.
- `iftop` - Zeigt die Bandbreitennutzung auf einer Schnittstelle an (wenn installiert).
- `nmap` - Netzwerk-Explorations-Tool und Sicherheits-/Port-Scanner (wenn installiert).

### Festplattenverwaltung
- `mount` - Mountet ein Dateisystem.
- `umount` - Mountet ein Dateisystem ab.
- `fdisk` - Partitionstabellensystem für Linux.
- `mkfs` - Erstellt ein Linux-Dateisystem.
- `fsck` - Überprüft und repariert ein Linux-Dateisystem.
- `df` - Berichtet über die Dateisystem-Diskplatznutzung.
- `du` - Schätzt den Dateispeicherplatz.
- `sync` - Synchronisiert zwischengespeicherte Schreibvorgänge mit dem persistenten Speicher.
- `dd` - Konvertiert und kopiert eine Datei.
- `hdparm` - Holt/Setzt Festplattenparameter.
- `smartctl` - Steuerung und Überwachung von SMART-fähigen ATA/SCSI-3-Laufwerken (wenn installiert).

### Paketverwaltung
- `brew` - Homebrew-Paketmanager (wenn installiert).
- `port` - MacPorts-Paketmanager (wenn installiert).
- `gem` - RubyGems-Paketmanager.
- `pip` - Python-Paketinstaller.
- `npm` - Node.js-Paketmanager.
- `cpan` - Perl-Paketmanager.

### Textverarbeitung
- `awk` - Musterabtast- und -verarbeitungs-Sprache.
- `sed` - Stream-Editor zum Filtern und Transformieren von Text.
- `sort` - Sortiert Zeilen von Textdateien.
- `uniq` - Berichtet oder unterdrückt wiederholte Zeilen.
- `cut` - Entfernt Abschnitte aus jeder Zeile von Dateien.
- `paste` - Fügt Zeilen von Dateien zusammen.
- `join` - Fügt Zeilen von zwei Dateien auf einem gemeinsamen Feld zusammen.
- `tr` - Übersetzt oder löscht Zeichen.
- `iconv` - Konvertiert Text von einer Kodierung in eine andere.
- `strings` - Findet druckbare Zeichenketten in Dateien.
- `wc` - Gibt Zeilen-, Wort- und Byteanzahlen für jede Datei aus.
- `nl` - Nummeriert Zeilen von Dateien.
- `od` - Dump-Dateien in verschiedenen Formaten.
- `xxd` - Erstellt eine Hexdump oder führt die Umkehrung durch.

### Shell-Skripting
- `echo` - Zeigt eine Textzeile an.
- `printf` - Formatiert und druckt Daten.
- `test` - Bewertet einen Ausdruck.
- `expr` - Bewertet Ausdrücke.
- `read` - Liest eine Zeile von der Standard-Eingabe.
- `export` - Setzt eine Umgebungsvariable.
- `unset` - Hebt Werte und Attribute von Shell-Variablen und -Funktionen auf.
- `alias` - Erstellt einen Alias für einen Befehl.
- `unalias` - Entfernt einen Alias.
- `source` - Führt Befehle aus einer Datei in der aktuellen Shell aus.
- `exec` - Führt einen Befehl aus.
- `trap` - Fängt Signale und andere Ereignisse ab.
- `set` - Setzt oder hebt Shell-Optionen und Positionsparameter auf.
- `shift` - Verschiebt Positionsparameter.
- `getopts` - Parsed Positionsparameter.
- `type` - Beschreibt einen Befehl.
- `which` - Sucht einen Befehl.
- `whereis` - Sucht die Binär-, Quell- und Handbuchseiten-Dateien für einen Befehl.

### Entwicklertools
- `gcc` - GNU-Projekt C- und C++-Compiler.
- `make` - Verzeichnisorientierter Makefile-Prozessor.
- `cmake` - Plattformübergreifender Makefile-Generator.
- `autoconf` - Generiert Konfigurationsskripte.
- `automake` - Generiert Makefile.in-Dateien.
- `ld` - Der GNU-Linker.
- `ar` - Erstellt, modifiziert und extrahiert aus Archiven.
- `nm` - Listet Symbole aus Objektdateien auf.
- `objdump` - Zeigt Informationen aus Objektdateien an.
- `strip` - Entfernt Symbole aus Objektdateien.
- `ranlib` - Generiert Index für Archiv.
- `gdb` - Der GNU-Debugger.
- `lldb` - Der LLVM-Debugger.
- `valgrind` - Instrumentierungsrahmenwerk zum Erstellen dynamischer Analyse-Tools (wenn installiert).
- `strace` - Verfolgt Systemaufrufe und Signale (wenn installiert).
- `ltrace` - Verfolgt Bibliotheksaufrufe (wenn installiert).
- `perf` - Leistungsanalyse-Tools für Linux.
- `time` - Zeitmessung der Ausführung eines Befehls.
- `xargs` - Erstellt und führt Befehlszeilen aus der Standard-Eingabe aus.
- `m4` - Makroprozessor.
- `cpp` - Der C-Preprozessor.
- `flex` - Schnell Lexikalischer Analysator-Generator.
- `bison` - Yacc-kompatibler Parser-Generator.
- `bc` - Eine Programmiersprache für beliebige Genauigkeit.
- `dc` - Eine Programmiersprache für beliebige Genauigkeit.

### Versionskontrolle
- `git` - Verteiltes Versionskontrollsystem.
- `svn` - Subversion-Versionskontrollsystem.
- `hg` - Mercurial verteiltes Versionskontrollsystem.
- `cvs` - Concurrent Versions System.

### Verschiedenes
- `man` - Formatiert und zeigt die Online-Handbuchseiten an.
- `info` - Liest Info-Dokumente.
- `apropos` - Sucht nach Handbuchseiten-Namen und -Beschreibungen.
- `whatis` - Zeigt eine einzeilige Handbuchseitenbeschreibung an.
- `history` - Zeigt oder manipuliert die Historie-Liste.
- `yes` - Gibt eine Zeichenkette wiederholt aus, bis sie getötet wird.
- `cal` - Zeigt einen Kalender an.
- `date` - Zeigt oder setzt Datum und Uhrzeit an.
- `sleep` - Verzögert um eine bestimmte Zeit.
- `watch` - Führt ein Programm periodisch aus, zeigt die Ausgabe im Vollbildmodus an.
- `xargs` - Erstellt und führt Befehlszeilen aus der Standard-Eingabe aus.
- `seq` - Druckt eine Zahlenfolge.
- `shuf` - Generiert zufällige Permutationen.
- `tee` - Liest von der Standard-Eingabe und schreibt in die Standard-Ausgabe und Dateien.
- `tput` - Initialisiert ein Terminal oder fragt die terminfo-Datenbank ab.
- `stty` - Ändert und druckt Terminalzeilen-Einstellungen.
- `clear` - Leert den Terminalbildschirm.
- `reset` - Setzt das Terminal in einen vernünftigen Zustand zurück.
- `script` - Erstellt einen Typskript der Terminal-Sitzung.
- `wall` - Schreibt eine Nachricht an alle Benutzer.
- `write` - Sendet eine Nachricht an einen anderen Benutzer.
- `mesg` - Steuert den Schreibzugriff auf Ihr Terminal.
- `talk` - Sprecht mit einem anderen Benutzer.
- `ytalk` - Noch ein Talk-Programm (wenn installiert).
- `crontab` - Pflegt crontab-Dateien für einzelne Benutzer.
- `at` - Plant Befehle, die einmal zu einem späteren Zeitpunkt ausgeführt werden sollen.
- `batch` - Plant Befehle, die in einer Batch-Warteschlange ausgeführt werden sollen.
- `nice` - Führt ein Programm mit geänderter Planungspriorität aus.
- `renice` - Ändert die Priorität laufender Prozesse.
- `time` - Zeitmessung der Ausführung eines Befehls.
- `ulimit` - Setzt oder berichtet über Benutzerressourcenlimits.
- `pr` - Konvertiert Textdateien zum Drucken.
- `lp` - Sendet Dateien an einen Drucker.
- `lpr` - Druckt Dateien.
- `lpq` - Zeigt den Druckerwarteschlangenstatus an.
- `lprm` - Entfernt Jobs aus der Druckerwarteschlange.
- `enscript` - Konvertiert Text in PostScript, HTML oder RTF mit Syntax-Hervorhebung (wenn installiert).
- `a2ps` - Jeder zu PostScript-Filter.
- `ps2pdf` - Konvertiert PostScript in PDF.
- `pdf2ps` - Konvertiert PDF in PostScript.
- `gs` - Ghostscript-Interpreter.
- `convert` - Konvertiert zwischen Bildformaten (wenn installiert).
- `mogrify` - Skaliert, dreht und transformiert Bilder (wenn installiert).
- `exiftool` - Liest, schreibt und bearbeitet Metainformationen in Dateien (wenn installiert).
- `jpegoptim` - Optimiert JPEG-Dateien (wenn installiert).
- `optipng` - Optimiert PNG-Dateien (wenn installiert).

Diese Befehle decken eine breite Palette von Funktionalitäten ab und sind für Benutzer, die ihr macOS-System effizient über das Terminal verwalten und damit interagieren möchten, unerlässlich.