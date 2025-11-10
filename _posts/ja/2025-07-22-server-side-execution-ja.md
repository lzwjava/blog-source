---
audio: false
generated: true
lang: ja
layout: post
title: サーバーサイド実行によるAIツール呼び出しの最適化
translated: true
type: note
---

はい、従来のチャットボットにおけるツールや関数呼び出しの往復的な性質（AIモデルが呼び出しを生成し、クライアントや別のサービスに送信し、実行を待ち、結果を受け取る）は、特にリアルタイムアプリケーションにおいて、確かにレイテンシを引き起こす可能性があります。これは多くの場合、ネットワークオーバーヘッド、シリアライゼーション/デシリアライゼーション、および複数回のAPIラウンドトリップが必要となることに起因します。Lambda関数の使用や、サーバーサイドで実行するためのPythonコードを受け入れるAPIを設計するというあなたの提案は、これを軽減する賢い方法です。つまり、クライアントとサーバー間のやり取りを最小限に抑えるために、計算をサーバーに移行するものです。これを概念的的に分解し、実現可能性、潜在的な実装方法、およびトレードオフについて説明します。

### 従来のツール呼び出しが遅くなる理由
多くのAIフレームワーク（例: LangChain、OpenAIの関数呼び出し、Anthropicのツール）では以下の処理が行われます：
- モデルが構造化されたツール呼び出し（例：関数名と引数を含むJSON）を出力します。
- クライアント（またはエージェント）が、関数をローカルまたは別のAPI経由で実行します。
- 結果が会話履歴に追加され、次の推論ステップのためにモデルに送り返されます。
このループは、データ分析や多段階の推論などの複雑なタスクでは、1サイクルあたり数秒の遅延を追加し、累積する可能性があります。

### Lambda関数またはサーバーサイドコード実行の使用
あなたのアイデアは、「サーバーレス」または「サンドボックス化された」実行モデルに沿っており、AIが生成したコード（またはLambdaのようなスニペット）がモデルをホストするサーバー上で直接実行されます。これにより、すべてを一つの環境に保ち、ユーザーからのAPI呼び出しを事実上1回だけに抑えることができます。

- **Lambda関数アプローチ**: AWS Lambda、Google Cloud Functions、Azure Functionsなどのサービスでは、サーバーを管理することなく、オンデマンドで小さな短命のPythonコードスニペットを実行できます。AIのコンテキストでは：
  - チャットボットのバックエンドがAIモデル（例: OpenAI API経由）をラップし、ツールとしてLambdaを統合できます。
  - モデルがLambda式または短い関数を生成し、サーバーサイドで呼び出されます。
  - 長所: スケーラブル、従量課金制、高速な起動（多くの場合、コールドスタートで100ミリ秒未満）。
  - 短所: 実行時間の制限（例：AWSでは最大15分）、タスクが複数の呼び出しにまたがる場合は状態管理を処理する必要があります。
  - 例: AIエージェントがデータを処理するためのLambda（例: `lambda x: sum(x) if isinstance(x, list) else 0`）を生成し、それをLambdaエンドポイントに送信し、結果をインラインで取得できます。

- **Pythonコードを受け入れて実行するAPIの設計**:
  - はい、これは絶対に可能であり、実際に運用システムで既に存在しています。鍵は、任意のコード実行（例：ファイルの削除やネットワーク呼び出し）のようなセキュリティリスクを防ぐための**サンドボックス化**です。
  - 仕組み: APIエンドポイントはコードスニペット（文字列として）を受け取り、隔離された環境で実行し、出力/エラーをキャプチャして結果を返します。AIモデルは、サーバーを離れることなく、このコードを反復的に生成して「呼び出す」ことができます。
  - 利点:
    - レイテンシの低減: 実行はモデルと同じデータセンターで行われ、多くの場合ミリ秒単位です。
    - 複雑なタスクの実現: 外部ツールなしでのデータ処理、数学的シミュレーション、ファイル操作など。
    - ステートフルなセッション: 一部の実装では、呼び出しを跨いでREPLのような環境を維持します。
  - セキュリティ対策:
    - コンテナ（Docker）、マイクロVM（Firecracker）、または制限付きPythonインタープリター（例: PyPyサンドボックス化や制限付きグローバル変数）の使用。
    - リソース制限: CPU/時間の割り当て、ネットワークアクセスなし、許可されたモジュールのみ（例: numpy、pandasは可、osやsubprocessは不可）。
    - `restrictedpython`のようなライブラリや、E2B/Firecrackerのようなツールは、既製のサンドボックスを提供します。

