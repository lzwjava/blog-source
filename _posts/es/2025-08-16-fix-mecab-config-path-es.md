---
audio: false
generated: true
image: false
lang: es
layout: post
title: Corregir Ruta del Archivo de Configuración de MeCab
translated: true
type: note
---

Tu error

```
RuntimeError: param.cpp(70) [ifs] no such file or directory: /usr/local/etc/mecabrc
```

significa que **MeCab no puede encontrar su archivo de configuración** (`mecabrc`).
En macOS, si instalaste MeCab a través de Homebrew recientemente, es probable que esté instalado bajo `/opt/homebrew/` en lugar de `/usr/local/`, pero el binding de Python sigue buscando en la ruta antigua `/usr/local/etc/mecabrc`.

Aquí te mostramos cómo solucionarlo:

---

### 1. Encuentra dónde está realmente `mecabrc`

Ejecuta:

```bash
brew list mecab
```

o:

```bash
find /opt/homebrew -name mecabrc
```

Probablemente verás algo como:

```
/opt/homebrew/etc/mecabrc
```

---

### 2. Dirige MeCab al mecabrc correcto

Puedes especificar la ruta en tu código Python:

```python
import MeCab

t = MeCab.Tagger(f"-r /opt/homebrew/etc/mecabrc -d /opt/homebrew/lib/mecab/dic/ipadic")
print(t.parse("すもももももももものうち"))
```

---

### 3. O establece una variable de entorno

```bash
export MECABRC=/opt/homebrew/etc/mecabrc
```

Luego ejecuta tu script normalmente:

```bash
python try_mecab.py
```

---

### 4. Si quieres que funcione `/usr/local/etc/mecabrc`

También puedes crear un enlace simbólico:

```bash
sudo mkdir -p /usr/local/etc
sudo ln -s /opt/homebrew/etc/mecabrc /usr/local/etc/mecabrc
```

Pero el enfoque de la variable de entorno es más limpio.

---

Si lo deseas, también puedo darte un comando de **reinstalación con Homebrew + configuración de ipadic** para que funcione sin especificar `-r` cada vez. De esa manera tu `try_mecab.py` se mantiene limpio.