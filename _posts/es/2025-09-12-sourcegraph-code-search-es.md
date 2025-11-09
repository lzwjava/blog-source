---
audio: false
date: 2025-09-12
generated: true
image: false
lang: es
layout: post
model: mistralai/mistral-medium-3.1
title: Guía de Búsqueda de Código de Sourcegraph
translated: true
type: note
---

Sourcegraph es una potente herramienta de búsqueda y navegación de código que permite a los desarrolladores buscar en múltiples repositorios, comprender las dependencias del código y navegar eficientemente por bases de código grandes. Esta guía cubre **sintaxis de búsqueda, mejores prácticas y búsquedas específicas por lenguaje (Java y Python)**.

---

## **1. Sintaxis de Búsqueda Básica**
Sourcegraph admite **búsqueda literal, por expresiones regulares y estructural** con filtros.

### **1.1. Búsqueda Literal**
Buscar texto exacto:
```
"def calculate_sum"
```

### **1.2. Búsqueda por Expresiones Regulares**
Usar `/.../` para regex:
```
/def \w+_sum\(/
```

### **1.3. Búsqueda Estructural (Beta)**
Buscar patrones de código (ej., definiciones de funciones):
```
type:func def calculate_sum
```

### **1.4. Filtros**
Refinar búsquedas con filtros:
- `repo:` – Buscar en un repositorio específico
  ```
  repo:github.com/elastic/elasticsearch "def search"
  ```
- `file:` – Buscar en archivos específicos
  ```
  file:src/main/java "public class"
  ```
- `lang:` – Buscar en un lenguaje específico
  ```
  lang:python "def test_"
  ```
- `type:` – Buscar símbolos (funciones, clases, etc.)
  ```
  type:func lang:go "func main"
  ```

---

## **2. Técnicas de Búsqueda Avanzadas**
### **2.1. Operadores Booleanos**
- `AND` (por defecto): `def calculate AND sum`
- `OR`: `def calculate OR def sum`
- `NOT`: `def calculate NOT def subtract`

### **2.2. Comodines**
- `*` – Coincide con cualquier secuencia de caracteres
  ```
  "def calculate_*"
  ```
- `?` – Coincide con un solo carácter
  ```
  "def calculate_?"
  ```

### **2.3. Sensibilidad a Mayúsculas**
- No distingue entre mayúsculas y minúsculas por defecto
- Forzar distinción con `case:yes`
  ```
  case:yes "Def Calculate"
  ```

### **2.4. Buscar en Comentarios**
Usar `patternType:literal` para buscar en comentarios:
```
patternType:literal "// TODO:"
```

---

## **3. Buscando Código Java**
### **3.1. Encontrar Clases**
```
type:symbol lang:java "public class"
```
### **3.2. Encontrar Métodos**
```
type:func lang:java "public void"
```
### **3.3. Encontrar Anotaciones**
```
lang:java "@Override"
```
### **3.4. Encontrar Imports**
```
lang:java "import org.springframework"
```
### **3.5. Encontrar Manejo de Excepciones**
```
lang:java "try {" AND "catch (Exception"
```

---

## **4. Buscando Código Python**
### **4.1. Encontrar Funciones**
```
type:func lang:python "def calculate"
```
### **4.2. Encontrar Clases**
```
type:symbol lang:python "class Calculator"
```
### **4.3. Encontrar Imports**
```
lang:python "import pandas"
```
### **4.4. Encontrar Decoradores**
```
lang:python "@app.route"
```
### **4.5. Encontrar Docstrings**
```
lang:python '"""'
```

---

## **5. Mejores Prácticas**
1. **Usa `lang:`** para acotar los resultados.
2. **Combina filtros** (`repo:`, `file:`, `type:`) para mayor precisión.
3. **Usa expresiones regulares** para una coincidencia de patrones flexible.
4. **Guarda búsquedas** para consultas frecuentes.
5. **Usa `case:yes`** cuando sea necesario.

---

## **6. Consultas de Ejemplo**

| **Objetivo** | **Consulta** |
|----------|-----------|
| Encontrar todos los métodos `main` en Java | `lang:java "public static void main"` |
| Encontrar funciones de test en Python | `lang:python "def test_"` |
| Encontrar comentarios TODO en Go | `lang:go "// TODO:"` |
| Encontrar controladores de Spring Boot | `lang:java "@RestController"` |
| Encontrar todas las sentencias `if` en JS | `lang:javascript "if ("` |

---

## **7. Conclusión**
La búsqueda de Sourcegraph es **potente y flexible**, admitiendo **búsquedas literales, por regex y estructurales** en múltiples lenguajes. Al dominar los filtros (`lang:`, `repo:`, `type:`), puedes navegar eficientemente por grandes bases de código.

### **Próximos Pasos**
- Prueba las **búsquedas guardadas** para consultas recurrentes.
- Explora la **inteligencia de código** (tooltips al pasar el cursor, navegación entre repositorios).
- Usa las **extensiones de Sourcegraph** (VS Code, JetBrains).

¿Te gustaría una inmersión más profunda en alguna característica específica? 🚀