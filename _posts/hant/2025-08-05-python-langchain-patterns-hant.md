---
audio: false
generated: true
image: false
lang: hant
layout: post
title: Python LangChain 模式
translated: true
type: note
---

以下是幾個簡潔的 Python 程式碼片段，展示了常見的 LangChain 模式。你可以混合搭配這些片段來建構更複雜的工作流程。

---

### 1. 使用 PromptTemplate 的簡單 LLM 鏈

```python
from langchain import OpenAI, LLMChain, PromptTemplate

# 1. 初始化 LLM
llm = OpenAI(temperature=0.7)

# 2. 建立提示模板
template = PromptTemplate(
    input_variables=["product"],
    template="為以下產品撰寫簡短的行銷文案：{product}。"
)

# 3. 建構鏈
chain = LLMChain(llm=llm, prompt=template)

# 4. 執行
result = chain.run({"product": "無線降噪耳機"})
print(result)
```

---

### 2. 具備記憶功能的對話鏈

```python
from langchain import OpenAI, ConversationChain
from langchain.memory import ConversationBufferMemory

# 1. LLM 與記憶體
llm = OpenAI(temperature=0)
memory = ConversationBufferMemory()

# 2. 建構對話鏈
conv = ConversationChain(llm=llm, memory=memory)

# 3. 模擬對話
print(conv.predict(input="你好！"))
print(conv.predict(input="可以提醒我們之前談論過什麼嗎？"))
```

---

### 3. 文件檢索 + 問答系統 (FAISS)

```python
from langchain import OpenAI, RetrievalQA
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import TextLoader

# 1. 載入並分割文件
loader = TextLoader("my_docs/guide.txt")
docs = loader.load()
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
chunks = splitter.split_documents(docs)

# 2. 嵌入與索引
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(chunks, embeddings)

# 3. 建構 RetrievalQA 鏈
qa = RetrievalQA.from_chain_type(
    llm=OpenAI(temperature=0),
    chain_type="stuff",
    retriever=vectorstore.as_retriever()
)

# 4. 提問
answer = qa.run("我們 API 的主要優勢是什麼？")
print(answer)
```

---

### 4. 具備工具的代理

```python
from langchain import OpenAI, SerpAPIWrapper, LLMMathChain, initialize_agent
from langchain.agents import Tool

# 1. 定義工具
search = SerpAPIWrapper()
tools = [
    Tool(
        name="Search",
        func=search.run,
        description="適用於網路搜尋"
    ),
    Tool(
        name="Calculator",
        func=LLMMathChain.from_llm(OpenAI(temperature=0)).run,
        description="適用於數學計算"
    )
]

# 2. 建立代理
agent = initialize_agent(
    tools,
    llm=OpenAI(temperature=0),
    agent="zero-shot-react-description",
    verbose=True
)

# 3. 執行代理
response = agent.run("法國的首都加上兩乘以五等於多少？")
print(response)
```

---

歡迎隨意改編這些程式碼片段——你可以替換不同的 LLM、更換檢索器（例如 Chroma、Pinecone），或根據需要加入自己的工具和記憶類型！