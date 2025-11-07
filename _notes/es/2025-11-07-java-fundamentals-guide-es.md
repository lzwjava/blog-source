---
audio: false
generated: true
image: false
lang: es
layout: post
model: anthropic/claude-4.5-sonnet
title: Guía de Estudio de Fundamentos de Programación Java
translated: true
---

## Examen Nacional de Educación Superior por Autodidacta

Esta guía cubre los conceptos fundamentales que necesitas dominar para la primera parte de tu curso de programación en Java.

---

## 1. Especificaciones del Lenguaje Java, API, JDK y Herramientas IDE

### **Especificaciones del Lenguaje Java**
La Especificación del Lenguaje Java define la sintaxis y semántica de Java. Conceptos clave a entender:

- **Independencia de Plataforma**: "Escribe Una Vez, Ejecuta en Cualquier Lugar" (WORA) - El código Java se compila a bytecode que se ejecuta en cualquier plataforma con una JVM (Java Virtual Machine)
- **Orientado a Objetos**: Todo en Java se organiza alrededor de objetos y clases
- **Fuertemente Tipado**: Las variables deben declararse con tipos de datos específicos
- **Gestión Automática de Memoria**: La recolección de basura maneja la liberación de memoria

### **API de Java (Application Programming Interface)**
La API de Java es una gran colección de clases preescritas organizadas en paquetes:

- **Paquetes principales**: `java.lang` (importado automáticamente), `java.util`, `java.io`
- **Propósito**: Proporciona funcionalidad lista para usar (colecciones, E/S de archivos, redes, etc.)
- **Documentación**: Disponible en el sitio oficial de documentación Java de Oracle
- **Cómo usarla**: Importa paquetes usando sentencias `import`

### **JDK (Java Development Kit)**
Componentes esenciales del JDK:

- **javac**: Compilador de Java (convierte archivos .java a archivos .class de bytecode)
- **java**: Lanzador del entorno de ejecución de Java
- **javadoc**: Generador de documentación
- **jar**: Herramienta de archivo Java
- **JRE incluido**: Entorno de Ejecución de Java para ejecutar programas
- **Librerías estándar**: Implementación completa de la API de Java

**Instalación y Configuración**:
- Descargar desde Oracle o usar OpenJDK
- Establecer la variable de entorno JAVA_HOME
- Agregar el directorio bin del JDK al PATH del sistema

### **Herramientas IDE (Integrated Development Environment)**
IDEs populares para el desarrollo en Java:

1. **Eclipse** - Gratuito, de código abierto, ampliamente usado en educación
2. **IntelliJ IDEA** - Características potentes, versiones gratuita y de pago
3. **NetBeans** - IDE oficial soportado por Oracle
4. **VS Code** - Ligero con extensiones para Java

**Beneficios del IDE**:
- Resaltado de sintaxis y detección de errores
- Autocompletado de código y sugerencias
- Herramientas de depuración integradas
- Gestión de proyectos
- Integración con control de versiones

---

## 2. Crear, Compilar y Ejecutar Programas Java

### **Estructura Básica de un Programa Java**

```java
// Cada aplicación Java necesita una clase principal
public class HolaMundo {
    // método main - punto de entrada del programa
    public static void main(String[] args) {
        // Tu código va aquí
        System.out.println("¡Hola, Mundo!");
    }
}
```

### **Proceso Paso a Paso**

**Paso 1: Crear un Programa Java**
- Crear un archivo de texto con extensión `.java`
- El NOMBRE del archivo DEBE coincidir con el nombre de la clase pública (sensible a mayúsculas)
- Ejemplo: `HolaMundo.java` para la clase `HolaMundo`

**Paso 2: Compilar**
```bash
javac HolaMundo.java
```
- Esto crea `HolaMundo.class` (archivo de bytecode)
- El compilador verifica errores de sintaxis
- Si existen errores, la compilación falla con mensajes de error

**Paso 3: Ejecutar**
```bash
java HolaMundo
```
- Nota: Usa el nombre de la clase SIN la extensión `.class`
- La JVM carga la clase y ejecuta el método main

### **Flujo de Trabajo: Línea de Comandos vs IDE**

**Línea de Comandos**:
- Abrir terminal/símbolo del sistema
- Navegar al directorio que contiene tu archivo .java
- Usar `javac` para compilar, `java` para ejecutar
- Bueno para entender el proceso subyacente

