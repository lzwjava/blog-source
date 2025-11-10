---
audio: false
generated: true
lang: ja
layout: post
title: APIにおけるAIツール活用の解説
translated: true
type: note
---

### AI APIにおけるツール使用とは？

ツール使用（「ツール呼び出し」や「関数呼び出し」とも呼ばれる）は、AI APIの機能の一つで、大規模言語モデル（LLM）が外部のツール、関数、またはAPIと連携することを可能にします。モデルは内部の知識のみに基づいて応答を生成するのではなく、必要に応じて事前に定義された関数を呼び出して、リアルタイムデータを取得したり、計算を実行したり、アクションを実行したりすることを決定できます。これにより、天気の問い合わせ、データベースの検索、他のサービスとの統合などのタスクにおいて、AIをより動的で有用なものにすることができます。

このプロセスは通常、以下のように機能します：
- JSON形式で説明とパラメータを持つツール（関数）を定義します。
- モデルはユーザーのクエリを分析し、必要に応じて関数名と引数を含む「ツール呼び出し」を出力します。
- アプリケーションは関数を実行し、結果をモデルにフィードバックします。
- モデルはツールの出力を組み込んだ最終的な応答を生成します。

これは一般的にOpenAIの関数呼び出しAPIに触発されており、MistralやDeepSeekなどの多くのプロバイダーが互換性のある実装をサポートしています。

### ツール使用にはMistralとDeepSeek、どちらを選ぶべきか？

Mistral AIとDeepSeek AIの両方がAPIでツール呼び出しをサポートしており、外部統合を必要とするエージェントやアプリケーションの構築に適しています。利用可能な情報に基づく簡単な比較を以下に示します：

- **ツール使用のサポート**:
  - 両者ともOpenAIのAPIと同様の構造に従っており、JSONスキーマを介したツールとの容易な統合が可能です。
  - Mistralは、Mistral LargeやMediumなどのモデルでサポートし、エージェントベースのワークフローのオプションを提供します。
  - DeepSeekは主に「deepseek-chat」モデルを通じてサポートし、OpenAIのSDKと完全に互換性があります。

- **長所と短所**:
  - **Mistral**: 一般的なタスクにおいてより汎用性が高く、一部のベンチマークでは推論が高速で、ヨーロッパのデータプライバシー要件により適しています。迅速な応答に優れ、強力な多言語対応能力を持っています。ただし、DeepSeekと比較して（例: 入力/出力コストが高いなど）より高価になる可能性があります。
  - **DeepSeek**: 大幅にコストが安く（一部の比較では最大28倍安い）、数学、コーディング、推論タスクに強いです。予算を重視するユーザーや高使用量に理想的です。欠点としては、非技術的なタスクでのパフォーマンスが遅い可能性があることや、マルチモーダル機能への重点が少ないことが挙げられます。
  - **どちらを選ぶべき？** コストが優先事項であり、ツールを使用したコーディング/数学に関するユースケースがある場合は、DeepSeekを選択してください。より広範なアプリケーション、高速な応答、またはエージェントなどのエンタープライズ機能の場合は、Mistralの方が優れています。両者ともオープンソースフレンドリーで高性能ですが、特定のニーズに合わせてテストしてください。

最終的には、ツール使用に関してどちらかが厳密に「優れている」わけではありません - 両者ともうまく機能します。DeepSeekはコスト削減で優位に立つ可能性があり、Mistralはより洗練されたエージェント統合を提供します。

### ツール使用の使用方法

ツール呼び出しを使用するには、それぞれのプロバイダーからAPIキーを取得する必要があります（Mistralの場合はmistral.ai、DeepSeekの場合はplatform.deepseek.comでサインアップしてください）。両者ともOpenAIのものと同様のPython SDKを使用します。以下に、簡単な天気問い合わせツールのステップバイステップの例を示します。

#### Mistral AIでのツール使用
MistralのAPIは、チャット補完において`MistralClient`を介したツール呼び出しをサポートしています。SDKは`pip install mistralai`でインストールします。

