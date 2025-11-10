---
audio: false
generated: true
image: false
lang: zh
layout: post
title: 修复Python版本不匹配问题
translated: true
type: note
---

明白了 — 你遇到了 **Python 版本不匹配** 的问题。

你的日志显示：

* `python3` → **3.10.12**
* `python` → **3.13.7**

所以当 Claude Code（或你的研究代理脚本）调用 `python3` 时，使用的是 3.10 版本，而该版本没有安装 `pyperclip`。你把 `pyperclip` 安装到了 3.13 的环境中，因此 3.10 无法识别它。

以下是几种解决方法：

---

### 1. 使用你指定的 Python 版本运行 Claude Code

如果你希望 Claude Code 始终使用 Python 3.13，请在 shell 中明确设置可执行文件：

```bash
export PYTHON_EXECUTABLE=$(which python)
```

或者如果你特别需要 `python3`：

```bash
export PYTHON_EXECUTABLE=$(which python3)
```

然后启动 Claude Code 或你的代理时，它会读取该环境变量。

---

### 2. 将 `python3` 指向 Python 3.13

在 Ubuntu 上，你可以更新 `alternatives` 系统：

```bash
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.13 2
sudo update-alternatives --config python3
```

然后选择 Python 3.13。

---

### 3. 将 `pyperclip` 安装到 Python 3.10

如果你想继续对 `python3` 使用 3.10 版本，只需在该版本中安装：

```bash
python3 -m pip install --user pyperclip
```

这能确保 `python3` 可以导入它。

---

### 4. 使用虚拟环境

最佳实践：用你想要的 Python 版本创建一个虚拟环境，并在其中运行 Claude Code：

```bash
python3.13 -m venv ~/.venvs/claude
source ~/.venvs/claude/bin/activate
pip install pyperclip
```

然后在这个虚拟环境中启动你的代理，这样它就会始终使用 3.13。

---

👉 请问：你是希望 Claude Code **始终使用 Python 3.13 运行**，还是愿意保持 3.10 作为 `python3` 但只修复缺失的模块？