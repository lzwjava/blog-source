---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: AWS Lambda 入門指南
translated: true
type: note
---

### AWS Lambda 入門指南

AWS Lambda 是一項無伺服器運算服務，可在事件觸發時執行您的程式碼，無需管理伺服器。以下是以初學者為導向的逐步指南，協助您建立、部署並使用第一個 Lambda 函數。本指南基於官方 AWS 文件編寫。

#### 前置準備
- 有效的 AWS 帳戶。若尚未擁有，請前往 [aws.amazon.com](https://aws.amazon.com/) 註冊。
- 對 Node.js 或 Python 等程式語言有基本認識（Lambda 支援多種執行環境）。

#### 步驟 1：建立 Lambda 函數
1. 登入 AWS 管理主控台，導覽至 Lambda 服務（在服務選單中搜尋「Lambda」）。
2. 在「函數」頁面中，點擊 **建立函數**。
3. 選擇 **從頭開始撰寫**。
4. 輸入 **函數名稱**（例如：`my-first-function`）。
5. 選擇 **執行環境**（例如：Node.js 22.x 或 Python 3.13）。
6. 保留預設架構（x86_64）並點擊 **建立函數**。

系統將自動建立執行角色（IAM 角色），並授予基本權限（例如將日誌寫入 Amazon CloudWatch）。

#### 步驟 2：編寫程式碼
在 Lambda 主控台的程式碼編輯器（位於 **程式碼** 分頁）中，將預設的「Hello World」程式碼替換為簡單範例。以下示範如何根據輸入 JSON 中的 `length` 與 `width` 鍵值計算矩形面積。

- **Node.js 範例**：
  ```javascript
  exports.handler = async (event) => {
    const length = event.length;
    const width = event.width;
    const area = length * width;
    console.log(`面積為 ${area}`);
    console.log('日誌群組：/aws/lambda/' + process.env.AWS_LAMBDA_FUNCTION_NAME);
    return { area: area };
  };
  ```

- **Python 範例**：
  ```python
  import json

  def lambda_handler(event, context):
    length = event['length']
    width = event['width']
    area = length * width
    print(f"面積為 {area}")
    print(f"日誌群組：/aws/lambda/{context.function_name}")
    return {
        'statusCode': 200,
        'body': json.dumps({'area': area})
    }
  ```

儲存變更後，直譯型語言將自動部署。

若為編譯型語言（例如 Java），請在本機建立部署套件，並透過主控台或 AWS CLI 上傳。

#### 步驟 3：測試函數
1. 在 **測試** 分頁中，點擊 **建立新測試事件**。
2. 為其命名（例如：`test-area-calc`）。
3. 貼上範例 JSON 輸入：
   ```json
   {
     "length": 6,
     "width": 7
   }
   ```
4. 儲存後點擊 **測試**。

於 **執行結果** 區塊查看結果（例如：`{"area": 42}`）。如需詳細資訊（如持續時間與記憶體使用量），請至 CloudWatch 查看日誌。

#### 步驟 4：呼叫與監控
- **手動呼叫**：使用主控台的測試按鈕或 AWS CLI：`aws lambda invoke --function-name my-first-function output.json`。
- **事件驅動呼叫**：連結觸發器如 API Gateway、S3 儲存貯體或 DynamoDB 串流。請至 **設定** > **觸發器** 分頁進行新增。
- **日誌**：將自動傳送至 CloudWatch Logs。可於 [console.aws.amazon.com/cloudwatch/home#logsV2:log-groups](https://console.aws.amazon.com/cloudwatch/home#logsV2:log-groups) 的 `/aws/lambda/您的函數名稱` 路徑下檢視。

關鍵概念：
- **事件來源/觸發器**：可呼叫函數並傳遞事件資料（JSON 承載）的服務（例如 S3 上傳）。
- **處理函數**：處理事件的入口點（例如 Node.js 的 `index.handler`）。

#### 步驟 5：清理資源（選用）
透過主控台刪除函數：操作 > 刪除。建議一併刪除相關日誌與 IAM 角色，以避免產生費用。

#### 實用提示
- 可先使用免費方案（每月 100 萬次請求）。
- 進階部署建議使用 AWS SAM 或 Serverless Framework。
- 於正式環境中，請在 **設定** 分頁中配置環境變數、層與 VPC 設定。

[建立您的第一個 Lambda 函數](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html)