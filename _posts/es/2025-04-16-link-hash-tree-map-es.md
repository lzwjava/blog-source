---
audio: false
generated: true
lang: es
layout: post
title: LinkedHashMap frente a TreeMap
translated: true
type: note
---

¡Excelente pregunta! Tanto `LinkedHashMap` como `TreeMap` son implementaciones de la interfaz `Map` en Java, pero tienen **diferentes estrategias de ordenación** y utilizan **diferentes estructuras de datos subyacentes**.

### 🌳 `TreeMap`
- **Ordenación**: Ordenado por el **orden natural** de las claves (o por un `Comparator` personalizado si se proporciona).
- **Estructura de Datos**: Respaldado por un **Árbol Rojo-Negro** (un tipo de árbol binario de búsqueda auto-balanceado).
- **Rendimiento**:
  - `O(log n)` para get/put/remove
  - El orden ordenado se mantiene en todo momento
- **Caso de Uso**: Cuando necesitas **claves ordenadas**.

### 🔗 `LinkedHashMap`
- **Ordenación**: Mantiene el **orden de inserción** (o, opcionalmente, el orden de acceso si se configura de esa manera).
- **Estructura de Datos**: Respaldado por una **tabla hash + lista enlazada**.
- **Rendimiento**:
  - `O(1)` para get/put/remove (como `HashMap`)
  - Ligeramente más sobrecarga de memoria debido a la lista enlazada
- **Caso de Uso**: Cuando te importa **el orden en que se añadieron las entradas**.

---

### ✅ Orden del Iterador
Sí, su **orden del iterador será diferente**:

| Tipo de Map    | Orden del Iterador                 |
|----------------|------------------------------------|
| `TreeMap`      | Ordenado por las claves            |
| `LinkedHashMap`| Orden de inserción (o de acceso)   |

---

### 🔍 Ejemplo

```java
Map<String, Integer> treeMap = new TreeMap<>();
Map<String, Integer> linkedMap = new LinkedHashMap<>();

treeMap.put("banana", 2);
treeMap.put("apple", 3);
treeMap.put("cherry", 1);

linkedMap.put("banana", 2);
linkedMap.put("apple", 3);
linkedMap.put("cherry", 1);

System.out.println("TreeMap:");
for (String key : treeMap.keySet()) {
    System.out.println(key);
}

System.out.println("LinkedHashMap:");
for (String key : linkedMap.keySet()) {
    System.out.println(key);
}
```

**Salida:**
```
TreeMap:
apple
banana
cherry

LinkedHashMap:
banana
apple
cherry
```

Déjame saber si quieres un desglose del rendimiento o del uso de memoria con más detalle.