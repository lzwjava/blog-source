---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Présentation des modèles MiniMax M1 et M2
translated: true
type: note
---

### MiniMax M1 et M2 : Contributeurs majeurs, auteurs des articles et responsable technique

MiniMax M1 et M2 sont des modèles d'IA avancés développés par MiniMax AI, une startup chinoise d'IA spécialisée dans les grands modèles de langage (LLM) et l'IA multimodale. Les deux modèles font partie de leurs versions à poids ouvert, M1 mettant l'accent sur le raisonnement en contexte long (jusqu'à 1 million de tokens) et une efficacité de calcul au moment du test, tandis que M2 cible le codage, les workflows agentiques et le support multi-agents. Le développement est un effort collaboratif de l'équipe MiniMax, mais les attributions spécifiques sont limitées dans les communications publiques.

#### Contributeurs majeurs
- **Équipe principale** : Les modèles sont construits par une large équipe d'ingénierie et de recherche chez MiniMax AI. Pour M1, l'entraînement a impliqué l'apprentissage par renforcement (RL) sur des tâches diverses comme l'ingénierie logicielle et l'utilisation d'outils, réalisé efficacement sur 512 GPU H800 en seulement trois semaines. M2 s'appuie sur des architectures hybrides similaires mais optimise l'efficacité des agents.
- Aucun "contributeur majeur" individuel n'est mis en avant au-delà de l'équipe collective, les crédits étant attribués à l'équipe. Les collaborations externes incluent l'équipe SGLang pour le support du déploiement de M2.

#### Auteurs des articles
- **MiniMax-M1** : Décrit dans le rapport technique *"MiniMax-M1: Scaling Test-Time Compute Efficiently with Lightning Attention"* (arXiv:2506.13585). Les auteurs sont listés par ordre alphabétique (plus de 50 au total, tous affiliés à MiniMax) :
  - Aili Chen, Aonian Li, Bangwei Gong, Binyang Jiang, Bo Fei, Bo Yang, Boji Shan, Changqing Yu, Chao Wang, Cheng Zhu, Chengjun Xiao, Chengyu Du, Chi Zhang, Chu Qiao, Chunhao Zhang, Chunhui Du, Congchao Guo, Da Chen, Deming Ding, Dianjun Sun, Dong Li, Enwei Jiao, Haigang Zhou, Haimo Zhang, Han Ding, Haohai Sun, Haoyu Feng, Huaiguang Cai, Haichao Zhu, Jian Sun, Jiaqi Zhuang, Jiaren Cai, Jiayuan Song, Jin Zhu, Jingyang Li, Jinhao Tian, Jinli Liu, Junhao Xu, Junjie Yan, Junteng Liu, Junxian He, Kaiyi Feng, Ke Yang, Kecheng Xiao, Le Han, Leyang Wang, Lianfei Yu, Liheng Feng, Lin Li, Lin Zheng, Linge Du, Lingyu Yang, Lunbin Zeng, Minghui Yu, Mingliang Tao, Mingyuan Chi, Mozhi Zhang, Mujie Lin, Nan Hu, Nongyu Di, Peng Gao, Pengfei Li, Pengyu Zhao, Qibing Ren, Qidi Xu, Qile Li, Qin Wang, Rong Tian, Ruitao Leng, Shaoxiang Chen, Shaoyu Chen, Shengmin Shi, Shitong Weng, Shuchang Guan, Shuqi Yu, Sichen Li, Songquan Zhu, Tengfei Li, Tianchi Cai, Tianrun Liang, Weiyu Cheng, Weize Kong, Wenkai Li, Xiancai Chen, Xiangjun Song, Xiao Luo, Xiao Su, Xiaobo Li, Xiaodong Han, Xinzhu Hou, Xuan Lu, Xun Zou, Xuyang Shen, Yan Gong, Yan Ma, Yang Wang, Yiqi Shi, Yiran Zhong, Yonghong Duan (et 27 auteurs supplémentaires).
  - Note : Junjie Yan (PDG) figure parmi les auteurs.
- **MiniMax-M2** : Aucun article académique dédié ou liste d'auteurs trouvé dans les sources publiques. Il est publié via Hugging Face avec des crédits d'équipe à MiniMax AI dans son ensemble, faisant référence à des innovations internes mais sans individus nommés.

#### Responsable technique
- **Yan Junjie** : Fondateur et PDG de MiniMax AI (établie en 2021). Il supervise l'orientation technique, y compris le développement des modèles M1 et M2. Ancien cadre de SenseTime, Yan a donné des keynotes sur ces modèles (par exemple, au WAIC 2025) et est crédité dans la liste des auteurs de M1. Il est le principal visage public des avancées en IA de l'entreprise.

L'approche de MiniMax met l'accent sur une IA efficace et évolutive pour des applications étendues, M1 et M2 représentant des itérations rapides dans les modèles de raisonnement open source.

#### Références
- [Article arXiv MiniMax-M1](https://arxiv.org/abs/2506.13585)
- [GitHub MiniMax-M1](https://github.com/MiniMax-AI/MiniMax-M1)
- [Hugging Face MiniMax-M2](https://huggingface.co/MiniMaxAI/MiniMax-M2)
- [Profil de Yan Junjie (SCMP)](https://www.scmp.com/topics/yan-junjie)
- [Crunchbase MiniMax](https://www.crunchbase.com/organization/minimax-a48a)