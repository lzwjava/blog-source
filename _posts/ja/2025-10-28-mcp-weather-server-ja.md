---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: 基本MCP気象サーバーの構築
translated: true
type: note
---

### Model Context Protocol（MCP）とは何ですか？

Model Context Protocol（MCP）は、アプリケーションとAIシステム（大規模言語モデルなど）がツール、リソース、プロンプトなどのコンテキストを交換する方法を定義するオープン標準です。LLM（Claudeなど）と外部サービスのシームレスな統合を可能にし、拡張可能なAIエージェントの構築を容易にします。このガイドでは、National Weather Service APIに接続するシンプルな天気サーバーの公式クイックスタートチュートリアルに基づき、`uv`を使用しないプレーンなPythonで基本的なMCPサーバーをセットアップする方法に焦点を当てます。このサーバーは、`get_alerts`（州の天気警報用）と`get_forecast`（場所の予報用）の2つのツールを公開します。

### 前提条件
- PythonとLLM（Claudeなど）の基本的な知識。
- Python 3.10以上がインストールされていること。
- ターミナルへのアクセス（macOS/Linux推奨。WindowsではPowerShellを使用）。
- テスト用：Claude for Desktopアプリ（macOS/Windowsで利用可能。Linuxでは不可—必要に応じてカスタムクライアントを使用）。
- 注意：MCPサーバーはstdio（stdin/stdout）を介したJSON-RPCで通信します。メッセージの破損を防ぐため、コードでstdoutに出力しないでください。代わりにstderrにロギングを使用します。

### ステップ1: 環境のセットアップ
1. 新しいプロジェクトディレクトリを作成：
   ```
   mkdir weather
   cd weather
   ```

2. 仮想環境を作成して有効化：
   ```
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```

3. pipをアップグレード（信頼性向上のため推奨）：
   ```
   python -m pip install --upgrade pip
   ```

4. 依存関係をインストール（MCP SDKとHTTPクライアント）：
   ```
   pip install "mcp[cli]" httpx
   ```

5. サーバーファイルを作成：
   ```
   touch weather.py  # またはエディタで作成
   ```

### ステップ2: MCPサーバーの構築
エディタで`weather.py`を開き、以下のコードを追加します。これはMCP SDKの`FastMCP`クラスを使用し、型ヒントとdocstringからツールスキーマを自動生成します。

```python
from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# MCPサーバーを初期化
mcp = FastMCP("weather")

# National Weather Service APIの定数
NWS_API_BASE = "https://api.weather.gov"
USER_AGENT = "weather-app/1.0"

async def make_nws_request(url: str) -> dict[str, Any] | None:
    """NWS APIに適切なエラーハンドリングでリクエストを送信"""
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/geo+json"
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None

def format_alert(feature: dict) -> str:
    """警報フィーチャーを読み取り可能な文字列にフォーマット"""
    props = feature["properties"]
    return f"""
Event: {props.get('event', 'Unknown')}
Area: {props.get('areaDesc', 'Unknown')}
Severity: {props.get('severity', 'Unknown')}
Description: {props.get('description', 'No description available')}
Instructions: {props.get('instruction', 'No specific instructions provided')}
"""

@mcp.tool()
async def get_alerts(state: str) -> str:
    """米国の州の天気警報を取得

    Args:
        state: 2文字の米国州コード（例: CA, NY）
    """
    url = f"{NWS_API_BASE}/alerts/active/area/{state}"
    data = await make_nws_request(url)

    if not data or "features" not in data:
        return "警報を取得できないか、警報が見つかりませんでした"

    if not data["features"]:
        return "この州にはアクティブな警報はありません"

    alerts = [format_alert(feature) for feature in data["features"]]
    return "\n---\n".join(alerts)

@mcp.tool()
async def get_forecast(latitude: float, longitude: float) -> str:
    """場所の天気予報を取得

    Args:
        latitude: 場所の緯度
        longitude: 場所の経度
    """
    # まず予報グリッドエンドポイントを取得
    points_url = f"{NWS_API_BASE}/points/{latitude},{longitude}"
    points_data = await make_nws_request(points_url)

    if not points_data:
        return "この場所の予報データを取得できませんでした"

    # pointsレスポンスから予報URLを取得
    forecast_url = points_data["properties"]["forecast"]
    forecast_data = await make_nws_request(forecast_url)

    if not forecast_data:
        return "詳細な予報を取得できませんでした"

    # 期間を読み取り可能な予報にフォーマット
    periods = forecast_data["properties"]["periods"]
    forecasts = []
    for period in periods[:5]:  # 次の5期間のみ表示
        forecast = f"""
{period['name']}:
Temperature: {period['temperature']}°{period['temperatureUnit']}
Wind: {period['windSpeed']} {period['windDirection']}
Forecast: {period['detailedForecast']}
"""
        forecasts.append(forecast)

    return "\n---\n".join(forecasts)

def main():
    # stdio経由でサーバーを実行
    mcp.run(transport='stdio')

if __name__ == "__main__":
    main()
```

