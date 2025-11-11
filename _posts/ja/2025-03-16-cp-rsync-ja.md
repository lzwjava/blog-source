---
audio: false
generated: true
lang: ja
layout: post
title: ディレクトリ構造を維持したファイルのコピー
translated: true
type: note
---

あなたの `find` コマンド出力を基に、すべての `.log` ファイルを `/Users/lzwjava/projects/logs` にディレクトリ構造を維持したままコピーしたいとします。例えば、`./CoreSimulator/FC275C39-59CC-4483-A64E-5D459D7A1D57/system.log` のようなファイルは、`/Users/lzwjava/projects/logs/CoreSimulator/FC275C39-59CC-4483-A64E-5D459D7A1D57/system.log` としてコピーされるべきです。`find` を `cp` または `rsync` と組み合わせて使用し、ディレクトリ階層を維持する方法を紹介します。

---

### **解決策 1: `find` と `cp` の使用**
`find` で `.log` ファイルを見つけ、`cp` の `--parents` オプションを使用してディレクトリ構造を維持しながらコピーできます。

#### **コマンド**
```bash
find . -name "*.log" -exec cp --parents {} /Users/lzwjava/projects/logs \;
```

#### **説明**
- **`find . -name "*.log"`**: カレントディレクトリとサブディレクトリ内のすべての `.log` ファイルを検索します（あなたの例のように）。
- **`-exec cp --parents {} /Users/lzwjava/projects/logs \;`**:
  - `cp --parents`: ファイルと、そのソース（`.`）からの相対的なディレクトリパスを再作成してコピーします。
  - `{}`: `find` によって見つかった各ファイルのプレースホルダーです。
  - `/Users/lzwjava/projects/logs`: コピー先のディレクトリです。
  - `\;`: `-exec` コマンドを終了します。

#### **結果**
- `./CoreSimulator/FC275C39-59CC-4483-A64E-5D459D7A1D57/system.log` → `/Users/lzwjava/projects/logs/CoreSimulator/FC275C39-59CC-4483-A64E-5D459D7A1D57/system.log`
- `CoreSimulator` 以下のディレクトリ構造が維持されます。

#### **実行前の準備**
- `/Users/lzwjava/projects/logs` が存在することを確認してください:
  ```bash
  mkdir -p /Users/lzwjava/projects/logs
  ```

---

### **解決策 2: `rsync` の使用**
`rsync` はディレクトリ構造を維持しながらファイルをコピできる強力なツールで、大量の操作ではより効率的なことが多いです。

#### **コマンド**
```bash
find . -name "*.log" -exec rsync -R -a {} /Users/lzwjava/projects/logs \;
```

#### **説明**
- **`-R`**: 相対パスを使用し、ソース（`.`）からのディレクトリ構造を維持します。
- **`-a`**: アーカイブモード（タイムスタンプ、パーミッションなどを保持します）。
- `{}`: 見つかった各 `.log` ファイルです。
- `/Users/lzwjava/projects/logs`: ターゲットディレクトリです。

#### **結果**
上記と同じです。ファイルは完全な相対パスを維持してコピーされます。

#### **実行前の準備**
- コピー先ディレクトリが存在しない場合は作成してください:
  ```bash
  mkdir -p /Users/lzwjava/projects/logs
  ```

---

### **コピーの確認**
いずれかのコマンドを実行した後、コピー先を確認してください:
```bash
ls -R /Users/lzwjava/projects/logs
```
以下のような表示がされるはずです:
```
/Users/lzwjava/projects/logs:
CoreSimulator

/Users/lzwjava/projects/logs/CoreSimulator:
CoreSimulator.log  FC275C39-59CC-4483-A64E-5D459D7A1D57  Simulator.log

/Users/lzwjava/projects/logs/CoreSimulator/FC275C39-59CC-4483-A64E-5D459D7A1D57:
com.apple.itunesstored  system.log

/Users/lzwjava/projects/logs/CoreSimulator/FC275C39-59CC-4483-A64E-5D459D7A1D57/com.apple.itunesstored:
itunesstored.log
```

---

### **重要な注意点**
- **パーミッション:** `/Users/lzwjava/projects/logs` への書き込み権限があることを確認してください。ない場合は、`sudo` を使用する（例: `sudo cp ...`）か、パーミッションを調整してください:
  ```bash
  chmod -R u+w /Users/lzwjava/projects/logs
  ```
- **上書き:** コピー先に既にファイルが存在する場合:
  - `cp` は警告なしで上書きします。
  - `rsync -a` も上書きしますが、`--ignore-existing` を追加して既存のファイルをスキップできます:
    ```bash
    find . -name "*.log" -exec rsync -R -a --ignore-existing {} /Users/lzwjava/projects/logs \;
    ```
- **ドライラン（事前テスト）:**
  - `cp` の場合、`echo` を追加してプレビューします:
    ```bash
    find . -name "*.log" -exec echo cp --parents {} /Users/lzwjava/projects/logs \;
    ```
  - `rsync` の場合、`--dry-run` を使用します:
    ```bash
    find . -name "*.log" -exec rsync -R -a --dry-run {} /Users/lzwjava/projects/logs \;
    ```

---

### **どちらを選ぶべきか？**
- **`cp`**: よりシンプルで、追加のツールは不要です（すべての Unix 系システムで利用可能です）。
- **`rsync`**: より柔軟性があります（例: 同期、重複のスキップ）が、`rsync` がインストールされている必要があります（ほとんどのシステムで標準です）。

あなたのケースではどちらも動作します。シンプルさから `cp --parents` から始めることをお勧めします。

---

### **最終的なコマンド（推奨）**
```bash
mkdir -p /Users/lzwjava/projects/logs
find . -name "*.log" -exec cp --parents {} /Users/lzwjava/projects/logs \;
```

これをあなたの `Logs` ディレクトリ（`lzwjava@anonymous Logs %`）から実行すれば、準備は完了です！問題が発生したり、動作を調整したい場合（例えば、構造をフラットにしたいなど）はお知らせください。