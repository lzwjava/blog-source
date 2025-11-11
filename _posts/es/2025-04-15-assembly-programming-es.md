---
audio: false
generated: true
lang: es
layout: post
title: Programación en Lenguaje Ensamblador
translated: true
type: note
---

A continuación se presenta un tutorial completo para **Parte 2: Programación en Lenguaje Ensamblador**, que cubre los temas esbozados: *Conjunto de Instrucciones del 8086 (Instrucciones de Transferencia de Datos, Aritméticas, Lógicas y de Control de Flujo), Programación en Lenguaje Ensamblador (Estructuras Secuenciales, de Bifurcación y de Bucle), y Rutinas de Servicio de Interrupciones*. Este tutorial está diseñado para ser exhaustivo, accesible y práctico, construyendo sobre los fundamentos de los microcomputadores (ej., arquitectura 8086/8088). Se asume un conocimiento básico de los registros de la CPU y el direccionamiento de memoria.

---

## Parte 2: Programación en Lenguaje Ensamblador

El lenguaje ensamblador es un lenguaje de programación de bajo nivel que proporciona control directo sobre las operaciones de un microprocesador. Para el Intel 8086/8088, el lenguaje ensamblador permite a los programadores escribir instrucciones que se mapean estrechamente al código máquina, ofreciendo un control detallado sobre recursos de hardware como registros, memoria y dispositivos de E/S.

### 1. Conjunto de Instrucciones del 8086

El conjunto de instrucciones del 8086 es una colección de comandos que la CPU entiende, categorizados por su función: **transferencia de datos**, **aritméticas**, **lógicas** y **control de flujo**. Cada instrucción opera sobre registros, memoria o valores inmediatos, utilizando los modos de direccionamiento del 8086 (ej., registro, directo, indirecto).

#### a. Instrucciones de Transferencia de Datos
Estas instrucciones mueven datos entre registros, memoria y valores inmediatos.

- **MOV (Mover)**:
  - Sintaxis: `MOV destino, origen`
  - Función: Copia datos del origen al destino.
  - Ejemplo: `MOV AX, BX` (copia BX a AX); `MOV AX, [1234h]` (copia datos de la dirección de memoria DS:1234h a AX).
  - Notas: No afecta los flags; el origen y el destino deben ser del mismo tamaño (8-bit o 16-bit).
- **XCHG (Intercambiar)**:
  - Sintaxis: `XCHG destino, origen`
  - Función: Intercambia los contenidos del origen y el destino.
  - Ejemplo: `XCHG AX, BX` (intercambia AX y BX).
- **PUSH (Empujar a la Pila)**:
  - Sintaxis: `PUSH origen`
  - Función: Empuja datos de 16 bits a la pila, decrementa SP en 2.
  - Ejemplo: `PUSH AX` (guarda AX en la pila).
- **POP (Sacar de la Pila)**:
  - Sintaxis: `POP destino`
  - Función: Saca datos de 16 bits de la pila al destino, incrementa SP en 2.
  - Ejemplo: `POP BX` (restaura BX desde la pila).
- **LEA (Cargar Dirección Efectiva)**:
  - Sintaxis: `LEA destino, origen`
  - Función: Carga la dirección de un operando de memoria en un registro.
  - Ejemplo: `LEA BX, [SI+4]` (carga la dirección de DS:SI+4 en BX).
- **IN/OUT**:
  - Sintaxis: `IN destino, puerto`; `OUT puerto, origen`
  - Función: Transfiere datos desde/hacia puertos de E/S.
  - Ejemplo: `IN AL, 60h` (leer puerto del teclado); `OUT 61h, AL` (escribir al puerto del altavoz).

#### b. Instrucciones Aritméticas
Estas realizan operaciones matemáticas, actualizando flags (ej., ZF, CF, SF, OF) basándose en los resultados.

- **ADD (Sumar)**:
  - Sintaxis: `ADD destino, origen`
  - Función: Suma el origen al destino, almacena el resultado en el destino.
  - Ejemplo: `ADD AX, BX` (AX = AX + BX).
