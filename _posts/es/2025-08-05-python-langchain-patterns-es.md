---
audio: false
generated: true
image: false
lang: es
layout: post
title: Patrones de Python LangChain
translated: true
type: note
---

Aquí tienes algunos fragmentos de código Python concisos e ilustrativos que muestran patrones comunes de LangChain. Puedes combinar estas piezas para construir flujos de trabajo más complejos.

---

### 1. Cadena LLM Simple con un PromptTemplate

```python
from langchain import OpenAI, LLMChain, PromptTemplate

# 1. Inicializar el LLM
llm = OpenAI(temperature=0.7)

# 2. Crear una plantilla de prompt
template = PromptTemplate(
    input_variables=["product"],
    template="Escribe una breve descripción de marketing para el producto: {product}."
)

# 3. Construir la cadena
chain = LLMChain(llm=llm, prompt=template)

# 4. Ejecutarla
result = chain.run({"product": "auriculares inalámbricos con cancelación de ruido"})
print(result)
```

---

### 2. Cadena de Conversación con Memoria

```python
from langchain import OpenAI, ConversationChain
from langchain.memory import ConversationBufferMemory

# 1. LLM y memoria
llm = OpenAI(temperature=0)
memory = ConversationBufferMemory()

# 2. Construir la cadena de conversación
conv = ConversationChain(llm=llm, memory=memory)

# 3. Simular un diálogo
print(conv.predict(input="¡Hola!"))
print(conv.predict(input="¿Puedes recordarme de qué hablamos antes?"))
```

---

### 3. Recuperación + Preguntas y Respuestas sobre Documentos (FAISS)

```python
from langchain import OpenAI, RetrievalQA
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import TextLoader

# 1. Cargar y dividir documentos
loader = TextLoader("my_docs/guide.txt")
docs = loader.load()
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
chunks = splitter.split_documents(docs)

# 2. Incrustar e indexar
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(chunks, embeddings)

# 3. Construir una cadena RetrievalQA
qa = RetrievalQA.from_chain_type(
    llm=OpenAI(temperature=0),
    chain_type="stuff",
    retriever=vectorstore.as_retriever()
)

# 4. Hacer preguntas
answer = qa.run("¿Cuáles son los beneficios principales de nuestra API?")
print(answer)
```

---

### 4. Agente con Herramientas

```python
from langchain import OpenAI, SerpAPIWrapper, LLMMathChain, initialize_agent
from langchain.agents import Tool

# 1. Definir herramientas
search = SerpAPIWrapper()
tools = [
    Tool(
        name="Search",
        func=search.run,
        description="Útil para búsquedas web"
    ),
    Tool(
        name="Calculator",
        func=LLMMathChain.from_llm(OpenAI(temperature=0)).run,
        description="Útil para cálculos matemáticos"
    )
]

# 2. Crear agente
agent = initialize_agent(
    tools,
    llm=OpenAI(temperature=0),
    agent="zero-shot-react-description",
    verbose=True
)

# 3. Ejecutar agente
response = agent.run("¿Cuál es la capital de Francia más dos por cinco?")
print(response)
```

---

¡Siéntete libre de adaptar cualquiera de estos fragmentos—cambia los LLM, modifica los recuperadores (por ejemplo, Chroma, Pinecone), o añade tus propias herramientas y tipos de memoria según sea necesario!