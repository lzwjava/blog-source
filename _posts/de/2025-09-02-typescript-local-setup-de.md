---
audio: false
generated: true
image: false
lang: de
layout: post
title: TypeScript Lokaler Einrichtungsleitfaden Schritte
translated: true
type: note
---

Um TypeScript lokal auszuführen, verwendest du normalerweise **npm** und den TypeScript-Compiler (`tsc`). Hier ist eine Schritt-für-Schritt-Anleitung:

---

### 1. Initialisiere dein Projekt

Falls du noch keine `package.json` hast:

```bash
npm init -y
```

Dies erstellt eine `package.json`, damit du Abhängigkeiten verwalten kannst.

---

### 2. Installiere TypeScript

Installiere es als eine Dev Dependency:

```bash
npm install typescript --save-dev
```

Falls du den TypeScript-Compiler (`tsc`) auch global verfügbar haben möchtest:

```bash
npm install -g typescript
```

---

### 3. Erstelle eine tsconfig.json

Erzeuge eine Standard-Konfigurationsdatei:

```bash
npx tsc --init
```

Dies erstellt `tsconfig.json`, die steuert, wie TypeScript deine Dateien kompiliert (Target, Modulsystem, Strict Mode, etc.).

---

### 4. Schreibe eine TypeScript-Datei

Beispiel `index.ts`:

```ts
function greet(name: string): string {
  return `Hello, ${name}!`;
}

console.log(greet("World"));
```

---

### 5. Kompiliere TypeScript

Führe aus:

```bash
npx tsc
```

Dies kompiliert alle `.ts`-Dateien gemäß `tsconfig.json`.

Oder, um nur eine einzelne Datei zu kompilieren:

```bash
npx tsc index.ts
```

Dies erzeugt eine `.js`-Datei (z.B. `index.js`).

---

### 6. Führe den kompilierten JavaScript-Code aus

Verwende Node.js:

```bash
node index.js
```

---

### 7. Optional: Automatische Kompilierung beim Speichern

Führe mit `--watch` aus, damit bei jeder Änderung neu kompiliert wird:

```bash
npx tsc --watch
```

---

👉 Das ist der Standard-Workflow:
`npm install` → `tsc` (kompilieren) → `node` (kompilierten Code ausführen).

---

Möchtest du, dass ich dir auch zeige, wie du die **manuelle Kompilierung umgehen** kannst, indem du TypeScript direkt mit `ts-node` ausführst?