- **SUB (Restar)**:
  - Sintaxis: `SUB destino, origen`
  - Función: Resta el origen del destino.
  - Ejemplo: `SUB CX, 10` (CX = CX - 10).
- **INC (Incrementar)**:
  - Sintaxis: `INC destino`
  - Función: Incrementa el destino en 1.
  - Ejemplo: `INC BX` (BX = BX + 1).
- **DEC (Decrementar)**:
  - Sintaxis: `DEC destino`
  - Función: Decrementa el destino en 1.
  - Ejemplo: `DEC CX` (CX = CX - 1).
- **MUL (Multiplicar, Sin Signo)**:
  - Sintaxis: `MUL origen`
  - Función: Multiplica AL (8-bit) o AX (16-bit) por el origen, almacena el resultado en AX o DX:AX.
  - Ejemplo: `MUL BX` (DX:AX = AX * BX).
- **DIV (Dividir, Sin Signo)**:
  - Sintaxis: `DIV origen`
  - Función: Divide AX (8-bit) o DX:AX (16-bit) por el origen, almacena el cociente en AL/AX, el resto en AH/DX.
  - Ejemplo: `DIV BX` (AX = DX:AX / BX, DX = resto).
- **ADC (Sumar con Acarreo)** y **SBB (Restar con Préstamo)**:
  - Función: Manejan aritmética multi-palabra usando el flag de acarreo.
  - Ejemplo: `ADC AX, BX` (AX = AX + BX + CF).

#### c. Instrucciones Lógicas
Estas realizan operaciones bit a bit y manipulan datos binarios.

- **AND (AND bit a bit)**:
  - Sintaxis: `AND destino, origen`
  - Función: Realiza un AND bit a bit, almacena el resultado en el destino.
  - Ejemplo: `AND AX, 0FFh` (limpia el byte superior de AX).
- **OR (OR bit a bit)**:
  - Sintaxis: `OR destino, origen`
  - Función: Realiza un OR bit a bit.
  - Ejemplo: `OR BX, 1000h` (establece el bit 12 en BX).
- **XOR (XOR bit a bit)**:
  - Sintaxis: `XOR destino, origen`
  - Función: Realiza un XOR bit a bit.
  - Ejemplo: `XOR AX, AX` (pone AX a 0).
- **NOT (NOT bit a bit)**:
  - Sintaxis: `NOT destino`
  - Función: Invierte todos los bits en el destino.
  - Ejemplo: `NOT BX` (BX = ~BX).
- **SHL/SHR (Desplazar a la Izquierda/Derecha)**:
  - Sintaxis: `SHL destino, cuenta`; `SHR destino, cuenta`
  - Función: Desplaza bits a la izquierda/derecha, rellena con 0 (SHR) o bit de signo (SAL/SAR).
  - Ejemplo: `SHL AX, 1` (AX = AX * 2).
- **ROL/ROR (Rotar a la Izquierda/Derecha)**:
  - Función: Rota bits, envolviendo a través del flag de acarreo.
  - Ejemplo: `ROL BX, 1` (rota BX a la izquierda 1 bit).

#### d. Instrucciones de Control de Flujo
Estas alteran la secuencia de ejecución del programa, permitiendo saltos, bucles y subrutinas.

- **JMP (Salto)**:
  - Sintaxis: `JMP etiqueta`
  - Función: Salta incondicionalmente a una etiqueta.
  - Ejemplo: `JMP inicio` (ir a la etiqueta `inicio`).
  - Variantes:
    - Salto corto (±127 bytes).
    - Salto cercano (dentro del segmento).
    - Salto lejano (segmento diferente).
- **Saltos Condicionales**:
  - Sintaxis: `Jcc etiqueta` (ej., JZ, JNZ, JC, JNC)
  - Función: Salta basándose en el estado de los flags.
  - Ejemplos:
    - `JZ fin_bucle` (saltar si el flag de cero está establecido).
    - `JC error` (saltar si el flag de acarreo está establecido).
    - Condiciones comunes: JZ (cero), JNZ (no cero), JS (signo), JO (desbordamiento).
