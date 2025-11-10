---
audio: false
generated: true
image: false
lang: ja
layout: post
title: Python 3.11 と pip3.11 のインストール
translated: true
type: note
---

Ubuntuシステムに複数のPythonおよびpipバージョンがインストールされているようですが、**Python 3.11**とそれに対応する**pip (pip3.11)**をインストールする方法をご紹介します：

---

### **1. Python 3.11のインストール**
まず、パッケージリストを更新してPython 3.11をインストールします：

```bash
sudo apt update
sudo apt install python3.11
```

インストールを確認：

```bash
python3.11 --version
```

---

### **2. Python 3.11用pipのインストール**
UbuntuのデフォルトリポジトリにはPython 3.11用の`pip`が含まれていない場合があります。以下の手順でインストールできます：

#### **オプションA: apt経由でpipをインストール（利用可能な場合）**
```bash
sudo apt install python3.11-venv python3.11-dev python3-pip
```
`python3-pip`が別のバージョンのpipをインストールする場合は、**オプションB**に進んでください。

#### **オプションB: ensurepipを使用してpipをインストール**
```bash
python3.11 -m ensurepip --upgrade
```
これにより、Python 3.11専用のpipがインストールされます。

#### **オプションC: get-pip.pyを使用してpipをインストール**
上記の方法が機能しない場合は、公式の`get-pip.py`スクリプトを使用します：

```bash
curl -sS https://bootstrap.pypa.io/get-pip.py | python3.11
```

---

### **3. pip3.11のインストール確認**
`pip3.11`が利用可能か確認します：

```bash
pip3.11 --version
```
以下のような出力が表示されるはずです：
```
pip 23.x.x from /usr/local/lib/python3.11/site-packages/pip (python 3.11)
```

---

### **4. （オプション）仮想環境の作成**
Pythonバージョン間の競合を避けるために、仮想環境を作成できます：

```bash
python3.11 -m venv myenv
source myenv/bin/activate
```
これで、仮想環境内の`pip`はPython 3.11を使用します。

---

### **まとめ表**

| コマンド | 目的 |
|---------|---------|
| `sudo apt update` | パッケージリストの更新 |
| `sudo apt install python3.11` | Python 3.11のインストール |
| `python3.11 -m ensurepip --upgrade` | Python 3.11用pipのインストール |
| `pip3.11 --version` | pipインストールの確認 |
| `python3.11 -m venv myenv` | 仮想環境の作成 |