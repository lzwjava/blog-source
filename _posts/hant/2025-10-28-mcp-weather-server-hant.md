---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 構建基本MCP天氣伺服器
translated: true
type: note
---

### 什麼是模型上下文協議（MCP）？

模型上下文協議（MCP）是一個開放標準，定義了應用程式與人工智能系統（如大型語言模型）之間如何交換上下文，例如工具、資源和提示。它實現了LLM（例如Claude）與外部服務之間的無縫整合，讓構建可擴展的AI代理變得更簡單。本指南基於官方快速入門教程，重點在於使用純Python（不使用`uv`）設置一個基本的MCP伺服器，該伺服器連接至國家氣象局API，提供一個簡單的天氣伺服器。此伺服器公開了兩個工具：`get_alerts`（用於獲取州天氣警報）和`get_forecast`（用於獲取位置預報）。

### 先決條件
- 對Python和LLM（例如Claude）有基本認識。
- 已安裝Python 3.10或更高版本。
- 可訪問終端機（推薦macOS/Linux；Windows指令類似，但請使用PowerShell）。
- 用於測試：Claude for Desktop應用程式（適用於macOS/Windows；不支援Linux——如有需要，請使用自定義客戶端）。
- 注意：MCP伺服器透過stdio（stdin/stdout）使用JSON-RPC進行通訊。為避免訊息損壞，請勿在程式碼中向stdout打印；請改用logging輸出至stderr。

### 步驟1：設置您的環境
1. 創建一個新的專案目錄：
   ```
   mkdir weather
   cd weather
   ```

2. 創建並啟動虛擬環境：
   ```
   python -m venv .venv
   source .venv/bin/activate  # Windows系統：.venv\Scripts\activate
   ```

3. 升級pip（推薦以確保可靠性）：
   ```
   python -m pip install --upgrade pip
   ```

4. 安裝依賴項（MCP SDK和HTTP客戶端）：
   ```
   pip install "mcp[cli]" httpx
   ```

5. 創建伺服器檔案：
   ```
   touch weather.py  # 或使用您的編輯器創建
   ```

### 步驟2：構建MCP伺服器
在您的編輯器中打開`weather.py`並添加以下程式碼。這使用了MCP SDK中的`FastMCP`類，它能根據類型提示和文檔字符串自動生成工具模式。

```python
from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# 初始化MCP伺服器
mcp = FastMCP("weather")

# 國家氣象局API的常量
NWS_API_BASE = "https://api.weather.gov"
USER_AGENT = "weather-app/1.0"

async def make_nws_request(url: str) -> dict[str, Any] | None:
    """向NWS API發送請求並進行適當的錯誤處理。"""
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
    """將警報特徵格式化為可讀字符串。"""
    props = feature["properties"]
    return f"""
事件: {props.get('event', 'Unknown')}
區域: {props.get('areaDesc', 'Unknown')}
嚴重程度: {props.get('severity', 'Unknown')}
描述: {props.get('description', 'No description available')}
指示: {props.get('instruction', 'No specific instructions provided')}
"""

@mcp.tool()
async def get_alerts(state: str) -> str:
    """獲取美國某個州的天氣警報。

    參數:
        state: 兩個字母的美國州代碼（例如 CA, NY）
    """
    url = f"{NWS_API_BASE}/alerts/active/area/{state}"
    data = await make_nws_request(url)

    if not data or "features" not in data:
        return "無法獲取警報或未找到任何警報。"

    if not data["features"]:
        return "該州沒有活躍警報。"

    alerts = [format_alert(feature) for feature in data["features"]]
    return "\n---\n".join(alerts)

@mcp.tool()
async def get_forecast(latitude: float, longitude: float) -> str:
    """獲取某個位置的天氣預報。

    參數:
        latitude: 位置的緯度
        longitude: 位置的經度
    """
    # 首先獲取預報網格端點
    points_url = f"{NWS_API_BASE}/points/{latitude},{longitude}"
    points_data = await make_nws_request(points_url)

    if not points_data:
        return "無法獲取此位置的預報數據。"

    # 從points響應中獲取預報URL
    forecast_url = points_data["properties"]["forecast"]
    forecast_data = await make_nws_request(forecast_url)

    if not forecast_data:
        return "無法獲取詳細預報。"

    # 將時段格式化為可讀預報
    periods = forecast_data["properties"]["periods"]
    forecasts = []
    for period in periods[:5]:  # 只顯示接下來5個時段
        forecast = f"""
{period['name']}:
溫度: {period['temperature']}°{period['temperatureUnit']}
風速: {period['windSpeed']} {period['windDirection']}
預報: {period['detailedForecast']}
"""
        forecasts.append(forecast)

    return "\n---\n".join(forecasts)

def main():
    # 透過stdio運行伺服器
    mcp.run(transport='stdio')

if __name__ == "__main__":
    main()
```

