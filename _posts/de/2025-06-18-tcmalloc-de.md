---
audio: false
generated: true
lang: de
layout: post
title: Beheben Sie den TCMalloc-Fehler
translated: true
type: note
---

Der Fehler "Cannot locate TCMalloc. Do you have tcmalloc or google-perftool installed on your system? (improves CPU memory usage)" weist darauf hin, dass die TCMalloc-Bibliothek, Teil von Googles gperftools, nicht installiert oder nicht korrekt auf Ihrem Linux-System konfiguriert ist. TCMalloc ist ein Memory Allocator, der die Leistung verbessern und den Speicherverbrauch verringern kann, insbesondere in Anwendungen wie Stable Diffusion. So beheben Sie dieses Problem:

### Schritte zur Behebung des TCMalloc-Fehlers

1.  **Installieren Sie TCMalloc und Google Perftools**
    Verwenden Sie je nach Ihrer Linux-Distribution den entsprechenden Paketmanager, um die erforderlichen Bibliotheken zu installieren.

    -   **Für Ubuntu/Debian-basierte Systeme**:
        ```bash
        sudo apt-get update
        sudo apt-get install libgoogle-perftools-dev libtcmalloc-minimal4 -y
        ```
        Dies installiert sowohl das vollständige `libgoogle-perftools-dev` (enthält TCMalloc) als auch `libtcmalloc-minimal4` (eine leichtgewichtige Version).

    -   **Für Fedora-basierte Systeme**:
        ```bash
        sudo dnf install gperftools-libs -y
        ```
        Dies installiert die notwendigen TCMalloc-Bibliotheken.

    -   **Für CentOS/RHEL-basierte Systeme**:
        ```bash
        sudo yum install gperftools-libs -y
        ```
        Falls das Paket in den Standard-Repositories nicht verfügbar ist, müssen Sie möglicherweise zuerst das EPEL-Repository aktivieren:
        ```bash
        sudo yum install epel-release
        sudo yum install gperftools-libs -y
        ```

2.  **Überprüfen Sie die Installation**
    Überprüfen Sie nach der Installation, ob TCMalloc installiert ist:
    ```bash
    dpkg -l | grep tcmalloc
    ```
    Sie sollten `libtcmalloc-minimal4` oder ähnliche Pakete aufgelistet sehen. Alternativ können Sie den Bibliothekspfad überprüfen:
    ```bash
    dpkg -L libgoogle-perftools-dev | grep libtcmalloc.so
    ```
    Dies zeigt den Pfad zur TCMalloc-Bibliothek an (z.B. `/usr/lib/libtcmalloc.so.4`).

3.  **Setzen Sie die LD_PRELOAD-Umgebungsvariable**
    Um sicherzustellen, dass Ihre Anwendung TCMalloc verwendet, setzen Sie die Umgebungsvariable `LD_PRELOAD` so, dass sie auf die TCMalloc-Bibliothek verweist. Dies kann temporär oder permanent erfolgen.

    -   **Temporär (für die aktuelle Sitzung)**:
        Führen Sie Ihre Anwendung mit gesetztem `LD_PRELOAD` aus:
        ```bash
        export LD_PRELOAD=/usr/lib/libtcmalloc.so.4
        ./launch.py
        ```
        Ersetzen Sie `/usr/lib/libtcmalloc.so.4` durch den tatsächlichen Pfad aus Schritt 2, falls dieser abweicht.

    -   **Permanent (für Stable Diffusion oder ähnliches)**:
        Wenn Sie ein Skript wie `webui.sh` (üblich bei Stable Diffusion) verwenden, bearbeiten Sie das Skript (z.B. `webui-user.sh`) und fügen Sie Folgendes hinzu:
        ```bash
        export LD_PRELOAD=libtcmalloc.so.4
        ```
        Speichern Sie die Datei und führen Sie das Skript erneut aus:
        ```bash
        ./webui.sh
        ```
        Alternativ können Sie es zu Ihrer Shell-Konfiguration hinzufügen (z.B. `~/.bashrc` oder `~/.zshrc`):
        ```bash
        echo 'export LD_PRELOAD=/usr/lib/libtcmalloc.so.4' >> ~/.bashrc
        source ~/.bashrc
        ```

