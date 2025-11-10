---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Bonnes pratiques pour la structure des répertoires de projet
translated: true
type: note
---

Bonne question.

La convention générale est la suivante :

* **`scripts/`** est destiné au code de votre application (les éléments que vous souhaitez exécuter en production ou dans le cadre de votre projet).
* **`tests/`** est destiné à votre code de test (les éléments qui valident la correction de vos scripts/modules).

Donc, si vous ajoutez un nouveau fichier de test, il doit normalement aller dans **`tests/llm/`**, et non dans `scripts/`.

Par exemple :

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

De cette façon, vos tests sont séparés de votre implémentation, et des outils comme `pytest` peuvent les découvrir facilement.

👉 Vous pouvez maintenant ajouter quelque chose comme :

```python
# tests/llm/test_basic.py
import pytest
from scripts.llm import utils

def test_addition():
    assert utils.add(2, 3) == 5
```

Puis exécuter :

```bash
pytest tests/llm/
```

Souhaitez-vous que je vous montre également comment configurer un `conftest.py` pour partager des fixtures entre vos fichiers `tests/llm/` ?