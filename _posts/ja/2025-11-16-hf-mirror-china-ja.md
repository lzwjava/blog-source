---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: 中国におけるhf-mirror.comの利用
translated: true
type: note
---

### hf-mirror.comの理解
hf-mirror.comは、公式Hugging Face Hub（huggingface.co）のコミュニティ管理ミラーで、中国（広州を含む）のユーザーがネットワーク制限を回避し、AIモデル/データセットをより高速にダウンロードできるように特別に設計されています。完全なリポジトリ構造を複製しているため、元のサイト（しばしば遅いかブロックされている）に直接アクセスせずに、GPT-2のようなモデルやWikiTextのようなデータセットにアクセスできます。あなたがClashプロキシを頻繁に使用することから、hf-mirror.comは国内でホストされており、通常アクセスにプロキシを必要としないことに注意してください—中国での直接使用に最適化されています。すでにClashを介してトラフィックをプロキシしている場合は、hf-mirror.comのトラフィックを直接ルーティング（不必要なホップを避けるため）するか、好みに応じてプロキシ経由のままにすることができます。

### 基本設定：ミラーの使用
鍵は、`HF_ENDPOINT`環境変数をミラーを指すように設定することです。これは`transformers`ライブラリ、`huggingface-cli`、`hfd`（より高速なダウンローダー）などのHugging Faceツールに対してグローバルに機能します。これをライブラリをインポートする前またはダウンロードを実行する**前に**行ってください。

#### 1. 環境変数の設定
- **Linux/macOSの場合（永続的）**: `~/.bashrc`または`~/.zshrc`に追加：
  ```
  echo 'export HF_ENDPOINT=https://hf-mirror.com' >> ~/.bashrc
  source ~/.bashrc
  ```
- **Windowsの場合（PowerShell、永続的）**: 一度実行：
  ```
  [System.Environment]::SetEnvironmentVariable('HF_ENDPOINT', 'https://hf-mirror.com', 'User')
  ```
  その後、ターミナルを再起動します。
- **一時的な設定（任意のOS）**: コマンドの前に付けます：
  ```
  HF_ENDPOINT=https://hf-mirror.com your_command_here
  ```

これにより、コードを変更することなく、すべてのHugging Faceダウンロードがミラーにリダイレクトされます。

#### 2. 必要なツールのインストール
- Hugging Face Hub CLIのインストール（ダウンロード用）：
  ```
  pip install -U huggingface_hub
  ```
- さらに高速なダウンロードには、`hfd`（Hugging Face Downloader、aria2を使用したマルチスレッド高速化）を入手：
  ```
  wget https://hf-mirror.com/hfd/hfd.sh  # またはブラウザでダウンロード
  chmod +x hfd.sh
  ```

#### 3. モデルまたはデータセットのダウンロード
- **huggingface-cliの使用**（中断からの再開をサポート）：
  ```
  # モデルのダウンロード（例：GPT-2）
  huggingface-cli download gpt2 --resume-download --local-dir ./gpt2

  # データセットのダウンロード（例：WikiText）
  huggingface-cli download --repo-type dataset wikitext --resume-download --local-dir ./wikitext
  ```
- **hfdの使用**（より高速、特に大きなファイル向け）：
  ```
  # モデル
  ./hfd.sh gpt2

  # データセット
  ./hfd.sh wikitext --dataset
  ```
- **Pythonコード内での使用**（例：transformersライブラリを使用）：
  ```python
  import os
  os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'  # インポート前に設定

  from transformers import AutoModel, AutoTokenizer
  model = AutoModel.from_pretrained('gpt2')  # 自動的にミラーからダウンロード
  tokenizer = AutoTokenizer.from_pretrained('gpt2')
  ```
  実行：`HF_ENDPOINT=https://hf-mirror.com python your_script.py`

