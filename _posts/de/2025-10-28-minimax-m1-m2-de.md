---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: MiniMax M1- und M2-Modellübersicht
translated: true
type: note
---

### MiniMax M1 und M2: Wichtige Mitwirkende, Autoren der Veröffentlichung und Technische Leitung

MiniMax M1 und M2 sind fortschrittliche KI-Modelle, die von MiniMax AI entwickelt wurden, einem chinesischen KI-Startup, das sich auf Large Language Models (LLMs) und multimodale KI konzentriert. Beide Modelle sind Teil ihrer Open-Weight-Veröffentlichungen, wobei M1 den Schwerpunkt auf Langkontext-Verarbeitung (bis zu 1 Million Tokens) und effiziente Test-Time-Compute legt, während M2 auf Coding, agentenbasierte Workflows und Multi-Agenten-Unterstützung abzielt. Die Entwicklung ist eine gemeinsame Anstrengung des MiniMax-Teams, jedoch sind spezifische Zuschreibungen in öffentlichen Veröffentlichungen begrenzt.

#### Wichtige Mitwirkende
- **Kernteam**: Die Modelle wurden von einem großen Team aus Ingenieuren und Forschern bei MiniMax AI entwickelt. Für M1 beinhaltete das Training Reinforcement Learning (RL) für verschiedene Aufgaben wie Softwareentwicklung und Tool Use, das effizient auf 512 H800 GPUs in nur drei Wochen abgeschlossen wurde. M2 baut auf ähnlichen Hybrid-Architekturen auf, optimiert jedoch für Agent-Effizienz.
- Es werden keine einzelnen "wichtigen Mitwirkenden" über das Kollektiv des Teams hinaus hervorgehoben, da die Anerkennung teambezogen ist. Externe Zusammenarbeiten umfassen das SGLang-Team für den M2-Implementierungssupport.

#### Autoren der Veröffentlichung
- **MiniMax-M1**: Detailliert im technischen Bericht *"MiniMax-M1: Scaling Test-Time Compute Efficiently with Lightning Attention"* (arXiv:2506.13585). Die Autoren sind alphabetisch aufgelistet (über 50 insgesamt, alle mit MiniMax verbunden):
  - Aili Chen, Aonian Li, Bangwei Gong, Binyang Jiang, Bo Fei, Bo Yang, Boji Shan, Changqing Yu, Chao Wang, Cheng Zhu, Chengjun Xiao, Chengyu Du, Chi Zhang, Chu Qiao, Chunhao Zhang, Chunhui Du, Congchao Guo, Da Chen, Deming Ding, Dianjun Sun, Dong Li, Enwei Jiao, Haigang Zhou, Haimo Zhang, Han Ding, Haohai Sun, Haoyu Feng, Huaiguang Cai, Haichao Zhu, Jian Sun, Jiaqi Zhuang, Jiaren Cai, Jiayuan Song, Jin Zhu, Jingyang Li, Jinhao Tian, Jinli Liu, Junhao Xu, Junjie Yan, Junxian He, Junteng Liu, Kaiyi Feng, Ke Yang, Kecheng Xiao, Le Han, Leyang Wang, Lianfei Yu, Liheng Feng, Lin Li, Lin Zheng, Linge Du, Lingyu Yang, Lunbin Zeng, Minghui Yu, Mingliang Tao, Mingyuan Chi, Mozhi Zhang, Mujie Lin, Nan Hu, Nongyu Di, Peng Gao, Pengfei Li, Pengyu Zhao, Qibing Ren, Qidi Xu, Qile Li, Qin Wang, Rong Tian, Ruitao Leng, Shaoxiang Chen, Shaoyu Chen, Shengmin Shi, Shitong Weng, Shuchang Guan, Shuqi Yu, Sichen Li, Songquan Zhu, Tengfei Li, Tianchi Cai, Tianrun Liang, Weiyu Cheng, Weize Kong, Wenkai Li, Xiancai Chen, Xiangjun Song, Xiao Luo, Xiao Su, Xiaobo Li, Xiaodong Han, Xinzhu Hou, Xuan Lu, Xun Zou, Xuyang Shen, Yan Gong, Yan Ma, Yang Wang, Yiqi Shi, Yiran Zhong, Yonghong Duan (und 27 weitere Autoren).
  - Hinweis: Junjie Yan (CEO) ist unter den Autoren.
- **MiniMax-M2**: In öffentlichen Quellen wurde keine eigene akademische Veröffentlichung oder Autorenliste gefunden. Es wurde über Hugging Face veröffentlicht, wobei die Team-Anerkennung allgemein MiniMax AI gilt und auf interne Innovationen verweist, jedoch ohne Nennung einzelner Personen.

#### Technische Leitung
- **Yan Junjie**: Gründer und CEO von MiniMax AI (gegründet 2021). Er verantwortet die technische Ausrichtung, einschließlich der Modellentwicklung für M1 und M2. Ein ehemaliger SenseTime-Manager, Yan hat Keynotes zu diesen Modellen gehalten (z.B. auf der WAIC 2025) und ist in der Autorenliste von M1 aufgeführt. Er ist das primäre öffentliche Gesicht für die KI-Fortschritte des Unternehmens.

MiniMax' Ansatz betont effiziente, skalierbare KI für breite Anwendungen, wobei M1 und M2 schnelle Iterationen in Open-Source-Reasoning-Modellen darstellen.

#### Referenzen
- [MiniMax-M1 arXiv Paper](https://arxiv.org/abs/2506.13585)
- [MiniMax-M1 GitHub](https://github.com/MiniMax-AI/MiniMax-M1)
- [MiniMax-M2 Hugging Face](https://huggingface.co/MiniMaxAI/MiniMax-M2)
- [Yan Junjie Profile (SCMP)](https://www.scmp.com/topics/yan-junjie)
- [MiniMax Crunchbase](https://www.crunchbase.com/organization/minimax-a48a)