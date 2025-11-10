---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Modèles Python LangChain
translated: true
type: note
---

Voici quelques extraits Python concis et illustratifs montrant des modèles courants de LangChain. Vous pouvez mélanger et assembler ces éléments pour créer des flux de travail plus complexes.

---

### 1. Chaîne LLM simple avec un PromptTemplate

```python
from langchain import OpenAI, LLMChain, PromptTemplate

# 1. Initialiser le LLM
llm = OpenAI(temperature=0.7)

# 2. Créer un modèle de prompt
template = PromptTemplate(
    input_variables=["product"],
    template="Rédigez un petit texte marketing pour le produit : {product}."
)

# 3. Construire la chaîne
chain = LLMChain(llm=llm, prompt=template)

# 4. L'exécuter
result = chain.run({"product": "casque sans fil à réduction de bruit"})
print(result)
```

---

### 2. Chaîne de conversation avec mémoire

```python
from langchain import OpenAI, ConversationChain
from langchain.memory import ConversationBufferMemory

# 1. LLM et mémoire
llm = OpenAI(temperature=0)
memory = ConversationBufferMemory()

# 2. Construire la chaîne de conversation
conv = ConversationChain(llm=llm, memory=memory)

# 3. Simuler un dialogue
print(conv.predict(input="Bonjour !"))
print(conv.predict(input="Pouvez-vous me rappeler de quoi nous avons parlé précédemment ?"))
```

---

### 3. Récupération + QA sur des documents (FAISS)

```python
from langchain import OpenAI, RetrievalQA
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import TextLoader

# 1. Charger et diviser les documents
loader = TextLoader("my_docs/guide.txt")
docs = loader.load()
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
chunks = splitter.split_documents(docs)

# 2. Intégrer et indexer
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(chunks, embeddings)

# 3. Construire une chaîne RetrievalQA
qa = RetrievalQA.from_chain_type(
    llm=OpenAI(temperature=0),
    chain_type="stuff",
    retriever=vectorstore.as_retriever()
)

# 4. Poser des questions
answer = qa.run("Quels sont les principaux avantages de notre API ?")
print(answer)
```

---

### 4. Agent avec des outils

```python
from langchain import OpenAI, SerpAPIWrapper, LLMMathChain, initialize_agent
from langchain.agents import Tool

# 1. Définir les outils
search = SerpAPIWrapper()
tools = [
    Tool(
        name="Search",
        func=search.run,
        description="Utile pour les recherches web"
    ),
    Tool(
        name="Calculator",
        func=LLMMathChain.from_llm(OpenAI(temperature=0)).run,
        description="Utile pour les calculs mathématiques"
    )
]

# 2. Créer l'agent
agent = initialize_agent(
    tools,
    llm=OpenAI(temperature=0),
    agent="zero-shot-react-description",
    verbose=True
)

# 3. Exécuter l'agent
response = agent.run("Quelle est la capitale de la France plus deux fois cinq ?")
print(response)
```

---

N'hésitez pas à adapter ces extraits — remplacez par différents LLM, changez les systèmes de récupération (par exemple, Chroma, Pinecone), ou ajoutez vos propres types d'outils et de mémoire selon vos besoins !