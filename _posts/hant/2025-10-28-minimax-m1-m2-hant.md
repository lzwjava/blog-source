---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: MiniMax M1 及 M2 型號概覽
translated: true
type: note
---

### MiniMax M1 與 M2：主要貢獻者、論文作者與技術負責人

MiniMax M1 和 M2 是由中國人工智能初創公司 MiniMax AI 開發的先進 AI 模型，該公司專注於大型語言模型（LLMs）和多模態 AI。這兩款模型均屬於其開放權重發佈系列，其中 M1 強調長上下文推理（高達 100 萬個 token）和高效的測試時計算，而 M2 則專注於編程、智能體工作流程以及多智能體支援。此開發項目是 MiniMax 團隊協作努力的成果，但公開發佈的具體歸屬資訊有限。

#### 主要貢獻者
- **核心團隊**：模型由 MiniMax AI 的大型工程與研究團隊構建。M1 的訓練涉及對軟件工程和工具使用等多樣任務的強化學習（RL），僅在 512 個 H800 GPU 上高效完成，歷時三週。M2 基於類似的混合架構，但針對智能體效率進行了優化。
- 除了團隊集體貢獻外，並未特別指明個別「主要貢獻者」，因為功勞歸屬於團隊整體。外部合作包括 SGLang 團隊為 M2 提供的部署支援。

#### 論文作者
- **MiniMax-M1**：詳細技術報告見 *"MiniMax-M1: Scaling Test-Time Compute Efficiently with Lightning Attention"* (arXiv:2506.13585)。作者按字母順序列出（總計超過 50 位，均隸屬於 MiniMax）：
  - Aili Chen, Aonian Li, Bangwei Gong, Binyang Jiang, Bo Fei, Bo Yang, Boji Shan, Changqing Yu, Chao Wang, Cheng Zhu, Chengjun Xiao, Chengyu Du, Chi Zhang, Chu Qiao, Chunhao Zhang, Chunhui Du, Congchao Guo, Da Chen, Deming Ding, Dianjun Sun, Dong Li, Enwei Jiao, Haigang Zhou, Haimo Zhang, Han Ding, Haohai Sun, Haoyu Feng, Huaiguang Cai, Haichao Zhu, Jian Sun, Jiaqi Zhuang, Jiaren Cai, Jiayuan Song, Jin Zhu, Jingyang Li, Jinhao Tian, Jinli Liu, Junhao Xu, Junjie Yan, Junteng Liu, Junxian He, Kaiyi Feng, Ke Yang, Kecheng Xiao, Le Han, Leyang Wang, Lianfei Yu, Liheng Feng, Lin Li, Lin Zheng, Linge Du, Lingyu Yang, Lunbin Zeng, Minghui Yu, Mingliang Tao, Mingyuan Chi, Mozhi Zhang, Mujie Lin, Nan Hu, Nongyu Di, Peng Gao, Pengfei Li, Pengyu Zhao, Qibing Ren, Qidi Xu, Qile Li, Qin Wang, Rong Tian, Ruitao Leng, Shaoxiang Chen, Shaoyu Chen, Shengmin Shi, Shitong Weng, Shuchang Guan, Shuqi Yu, Sichen Li, Songquan Zhu, Tengfei Li, Tianchi Cai, Tianrun Liang, Weiyu Cheng, Weize Kong, Wenkai Li, Xiancai Chen, Xiangjun Song, Xiao Luo, Xiao Su, Xiaobo Li, Xiaodong Han, Xinzhu Hou, Xuan Lu, Xun Zou, Xuyang Shen, Yan Gong, Yan Ma, Yang Wang, Yiqi Shi, Yiran Zhong, Yonghong Duan（以及另外 27 位作者）。
  - 註：閆俊杰（CEO）亦在作者之列。
- **MiniMax-M2**：公開來源中未找到專門的學術論文或作者列表。該模型通過 Hugging Face 發佈，團隊功勞歸屬於 MiniMax AI 整體，提及內部創新但未列出具體個人姓名。

#### 技術負責人
- **閆俊杰**：MiniMax AI 的創始人兼 CEO（公司成立於 2021 年）。他負責監督技術方向，包括 M1 和 M2 的模型開發。作為前商湯科技高管，閆俊杰曾就這些模型發表主題演講（例如在 2025 年世界人工智能大會上），並在 M1 的作者名單中獲得認可。他是公司 AI 進展的主要公開代表。

MiniMax 的方法強調高效、可擴展的 AI 以實現廣泛應用，M1 和 M2 代表了開源推理模型的快速迭代。

#### 參考資料
- [MiniMax-M1 arXiv 論文](https://arxiv.org/abs/2506.13585)
- [MiniMax-M1 GitHub](https://github.com/MiniMax-AI/MiniMax-M1)
- [MiniMax-M2 Hugging Face](https://huggingface.co/MiniMaxAI/MiniMax-M2)
- [閆俊杰簡介 (SCMP)](https://www.scmp.com/topics/yan-junjie)
- [MiniMax Crunchbase](https://www.crunchbase.com/organization/minimax-a48a)