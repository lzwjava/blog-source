---
audio: false
generated: true
image: false
lang: ja
layout: post
title: GitHub Copilot CLI統合
translated: true
type: note
---

`code --plugin copilot "hi"` のような構文を使用してコマンドラインから直接 GitHub Copilot をプラグインとして呼び出し、応答を得ることはできません。ただし、GitHub Copilot は GitHub CLI を通じて `gh copilot` 拡張機能を提供しており、コマンドの提案や説明のためのチャットのようなインターフェースを提供します。これは `code` コマンド経由で呼び出される一般的なプラグインと全く同じではありませんが、コマンドラインでの対話に関しては同様の目的を果たします。

### GitHub Copilot in the CLI の詳細
- **必要条件**: GitHub Copilot のサブスクリプション、GitHub CLI (`gh`) のインストール、および `gh-copilot` 拡張機能のインストールが必要です。セットアップ手順は GitHub CLI リポジトリまたはドキュメント [GitHub CLI Installation](https://cli.github.com/) および [Installing GitHub Copilot in the CLI](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-in-the-command-line) で利用できます。
- **使用方法**: セットアップが完了すると、以下のようなコマンドを使用できます:
  - `gh copilot suggest -t shell "hi"` を実行してシェルコマンドの提案を得る。
  - `gh copilot explain "hi"` を実行してコマンドの説明を得る。
  - 例: `gh copilot suggest -t shell "say hello"` を実行すると、コンテキストに応じて `echo "hello"` や macOS での `say "hello"` のようなテキスト読み上げコマンドが提案される可能性があります。
- **制限事項**: この CLI インターフェースは、コマンドライン関連のタスク (例: シェル、Git、または GitHub CLI コマンド) 向けに設計されており、チャットボットのような一般的な会話応答はサポートしていません。また、英語のプロンプトのみをサポートしています [Responsible use of GitHub Copilot in the CLI](https://docs.github.com/en/copilot/using-github-copilot/responsible-use-of-github-copilot-in-the-cli)。[](https://docs.github.com/en/copilot/responsible-use/copilot-in-the-cli)[](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-in-the-cli)
- **インタラクティブモード**: `suggest` コマンドを実行した後、Copilot はインタラクティブセッションを開始し、提案を改良したり、実行したり (クリップボードにコピー)、評価したりできます。自動実行するには、`ghcs` エイリアスを設定する必要があります [Using GitHub Copilot in the command line](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-in-the-command-line)。[](https://docs.github.com/en/copilot/how-tos/use-copilot-for-common-tasks/use-copilot-in-the-cli)[](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-in-the-command-line)

### `code --plugin copilot "hi"` が動作しない理由
- **Visual Studio Code CLI**: `code` コマンド (VS Code 用) は拡張機能をインストールするための `--install-extension` のようなオプションをサポートしていますが、`"hi"` のような入力を伴う拡張機能を直接呼び出すための `--plugin` フラグはありません。GitHub Copilot のような拡張機能は通常、VS Code エディター内で動作し、インライン提案やチャットインターフェースを提供します。スタンドアロンの CLI ツールとしては動作しません [GitHub Copilot in VS Code](https://code.visualstudio.com/docs/copilot/overview)。[](https://code.visualstudio.com/docs/copilot/overview)
- **Copilot のアーキテクチャ**: VS Code 用の GitHub Copilot プラグインは、コード補完とチャットのために言語サーバーおよび GitHub のバックエンドと通信します。コマンドラインから `"hi"` のような任意の文字列をプラグインに直接渡して応答を得るための公開 API や CLI メカニズムは存在しません [How to invoke Github Copilot programmatically?](https://stackoverflow.com/questions/76761429/how-to-invoke-github-copilot-programmatically)。[](https://stackoverflow.com/questions/76741410/how-to-invoke-github-copilot-programmatically)
- **一般的な入力に対する代替手段**: `"hi"` のようなプロンプトを Copilot に送信して応答を得たい場合は、VS Code または別のサポートされている IDE 内の Copilot Chat を使用するか、会話型プロンプトをサポートする他の AI CLI ツールを探す必要があります (例: Azure CLI 用の Microsoft の AI Shell) [Use Microsoft Copilot in Azure with AI Shell](https://learn.microsoft.com/en-us/azure/copilot/use-copilot-cli)。[](https://learn.microsoft.com/en-us/azure/copilot/ai-shell-overview)

### 目標達成のための回避策
`"hi"` のようなプロンプトでコマンドラインから Copilot のような AI アシスタントを呼び出して応答を得ることが目標である場合、以下の方法があります:
1. **コマンドラインツールとして `gh copilot` を使用する**:
   - GitHub CLI と Copilot 拡張機能をインストールします。
   - `gh copilot suggest -t shell "greet with hi"` を実行して、`echo "hi"` のようなコマンドを得ます。
   - これはコマンドラインのコンテキストに限定されるため、`"hi"` だけでは、コマンドリクエストとして構成されない限り、意味のある応答が得られない可能性があります。
2. **VS Code の Copilot Chat を使用する**:
   - VS Code を開き、Copilot Chat インターフェース (`⌃⌘I` またはチャットアイコンからアクセス可能) を使用して、`"hi"` と入力して会話応答を得ます。
   - これはエディター内での手動操作が必要であり、CLI 呼び出しではありません [GitHub Copilot in VS Code cheat sheet](https://code.visualstudio.com/docs/copilot/copilot-cheat-sheet)。[](https://code.visualstudio.com/docs/copilot/reference/copilot-vscode-features)
3. **他の AI CLI ツールを探す**:
   - **AI Shell**: Microsoft の AI Shell は、Azure 関連タスク向けに CLI で自然言語プロンプトを可能にします。インストールして `"hi"` のようなプロンプトを試すことができますが、Azure CLI および PowerShell コマンド向けに最適化されています [Use Microsoft Copilot in Azure with AI Shell](https://learn.microsoft.com/en-us/azure/copilot/use-copilot-cli)。[](https://learn.microsoft.com/en-us/azure/copilot/ai-shell-overview)
   - **カスタムスクリプト**: AI モデルの API (例: アクセス可能であれば OpenAI の API) と対話して `"hi"` のようなプロンプトを処理するスクリプトを作成できます。ただし、GitHub Copilot の API はそのような用途で公開されていません [How to invoke Github Copilot programmatically?](https://stackoverflow.com/questions/76761429/how-to-invoke-github-copilot-programmatically)。[](https://stackoverflow.com/questions/76741410/how-to-invoke-github-copilot-programmatically)
4. **プラグインの動作をシミュレートする**:
   - 入力を `gh copilot suggest` または別の AI CLI ツールにパイプするシェルスクリプトまたはエイリアスを作成します。
   - 例:
     ```bash
     alias ai='gh copilot suggest -t shell'
     ai "greet with hi"
     ```
     これは `echo "hi"` または類似のコマンドを提案します。

### プログラムによる呼び出し
(あなたの例が示唆するように) Copilot のような機能をプログラム的に呼び出そうとしている場合、以下の点に注意してください:
- GitHub Copilot は、直接プログラム的にアクセスするための公開 API を公開していません。言語サーバーをリバースエンジニアリングしたり、提案をキャプチャするためにプロキシを使用したりするコミュニティの取り組みもありますが、これらは複雑でリスク (例: アカウント停止の可能性) を伴います [How to invoke Github Copilot programmatically?](https://stackoverflow.com/questions/76761429/how-to-invoke-github-copilot-programmatically)。[](https://stackoverflow.com/questions/76741410/how-to-invoke-github-copilot-programmatically)
- オープンソースの代替手段や、CLI 統合を持つ他の AI モデル (例: Hugging Face の CLI ツールや LLaMA のようなローカル LLM とカスタムラッパー) を探すこともできます。

### 結論
`code --plugin copilot "hi"` はサポートされていませんが、コマンドラインタスクには `gh copilot` を、会話型プロンプトには VS Code の Copilot Chat を使用することで同様の機能を実現できます。一般的な CLI AI 体験には、AI Shell や他の AI API を使用したカスタムスクリプトなどのツールを検討してください。Copilot の CLI 応答にはトレーニングデータからのエラーやバイアスが含まれる可能性があるため、提案は常に確認してください [Responsible use of GitHub Copilot in the CLI](https://docs.github.com/en/copilot/using-github-copilot/responsible-use-of-github-copilot-in-the-cli)。[](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-in-the-cli)

特定のユースケース (例: 会話型 AI とコマンド生成) がある場合は、さらに解決策を調整できますのでお知らせください！