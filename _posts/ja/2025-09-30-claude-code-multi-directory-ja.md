---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-code-fast-1
title: クロードコードマルチディレクトリサポート
translated: true
type: note
---

Claude Codeは、AnthropicのAIを活用したコーディングアシスタントで、セキュリティと集中力を考慮して主に初期化された作業ディレクトリ内で動作しますが、最近のアップデート（バージョン1.0.18以降など）で導入されたマルチディレクトリ機能により、クロスプロジェクト機能を完全にサポートするようになりました。これにより、単一セッションで元のディレクトリ外の複数の無関係なプロジェクトやディレクトリのファイルにアクセスして作業できるようになり、コンテキストの切り替えなしで共有設定の参照、フロントエンド/バックエンドコードの統合、モノレポ設定の処理などのタスクが可能になります。[1][2][3]

### クロスプロジェクト機能の仕組み
- **コアメカニズム**: Claude Codeは1つのルートディレクトリ（「プライマリ」プロジェクト）で起動しますが、追加のディレクトリに対する読み取り、編集、コマンド実行の権限を拡張できます。これは、`--add-dir`フラグまたはセッション中のインタラクティブな`/add-dir`コマンドを使用して行われます。追加されたディレクトリはワークスペースの拡張として扱われ、シームレスなファイル操作が可能になります（例：プロジェクトBで編集中にプロジェクトAのファイルをリントする）。[3][4]
- **セッションスコープ**: 各プロジェクトの追加は、設定を通じて永続化されない限り一時的なものです。Git worktreesを使用すると、より深いコラボレーションのためにプロジェクトの一部で同時セッションを有効にできます。[5][6]
- **制限事項**: Claude Codeはファイルアクセスを追加されたディレクトリのみに制限します。無関係なパスを自動的に検出することはありません。永続的なマルチプロジェクト設定（モノレポなど）の場合は、サブフォルダを含む親ディレクトリから実行してください。[3][7]
- **ユースケース**:
  - **モノレポ**: フロントエンド/バックエンド分割のためのサブディレクトリを追加。[3][5][7][8]
  - **共有リソース**: 別プロジェクトからの設定やライブラリを参照。[3][6]
  - **クロスプロジェクトコラボレーション**: 異なるリポジトリのライブラリやツールからのコードを統合。[1][3]

### Claude Codeに別のプロジェクトを関与させる方法
現在のディレクトリ外のプロジェクト（例：`${another_project_path}`）を追加するには：

1. **Claude Codeを起動**：プライマリプロジェクトディレクトリで起動（例：`cd /path/to/primary/project && claude`）。
2. **インタラクティブに追加ディレクトリを追加**:
   - セッション中に、`/add-dir /full/path/to/another/project`または相対パス（例：`../another-project`）を入力。
   - Claude Codeがアクセスを確認します。プロンプトが表示されたら「yes」と応答してください。[2][3][4]
3. **CLIフラグで起動時**（即時マルチディレクトリ設定用）:
   - 実行：`claude --add-dir /path/to/another/project`（複数追加するにはフラグを繰り返し指定）。[4][5][7]
4. **Claude Bots/Agentsに指示**: 追加後、「追加されたディレクトリ`/path/to/another/project`からAPIファイルを参照して」や「プロジェクトBからこの共有設定を統合して」などの自然言語プロンプトを与えます。Claudeのエージェント設計により、拡張されたコンテキスト内でこれらの要求を理解します。[3][5][6]

### ベストプラクティスとヒント
- **パス指定**: 環境間での明確さのために絶対パスを使用。パフォーマンス低下を防ぐため、あまりにも多くのディレクトリを追加しないでください。[3][7]
- **ワークスペース設定**: チームでは、再利用可能な設定のための設定ファイルを検討。ディレクトリ間でのAPIテストにApidogなどのツールと組み合わせて使用。[3][8]
- **トラブルシューティング**: パス解決に失敗した場合は、書き込み権限を確認。変更のためにセッションを再起動。永続的な問題がある場合は、ログを確認するか、より上位レベルのディレクトリから実行してください。[3][7]
- **チームワークフロー**: マイクロサービスや共有ライブラリに使用。バージョン管理のためにGitで同期。[5][6][8]

この機能は、各ディレクトリで個別のセッションを実行する場合と比較して、複雑な設定のワークフローを変革し、摩擦を軽減します。[3][6] 特定のツールに関する問題が発生したり例が必要な場合は、詳細を提供してください！

引用:
[1] https://www.reddit.com/r/ClaudeAI/comments/1l896ek/claude_code_v1018_we_can_now_specify_additional/
[2] https://www.threads.com/@boris_cherny/post/DMtFLWOzKAS/video-claude-code-can-now-work-across-multiple-directories-in-a-single-sessiontype-add?hl=en
[3] https://apidog.com/blog/claude-code-multi-directory-support/
[4] https://claudelog.com/faqs/--add-dir/
[5] https://www.anthropic.com/engineering/claude-code-best-practices
[6] https://www.linkedin.com/posts/valokafor_how-to-set-up-claude-code-the-right-way-for-activity-7353146981034201089-dhdX
[7] https://stackoverflow.com/questions/79763754/best-practices-for-multi-project-workspaces-in-claude-code
[8] https://www.siddharthbharath.com/claude-code-the-complete-guide/