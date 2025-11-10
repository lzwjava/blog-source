---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 修復MeCab設定檔案路徑
translated: true
type: note
---

你的錯誤

```
RuntimeError: param.cpp(70) [ifs] no such file or directory: /usr/local/etc/mecabrc
```

意思是 **MeCab 找不到其設定檔** (`mecabrc`)。
在 macOS 上，如果你最近透過 Homebrew 安裝 MeCab，它很可能安裝在 `/opt/homebrew/` 而不是 `/usr/local/`，但 Python 綁定仍在尋找舊的 `/usr/local/etc/mecabrc` 路徑。

以下是修復方法：

---

### 1. 找出 `mecabrc` 的實際位置

執行：

```bash
brew list mecab
```

或：

```bash
find /opt/homebrew -name mecabrc
```

你可能會看到類似：

```
/opt/homebrew/etc/mecabrc
```

---

### 2. 將 MeCab 指向正確的 mecabrc

你可以在 Python 程式碼中指定路徑：

```python
import MeCab

t = MeCab.Tagger(f"-r /opt/homebrew/etc/mecabrc -d /opt/homebrew/lib/mecab/dic/ipadic")
print(t.parse("すもももももももものうち"))
```

---

### 3. 或設定環境變數

```bash
export MECABRC=/opt/homebrew/etc/mecabrc
```

然後正常執行你的腳本：

```bash
python try_mecab.py
```

---

### 4. 如果你想讓 `/usr/local/etc/mecabrc` 生效

你也可以建立符號連結：

```bash
sudo mkdir -p /usr/local/etc
sudo ln -s /opt/homebrew/etc/mecabrc /usr/local/etc/mecabrc
```

但環境變數的方法更為整潔。

---

如果你需要，我也可以提供 **Homebrew 重新安裝 + ipadic 設定** 指令，這樣你就不需要每次都指定 `-r` 參數。這樣你的 `try_mecab.py` 就能保持簡潔。