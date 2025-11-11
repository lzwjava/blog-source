---
audio: false
generated: true
lang: de
layout: post
title: CUDA unter Windows verwenden
translated: true
type: note
---

Um NVIDIA CUDA auf Ihrem HP ZBook Studio 16 G11 zu verwenden, müssen Sie die folgenden Schritte ausführen. CUDA ermöglicht es Entwicklern, Anwendungen zu beschleunigen, indem sie die Leistung der GPU für die Parallelverarbeitung nutzen. So können Sie beginnen:

### Schritt 1: Hardware-Kompatibilität überprüfen
- Stellen Sie sicher, dass Ihr HP ZBook Studio 16 G11 mit einer kompatiblen NVIDIA GPU ausgestattet ist. Das ZBook Studio 16 G11 kann mit GPUs wie der NVIDIA RTX 3000 Ada Generation oder höher ausgeliefert werden, die CUDA unterstützen.

### Schritt 2: NVIDIA-Treiber installieren
- **Treiber herunterladen:** Besuchen Sie die [NVIDIA-Treiber-Download-Seite](https://www.nvidia.com/Download/index.aspx) und laden Sie die neuesten Treiber für Ihr spezifisches GPU-Modell herunter.
- **Treiber installieren:** Führen Sie das Installationsprogramm aus und befolgen Sie die Anweisungen auf dem Bildschirm, um die Treiber auf Ihrem System zu installieren.

### Schritt 3: CUDA Toolkit installieren
- **CUDA Toolkit herunterladen:** Gehen Sie zur [NVIDIA CUDA Toolkit-Website](https://developer.nvidia.com/cuda-downloads) und laden Sie die Version des CUDA Toolkits herunter, die zu Ihrem Betriebssystem passt.
- **CUDA Toolkit installieren:** Führen Sie das CUDA Toolkit-Installationsprogramm aus und befolgen Sie die Anweisungen. Stellen Sie sicher, dass Sie die geeigneten Optionen für Ihre Entwicklungsumgebung auswählen.

### Schritt 4: Umgebungsvariablen einrichten
- Während des Installationsvorgangs sollten die notwendigen Umgebungsvariablen automatisch eingerichtet werden. Möglicherweise müssen Sie die CUDA-Binärdateien jedoch manuell zum PATH Ihres Systems hinzufügen, falls dies nicht automatisch geschieht.
- Unter Windows können Sie dies tun, indem Sie zu `Systemsteuerung > System und Sicherheit > System > Erweiterte Systemeinstellungen > Umgebungsvariablen` gehen und den Pfad zum CUDA-Bin-Verzeichnis hinzufügen (z. B. `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\vX.X\bin`).

### Schritt 5: Installation überprüfen
- Öffnen Sie eine Eingabeaufforderung oder ein Terminal und geben Sie `nvidia-smi` ein. Dieser Befehl sollte Informationen zu Ihrer GPU anzeigen und bestätigen, dass die Treiber korrekt installiert sind.
- Geben Sie `nvcc --version` ein, um die Version des CUDA-Compilers zu überprüfen. Dies bestätigt, dass das CUDA Toolkit korrekt installiert ist.

### Schritt 6: CUDA-Anwendungen entwickeln und ausführen
- **CUDA-Code schreiben:** Sie können CUDA-Programme in C, C++, Python oder Fortran schreiben. NVIDIA bietet umfangreiche Dokumentation und Beispielcodes, um Ihnen den Einstieg zu erleichtern.
- **CUDA-Code kompilieren:** Verwenden Sie den `nvcc`-Compiler, um Ihre CUDA-Programme zu kompilieren. Wenn Sie beispielsweise ein CUDA-Programm namens `my_program.cu` haben, können Sie es mit dem Befehl `nvcc my_program.cu -o my_program` kompilieren.
- **CUDA-Code ausführen:** Führen Sie Ihr kompiliertes Programm über die Befehlszeile aus. Zum Beispiel `./my_program` unter Linux oder `my_program.exe` unter Windows.

### Schritt 7: CUDA-Bibliotheken verwenden
- NVIDIA bietet mehrere für CUDA optimierte Bibliotheken an, wie z. B. cuBLAS für lineare Algebra, cuFFT für Fourier-Transformationen und cuDNN für tiefe neuronale Netze. Sie können diese Bibliotheken in Ihre Projekte einbinden, um vorgefertigte, optimierte Funktionen zu nutzen.

### Zusätzliche Ressourcen
- **NVIDIA Developer Zone:** Besuchen Sie die [NVIDIA Developer Zone](https://developer.nvidia.com/) für Tutorials, Dokumentation und Community-Support.
- **CUDA-Dokumentation:** Konsultieren Sie die [CUDA-Dokumentation](https://docs.nvidia.com/cuda/) für detaillierte Informationen zur CUDA-Programmierung und Best Practices.

Indem Sie diese Schritte befolgen, können Sie NVIDIA CUDA auf Ihrem HP ZBook Studio 16 G11 einrichten und verwenden, um Ihre Anwendungen zu beschleunigen und die Vorteile des GPU-Computings zu nutzen.