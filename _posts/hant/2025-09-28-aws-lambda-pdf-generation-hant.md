---
audio: false
generated: true
image: false
lang: hant
layout: post
model: anthropic/claude-sonnet-4
title: AWS Lambda PDF 生成方案
translated: true
type: note
---

是的，AWS Lambda（或類似的無伺服器函數）非常適合您的使用場景！這正是無伺服器計算設計的初衷——針對不頻繁、零散的工作負載，避免基礎設施閒置。

以下是 Lambda 適合用於 PDF 生成的原因：

**成本優勢：**
- 僅在函數執行時付費（按請求次數 + 執行時間計算）
- 閒置時無需付費——對您每日 1-2 次的使用頻率至關重要
- Lambda 免費方案包含每月 100 萬次請求和 400,000 GB-秒
- 對於數百名用戶且 PDF 使用量低的情況，很可能完全適用免費方案

**技術實現方式：**
```
部落格 → API Gateway → Lambda 函數 → PDF 生成 → S3 儲存 → 返回 URL
```

**架構選項：**

1. **簡易 Lambda + Puppeteer/Playwright：**
   - 透過含無頭瀏覽器的 Lambda 函數將 HTML 轉換為 PDF
   - 適合含樣式的部落格內容
   - 冷啟動約 2-3 秒，但對您的使用頻率可接受

2. **Lambda + PDF 程式庫：**
   - 使用 jsPDF、PDFKit 或 wkhtmltopdf 等程式庫
   - 執行速度更快，套件體積更小
   - 更適合文字密集型內容

3. **混合方案：**
   - Lambda 生成 PDF 並儲存至 S3
   - 透過 CloudFront 分發 PDF
   - 可選：如需非同步處理可加入 SQS

**其他無伺服器方案：**
- **Vercel Functions**——若您的部落格部署在 Vercel
- **Netlify Functions**——類似概念
- **Google Cloud Functions**——價格相近
- **Railway/Render**——無伺服器容器方案

就您的規模（數百名用戶，每日 1-2 次 PDF 請求）而言，使用 Lambda 幾乎無需成本，同時能完全免除伺服器維護工作。這遠比為了偶爾的 PDF 生成而持續運行伺服器要划算得多。

需要我詳細說明任何具體的實作方案嗎？