- **主な注意点**:
  - ツールは`@mcp.tool()`デコレータで定義されます。LLMホスト（Claudeなど）はユーザークエリに基づいてこれらを呼び出します。
  - この例ではAPI呼び出しに非同期関数を使用しています。
  - エラーハンドリングにより、データがない場合などにユーザーフレンドリーなメッセージを返します。
  - 本番環境では、ロギング（`logging`モジュールでstderrに）とレート制限を追加してください。

### ステップ3: サーバーをローカルでテスト
サーバーを実行：
```
python weather.py
```
出力なしでstdioをリッスン開始するはずです（正常な動作）。手動でテストするにはMCPクライアントが必要ですが、統合テストに進んでください。

### ステップ4: ホストへの接続（Claude for Desktopなど）
1. [claude.ai/download](https://claude.ai/download)からClaude for Desktopをダウンロードしてインストール。

2. アプリを設定：`~/Library/Application Support/Claude/claude_desktop_config.json`（macOS）またはWindowsの同等のパス（`%APPDATA%\Claude\claude_desktop_config.json`）を作成/編集：
   ```json
   {
     "mcpServers": {
       "weather": {
         "command": "python",
         "args": [
           "/ABSOLUTE/PATH/TO/weather/weather.py"  # プロジェクトパスに置き換え（pwdで確認）
         ],
         "cwd": "/ABSOLUTE/PATH/TO/weather"  # オプション：必要に応じて作業ディレクトリを設定
       }
     }
   }
   ```
   - 絶対パスを使用（例：macOSでは`/Users/yourname/weather/weather.py`）。
   - Windowsではスラッシュ`/`または二重バックスラッシュ`\\`を使用。
   - ローカルテストでは仮想環境が有効化されていることを確認してください。Claudeの場合、システムのPython実行可能ファイルが実行されます（venvのsite-packagesにアクセス可能か、グローバルにインストールしてください—venvが推奨されます）。
   - Pythonのパスは`which python`（macOS/Linux）または`where python`（Windows）で確認。

3. Claude for Desktopを完全に再起動（例：macOSではCmd+Qで完全終了）。

4. Claudeでテスト：
   - Claudeを開き、「Search and tools」アイコン（スライダーアイコン）をクリック。
   - `get_alerts`と`get_forecast`がリスト表示されるはずです。
   - クエリ例：
     - 「カリフォルニア州のアクティブな天気警報は何ですか？」
     - 「緯度37.77、経度-122.41の天気予報は？」（サンフランシスコの座標）。
   - Claudeは自動的にツールを呼び出し、結果をレスポンスに組み込みます。
   - 注意：このAPIは米国の場所のみサポートしています。

### トラブルシューティング
- **サーバーがClaudeに表示されない**: JSON構文、絶対パス、アプリの完全な再起動を確認。ログは`~/Library/Logs/Claude/mcp*.log`で確認。
- **ツールエラー**: サーバーがローカルでエラーなく実行されることを確認。必要に応じてAPIレート制限のための遅延を追加。
- **米国外のクエリ**: NWS APIは米国のみサポート。グローバルサポートには他のAPIで拡張。
- 高度な機能（リソース、プロンプト、通知）については、完全なMCPドキュメントを参照。

これでプレーンなPythonを使用した機能的なMCPサーバーがセットアップされました。TypeScript/Node.jsの代替やその他の例については、以下のリソースを確認してください。

### 参考文献
- [Build an MCP Server (公式ドキュメント)](https://modelcontextprotocol.io/docs/develop/build-server)
- [MCP Quickstart Guide](https://modelcontextprotocol.info/docs/quickstart/quickstart/)
- [Model Context Protocol Guide with Demo](https://www.datacamp.com/tutorial/mcp-model-context-protocol)
- [How the Model Context Protocol Works](https://www.freecodecamp.org/news/how-the-model-context-protocol-works/)
- [Practical Introduction to MCP](https://medium.com/@davidlfliang/guide-a-practical-introduction-to-model-context-protocol-mcp-2f63b636f510)