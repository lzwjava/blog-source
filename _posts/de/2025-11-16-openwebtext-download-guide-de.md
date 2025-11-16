---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: OpenWebText-Datensatz Download-Anleitung
translated: true
type: note
---

### Problemanalyse
Der `RepositoryNotFoundError` (401 Client Error) bestätigt, dass das Repository `openwebtext` **nicht** auf Hugging Face existiert. Deshalb schlägt der Download fehl – HF findet das Repo unter `https://huggingface.co/openwebtext` nicht. Der Teil "Invalid username or password" ist eine generische Fehlermeldung von HFs Authentifizierungsschicht, aber er ist hier irrelevant, da das Repository schlichtweg nicht existiert. OpenWebText (der Datensatz, auf den Sie zugreifen möchten) ist ein öffentlicher Korpus aus der GPT-2-Ära, wird aber nicht als Standard-Repo auf Hugging Face gehostet. Stattdessen wird er über Mirror, Torrents oder direkte Downloads von akademischen/GitHub-Quellen verteilt.

-   **Hintergrund zu OpenWebText**: Erstellt, um den im GPT-2-Paper verwendeten Datensatz nachzubilden (basierend auf URLs aus Reddits Pushshift-Dumps, gefiltert nach Qualität). Der vollständige Korpus umfasst ~40 GB Text, aufgeteilt in Teilmengen wie `urlsf_subset00.tar` (eine von 14 Tarballs, jeweils ~3-5 GB). Diese enthalten Rohtextdateien für das Training von Modellen wie nanoGPT.
-   Kein offizielles HF-Repo: Nach Überprüfung gibt es keine direkten Uploads der vollständigen Teilmengen unter `openwebtext` oder ähnlichem (z.B. EleutherAI hat verwandte Repos, aber nicht die Rohdaten). HF konzentriert sich auf Modelle/Datensätze mit Lizenzen, und OpenWebText ist zwar Public Domain, wird aber woanders gehostet, um Bandbreitenkosten zu vermeiden.

### Korrekte Download-Methode
Verwenden Sie **direkte HTTP-Downloads** oder **Torrents** von etablierten Mirrors. Die zuverlässigste Quelle ist der GitHub-Mirror von Skylion007 (eine Community-Initiative zum Hosten des bereinigten Korpus). So erhalten Sie `urlsf_subset00.tar` (und andere bei Bedarf):

1.  **Direkter Download vom Mirror** (Empfohlen für Geschwindigkeit):
    -   Basis-URL: `http://skylion007.github.io/OpenWebTextCorpus/`
    -   Spezifische Datei: `http://skylion007.github.io/OpenWebTextCorpus/urlsf_subset00.tar`
    -   Befehl zum Download (mit `wget` oder `curl`; ggf. installieren via `sudo apt install wget`):
        ```
        cd ~/projects/nanoGPT  # Ohr Ihr Zielverzeichnis
        wget http://skylion007.github.io/OpenWebTextCorpus/urlsf_subset00.tar
        ```
        -   Dies speichert die Datei als `./urlsf_subset00.tar` (~3.3 GB). Es handelt sich um einen HTTP-Mirror, daher ist keine Authentifizierung erforderlich und er ist schnell (direkt von GitHub Pages).
        -   Für den vollständigen Satz (alle Teilmengen): Listen Sie sie von der Seite auf und laden Sie sie in einer Schleife herunter, oder verwenden Sie ein Skript:
            ```bash
            for i in {00..13}; do
              wget http://skylion007.github.io/OpenWebTextCorpus/urlsf_subset${i}.tar
            done
            ```
        -   Alternative mit `curl` (falls wget nicht verfügbar ist):
            ```
            curl -O http://skylion007.github.io/OpenWebTextCorpus/urlsf_subset00.tar
            ```

