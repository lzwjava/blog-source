---
audio: false
generated: true
lang: es
layout: post
title: Programación Reactiva en Java
translated: true
type: note
---

Para usar **reactor-core**, una librería Java para construir aplicaciones asíncronas y no bloqueantes basadas en la especificación Reactive Streams, sigue estos pasos:

---

### 1. Agregar reactor-core como Dependencia
Primero, incluye **reactor-core** en tu proyecto. Dependiendo de tu herramienta de construcción:

- **Maven**: Añade esto a tu `pom.xml`:
  ```xml
  <dependency>
    <groupId>io.projectreactor</groupId>
    <artifactId>reactor-core</artifactId>
    <version>3.7.3</version>
  </dependency>
  ```

- **Gradle**: Añade esto a tu `build.gradle`:
  ```groovy
  implementation 'io.projectreactor:reactor-core:3.7.3'
  ```

Esto asegura que la librería esté disponible en tu proyecto. Verifica la última versión en [Maven Central](https://central.sonatype.com/artifact/io.projectreactor/reactor-core) si es necesario.

---

### 2. Comprender los Componentes Principales
Reactor-core proporciona dos clases principales para la programación reactiva:
- **`Flux`**: Representa un flujo asíncrono que puede emitir **de 0 a N elementos**.
- **`Mono`**: Representa un flujo asíncrono que emite **0 o 1 elemento**.

Estos son los bloques de construcción que usarás para manejar datos de forma reactiva.

---

### 3. Crear un Flux o Mono
Puedes crear instancias de `Flux` o `Mono` para representar tus flujos de datos.

- **Ejemplo con Flux** (múltiples elementos):
  ```java
  Flux<Integer> numbers = Flux.just(1, 2, 3, 4, 5);
  ```

- **Ejemplo con Mono** (un solo elemento):
  ```java
  Mono<String> greeting = Mono.just("Hello, World!");
  ```

El método `just` es una forma sencilla de crear un flujo a partir de valores estáticos, pero Reactor ofrece muchos otros métodos de creación (por ejemplo, desde arrays, rangos o fuentes personalizadas).

---

### 4. Suscribirse para Procesar los Datos
Para consumir los elementos emitidos, necesitas **suscribirte** al `Flux` o `Mono`. Suscribirse activa el flujo para que comience a emitir datos.

- **Suscribirse a Flux**:
  ```java
  numbers.subscribe(System.out::println);  // Imprime: 1, 2, 3, 4, 5
  ```

- **Suscribirse a Mono**:
  ```java
  greeting.subscribe(System.out::println); // Imprime: Hello, World!
  ```

El método `subscribe` también puede tomar argumentos adicionales, como manejadores de errores o callbacks de finalización, para un mayor control.

---

### 5. Transformar Datos con Operadores
Reactor proporciona un rico conjunto de operadores para manipular flujos, como `map`, `filter` y más.

- **Ejemplo con Flux y map**:
  ```java
  numbers.map(n -> n * 2).subscribe(System.out::println);  // Imprime: 2, 4, 6, 8, 10
  ```

- **Ejemplo con Mono y map**:
  ```java
  greeting.map(s -> s.toUpperCase()).subscribe(System.out::println); // Imprime: HELLO, WORLD!
  ```

Estos operadores te permiten transformar, filtrar o combinar datos de forma declarativa.

---

### 6. Manejar Errores y Backpressure
Reactor-core soporta el manejo de errores y la gestión de backpressure:
- **Manejo de Errores**: Usa `subscribe` con un consumidor de error:
  ```java
  Flux.error(new RuntimeException("Oops!"))
      .subscribe(System.out::println, error -> System.err.println(error.getMessage()));
  // Imprime: Oops!
  ```
- **Backpressure**: Controla cómo los suscriptores manejan flujos de datos abrumadores usando operadores como `onBackpressureBuffer()` o `onBackpressureDrop()`.

---

### 7. Explorar Más Allá
Para usos más avanzados:
- Consulta la [documentación oficial de Reactor](https://projectreactor.io/docs/core/release/reference/) para ver ejemplos detallados y tutoriales.
- Echa un vistazo al [repositorio de GitHub de reactor-core](https://github.com/reactor/reactor-core) para recursos adicionales.

---

### Resumen
Para usar **reactor-core**:
1. Agrégalo como dependencia en tu proyecto.
2. Usa `Flux` para múltiples elementos o `Mono` para un solo elemento.
3. Crea flujos con métodos como `just`.
4. Suscríbete para procesar los datos.
5. Aplica operadores para transformar los flujos según sea necesario.

Este es un punto de partida amigable para principiantes en la programación reactiva con reactor-core. ¡Experimenta con pequeños ejemplos para familiarizarte con su paradigma reactivo