### 実世界の例と実装
いくつかのAIプラットフォームが、すでに様々な程度でこれをサポートしています：
- **OpenAIのAssistants APIとCode Interpreter**: モデルがOpenAIのサーバー上のサンドボックス化された環境でPythonコードを記述および実行することを可能にします。モデルはファイルをアップロードし、コードを実行し、結果に対して反復処理を行えます—すべてサーバーサイドで。クライアントサイドでの実行は不要です。
- **GoogleのGemini API Code Execution**: モデルがコードを反復的に生成および実行し、外部呼び出しなしで出力から学習できる組み込みのPythonサンドボックスを提供します。
- **カスタムソリューション**:
  - **E2B Sandbox**: Jupyterカーネルを使用したクラウドベースのサンドボックスを作成するためのSDK/API。データ分析ツールに最適で、AIエージェントが安全に実行するコードを送信できます。
  - **Modal Sandboxes**: 隔離された環境でAI生成コードを実行するためのプラットフォーム。LLMエージェントでよく使用されます。
  - **SandboxAI (オープンソース)**: AI生成のPythonをサンドボックスで実行するためのランタイム。
  - DIYの場合: コードをPOSTで受け取り、制限された名前空間で`exec()`を使用するか、リクエストごとにDockerコンテナを起動するFastAPIまたはFlaskサーバーを構築します。

コード的には、単純なAPIエンドポイントは以下のようになるかもしれません（説明のための疑似コード）：

```python
from fastapi import FastAPI
import restrictedpython  # 安全な実行のため

app = FastAPI()

@app.post("/execute")
def execute_code(code: str):
    safe_globals = {"__builtins__": restrictedpython.safe_builtins}  # 制限された環境
    try:
        result = {}
        exec(code, safe_globals, result)  # コードを実行
        return {"output": result.get("output")}
    except Exception as e:
        return {"error": str(e)}
```

これをチャットボットに統合：AIがユーザー入力に基づいてコードを生成し、エンドポイントを内部的に呼び出し、結果を組み込みます。

### 潜在的な欠点とベストプラクティス
- **セキュリティリスク**: 任意のコード実行は危険です—常にサンドボックス化してください。信頼できないユーザーを扱う場合は避けてください。
- **コストとスケーラビリティ**: サーバーサイド実行はより多くの計算リソースを使用します。最適化のためにNew Relicなどのツールで監視してください。
- **デバッグ**: 生成されたコードのエラーは、適切に処理されないとループする可能性があります。
- **最適化のための代替案**:
  - ツール呼び出しのバッチ処理: 複数の関数を1回のサーバーラウンドトリップにグループ化します。
  - ストリーミング: ツールを並列実行しながら応答をストリーミングするAPIを使用します。
  - レイテンシに耐性がある場合はクライアントサイド: 非機密タスクの場合、ローカルで実行します。
- スクラッチから構築する場合は、カスタムツールをサポートし、サーバーサイド実行用に設定できるLangChainやVercelのAI SDKなどのフレームワークから始めてください。

このアプローチは、特に計算タスクにおいて、チャットボットを大幅に高速化し、より高機能にすることができます。これを実装する場合は、迅速な成果を得るために、まずOpenAIやGeminiの組み込み機能から始めることを検討してください。

[Building a Sandboxed Environment for AI generated Code Execution](https://anukriti-ranjan.medium.com/building-a-sandboxed-environment-for-ai-generated-code-execution-e1351301268a)  
[substratusai/sandboxai: Run AI generated code in isolated sandboxes](https://github.com/substratusai/sandboxai)  
[Build AI data analyst with sandboxed code execution using TS ... - E2B](https://e2b.dev/blog/build-ai-data-analyst-with-sandboxed-code-execution-using-typescript-and-gpt-4o)  
[Code execution | Gemini API](https://ai.google.dev/gemini-api/docs/code-execution)  
[Assistants Code Interpreter - OpenAI API](https://platform.openai.com/docs/assistants/tools/code-interpreter)  
[Modal Sandboxes](https://modal.com/use-cases/sandboxes)  
[Optimizing AI chatbot performance with New Relic AI monitoring](https://newrelic.com/blog/how-to-relic/optimizing-ai-chatbot-performance)