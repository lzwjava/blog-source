---
audio: false
generated: true
image: false
lang: es
layout: post
model: openai/gpt-5
title: Inversión de una matriz de 3x3
translated: true
type: note
---

Claro — desglosemos esto de manera clara e intuitiva, sin formato de tabla para que sea fácil de leer línea por línea.  

---

### 1. Cuál es el objetivo  
Queremos encontrar la inversa de una matriz de 3×3, generalmente escrita como A⁻¹.  
La inversa es la matriz que "deshace" A, lo que significa  
A × A⁻¹ = I,  
donde I es la matriz identidad.  

---

### 2. La fórmula central  
La fórmula general para cualquier matriz cuadrada invertible es  

A⁻¹ = (1 / det(A)) × adj(A).  

Así que necesitamos dos ingredientes:  
- el determinante det(A), y  
- la matriz adjunta adj(A), que es la transpuesta de la matriz de cofactores.  

---

### 3. Determinante de una matriz 3×3  
Si  
A =  
[a  b  c]  
[d  e  f]  
[g  h  i],  

entonces  

det(A) = a(ei − fh) − b(di − fg) + c(dh − eg).  

Este valor te dice si la matriz es invertible:  
- si det(A) = 0 → no hay inversa (la matriz es singular),  
- si det(A) ≠ 0 → la inversa existe.  

---

### 4. Cofactores  
Para construir adj(A), primero encontramos el cofactor de cada elemento.  
El cofactor de la entrada aᵢⱼ es  
Cᵢⱼ = (−1)^(i+j) × Mᵢⱼ,  
donde Mᵢⱼ es el determinante de la submatriz 2×2 que obtienes después de eliminar la fila i y la columna j.  

Hacer esto para las nueve posiciones da la "matriz de cofactores".  
Para el caso general anterior:  

C₁₁ = ei − fh  
C₁₂ = −(di − fg)  
C₁₃ = dh − eg  

C₂₁ = −(bi − ch)  
C₂₂ = ai − cg  
C₂₃ = −(ah − bg)  

C₃₁ = bf − ce  
C₃₂ = −(af − cd)  
C₃₃ = ae − bd  

---

### 5. Transponer la matriz de cofactores  
Ahora toma esa matriz de cofactores y transpónla — es decir, intercambia filas y columnas.  
Esa nueva matriz se llama la **adjunta** de A, escrita como adj(A).  
Si lo piensas visualmente, esta "transposición" es como rotar la matriz: lo que estaba en la primera fila se convierte en la primera columna, y así sucesivamente.  

---

### 6. Multiplicar por 1/det(A)  
Finalmente, escala la matriz adjunta dividiendo cada término por det(A).  
Eso te da A⁻¹.  

Simbólicamente:  
A⁻¹ = (1/det(A)) × adj(A).  

---

### 7. Por qué funciona  
Esta fórmula proviene de una propiedad fundamental de los determinantes y los cofactores:  

A × adj(A) = det(A) × I.  

Si divides ambos lados por det(A), obtienes exactamente  
A × [(1/det(A)) × adj(A)] = I.  

Así que el factor del lado derecho debe ser la inversa.  

La razón por la que se cumple esta identidad es que cuando multiplicas A por su matriz de cofactores, cada término diagonal se convierte en el determinante mismo (ya que es la expansión a lo largo de esa fila), y cada término fuera de la diagonal se vuelve cero debido a los signos alternantes de los cofactores — esa es la cancelación algebraica en acción.  

---

### 8. Ejemplo  
Sea  
A =  
[1  2  3]  
[0  1  4]  
[5  6  0].  

Calcula det(A):  
= 1(1×0 − 4×6) − 2(0×0 − 4×5) + 3(0×6 − 1×5)  
= (−24) − (−40) + (−15)  
= −24 + 40 − 15 = 1.  

Entonces det(A) = 1.  

Luego encuentra todos los cofactores (un poco tedioso, pero sencillo), transpónelos para obtener adj(A), y como det(A) = 1, la adjunta ya es la inversa.  

---

### 9. Intuición resumida  
- Determinante → una medida de cómo la matriz "escala el espacio".  
- Cofactor → captura la contribución de cada elemento a ese escalado.  
- Transponer → alinea esas contribuciones para que la multiplicación reconstruya la identidad.  
- Dividir por el determinante → normaliza el escalado.  

---

¿Te gustaría que muestre los cálculos detallados de los cofactores para ese ejemplo (el [1 2 3; 0 1 4; 5 6 0]) para que puedas ver cada menor y signo?