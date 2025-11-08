---
audio: false
generated: false
image: true
lang: hant
layout: post
title: 防火牆、代理API、VPN偵測
translated: true
type: post
---

### 目錄

1. [代理伺服器中的 API 能否避開 GFW 封鎖？](#代理伺服器中的-api-能否避開-gfw-封鎖)
   - 混合代理與 API 流量可避免 GFW 封鎖
   - GFW 能區分代理與一般 HTTP/HTTPS 流量
   - GFW 可能基於純代理流量進行封鎖
   - GFW 使用時間窗口進行流量分析
   - 定期存取 API 或可防止偵測

2. [防火長城 (GFW) 運作原理](#防火長城-gfw-運作原理)
   - GFW 記錄含來源與目標資料的請求
   - 封鎖與非法活動相關的 IP
   - 使用規則檢測特定協議
   - 可根據非法請求比例進行封鎖
   - 採用 AI 進行智能流量模式檢測

3. [ChatGPT iOS VPN 檢測分析](#chatgpt-ios-vpn-檢測分析)
   - ChatGPT iOS 現可配合部分 VPN 使用
   - 存取取決於 VPN 伺服器位置
   - 檢測基於特定 IP 地址
   - 部分雲端供應商 IP 遭封鎖

## 代理伺服器中的 API 能否避開 GFW 封鎖？

我在 Shadowsocks 實例上運行了一個簡單伺服器，程式碼如下：

```python
from flask import Flask, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)  # 為所有路由啟用 CORS

@app.route('/bandwidth', methods=['GET'])
def get_bandwidth():
    # 運行 vnstat 命令獲取 eth0 的 5 分鐘間隔流量統計
    result = subprocess.run(['vnstat', '-i', 'eth0', '-5', '--json'], capture_output=True, text=True)
    data = result.stdout

    # 將捕獲的資料作為 JSON 回應返回
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

並使用 nginx 監聽 443 端口，配置如下：

```bash
server {
    listen 443 ssl;
    server_name www.some-domain.xyz;

    ssl_certificate /etc/letsencrypt/live/www.some-domain.xyz/fullchain.pem; # managed by 
    # ...
    location / {

        proxy_pass http://127.0.0.1:5000/;
        # ...
    }
}
```

此伺服器程式提供網路數據，我將其作為代理伺服器使用，讓我能透過網路數據在部落格上顯示線上狀態。

有趣的是，該伺服器至今數日尚未遭到防火長城（GFW）或其他網路管控系統封鎖。通常，我設定的代理伺服器會在一兩天內遭封鎖。此伺服器在如 51939 的端口運行 Shadowsocks 程式，因此其流量混合了 Shadowsocks 與常規 API 流量。這種混合似乎讓 GFW 認為該伺服器並非專用代理，而是正常伺服器，從而避免 IP 遭封鎖。

此觀察頗具啟發性。GFW 似乎採用特定邏輯來區分代理流量與常規流量。雖然 Twitter 和 YouTube 等許多網站在中國被封鎖，但仍有大量境外網站（如國際大學和企業網站）可正常存取。

這表明 GFW 可能基於區分正常 HTTP/HTTPS 流量與代理相關流量的規則運作。同時處理兩類流量的伺服器似乎能避開封鎖，而僅處理代理流量的伺服器則較易遭封鎖。

關鍵問題在於 GFW 用於累積封鎖資料的時間範圍——是一天還是一小時。在此時間範圍內，系統會檢測流量是否純屬代理性質。若是，則該伺服器 IP 將遭封鎖。

我常瀏覽部落格回顧所寫內容，但接下來幾週我的重心將轉移至其他任務而非撰寫文章。這將減少我透過 443 端口存取 `bandwidth` API 的頻率。若發現再次遭封鎖，我應編寫程式定期存取此 API 以誤導 GFW。

以下是經優化結構與清晰度的文本：

## 防火長城 (GFW) 運作原理

### 步驟 1：記錄請求

```python
import time

# 儲存請求資料的資料庫
request_log = []

# 記錄請求的函數
def log_request(source_ip, target_ip, target_port, body):
    request_log.append({
        'source_ip': source_ip,
        'target_ip': target_ip,
        'target_port': target_port,
        'body': body,
        'timestamp': time.time()
    })
```

`log_request` 函數記錄傳入請求的基本資訊，包括來源 IP、目標 IP、目標端口、請求主體及時間戳。

### 步驟 2：檢查並封鎖 IP

```python
# 檢查請求並封鎖 IP 的函數
def check_and_ban_ips():
    banned_ips = set()

    # 遍歷所有已記錄的請求
    for request in request_log:
        if is_illegal(request):
            banned_ips.add(request['target_ip'])
        else:
            banned_ips.discard(request['target_ip'])

    # 對所有識別出的 IP 實施封鎖
    ban_ips(banned_ips)
```

`check_and_ban_ips` 函數遍歷所有已記錄請求，識別並封鎖與非法活動相關的 IP。

### 步驟 3：定義非法請求的標準

```python
# 模擬檢查請求是否非法的函數
def is_illegal(request):
    # 實際非法請求檢查邏輯的佔位符
    # 例如檢查請求主體或目標
    return "illegal" in request['body']
```

此處 `is_illegal` 檢查請求主體是否包含 "illegal" 一詞。可根據非法活動的具體定義擴展更複雜的邏輯。

### 步驟 4：封鎖已識別 IP

```python
# 封鎖 IP 列表的函數
def ban_ips(ip_set):
    for ip in ip_set:
        print(f"封鎖 IP: {ip}")
```

一旦識別出非法 IP，`ban_ips` 函數便透過列印其 IP 地址實施封鎖（在實際系統中可能直接阻擋）。

### 步驟 5：基於 80% 非法請求的替代封鎖方法

```python
# 根據 80% 非法請求檢查並封鎖 IP 的函數
def check_and_ban_ips():
    banned_ips = set()
    illegal_count = 0
    total_requests = 0

    # 遍歷所有已記錄的請求
    for request in request_log:
        total_requests += 1
        if is_illegal(request):
            illegal_count += 1

    # 若 80% 或以上請求屬非法，則封鎖相關 IP
    if total_requests > 0 and (illegal_count / total_requests) >= 0.8:
        for request in request_log:
            if is_illegal(request):
                banned_ips.add(request['target_ip'])

    # 對所有識別出的 IP 實施封鎖
    ban_ips(banned_ips)
```

此替代方法根據非法請求的比例判斷是否封鎖 IP。若某 IP 的請求中有 80% 或以上屬非法，則予封鎖。

### 步驟 6：增強的非法請求檢查（例如 Shadowsocks 與 Trojan 協議檢測）

```python
def is_illegal(request):
    # 檢查是否使用 Shadowsocks 協議（主體包含類二進位資料）
    if request['target_port'] == 443:
        if is_trojan(request):
            return True
    elif is_shadowsocks(request):
        return True
    return False
```

`is_illegal` 函數現亦檢查特定協議如 Shadowsocks 和 Trojan：
- **Shadowsocks**：可檢查請求主體是否包含加密或類二進位資料。
- **Trojan**：若請求經 443 端口（HTTPS）傳輸且符合特定模式（如 Trojan 流量特徵），則標記為非法。

### 步驟 7：合法請求範例

例如，`GET https://some-domain.xyz/bandwidth` 等請求顯然合法，不會觸發封鎖機制。

### 步驟 8：代理伺服器流量特徵

代理伺服器的流量特徵與常規網站或 API 伺服器截然不同。GFW 需區分正常網站流量與代理伺服器流量，兩者外觀可能完全不同。

### 步驟 9：用於智能檢測的機器學習與 AI 模型

考慮到網路上傳輸的請求與回應範圍廣泛，GFW 可能採用 AI 與機器學習模型分析流量模式，智能檢測非法行為。透過訓練系統識別多類流量並使用先進技術，可更有效地根據觀測模式封鎖或過濾流量。

## 更新

儘管多方嘗試，我的代理伺服器持續遭封鎖。為緩解此問題，我已實施透過 Digital Ocean 的反向 IP 功能實現的應對方案，可在每次封鎖時快速分配新 IP 地址。

---

## ChatGPT iOS VPN 檢測分析

*2024.12.26*

今日，我發現 ChatGPT iOS 應用程式現可於中國透過 VPN 登入。此前，其會顯示如下阻擋提示。

然而，截至今日，配合 VPN 使用一切正常。  

我記得 ChatGPT iOS 應用程式初發行時，配合 VPN 使用並無障礙。其後，VPN 檢測轉趨嚴格，導致登入困難。慶幸的是，此限制近期似乎已放寬。  

經進一步測試，我發現使用 DigitalOcean 新加坡區域 VPN 時無法存取應用程式。但使用台灣或英國的 VPN（由 https://zhs.cloud 提供）時，則運作完美。

ChatGPT iOS 的 VPN 檢測似乎基於特定 IP 地址。部分雲端供應商或特定 IP 地址遭封鎖，這或可解釋為何 VPN 伺服器位置會導致不一致的結果。

![](assets/images/chatgpt/block.jpg){: .responsive }

![](assets/images/chatgpt/c1.png){: .responsive }