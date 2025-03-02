---
audio: false
generated: false
lang: de
layout: post
title: WebSphere Liberty Server Befehle
translated: true
---

Beim Verwalten eines WebSphere Liberty-Servers werden mehrere Befehle häufig verwendet, um wesentliche Aufgaben wie das Erstellen, Starten, Stoppen und Überwachen des Servers durchzuführen. Im Folgenden finden Sie eine Liste der am häufigsten verwendeten Befehle mit einer kurzen Beschreibung jedes Befehls:

- **`./server create <server_name>`**
  Erstellt eine neue Serverinstanz mit dem angegebenen Namen. Dieser Befehl richtet die erforderliche Verzeichnisstruktur und die Standardkonfigurationsdateien (z. B. `server.xml`) für den Server ein.

- **`./server start <server_name>`**
  Startet den Server im Hintergrund. Der Server läuft als Hintergrundprozess und Protokolle werden in die Protokolldateien des Servers geschrieben.

- **`./server stop <server_name>`**
  Stoppt eine laufende Serverinstanz. Dieser Befehl schaltet den Server ordnungsgemäß ab.

- **`./server status <server_name>`**
  Überprüft, ob der angegebene Server läuft. Er gibt den aktuellen Status (z. B. gestartet oder gestoppt) zurück.

- **`./server run <server_name>`**
  Startet den Server im Vordergrund. Dies ist nützlich zum Debuggen oder Überwachen, da die Serverausgabe direkt in der Konsole angezeigt wird.

- **`./server package <server_name>`**
  Paketiert den Server, einschließlich seiner Konfiguration und Anwendungen, in eine Zip-Datei. Dies ist hilfreich für die Bereitstellung des Servers in einer anderen Umgebung oder für Backup-Zwecke.

- **`./server debug <server_name>`**
  Startet den Server im Debug-Modus, sodass Sie einen Debugger an den Serverprozess anhängen können, um Probleme zu beheben.

Diese Befehle decken die grundlegenden Operationen ab, die zum effektiven Verwalten eines WebSphere Liberty-Servers benötigt werden. Für fortgeschrittene Aufgaben, wie das Installieren von Funktionen oder das Verwalten der Sicherheit, stehen zusätzliche Hilfsprogramme wie `featureUtility` oder `securityUtility` zur Verfügung, die jedoch weniger häufig im täglichen Betrieb verwendet werden.