---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Erstellen von Ubuntu-Benutzerkonten
translated: true
---

### Erstellen eines neuen Benutzers in Ubuntu Linux

Ubuntu bietet sowohl Befehlszeilen- als auch grafische Methoden zum Erstellen eines Benutzers. Der Befehlszeilenansatz ist unkompliziert und funktioniert auf allen Editionen (einschließlich Servern), während die GUI auf Desktop-Versionen verfügbar ist.

#### Befehlszeilenmethode (Empfohlen)
1. Öffnen Sie ein Terminal (Strg+Alt+T).
2. Führen Sie den folgenden Befehl aus und ersetzen Sie `username` durch Ihren gewünschten Benutzernamen:
   ```
   sudo adduser username
   ```
   - Sie werden aufgefordert, ein sicheres Passwort für den neuen Benutzer festzulegen.
   - Sie werden auch nach optionalen Details wie vollständigem Namen, Zimmernummer, Diensttelefon usw. gefragt. Drücken Sie die Eingabetaste, um diese zu überspringen, oder geben Sie die Informationen nach Bedarf ein.
3. (Optional) Um dem neuen Benutzer administrative (sudo) Berechtigungen zu erteilen:
   ```
   sudo usermod -aG sudo username
   ```
   - Dies fügt den Benutzer zur `sudo`-Gruppe hinzu, was ihm erlaubt, Befehle mit erweiterten Berechtigungen auszuführen.

Der neue Benutzer erhält ein Home-Verzeichnis unter `/home/username` und kann sich sofort anmelden.

#### Grafische Methode (Nur Desktop)
1. Öffnen Sie die **Einstellungen**-App (suchen Sie danach in der Aktivitätenübersicht).
2. Navigieren Sie zu **Benutzer** in der Seitenleiste.
3. Klicken Sie oben rechts auf **Entsperren** und geben Sie Ihr Admin-Passwort ein.
4. Klicken Sie auf **Benutzer hinzufügen**.
5. Füllen Sie die Felder für Kontotyp (Standard oder Administrator), vollständigen Namen, Benutzernamen und Passwort aus.
6. Klicken Sie auf **Hinzufügen**.

#### Überprüfung
- Wechseln Sie zum neuen Benutzer mit `su - username` oder melden Sie sich ab und wieder an.
- Überprüfen Sie Benutzer mit `cat /etc/passwd | grep username`.

Dieser Prozess funktioniert auf Ubuntu 24.04 LTS und späteren Versionen.

[Benutzerverwaltung - Ubuntu Server Dokumentation](https://documentation.ubuntu.com/server/how-to/security/user-management/)  
[Hinzufügen eines neuen Benutzerkontos - Ubuntu Dokumentation](https://help.ubuntu.com/stable/ubuntu-help/user-add.html.en)