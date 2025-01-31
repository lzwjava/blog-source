---
audio: false
lang: es
layout: post
title: Promptos útiles
translated: true
---

Crea una conversación natural y extendida entre dos expertos, A y B, con al menos 100 turnos. Los expertos deben discutir un tema específico en profundidad, con la conversación fluirendo de ida y vuelta. Ambos participantes deben hacer preguntas, compartir ideas y explorar las sutilezas del tema. Utiliza habilidades como profundizar en subsecciones, comparar tecnologías, explorar casos de uso, debatir compensaciones y discutir tendencias emergentes. Amplía a 100+ turnos.

El formato debe ser el siguiente:

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

生成一个带有文本姓名的快乐农历蛇年图像

---

使用以下元素创建一个480p的YouTube视频封面图像，AI，鲨鱼，未来感，生动，色彩斑斓，日出，城市，中心有超大文字DeepSeek R1

---

为Deepseek R1创建一个YouTube标题。标题应包括所使用的主要技术。

---

生成一个简洁的提交消息，格式为Conventional Commits。使用以下类型之一：feat、fix、docs、style、refactor、test、chore、perf、ci、build或revert。如果适用，包括一个范围（括号内）来描述受影响的代码库部分。提交消息不得超过70个字符。只提供提交消息，不附带任何前导或尾随说明。

更改的文件：
{', '.join(file_changes)}