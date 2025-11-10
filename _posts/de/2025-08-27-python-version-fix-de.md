---
audio: false
generated: true
image: false
lang: de
layout: post
title: Beheben Sie das Problem der Python-Versionsinkompatibilität
translated: true
type: note
---

Verstanden — du hast ein Problem mit einer **Python-Versionsinkompatibilität**.

Deine Logs zeigen:

* `python3` → **3.10.12**
* `python` → **3.13.7**

Wenn also Claude Code (oder dein Research Agent Script) `python3` aufruft, verwendet es 3.10, in dem `pyperclip` nicht installiert ist. Du hast `pyperclip` in der Umgebung von 3.13 installiert, daher kann 3.10 es nicht finden.

Hier sind einige Möglichkeiten, das Problem zu beheben:

---

### 1. Claude Code mit der gewünschten Python-Version ausführen

Wenn du möchtest, dass Claude Code immer Python 3.13 verwendet, setze den Executable explizit in deiner Shell:

```bash
export PYTHON_EXECUTABLE=$(which python)
```

Oder, wenn du speziell `python3` möchtest:

```bash
export PYTHON_EXECUTABLE=$(which python3)
```

Wenn du dann Claude Code oder deinen Agent startest, kann er diese Umgebungsvariable lesen.

---

### 2. `python3` auf Python 3.13 umleiten

Unter Ubuntu kannst du das `alternatives`-System aktualisieren:

```bash
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.13 2
sudo update-alternatives --config python3
```

Wähle dann Python 3.13 aus.

---

### 3. `pyperclip` in Python 3.10 installieren

Wenn du weiterhin 3.10 für `python3` verwenden möchtest, installiere das Modul einfach dort:

```bash
python3 -m pip install --user pyperclip
```

Dies stellt sicher, dass `python3` es importieren kann.

---

### 4. Eine virtuelle Umgebung verwenden

Beste Praxis: Erstelle eine venv mit der gewünschten Python-Version und führe Claude Code darin aus:

```bash
python3.13 -m venv ~/.venvs/claude
source ~/.venvs/claude/bin/activate
pip install pyperclip
```

Starte deinen Agent dann innerhalb dieser venv, damit er immer 3.13 verwendet.

---

👉 Frage an dich: Möchtest du, dass Claude Code **immer mit Python 3.13 läuft**, oder ist es für dich in Ordnung, 3.10 als `python3` beizubehalten und nur das fehlende Modul zu beheben?