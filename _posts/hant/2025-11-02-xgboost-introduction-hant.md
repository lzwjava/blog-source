---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: XGBoost：入門簡介
translated: true
type: note
---

### 什麼是 XGBoost？

XGBoost，全稱為**極限梯度提升**，是一個專為監督式學習任務設計的開源機器學習函式庫，特別擅長處理結構化（表格）資料的迴歸、分類和排序問題。它採用決策樹作為基礎學習器來實現梯度提升框架，透過依序建立模型來修正前序模型的錯誤，從而達到極高的預測準確度。

#### 主要特性
- **可擴展性**：針對大型資料集進行優化，支援平行處理與分散式運算（例如透過 Dask 或 Spark）。
- **高效能**：內建正則化防止過度擬合，原生支援缺失值處理，並可自訂目標函數。
- **高效率**：透過加權分位數草圖等近似演算法加速分割點尋找，訓練速度較傳統梯度提升方法更快。
- **多功能性**：可與 Python、R、Java、Scala 等語言整合，廣泛應用於 Kaggle 競賽與產業實務。

XGBoost 自 2014 年發布並於 2016 年發表關鍵論文後聲名鵲起，因其速度與準確度的完美平衡，成為資料科學家的首選工具。

#### 創作者：陳天奇
陳天奇是機器學習與系統領域的知名研究者，他在華盛頓大學期間開發了 XGBoost。現任卡內基美隆大學機器學習與電腦科學系助理教授，並於 NVIDIA 從事人工智慧系統研究。陳天奇還共同創立了 MXNet、TVM 等專案，專注於高效能深度學習框架開發。他對 XGBoost 的研究靈感源自結合樹提升演算法變體與條件隨機場的探索。

更多詳細資訊請參閱官方文件或原始論文。

### 參考資料
- [XGBoost：可擴展的樹提升系統（arXiv 論文）](https://arxiv.org/abs/1603.02754)
- [陳天奇的個人網站](https://tqchen.com/)
- [XGBoost 演進歷程與經驗分享（陳天奇部落格）](https://tqchen.com/old_post/2016-03-10-story-and-lessons-behind-the-evolution-of-xgboost)
- [什麼是 XGBoost？（IBM 概述）](https://www.ibm.com/think/topics/xgboost)
- [XGBoost 官方文件](https://xgboost.readthedocs.io/en/stable/)