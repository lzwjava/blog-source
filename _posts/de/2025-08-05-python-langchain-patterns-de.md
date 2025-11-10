---
audio: false
generated: true
image: false
lang: de
layout: post
title: Python LangChain Muster
translated: true
type: note
---

Hier sind einige prägnante, illustrative Python-Codeausschnitte, die gängige LangChain-Muster zeigen. Sie können diese Teile kombinieren, um komplexere Workflows zu erstellen.

---

### 1. Einfache LLM-Kette mit einem PromptTemplate

```python
from langchain import OpenAI, LLMChain, PromptTemplate

# 1. Initialisiere das LLM
llm = OpenAI(temperature=0.7)

# 2. Erstelle eine Prompt-Vorlage
template = PromptTemplate(
    input_variables=["product"],
    template="Schreibe einen kurzen Marketing-Text für das Produkt: {product}."
)

# 3. Baue die Kette
chain = LLMChain(llm=llm, prompt=template)

# 4. Führe sie aus
result = chain.run({"product": "kabellose Noise-Cancelling-Kopfhörer"})
print(result)
```

---

### 2. Konversationskette mit Gedächtnis

```python
from langchain import OpenAI, ConversationChain
from langchain.memory import ConversationBufferMemory

# 1. LLM und Gedächtnis
llm = OpenAI(temperature=0)
memory = ConversationBufferMemory()

# 2. Baue die Konversationskette
conv = ConversationChain(llm=llm, memory=memory)

# 3. Simuliere einen Dialog
print(conv.predict(input="Hallo!"))
print(conv.predict(input="Kannst du mich daran erinnern, worüber wir vorher gesprochen haben?"))
```

---

### 3. Retrieval + QA über Dokumente (FAISS)

```python
from langchain import OpenAI, RetrievalQA
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import TextLoader

# 1. Lade und teile Dokumente
loader = TextLoader("my_docs/guide.txt")
docs = loader.load()
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
chunks = splitter.split_documents(docs)

# 2. Embedde und indexiere
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(chunks, embeddings)

# 3. Baue eine RetrievalQA-Kette
qa = RetrievalQA.from_chain_type(
    llm=OpenAI(temperature=0),
    chain_type="stuff",
    retriever=vectorstore.as_retriever()
)

# 4. Stelle Fragen
answer = qa.run("Was sind die Hauptvorteile unserer API?")
print(answer)
```

---

### 4. Agent mit Tools

```python
from langchain import OpenAI, SerpAPIWrapper, LLMMathChain, initialize_agent
from langchain.agents import Tool

# 1. Definiere Tools
search = SerpAPIWrapper()
tools = [
    Tool(
        name="Search",
        func=search.run,
        description="Nützlich für Websuchen"
    ),
    Tool(
        name="Calculator",
        func=LLMMathChain.from_llm(OpenAI(temperature=0)).run,
        description="Nützlich für mathematische Berechnungen"
    )
]

# 2. Erstelle einen Agenten
agent = initialize_agent(
    tools,
    llm=OpenAI(temperature=0),
    agent="zero-shot-react-description",
    verbose=True
)

# 3. Führe den Agenten aus
response = agent.run("Was ist die Hauptstadt von Frankreich plus zwei mal fünf?")
print(response)
```

---

Sie können jeden dieser Codeausschnitte anpassen – tauschen Sie verschiedene LLMs aus, ändern Sie Retriever (z.B. Chroma, Pinecone) oder fügen Sie Ihre eigenen Tools und Gedächtnistypen nach Bedarf hinzu!