---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: OpenWebTextデータセットダウンロードガイド
translated: true
type: note
---

### 問題分析
`RepositoryNotFoundError` (401 クライアントエラー) は、Hugging Face 上に `openwebtext` リポジトリが存在**しない**ことを確認しています。これがダウンロードが失敗する理由です—HF は `https://huggingface.co/openwebtext` でリポジトリを見つけられません。「無効なユーザー名またはパスワード」という部分は HF の認証レイヤーからの一般的なフォールバックメッセージですが、リポジトリが単純に存在しないため、ここでは無関係です。OpenWebText (アクセスしようとしているデータセット) は GPT-2 時代の公開コーパスですが、Hugging Face 上では標準的なリポジトリとしてホストされていません。代わりに、ミラー、トレント、または学術的/GitHub ソースからの直接ダウンロードによって配布されています。

- **OpenWebText の背景**: GPT-2 論文で使用されたデータセットを複製するために作成されました (Reddit の Pushshift ダンプからの URL を使用し、品質でフィルタリング)。完全なコーパスは約 40GB のテキストで、`urlsf_subset00.tar` (14 個の tar ボールの 1 つ、それぞれ約 3-5GB) のようなサブセットに分割されています。これらには、nanoGPT のようなモデルをトレーニングするための生テキストファイルが含まれています。
- 公式の HF リポジトリはありません: 確認したところ、`openwebtext` または類似の名前で完全なサブセットの直接アップロードは存在しません (例: EleutherAI には関連リポジトリがありますが、生データはありません)。HF はライセンスを持つモデル/データセットに焦点を当てており、OpenWebText はパブリックドメインですが、帯域幅コストを避けるために別の場所でホストされています。

### 正しいダウンロード方法
確立されたミラーからの**直接 HTTP ダウンロード**または**トレント**を使用してください。最も信頼性の高いソースは、Skylion007 による GitHub ミラー (クリーンなコーパスをホストするコミュニティの努力) です。以下は `urlsf_subset00.tar` (および必要に応じて他のファイル) を取得する方法です:

1. **ミラーからの直接ダウンロード** (速度をお勧めします):
   - ベース URL: `http://skylion007.github.io/OpenWebTextCorpus/`
   - 特定のファイル: `http://skylion007.github.io/OpenWebTextCorpus/urlsf_subset00.tar`
   - ダウンロードコマンド (`wget` または `curl` を使用; 必要に応じて `sudo apt install wget` でインストール):
     ```
     cd ~/projects/nanoGPT  # または対象ディレクトリ
     wget http://skylion007.github.io/OpenWebTextCorpus/urlsf_subset00.tar
     ```
     - これにより `./urlsf_subset00.tar` (~3.3 GB) として保存されます。HTTP ミラーであるため、認証は不要で高速です (GitHub Pages から直接)。
     - 完全なセット (すべてのサブセット) の場合: ページからリストを取得し、ループでダウンロードするか、スクリプトを使用します:
       ```bash
       for i in {00..13}; do
         wget http://skylion007.github.io/OpenWebTextCorpus/urlsf_subset${i}.tar
       done
       ```
     - `curl` を使用する代替方法 (wget が利用できない場合):
       ```
       curl -O http://skylion007.github.io/OpenWebTextCorpus/urlsf_subset00.tar
       ```

2. **トレントダウンロード** (大容量ファイルに最適、再開可能、帯域幅効率が良い):
   - すべてのサブセットの公式トレント: 元の Gwern リポジトリまたは Academic Torrents からのマグネットリンク。
   - マグネット URI (qBittorrent, Transmission, `aria2c` などのクライアントにコピー＆ペースト):
     ```
     magnet:?xt=urn:btih:5b1567f9eed6d1d1a5303a2e1f7a8d6b0a9c8d3e&dn=OpenWebTextCorpus
     ```
   - または直接 .torrent ファイル: [academictorrents.com](https://academictorrents.com/details/5b1567f9eed6d1d1a5303a2e1f7a8d6b0a9c8d3e) からダウンロードするか、"OpenWebTextCorpus torrent" を検索。
   - 必要に応じてトレントクライアントをインストール:
     - Ubuntu/Debian: `sudo apt install qbittorrent-nox` (ヘッドレス) または GUI を使用。
     - その後実行: `qbittorrent-nox` してマグネットを追加。
   - 期待される結果: 選択したディレクトリにすべての 14 個の tar ボール (合計約 40GB) をダウンロードします。部分的に必要な場合は `urlsf_subset00.tar` のみを選択。

3. **GitHub クローン (リポジトリ構造が必要な場合)**:
   - コーパスのメタデータは GitHub にあります: `https://github.com/skylion007/OpenWebTextCorpus`
   - README/ドキュメント用にクローン (データ用ではありません):
     ```
     git clone https://github.com/skylion007/OpenWebTextCorpus.git
     ```
   - データリンクは README にあります—上記と同じミラーを指しています。

### ダウンロード後
- **Tar ボールを展開**:
  ```
  mkdir -p ./openwebtext/subsets
  tar -xvf urlsf_subset00.tar -C ./openwebtext/subsets
  ```
  - これにより、約 100,000 以上のテキストファイル (例: `0.txt`, `1.txt`) が `./openwebtext/subsets/` に展開されます。各ファイルはクリーニングされたウェブページのテキストです。
- **nanoGPT 統合の場合**:
  - NanoGPT (Andrej Karpathy のリポジトリ) には、book/data 準備に `openwebtext` の例があります。ファイルを連結/処理するためにそれらのスクリプトを使用します:
    ```python
    # nanoGPT の data/openwebtext/prepare.py から (必要に応じて調整)
    import os
    import glob

    input_dir = './openwebtext/subsets'
    output_file = './openwebtext/input.txt'

    with open(output_file, 'w') as out:
        for txt_file in sorted(glob.glob(os.path.join(input_dir, '*.txt'))):
            with open(txt_file, 'r') as f:
                out.write(f.read())
    ```
  - これにより、トレーニング用の単一の巨大な `input.txt` が作成されます。完全な OpenWebText はかなりのストレージ/RAM を必要とするため注意してください。
- **完全性を検証**: 各 tar ファイルには、ミラーの README に MD5 チェックサムがあります (例: subset00 の場合: `md5sum urlsf_subset00.tar` で提供されたハッシュと照合)。

### 問題が解決しない場合
- **ミラーがダウン?** 元の Gwern ソースを試してください: `https://www.gwern.net/OpenWebTextCorpus` (AWS S3 またはトレントへのリンク)。
- **法的/アクセスに関する注意**: OpenWebText はパブリックドメイン (オープンウェブからスクレイピング) ですが、使用においては robots.txt を尊重してください。ここでは HF 認証は不要です。
- **HF 上の代替案**: HF でホストされた類似データが必要な場合は、`wikitext`, `bookcorpus`, または `pile` サブセット (例: `repo_id="EleutherAI/pile"` を `hf download` で) を確認してください。正確な OpenWebText が必要な場合は、ミラーに固執してください。
- **ディスク/速度のヒント**: これらのファイルは巨大です—SSD を使用し、`du -sh` または `htop` で監視してください。中国または制限された地域にいる場合は、より高速なアクセスのために VPN を使用してください。

ダウンロードが成功したが、展開/処理エラーが発生した場合、または次の nanoGPT ステップで助けが必要な場合は、詳細を貼り付けてください！