#### 4. ゲート/ログインが必要なモデルの取り扱い
一部のモデル（例：Llama-2）はHugging Faceアカウントとトークンを必要とします：
- huggingface.coでログイン（サイトがブロックされている場合はClashプロキシを使用）。
- https://huggingface.co/settings/tokens でトークンを生成。
- 以下のコマンドでダウンロード：
  ```
  huggingface-cli download --token hf_YourTokenHere meta-llama/Llama-2-7b-hf --resume-download --local-dir ./Llama-2-7b-hf
  ```
  またはhfdの場合：
  ```
  ./hfd.sh meta-llama/Llama-2-7b-hf --hf_username your_username --hf_token hf_YourTokenHere
  ```

### Clashプロキシとの統合
hf-mirror.comは中国のミラーであるため、Clashなしでアクセス可能（直接接続の方が高速）であるべきです。しかし、プロキシ経由にしたい場合（一貫性のためや問題が発生した場合など）、Clashを設定してhf-mirror.comへのトラフィックを希望のプロキシグループ経由でルーティングします。Clashは特別な「HF」設定を必要としません—システム全体に適用されます。

#### クイックClash設定のヒント
- Clashが実行中であり、システムプロキシとして設定されていることを確認（Clashで：「General」 > 「System Proxy」を有効化）。
- **hf-mirror.comを直接ルーティング（速度のために推奨）**: Clashの設定YAML（通常はClashフォルダ内の`config.yaml`）を編集。ミラーへのプロキシをバイパスするルールを追加：
  ```
  rules:
    # ... 既存のルール ...
    - DOMAIN-SUFFIX,hf-mirror.com,DIRECT  # プロキシをバイパス、直接接続
    # ... 残りのルール ...
  ```
  Clashで設定をリロード（Profiles > Reload）。
- **必要に応じてプロキシ経由**: Clash経由でルーティングしたい場合は、特別なルールを追加しない—デフォルト（例：`MATCH,Proxy`）に従います。Clashのオン/オフでブラウザでhf-mirror.comをpingしてテスト。
- ダウンロードの場合：システムプロキシがアクティブなターミナルでコマンドを実行（Clashが処理）。Pythonを使用する場合、`requests`（transformersで使用）のようなライブラリはClashによって設定された`HTTP_PROXY`/`HTTPS_PROXY`環境変数（例：HTTPポート用に`http://127.0.0.1:7890`）を尊重します。
- テスト：`distilbert-base-uncased`のような小さなモデルのダウンロードを試みます。遅い場合は、hf-mirror.comトラフィックに対してClashをオフに切り替えてください。

### トラブルシューティング
- **ダウンロードがまだhuggingface.coをヒットする？** `HF_ENDPOINT`が**すべての**HFライブラリをインポートする**前に**設定されていることを確認（ノートブック/ターミナルを再起動）。
- **速度が遅い？** aria2を使用する`hfd`を使用（マルチ接続をサポート）。またはネットワークを確認—広州のユーザーはしばしばhf-mirror.comで10-50MB/sを達成。
- **データセットでのエラー？** カスタムスクリプトを持つものがある；ベースURLとして`https://hf-mirror.com`を使用するように編集。
- **Windows固有**: Anacondaを使用している場合、ベース環境で環境変数を設定。
- 高度なローカルミラーの自己ホスト（完全な制御が必要な場合）には、Olahやhf-mirror-siteなどのオープンソースツールをGitHubで確認してください。ただし、まずは公開ミラーから始めてください。

この設定で信頼性の高いダウンロードができるはずです。特定のエラーに遭遇した場合は、出力を共有してさらなるヘルプを！

### 参考文献
- [HF-Mirror公式ガイド](https://hf-mirror.com/)
- [Hugging Face Hubドキュメント：エンドポイント](https://huggingface.co/docs/huggingface_hub/en/package_reference/environment_variables#huggingface_hub_constants.HF_ENDPOINT)
- [hfdダウンローダー](https://hf-mirror.com/hfd/hfd.sh)
- [Clash設定ルール](https://github.com/Dreamacro/clash/wiki/Configuration#rules)
- [Stack Overflow: 中国でのダウンロード](https://stackoverflow.com/questions/77388822/how-to-download-huggingface-bert-base-uncased-in-china)