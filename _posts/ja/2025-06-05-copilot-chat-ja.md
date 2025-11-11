---
audio: false
generated: true
lang: ja
layout: post
title: 'Copilot Chat: IDEAとVSCodeのコンテキスト'
translated: true
type: note
---

GitHub Copilot Chatは、JetBrains IDEAとVisual Studio Code（VS Code）の両方に統合されたAI搭載アシスタントで、自然言語での対話、コード提案、コンテキストを考慮した支援を通じて開発者のコーディングタスクを支援するように設計されています。Copilot Chatのコア機能は両方のIDEで同様ですが、JetBrains IDEAとVS Codeの異なるアーキテクチャとエコシステムにより、実装方法、コンテキストの扱い、利用可能な機能に違いがあります。以下では、最近使用したファイルのコンテキストとしての扱い方やその他の主な違いに焦点を当て、包括的な説明を行います。

---

### **1. コンテキスト認識と最近使用したファイルの扱い**
Copilot ChatのJetBrains IDEAとVS Code間の主な違いの1つは、コンテキスト、特に最近使用したファイルの取り込み方にあります。

#### **JetBrains IDEA: 最近使用したファイルを含むコンテキスト**
- **動作**: JetBrains IDEAでは、Copilot ChatはIDEの強力なプロジェクトインデックス作成とコンテキスト認識機能を活用する傾向があります。JetBrains IDEは、ファイル間の関係、依存関係、最近開いたファイルを含むプロジェクト構造への深い理解で知られています。IDEAのCopilot Chatはこれを使用し、ユーザーが明示的に参照していなくても、最近使用したファイルを応答生成のコンテキストの一部として含めます。
- **メカニズム**: JetBrains IDEAでCopilot Chatと対話する際、コンテキストは以下から取得されます：
  - エディタで現在開いているファイル。
  - プロジェクト内で最近開いた、またはアクティブなファイル（IDEの内部インデックスの一部）。
  - プロジェクトのコードベース構造（特に、2025年初頭に導入された`@project`コンテキストなどの機能を使用する場合。これによりCopilotは関連するファイルやシンボルに対してコードベース全体を分析できます）。[](https://github.blog/changelog/2025-02-19-boost-your-productivity-with-github-copilot-in-jetbrains-ides-introducing-project-context-ai-generated-commit-messages-and-other-updates/)
- **利点**:
  - **プロジェクトコンテキストとのシームレスな統合**: JetBrainsのインデックス作成により、Copilotが最近編集したファイル内のクラス、メソッド、依存関係などを参照するなど、プロジェクトの構造に沿った提案を提供しやすくなります。
  - **暗黙的なコンテキストとしての最近使用したファイル**: 最近ファイルを操作した場合、Copilotは手動での指定を必要とせずにそれをコンテキストに含めることがあり、コーディングセッションの継続性を維持するのに役立ちます。
- **制限事項**:
  - 最近使用したファイルへの依存は、IDEが無関係なファイルを含めてしまった場合、精度の低いコンテキストにつながることがあります。例えば、多くのファイルを最近開いた場合、Copilotは古いまたは無関係なコンテキストを取り込む可能性があります。
  - 最近（例：2025年2月の`@project`機能）まで、JetBrainsはVS Codeとは異なり、コードベース全体を明示的に含める方法が欠如していました。[](https://www.reddit.com/r/Jetbrains/comments/1fyf6oj/github_copilot_on_jetbrains_dont_have_option_to/)

#### **VS Code: 明示的で柔軟なオプションによるコンテキスト管理**
- **動作**: VS Codeでは、Copilot Chatは`#codebase`、`#file`などのチャット変数などの機能により、より明示的でカスタマイズ可能なコンテキスト管理を備えており、ユーザーがコンテキストの範囲を定義できます。最近開いたファイルを使用することはできますが、JetBrains IDEAほど自動的かつ強力にそれらを優先することはありません（明示的に指示しない限り）。
- **メカニズム**: VS CodeのCopilot Chatは、以下のものからコンテキストを収集します：
  - エディタ内のアクティブなファイル。
  - チャットプロンプト内で`#file`や`#codebase`を使用して明示的に参照されたファイル。例えば、`#codebase`はワークスペース全体を検索し、`#file:<filename>`は特定のファイルを対象とします。[](https://code.visualstudio.com/docs/copilot/chat/copilot-chat)[](https://code.visualstudio.com/docs/copilot/chat/copilot-chat-context)
  - ワークスペースのインデックス作成。特に`github.copilot.chat.codesearch.enabled`設定が有効な場合、コードベースのローカルまたはリモート（GitHubホスト）のインデックスを含むことができます。[](https://code.visualstudio.com/docs/copilot/reference/workspace-context)
  - `#fetch`や`#githubRepo`などを通じた、ターミナル出力、テスト結果、またはWebコンテンツなどの追加のコンテキストソース。[](https://code.visualstudio.com/docs/copilot/chat/copilot-chat-context)
- **利点**:
  - **きめ細かい制御**: ユーザーは、どのファイルまたはコードベースのどの部分を含めるかを正確に指定できるため、無関係なファイルからのノイズを減らせます。
  - **コードベース全体の検索**: `@workspace`および`#codebase`機能により、Copilotはワークスペース内のすべてのインデックス可能なファイルにわたって検索を行うことができ、大規模プロジェクトで特に強力です。[](https://code.visualstudio.com/docs/copilot/reference/workspace-context)
  - **動的なコンテキスト追加**: 画像のドラッグ＆ドロップ、ターミナル出力、またはWeb参照などの機能により、多様なタイプのコンテキストを柔軟に追加できます。[](https://code.visualstudio.com/docs/copilot/chat/copilot-chat)
- **制限事項**:
  - VS Codeは、JetBrains IDEAほど最近開いたファイルを自動的に優先しないため、ユーザーはより頻繁に手動でコンテキストを指定する必要があるかもしれません。
  - 非常に大規模なコードベースの場合、インデックス作成の制約（例：ローカルインデックスは2500ファイルに制限）により、コンテキストは最も関連性の高いファイルに限定される可能性があります。[](https://code.visualstudio.com/docs/copilot/reference/workspace-context)

#### **最近使用したファイルのコンテキストにおける主な違い**
- **JetBrains IDEA**: IDEのプロジェクトインデックス作成により、最近開いたファイルを自動的にコンテキストの一部として含めます。これにより、単一のプロジェクト内で作業するユーザーにとって、より「暗黙的」でシームレスに感じられます。ただし、ユーザーが多くのファイルを最近開いた場合、無関係なファイルが含まれることがあります。
- **VS Code**: より明示的なコンテキスト指定（例：`#file`や`#codebase`）を必要としますが、より優れた制御性と柔軟性を提供します。最近使用したファイルは、エディタで開いているか、明示的に参照されない限り、自動的には優先されません。

---

### **2. 機能の可用性と統合**
両方のIDEがCopilot Chatをサポートしていますが、統合の深さと機能の展開スピードは、GitHub（VS Codeも維持するMicrosoftの子会社）の開発優先順位と、JetBrainsおよびVS Codeの異なるエコシステムにより異なります。

#### **JetBrains IDEA: IDEとの緊密な統合だが機能展開は遅め**
- **統合**: Copilot ChatはGitHub Copilotプラグインを通じてJetBrains IDEAに深く統合されており、IntelliSense、プロジェクトインデックス作成、リファクタリングツールなどのIDEの強力な機能を活用します。2024年9月に導入されたInline Chatにより、ユーザーはコードエディタ内で直接Copilotと対話できます（Mac: Shift+Ctrl+I, Windows: Shift+Ctrl+G）。[](https://github.blog/changelog/2024-09-11-inline-chat-is-now-available-in-github-copilot-in-jetbrains/)
- **機能**:
  - **Inline Chat**: アクティブなファイル内でのリファクタリング、テスト、コード改善のための集中した対話をサポートします。[](https://github.blog/changelog/2024-09-11-inline-chat-is-now-available-in-github-copilot-in-jetbrains/)
  - **@project コンテキスト**: 2025年2月現在、JetBrainsのCopilotは`@project`を使用したコードベース全体のクエリをサポートし、関連するファイルやシンボルへの参照を含む詳細な回答を提供します。[](https://github.blog/changelog/2025-02-19-boost-your-productivity-with-github-copilot-in-jetbrains-ides-introducing-project-context-ai-generated-commit-messages-and-other-updates/)
  - **コミットメッセージ生成**: Copilotはコード変更に基づいてコミットメッセージを生成でき、ワークフローの効率を向上させます。[](https://github.blog/changelog/2025-02-19-boost-your-productivity-with-github-copilot-in-jetbrains-ides-introducing-project-context-ai-generated-commit-messages-and-other-updates/)
- **制限事項**:
  - 機能はしばしばVS Codeより遅れます。例えば、マルチモデルサポート（例：Claude、Gemini）やエージェントモードでのマルチファイル編集は、JetBrainsより先にVS Codeで導入されました。[](https://www.reddit.com/r/Jetbrains/comments/1gfjbta/is_jetbrains_bringing_the_new_copilotvs_code/)
  - プロンプトへの画像添付や、自律的なマルチファイル編集のためのエージェントモードなどの高度な機能の一部は、最新のアップデート時点ではJetBrainsではまだ完全にはサポートされていません。[](https://code.visualstudio.com/docs/copilot/chat/getting-started-chat)[](https://code.visualstudio.com/blogs/2025/02/24/introducing-copilot-agent-mode)
- **パフォーマンス**: JetBrainsの重いIDE環境により、特に大規模プロジェクトでは、そのインデックス作成および分析エンジンのオーバーヘッドが原因で、Copilotの応答がVS Codeよりわずかに遅くなる可能性があります。

#### **VS Code: より速い機能展開と広範な機能性**
- **統合**: Microsoft製品として、VS CodeはGitHub Copilotとの緊密な統合とより速い機能展開の恩恵を受けています。Copilot Chatは、チャットビュー、インラインチャット（Mac: ⌘I, Windows: Ctrl+I）、またはコンテキストメニュー経由のスマートアクションを通じて、エディタにシームレスに組み込まれています。[](https://code.visualstudio.com/docs/copilot/chat/getting-started-chat)
- **機能**:
  - **複数のチャットモード**: 質問モード（一般的な質問）、編集モード（ユーザー制御によるマルチファイル編集）、エージェントモード（ターミナルコマンドを使用した自律的なマルチファイル編集）をサポートします。[](https://code.visualstudio.com/docs/copilot/chat/copilot-chat)[](https://code.visualstudio.com/blogs/2025/02/24/introducing-copilot-agent-mode)
  - **カスタム指示とプロンプトファイル**: ユーザーは`.github/copilot-instructions.md`または`.prompt.md`ファイルでコーディングプラクティスを定義し、VS CodeとVisual Studioの両方で応答をカスタマイズできます。[](https://code.visualstudio.com/docs/copilot/copilot-customization)
  - **画像添付**: Visual Studio 17.14 Preview 1以降、ユーザーは追加のコンテキストのためにプロンプトに画像を添付できます。この機能はJetBrainsではまだ利用できません。[](https://learn.microsoft.com/en-us/visualstudio/ide/visual-studio-github-copilot-chat?view=vs-2022)
  - **マルチモデルサポート**: VS Codeは複数の言語モデル（例：GPT-4o、Claude、Gemini）をサポートし、ユーザーがタスクに応じてモデルを切り替えることができます。[](https://www.reddit.com/r/Jetbrains/comments/1gfjbta/is_jetbrains_bringing_the_new_copilotvs_code/)
  - **ワークスペースインデックス作成**: `@workspace`機能と`#codebase`検索は、GitHubホストのリポジトリに対してリモートインデックス作成によって強化された、包括的なコードベースコンテキストを提供します。[](https://code.visualstudio.com/docs/copilot/reference/workspace-context)
- **利点**:
  - **迅速な機能アップデート**: VS Codeは多くの場合、エージェントモードやマルチモデルサポートなどのCopilot機能を最初に受け取ります。[](https://www.reddit.com/r/Jetbrains/comments/1gfjbta/is_jetbrains_bringing_the_new_copilotvs_code/)
  - **軽量で柔軟**: VS Codeの軽量な性質により、ほとんどの場合Copilotの応答が高速になり、その拡張機能エコシステムにより、追加のAIツールやカスタマイズが可能です。
- **制限事項**:
  - JetBrainsと比較してプロジェクトインデックス作成の堅牢性が低く、より手動でのコンテキスト指定が必要になる場合があります。
  - 拡張機能ベースのアーキテクチャは、一部のユーザーにとってJetBrainsのオールインワンIDE体験よりも一体感に欠けると感じられることがあります。[](https://www.reddit.com/r/Jetbrains/comments/1fyf6oj/github_copilot_on_jetbrains_dont_have_option_to/)

---

### **3. ユーザーエクスペリエンスとワークフロー**
各IDEにおけるCopilot Chatのユーザーエクスペリエンスは、それぞれのプラットフォームの設計思想を反映しています。

#### **JetBrains IDEA: 大型IDEユーザー向けに合理化**
- **ワークフロー**: Copilot Chatは、大規模で複雑なプロジェクトに取り組む開発者向けに調整された、JetBrainsの包括的なIDE環境に統合されています。インラインチャットとサイドパネルチャットは、それぞれ集中型および広範な対話モードを提供します。[](https://github.blog/changelog/2024-09-11-inline-chat-is-now-available-in-github-copilot-in-jetbrains/)
- **コンテキスト認識**: IDEのプロジェクト構造と最近使用したファイルへの深い理解により、Copilotは広範な手動コンテキスト指定を必要とせずに、プロジェクトをより「認識」しているように感じさせます。
- **使用例**: JetBrainsの高度なリファクタリング、デバッグ、テストツールに依存し、統一されたIDE体験を好む開発者に理想的です。Copilotは、同じワークフロー内でコンテキストを考慮した提案を提供することでこれを強化します。
- **学習曲線**: JetBrainsの機能豊富な環境は新規ユーザーには圧倒される可能性がありますが、プラグインがセットアップされればCopilotの統合は比較的直感的です。

#### **VS Code: 多様なワークフローに対応する柔軟性**
- **ワークフロー**: VS CodeのCopilot Chatは柔軟性を重視して設計されており、軽量なスクリプティングから大規模プロジェクトまで、幅広い開発者に対応します。チャットビュー、インラインチャット、スマートアクションは、対話のための複数のエントリーポイントを提供します。[](https://code.visualstudio.com/docs/copilot/chat/getting-started-chat)
- **コンテキスト認識**: 強力ですが、VS Codeのコンテキスト管理は、JetBrainsと同じレベルのプロジェクト認識を実現するためにより多くのユーザー入力を必要とします。ただし、`#codebase`やカスタム指示などの機能により、非常にカスタマイズ可能です。[](https://code.visualstudio.com/docs/copilot/chat/copilot-chat)
- **使用例**: 軽量でカスタマイズ可能なエディタを好み、多様なプロジェクトや言語にわたって作業する必要がある開発者に適しています。Webコンテンツ、画像、複数のモデルを統合する能力は、その汎用性を高めます。
- **学習曲線**: VS CodeのシンプルなインターフェースはCopilot Chatを初心にとってよりアクセスしやすくしますが、コンテキスト管理（例：`#`メンション）を習得するにはある程度の慣れが必要です。

---

### **4. 最新ファイルのコンテキストにおける具体的な違い**
- **JetBrains IDEA**:
  - IDEのプロジェクトインデックス作成を活用し、最近開いたファイルを自動的にコンテキストに含めます。これは、プロジェクト内で関連するファイルを頻繁に切り替える開発者に特に有用です。
  - `@project`機能（2025年2月導入）によりコードベース全体のクエリが可能ですが、JetBrainsのインデックス作成により、最近使用したファイルは依然として暗黙的に優先されます。[](https://github.blog/changelog/2025-02-19-boost-your-productivity-with-github-copilot-in-jetbrains-ides-introducing-project-context-ai-generated-commit-messages-and-other-updates/)
  - 例: 最近`utils.py`ファイルを編集し、Copilotに関数を生成するように依頼した場合、それを指定しなくても自動的に`utils.py`からのコードを考慮する可能性があります。
- **VS Code**:
  - 最近使用したファイルを自動的に優先するのではなく、明示的なコンテキスト指定（例：`#file:utils.py`や`#codebase`）に依存します。ただし、エディタで開いているファイルはデフォルトでコンテキストに含まれます。[](https://github.com/orgs/community/discussions/51323)
  - 例: `utils.py`をコンテキストに含めるには、明示的に参照するか、エディタで開いているか、または`#codebase`を使用してワークスペース全体を検索する必要があります。
- **実用的な影響**:
  - **JetBrains**: 最近使用したファイルが関連する可能性が高いワークフローに優れており、手動でのコンテキスト指定の必要性を減らします。
  - **VS Code**: 特に最近使用したファイルが常に関連するとは限らない大規模プロジェクトでは、コンテキストに対する正確な制御を好むワークフローに優れています。

---

### **5. その他の注目すべき違い**
- **マルチモデルサポート**:
  - **VS Code**: 複数の言語モデル（例：GPT-4o、Claude、Gemini）をサポートし、ユーザーが要件に基づいて切り替えることができます。[](https://www.reddit.com/r/Jetbrains/comments/1gfjbta/is_jetbrains_bringing_the_new_copilotvs_code/)
  - **JetBrains IDEA**: マルチモデルサポートでは遅れており、Copilotは主にGitHubのデフォルトモデルを使用します。JetBrains自身のAI Assistantが代替モデルを提供する可能性がありますが、Copilotとの統合は限られています。[](https://www.reddit.com/r/Jetbrains/comments/1gfjbta/is_jetbrains_bringing_the_new_copilotvs_code/)
- **エージェントモード**:
  - **VS Code**: エージェントモードをサポートし、自律的に複数のファイルを編集し、タスクを完了するためにターミナルコマンドを実行します。[](https://code.visualstudio.com/blogs/2025/02/24/introducing-copilot-agent-mode)
  - **JetBrains IDEA**: エージェントモードはまだ利用できず、Copilotはユーザーが制御する編集または単一ファイルの対話に限定されます。[](https://docs.github.com/en/copilot/about-github-copilot/github-copilot-features)
- **カスタム指示**:
  - **VS Code**: `.github/copilot-instructions.md`およびプロンプトファイルによるカスタム指示をサポートし、ユーザーがコーディングプラクティスとプロジェクト要件を定義できます。[](https://code.visualstudio.com/docs/copilot/copilot-customization)
  - **JetBrains IDEA**: 同様のカスタム指示をサポートしますが、外部設定ファイルよりもJetBrains組み込みのインデックス作成を活用することに重点を置いているため、柔軟性は低いです。[](https://code.visualstudio.com/docs/copilot/copilot-customization)
- **パフォーマンス**:
  - **VS Code**: 一般的に軽量なアーキテクチャにより、特に小規模プロジェクトでは高速です。
  - **JetBrains IDEA**: 大規模プロジェクトでは、IDEのリソースを多く消費するインデックス作成により、わずかな遅延が発生する可能性がありますが、これによりより豊富なコンテキスト認識が可能になります。

---

### **6. まとめ表**

| **機能/側面**                 | **JetBrains IDEA**                                                                 | **VS Code**                                                                   |
|-------------------------------|-----------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| **最近使用したファイルのコンテキスト** | IDEのインデックス作成により、最近開いたファイルを自動的に含む。                    | 明示的なコンテキスト指定（例：`#file`, `#codebase`）を必要とする。             |
| **コードベース全体のコンテキスト**  | コードベース全体のクエリに対する`@project`機能（2025年2月）。                      | ワークスペース全体の検索に対する`@workspace`および`#codebase`。                |
| **Inline Chat**               | サポート（Shift+Ctrl+I/G）。集中した対話用。                                       | サポート（⌘I/Ctrl+I）。より広範なスマートアクション付き。                      |
| **マルチモデルサポート**        | 限定的。主にGitHubのデフォルトモデルを使用。                                        | GPT-4o, Claude, Geminiなどをサポート。                                         |
| **エージェントモード**          | 利用不可。                                                                        | 自律的なマルチファイル編集とターミナルコマンド用に利用可能。                  |
| **カスタム指示**               | サポートされているが柔軟性は低い。IDEのインデックス作成に依存。                    | `.github/copilot-instructions.md`およびプロンプトファイルにより高度にカスタマイズ可能。 |
| **機能展開**                   | 遅い。機能はVS Codeより遅れる。                                                    | 速い。新しい機能を最初に受け取ることが多い。                                  |
| **パフォーマンス**             | 大規模プロジェクトでは重いインデックス作成により遅い。                              | 軽量なアーキテクチャにより速い。                                              |
| **使用例**                     | 深いIDE統合を伴う複雑なプロジェクトに最適。                                        | 多様なプロジェクトにわたる柔軟で軽量なワークフローに最適。                    |

---

### **7. 推奨事項**
- **JetBrains IDEA with Copilot Chatを選ぶ場合**:
  - JetBrainsのプロジェクトインデックス作成と最近使用したファイルの自動取り込みがワークフローを合理化する、大規模で複雑なプロジェクトに取り組む。
  - 機能が豊富で言語サポートが深い、まとまりのあるIDEを好み、機能の展開が遅いことを気にしない。
  - 最近使用したファイルとプロジェクト構造に対する暗黙的なコンテキスト認識を重視する。
- **VS Code with Copilot Chatを選ぶ場合**:
  - コンテキスト（例：特定のファイル、Webコンテンツ、コードベース検索）に対する正確な制御が必要。
  - エージェントモード、マルチモデルサポート、画像添付などの最新のCopilot機能にアクセスしたい。
  - 多様なプロジェクトや迅速なプロトタイピングのための、軽量でカスタマイズ可能なエディタを好む。

---

### **結論**
JetBrains IDEAとVS Codeの間のCopilot Chatの主な違いは、コンテキストの扱い方にあります。JetBrains IDEAはその強力なプロジェクトインデックス作成により最近開いたファイルを自動的に含むため、プロジェクト中心のワークフローではよりシームレスに感じられます。一方、VS Codeは明示的で柔軟なコンテキスト管理を提供し、きめ細かい制御を好むユーザーに理想的です。さらに、VS Codeは新しい機能をより速く受け取り、エージェントモードやマルチモデル選択などのより高度な機能をサポートする傾向があります。選択は、JetBrainsの深いIDE統合を優先するか、VS Codeの柔軟性と迅速なアップデートを優先するかによって異なります。Copilot機能に関する最新情報については、GitHub CopilotドキュメントまたはJetBrainsプラグインのアップデートを確認してください。[](https://docs.github.com/en/copilot/about-github-copilot/github-copilot-features)[](https://code.visualstudio.com/docs/copilot/overview)