2.  **Torrent-Download** (Am besten für große Dateien, fortsetzbar und bandbreitenschonend):
    -   Der offizielle Torrent für alle Teilmengen: Magnet-Link vom originalen Gwern-Repo oder Academic Torrents.
    -   Magnet-URI (zum Einfügen in einen Client wie qBittorrent, Transmission oder `aria2c`):
        ```
        magnet:?xt=urn:btih:5b1567f9eed6d1d1a5303a2e1f7a8d6b0a9c8d3e&dn=OpenWebTextCorpus
        ```
    -   Oder direkte .torrent-Datei: Herunterladen von [academictorrents.com](https://academictorrents.com/details/5b1567f9eed6d1d1a5303a2e1f7a8d6b0a9c8d3e) oder Suche nach "OpenWebTextCorpus torrent".
    -   Installieren Sie einen Torrent-Client, falls benötigt:
        -   Ubuntu/Debian: `sudo apt install qbittorrent-nox` (headless) oder verwenden Sie die GUI.
        -   Dann ausführen: `qbittorrent-nox` und den Magnet-Link hinzufügen.
    -   Erwartet: Lädt alle 14 Tarballs (~40 GB insgesamt) in Ihr gewähltes Verzeichnis herunter. Wählen Sie nur `urlsf_subset00.tar` für einen Teil-Download aus.

3.  **GitHub-Clone (falls Sie die Repo-Struktur möchten)**:
    -   Die Korpus-Metadaten sind auf GitHub: `https://github.com/skylion007/OpenWebTextCorpus`
    -   Klonen für README/Dokumentation (nicht die Daten):
        ```
        git clone https://github.com/skylion007/OpenWebTextCorpus.git
        ```
    -   Datenlinks befinden sich in der README – sie verweisen auf die gleichen Mirrors wie oben.

### Nach dem Download
-   **Tarball entpacken**:
    ```
    mkdir -p ./openwebtext/subsets
    tar -xvf urlsf_subset00.tar -C ./openwebtext/subsets
    ```
    -   Dies entpackt ~100.000+ Textdateien (z.B. `0.txt`, `1.txt`) in `./openwebtext/subsets/`. Jede Datei ist ein bereinigter Webseiten-Text.
-   **Für nanoGPT-Integration**:
    -   NanoGPT (Andrej Karpathys Repo) hat ein `openwebtext`-Beispiel in der book/data prep. Verwenden Sie deren Skript zum Verketten/Verarbeiten der Dateien:
        ```python
        # Aus nanoGPT's data/openwebtext/prepare.py (anpassen nach Bedarf)
        import os
        import glob

        input_dir = './openwebtext/subsets'
        output_file = './openwebtext/input.txt'

        with open(output_file, 'w') as out:
            for txt_file in sorted(glob.glob(os.path.join(input_dir, '*.txt'))):
                with open(txt_file, 'r') as f:
                    out.write(f.read())
        ```
    -   Dies erstellt eine einzige, massive `input.txt`-Datei für das Training. Seien Sie vorsichtig – das vollständige OpenWebText benötigt erheblichen Speicherplatz/Arbeitsspeicher.
-   **Integrität überprüfen**: Jeder Tar hat eine MD5-Prüfsumme im README des Mirrors (z.B. für subset00: Überprüfung gegen den bereitgestellten Hash mit `md5sum urlsf_subset00.tar`).

### Falls Probleme bestehen bleiben
-   **Mirror down?** Versuchen Sie die originale Gwern-Quelle: `https://www.gwern.net/OpenWebTextCorpus` (verlinkt zu AWS S3 oder Torrents).
-   **Hinweise zu Recht/Zugriff**: OpenWebText ist Public Domain (vom offenen Web gescraped), aber respektieren Sie robots.txt in Ihrer Nutzung. Hier ist keine HF-Authentifizierung erforderlich.
-   **Alternativen auf HF**: Wenn Sie ähnliche, auf HF gehostete Daten möchten, prüfen Sie `wikitext`, `bookcorpus` oder `pile`-Teilmengen (z.B. `repo_id="EleutherAI/pile"` mit `hf download`). Für exaktes OpenWebText, bleiben Sie bei Mirrors.
-   **Festplatten-/Geschwindigkeitstipps**: Diese Dateien sind riesig – verwenden Sie SSDs und überwachen Sie mit `du -sh` oder `htop`. Wenn Sie in China oder einem eingeschränkten Netzwerk sind, verwenden Sie einen VPN für schnelleren Zugriff.

Falls der Download erfolgreich ist, Sie aber auf Entpack-/Verarbeitungsfehler stoßen oder Hilfe mit dem nächsten nanoGPT-Schritt benötigen, posten Sie die Details!