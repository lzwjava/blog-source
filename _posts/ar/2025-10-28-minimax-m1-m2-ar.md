---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: نظرة عامة على نموذجي مينيماكس إم 1 وإم 2
translated: true
type: note
---

### MiniMax M1 و M2: المساهمون الرئيسيون، مؤلفو الأوراق البحثية، والقيادة التقنية

MiniMax M1 و M2 هما نموذجان متقدمان للذكاء الاصطناعي طورتهما شركة MiniMax AI الناشئة في الصين، والتي تركز على النماذج اللغوية الكبيرة (LLMs) والذكاء الاصطناعي متعدد الوسائط. كلا النموذجين جزء من إصداراتهما مفتوحة الوزن، حيث يركز M1 على الاستدلال طويل السياق (حتى 1 مليون رمز) وكفاءة الحوسبة في وقت الاختبار، بينما يستهدف M2 البرمجة، سير عمل الوكيل الآلي، ودعم الوكيل الآلي المتعدد. التطوير هو جهد تعاوني من فريق MiniMax، ولكن الإسنادات المحدودة محدودة في الإصدارات العامة.

#### المساهمون الرئيسيون
- **الفريق الأساسي**: تم بناء النماذج من قبل فريق كبير من المهندسين والباحثين في MiniMax AI. بالنسبة لـ M1، اشتمل التدريب على التعلم المعزز (RL) على مهام متنوعة مثل هندسة البرمجيات واستخدام الأدوات، وتم إكماله بكفاءة على 512 من وحدات معالجة الرسومات H800 في ثلاثة أسابيع فقط. بينما يُبنى M2 على هياكل هجينة مماثلة ولكنه يحسن كفاءة الوكيل الآلي.
- لم يتم تسليط الضوء على "مساهمين رئيسيين" أفراد خارج الفريق الجماعي، حيث أن الفضل يعود للفريق. تشمل التعاونات الخارجية فريق SGLang لدعم نشر M2.

#### مؤلفو الأوراق البحثية
- **MiniMax-M1**: تم تفصيله في التقرير التقني *"MiniMax-M1: Scaling Test-Time Compute Efficiently with Lightning Attention"* (arXiv:2506.13585). تم سرد المؤلفين أبجديًا (أكثر من 50 إجمالاً، جميعهم منتسبون إلى MiniMax):
  - Aili Chen, Aonian Li, Bangwei Gong, Binyang Jiang, Bo Fei, Bo Yang, Boji Shan, Changqing Yu, Chao Wang, Cheng Zhu, Chengjun Xiao, Chengyu Du, Chi Zhang, Chu Qiao, Chunhao Zhang, Chunhui Du, Congchao Guo, Da Chen, Deming Ding, Dianjun Sun, Dong Li, Enwei Jiao, Haigang Zhou, Haimo Zhang, Han Ding, Haohai Sun, Haoyu Feng, Huaiguang Cai, Haichao Zhu, Jian Sun, Jiaqi Zhuang, Jiaren Cai, Jiayuan Song, Jin Zhu, Jingyang Li, Jinhao Tian, Jinli Liu, Junhao Xu, Junjie Yan, Junteng Liu, Junxian He, Kaiyi Feng, Ke Yang, Kecheng Xiao, Le Han, Leyang Wang, Lianfei Yu, Liheng Feng, Lin Li, Lin Zheng, Linge Du, Lingyu Yang, Lunbin Zeng, Minghui Yu, Mingliang Tao, Mingyuan Chi, Mozhi Zhang, Mujie Lin, Nan Hu, Nongyu Di, Peng Gao, Pengfei Li, Pengyu Zhao, Qibing Ren, Qidi Xu, Qile Li, Qin Wang, Rong Tian, Ruitao Leng, Shaoxiang Chen, Shaoyu Chen, Shengmin Shi, Shitong Weng, Shuchang Guan, Shuqi Yu, Sichen Li, Songquan Zhu, Tengfei Li, Tianchi Cai, Tianrun Liang, Weiyu Cheng, Weize Kong, Wenkai Li, Xiancai Chen, Xiangjun Song, Xiao Luo, Xiao Su, Xiaobo Li, Xiaodong Han, Xinzhu Hou, Xuan Lu, Xun Zou, Xuyang Shen, Yan Gong, Yan Ma, Yang Wang, Yiqi Shi, Yiran Zhong, Yonghong Duan (و 27 مؤلفًا إضافيًا).
  - ملاحظة: Junjie Yan (الرئيس التنفيذي) من بين المؤلفين.
- **MiniMax-M2**: لم يتم العثور على ورقة أكاديمية مخصصة أو قائمة مؤلفين في المصادر العامة. تم إصداره عبر Hugging Face مع إسناد الفضل للفريق بشكل عام لـ MiniMax AI، مع الإشارة إلى الابتكارات الداخلية ولكن بدون أسماء أفراد.

#### القيادة التقنية
- **Yan Junjie**: المؤسس والرئيس التنفيذي لشركة MiniMax AI (تأسست في 2021). يشرف على الاتجاه التقني، بما في ذلك تطوير النماذج لـ M1 و M2. كونه تنفيذيًا سابقًا في SenseTime، قدم Yan كلمات رئيسية حول هذه النماذج (على سبيل المثال، في WAIC 2025) وتم إدراجه في قائمة مؤلفي M1. وهو الوجه العام الرئيسي لتقدم الشركة في مجال الذكاء الاصطناعي.

يركز نهج MiniMax على الذكاء الاصطناعي الكفؤ والقابل للتطوير للتطبيقات الواسعة، حيث يمثل M1 و M2 تكرارات سريعة في نماذج الاستدلال مفتوحة المصدر.

#### المراجع
- [ورقة MiniMax-M1 على arXiv](https://arxiv.org/abs/2506.13585)
- [MiniMax-M1 على GitHub](https://github.com/MiniMax-AI/MiniMax-M1)
- [MiniMax-M2 على Hugging Face](https://huggingface.co/MiniMaxAI/MiniMax-M2)
- [ملف Yan Junjie الشخصي (SCMP)](https://www.scmp.com/topics/yan-junjie)
- [MiniMax على Crunchbase](https://www.crunchbase.com/organization/minimax-a48a)