---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: Hugging Faceのダウンロード速度改善ソリューション
translated: true
type: note
---

あなたが直面している問題は、中国本土（特に広州のような華南地域）でHugging Faceから大容量ファイルをダウンロードする際に非常に典型的なものです。

### プロキシなしの場合→極端に遅い（〜200–300 KB/s）理由
- **hf-mirror.com**（HFと01.AIが運営する公式中国ミラー）を使用している場合でも、FineWebの実際の大容量parquetファイルは**中国国内にキャッシュされていません**。
- hf-mirror.comは単にグローバルCDN（現在はAWS us-east-1上のxet-bridgeを使用）にリダイレクトするだけです。
- 広州からプロキシなしの場合→トラフィックは国際ゲートウェイ（中国電信/聯通/移動の基幹回線→米国AWS）を経由し、大容量ファイルのダウンロードは大幅にスロットリングまたはQoS制限されます。2GBのファイルは簡単に<500 KB/s、時には100 KB/sまで低下します。

### Clashプロキシ使用時→突然高速化（20–100 MB/s）する理由
- あなたのClashはほぼ確実に香港、台湾、日本、シンガポール、または韓国のノードを使用しています（広州ユーザーには非常に一般的）。
- これらのノードには以下があります：
  - AWS us-east-1（またはHFも使用するCloudflare）への直接ピアリングまたは非常に優れた接続性
  - 送信トラフィックに対するGFWのスロットリングなし
  - はるかに高い帯域幅
- そのため、プロキシを経由して「迂回」しているにもかかわらず、実際のパスは中国本土からの直接国際回線出口よりもはるかに高速です。

### 要約
広州からの直接接続（hf-mirror.com経由でも）→実際のストレージは依然として米国にあるため遅く、中国→米国の大容量ファイル向け帯域幅は2025年現在も非常に劣悪です。  
Clashプロキシ（HK/TW/JPノード）→それらのノードは米国AWSへの優れた接続性を持つため高速です。

### 推奨解決策（高速な順）

1. **低遅延のHK/TW/JPノードを使用したClash（またはv2rayN、Surgeなど）の継続使用** — 現在、中国本土でFineWeb、RedPajama、The Stackなどを扱う最速の方法です。

2. **HFの公式中国加速エンドポイント**の使用（2024-2025年現在、多くのユーザーがプロキシなしで動作）：
   ```bash
   export HF_ENDPOINT=https://hf-mirror.com
   ```
   その後、huggingface-cliまたはdatasetsライブラリを直接使用（wgetではない）。2025年にHFがAliyun/Tencent Cloudにより多くのシャードをキャッシュし始めたため、この方法で50–200 MB/sを報告する中国ユーザーが多い。

3. **FastGit + hugger**または**openi/pkulawミラー**の使用（一部シャードは中国国内にキャッシュ）：
   例：
   ```bash
   pip install hugger
   hugger download HuggingFaceFW/fineweb --revision main --include "CC-MAIN-2013-20/*.parquet"
   ```

4. wget + hf-mirror.comの継続使用だが、Clashプロキシ経由を強制（現在実施済みの方法）。

### 広州から任意のFineWebシャードを高速ダウンロードするクイックワンライナー
```bash
# Clash HTTPプロキシ設定（ポートは通常7890）
export https_proxy=http://127.0.0.1:7890

# その後aria2を使用（wgetよりはるかに高速＋レジューム機能）
aria2c -x16 -s16 -k1M "https://hf-mirror.com/datasets/HuggingFaceFW/fineweb/resolve/main/data/CC-MAIN-2013-20/000_00000.parquet"
```

プロキシノードに応じて、30–100 MB/sを容易に達成できます。

結論：2025年現在の中国本土では、Hugging Faceの1GB超のファイルについては、hf-mirror.comを使用する場合でも、HK/TW/JPプロキシ経由の方が直接接続よりもほぼ常に高速です。これは現在の中国からの国際帯域幅の現実です。