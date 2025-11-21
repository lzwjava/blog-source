---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Longitud de la Subcadena de Caracteres Únicos Más Larga
translated: true
type: note
---

**Problema**: Encuentra la longitud de la subcadena más larga sin caracteres repetidos.

**Solución**: Ventana Deslizante + HashMap (o array ya que son letras minúsculas)

Usamos dos punteros (`left` y `right`) para mantener una ventana `[left, right]`.  
A medida que movemos `right`, verificamos si `s[right]` ya apareció en la ventana actual:
- Si es así, movemos `left` hacia adelante hasta que se elimine el duplicado.
- Rastreamos la posición donde cada carácter fue visto por última vez para saltar `left` directamente.

Esto se ejecuta en tiempo **O(n)** y espacio **O(1)** (como máximo 26 o 128 caracteres).

```python
def lengthOfLongestSubstring(s: str) -> int:
    if not s:
        return 0
    
    # char -> último índice visto
    last_seen = {}
    max_len = 0
    left = 0
    
    for right in range(len(s)):
        ch = s[right]
        
        # Si el carácter ya está en la ventana actual, reducir desde la izquierda
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1
        else:
            # Actualizar la longitud máxima cuando la ventana es válida
            max_len = max(max_len, right - left + 1)
        
        # Registrar la última posición de este carácter
        last_seen[ch] = right
    
    return max_len
```

### Casos de prueba

```python
print(lengthOfLongestSubstring("abacabcbb"))  # 3 ("abc" o "bac")
print(lengthOfLongestSubstring("bbbbb"))      # 1 ("b")
print(lengthOfLongestSubstring("pwwkew"))     # 3 ("wke")
```

**Explicación de los ejemplos**:
- "abacabcbb" → "abc" o "bac" longitud = 3
- "bbbbb" → solo "b" longitud = 1
- "pwwkew" → "wke" longitud = 3 (nota: "pwke" también es válida, pero "ww" la rompe antes)

También puedes usar una lista de tamaño 128 en lugar de un dict para un tiempo constante ligeramente más rápido si sabes que el conjunto de caracteres es ASCII.