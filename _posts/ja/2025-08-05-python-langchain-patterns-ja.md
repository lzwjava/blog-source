---
audio: false
generated: true
image: false
lang: ja
layout: post
title: Python LangChainパターン
translated: true
type: note
---

以下は、一般的なLangChainパターンを実演する簡潔なPythonスニペットです。これらの要素を組み合わせて、より複雑なワークフローを構築できます。

---

### 1. PromptTemplateを使用したシンプルなLLMチェーン

```python
from langchain import OpenAI, LLMChain, PromptTemplate

# 1. LLMの初期化
llm = OpenAI(temperature=0.7)

# 2. プロンプトテンプレートの作成
template = PromptTemplate(
    input_variables=["product"],
    template="製品の短いマーケティング紹介文を作成してください: {product}."
)

# 3. チェーンの構築
chain = LLMChain(llm=llm, prompt=template)

# 4. 実行
result = chain.run({"product": "ワイヤレスノイズキャンセリングヘッドフォン"})
print(result)
```

---

### 2. メモリ機能付き会話チェーン

```python
from langchain import OpenAI, ConversationChain
from langchain.memory import ConversationBufferMemory

# 1. LLMとメモリ
llm = OpenAI(temperature=0)
memory = ConversationBufferMemory()

# 2. 会話チェーンの構築
conv = ConversationChain(llm=llm, memory=memory)

# 3. 対話のシミュレーション
print(conv.predict(input="こんにちは！"))
print(conv.predict(input="前回私たちが何について話したか思い出させてくれますか？"))
```

---

### 3. ドキュメント検索＋QA（FAISS使用）

```python
from langchain import OpenAI, RetrievalQA
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import TextLoader

# 1. ドキュメントの読み込みと分割
loader = TextLoader("my_docs/guide.txt")
docs = loader.load()
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
chunks = splitter.split_documents(docs)

# 2. 埋め込みとインデックス作成
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(chunks, embeddings)

# 3. RetrievalQAチェーンの構築
qa = RetrievalQA.from_chain_type(
    llm=OpenAI(temperature=0),
    chain_type="stuff",
    retriever=vectorstore.as_retriever()
)

# 4. 質問
answer = qa.run("私たちのAPIの主な利点は何ですか？")
print(answer)
```

---

### 4. ツールを使用したエージェント

```python
from langchain import OpenAI, SerpAPIWrapper, LLMMathChain, initialize_agent
from langchain.agents import Tool

# 1. ツールの定義
search = SerpAPIWrapper()
tools = [
    Tool(
        name="Search",
        func=search.run,
        description="ウェブ検索に有用"
    ),
    Tool(
        name="Calculator",
        func=LLMMathChain.from_llm(OpenAI(temperature=0)).run,
        description="数学計算に有用"
    )
]

# 2. エージェントの作成
agent = initialize_agent(
    tools,
    llm=OpenAI(temperature=0),
    agent="zero-shot-react-description",
    verbose=True
)

# 3. エージェントの実行
response = agent.run("フランスの首都に2×5を足した数は？")
print(response)
```

---

これらのスニペットを自由に適応させてください。異なるLLMへの切り替え、Retrieverの変更（例：Chroma、Pinecone）、独自のツールやメモリタイプの追加などが可能です！