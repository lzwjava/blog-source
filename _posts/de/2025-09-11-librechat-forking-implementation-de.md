---
audio: false
date: 2025-09-11
generated: true
image: false
lang: de
layout: post
model: mistralai/mistral-medium-3.1
title: Implementierung von Konversationsverzweigungen in LibreChat
translated: true
type: note
---

Gute Frage! **LibreChat** (v0.8.0-rc3) unterstützt **Conversation Forking** (Verzweigung) bereits seit einer Weile, und es funktioniert anders als die kürzliche Implementierung von OpenAI. Hier ist eine Erläuterung, wie es in LibreChat funktioniert und wie es sich zum Ansatz von ChatGPT verhält:

---

### **Wie Forking in LibreChat funktioniert**
1. **Manuelles Verzweigen**
   - LibreChat erlaubt es Ihnen, ein Gespräch **explizit an jedem Punkt zu verzweigen**, indem Sie auf die **"Fork"** Schaltfläche klicken (üblicherweise in der Nähe der Nachricht, von der aus Sie verzweigen möchten).
   - Dies erstellt eine **neue Unterhaltung**, die von der ausgewählten Nachricht ausgeht und den gesamten vorherigen Kontext bis zu diesem Punkt bewahrt.

2. **Unabhängige Pfade**
   - Nach dem Verzweigen beeinflussen Änderungen im neuen Zweig **nicht die ursprüngliche Unterhaltung**.
   - Sie können verschiedene Richtungen erkunden (z.B. Debugging-Ansätze, kreative Ideen), ohne den ursprünglichen Gesprächsfaden zu verlieren.

3. **Kein Auto-Forking (Im Gegensatz zu ChatGPT)**
   - LibreChat **verzweigt Unterhaltungen nicht automatisch**, wenn Sie Nachrichten bearbeiten (im Gegensatz zum kürzlichen "Branch on Edit"-Feature von ChatGPT).
   - Sie müssen **manuell** entscheiden, wann Sie verzweigen möchten.

4. **Backend-Implementierung**
   - LibreChat speichert den Gesprächsverlauf auf strukturierte Weise (z.B. unter Verwendung von `conversationId` und `parentMessageId` in seiner Datenbank).
   - Beim Verzweigen wird eine neue `conversationId` erstellt, während die übergeordneten Nachrichten bis zum Verzweigungspunkt wiederverwendet werden.

---

### **Vergleich mit ChatGPTs Forking**

| Merkmal               | LibreChat (v0.8.0-rc3)       | ChatGPT (Kürzliches Update)   |
|-----------------------|-----------------------------|-------------------------------|
| **Auslöser**          | Manuell (Klick auf "Fork")  | Automatisch (bei Nachrichtenbearbeitung) |
| **Anwendungsfall**    | Alternativen erkunden       | Wiederherstellung nach Bearbeitungen |
| **UI-Anzeige**        | Klare Zweigliste            | Unauffälliger "Bearbeitete Version anzeigen"-Hinweis |
| **Beständigkeit**     | In Datenbank gespeichert    | Vorläufig (Sitzungsbasiert?)  |
| **Multi-Branch**      | Ja (mehrere Forks)          | Eingeschränkt (einzelner Bearbeitungszweig) |

---

### **Warum LibreChat es früher hatte**
1. **Open-Source-Flexibilität**
   - LibreChat baut auf APIs wie der von OpenAI auf, fügt jedoch seine eigene **Konversationsverwaltungsebene** hinzu.
   - Forking war ein naheliegendes Feature für eine selbst gehostete Chat-Plattform, bei der Benutzer **volle Kontrolle** über ihren Gesprächsverlauf wünschen.

2. **Für Workflows konzipiert**
   - LibreChat zielt auf **Entwickler, Forscher und Teams** ab, die folgendes benötigen:
     - Verschiedene Prompts testen, ohne den Kontext zu verlieren.
     - KI-Antworten nebeneinander vergleichen.
     - An verzweigten Diskussionen zusammenarbeiten.

3. **Kein Vendor Lock-in**
   - Im Gegensatz zu ChatGPT (das Forking an das Backend von OpenAI bindet) funktioniert das Forking in LibreChat **unabhängig vom KI-Anbieter** (z.B. funktioniert es gleich für Claude, Gemini oder lokale Modelle).

---

### **Wie man Forking in LibreChat verwendet**
1. **Eine Unterhaltung verzweigen**:
   - Fahren Sie mit der Maus über eine Nachricht → Klicken Sie auf **"Fork"** (oder nutzen Sie das Konversationsmenü).
   - Ein neuer Chat wird geöffnet, der alle Nachrichten bis zu diesem Punkt enthält.

2. **Zweige verwalten**:
   - Nutzen Sie die **Seitenleiste**, um zwischen ursprünglichen und verzweigten Unterhaltungen zu wechseln.
   - Benennen Sie Zweige zur besseren Übersicht um (z.B. "Debugging Ansatz A" vs. "Ansatz B").

3. **Kontext zusammenführen (Fortgeschritten)**:
   - Während LibreChat nicht automatisch zusammenführt, können Sie wichtige Nachrichten zwischen Zweigen **kopieren und einfügen**.

---

### **Beispiel-Workflow**
1. Sie debuggen ein Python-Skript mit einer KI.
2. Bei Nachricht #5 verzweigen Sie, um einen **anderen Ansatz** zu testen.
3. Im ursprünglichen Zweig fahren Sie mit Ansatz A fort.
4. Im verzweigten Zweig testen Sie Ansatz B.
5. Vergleichen Sie später die Ergebnisse, ohne den Kontext erneut eingeben zu müssen.

---

### **Einschränkungen**
- **Kein Visueller Diff**: Im Gegensatz zu Git-Zweigen zeigt LibreChat (noch) keine Unterschiede zwischen Forks an.
- **Speicher**: Zu viele Forks können Ihre Datenbank aufblähen (räumen Sie alte Zweige regelmäßig auf).

---
### **Unter der Haube (Technisch)**
Das Forking von LibreChat basiert auf:
- **MongoDB/PostgreSQL**: Speichert Unterhaltungen mit `parentMessageId`-Referenzen.
- **Frontend-State**: React verwaltet aktive Zweige in der UI.
- **API-Abstraktion**: Funktioniert einheitlich über alle KI-Anbieter hinweg (OpenAI, Anthropic, etc.).

---
### **Zukünftige Verbesserungen (Möglicherweise in späteren Versionen)**
- **Auto-Fork bei Bearbeitungen** (wie bei ChatGPT).
- **Zweigvergleich** (Side-by-Side-Ansicht).
- **Zusammenführungsfunktionalität** (Kombinieren zweier Zweige).

Möchten Sie einen tieferen Einblick in einen bestimmten Teil (z.B. Datenbankschema, UI-Tricks oder Self-Hosting-Tipps)?