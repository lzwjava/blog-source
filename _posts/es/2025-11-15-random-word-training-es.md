---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Capacitación sobre Ensalada de Palabras Aleatorias
translated: true
type: note
---

Si entrenas un modelo pequeño como nanoGPT (o cualquier transformer similar a GPT-2 small) con 2–3 GB de **palabras aleatorias que parezcan inglés** (es decir, secuencias de palabras reales en inglés escogidas uniformemente al azar, sin gramática, sin significado, solo una ensalada de palabras), esto es lo que realmente sucederá:

### El modelo aprenderá que **no hay estructura** que aprender
- Descubrirá muy rápidamente la distribución de tokens (las frecuencias unigramas de las palabras).
- Se dará cuenta de que la siguiente palabra es esencialmente independiente de las palabras anteriores (o muy cercana a la independencia).
- La perplejidad en los datos de entrenamiento tocará fondo extremadamente rápido (después de pocas épocas ya estará cerca de la entropía de la distribución uniforme de palabras).
- El modelo esencialmente se convertirá en un **muestreador unigrama**: simplemente generará palabras de acuerdo con su frecuencia marginal en los datos de entrenamiento, con casi cero dependencia del contexto.

### El texto generado será ligeramente mejor que un sinsentido puro, pero seguirá siendo basura completa
Ejemplo de lo que obtendrás después del entrenamiento:

> el gato rápidamente bajo ayer manzana plátano elefante corriendo púrpura sin embargo mañana queso rayo rápidamente cebra sándwich para siempre montaña bicicleta naranja elefante ayer plátano

Hará lo siguiente:
- Usar palabras reales en inglés ✓
- Respetar las frecuencias de las palabras (palabras comunes como "the", "and", "to" aparecerán mucho) ✓
- Tener una ortografía perfecta ✓
- Ser 100% gramatical y semánticamente incoherente ✗

**No** aprenderá:
- Gramática o sintaxis
- Cualquier estructura de frase
- La ubicación de las palabras funcionales
- Cualquier tipo de significado o coherencia temática
- Incluso bigramas/trigramas más allá de un débil ruido estadístico

### Comparación con el entrenamiento en texto real
Cuando entrenas nanoGPT con texto real (por ejemplo, Shakespeare u OpenWebText), incluso con solo 2–3 GB, empiezas a ver surgir oraciones reales sorprendentemente rápido porque hay una estructura rica y predecible.

Con palabras puramente aleatorias, nunca cruzarás el umbral hacia la coherencia, sin importar cuánto tiempo entrenes. El modelo converge casi inmediatamente a "la siguiente palabra es aleatoria según la frecuencia" y deja de mejorar.

### Experimento divertido que puedes probar
Puedes generar fácilmente un conjunto de datos así:

```python
import random
words = open('big-wordlist.txt').read().splitlines()  # por ejemplo, 300k palabras en inglés
with open('random_3gb.txt', 'w') as f:
    for _ in range(500_000_000):  # ~3 GB
        f.write(random.choice(words) + ' ')
```

Entrena nanoGPT con él durante unas horas. Verás que la pérdida cae a ~4–5 nats (que es básicamente la entropía de la distribución de palabras en inglés) y luego se aplana por completo. El muestreo posterior dará exactamente la ensalada de palabras anterior.

### Conclusión
Sí, el texto generado será casi puro sinsentido, solo un sinsentido ligeramente más "natural" que si muestreararas palabras uniformemente de un diccionario, porque coincidirá con las frecuencias reales de las palabras. Pero nunca dirá nada remotamente significativo o gramatical.

En realidad, es una forma excelente de demostrarte a ti mismo cuánto el lenguaje real depende de las dependencias de largo alcance y la estructura, porque cuando eliminas todo eso, incluso una arquitectura potente como GPT aprende esencialmente nada útil.