---
audio: false
generated: true
image: false
lang: de
layout: post
title: JAR-Quellcode in IntelliJ IDEA anzeigen
translated: true
type: note
---

In IntelliJ IDEA können Sie problemlos den Quellcode einer JAR-Datei einsehen. Es gibt mehrere Ansätze, je nachdem ob die JAR Quelldateien oder nur kompilierte `.class`-Dateien enthält:

---

### 1. JAR in IDEA öffnen

* Gehen Sie zu **Datei > Öffnen…**
* Wählen Sie die JAR-Datei aus.
* IDEA öffnet sie in der **Projektansicht** wie ein reguläres Archiv.
* Wenn die JAR `.java`-Quelldateien enthält, können Sie diese direkt durchsuchen.
* Wenn sie nur `.class`-Dateien enthält, wird IDEA diese automatisch in lesbaren Java-Code dekompilieren.

---

### 2. Quellen zu einer Bibliotheks-JAR hinzufügen

Wenn die JAR Teil einer Bibliothek ist (wie Maven- oder Gradle-Abhängigkeiten):

* Gehen Sie zu **Datei > Projektstruktur > Bibliotheken** (oder **Module > Abhängigkeiten**, falls modulespezifisch).
* Wählen Sie die JAR aus.
* Klicken Sie auf **Quellen anhängen…** und weisen Sie IDEA auf die `-sources.jar` hin (falls verfügbar).
* Jetzt zeigt IDEA die echten Quellen anstelle des nur dekompilierten Bytecodes.

---

### 3. Schnelle Navigation

* Halten Sie **Strg (Cmd auf macOS)** gedrückt und klicken Sie auf eine Klasse oder Methode, die aus der JAR stammt.
* Wenn keine Quellen angehängt sind, zeigt IDEA die dekompilierte Version an.
* Wenn Quellen angehängt sind, sehen Sie den originalen Java-Code.

---

### 4. Externe Dekompiler-Plugins (Optional)

IDEA hat bereits einen integrierten Dekompiler, aber Sie können Plugins wie **Fernflower** oder **CFR** installieren, wenn Sie alternative Dekompilierung wünschen.

---

👉 Normalerweise kann IDEA, wenn es sich um eine von Maven/Gradle verwaltete Abhängigkeit handelt, die `-sources.jar` automatisch aus dem Repository herunterladen und anhängen. Bei einer eigenständigen JAR müssen Sie Quellen manuell anhängen oder sich auf den Dekompiler verlassen.

Möchten Sie, dass ich auch erkläre, **wie man den Quellcode der JAR außerhalb von IDEA extrahiert** (mit Tools wie `jd-gui` oder `jar xf`), oder möchten Sie sich hauptsächlich auf die Arbeit innerhalb von IDEA beschränken?