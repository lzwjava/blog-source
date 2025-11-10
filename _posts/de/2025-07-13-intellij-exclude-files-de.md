---
audio: false
generated: true
image: false
lang: de
layout: post
title: Ausschließen von Dateien in IntelliJ IDEA
translated: true
type: note
---

In IntelliJ IDEA können Sie Dateien oder Verzeichnisse ausschließen, damit sie nicht in Suchen, der Indizierung, Code-Vervollständigung oder Builds erscheinen. Es gibt mehrere Möglichkeiten, dies zu tun, abhängig von Ihrem Zweck:

---

### 1. Ein Verzeichnis als *Excluded* markieren

* Klicken Sie in der **Projektansicht** mit der rechten Maustaste auf den Ordner, den Sie ausschließen möchten.
* Wählen Sie **Mark Directory as → Excluded**.
* IDEA wird aufhören, ihn zu indizieren, sodass er nicht mehr in Suchen, der Navigation oder der Code-Analyse auftaucht.

Dies wird typischerweise für Build-Ausgabeverzeichnisse verwendet (`target/`, `out/`, `dist/`, etc.).

---

### 2. Von der Versionskontrolle ausschließen (VCS Ignore)

Wenn Sie nicht möchten, dass IDEA (und Git) bestimmte Dateien verfolgt:

* Erstellen oder bearbeiten Sie eine `.gitignore`-Datei in Ihrem Projekt.
* Fügen Sie dort die Verzeichnis- oder Dateinamen-Muster hinzu.
* IDEA erkennt die `.gitignore`-Datei und blendet sie bei VCS-Operationen aus.

---

### 3. Dateien von der Code-Analyse / Inspektionen ausschließen

* Gehen Sie zu **Einstellungen → Editor → Inspections**.
* Dort können Sie **Scopes** konfigurieren und Inspektionen nur bestimmten Dateigruppen zuweisen, während Sie andere ausschließen.

---

### 4. Vom Build ausschließen (Gradle/Maven)

Wenn Sie Gradle oder Maven verwenden, können Sie `build.gradle` oder `pom.xml` so konfigurieren, dass bestimmte Verzeichnisse (wie generierter Code oder Ressourcen) ausgeschlossen werden. IDEA berücksichtigt diese Build-Tool-Konfigurationen.

---

### 5. Bestimmte Dateitypen ausschließen

* Gehen Sie zu **Einstellungen → Editor → File Types**.
* Fügen Sie Muster (wie `*.log`, `*.tmp`) zur Liste "Ignore files and folders" hinzu.

---

👉 Kurzer Tipp: Wenn Ihr Ziel nur darin besteht, zu verhindern, dass IDEA Ressourcen für die Indizierung großer Ordner (wie `node_modules/`) verschwendet, ist die Option **Mark Directory as Excluded** die schnellste und effektivste.

Möchten Sie, dass ich Ihnen auch zeige, wie Sie Testverzeichnisse (wie `src/test/java`) von **Code Coverage**-Läufen in IDEA ausschließen?