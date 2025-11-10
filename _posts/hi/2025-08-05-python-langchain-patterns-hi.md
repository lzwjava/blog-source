---
audio: false
generated: true
image: false
lang: hi
layout: post
title: पाइथन लैंगचेन पैटर्न्स
translated: true
type: note
---

यहाँ LangChain पैटर्न के कुछ संक्षिप्त, उदाहरणात्मक Python स्निपेट दिए गए हैं। आप इन टुकड़ों को मिलाकर अधिक जटिल वर्कफ़्लो बना सकते हैं।

---

### 1. PromptTemplate के साथ सरल LLM चेन

```python
from langchain import OpenAI, LLMChain, PromptTemplate

# 1. LLM को इनिशियलाइज़ करें
llm = OpenAI(temperature=0.7)

# 2. एक प्रॉम्प्ट टेम्पलेट बनाएँ
template = PromptTemplate(
    input_variables=["product"],
    template="इस उत्पाद के लिए एक छोटा सा मार्केटिंग ब्लर्ब लिखें: {product}."
)

# 3. चेन बनाएँ
chain = LLMChain(llm=llm, prompt=template)

# 4. इसे रन करें
result = chain.run({"product": "wireless noise-cancelling headphones"})
print(result)
```

---

### 2. मेमोरी के साथ कन्वर्सेशन चेन

```python
from langchain import OpenAI, ConversationChain
from langchain.memory import ConversationBufferMemory

# 1. LLM और मेमोरी
llm = OpenAI(temperature=0)
memory = ConversationBufferMemory()

# 2. कन्वर्सेशन चेन बनाएँ
conv = ConversationChain(llm=llm, memory=memory)

# 3. डायलॉग सिम्युलेट करें
print(conv.predict(input="Hi there!"))
print(conv.predict(input="Can you remind me what we talked about before?"))
```

---

### 3. डॉक्यूमेंट्स पर रिट्रीवल + प्रश्नोत्तर (FAISS)

```python
from langchain import OpenAI, RetrievalQA
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import TextLoader

# 1. डॉक्यूमेंट्स लोड और स्प्लिट करें
loader = TextLoader("my_docs/guide.txt")
docs = loader.load()
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
chunks = splitter.split_documents(docs)

# 2. एम्बेड और इंडेक्स करें
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(chunks, embeddings)

# 3. एक RetrievalQA चेन बनाएँ
qa = RetrievalQA.from_chain_type(
    llm=OpenAI(temperature=0),
    chain_type="stuff",
    retriever=vectorstore.as_retriever()
)

# 4. सवाल पूछें
answer = qa.run("What are the primary benefits of our API?")
print(answer)
```

---

### 4. टूल्स के साथ एजेंट

```python
from langchain import OpenAI, SerpAPIWrapper, LLMMathChain, initialize_agent
from langchain.agents import Tool

# 1. टूल्स डिफाइन करें
search = SerpAPIWrapper()
tools = [
    Tool(
        name="Search",
        func=search.run,
        description="वेब सर्च के लिए उपयोगी"
    ),
    Tool(
        name="Calculator",
        func=LLMMathChain.from_llm(OpenAI(temperature=0)).run,
        description="गणना के लिए उपयोगी"
    )
]

# 2. एजेंट बनाएँ
agent = initialize_agent(
    tools,
    llm=OpenAI(temperature=0),
    agent="zero-shot-react-description",
    verbose=True
)

# 3. एजेंट को रन करें
response = agent.run("What's the capital of France plus two times five?")
print(response)
```

---

इनमें से किसी भी स्निपेट को अपने अनुसार बदलने के लिए स्वतंत्र महसूस करें—अलग-अलग LLM इस्तेमाल करें, रिट्रीवर बदलें (जैसे, Chroma, Pinecone), या अपनी खुद की टूल्स और मेमोरी प्रकार जोड़ें!