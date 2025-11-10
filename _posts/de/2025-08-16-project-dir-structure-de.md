---
audio: false
generated: true
image: false
lang: de
layout: post
title: Beste Praktiken für die Projektverzeichnisstruktur
translated: true
type: note
---

Gute Frage.

Die allgemeine Konvention ist:

* **`scripts/`** ist für Ihren Anwendungscode (Dinge, die Sie in der Produktion oder als Teil Ihres Projekts ausführen möchten).
* **`tests/`** ist für Ihren Testcode (Dinge, die die Korrektheit Ihrer Skripte/Module validieren).

Wenn Sie also eine neue Testdatei hinzufügen, sollte diese normalerweise unter **`tests/llm/`** abgelegt werden, nicht unter `scripts/`.

Zum Beispiel:

```
scripts/
  llm/
    main.py
    utils.py
tests/
  llm/
    test_main.py
    test_utils.py
```

Auf diese Weise sind Ihre Tests von Ihrer Implementierung getrennt, und Tools wie `pytest` können sie leicht finden.

👉 Sie können jetzt etwa Folgendes hinzufügen:

```python
# tests/llm/test_basic.py
import pytest
from scripts.llm import utils

def test_addition():
    assert utils.add(2, 3) == 5
```

Und dann ausführen:

```bash
pytest tests/llm/
```

Möchten Sie, dass ich Ihnen auch zeige, wie Sie eine `conftest.py` einrichten können, um Fixtures über Ihre `tests/llm/`-Dateien hinweg zu teilen?