- **LOOP (Bucle)**:
  - Sintaxis: `LOOP etiqueta`
  - Función: Decrementa CX, salta a la etiqueta si CX ≠ 0.
  - Ejemplo: `LOOP procesar` (repetir hasta CX = 0).
  - Variantes:
    - `LOOPE/LOOPZ`: Bucle si CX ≠ 0 y ZF = 1.
    - `LOOPNE/LOOPNZ`: Bucle si CX ≠ 0 y ZF = 0.
- **CALL (Llamar a Subrutina)**:
  - Sintaxis: `CALL etiqueta`
  - Función: Empuja la dirección de retorno a la pila, salta a la subrutina.
  - Ejemplo: `CALL calcular_suma` (llamar a la subrutina).
- **RET (Retornar)**:
  - Sintaxis: `RET`
  - Función: Saca la dirección de retorno de la pila, reanuda la ejecución.
  - Ejemplo: `RET` (retornar de la subrutina).
- **INT (Interrupción)**:
  - Sintaxis: `INT número`
  - Función: Dispara una interrupción por software, llamando a una rutina de servicio de interrupción (ISR).
  - Ejemplo: `INT 21h` (llamada al sistema DOS).
- **IRET (Retorno de Interrupción)**:
  - Función: Retorna de una ISR, restaurando flags y dirección de retorno.

---

### 2. Programación en Lenguaje Ensamblador

Los programas en lenguaje ensamblador se escriben como instrucciones legibles por humanos que son ensambladas en código máquina. El 8086 utiliza un **modelo de memoria segmentado**, con segmentos de código, datos y pila definidos explícitamente.

#### a. Estructura del Programa
Un programa típico en ensamblador 8086 incluye:
- **Directivas**: Instrucciones para el ensamblador (ej., NASM, MASM).
  - `SEGMENT`: Define segmentos de código, datos o pila.
  - `ORG`: Establece la dirección de origen.
  - `DB/DW`: Define datos de byte/palabra.
- **Instrucciones**: Operaciones de la CPU (ej., MOV, ADD).
- **Etiquetas**: Marcan ubicaciones para saltos o datos.
- **Comentarios**: Explican el código (ej., `; comentario`).

**Ejemplo de Estructura de Programa (sintaxis MASM)**:
```asm
.model small
.stack 100h
.data
    mensaje db '¡Hola, Mundo!$'
.code
main proc
    mov ax, @data    ; Inicializar DS
    mov ds, ax
    mov dx, offset mensaje ; Cargar dirección del mensaje
    mov ah, 09h      ; Función DOS imprimir cadena
    int 21h          ; Llamar interrupción DOS
    mov ah, 4Ch      ; Salir del programa
    int 21h
main endp
end main
```

#### b. Estructuras Secuenciales
El código secuencial ejecuta instrucciones en orden, sin saltos ni bucles.

**Ejemplo: Sumar Dos Números**
```asm
mov ax, 5        ; AX = 5
mov bx, 10       ; BX = 10
add ax, bx       ; AX = AX + BX (15)
mov [resultado], ax ; Almacenar resultado en memoria
```
- Las instrucciones se ejecutan una tras otra.
- Común para cálculos simples o inicialización de datos.

#### c. Estructuras de Bifurcación
La bifurcación utiliza saltos condicionales/incondicionales para alterar el flujo del programa basándose en condiciones.

**Ejemplo: Comparar y Bifurcar**
```asm
mov ax, 10       ; AX = 10
cmp ax, 15       ; Comparar AX con 15
je igual         ; Saltar si AX == 15
mov bx, 1        ; Si no, BX = 1
jmp hecho
igual:
    mov bx, 0    ; BX = 0 si igual
hecho:
    ; Continuar programa
```
- **CMP**: Establece flags basándose en la resta (AX - 15).
- **JE**: Salta si ZF = 1 (igual).
- Útil para lógica if-then-else.

#### d. Estructuras de Bucle
Los bucles repiten instrucciones hasta que se cumple una condición, a menudo usando `LOOP` o saltos condicionales.