**Flujo de Trabajo en IDE**:
- Crear un nuevo proyecto Java
- Crear una nueva clase
- Escribir código en el editor
- Hacer clic en el botón "Ejecutar" (el IDE maneja la compilación automáticamente)
- Más conveniente para proyectos grandes

---

## 3. Guías de Estilo de Programación

Un buen estilo de programación hace que el código sea legible y mantenible. Sigue estas convenciones:

### **Convenciones de Nomenclatura**

- **Clases**: PascalCase (capitalizar la primera letra de cada palabra)
  - Ejemplos: `ExpedienteEstudiante`, `CuentaBancaria`, `HolaMundo`

- **Métodos y Variables**: camelCase (primera palabra en minúscula, capitalizar palabras subsiguientes)
  - Ejemplos: `calcularTotal()`, `primerNombre`, `edadEstudiante`

- **Constantes**: MAYÚSCULAS_CON_GUIONES_BAJOS
  - Ejemplos: `TAMAÑO_MÁXIMO`, `PI`, `VALOR_POR_DEFECTO`

- **Paquetes**: todo en minúsculas, a menudo nombre de dominio inverso
  - Ejemplos: `com.empresa.proyecto`, `java.util`

### **Formato del Código**

**Sangría**:
```java
public class Ejemplo {
    public static void main(String[] args) {
        if (condición) {
            // Sangría de 4 espacios o 1 tabulación
            sentencia;
        }
    }
}
```

**Llaves**:
- Llave de apertura en la misma línea (convención de Java)
- Llave de cierre en su propia línea, alineada con la sentencia

**Espaciado**:
```java
// Buen espaciado
int suma = a + b;
if (x > 0) {

// Espaciado deficiente
int suma=a+b;
if(x>0){
```

### **Comentarios**

**Comentarios de una línea**:
```java
// Este es un comentario de una línea
int edad = 20; // Comentario después del código
```

**Comentarios multi-línea**:
```java
/*
 * Este es un comentario multi-línea
 * Usado para explicaciones más largas
 */
```

**Comentarios Javadoc** (para documentación):
```java
/**
 * Calcula la suma de dos números.
 * @param a el primer número
 * @param b el segundo número
 * @return la suma de a y b
 */
public int sumar(int a, int b) {
    return a + b;
}
```

### **Mejores Prácticas**

1. **Nombres significativos**: Usa nombres descriptivos para variables y métodos
   - Bueno: `contadorEstudiantes`, `calcularPromedio()`
   - Malo: `x`, `hacerAlgo()`

2. **Una sentencia por línea**: Evita apretar múltiples sentencias en una línea

3. **Estilo consistente**: Sigue las mismas convenciones en todo tu código

4. **Espacio en blanco**: Usa líneas en blanco para separar secciones lógicas

5. **Mantén los métodos cortos**: Cada método debe hacer una cosa bien

---

## 4. Errores de Programación Comunes y Conceptos Básicos de Depuración

### **Tipos de Errores**

#### **A. Errores de Sintaxis (Errores de Tiempo de Compilación)**
Estos evitan la compilación y deben corregirse antes de ejecutar:

**Errores de sintaxis comunes**:
```java
// Punto y coma faltante
int x = 5  // ERROR: falta ;

// Llaves no coincidentes
public class Prueba {
    public static void main(String[] args) {
        System.out.println("Hola");
    // Falta llave de cierre }

// Sensibilidad a mayúsculas
String nombre = "Juan";
system.out.println(nombre); // ERROR: debería ser 'System'

// Nombre de archivo no coincide
// Archivo: Prueba.java
public class MiClase { // ERROR: el nombre de la clase debe coincidir con el nombre del archivo
```

#### **B. Errores de Tiempo de Ejecución**
El programa se compila pero se bloquea durante la ejecución:

```java
// División por cero
int resultado = 10 / 0; // ArithmeticException

// Puntero nulo
String str = null;
int longitud = str.length(); // NullPointerException

// Índice de array fuera de límites
int[] arr = {1, 2, 3};
int valor = arr[5]; // ArrayIndexOutOfBoundsException
```

#### **C. Errores Lógicos**
El programa se ejecuta pero produce resultados incorrectos:

```java
// Operador incorrecto
int promedio = (a + b) * 2; // Debería ser / no *

// Error por uno (Off-by-one)
for (int i = 0; i <= arr.length; i++) { // Debería ser i < arr.length

// Condición incorrecta
if (edad > 18) { // Debería ser >= para "18 años o más"
```

