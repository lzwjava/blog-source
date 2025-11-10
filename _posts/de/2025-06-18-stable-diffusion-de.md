---
audio: false
generated: true
lang: de
layout: post
title: Stable Diffusion Proxy Problem
translated: true
type: note
---

Basierend auf dem Fehler und Ihrer Umgebung finden Sie hier die Lösung für das Problem "Unknown scheme for proxy URL":

### Lösung:
Der Fehler tritt auf, weil **`httpx` standardmäßig keine `socks://` Proxys unterstützt**. Sie haben zwei Möglichkeiten:

#### Option 1: SOCKS-Proxy-Referenz entfernen
1. Überprüfen Sie Ihre Umgebungsvariablen auf verirrte Proxy-Einstellungen:
   ```bash
   env | grep -i proxy
   ```
   Suchen Sie nach `socks://`-Referenzen (insbesondere `ALL_PROXY` oder `http_proxy`).

2. Setzen Sie die problematische Variable zurück (ersetzen Sie `VAR_NAME` mit dem tatsächlichen Namen, den Sie oben gefunden haben):
   ```bash
   unset VAR_NAME  # z.B., unset ALL_PROXY
   ```

#### Option 2: SOCKS-Unterstützung zu `httpx` hinzufügen
1. Aktivieren Sie Ihre Python-Virtual-Umgebung:
   ```bash
   source /home/lzw/Projects/stable-diffusion-webui/venv/bin/activate
   ```

2. Installieren Sie die erforderlichen Abhängigkeiten:
   ```bash
   pip install -U "httpx[socks]"
   ```

3. Deaktivieren Sie die Umgebung:
   ```bash
   deactivate
   ```

### Warum das passiert:
- Ihre Haupt-Proxys (`HTTP_PROXY/HTTPS_PROXY`) verwenden `http://` (unterstützt), aber etwas (wahrscheinlich eine andere App/ein anderes Skript) setzt einen `socks://` Proxy, den `httpx` ohne zusätzliche Pakete nicht verarbeiten kann.
- Der Stack-Trace zeigt, dass Gradio/`httpx` versucht, `socks://127.0.0.1:7891` zu verwenden, der nicht in Ihrer `checkproxy`-Ausgabe enthalten ist.

### Überprüfung:
Führen Sie nach der Fehlerbehebung aus:
```bash
./webui.sh
```
Der SOCKS-Proxy-Fehler sollte verschwinden.

> 💡 **Hinweis**: Wenn Sie keinen SOCKS-Proxy absichtlich eingerichtet haben, untersuchen Sie Anwendungen, die Proxys automatisch konfigurieren könnten (z.B. VPNs, Netzwerk-Manager oder Shell-Konfigurationsdateien wie `~/.bashrc`).

---

Der Fehler `Torch is not able to use GPU; add --skip-torch-cuda-test to COMMANDLINE_ARGS variable to disable this check` zeigt an, dass PyTorch, das von Stable Diffusion WebUI verwendet wird, keine kompatible GPU erkennen oder darauf zugreifen kann. Dies liegt wahrscheinlich an fehlenden CUDA-Bibliotheken, einer inkompatiblen GPU, Treiberproblemen oder einem Konfigurationsproblem. Im Folgenden finden Sie Schritte zur Behebung dieses Problems, angepasst an Ihre Umgebung (glibc 2.35, Python 3.10.12, GCC 11.4.0, wahrscheinlich Ubuntu 22.04 basierend auf der glibc-Version).

### Schritte zur Problembehebung

