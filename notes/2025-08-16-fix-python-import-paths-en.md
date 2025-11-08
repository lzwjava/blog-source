---
audio: false
generated: true
image: false
lang: en
layout: post
title: Fix Python Module Import Paths
translated: false
type: note
---

The short answer: you need `sys` here so you can modify the Python module search path (`sys.path`) before doing the `from scripts.create.delete import delete_md`.

---

### Why `sys` is needed

* Python looks for modules/packages to import in a list of directories stored in `sys.path`.
* By default, it contains:

  * The current script’s directory.
  * Standard library directories.
  * Installed site-packages.
* If your `scripts/create/delete.py` file isn’t in one of those default places, the import will fail with `ModuleNotFoundError`.

So the code does:

```python
sys.path.append(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)
```

That means:

* Take the current file’s absolute path (`__file__`).
* Go three directories up.
* Add that directory to `sys.path`.

After that, Python can resolve `scripts.create.delete` as if it were installed or in the project root.

---

### Without `sys`

If your project is laid out like:

```
project/
├── scripts/
│   └── create/
│       └── delete.py
└── tools/
    └── myscript.py   <-- you're running this one
```

and you run `myscript.py` directly, Python won’t automatically know that `project/` is the root. The import fails unless you either:

* Run it with `PYTHONPATH=...` (e.g., `PYTHONPATH=.. python myscript.py`), or
* Package the project and install it (`pip install -e .`), or
* Dynamically add the path in code with `sys.path.append(...)` (as done here).

---

👉 So `sys` is needed purely to **manipulate the import path at runtime**, letting you import modules relative to your project root.

Do you want me to also show you some **cleaner alternatives** to avoid messing with `sys.path` manually?