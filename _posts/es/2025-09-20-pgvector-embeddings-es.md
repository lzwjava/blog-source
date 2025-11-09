---
audio: false
generated: true
image: false
lang: es
layout: post
model: openai/gpt-5
title: 'PGVector: Incrustaciones Vectoriales en PostgreSQL'
translated: true
type: note
---

PGVector es una **extensión de PostgreSQL** que agrega soporte para almacenar y consultar *incrustaciones vectoriales* (arreglos de números, generalmente de 128 a 4096 dimensiones) dentro de una base de datos Postgres.

Se usa comúnmente en **aplicaciones de IA y aprendizaje automático** donde necesitas almacenar y buscar incrustaciones generadas por modelos como OpenAI, Hugging Face u otros proveedores de embeddings. Por ejemplo, podrías convertir documentos, fragmentos de código o descripciones de productos en vectores y luego usar PGVector para encontrar rápidamente los más similares a una consulta del usuario.

### Características Principales

* **Tipo de dato vector**: Agrega un tipo de columna `vector` a las tablas de Postgres.
* **Búsqueda por similitud**: Soporta operaciones como similitud coseno, distancia euclidiana o producto interno para comparar vectores.
* **Índices para velocidad**: Proporciona tipos de índice `ivfflat` y `hnsw` para una búsqueda *aproximada del vecino más cercano (ANN)* eficiente, permitiendo una recuperación rápida incluso con millones de incrustaciones.
* **Integración SQL**: Al ejecutarse dentro de Postgres, puedes combinar la búsqueda vectorial con consultas SQL normales, joins y filtros.

### Ejemplo de Uso

```sql
-- Crear tabla con columna vector
CREATE TABLE items (
  id bigserial PRIMARY KEY,
  embedding vector(1536)  -- la dimensión debe coincidir con tu modelo
);

-- Insertar una fila
INSERT INTO items (embedding) VALUES ('[0.25, 0.1, ...]');

-- Buscar la incrustación más similar
SELECT id, embedding
FROM items
ORDER BY embedding <-> '[0.24, 0.11, ...]'
LIMIT 5;
```

Aquí `<->` es el operador de similitud.

### Por qué es Importante

PGVector te permite construir una **base de datos vectorial completa directamente en Postgres**, en lugar de usar una base de datos vectorial especializada por separado (como Pinecone, Weaviate o Milvus). Esto es atractivo si ya usas Postgres y quieres mantener todos los datos y consultas en un solo lugar.

---

¿Quieres que también compare **PGVector vs bases de datos vectoriales dedicadas** (como Pinecone o Weaviate) para que puedas ver cuándo usar cada una?