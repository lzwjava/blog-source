---
audio: false
lang: zh
layout: post
title: Mistral AI 向量
translated: true
---

要使用 Mistral AI 提供的嵌入示例，可以利用他们的嵌入 API 生成捕捉语义意义的文本数值表示（嵌入）。这些嵌入对于相似性检测、聚类、分类或搜索等任务非常有用。下面，我将演示如何为一组句子生成嵌入并计算它们的相似性，使用 Mistral AI 的嵌入端点。这个示例基于提供的代码结构，但专门针对嵌入进行了调整，如文档中所述：[Mistral AI 嵌入](https://docs.mistral.ai/capabilities/embeddings/)。

### 前提条件

在运行示例之前，请确保你有：
1. **API 密钥**：有效的 Mistral AI API 密钥存储在 `MISTRAL_API_KEY` 环境变量中。
2. **依赖项**：安装所需的 Python 包。你可以使用以下命令安装它们：
   ```bash
   pip install requests numpy
   ```

### 示例代码

以下是一个完整的 Python 脚本，它为三个句子生成嵌入并计算它们的相似性：

```python
import os
import requests
import numpy as np

def call_mistral_embeddings_api(texts, model="mistral-embed"):
    """
    调用 Mistral AI 嵌入 API 为文本列表生成嵌入。

    参数:
        texts (list): 要嵌入的字符串列表。
        model (str): 要使用的嵌入模型（默认: "mistral-embed"）。

    返回:
        list: 嵌入向量列表，如果请求失败则返回 None。
    """
    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        print("错误: MISTRAL_API_KEY 环境变量未设置。")
        return None

    url = "https://api.mistral.ai/v1/embeddings"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": model,
        "input": texts
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        response_json = response.json()
        if response_json and "data" in response_json:
            embeddings = [item["embedding"] for item in response_json["data"]]
            return embeddings
        else:
            print(f"Mistral 嵌入 API 错误: 无效的响应格式: {response_json}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Mistral 嵌入 API 错误: {e}")
        if e.response:
            print(f"响应状态码: {e.response.status_code}")
            print(f"响应内容: {e.response.text}")
        return None

def calculate_similarity(emb1, emb2):
    """
    使用点积计算两个嵌入之间的相似性。

    参数:
        emb1 (list): 第一个嵌入向量。
        emb2 (list): 第二个嵌入向量。

    返回:
        float: 相似性得分（点积，等同于归一化向量的余弦相似性）。
    """
    return np.dot(emb1, emb2)

if __name__ == "__main__":
    # 示例文本嵌入
    texts = [
        "我喜欢用 Python 编程。",
        "Python 是一种伟大的编程语言。",
        "今天天气晴朗。"
    ]

    # 生成嵌入
    embeddings = call_mistral_embeddings_api(texts)
    if embeddings:
        # 打印嵌入维度
        print(f"嵌入维度: {len(embeddings[0])}")

        # 计算成对相似性
        sim_12 = calculate_similarity(embeddings[0], embeddings[1])
        sim_13 = calculate_similarity(embeddings[0], embeddings[2])
        sim_23 = calculate_similarity(embeddings[1], embeddings[2])

        # 显示结果
        print(f"\n相似性结果:")
        print(f"文本 1: '{texts[0]}'")
        print(f"文本 2: '{texts[1]}'")
        print(f"文本 3: '{texts[2]}'")
        print(f"\n文本 1 和文本 2 的相似性: {sim_12:.4f}")
        print(f"文本 1 和文本 3 的相似性: {sim_13:.4f}")
        print(f"文本 2 和文本 3 的相似性: {sim_23:.4f}")
```

### 如何运行

1. **设置 API 密钥**：
   ```bash
   export MISTRAL_API_KEY="your_api_key_here"
   ```

2. **保存并执行**：
   将脚本保存（例如，作为 `embedding_example.py`）并运行它：
   ```bash
   python embedding_example.py
   ```

### 预期输出

假设 API 调用成功，你将看到类似以下的输出（具体值取决于返回的嵌入）：
```
嵌入维度: 1024

相似性结果:
文本 1: '我喜欢用 Python 编程。'
文本 2: 'Python 是一种伟大的编程语言。'
文本 3: '今天天气晴朗。'

文本 1 和文本 2 的相似性: 0.9200
文本 1 和文本 3 的相似性: 0.6500
文本 2 和文本 3 的相似性: 0.6700
```

### 解释

- **API 端点**：`call_mistral_embeddings_api` 函数向 `https://api.mistral.ai/v1/embeddings` 发送 POST 请求，传递文本列表和 `"mistral-embed"` 模型。API 返回一个包含嵌入的 JSON 响应，嵌入位于 `"data"` 键下。

- **嵌入**：每个嵌入是一个 1024 维向量（根据 Mistral 的文档），表示输入文本的语义内容。嵌入归一化到 1 的范数。

- **相似性计算**：由于嵌入已归一化，两个嵌入之间的点积（`np.dot`）等于它们的余弦相似性。较高的值表示更大的语义相似性：
  - **文本 1 和文本 2**：两者都涉及用 Python 编程，因此它们的相似性应该很高（例如，约 0.92）。
  - **文本 1 和文本 3**：一个涉及编程，另一个涉及天气，因此它们的相似性应该较低（例如，约 0.65）。
  - **文本 2 和文本 3**：相似的模式，由于主题不同，相似性较低。

### 附加用例

Mistral AI 的嵌入可以应用于相似性检测之外的更多用例：
- **聚类**：使用 K-means 等算法对相似文本进行分组（需要 `scikit-learn`）。
  ```python
  from sklearn.cluster import KMeans
  kmeans = KMeans(n_clusters=2).fit(np.array(embeddings))
  print(kmeans.labels_)
  ```
- **搜索**：嵌入查询并找到最相似的文本：
  ```python
  query = "告诉我关于 Python 的信息。"
  query_emb = call_mistral_embeddings_api([query])[0]
  similarities = [calculate_similarity(query_emb, emb) for emb in embeddings]
  most_similar = texts[np.argmax(similarities)]
  print(f"最相似的文本: '{most_similar}'")
  ```
- **分类**：将嵌入作为机器学习模型的特征。

### 注意事项

- **模型**：`"mistral-embed"` 模型专为嵌入优化。请查看[文档](https://docs.mistral.ai/capabilities/embeddings/)以获取更新或其他模型。
- **批处理**：API 可以在一个调用中处理多个文本，从而提高效率。
- **高级应用**：对于大规模相似性搜索，可以与 Faiss 或 Milvus 等向量数据库集成。

这个示例提供了使用 Mistral AI 嵌入的实际介绍，可以通过更改端点和数据格式适应提供的聊天完成代码结构。