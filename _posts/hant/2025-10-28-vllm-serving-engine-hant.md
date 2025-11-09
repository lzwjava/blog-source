---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: vLLM：高效大型語言模型服務引擎
translated: true
type: note
---

### vLLM 的誕生

vLLM（全稱為「virtual LLM」）是一個專為大語言模型設計的高吞吐量、記憶體高效能推理與服務開源函式庫。它由加州大學柏克萊分校 RISELab 的 Sky Computing Lab 研究人員於 2023 年初發明。該專案最初是專為 NVIDIA A100 GPU 和有限模型集優化的專用推理引擎，旨在解決 LLM 服務中的關鍵挑戰，如記憶體碎片化和低吞吐量。

早期重要里程碑：
- **2023 年 4 月中旬**：首次與 FastChat 公開整合，為 LMSYS 的 Vicuna 和 Chatbot Arena 演示提供技術支援。
- **2023 年 6 月**：正式發布並公開 GitHub 儲存庫。
- **2023 年 9 月 12 日**：基礎研究論文《Efficient Memory Management for Large Language Model Serving with PagedAttention》於 arXiv 發表，引入了核心的 PagedAttention 機制，實現了連續批次處理和近乎零的 KV 快取浪費。

GitHub 儲存庫 (vllm-project/vllm) 約在 2023 年 5 月至 6 月期間創建，與初期開發推進時間相符。

### 知名度攀升

vLLM 於 2024 年開始獲得顯著關注，從一個小眾研究工具演變為開源 LLM 服務的事實標準。其知名度因快速的功能增進（如量化、推測解碼、多模態支援）、硬體擴展（NVIDIA、AMD、Google TPU 等）以及企業生產環境採用（如 Amazon 在 2024 年 Prime Day 期間支援 Rufus、LinkedIn 等）而爆增。

2024 年關鍵成長指標：
- **GitHub 星標數**：從 14,000（2024 年初）增長 2.3 倍至 32,600（2024 年底）。
- **月下載量**：從 6,000 飆升 4.5 倍至 27,000。
- **GPU 使用量**：在 2024 年下半年增長約 10 倍。
- **社群**：貢獻者數量增長 3.9 倍至 740 人，並設立雙週辦公室時間及建立合作夥伴關係（如 NVIDIA、IBM、AWS）。

截至 2024 年中，vLLM 已獲得約 20,000 顆星標，並因在吞吐量方面優於替代方案而頻繁在 AI 社群中被討論。這股動能持續至 2025 年：
- 2024 年 12 月加入 PyTorch 生態系統。
- 2024 年 10 月進入 LF AI & Data 孵化階段。
- 2025 年 6 月達到 50,000 顆星標。

時至今日（2025 年 10 月），vLLM 已擁有超過 55,000 顆星標並支援近 100 種模型架構，成為可擴展 AI 部署的基石技術。

[arXiv 上關於 PagedAttention 的論文](https://arxiv.org/abs/2309.06180)  
[vLLM GitHub 儲存庫](https://github.com/vllm-project/vllm)  
[vLLM 2024 回顧部落格](https://blog.vllm.ai/2025/01/10/vllm-2024-wrapped-2025-vision.html)  
[PyTorch 整合公告](https://pytorch.org/blog/vllm-joins-pytorch/)