### **Técnicas de Depuración**

#### **1. Leer los Mensajes de Error Cuidadosamente**
```
HolaMundo.java:5: error: ';' expected
        int x = 5
                 ^
1 error
```
- **Número de línea**: Muestra dónde ocurrió el error (línea 5)
- **Tipo de error**: Te dice qué está mal (falta punto y coma)
- **Puntero**: Muestra la ubicación exacta

#### **2. Depuración con Sentencias de Impresión**
```java
public static int calcularSuma(int a, int b) {
    System.out.println("Depuración: a = " + a + ", b = " + b);
    int suma = a + b;
    System.out.println("Depuración: suma = " + suma);
    return suma;
}
```

#### **3. Usar el Depurador del IDE**
- **Puntos de interrupción**: Pausan la ejecución en líneas específicas
- **Paso por procedimiento**: Ejecuta la línea actual y pasa a la siguiente
- **Paso a paso**: Entra en las llamadas a métodos para ver la ejecución interna
- **Observar Variables**: Monitorea los valores de las variables en tiempo real
- **Pila de Llamadas**: Ve la secuencia de llamadas a métodos

#### **4. Divide y Vencerás**
- Comenta secciones del código para aislar el problema
- Prueba pequeñas partes independientemente
- Agrega gradualmente el código hasta que el error reaparezca

#### **5. Depuración con Pato de Goma**
- Explica tu código línea por línea a alguien (o algo)
- A menudo te ayuda a detectar el problema tú mismo

### **Errores Comunes de Principiantes**

1. **Olvidar compilar después de los cambios**
   - Siempre recompila antes de ejecutar

2. **El nombre de la clase no coincide con el nombre del archivo**
   - `public class Estudiante` debe estar en `Estudiante.java`

3. **Falta la firma del método main**
   - Debe ser exactamente: `public static void main(String[] args)`

4. **Olvidar importar paquetes**
   ```java
   import java.util.Scanner; // ¡No olvides esto!
   ```

5. **Capitalización incorrecta**
   - `String` no `string`, `System` no `system`

6. **Usar = en lugar de == en condiciones**
   ```java
   if (x = 5) { // ERROR: asignación, no comparación
   if (x == 5) { // CORRECTO
   ```

---

## Consejos para la Preparación del Examen

### **Qué Estudiar**

1. **Memorizar**:
   - Firma del método main
   - Estructura básica del programa
   - Convenciones de nomenclatura
   - Tipos de errores comunes

2. **Entender**:
   - Diferencia entre JDK, JRE y JVM
   - Proceso de compilación vs ejecución
   - Por qué Java es independiente de la plataforma

3. **Practicar**:
   - Escribir programas simples a mano
   - Identificar errores en muestras de código
   - Rastrear la ejecución del programa

### **Tipos Comunes de Preguntas en el Examen**

1. **Opción múltiple**: "¿Cuál es la firma correcta del método main?"
2. **Identificación de errores**: "Encuentra los errores de sintaxis en este código"
3. **Rastreo de código**: "¿Cuál es la salida de este programa?"
4. **Respuesta corta**: "Explica la diferencia entre JDK y JRE"
5. **Escritura de código**: "Escribe un programa que imprima '¡Hola, China!'"

### **Ejercicio de Práctica**

Intenta identificar y corregir todos los errores en este código:

```java
public class test {
    Public Static Void Main(string[] args) {
        int x = 5
        int y = 10;
        System.Out.Println(x + y)
    }
}
```

**Respuestas**:
- El nombre de la clase debería ser `Test` (T mayúscula) y coincidir con el nombre del archivo
- `Public` → `public`, `Static` → `static`, `Void` → `void`
- `string` → `String`
- Falta punto y coma después de `int x = 5`
- `System.Out` → `System.out`
- Falta punto y coma después de la sentencia println

---

## Lista de Verificación Resumen

Antes del examen, asegúrate de que puedes:

- ☐ Explicar qué son JDK, JRE, JVM y API
- ☐ Escribir un programa Java básico con estructura adecuada
- ☐ Compilar y ejecutar un programa usando la línea de comandos
- ☐ Seguir las convenciones de nomenclatura de Java
- ☐ Identificar errores de sintaxis, tiempo de ejecución y lógicos
- ☐ Usar técnicas básicas de depuración
- ☐ Escribir código correctamente formateado y comentado

¡Buena suerte con tu examen! 加油！