---
audio: false
generated: true
image: false
lang: ar
layout: post
title: أنماط لانج تشين في بايثون
translated: true
type: note
---

فيما يلي بعض المقاطع البرمجية التوضيحية المختصرة في Python التي تُظهر أنماط LangChain الشائعة. يمكنك خلط ومطابقة هذه الأجزاء لبناء سير عمل أكثر تعقيدًا.

---

### 1. سلسلة LLM بسيطة مع PromptTemplate

```python
from langchain import OpenAI, LLMChain, PromptTemplate

# 1. تهيئة الـ LLM
llm = OpenAI(temperature=0.7)

# 2. إنشاء قالب prompt
template = PromptTemplate(
    input_variables=["product"],
    template="Write a short marketing blurb for the product: {product}."
)

# 3. بناء السلسلة
chain = LLMChain(llm=llm, prompt=template)

# 4. تشغيلها
result = chain.run({"product": "wireless noise-cancelling headphones"})
print(result)
```

---

### 2. سلسلة محادثة مع الذاكرة

```python
from langchain import OpenAI, ConversationChain
from langchain.memory import ConversationBufferMemory

# 1. الـ LLM والذاكرة
llm = OpenAI(temperature=0)
memory = ConversationBufferMemory()

# 2. بناء سلسلة المحادثة
conv = ConversationChain(llm=llm, memory=memory)

# 3. محاكاة الحوار
print(conv.predict(input="Hi there!"))
print(conv.predict(input="Can you remind me what we talked about before?"))
```

---

### 3. استرجاع + سؤال وجواب على المستندات (FAISS)

```python
from langchain import OpenAI, RetrievalQA
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import TextLoader

# 1. تحميل وتقسيم المستندات
loader = TextLoader("my_docs/guide.txt")
docs = loader.load()
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
chunks = splitter.split_documents(docs)

# 2. التضمين والفهرسة
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(chunks, embeddings)

# 3. بناء سلسلة RetrievalQA
qa = RetrievalQA.from_chain_type(
    llm=OpenAI(temperature=0),
    chain_type="stuff",
    retriever=vectorstore.as_retriever()
)

# 4. طرح الأسئلة
answer = qa.run("What are the primary benefits of our API?")
print(answer)
```

---

### 4. وكيل مع أدوات

```python
from langchain import OpenAI, SerpAPIWrapper, LLMMathChain, initialize_agent
from langchain.agents import Tool

# 1. تعريف الأدوات
search = SerpAPIWrapper()
tools = [
    Tool(
        name="Search",
        func=search.run,
        description="Useful for web searches"
    ),
    Tool(
        name="Calculator",
        func=LLMMathChain.from_llm(OpenAI(temperature=0)).run,
        description="Useful for math calculations"
    )
]

# 2. إنشاء الوكيل
agent = initialize_agent(
    tools,
    llm=OpenAI(temperature=0),
    agent="zero-shot-react-description",
    verbose=True
)

# 3. تشغيل الوكيل
response = agent.run("What's the capital of France plus two times five?")
print(response)
```

---

لا تتردد في تعديل أي من هذه المقاطع البرمجية — استبدل نماذج LLM مختلفة، أو غيّر أدوات الاسترجاع (مثل Chroma أو Pinecone)، أو أضف أدواتك الخاصة وأنواع الذاكرة حسب الحاجة!