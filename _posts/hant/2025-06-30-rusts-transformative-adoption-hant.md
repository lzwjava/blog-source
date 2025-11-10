---
audio: false
generated: true
lang: hant
layout: post
title: Rust對Cloudflare的影響
translated: true
type: note
---

Cloudflare 採用 Rust 的轉型之路，是由其獨特融合的效能、安全性與擴展性所驅動。以下詳細解析 Cloudflare 選擇 Rust 的原因及其帶來的具體成果：

---

### **為何 Cloudflare 使用 Rust**
1. **記憶體安全且不犧牲效能**  
   - Rust 的所有權模型消除了 C/C++ 程式碼中常見的整類漏洞（例如緩衝區溢位、釋放後使用錯誤），這對 Cloudflare 安全至上的基礎架構至關重要。  
   - 與垃圾回收語言不同，Rust 在實現此目標的同時無需運行時開銷，使其成為代理伺服器和邊緣運算等高效能系統的理想選擇。

2. **並行處理與擴展能力**  
   - Rust 的非同步運行時（Tokio）能有效處理數百萬個並行連線，表現優於 NGINX 的每請求單線程模型。例如，Cloudflare 基於 Rust 的代理伺服器 Pingora 每秒處理 **超過 3500 萬次請求**，且 CPU/記憶體使用率更低。  
   - Workers 中的非同步支援（透過 `wasm-bindgen-futures`）讓基於 Rust 的 Workers 能無縫處理 I/O 密集型任務。

3. **效能提升**  
   - Cloudflare 採用 Rust 的 QUIC/HTTP/3 堆疊比其 C++ 前身快 **30%**，記憶體使用量降低 **35%**，在相同硬體上吞吐量提升 **50%**。  
   - Rust 中的微觀優化（例如將每個請求的延遲降低微秒級）在 Cloudflare 的規模下節省了數千美元的運算成本。

4. **開發者生產力**  
   - Rust 的強型別系統和現代化工具（例如 Cargo）簡化了維護工作並減少錯誤。例如，Cloudflare 的代理框架 Oxy 讓功能豐富的應用程式能以 **少於 200 行程式碼** 建構完成。  
   - Workers 的 Rust SDK（`workers-rs`）為 KV、Durable Objects 和 AI 提供了符合人體工學的 API，實現快速開發。

5. **生態系統與未來適應性**  
   - Rust 日益增長的採用率（例如 AWS Lambda、Discord）與 Cloudflare 的長期願景一致。開源專案如 Pingora 和 Oxy 促進了社群協作。  

---

### **使用 Rust 的成果**
- **Pingora**：取代了 NGINX，每月處理數兆次請求，具備 **更低延遲** 和 **更強的 DDoS 韌性**。  
- **Workers**：Rust 支援讓運算密集型任務（例如 AI 推論）能以接近原生的速度執行，吸引了金融科技和配送平台等高端客戶。  
- **可靠性**：Rust 的安全特性減少了關鍵服務（如 QUIC 和 TLS）中的崩潰情況（例如 Oxy 中的 BoringSSL 整合）。  
- **成本節省**：Pingora 的優化在全球節省了 **超過 500 個 CPU**，轉化為顯著的營運節省。  

---

### **挑戰與應對措施**
- **學習曲線**：Rust 的複雜性需要前期培訓，但 Cloudflare 透過內部函式庫（例如 `workers-rs`）和模板緩解了此問題。  
- **Wasm 限制**：早期的 Workers Rust 支援有大小限制，但現在透過 `wasm-opt` 和 `worker-build` 等工具能有效優化二進位檔案。  

---

### **未來方向**
Cloudflare 持續擴展 Rust 的應用範圍，包括：  
- **容器**：基於 Rust 的 Durable Objects 為新的容器編排提供動力（預計 2025 年 6 月推出）。  
- **AI**：Workers AI 利用 Rust 實現低延遲模型推論。  

總而言之，Rust 已成為 Cloudflare 基礎架構的基石，在降低成本的同時提供了 **安全性、效能與擴展性**。其採用標誌著業界在關鍵系統中朝向記憶體安全語言的廣泛轉變。