---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Centrado de Elementos de Formulario Apilados con Flexbox
translated: true
---

```css
.sort-container {
    display: flex;
    flex-direction: column; /* Añade esto para apilar elementos verticalmente */
    align-items: center; /* Centra elementos horizontalmente en la columna */
    justify-content: center; /* Centra la columna verticalmente */
    gap: 10px;
    margin-bottom: 1rem;
}

.sort-container select {
    padding: 5px;
    font-size: 16px;
}

.sort-container .post-number {
    font-size: 16px;
}
```

### Explicación
- **flex-direction: column**: Cambia el eje principal de horizontal (row) a vertical, apilando los elementos `select` y `.post-number` de arriba a abajo.
- **align-items: center**: Mantiene el centrado horizontal de los elementos hijos.
- **justify-content: center**: Centra toda la pila vertical dentro del contenedor.
- También corregí la sintaxis de los selectores anidados (moví `select` y `.post-number` fuera del bloque principal para una mejor práctica, asumiendo que son hijos directos—ajusta si es necesario). El `gap` ahora se aplica verticalmente entre elementos.