**Ejemplo: Sumar Números del 1 al 10**
```asm
mov cx, 10       ; Contador del bucle = 10
mov ax, 0        ; Suma = 0
bucle_suma:
    add ax, cx   ; Sumar CX a la suma
    loop bucle_suma ; Decrementar CX, bucle si CX ≠ 0
    ; AX = 55 (1 + 2 + ... + 10)
```
- `LOOP` simplifica la iteración basada en contador.
- Alternativa: Usar `CMP` y `JNZ` para condiciones personalizadas.

**Ejemplo con Bucle Condicional**
```asm
mov ax, 0        ; Contador
mov bx, 100      ; Límite
contar_arriba:
    inc ax       ; AX++
    cmp ax, bx   ; Comparar con 100
    jle contar_arriba ; Saltar si AX <= 100
```
- Flexible para bucles no basados en contador.

#### e. Subrutinas
Las subrutinas modularizan el código, permitiendo reutilización mediante `CALL` y `RET`.

**Ejemplo: Elevar un Número al Cuadrado**
```asm
main:
    mov ax, 4    ; Entrada
    call cuadrado ; Llamar subrutina
    ; AX = 16
    jmp salir
cuadrado:
    push bx      ; Guardar BX
    mov bx, ax   ; Copiar AX
    mul bx       ; AX = AX * BX
    pop bx       ; Restaurar BX
    ret          ; Retornar
salir:
    ; Fin del programa
```
- **PUSH/POP**: Guardar/restaurar registros para evitar efectos secundarios.
- La pila gestiona automáticamente las direcciones de retorno.

---

### 3. Rutinas de Servicio de Interrupciones (ISRs)

Las interrupciones permiten a la CPU responder a eventos externos o internos (ej., entrada del teclado, ticks del temporizador) pausando el programa actual y ejecutando una ISR.

#### Mecanismo de Interrupción
- **Tabla de Vectores de Interrupción (IVT)**:
  - Ubicada en memoria 0000:0000h–0000:03FFh.
  - Almacena direcciones de las ISRs para 256 tipos de interrupción (0–255).
  - Cada entrada: Segmento:Offset (4 bytes).
- **Tipos**:
  - **Interrupciones de Hardware**: Disparadas por dispositivos (ej., IRQ).
  - **Interrupciones de Software**: Disparadas por la instrucción `INT` (ej., INT 21h para DOS).
  - **Excepciones**: Errores de la CPU (ej., división por cero).
- **Proceso**:
  1. Ocurre una interrupción.
  2. La CPU guarda flags, CS e IP en la pila.
  3. Salta a la ISR a través de la IVT.
  4. La ISR ejecuta, termina con `IRET` para restaurar el estado.

#### Escribir una ISR
Las ISRs deben:
- Preservar registros (PUSH/POP).
- Manejar la interrupción rápidamente.
- Terminar con `IRET`.

**Ejemplo: ISR de Temporizador Personalizada**
```asm
.data
vec_ant dw 2 dup(0) ; Almacenar vector de interrupción antiguo
.code
instalar_isr:
    cli             ; Deshabilitar interrupciones
    mov ax, 0
    mov es, ax      ; ES = 0 (segmento IVT)
    mov bx, 1Ch*4   ; Interrupción de temporizador (1Ch)
    mov ax, es:[bx] ; Guardar vector antiguo
    mov vec_ant, ax
    mov ax, es:[bx+2]
    mov vec_ant+2, ax
    mov ax, offset mi_isr ; Establecer nuevo vector
    mov es:[bx], ax
    mov ax, cs
    mov es:[bx+2], ax
    sti             ; Habilitar interrupciones
    ret
mi_isr:
    push ax
    inc word ptr [contador] ; Incrementar contador
    pop ax
    iret            ; Retornar de la interrupción
```
- Engancha la interrupción del temporizador (1Ch, ~18.2 Hz).
- Incrementa una variable contador.
- Preserva registros y usa `IRET`.

