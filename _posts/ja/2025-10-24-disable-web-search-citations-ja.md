---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: LibreChatウェブ検索引用の無効化
translated: true
type: note
---

## LibreChat Web Searchモードでの引用表示の無効化

LibreChatのWeb検索機能（Serper.devやSearxNGなどのプロバイダーを基にし、Firecrawlなどのスクレイパーと連携）は、ソースの出典明示と透明性向上のために、応答に自動的に引用を含めます。公式ドキュメントとコミュニティの議論に基づくと、個々のユーザーレベルでWeb検索の引用を無効にするための組み込みのユーザー向けトグルは特に存在しません。ただし、管理者またはセルフホスター向けに、設定変更を通じてこれを実現または近似することができます。以下に方法を示します：

### 1. **管理者レベルの設定（推奨アプローチ）**
   自身のLibreChatインスタンスを運用している場合（セルフホスト）、設定ファイルを変更して引用のレンダリングを制限または削除します。引用はインターフェースと検索コンポーネントを介して処理されます。

   - **インターフェース設定のため`librechat.yaml`を編集**:
     LibreChatはグローバル設定にYAMLファイルを使用します。引用表示を制御する`interface`セクションを探してください（ファイル検索用の制御に触発されており、Web検索のUIレンダリングに影響する場合があります）。
     - `fileCitations`を`false`に設定して、グローバルに引用表示権限を無効にします。これは明示的にファイル検索用ですが、一部の設定ではWeb検索のUIレンダリングに影響を与える可能性があります。
       ```yaml
       interface:
         fileCitations: false  # 検索全体での引用表示を無効化
       ```
     - Web検索に特化しては、`webSearch`セクションの下で、プロバイダーを無効化またはカスタマイズして、詳細なソースリンクを回避できます：
       ```yaml
       webSearch:
         enabled: true  # 有効に保つが、プロバイダーを調整
         serper:  # または使用中のプロバイダー
           enabled: true
           # 直接的な'citations'フラグはないが、FirecrawlのようなスクレイパーのAPIキーを省略すると詳細な抽出/引用が減少
         firecrawl:
           enabled: false  # コンテンツスクレイピングを無効化（引用を生成することが多い）
       ```
     - 変更後はLibreChatインスタンスを再起動してください。インターフェース設定のソース：[LibreChat Interface Object Structure](https://www.librechat.ai/docs/configuration/librechat_yaml/object_structure/interface)[1]。

   - **環境変数（.env ファイル）**:
     `.env`ファイルで、引用を強制する可能性のあるデバッグやロギングモードを無効にするか、Web検索を最小限のプロバイダーに設定します。
     - 例：
       ```
       DEBUG_PLUGINS=false  # 詳細な出力（引用を含む）を削減
       SERPER_API_KEY=your_key  # スクレイピングなしの基本的な検索プロバイダーを使用して引用を減少
       FIRECRAWL_API_KEY=  # 空白のままにしてスクレイパーを無効化（ページ抽出/引用なし）
       ```
     - これにより、応答はインライン引用なしの要約のみの検索結果に移行します。完全なセットアップ：[LibreChat .env Configuration](https://www.librechat.ai/docs/configuration/dotenv)[2]。

   - **Web検索プロバイダーのカスタマイズ**:
     SearxNGのようなプロバイダーに切り替えます。これはサーバー側でソースリンクを省略するように設定できます。
     - `.env`で`SEARXNG_INSTANCE_URL=your_minimal_searxng_url`を設定します。
     - SearxNGインスタンスで、結果のメタデータを抑制するように設定を編集します（例：SearxNGの`settings.yml`で`reveal_version: false`を無効にし、リンクを削除するようにテンプレートをカスタマイズ）。
     - ドキュメント：[Web Search Configuration](https://www.librechat.ai/docs/configuration/librechat_yaml/object_structure/web_search)[3]。

### 2. **ユーザーレベルの回避策（管理者アクセスなし）**
   ホストされたLibreChat（例：公開インスタンス）を使用している場合、正確性のために引用が強制されることが多いため、オプションは限られています：
   - **プロンプトエンジニアリング**: メッセージでAIに明示的に指示します。例：「Webを検索してください。ただし、応答に引用やソースを含めないでください。」検索ツールがそれらを追加する可能性がありますが、多くのモデルは部分的に従います。
   - **Web検索を完全に無効化**: 引用が主な問題である場合、会話ごとにWeb検索をオフにします：
     - チャットインターフェースで、「Web Search」ボタンをクリックしないようにします。
     - エージェントの場合：エージェントの作成/編集時、エージェントの設定（Agents UI経由）で`web_search`機能を削除します。ソース：[Agents Documentation](https://www.librechat.ai/docs/features/agents)[4]。
     - 管理者にトグルの追加をリクエストします。コミュニティの議論では、これは機能リクエストとして提案されています（例：[GitHub Discussion on Web Search Toggle](https://github.com/danny-avila/LibreChat/discussions/7738)[5]）。

### 3. **制限事項と注意点**
   - 引用は、倫理的AI使用と追跡可能性を確保するためのWeb検索の核心部分であるため、完全に無効化するにはカスタムコードの変更（例：GitHubリポジトリの`WebSearchResults.jsx`のようなフロントエンドコンポーネントを編集して引用要素を非表示にする）が必要な場合があります。
   - 現在のバージョン（2025年10月現在）では、直接的な「引用をオフ」フラグは存在しません。機能は進化するため、[Web Search Feature Docs](https://www.librechat.ai/docs/features/web_search)[6]で更新を確認してください。
   - セルフホストしている場合、開発環境で変更をテストしてください—スクレイパーを無効にすると応答品質が低下する可能性があります。
   - コミュニティのフィードバック（例：Reddit）では、検索機能に関する時折のバグが指摘されていますが、引用に特化したものはありません：[Reddit Thread on LibreChat Issues](https://www.reddit.com/r/LocalLLaMA/comments/1k2hraj/is_it_just_me_or_is_librechat_a_complete_buggy/)[7]。

公式サポートについては、LibreChat Discordに参加するか、GitHubイシューをセットアップの詳細とともに開いてください。これで解決しない場合は、使用しているLibreChatのバージョンやホスティング方法についてより多くのコンテキストを提供してください！

引用：
[1] https://www.librechat.ai/docs/configuration/librechat_yaml/object_structure/interface
[2] https://www.librechat.ai/docs/configuration/dotenv
[3] https://www.librechat.ai/docs/configuration/librechat_yaml/object_structure/web_search
[4] https://www.librechat.ai/docs/features/agents
[5] https://github.com/danny-avila/LibreChat/discussions/7738
[6] https://www.librechat.ai/docs/features/web_search
[7] https://www.reddit.com/r/LocalLLaMA/comments/1k2hraj/is_it_just_me_or_is_librechat_a_complete_buggy/