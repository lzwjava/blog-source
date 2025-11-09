---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: PyYAMLインストールエラーの修正
translated: true
type: note
---

### エラーの理解

この出力は、Linuxシステム上のPython 3.13で`python setup.py install`または`pip install pyyaml`（ソースから）を実行した際のものと思われます。主に2つの問題があります：

1. **C拡張のコンパイル失敗**：
   - ビルドプロセスがC拡張（`yaml._yaml`）のコンパイルを試みていますが、ソースファイル`yaml/_yaml.c`が見つかりません。
   - これは、新しいバージョンのPyYAML（約4.x以降）がビルド中にCythonを使用して`_yaml.c`ファイルを動的に生成するためです。PyPIのソース配布物には事前生成された`.c`ファイルが含まれていないため、これを作成するには事前にCythonをインストールする必要があります。
   - その結果、プロセスは純粋なPython版（動作しますが遅く、libyamlサポートなどの一部機能が欠如）にフォールバックします。

2. **インストール中の権限拒否**：
   - インストールがシステム全体のPythonディレクトリ（`/usr/local/lib/python3.13/dist-packages`）への書き込みを試みており、これにはroot権限が必要です。
   - これは`sudo`や`--user`フラグなしで実行した際によく発生します。

### 解決策

#### コンパイル問題の修正
まずCythonをインストールし、その後PyYAMLのインストールを再試行してください。これにより、不足している`_yaml.c`ファイルが生成され、C拡張のビルドが可能になります。

- **pipを使用する場合（推奨）**：
  ```
  pip install cython
  pip install pyyaml
  ```
  - より高速なC拡張とlibyamlサポートを希望する場合（システムのlibyaml-devが必要。Ubuntu/Debianでは`sudo apt install libyaml-dev`などでインストール）：
    ```
    pip install cython libyaml
    pip install --upgrade --force-reinstall --no-cache-dir pyyaml
    ```

- **setup.pyを直接使用する場合**（非推奨、pipを優先）：
  ```
  pip install cython
  python setup.py build_ext --inplace
  python setup.py install
  ```

注意：Python 3.13は比較的新しいため、互換性のために最新のCython（例：3.0.11以降）を使用していることを確認してください。フリースレッド版Pythonビルドを使用している場合、追加のコンパイル調整が必要な可能性があります—PyYAMLのGitHubイシューで更新情報を確認してください。

#### 権限問題の修正
- **ユーザーディレクトリにインストール**（最も安全、sudo不要）：
  ```
  pip install --user cython pyyaml
  ```
  - これは`~/.local/lib/python3.13/site-packages`にインストールします。

- **システム全体へのインストールにsudoを使用**（パッケージマネージャーと競合する可能性があるため注意して使用）：
  ```
  sudo pip install cython pyyaml
  ```

- **ベストプラクティス：仮想環境を使用**：
  権限問題を完全に回避するには：
  ```
  python -m venv myenv
  source myenv/bin/activate  # Linux/Macの場合
  pip install cython pyyaml
  ```
  これにより、すべてが隔離された状態で保持されます。

インストール後、`python -c "import yaml; print(yaml.__version__)"`でテストしてください。エラーなくインポートされれば成功です。

これらで解決しない場合（例：特定のPython 3.13の特性による）、使用した正確なコマンドやOSバージョンなどの詳細を提供してください。

[Macでのビルド - _yaml.c not found](https://github.com/yaml/pyyaml/issues/122)  
[extension _yaml is not built](https://github.com/yaml/pyyaml/issues/179)  
[MacOSでのlibyamlサポート付きPyyamlのインストール](https://akasurde.github.io/installing-pyyaml-with-libyaml-on-macos.html)