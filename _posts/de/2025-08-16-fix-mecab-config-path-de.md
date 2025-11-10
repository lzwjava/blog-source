---
audio: false
generated: true
image: false
lang: de
layout: post
title: Beheben Sie MeCab-Konfigurationsdateipfad
translated: true
type: note
---

Ihr Fehler

```
RuntimeError: param.cpp(70) [ifs] no such file or directory: /usr/local/etc/mecabrc
```

bedeutet **MeCab kann seine Konfigurationsdatei nicht finden** (`mecabrc`).
Unter macOS, wenn Sie MeCab kürzlich über Homebrew installiert haben, wurde es wahrscheinlich unter `/opt/homebrew/` anstelle von `/usr/local/` installiert, aber die Python-Bindung sucht immer noch nach dem alten Pfad `/usr/local/etc/mecabrc`.

So können Sie das Problem beheben:

---

### 1. Finden Sie heraus, wo sich `mecabrc` tatsächlich befindet

Führen Sie aus:

```bash
brew list mecab
```

oder:

```bash
find /opt/homebrew -name mecabrc
```

Sie werden wahrscheinlich etwas sehen wie:

```
/opt/homebrew/etc/mecabrc
```

---

### 2. Weisen Sie MeCab den korrekten mecabrc-Pfad zu

Sie können den Pfad in Ihrem Python-Code angeben:

```python
import MeCab

t = MeCab.Tagger(f"-r /opt/homebrew/etc/mecabrc -d /opt/homebrew/lib/mecab/dic/ipadic")
print(t.parse("すもももももももものうち"))
```

---

### 3. Oder setzen Sie eine Umgebungsvariable

```bash
export MECABRC=/opt/homebrew/etc/mecabrc
```

Dann führen Sie Ihr Skript normal aus:

```bash
python try_mecab.py
```

---

### 4. Wenn Sie möchten, dass `/usr/local/etc/mecabrc` funktioniert

Sie können auch einen symbolischen Link erstellen:

```bash
sudo mkdir -p /usr/local/etc
sudo ln -s /opt/homebrew/etc/mecabrc /usr/local/etc/mecabrc
```

Aber der Ansatz mit der Umgebungsvariable ist sauberer.

---

Wenn Sie möchten, kann ich Ihnen auch einen **Homebrew Reinstall + ipadic Setup** Befehl geben, damit es ohne die Angabe von `-r` jedes Mal funktioniert. Auf diese Weise bleibt Ihr `try_mecab.py` sauber.