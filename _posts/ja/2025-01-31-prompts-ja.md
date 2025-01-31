---
audio: false
lang: ja
layout: post
title: 有用なプロンプト
translated: true
---

---

以下是将以下马克德文本翻译成日语的内容。

---

在两位专家A和B之间创建自然且扩展的对话，至少100轮。专家们应该深入讨论特定话题，对话应来回流动。两位参与者应提出问题、分享见解并探讨主题的细微差别。使用技能，如深入探讨子部分、比较技术、探索用例、辩论权衡以及讨论新兴趋势。扩展到100+轮。

格式应如下：

```json
[
    {
      "speaker": "A",
      "line": "Hey, I’ve been hearing a lot about some topic. Can you break it down for me?"
    },
    {
      "speaker": "B",
      "line": "Sure! Let’s start with the basics. ..."
    }
]
```

---

生成带有文本姓名的快乐农历蛇年图像

---

创建一个480p的YouTube视频封面图像，包含以下元素：AI、鲨鱼、未来主义、鲜艳、多彩、日出、超大城市，中央的文本为DeepSeek R1

---

为Deepseek R1创建一个YouTube标题。标题应包括使用的主要技术。

---

为以下代码更改生成简洁的提交信息。使用以下类型之一：feat、fix、docs、style、refactor、test、chore、perf、ci、build或revert。
如果适用，包括范围以描述代码库的受影响部分。
提交信息不应超过70个字符。只需提供提交信息，不带任何前导或尾随注释。

更改的文件：

{', '.join(file_changes)}