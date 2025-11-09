---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 經濟實惠的 Markdown 轉 PDF API
translated: true
type: note
---

### 推薦的平價選擇：Google Cloud Run

對於一個簡單的基於 Java 的 API，用於將 Markdown 轉換為 PDF（例如使用 Flying Saucer 或 iText 等函式庫），每週僅約 100 個請求用於個人部落格使用，**Google Cloud Run** 是最具成本效益的選擇。它是一個無伺服器平台，運行容器化應用程式，在閒置時可縮減至零，並且僅按實際使用量收費。無需管理虛擬機器或擔心持續運行的成本——非常適合像您這樣的低流量場景。

#### 為什麼選擇 Cloud Run 而非其他選項？
- **與 Compute Engine（虛擬機器）比較**：虛擬機器即使在閒置時也有固定的每小時成本，這將顯得過度且更昂貴（對於小型實例，每月最低約 5-10 美元）。
- **與 App Engine 比較**：雖然有類似的無伺服器優勢，但 Cloud Run 對於 Java 容器更為靈活，並且在零星使用情況下通常更便宜。
- 您的工作負載完全在免費額度內，因此實際上預計每月**0 美元**。

#### 預估成本
以每週 100 個請求（約每月 400 個）計算：
- 假設每個請求使用 1 個 vCPU 和 0.5 GiB 記憶體，持續 10 秒（對於快速的 Markdown 轉 PDF 轉換來說是保守估計）。
- 總使用量：每月約 4,000 vCPU 秒和 2,000 GiB 秒。
- **免費額度完全涵蓋**：每月 180,000 vCPU 秒、360,000 GiB 秒和 200 萬個請求（在大多數區域）。
- 如果超出（可能性很低），付費費率約為 $0.000024/vCPU 秒 + $0.0000025/GiB 秒 + $0.40/百萬請求（超出免費額度後）——每月仍低於 $0.10。

在您的情況下沒有出口費用（同一區域內的內部 API 呼叫免費）。

#### 推薦區域：us-central1（愛荷華州）
- 這是 Cloud Run 最便宜的 Tier 1 區域，擁有最低的計算費率，並且在北美沒有延遲溢價。
- Tier 1 區域（美國/歐洲）的定價相似，但 us-central1 在平均實例成本上略勝一籌。
- 如果您在北美以外（例如歐洲或亞洲），請切換到最近的 Tier 1 區域，如 europe-west1（比利時），以獲得更好的延遲——成本差異小於 10%。
- 避免使用 Tier 2 區域（例如 asia-southeast1），因為它們的費用高出 20-50%。

#### 適用於您的 Java 伺服器的快速設定指南
1. **建置您的應用程式**：使用 Spring Boot 建立一個簡單的 REST API。端點範例：POST `/convert`，帶有 Markdown 主體，返回 PDF。
   - 添加依賴項：`implementation 'org.xhtmlrenderer:flying-saucer-pdf:9.1.22'`（或類似）。
   - 範例程式碼片段：
     ```java:disable-run
     @RestController
     public class MarkdownController {
         @PostMapping("/convert")
         public ResponseEntity<byte[]> convert(@RequestBody String markdown) {
             // 轉換邏輯在此（例如，markdown 轉 HTML，然後轉 PDF）
             byte[] pdfBytes = // 您的轉換結果;
             return ResponseEntity.ok()
                 .header("Content-Type", "application/pdf")
                 .body(pdfBytes);
         }
     }
     ```
2. **容器化**：建立一個 `Dockerfile`：
   ```
   FROM openjdk:17-jdk-slim
   COPY target/your-app.jar app.jar
   ENTRYPOINT ["java", "-jar", "/app.jar"]
   ```
   建置：`docker build -t gcr.io/your-project/markdown-api .`
3. **部署到 Cloud Run**：
   - 在 GCP 控制台中啟用 Cloud Run API。
   - `gcloud run deploy markdown-api --image gcr.io/your-project/markdown-api --platform managed --region us-central1 --allow-unauthenticated --memory 512Mi --cpu 1 --max-instances 1`
   - 取得 URL：`https://markdown-api-abc.run.app/convert`
4. **測試**：發送一個 Markdown POST 請求；它會自動擴展。

如果是 GCP 新用戶，請註冊 $300 免費試用。在「結算」儀表板中監控成本。

[Cloud Run 定價](https://cloud.google.com/run/pricing)  
[GCP 區域指南](https://www.cloudzero.com/blog/gcp-regions/)  
[Cloud Run 快速入門](https://cloud.google.com/run/docs/quickstarts/build-and-deploy)