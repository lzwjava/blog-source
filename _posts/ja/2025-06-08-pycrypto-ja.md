---
audio: false
generated: true
lang: ja
layout: post
title: pycryptoのビルドエラー
translated: true
type: note
---

このエラーは、`pycrypto`パッケージがPythonの開発ヘッダーに含まれるヘッダーファイル`longintrepr.h`を必要とするために発生します。このファイルがPython 3.13環境に存在しません。解決方法は以下の通りです：

### 解決策：
1. **Python開発ヘッダーのインストール**  
   お使いのOS用のPython 3.13開発パッケージをインストールします。Ubuntu/Debianの場合：
   ```bash
   sudo apt-get install python3.13-dev
   ```

2. **`pycrypto`の再インストール**  
   ヘッダーをインストールした後、再度インストールを試みます：
   ```bash
   pip install pycrypto
   ```

---

### 代替案の推奨：
**オプション1: `pycrypto`を`pycryptodome`に置き換える（推奨）**  
`pycrypto`は非推奨でメンテナンスされていません。メンテナンスされているフォークである`pycryptodome`に切り替えてください（API互換性あり）：
```bash
pip uninstall pycrypto
pip install pycryptodome
```

**オプション2: レガシーPythonバージョンの使用**  
互換性が許せば、Python ≤3.9を使用します（`pycrypto`が動作することが確認されているバージョン）：
```bash
# pyenvを使用する例
pyenv install 3.9.18
pyenv local 3.9.18
pip install -r requirements.txt
```

---

### 原因：
- `longintrepr.h`は整数表現に使用されるPython内部のヘッダーファイルです。これはPython開発パッケージに含まれますが、標準インストールには含まれません。
- Python 3.13には、`pycrypto`（最終更新2014年）のようなレガシーパッケージを破壊する構造的変更がある可能性があります。
- 非推奨警告は、`pycrypto`が新しい`pip`バージョンでサポートされていない古いビルド方法を使用していることを示しています。

### 予防策：
1. **`pycrypto`を避ける**：暗号化ニーズには`pycryptodome`を使用します。
2. **Pythonバージョンの固定**：レガシープロジェクトでは、Docker/Venvなどの環境でPython ≤3.9を使用します。
3. **依存関係の確認**：互換性のないパッケージを特定するために`pip check`を使用します。

---

あなたがリストしたパッケージ（`aliyunsdkcore`, `aliyun-python-sdk-ecs`, `alibabacloud_vpc20160428`など）は、どれも直接**`pycrypto`**に依存していません。

しかし、`pycrypto`がインストールされている場合、これらパッケージのいずれかの**間接的な依存関係**である可能性があります。どのパッケージが`pycrypto`を要求しているか確認するには、以下を実行します：

```bash
pip show pycrypto
```
または
```bash
pipdeptree | grep -i pycrypto
```

### 考えられる原因：
1. **古いまたは非推奨のセキュリティ関連パッケージ**（あなたのリストには明示的に`pycrypto`を要求するものはありません）。
2. **`paramiko`（SSH）や`google-auth`のようなパッケージからのレガシー依存関係**ですが、これらは通常`pycryptodome`に切り替えられています。

### 推奨アクション：
1. **`pycrypto`を`pycryptodome`に置き換える**（モダンでメンテナンスされているフォーク）：
   ```bash
   pip uninstall pycrypto
   pip install pycryptodome
   ```
   一部のパッケージは`pycryptodome`をドロップイン置換として受け入れます。

2. **隠れたリンクがないことを確認するために依存関係を強制再インストール**：
   ```bash
   pip install --upgrade --force-reinstall -r requirements.txt
   ```

3. **`pycrypto`が残る場合**、環境を監査します：
   ```bash
   pipdeptree --warn silence | grep -i crypto
   ```

### 重要なポイント：
あなたのリストされたパッケージは直接`pycrypto`に依存していませんが、別の隠れた依存関係がある可能性があります。`pipdeptree`でそれを分離すると原因が明確になります。重要なパッケージがそれを要求していない場合は、**`pycrypto`を完全に削除**してください—これは非推奨で、潜在的に安全でない可能性があります。

---

あなたのログに基づくと、**明示的にリストされたパッケージ**のどれも直接`pycrypto`に依存していません。しかし、あなたの依存関係の1つが**間接的な依存関係**としてそれを持っています。特定して解決する方法は以下の通りです：

### 1. 原因パッケージの特定
どのトップレベルパッケージが`pycrypto`を要求しているか見つけるコマンド：
```bash
pipdeptree --warn silence | grep -i pycrypto
```

### 2. あなたのスタックにおける一般的な原因
あなたのパッケージに基づくと、最も可能性の高い候補は以下の通りです：
- **`paramiko`**（`hcloud`, `tigeropen`、またはクラウドSDKで使用）
- **`google-auth`**（Google Cloudパッケージで使用）
- **`boto`**（古いAWSライブラリ）
- **`ansible`**（間接的に使用されている場合）

### 3. 即時解決策：`pycrypto`の置き換え
`pycrypto`は非推奨でPython 3.13で動作しないため、メンテナンスされているフォークに置き換えます：
```bash
pip uninstall pycrypto
pip install pycryptodome
```

### 4. 依存関係が残る場合
依存関係チェックですべてのパッケージを強制再インストール：
```bash
pip install --upgrade --force-reinstall -r requirements.txt
```

### 5. インストールの確認
`pycryptodome`が依存関係を満たしているか確認：
```bash
python -c "from Crypto import Random; print('Success')"
```

### これが起こる理由
- `pycrypto`は古いパッケージ（最終更新2014年）の一般的な暗号依存関係でした
- Python 3.13は`pycrypto`が依存していた`longintrepr.h`のような内部ヘッダーを削除しました
- あなたがインストールしている`cryptography`のようなモダンな代替手段は`pycrypto`を使用しません

最速の解決策は**ステップ3**です — `pycrypto`をAPI互換の`pycryptodome`に置き換えることです。これにより互換性を維持しながらコンパイル問題が解決されます。