#### 1. **GPU- und CUDA-Kompatibilität überprüfen**
   - **Überprüfen Sie, ob Sie eine NVIDIA-GPU haben**:
     Führen Sie aus:
     ```bash
     lspci | grep -i nvidia
     ```
     Dies listet NVIDIA-Hardware auf. Wenn keine Ausgabe erscheint, hat Ihr System möglicherweise keine NVIDIA-GPU, und PyTorch benötigt eine NVIDIA-GPU für die CUDA-Unterstützung.
   - **Überprüfen Sie die NVIDIA-Treiberinstallation**:
     Führen Sie aus:
     ```bash
     nvidia-smi
     ```
     Wenn installiert, wird eine Tabelle mit GPU-Details angezeigt (z.B. Treiberversion, CUDA-Version). Wenn nicht, installieren Sie den NVIDIA-Treiber:
     ```bash
     sudo apt-get update
     sudo apt-get install nvidia-driver-<version> nvidia-utils-<version> -y
     ```
     Ersetzen Sie `<version>` durch den neuesten stabilen Treiber (z.B. `535` oder `550`). Finden Sie die passende Treiberversion mit:
     ```bash
     ubuntu-drivers devices
     sudo ubuntu-drivers autoinstall
     ```
   - **CUDA-Version überprüfen**:
     PyTorch benötigt CUDA-Bibliotheken. Überprüfen Sie die installierte CUDA-Version:
     ```bash
     nvcc --version
     ```
     Wenn nicht installiert, installieren Sie das CUDA Toolkit:
     ```bash
     sudo apt-get install nvidia-cuda-toolkit -y
     ```
     Alternativ laden Sie das neueste CUDA Toolkit von der NVIDIA-Website herunter (z.B. CUDA 11.8 oder 12.1) und folgen Sie deren Installationsanleitung.

#### 2. **PyTorch-Installation überprüfen**
   Der Fehler deutet darauf hin, dass PyTorch installiert ist, aber die GPU nicht verwenden kann. Stellen Sie sicher, dass Sie die korrekte PyTorch-Version mit CUDA-Unterstützung haben.
   - **PyTorch-Installation überprüfen**:
     Führen Sie aus:
     ```bash
     python3 -c "import torch; print(torch.__version__); print(torch.cuda.is_available())"
     ```
     Die erwartete Ausgabe sollte eine PyTorch-Version (z.B. `2.0.1`) und `True` für `torch.cuda.is_available()` enthalten. Wenn `False` ausgegeben wird, erkennt PyTorch die GPU nicht.
   - **PyTorch mit CUDA-Unterstützung neu installieren**:
     Für Python 3.10 und CUDA (z.B. 11.8) installieren Sie PyTorch in Ihrer Stable-Diffusion-Umgebung:
     ```bash
     cd /home/lzw/Projects/stable-diffusion-webui
     source venv/bin/activate
     pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
     ```
     Ersetzen Sie `cu118` durch Ihre CUDA-Version (z.B. `cu121` für CUDA 12.1). Überprüfen Sie die unterstützten Versionen auf der offiziellen PyTorch-Website.
   - **Nach der Neuinstallation überprüfen**:
     Führen Sie die Überprüfung erneut aus:
     ```bash
     python3 -c "import torch; print(torch.cuda.is_available()); print(torch.cuda.get_device_name(0))"
     ```

#### 3. **CUDA-Check umgehen (Vorübergehende Problemumgehung)**
   Wenn Sie Stable Diffusion ohne GPU-Unterstützung ausführen möchten (z.B. zum Testen auf der CPU), umgehen Sie den CUDA-Check, indem Sie `--skip-torch-cuda-test` zu den Befehlszeilenargumenten hinzufügen.
   - Bearbeiten Sie `webui-user.sh` (oder erstellen Sie sie, falls sie nicht existiert):
     ```bash
     nano /home/lzw/Projects/stable-diffusion-webui/webui-user.sh
     ```
     Fügen Sie die Zeile `COMMANDLINE_ARGS` hinzu oder modifizieren Sie sie:
     ```bash
     export COMMANDLINE_ARGS="--skip-torch-cuda-test"
     ```
     Speichern Sie und beenden Sie.
   - Führen Sie das Skript aus:
     ```bash
     ./webui.sh
     ```
     Dies ermöglicht es Stable Diffusion, auf der CPU zu laufen, aber die Leistung wird deutlich langsamer sein.

#### 4. **Sicherstellen, dass TCMalloc korrekt konfiguriert ist**
   Ihre Ausgabe zeigt, dass TCMalloc (`libtcmalloc_minimal.so.4`) erkannt und mit `LD_PRELOAD` verlinkt wird. Bestätigen Sie, dass es funktioniert:
   ```bash
   echo $LD_PRELOAD
   ```
   Wenn es `/lib/x86_64-linux-gnu/libtcmalloc_minimal.so.4` ausgibt, ist alles in Ordnung. Wenn nicht, setzen Sie es manuell:
   ```bash
   export LD_PRELOAD=/lib/x86_64-linux-gnu/libtcmalloc_minimal.so.4
   ```
   Oder fügen Sie es zu `webui-user.sh` hinzu:
   ```bash
   export LD_PRELOAD=/lib/x86_64-linux-gnu/libtcmalloc_minimal.so.4
   ```

