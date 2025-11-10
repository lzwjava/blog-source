---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Corriger le chemin du fichier de configuration MeCab
translated: true
type: note
---

Votre erreur

```
RuntimeError: param.cpp(70) [ifs] no such file or directory: /usr/local/etc/mecabrc
```

signifie que **MeCab ne trouve pas son fichier de configuration** (`mecabrc`).
Sur macOS, si vous avez installé MeCab via Homebrew récemment, il est probablement installé sous `/opt/homebrew/` au lieu de `/usr/local/`, mais le binding Python cherche toujours l'ancien chemin `/usr/local/etc/mecabrc`.

Voici comment résoudre le problème :

---

### 1. Trouver où se trouve réellement `mecabrc`

Exécutez :

```bash
brew list mecab
```

ou :

```bash
find /opt/homebrew -name mecabrc
```

Vous verrez probablement quelque chose comme :

```
/opt/homebrew/etc/mecabrc
```

---

### 2. Indiquer le bon chemin à MeCab

Vous pouvez spécifier le chemin dans votre code Python :

```python
import MeCab

t = MeCab.Tagger(f"-r /opt/homebrew/etc/mecabrc -d /opt/homebrew/lib/mecab/dic/ipadic")
print(t.parse("すもももももももものうち"))
```

---

### 3. Ou définir une variable d'environnement

```bash
export MECABRC=/opt/homebrew/etc/mecabrc
```

Puis exécutez votre script normalement :

```bash
python try_mecab.py
```

---

### 4. Si vous voulez que `/usr/local/etc/mecabrc` fonctionne

Vous pouvez aussi créer un lien symbolique :

```bash
sudo mkdir -p /usr/local/etc
sudo ln -s /opt/homebrew/etc/mecabrc /usr/local/etc/mecabrc
```

Mais l'approche par variable d'environnement est plus propre.

---

Si vous voulez, je peux aussi vous donner une commande de **réinstallation Homebrew + configuration ipadic** pour que cela fonctionne sans spécifier `-r` à chaque fois. Ainsi votre `try_mecab.py` reste propre.