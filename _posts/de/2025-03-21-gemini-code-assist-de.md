---
audio: false
generated: true
lang: de
layout: post
title: Gemini Code Assist
translated: true
type: note
---

Um **Gemini Code Assist** zu verwenden, einen KI-gestützten Code-Assistenten, der von Google entwickelt wurde, können Sie ihn in Ihre Entwicklungsumgebung integrieren, z. B. in Visual Studio Code (VSCode), um Ihr Coding-Erlebnis zu verbessern. Gemini Code Assist hilft bei Code-Vervollständigung, Code-Generierung, Erklärungen, Debugging und mehr. Nachfolgend finden Sie eine Schritt-für-Schritt-Anleitung zur Einrichtung und Verwendung in VSCode.

---

### Schritt 1: Installieren der Gemini Code Assist-Erweiterung
- Öffnen Sie **VSCode**.
- Navigieren Sie zur **Erweiterungen-Ansicht**, indem Sie auf das Erweiterungen-Symbol in der Aktivitätsleiste klicken oder `Strg+Umschalt+X` (Windows/Linux) bzw. `Cmd+Umschalt+X` (macOS) drücken.
- Geben Sie in die Suchleiste **"Gemini Code Assist"** ein.
- Suchen Sie die offizielle Erweiterung im Marketplace, klicken Sie auf **Installieren** und starten Sie VSCode bei Aufforderung neu.

---

### Schritt 2: Melden Sie sich mit Ihrem Google-Konto an
- Suchen Sie nach der Installation nach dem **Gemini Code Assist-Symbol** in der Aktivitätsleiste (auf der linken Seite von VSCode).
- Klicken Sie auf das Symbol, um den Gemini-Bereich zu öffnen.
- Wählen Sie **"Mit Google anmelden"** und folgen Sie den Authentifizierungsaufforderungen mit Ihrem Google-Konto.
  - Für die **kostenlose Version** (Gemini Code Assist für Privatpersonen) ist ein persönliches Gmail-Konto ausreichend.
  - Für die **Standard- oder Enterprise-Versionen** müssen Sie es möglicherweise mit einem Google Cloud-Projekt verknüpfen, in dem die notwendigen APIs aktiviert sind.

---

### Schritt 3: Beginnen Sie mit der Verwendung von Gemini Code Assist
Sobald Sie angemeldet sind, können Sie seine Funktionen auf verschiedene Weise nutzen:

#### a. Code-Vervollständigung
- Während Sie im Editor tippen, schlägt Gemini automatisch Code-Vervollständigungen vor.
- Nehmen Sie diese Vorschläge an, indem Sie die `Tab`-Taste (oder eine andere konfigurierte Taste) drücken.

#### b. Code-Generierung und Erklärungen per Chat
- Öffnen Sie den **Gemini-Bereich**, indem Sie auf sein Symbol in der Aktivitätsleiste klicken.
- Geben Sie eine Aufforderung in natürlicher Sprache ein, wie z. B.:
  - "Erkläre diesen Code"
  - "Generiere eine Funktion, um ein Array zu sortieren"
  - "Hilf mir, diesen Fehler zu debuggen"
- Um sich auf bestimmten Code zu beziehen, markieren Sie ihn im Editor, bevor Sie Ihre Aufforderung eingeben.
- Gemini wird im Chat-Bereich antworten, und Sie können generierten Code bei Bedarf in Ihre Datei einfügen.

#### c. Code-Transformation
- Rufen Sie das Schnellauswahl-Menü auf, indem Sie `Strg+I` (Windows/Linux) oder `Cmd+I` (macOS) drücken.
- Geben Sie einen Befehl wie `/generate function to create a Cloud Storage bucket` ein.
- Überprüfen Sie die vorgeschlagenen Änderungen in einer Diff-Ansicht und wenden Sie sie bei Bedarf an.

#### d. Inline-Vorschläge
- Während des Codings kann Gemini Inline-Vorschläge zum Vervollständigen von Zeilen oder Codeblöcken anbieten.
- Diese erscheinen während Sie tippen und können mit einem Tastendruck angenommen werden.

---

### Zusätzliche Tipps
- **Walkthrough**: Bei der ersten Verwendung sehen Sie möglicherweise eine Option, eine geführte Tour in VSCode zu starten. Dieser interaktive Leitfaden stellt die Funktionen der Erweiterung vor.
- **Unterstützte Sprachen**: Gemini Code Assist funktioniert mit allen Programmiersprachen in der Public Domain, wie z. B. Python, JavaScript und Java.
- **Validieren Sie Vorschläge**: Überprüfen Sie immer KI-generierten Code, da er gelegentlich plausibel, aber falsch sein kann.
- **Datenschutz**: Sie können die Datennutzungseinstellungen innerhalb der Erweiterung an Ihre Präferenzen anpassen.

---

### Mögliche Überlegungen
- **Netzwerk**: Wenn Sie sich hinter einem Proxy befinden, konfigurieren Sie die Netzwerkeinstellungen von VSCode entsprechend.
- **Nutzungslimits**: Die kostenlose Version bietet bis zu 6.000 codebezogene Anfragen und 240 Chat-Anfragen täglich, was für die meisten Benutzer ausreicht.
- **GitHub-Integration**: Für KI-gestützte Code-Reviews auf GitHub ist eine zusätzliche Einrichtung erforderlich, dies ist jedoch von der Kern-IDE-Funktionalität getrennt.

---

Indem Sie diese Schritte befolgen, können Sie Gemini Code Assist effektiv nutzen, um Ihre Coding-Aufgaben in VSCode zu optimieren. Weitere Details finden Sie in der offiziellen Dokumentation von Google.