#### 5. **Umgebungsvariablen und Pfade überprüfen**
   Stellen Sie sicher, dass Ihre Umgebung korrekt eingerichtet ist:
   - **LD_LIBRARY_PATH überprüfen**:
     CUDA-Bibliotheken müssen zugänglich sein. Fügen Sie sie bei Bedarf hinzu:
     ```bash
     export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
     ```
     Fügen Sie dies zu `~/.bashrc` oder `webui-user.sh` für Persistenz hinzu.
   - **Virtuelle Umgebung aktivieren**:
     Aktivieren Sie immer die Stable-Diffusion-Virtual-Umgebung vor der Ausführung:
     ```bash
     cd /home/lzw/Projects/stable-diffusion-webui
     source venv/bin/activate
     ```

#### 6. **Stable Diffusion WebUI aktualisieren**
   Ihre Version (`v1.10.1`, Commit `82a973c`) könnte Kompatibilitätsprobleme haben. Aktualisieren Sie auf die neueste Version:
   ```bash
   cd /home/lzw/Projects/stable-diffusion-webui
   git pull
   ```
   Installieren Sie dann die Abhängigkeiten neu:
   ```bash
   ./webui.sh
   ```

#### 7. **Fehlerbehebung**
   - **Wenn `nvidia-smi` fehlschlägt**: Installieren Sie den NVIDIA-Treiber neu oder überprüfen Sie auf GPU-Hardwareprobleme.
   - **Wenn PyTorch die GPU immer noch nicht erkennt**:
     - Stellen Sie sicher, dass CUDA und cuDNN korrekt installiert sind. Installieren Sie cuDNN, falls es fehlt:
       ```bash
       sudo apt-get install libcudnn8
       ```
     - Überprüfen Sie die Kompatibilität der CUDA-Version mit Ihrer GPU und PyTorch. Ältere GPUs (z.B. Kepler-Serie) unterstützen beispielsweise möglicherweise CUDA 12 nicht.
   - **Wenn Fehler bestehen bleiben**: Überprüfen Sie die Stable-Diffusion-Logs auf detaillierte Fehler:
     ```bash
     cat /home/lzw/Projects/stable-diffusion-webui/log/webui.log
     ```
     Teilen Sie spezifische Fehler für weitere Unterstützung mit.
   - **Hardware-Einschränkungen**: Wenn Ihre GPU zu alt ist (z.B. NVIDIA-GPUs vor 2016), unterstützt sie möglicherweise keine modernen CUDA-Versionen. Verwenden Sie in diesem Fall `--skip-torch-cuda-test` oder upgraden Sie Ihre GPU.

#### 8. **Anwendung ausführen**
   Nachdem Sie die Korrekturen angewendet haben, führen Sie die WebUI aus:
   ```bash
   cd /home/lzw/Projects/stable-diffusion-webui
   ./webui.sh
   ```
   Wenn Sie das GPU-Problem behoben haben, sollte der Fehler verschwinden. Wenn Sie `--skip-torch-cuda-test` verwenden, wird es auf der CPU laufen.

### Hinweise
- **Systeminfo**: Ihr Setup (glibc 2.35, Python 3.10.12, GCC 11.4.0) deutet auf Ubuntu 22.04 hin, das mit CUDA 11.8 oder 12.1 und aktuellen PyTorch-Versionen kompatibel ist.
- **Leistung**: Das Ausführen auf der CPU (mit `--skip-torch-cuda-test`) ist ein Fallback, wird aber langsam sein. Das Beheben der GPU-Unterstützung wird für Stable Diffusion empfohlen.
- **TCMalloc**: Das TCMalloc-Problem scheint basierend auf Ihrer Ausgabe behoben zu sein. Stellen Sie sicher, dass `LD_PRELOAD` gesetzt bleibt, wenn Sie speicherbezogene Probleme feststellen.

Wenn Sie immer noch Probleme haben oder Hilfe mit spezifischen Fehlermeldungen benötigen, geben Sie bitte zusätzliche Details an (z.B. GPU-Modell, CUDA-Version oder vollständige Logs), und ich kann die Lösung verfeinern!