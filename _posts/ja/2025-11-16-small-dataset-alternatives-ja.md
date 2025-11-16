---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: 小型高品質データセットの代替案
translated: true
type: note
---

はい、OpenWebTextは巨大（約90億トークン、17GBのuint16ファイル）で、前処理に長時間かかり、多くのディスク容量を必要とします。以下は、テストやデバッグ、小さなモデルの迅速なトレーニングによく使用される、はるかに小規模で高品質な代替データセットです：

| データセット             | 概算トークン数 | 最終.binサイズ（uint16） | 特徴                                                                              | 迅速な取得方法                                            |
|--------------------------|----------------|--------------------------|-----------------------------------------------------------------------------------|-----------------------------------------------------------|
| **OpenWebText-10k**      | ~4000万        | ~80MB                    | 完全版OpenWebTextと同じ分布、最初の1万ドキュメントのみ                           | `load_dataset("openwebtext", split="train[:10k]")`        |
| **OpenWebText-100k**     | ~4億           | ~800MB                   | 依然として代表性が高く、トークン化は数分で完了                                   | `split="train[:100k]"`                                    |
| **FineWeb-Eduサンプル**  | 5000万〜10億   | 100MB〜2GB               | OWTより高品質（LLamaスタイルのフィルタリング）、最近非常に人気                   | `load_dataset("HuggingFaceFW/fineweb-edu", name="sample-10BQ", split="train")` → 約5000万トークン |
| **Shakespeare**          | ~100万         | ~2MB                     | 古典的な小型データセット、迅速なサニティチェックに最適                           | `load_dataset("tiny_shakespeare")` または単一.txtファイルをダウンロード |
| **PG-19（書籍）**        | 完全版28億     | ~5.5GB                   | 非常にクリーンなパブリックドメイン書籍、一部のみ取得可能                         | `load_dataset("pg19", split="train[:5%]")` → 約1億4000万トークン |
| **C4（サブセット）**     | 可変           | 可変                     | T5チームによってクリーニングされたCommon Crawl、英語のみ                         | `load_dataset("allenai/c4", "en", split="train[:1%]")` streaming=True |
| **RedPajamaサンプル**    | 500万〜2億     | 10MB〜400MB              | 複数ソースの混合（CommonCrawl、Wikipedia、書籍など）、LLaMAと同じレシピ          | `load_dataset("togethercomputer/RedPajama-Data-1T", name="sample", split="train")` |

### 目的別の個人的な推奨データセット

1. 5分未満で実行でき、どこでも動作するものが欲しい → **tiny_shakespeare**  
   （nanoGPTユーザーに人気）

2. 依然として「実際のインターネットテキスト」だが小型のものが欲しい → OpenWebTextの最初の1万ドキュメント  
   ```python
   dataset = load_dataset("openwebtext", split="train[:10000]")
   ```

3. 現在（2025年）最高品質の小型データセットが欲しい → FineWeb-Edu 100億トークンサンプル  
   （約5000万トークン、OWTよりはるかにクリーン、トップラボが使用する品質とほぼ同等）

   ```python
   dataset = load_dataset(
       "HuggingFaceFW/fineweb-edu",
       name="sample-10BQ",  # 100億トークンからサンプリング、分割時は約5000万トークン/シャード
       split="train"
   )
   ```

4. 500MB未満で多様性のあるものが欲しい → RedPajamaサンプル（2億トークンバージョン）  
   ```python
   dataset = load_dataset("togethercomputer/RedPajama-Data-1T", name="sample-200M", split="train")
   ```

これらすべては、前処理スクリプトを全く変更せずに使用できます（load_dataset行を置き換えるだけ）。

迅速な反復処理のため、私は通常3つのバイナリをディスクに保持しています：
- `shakespeare.bin`   (~2MB)   → 過学習テスト用
- `owt_10k.bin`       (~80MB)  → 新規コードのデバッグ用
- `fineweb_edu_1B.bin` (~2GB) → 実際の小型モデルトレーニング用

どのサイズがご希望かお知らせいただければ、正確なワンライナーをお伝えします！