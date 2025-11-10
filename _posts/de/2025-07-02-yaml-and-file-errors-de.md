---
audio: false
generated: true
lang: de
layout: post
title: Beheben von Jekyll-YAML- und Dateifehlern
translated: true
type: note
---

Die ausgegebene Fehlermeldung zeigt zwei Arten von Problemen:

1.  **YAML Exception:** Dies weist auf ein Problem mit dem Front Matter (dem YAML-Block am Anfang) Ihrer Markdown-Dateien hin:

      * `/Users/lzwjava/projects/lzwjava.github.io/notes/2025-06-25-company-valuation-comparison-en.md`
      * `/Users/lzwjava/projects/lzwjava.github.io/notes/2025-06-25-top-companies-evolve-en.md`
        Der Fehler "did not find expected key while parsing a block mapping at line 2 column 1" deutet darauf hin, dass die YAML-Syntax in diesen Dateien fehlerhaft ist, wahrscheinlich fehlt ein Schlüssel oder die Einrückung ist im Front Matter nicht korrekt.

2.  **`Errno::ENOENT: No such file or directory @ rb_sysopen - /Users/lzwjava/projects/lzwjava.github.io/wandb/debug-internal.log`**: Dieser Fehler zeigt an, dass Jekyll versucht, auf eine Datei oder ein Verzeichnis zuzugreifen, die/das nicht existiert, konkret `/wandb/debug-internal.log`. Dabei könnte es sich um eine temporäre Datei oder eine Abhängigkeit eines anderen Tools (wie Weights & Biases - `wandb`) handeln, die Jekyll verarbeiten möchte.

Um Ihre Frage zu beantworten, wie Jekyll bestimmte Verzeichnisse ignorieren kann, können Sie die Option `exclude` in Ihrer `_config.yml`-Datei verwenden.

So gehen Sie vor:

1.  **Öffnen Sie Ihre `_config.yml`-Datei** (befindet sich im Stammverzeichnis Ihres Jekyll-Projekts).

2.  **Fügen Sie die `exclude`-Direktive hinzu oder ändern Sie sie.** Diese Direktive erwartet ein Array von Pfaden (Dateien oder Verzeichnissen), die Jekyll während des Build-Vorgangs ignorieren soll.

    Um beispielsweise das Verzeichnis `wandb` und alle anderen Verzeichnisse, die Sie ausschließen möchten, zu ignorieren, fügen Sie Folgendes zu Ihrer `_config.yml` hinzu:

    ```yaml
    exclude:
      - wandb/
      - some_other_directory/
      - another_file_to_ignore.md
    ```

    **Wichtige Hinweise:**

      * Stellen Sie sicher, dass Sie den nachgestellten Schrägstrich (`/`) für Verzeichnisse verwenden, um sicherzustellen, dass der gesamte Inhalt darin ignoriert wird.
      * Pfade sind relativ zum Stammverzeichnis Ihres Jekyll-Projekts.

**Behebung Ihrer spezifischen Fehler mit `exclude`:**

  * **Für den `wandb`-Verzeichnisfehler:** Wenn Sie `wandb/` zur `exclude`-Liste in Ihrer `_config.yml` hinzufügen, sollte dies verhindern, dass Jekyll versucht, Dateien darin zu lesen, und den `No such file or directory`-Fehler für `wandb/debug-internal.log` beheben.

  * **Für die YAML Exception:** Die `exclude`-Direktive behebt die YAML-Fehler in Ihren Markdown-Dateien nicht. Sie müssen **den Front Matter in `notes/2025-06-25-company-valuation-comparison-en.md` und `notes/2025-06-25-top-companies-evolve-en.md` manuell korrigieren**.

    **Typische Jekyll-Front-Matter-Struktur:**

    ```yaml
    ---
    layout: post
    title: "My Awesome Post"
    date: 2025-07-02 10:00:00 +0800
    categories: [notes, tech]
    tags: [jekyll, markdown]
    ---

    Your content goes here.
    ```

    Überprüfen Sie die in der YAML Exception genannten Dateien, um sicherzustellen, dass sie dieser Struktur folgen, insbesondere in Bezug auf die Einrückung und korrekte Schlüssel-Wert-Paare. Der Fehler "did not find expected key while parsing a block mapping at line 2 column 1" deutet darauf hin, dass gleich zu Beginn Ihres Front Matters etwas nicht stimmt, möglicherweise fehlt ein Schlüssel oder ein Leerzeichen steht an einer Stelle, wo ein Schlüssel sein sollte.

Nachdem Sie diese Änderungen an Ihrer `_config.yml` vorgenommen und Ihre Markdown-Dateien korrigiert haben, versuchen Sie, Ihren Jekyll-Build- oder Serve-Befehl erneut auszuführen.