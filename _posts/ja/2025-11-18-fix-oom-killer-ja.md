---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: FineWebスクリプトのOOM Killer修正
translated: true
type: note
---

Pythonのトレースバックなしで「Killed」メッセージが表示されるのは、LinuxのOOM（Out-of-Memory）キラーがプロセスを終了させたことを意味します。これは`data/fineweb/prepare.py`スクリプトで発生しており、~15GBの連結テキストファイル（`train_fineweb.txt`）をトークン化する前に、`open(...).read()`のような処理で一度にすべてRAMに読み込もうとするためです。

FineWeb-Eduはストリーミング処理用に設計されています（公式ダウンローダーはHugging Faceの`datasets`を使用し、~1億トークンのシャードごとに処理してすべてをメモリに読み込むことはありません）が、nanoGPTのfinewebフォルダーには、大きなファイルに対してメモリ効率が良くないカスタムのローカルファイルパスが使用されています。

### クイックフィックス（いずれか一つを選択）

1. **最適で推奨: ローカルファイルの代わりに公式のストリーミングFineWeb-Eduダウンローダーを使用する**  
   nanoGPTの`data/fineweb/prepare.py`をまったく使用しない。  
   FineWeb-Edu 10Bトークン（またはそれ以上）用に正確に作成されたKarpathyの新しいスクリプトを使用する：

   ```bash
   # nanoGPTのルートから（またはどこからでも）
   wget https://raw.githubusercontent.com/karpathy/build-nanogpt/master/fineweb.py
   python fineweb.py
   ```

   これは、`datasets.load_dataset(..., streaming=True)`とマルチプロセッシングを使用して、FineWeb-Edu sample-10BT（100億トークン、~15-20 GB 生データ）をストリーミング方式でダウンロードおよびトークン化します。フルデータセットをRAMに読み込むことはなく、nanoGPTが期待する正確に同じ`.bin`シャードを`edu_fineweb10B/`のようなフォルダーに生成します。  
   これは32-64 GB RAMのマシン（またはスクリプト内の`num_proc_load_dataset`と`num_proc`を減らせばそれ以下でも）で問題なく動作します。

   フル100Bまたは1Tバージョンの場合は、`remote_name = "sample-10BT"`を`"100BT"`など必要なものに変更するだけです。

2. **どうしても10個のローカルparquet → txtファイルを保持したい場合**  
   `data/fineweb/prepare.py`を変更して、テキストをすべて読み込むのではなくチャンクで処理する：

   スクリプトを開き、大きな`with open(local_file, 'r', encoding='utf-8') as f: data = f.read()`ブロックを以下のようなものに置き換える：

   ```python
   from tqdm import tqdm
   import tiktoken
   enc = tiktoken.get_encoding("gpt2")

   chunk_size = 1_000_000  # チャンクあたりの文字数、必要に応じて調整
   tokens = []
   with open(local_file, "r", encoding="utf-8") as f:
       while True:
           chunk = f.read(chunk_size)
           if not chunk:
               break
           tokens.extend(enc.encode_ordinary(chunk))  # または enc.encode(chunk)
           print(f"Tokenized so far: {len(tokens)/1e6:.1f}M tokens")
   tokens = np.array(tokens, dtype=np.uint16)
   ```

   これにより、15GBのファイルでもピークRAMを~10-15GB以下に抑えられます。

3. **ハードウェアの回避策（一時的、理想的ではない）**  
   - 大量のスワップを追加する（例：64-128 GBのスワップファイル）。スワップが始まると非常に遅くなりますが、完了する可能性はあります。  
     ```bash
     sudo fallocate -l 64G /swapfile
     sudo chmod 600 /swapfile
     sudo mkswap /swapfile
     sudo swapon /swapfile
     ```
   - ≥64 GB RAMのマシン/インスタンスで実行する（例：AWS r6i.4xlarge以上）。

### まとめ
build-nanogptの公式`fineweb.py`を実行するだけです — これが最もクリーンな解決策であり、現在FineWebを使用する全員が使用している方法です。問題はFineWeb自体ではなく、あなたが連結した15GBのtxtファイルです。

[公式FineWeb-Eduダウンローダースクリプト](https://raw.githubusercontent.com/karpathy/build-nanogpt/master/fineweb.py)  
[FineWeb-Eduデータセットページ](https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu)