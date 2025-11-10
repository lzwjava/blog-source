---
audio: false
generated: true
image: false
lang: ja
layout: post
title: カスタムモデルのためのCopilot設定
translated: true
type: note
---

GitHub Copilotで「managed models」を選択しても依然としてGPT-4.1がデフォルトとして表示される場合、またはOpenRouterのGrokやKimiモデルが期待通りに使用できない場合、いくつかの潜在的な理由と対処法があります。以下に問題の分析と、OpenRouter経由でGrokやKimiモデルを使用するようにCopilotを設定する方法を説明します。

### GPT-4.1が引き続き使用される理由
1. **デフォルトモデル設定**: GitHub Copilotは、明示的に変更しない限り、Copilot Chat、Edits、Agent ModeでGPT-4.1をデフォルトとしています。「managed models」を選択しても、OpenRouterの統合が完全に設定されていない場合や特定のモデルが選択されていない場合、デフォルトモデルが維持される可能性があります。
2. **コンテキスト固有のモデル使用**: Copilotの「fix box」（インラインチャットまたはコード補完）は、特定のコンテキストではGrokやKimiのようなカスタムモデルへの切り替えをサポートしていない可能性があります。例えば、Copilot Chatパネルやインラインサジェストは、没入型ビューやAgent Modeで明示的にカスタムモデルに切り替えない限り、デフォルトモデル（GPT-4.1）を使用する可能性があります。
3. **OpenRouter統合の制限**: OpenRouterはGrok（xAI作成）やKimi（Moonshot AI提供）などのモデルへのアクセスを可能にしますが、CopilotとOpenRouterの統合には特定の設定が必要であり、APIの制限や設定の問題ですべてのモデルがすぐに利用可能ではない場合があります。例えば、OpenRouterのAPIがすべてのモデルに対してツールサポートを告知しないため、Agent Modeや特定の機能がGrokやKimiで動作しない可能性があります。
4. **サブスクリプションまたは設定の制限**: 無料ティアまたは非Pro/BusinessのCopilotサブスクリプションを使用している場合、GPT-4.1のようなデフォルトモデルに制限される可能性があります。さらに、一部のモデル（例: GrokやKimi）は、OpenRouterを通じて特定の設定またはプレミアムアクセスが必要な場合があります。

### OpenRouter経由でCopilotでGrokまたはKimiモデルを使用する方法
OpenRouterのGrokやKimiモデルをCopilotで使用するには、特に「fix box」（インラインチャットまたはコード補完）に対して、以下の手順に従ってください。

1. **CopilotでOpenRouterを設定する**:
   - **OpenRouter APIキーを取得**: [openrouter.ai](https://openrouter.ai) でサインアップし、APIキーを取得します。Grok（xAI）およびKimi（Moonshot AI K2）モデルへのアクセスをサポートするクレジットまたはプランがあることを確認してください。
   - **VS CodeでOpenRouterを設定**:
     - Visual Studio Code（VS Code）を開き、最新のGitHub Copilot拡張機能（v1.100.2以降）がインストールされていることを確認します。
     - ステータスバーのCopilotダッシュボードに移動するか、コマンドパレット（`Ctrl+Shift+P` またはMacでは `Command+Shift+P`）を開き、`GitHub Copilot: Manage Models` と入力します。
     - OpenRouter APIキーを追加し、エンドポイントを設定してOpenRouterモデルを含めます。VS CodeのCopilot拡張機能と統合するために、OpenRouterのドキュメントに従う必要がある場合があります。
   - **モデルの可用性を確認**: OpenRouterエンドポイントを追加した後、Copilotの「Manage Models」セクションを確認します。`openrouter/xai/grok` や `openrouter/moonshotai/kimi-k2` などのモデルがモデルピッカーに表示されるはずです。表示されない場合は、OpenRouterアカウントがこれらのモデルにアクセスできること、および制限（例: 無料ティアの制限）がないことを確認してください。

2. **Fix Boxのモデルを切り替える**:
   - **インラインチャット（Fix Box）の場合**: 「fix box」はおそらくCopilotのインラインチャットまたはコード補完機能を指します。インラインチャットのモデルを変更するには:
     - VS CodeでCopilot Chatインターフェースを開きます（タイトルバーまたはサイドバーのアイコンから）。
     - チャットビューで、`CURRENT-MODEL` ドロップダウンメニュー（通常は右下）を選択し、利用可能な場合は `openrouter/xai/grok` または `openrouter/moonshotai/kimi-k2` を選択します。
     - ドロップダウンにGrokやKimiが表示されない場合、OpenRouterのAPIがこれらのモデルに対してツールサポートを告知していないことが原因である可能性があり、Agent Modeやインラインフィックスなどの特定のCopilot機能での使用が制限される場合があります。
   - **コード補完の場合**: コード補完（チャットのみではない）のモデルを変更するには:
     - コマンドパレット（`Ctrl+Shift+P` または `Command+Shift+P`）を開き、`GitHub Copilot: Change Completions Model` と入力します。
     - リストから目的のOpenRouterモデル（例: GrokやKimi）を選択します。VS Codeの現在の制限として、カスタムモデルに対してOllamaエンドポイントのみをサポートしているため、すべてのOpenRouterモデルがコード補完をサポートしていない可能性があることに注意してください（ただし、OpenRouterはプロキシワークアラウンドで動作する可能性があります）。

3. **OpenRouterモデルのワークアラウンド**:
   - **プロキシソリューション**: OpenRouterのAPIが常にツールサポート（Agent Modeや高度な機能に必要）を告知しないため、`litellm` のようなプロキシを使用してCopilotでGrokやKimiを有効にすることができます。`config.yaml` ファイルを編集して以下を含めます:
     ```yaml
     model_list:
       - model_name: grok
         litellm_params:
           model: openrouter/xai/grok
       - model_name: kimi-k2
         litellm_params:
           model: openrouter/moonshotai/kimi-k2
     ```
     - [Bas codes](https://bas.codes) や [DEV Community](https://dev.to) などのソースから、プロキシを設定する詳細な手順についてのセットアップ手順に従ってください。
   - **VS Codeを再起動**: プロキシを設定した後、VS Codeを再起動して新しいモデルがモデルピッカーで利用可能であることを確認します。

4. **サブスクリプションと権限を確認する**:
   - **Copilotサブスクリプション**: 無料ティアユーザーはカスタムモデルを追加するオプションがない可能性があるため、Copilot ProまたはBusinessサブスクリプションがあることを確認してください。
   - **ビジネス制限**: Copilot Businessサブスクリプションを使用している場合、組織がモデル切り替えを有効にする必要があります。管理者に確認するか、GitHubのCopilotポリシー管理に関するドキュメントを参照してください。
   - **OpenRouterクレジット**: GrokやKimiのようなプレミアムモデルは他のモデルよりも多くのクレジットを消費する可能性があるため、OpenRouterアカウントに十分なクレジットがあることを確認してください。

5. **Fix Boxのトラブルシューティング**:
   - fix boxが依然としてGPT-4.1を使用する場合、インラインチャット機能が特定のコンテキスト（例: 非没入型ビュー）でデフォルトモデルにロックされているためである可能性があります。明示的にGrokやKimiを選択するために、Copilot Chatの没入型ビュー（`https://github.com/copilot`）に切り替えてみてください。
   - GrokやKimiがモデルピッカーに表示されない場合は、`Manage Models` でのOpenRouter統合を再確認してください。モデルリストを更新するか、OpenRouter APIキーを再追加する必要がある場合があります。
   - 問題が解決しない場合は、まずCopilotのAgent Modeまたはチャットインターフェースでモデルをテストして動作を確認し、その後インラインフィックスに適用してみてください。

6. **代替ツール**:
   - OpenRouterとCopilotの統合が問題になる場合は、[grok.com](https://grok.com) を介して直接Grokを使用するか、Grok iOS/Androidアプリ（使用量クォータ付きで無料アクセスを提供）を検討してください。Kimiモデルは、OpenRouterのチャットインターフェースを介してテストし、アクセス可能であることを確認することもできます。
   - よりシームレスな体験のために、Cursorなどの他のIDEやツールを探索することもできます。これはOpenRouterのKimi K2モデルでうまく動作することが報告されています。

### 追加の注意点
- **モデルパフォーマンス**: Grokは推論と真実追求に最適化されているため、複雑なデバッグやアーキテクチャタスクに適しています。一方、Kimi（K2）は特定のコーディングシナリオで優れている可能性があります。ユースケースにどちらが適しているかテストしてください。
- **コミュニティフィードバック**: 一部のユーザーは、特に無料ティアアカウントでOpenRouterモデルがCopilotのモデルピッカーに表示されない問題を報告しています。これは有料のOpenRouterプランまたはCopilot Proサブスクリプションが必要な場合があります。
- **継続的な制限**: CopilotでカスタムAPIエンドポイントを直接有効にするためのオープンな議論があります（[microsoft/vscode-copilot-release#7518](https://github.com/microsoft/vscode-copilot-release/issues/7518) 参照）。これが実装されるまで、プロキシワークアラウンドがGrokやKimiを使用する最も信頼性の高い方法です。

### 引用文献
- [Changing the AI model for Copilot Chat - GitHub Docs](https://docs.github.com/en/copilot/managing-copilot/changing-the-ai-model-for-copilot-chat)
- [How to Use Third Party Models in GitHub Copilot Agent Mode - Bas codes](https://bas.codes)
- [Openrouter - openrouter.ai](https://openrouter.ai)
- [Agent Mode With Third-Party Models in Copilot - DEV Community](https://dev.to)
- [r/LocalLLaMA on Reddit: Github Copilot now supports Ollama and OpenRouter Models](https://www.reddit.com)
- [Which AI model should I use with GitHub Copilot? - The GitHub Blog](https://github.blog)
- [OpenAI GPT-4.1 is now generally available in GitHub Copilot - GitHub Changelog](https://github.blog)
- [OpenRouter (free) Models Missing from Manage Models - GitHub Issues](https://github.com/microsoft/vscode-copilot-release/issues/10193)

特定のエラーが発生した場合、またはセットアップに関するさらなる支援が必要な場合は、詳細（例: エラーメッセージ、VS Codeバージョン、サブスクリプションタイプ）を提供してください。それに応じてソリューションをさらに調整できます！