- **關鍵注意事項**：
  - 工具使用`@mcp.tool()`裝飾器定義。LLM主機（例如Claude）將根據用戶查詢調用它們。
  - 此範例使用異步函數進行API調用。
  - 錯誤處理確保了優雅的失敗（例如，沒有數據時返回用戶友好的訊息）。
  - 對於生產環境，請添加日誌記錄（例如，透過`logging`模組輸出至stderr）和速率限制。

### 步驟3：本地測試伺服器
運行伺服器：
```
python weather.py
```
它應該在stdio上開始監聽而沒有輸出（這是正常的）。要手動測試，您需要一個MCP客戶端，但可以繼續進行整合以進行完整測試。

### 步驟4：連接到主機（例如Claude for Desktop）
1. 從[claude.ai/download](https://claude.ai/download)下載並安裝Claude for Desktop。

2. 通過創建/編輯`~/Library/Application Support/Claude/claude_desktop_config.json`（macOS）或Windows上的等效路徑（`%APPDATA%\Claude\claude_desktop_config.json`）來配置應用程式：
   ```json
   {
     "mcpServers": {
       "weather": {
         "command": "python",
         "args": [
           "/ABSOLUTE/PATH/TO/weather/weather.py"  // 替換為您的專案路徑（使用 pwd 來查找它）
         ],
         "cwd": "/ABSOLUTE/PATH/TO/weather"  // 可選：如有需要，設置工作目錄
       }
     }
   }
   ```
   - 使用絕對路徑（例如，macOS上為`/Users/yourname/weather/weather.py`）。
   - 在Windows上，使用正斜杠`/`或雙反斜杠`\\`。
   - 確保在本地測試時您的虛擬環境已啟動，但對於Claude，它運行的是您系統中的Python可執行檔（確保venv的site-packages可訪問，或者如果偏好，可以全域安裝——但推薦使用venv）。
   - 使用`which python`（macOS/Linux）或`where python`（Windows）查找Python路徑。

3. 完全重啟Claude for Desktop（完全退出，例如在macOS上使用Cmd+Q）。

4. 在Claude中測試：
   - 打開Claude並點擊「搜尋與工具」圖示（滑桿圖示）。
   - 您應該看到`get_alerts`和`get_forecast`被列出。
   - 查詢範例：
     - "加利福尼亞州有哪些活躍天氣警報？"
     - "緯度37.77，經度-122.41的天氣預報是什麼？"（三藩市座標）。
   - Claude將自動調用工具並將結果納入其回應中。
   - 注意：此API僅支援美國位置。

### 疑難排解
- **伺服器未出現在Claude中**：驗證JSON語法、絕對路徑以及應用程式的完全重啟。檢查日誌`~/Library/Logs/Claude/mcp*.log`。
- **工具錯誤**：確保伺服器在本地運行無錯誤。如果需要，添加延遲以處理API速率限制。
- **非美國查詢**：NWS API僅限美國；如需全球支援，請擴展其他API。
- 有關進階功能（資源、提示、通知），請參閱完整的MCP文檔。

這將使用純Python設置一個功能齊全的MCP伺服器。有關TypeScript/Node.js替代方案或更多範例，請查看以下資源。

### 參考資料
- [構建MCP伺服器（官方文檔）](https://modelcontextprotocol.io/docs/develop/build-server)
- [MCP快速入門指南](https://modelcontextprotocol.info/docs/quickstart/quickstart/)
- [模型上下文協議指南與演示](https://www.datacamp.com/tutorial/mcp-model-context-protocol)
- [模型上下文協議如何運作](https://www.freecodecamp.org/news/how-the-model-context-protocol-works/)
- [MCP實用入門指南](https://medium.com/@davidlfliang/guide-a-practical-introduction-to-model-context-protocol-mcp-2f63b636f510)