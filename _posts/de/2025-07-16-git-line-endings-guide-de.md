---
audio: false
generated: true
image: false
lang: de
layout: post
title: Leitfaden zur Kontrolle von Git-Zeilentrennzeichen
translated: true
type: note
---

`git config core.autocrlf` steuert, wie Git Zeilenenden behandelt, wenn Sie Dateien aus dem Repository auschecken und wenn Sie sie wieder eincommitten. Dies ist wichtig, weil Windows **CRLF** (`\r\n`) für Zeilenenden verwendet, während Linux und macOS **LF** (`\n`) verwenden. Ohne diese Behandlung könnten Dateien je nach Bearbeiter zwischen den Formaten wechseln, was zu "unsauberen" Diffs und unnötigen Änderungen führt.

---

### So funktioniert es

*   **Beim Auschecken (Lesen)** einer Datei kann Git Zeilenenden konvertieren, um der Konvention Ihres Betriebssystems zu entsprechen (damit sie in Ihrem Editor natürlich aussehen).
*   **Beim Committen (Schreiben)** einer Datei kann Git Zeilenenden zurück zu LF konvertieren (dem plattformübergreifenden Standard in Repositories).

---

### Einstellungen

Sie setzen es mit:

```bash
git config --global core.autocrlf <value>
```

Die gängigen Werte:

*   `true`
    Konvertiert **LF → CRLF** beim Auschecken und **CRLF → LF** beim Committen.
    Am besten für **Windows-Entwickler**, die Code in Windows-Editoren bearbeiten.

*   `input`
    Dateien beim Auschecken **nicht** verändern, aber **CRLF → LF** beim Committen konvertieren.
    Am besten für **Linux/macOS-Entwickler**, um LF-only Repositories sicherzustellen.

*   `false`
    Keine Konvertierung. Git speichert und checkt Dateien genau so aus, wie sie sind.
    Am besten, wenn Ihr Team/Ihr Editor Zeilenenden konsistent handhabt.

---

### Typische Empfehlungen

*   **Windows**:

    ```bash
    git config --global core.autocrlf true
    ```
*   **Linux/macOS**:

    ```bash
    git config --global core.autocrlf input
    ```

Für gemischte Teams ist es auch gut, eine `.gitattributes`-Datei im Repository hinzuzufügen, um konsistente Zeilenenden zu erzwingen, z. B.:

```
* text=auto
```

---

Möchten Sie, dass ich Ihnen auch eine empfohlene **`.gitattributes`-Einrichtung** zeige, die gut für plattformübergreifende Teams funktioniert (damit Sie sich nicht nur auf `core.autocrlf` verlassen müssen)?