4.  **Starten Sie die Anwendung neu**
    Nach der Installation von TCMalloc und dem Setzen von `LD_PRELOAD` starten Sie Ihre Anwendung neu:
    ```bash
    ./launch.py
    ```
    Der Fehler sollte nicht mehr auftreten und Sie könnten einen verbesserten Speicherverbrauch oder eine bessere Leistung feststellen.

5.  **Fehlerbehebung**
    -   **Falls der Bibliothekspfad falsch ist**: Wenn `LD_PRELOAD` fehlschlägt (z.B. "cannot open shared object file"), überprüfen Sie den genauen Bibliotheksnamen und -pfad:
        ```bash
        find /usr/lib -name "libtcmalloc*.so*"
        ```
        Aktualisieren Sie `LD_PRELOAD` mit dem korrekten Pfad (z.B. `libtcmalloc_minimal.so.4` bei Verwendung der Minimal-Version).
    -   **Falls der Fehler bestehen bleibt**: Stellen Sie sicher, dass die installierte TCMalloc-Version mit Ihrem System kompatibel ist (in Ihrem Fall glibc 2.35 und GCC 11.4.0). Falls die Probleme weiterhin bestehen, versuchen Sie, TCMalloc aus den Quellen zu installieren:
        ```bash
        git clone https://github.com/google/tcmalloc.git
        cd tcmalloc
        bazel build //tcmalloc:hello_main
        bazel run //tcmalloc:hello_main
        ```
        Befolgen Sie den TCMalloc Quickstart-Guide für detaillierte Anweisungen.
    -   **Speicherprobleme**: Wenn Sie Allokierungsfehler oder Abstürze feststellen, stellen Sie sicher, dass Ihr System über ausreichend Arbeitsspeicher verfügt und dass TCMalloc nicht mit anderen Allokatoren in Konflikt steht.

6.  **Optional: Überprüfen Sie die TCMalloc-Nutzung**
    Um zu bestätigen, dass TCMalloc funktioniert, können Sie ein einfaches Testprogramm ausführen oder den Speicherverbrauch mit Tools wie `top` oder `htop` überprüfen, während Ihre Anwendung läuft. TCMalloc reduziert typischerweise die Speicherfragmentierung und kann einen leichten Leistungsschub bieten.

### Zusätzliche Hinweise
-   **Warum TCMalloc?** TCMalloc ist ein leistungsstarker Memory Allocator, der die CPU-Speichernutzung und Fragmentierung verringert, insbesondere in Thread-Anwendungen wie Stable Diffusion. Es ist nicht zwingend erforderlich, kann aber die Leistung verbessern.
-   **Kompatibilität**: Ihr System (glibc 2.35, Python 3.10.12, GCC 11.4.0) ist mit den neuesten TCMalloc-Versionen kompatibel, daher sollten die oben genannten Schritte funktionieren. Wenn Sie eine selbst kompilierte Anwendung verwenden, stellen Sie sicher, dass sie mit TCMalloc-Unterstützung kompiliert wurde.
-   **Stable Diffusion-Kontext**: Dieser Fehler tritt häufig mit AUTOMATIC1111s Stable Diffusion WebUI auf. Die oben genannten Schritte, insbesondere die Installation von `libgoogle-perftools-dev` und das Setzen von `LD_PRELOAD`, sind bekannt dafür, das Problem zu beheben.

Wenn Sie auf spezifische Fehler stoßen oder Hilfe mit einer bestimmten Linux-Distribution benötigen, lassen Sie es mich wissen, und ich kann die Anweisungen weiter anpassen!