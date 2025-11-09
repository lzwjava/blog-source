---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: MiniMax M1およびM2モデルの概要
translated: true
type: note
---

### MiniMax M1とM2：主要貢献者、論文著者、テクニカルリード

MiniMax M1とM2は、中国のAIスタートアップであるMiniMax AIによって開発された先進的なAIモデルです。同社は大規模言語モデル(LLM)とマルチモーダルAIに焦点を当てています。両モデルはオープンウェイトで公開されており、M1は長文脈推論（最大100万トークン）と効率的なテストタイムコンピュートを重視し、M2はコーディング、エージェントワークフロー、マルチエージェントサポートを標的としています。開発はMiniMaxチームの共同作業によるものですが、公開情報における特定の帰属情報は限られています。

#### 主要貢献者
- **コアチーム**: モデルはMiniMax AIの大規模なエンジニアリングおよび研究チームによって構築されました。M1の場合、ソフトウェアエンジニアリングやツール使用など多様なタスクに対する強化学習(RL)を用いたトレーニングが、512台のH800 GPU上でわずか3週間で効率的に完了しました。M2は同様のハイブリッドアーキテクチャを基盤としつつ、エージェント効率のために最適化されています。
- クレジットはチームベースであるため、「主要貢献者」として特定の個人が挙げられることはありません。外部コラボレーションとしては、M2のデプロイメントサポートにSGLangチームが含まれます。

#### 論文著者
- **MiniMax-M1**: 技術報告書 *"MiniMax-M1: Scaling Test-Time Compute Efficiently with Lightning Attention"* (arXiv:2506.13585) に詳細が記載されています。著者はアルファベット順にリストされています（合計50名以上、全員がMiniMax所属）。
  - Aili Chen, Aonian Li, Bangwei Gong, Binyang Jiang, Bo Fei, Bo Yang, Boji Shan, Changqing Yu, Chao Wang, Cheng Zhu, Chengjun Xiao, Chengyu Du, Chi Zhang, Chu Qiao, Chunhao Zhang, Chunhui Du, Congchao Guo, Da Chen, Deming Ding, Dianjun Sun, Dong Li, Enwei Jiao, Haigang Zhou, Haimo Zhang, Han Ding, Haohai Sun, Haoyu Feng, Huaiguang Cai, Haichao Zhu, Jian Sun, Jiaqi Zhuang, Jiaren Cai, Jiayuan Song, Jin Zhu, Jingyang Li, Jinhao Tian, Jinli Liu, Junhao Xu, Junjie Yan, Junteng Liu, Junxian He, Kaiyi Feng, Ke Yang, Kecheng Xiao, Le Han, Leyang Wang, Lianfei Yu, Liheng Feng, Lin Li, Lin Zheng, Linge Du, Lingyu Yang, Lunbin Zeng, Minghui Yu, Mingliang Tao, Mingyuan Chi, Mozhi Zhang, Mujie Lin, Nan Hu, Nongyu Di, Peng Gao, Pengfei Li, Pengyu Zhao, Qibing Ren, Qidi Xu, Qile Li, Qin Wang, Rong Tian, Ruitao Leng, Shaoxiang Chen, Shaoyu Chen, Shengmin Shi, Shitong Weng, Shuchang Guan, Shuqi Yu, Sichen Li, Songquan Zhu, Tengfei Li, Tianchi Cai, Tianrun Liang, Weiyu Cheng, Weize Kong, Wenkai Li, Xiancai Chen, Xiangjun Song, Xiao Luo, Xiao Su, Xiaobo Li, Xiaodong Han, Xinzhu Hou, Xuan Lu, Xun Zou, Xuyang Shen, Yan Gong, Yan Ma, Yang Wang, Yiqi Shi, Yiran Zhong, Yonghong Duan (および追加27名の著者)。
  - 注: Junjie Yan (CEO) も著者の一人です。
- **MiniMax-M2**: 公開情報において、専用の学術論文や著者リストは見つかりませんでした。Hugging Faceを通じて公開されており、クレジットはMiniMax AI全体に帰属し、内部的な革新には言及しているものの、個人名は挙げられていません。

#### テクニカルリード
- **Yan Junjie**: MiniMax AIの創業者兼CEO（2021年設立）。M1とM2を含むモデル開発の技術方向性を統括しています。元SenseTime幹部であり、これらのモデルについて（例: WAIC 2025での基調講演など）講演を行い、M1の著者リストにも名を連ねています。同社のAI進歩における主要な広報担当者です。

MiniMaxのアプローチは、効率的でスケーラブルなAIを広範なアプリケーション向けに提供することを重視しており、M1とM2はオープンソース推論モデルにおける迅速な反復を代表しています。

#### 参考文献
- [MiniMax-M1 arXiv Paper](https://arxiv.org/abs/2506.13585)
- [MiniMax-M1 GitHub](https://github.com/MiniMax-AI/MiniMax-M1)
- [MiniMax-M2 Hugging Face](https://huggingface.co/MiniMaxAI/MiniMax-M2)
- [Yan Junjie Profile (SCMP)](https://www.scmp.com/topics/yan-junjie)
- [MiniMax Crunchbase](https://www.crunchbase.com/organization/minimax-a48a)