**Ejemplo: Interrupción DOS (INT 21h)**
```asm
mov ah, 09h      ; Función imprimir cadena
mov dx, offset msg ; Dirección de la cadena terminada en '$'
int 21h          ; Llamar a DOS
```
- INT 21h proporciona servicios del SO (ej., E/S, manejo de archivos).
- AH especifica el código de función.

#### Notas Prácticas
- **Guardar Estado**: Las ISRs deben preservar todos los registros para evitar corromper el programa principal.
- **Prioridad**: Las interrupciones de hardware pueden preemptar a otras (gestionadas por el PIC).
- **Depuración**: Usar herramientas como DEBUG.COM o emuladores modernos (ej., DOSBox, Bochs).

---

### Programa Ejemplo: Cálculo de Factorial
Este programa calcula el factorial de un número (ej., 5! = 120) usando un bucle y una subrutina.

```asm
.model small
.stack 100h
.data
    num dw 5        ; Número de entrada
    resultado dw ?  ; Almacenar resultado
.code
main proc
    mov ax, @data
    mov ds, ax      ; Inicializar DS
    mov ax, num     ; Cargar número
    call factorial  ; Calcular factorial
    mov resultado, ax ; Almacenar resultado
    mov ah, 4Ch     ; Salir
    int 21h
main endp
factorial proc
    push bx
    mov bx, ax      ; BX = n
    mov ax, 1       ; AX = resultado
bucle_fact:
    cmp bx, 1
    jle hecho        ; Si BX <= 1, salir
    mul bx          ; AX = AX * BX
    dec bx          ; BX--
    jmp bucle_fact
hecho:
    pop bx
    ret
factorial endp
end main
```
- **Lógica**:
  - Entrada: num = 5.
  - Bucle: AX = AX * BX, BX-- hasta BX = 1.
  - Resultado: AX = 5 * 4 * 3 * 2 * 1 = 120.
- **Características**:
  - Subrutina para modularidad.
  - Pila para preservación de registros.
  - Estructuras secuenciales y de bucle.

---

### Mejores Prácticas
1. **Comentar el Código**: El ensamblador es críptico; explica cada paso.
2. **Minimizar el Uso de Registros**: Evitar sobrescrituras innecesarias.
3. **Probar Incrementalmente**: Usar depuradores para trazar la ejecución.
4. **Manejar Casos Límite**: Verificar desbordamiento, cero o entradas negativas.
5. **Optimizar**: Reducir instrucciones (ej., usar XOR AX, AX en lugar de MOV AX, 0).

---

### Resumen
- **Conjunto de Instrucciones del 8086**:
  - **Transferencia de Datos**: MOV, PUSH, POP para mover datos.
  - **Aritméticas**: ADD, SUB, MUL para cálculos.
  - **Lógicas**: AND, OR, XOR para manipulación de bits.
  - **Control de Flujo**: JMP, LOOP, CALL para el flujo del programa.
- **Estructuras de Programación**:
  - **Secuencial**: Ejecución lineal para tareas simples.
  - **Bifurcación**: Saltos condicionales para decisiones.
  - **Bucle**: LOOP o Jcc para repetición.
  - **Subrutinas**: CALL/RET para código modular.
- **Interrupciones**:
  - Las ISRs manejan eventos a través de la IVT.
  - Preservan el estado, terminan con IRET.
  - Usadas para interrupciones de hardware (ej., temporizador) y software (ej., DOS).

---

### Preguntas de Práctica
1. Escribe un programa para invertir una cadena en memoria.
2. Implementa una subrutina para verificar si un número es primo.
3. Crea una ISR para la interrupción del teclado (INT 09h) para contar pulsaciones de teclas.
4. Explica la diferencia entre `JMP` y `CALL`.
5. Optimiza este código: `MOV AX, 0; MOV BX, AX; ADD BX, 5`.

---

Este tutorial cubre los aspectos esenciales de la programación en ensamblador 8086, con ejemplos y explicaciones para construir habilidades prácticas. Si deseas explorar instrucciones específicas, técnicas avanzadas (ej., operaciones con cadenas) o herramientas de emulación, ¡avísame!