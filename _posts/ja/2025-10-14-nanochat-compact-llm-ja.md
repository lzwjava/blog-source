---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: ナノチャットコンパクトフルスタックLLM
translated: true
type: note
---

### NanoChatとは

NanoChatは、ChatGPTに似た大規模言語モデル（LLM）システムのコンパクトでフルスタックな実装です。最小限のコードベースで構築されており、ハッキングが容易で、依存関係が少ない特徴があります。AI分野で著名なAndrej Karpathy（nanoGPTなどで知られる）によって作成され、手頃な価格のハードウェア（単一の8xH100 GPUノードなど）上で、トークン化、事前学習、ファインチューニング、評価、推論、さらにはモデルとチャットするためのシンプルなWeb UIまで、完全なLLMパイプラインを実行するように設計されています。

「100ドルで購入できる最高のChatGPT」として位置づけられており、予算に優しいLLM開発（総額1,000ドル未満）のベースラインを提供します。これは、Eureka LabsによるKarpathyの今後のLLM101nコースの集大成プロジェクトであり、複雑な設定よりもシンプルさを重視しています。

### 主な特徴
- **エンドツーエンドのパイプライン**: 約2,000行のコード（依存関係は小さな`uv.lock`ファイル）ですべてを処理します。約24ドル/時間の8xH100セットアップで約4時間、4e19 FLOPsの能力のあるモデルを学習します。
- **ChatGPTライクなUI**: 学習後、Webサーバーを起動して、本物のChatGPTのようにモデルと対話できます。
- **評価レポート**: ARC-Challenge、GSM8K、HumanEval、MMLUなどのタスクにおけるベンチマークスコアを含む`report.md`を自動生成します。例えば、100ドル規模の実行サンプルでは、各ステージ（BASE、MID、SFT、RL）での段階的な改善が示されています：

| 指標          | BASE   | MID    | SFT    | RL     |
|---------------|--------|--------|--------|--------|
| CORE          | 0.2219 | -      | -      | -      |
| ARC-Challenge | -      | 0.2875 | 0.2807 | -      |
| ARC-Easy      | -      | 0.3561 | 0.3876 | -      |
| GSM8K         | -      | 0.0250 | 0.0455 | 0.0758 |
| HumanEval     | -      | 0.0671 | 0.0854 | -      |
| MMLU          | -      | 0.3111 | 0.3151 | -      |
| ChatCORE      | -      | 0.0730 | 0.0884 | -      |

(総所要時間: フル実行で約3時間51分。)
- **ハードウェアの柔軟性**: Ampere 8xA100（低速）、単一GPU（自動勾配累積対応）、またはバッチサイズを調整した低VRAMセットアップで動作します。バニラPyTorchを使用；他のデバイスへの適応も調整可能です。
- **データソース**: FineWebやSmolTalkなどのHugging Faceデータセットから取得します。
- **その他**: Rustベースのトークナイザーのテストなどが含まれ、リポジトリ全体（約330KB）を他のLLMでクエリするためにパッケージ化するのも容易です。

Karpathyの以前のnanoGPTプロジェクトやmodded-nanoGPTに触発されていますが、完全なチャット体験のためにスケールアップされています。

### 始め方
最速の方法は、8xH100（例: Lambda Labs経由）で100ドル層のモデルをエンドツーエンドで処理する`speedrun.sh`スクリプトを使用することです：

1.  8xH100インスタンスを起動し、リポジトリをクローンします。
2.  以下を実行：
    ```
    bash speedrun.sh
    ```
    （またはログ取得のためscreenセッション内で: `screen -L -Logfile speedrun.log -S speedrun bash speedrun.sh`。Ctrl+A+Dでデタッチし、ログをtailできます。）

3.  完了後（約4時間）、環境をアクティベートし（`source .venv/bin/activate`）、UIをサーブ：
    ```
    python -m scripts.chat_web
    ```
    ローカルURL（例: http://your-ip:8000）を開いてモデルとチャットできます。結果は`report.md`で確認してください。

より大規模なモデル（例: 約12時間の300ドル層、一部スコアでGPT-2を上回る）の場合、`speedrun.sh`を編集してより多くのデータシャードをダウンロードし、深度やバッチサイズを調整します。テストは`python -m pytest tests/test_rustbpe.py -v -s`のように実行します。

MITライセンスの下で公開されており、マイクロモデルをさらに推進するための貢献を受け付けています。詳細な手順については、リポジトリのDiscussionsを確認してください。

[nanoChat GitHubリポジトリ](https://github.com/karpathy/nanochat)