**Pythonコード例**（公式およびコミュニティソースから改変）:
```python
from mistralai import Mistral

# APIキーでクライアントを初期化
api_key = "YOUR_MISTRAL_API_KEY"
model = "mistral-large-latest"  # ツール呼び出しをサポート
client = Mistral(api_key=api_key)

# ツール（関数）を定義
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the weather for a location.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string", "description": "The city, e.g., San Francisco"}
                },
                "required": ["location"]
            }
        }
    }
]

# ユーザーメッセージ
messages = [{"role": "user", "content": "What's the weather in Hangzhou?"}]

# 最初のAPI呼び出し: モデルがツールの必要性を判断
response = client.chat.complete(
    model=model,
    messages=messages,
    tools=tools,
    tool_choice="auto"  # ツール使用を自動決定
)

# ツール呼び出しをチェック
tool_calls = response.choices[0].message.tool_calls
if tool_calls:
    # モデルの応答をメッセージに追加
    messages.append(response.choices[0].message)
    
    # ツールの実行をシミュレート（実際のコードでは実際のAPIを呼び出す）
    tool_call = tool_calls[0]
    if tool_call.function.name == "get_weather":
        location = eval(tool_call.function.arguments)["location"]
        weather_result = "24°C and sunny"  # 実際の関数呼び出しに置き換え
        
        # ツール結果を追加
        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "name": tool_call.function.name,
            "content": weather_result
        })
    
    # 2回目のAPI呼び出し: モデルが最終応答を生成
    final_response = client.chat.complete(model=model, messages=messages)
    print(final_response.choices[0].message.content)
else:
    print(response.choices[0].message.content)
```

このコードは、クエリを送信し、ツール呼び出しをチェックし、それを実行（ここではシミュレート）し、最終的な回答を取得します。エージェントベースの設定の場合、より複雑なワークフローのためにMistralのベータ版エージェントAPIを使用してください。

#### DeepSeek AIでのツール使用
DeepSeekのAPIはOpenAI互換なので、OpenAI Python SDKを使用できます。`pip install openai`でインストールします。

**Pythonコード例**（公式ドキュメントから）:
```python
from openai import OpenAI

# DeepSeekのベースURLとAPIキーでクライアントを初期化
client = OpenAI(
    api_key="YOUR_DEEPSEEK_API_KEY",
    base_url="https://api.deepseek.com"
)

# ツールを定義
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get weather of a location, the user should supply a location first",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA",
                    }
                },
                "required": ["location"]
            },
        }
    },
]

# メッセージを送信する関数
def send_messages(messages):
    response = client.chat.completions.create(
        model="deepseek-chat",  # ツール呼び出しをサポート
        messages=messages,
        tools=tools
    )
    return response.choices[0].message

# ユーザーメッセージ
messages = [{"role": "user", "content": "How's the weather in Hangzhou?"}]
message = send_messages(messages)
print(f"User>\t {messages[0]['content']}")

# ツール呼び出しを処理
tool = message.tool_calls[0]
messages.append(message)

# ツール実行をシミュレート（実際の関数に置き換え）
messages.append({"role": "tool", "tool_call_id": tool.id, "content": "24℃"})

# 最終応答を取得
message = send_messages(messages)
print(f"Model>\t {message.content}")
```

これは同じ流れに従います：クエリ → ツール呼び出し → 実行 → 最終応答。DeepSeekはコンテキスト長を制限しているので、メッセージは簡潔に保ってください。

高度な使用法については、レート制限、コスト、モデル固有のドキュメントを確認してください。無効なパラメータなどのエラーを処理するために、サンドボックスでテストしてください。

### 参考文献
- [Mistral AI Function Calling Documentation](https://docs.mistral.ai/agents/function_calling/)
- [DeepSeek API Function Calling Guide](https://api-docs.deepseek.com/guides/function_calling)
- [Mistral AI Function Calling Example with Code](https://medium.com/@jcrsch/mistral-ai-function-calling-a-simple-example-with-code-72f3a762550f)
- [DeepSeek vs. Mistral: A Comprehensive AI Models Comparison](https://medium.com/ai-tools-tips-and-news/deepseek-vs-mistral-a-comprehensive-ai-models-comparison-f7d7b86f4b28)
- [Mistral Large vs DeepSeek-V3 Comparison](https://docsbot.ai/models/compare/mistral-large-2/deepseek-v3)