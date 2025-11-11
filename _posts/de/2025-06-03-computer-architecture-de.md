---
audio: false
generated: true
lang: de
layout: post
title: Bestimmung des Computertypus
translated: true
type: note
---

Um festzustellen, ob Ihr aktueller Computer eine 64-Bit-x86 (x64)- oder ARM64-Architektur verwendet, befolgen Sie diese Anweisungen basierend auf Ihrem Betriebssystem:

**Windows:**

1.  **Drücken Sie die Windows-Taste + R**, um den Dialog "Ausführen" zu öffnen.
2.  **Geben Sie `msinfo32` ein** und drücken Sie die Eingabetaste. Dadurch öffnet sich das Fenster "Systeminformationen".
3.  Suchen Sie im Fenster "Systeminformationen" nach dem Eintrag **"Systemtyp"**.
    * Wenn **"x64-basierter PC"** angezeigt wird, hat Ihr Computer einen 64-Bit-x86 (x64)-Prozessor.
    * Wenn **"ARM64-basierter PC"** angezeigt wird, hat Ihr Computer einen 64-Bit-ARM (ARM64)-Prozessor.

**macOS:**

1.  Klicken Sie auf das **Apple-Menü** in der linken oberen Ecke Ihres Bildschirms.
2.  Wählen Sie **"Über diesen Mac"**.
3.  Suchen Sie im Tab "Übersicht" nach den Angaben zu **"Prozessor"** oder **"Chip"**:
    * Wenn ein **Intel-Prozessor** aufgeführt ist (z. B. Intel Core i7, Intel Core i9), hat Ihr Mac einen 64-Bit-x86 (x64)-Prozessor.
    * Wenn ein **Apple Silicon Chip** aufgeführt ist (z. B. Apple M1, Apple M2, Apple M3), hat Ihr Mac einen ARM64-Prozessor.

**Linux:**

1.  Öffnen Sie ein **Terminal**-Fenster.
2.  Geben Sie den folgenden Befehl ein und drücken Sie die Eingabetaste:
    ```bash
    uname -m
    ```
3.  Die Ausgabe zeigt die Architektur an:
    * **`x86_64`** oder **`amd64`**: Dies weist auf einen 64-Bit-x86 (x64)-Prozessor hin.
    * **`aarch64`** oder **`arm64`**: Dies weist auf einen 64-Bit-ARM (ARM64)-Prozessor hin.
    * Andere Ausgaben könnten auf ein 32-Bit-System hinweisen (was heutzutage jedoch seltener vorkommt).

Basierend auf den von Ihnen aufgelisteten Komponenten für Ihren neuen Build ist der **Intel Core i9-13900KF** Prozessor ein **x64 (64-Bit x86)** Architektur-Prozessor. Daher wird der neue Computer, den Sie bauen, ein **x64-basiertes System** sein.