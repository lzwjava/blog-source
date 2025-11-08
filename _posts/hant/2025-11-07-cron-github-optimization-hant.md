---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 優化 Cron 與 GitHub 工作流程效率
translated: true
type: note
---

這確實是個很棒的優化！將你的 cron 排程改為 `'0 */2 * * *'`（每 2 小時執行一次），在保持內容新鮮度與控制執行時間之間取得了良好平衡——特別是對於持續累積的 AI 生成筆記，既能避免讓筆記數量暴增到每年 3000+ 篇，又能確保遠低於 GitHub 免費帳戶的 2000 分鐘月度限制。透過註解掉 `original/**` 和 `_posts/**` 這類路徑（同時保留核心路徑如 `_layouts/**`、`_includes/**` 等），可確保工作流程僅在有意義的變更時觸發，減少不必要的執行次數。

若你的儲存庫涉及 Jekyll 網站或類似架構（從 `_config.yml` 和 `_sass/**` 路徑可看出），此設定應能保持部署流程簡潔高效。這裡有幾個小技巧可進一步節省執行時間：
- **在工作流程 YAML 中加入 `concurrency` 區塊**，當新執行開始時可取消正在進行的任務（例如處理排程與推送事件重疊的情況）：
  ```yaml
  concurrency:
    group: ${{ github.workflow }}-${{ github.ref }}
    cancel-in-progress: true
  ```
- **透過 GitHub 設定 > 帳單 > 使用量 監控執行時間**——可設置簡單腳本或警示機制，當使用量接近 1500 分鐘時及時發現異常峰值。
- 若筆記累積是主要觸發因素，可考慮在排程觸發器中加入 `if` 條件，針對 AI 相關路徑（例如 `scripts/llm/**`）的近期提交進行過濾。

總體而言，這是個非常高效的調整——既優化了資源使用，又保留了 AI 生成內容的價值。如果你願意分享完整的工作流程檔案，或需要進一步調整的協助，我隨時提供支援！