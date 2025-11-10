---
audio: false
generated: true
lang: es
layout: post
title: Generación de Cadenas Aleatorias con Apache Commons Lang
translated: true
type: note
---

`RandomStringUtils` es una clase muy útil de la biblioteca Apache Commons Lang que proporciona varios métodos estáticos para generar cadenas aleatorias. Esto incluye generar cadenas con longitudes específicas, que contengan solo letras, solo números, caracteres alfanuméricos, o incluso a partir de un conjunto personalizado de caracteres.

Aquí se explica cómo usarla y la dependencia de Maven necesaria:

## Cómo usar `org.apache.commons.lang3.RandomStringUtils;`

Primero, necesitas importar la clase en tu archivo Java:

```java
import org.apache.commons.lang3.RandomStringUtils;
```

Luego puedes usar sus métodos estáticos. Aquí hay algunos ejemplos comunes:

1.  **Generar una cadena alfanumérica aleatoria de una longitud específica:**

    ```java
    String randomAlphaNumeric = RandomStringUtils.randomAlphanumeric(10);
    System.out.println("Alfanumérico aleatorio: " + randomAlphaNumeric); // ej., "aB5cY2x9Pq"
    ```

2.  **Generar una cadena alfabética aleatoria de una longitud específica:**

    ```java
    String randomAlphabetic = RandomStringUtils.randomAlphabetic(8);
    System.out.println("Alfabético aleatorio: " + randomAlphabetic); // ej., "GhJkLmNo"
    ```

3.  **Generar una cadena numérica aleatoria de una longitud específica:**

    ```java
    String randomNumeric = RandomStringUtils.randomNumeric(6);
    System.out.println("Numérico aleatorio: " + randomNumeric); // ej., "123456"
    ```

4.  **Generar una cadena aleatoria con una mezcla de letras y números, especificando banderas:**

    ```java
    String randomLettersAndNumbers = RandomStringUtils.random(12, true, true);
    System.out.println("Letras y números aleatorios: " + randomLettersAndNumbers); // ej., "abC123DeF456"
    ```

5.  **Generar una cadena aleatoria a partir de un conjunto personalizado de caracteres:**

    ```java
    String chars = "abcdefg";
    String randomFromCustomSet = RandomStringUtils.random(5, chars);
    System.out.println("Aleatorio de conjunto personalizado: " + randomFromCustomSet); // ej., "gcfae"
    ```

## Qué biblioteca usar en `pom.xml`

Para usar `RandomStringUtils` en un proyecto Maven, necesitas agregar la dependencia `commons-lang3` a tu archivo `pom.xml`.

Aquí está el fragmento de la dependencia:

```xml
<dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-lang3</artifactId>
    <version>3.14.0</version> </dependency>
```

**Notas importantes:**

  * **Versión:** Siempre verifica en [Maven Central](https://mvnrepository.com/artifact/org.apache.commons/commons-lang3) la última versión estable de `commons-lang3`. Según mi última actualización, `3.14.0` o superior es una buena opción, pero siempre es mejor usar la última versión estable disponible absoluta.
  * **Alcance:** El alcance predeterminado para las dependencias es `compile`, que normalmente es lo que quieres para bibliotecas de utilidad como esta. Significa que el JAR estará disponible durante la compilación, las pruebas y el tiempo de ejecución. Si solo lo usaras para pruebas, podrías usar `<scope>test</scope>`.
  * **Desuso:** Ten en cuenta que algunos métodos antiguos como `RandomStringUtils.randomAlphabetic(int count)` están en desuso en versiones más nuevas de Apache Commons Lang 3. En su lugar, se recomienda usar los métodos `secure()`, `secureStrong()` o `insecure()`, que proporcionan más control sobre la fuente de aleatoriedad. Por ejemplo, `RandomStringUtils.secure().nextAlphanumeric(10)`. Sin embargo, los métodos más antiguos aún funcionan para muchos casos de uso.