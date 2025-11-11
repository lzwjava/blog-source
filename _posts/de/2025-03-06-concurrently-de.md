---
audio: false
generated: true
lang: de
layout: post
title: Nebeneinander verwenden
translated: true
type: note
---

Es scheint, als würdest du nach der Verwendung von "concurrently" im Kontext der Frontend-Entwicklung fragen. Allerdings ist "concurrently" typischerweise ein Node.js-Paket, das verwendet wird, um mehrere Befehle oder Skripte gleichzeitig auszuführen, oft in einem Backend- oder Entwicklungs-Workflow-Kontext und nicht direkt im Frontend-Code. Meintest du, wie man es in einem Frontend-Projekt-Setup verwendet (z.B. zum Ausführen von Skripten), oder bezogst du dich auf etwas anderes wie nebenläufige Operationen in Frontend-JavaScript (z.B. Promises, async/await)? Ich gehe erstmal von Ersterem aus, aber kläre mich gerne auf!

### Verwendung von `concurrently` in einem Frontend-Projekt

Wenn du an einem Frontend-Projekt (z.B. mit React, Vue oder Angular) arbeitest, wird `concurrently` in der Entwicklung häufig verwendet, um mehrere Prozesse gleichzeitig auszuführen – wie das Starten eines Development-Servers und eines Build-Watchers. So kannst du es verwenden:

#### 1. Installiere `concurrently`
Installiere es zunächst als Dev-Dependency in deinem Projekt:
```bash
npm install --save-dev concurrently
```

#### 2. Füge Skripte zur `package.json` hinzu
Definiere die Skripte, die du parallel ausführen möchtest, in deiner `package.json`. Wenn du zum Beispiel einen Frontend-Dev-Server und einen CSS-Preprocessor wie Sass ausführst:
```json
{
  "scripts": {
    "start:frontend": "react-scripts start", // oder dein Frontend-Dev-Befehl
    "watch:css": "sass --watch src/styles:dist/styles",
    "dev": "concurrently \"npm run start:frontend\" \"npm run watch:css\""
  }
}
```

- `start:frontend`: Führt deinen Frontend-Development-Server aus (z.B. React, Vite, etc.).
- `watch:css`: Beobachtet und kompiliert deine CSS-Dateien.
- `dev`: Verwendet `concurrently`, um beide Befehle gleichzeitig auszuführen.

#### 3. Führe die parallelen Skripte aus
Führe in deinem Terminal einfach aus:
```bash
npm run dev
```
Dies startet sowohl den Frontend-Server als auch den CSS-Watcher gleichzeitig. Du siehst die Ausgabe beider Prozesse im selben Terminal, und `concurrently` hält sie gemeinsam am Laufen.

#### 4. Optionale Konfiguration
Du kannst `concurrently` mit Optionen anpassen, wie:
- `--kill-others`: Beendet alle Prozesse, wenn einer fehlschlägt.
- `--names`: Beschriftet jeden Prozess für eine klarere Ausgabe.

Beispiel mit Optionen in `package.json`:
```json
"dev": "concurrently --names \"Frontend,CSS\" --kill-others \"npm run start:frontend\" \"npm run watch:css\""
```
Die Ausgabe könnte so aussehen:
```
[Frontend] Starting frontend server...
[CSS] Watching CSS files...
```

#### Anwendungsfall im Frontend-Workflow
Stell dir vor, du baust eine React-App mit einem separaten API-Server:
- Frontend: `npm run start` (React-Dev-Server auf Port 3000).
- API: `npm run start:api` (z.B. Node.js-Server auf Port 5000).
Mit `concurrently` kannst du beide ausführen:
```json
"dev": "concurrently \"npm run start\" \"npm run start:api\""
```

### Falls du nebenläufiges JavaScript im Frontend meintest
Wenn du nach der Handhabung nebenläufiger Operationen im Frontend-Code gefragt hast (z.B. das gleichzeitige Abfragen mehrerer APIs), hier ein kurzes Beispiel mit `Promise.all`:
```javascript
async function fetchData() {
  const [userData, postsData] = await Promise.all([
    fetch('https://api.example.com/user').then(res => res.json()),
    fetch('https://api.example.com/posts').then(res => res.json())
  ]);
  console.log(userData, postsData);
}
fetchData();
```
Dies führt die API-Aufrufe gleichzeitig aus und wartet, bis beide aufgelöst sind.

### Kläre mich bei Bedarf auf!
Lass mich wissen, falls du mit "concurrently im Frontend" etwas anderes gemeint hast – wie eine bestimmte Bibliothek, ein Framework oder einen Anwendungsfall – und ich passe die Antwort weiter an!