---
audio: false
generated: true
lang: es
layout: post
title: Usando la biblioteca de colecciones de Scala en Java
translated: true
---

Para usar el paquete `scala.collection` en Java, puedes aprovechar la interoperabilidad entre Scala y Java, ya que ambos lenguajes se compilan a bytecode de JVM. Esto permite que el código Java llame a clases Scala, incluidas las del paquete `scala.collection`, siempre y cuando la biblioteca Scala esté accesible para tu proyecto Java. A continuación, se presenta una guía paso a paso para lograr esto, completa con explicaciones y ejemplos.

---

### **Paso 1: Incluir la Biblioteca Scala en tu Proyecto Java**
Dado que el paquete `scala.collection` es parte de la biblioteca estándar de Scala, necesitas incluir la biblioteca Scala en el classpath de tu proyecto Java. Esto se puede hacer agregando la dependencia de la biblioteca Scala a tu herramienta de construcción:

- **Maven**:
  Agrega lo siguiente a tu `pom.xml`:
  ```xml
  <dependency>
      <groupId>org.scala-lang</groupId>
      <artifactId>scala-library</artifactId>
      <version>2.13.12</version> <!-- Usa la versión que coincida con tus necesidades -->
  </dependency>
  ```

- **Gradle**:
  Agrega esto a tu `build.gradle`:
  ```gradle
  implementation 'org.scala-lang:scala-library:2.13.12'
  ```

Esto asegura que las clases Scala, incluidas las de `scala.collection`, estén disponibles para tu código Java.

---

### **Paso 2: Importar Clases de Colecciones Scala**
Una vez que la biblioteca Scala esté en tu classpath, puedes importar clases específicas del paquete `scala.collection` en tu código Java. Por ejemplo, para usar la lista inmutable de Scala, importarías:

```java
import scala.collection.immutable.List;
```

Otras colecciones comúnmente utilizadas incluyen:
- `scala.collection.immutable.Set`
- `scala.collection.immutable.Map`
- `scala.collection.mutable.Buffer`

Ten en cuenta que las colecciones de Scala vienen en variantes mutables e inmutables, a diferencia de las colecciones de Java, que son típicamente mutables a menos que se envuelvan (por ejemplo, mediante `Collections.unmodifiableList`).

---

### **Paso 3: Crear Colecciones Scala en Java**
Las colecciones de Scala se crean típicamente utilizando objetos acompañantes, que proporcionan métodos de fábrica como `apply`. Sin embargo, dado que Java no soporta la sintaxis de Scala directamente (por ejemplo, `List(1, 2, 3)`), necesitas trabajar con estos métodos de manera explícita. Además, el método `apply` de Scala para colecciones como `List` espera un `Seq` como argumento cuando se llama desde Java, debido a cómo se compilan los varargs de Scala.

Para conectar las colecciones de Java y Scala, usa las utilidades de conversión proporcionadas por Scala, como `scala.collection.JavaConverters` (para Scala 2.12 y versiones anteriores) o `scala.jdk.CollectionConverters` (para Scala 2.13 y versiones posteriores). Aquí está cómo crear una lista Scala a partir de una lista Java:

#### **Ejemplo: Crear una Lista Scala**
```java
import scala.collection.immutable.List;
import scala.collection.Seq;
import scala.jdk.CollectionConverters;
import java.util.Arrays;

public class ScalaCollectionExample {
    public static void main(String[] args) {
        // Crear una lista Java
        java.util.List<Integer> javaList = Arrays.asList(1, 2, 3);

        // Convertir la lista Java a Scala Seq
        Seq<Integer> scalaSeq = CollectionConverters.asScala(javaList);

        // Crear una lista Scala utilizando el objeto acompañante
        List<Integer> scalaList = List$.MODULE$.apply(scalaSeq);

        // Imprimir la lista Scala
        System.out.println(scalaList); // Salida: List(1, 2, 3)
    }
}
```

- **`CollectionConverters.asScala`**: Convierte una lista Java a un `Seq` de Scala (específicamente un `mutable.Buffer` en Scala 2.13, que es un subtipo de `Seq`).
- **`List$.MODULE$`**: Accede a la instancia singleton del objeto acompañante de `List` en Scala, permitiéndote llamar a su método `apply`.
- **`apply(scalaSeq)`**: Crea una nueva lista inmutable de Scala a partir del `Seq`.

---

### **Paso 4: Usar Colecciones Scala**
Una vez que tengas una colección Scala en Java, puedes usar sus métodos. Sin embargo, ten en cuenta las diferencias entre Scala y Java:
- **Inmutabilidad**: Muchas colecciones de Scala (por ejemplo, `scala.collection.immutable.List`) son inmutables, lo que significa que los métodos devuelven nuevas colecciones en lugar de modificar la original.
- **Borrado de Tipos**: Tanto Scala como Java usan el borrado de tipos, por lo que es posible que necesites hacer un cast al recuperar elementos.
- **Métodos Funcionales**: Las colecciones de Scala soportan operaciones funcionales como `map`, `filter`, etc., que puedes usar con lambdas de Java 8+.

#### **Ejemplo: Acceder a Elementos**
```java
// Obtener el primer elemento
Integer head = (Integer) scalaList.head();
System.out.println("Head: " + head); // Salida: Head: 1

// Obtener la cola (todo excepto la cabeza)
List<Integer> tail = scalaList.tail();
System.out.println("Tail: " + tail); // Salida: Tail: List(2, 3)
```

#### **Ejemplo: Mapear sobre una Lista Scala**
Usando una lambda para duplicar cada elemento:
```java
import scala.Function1;

Function1<Integer, Integer> doubler = x -> x * 2;
List<Integer> doubledList = scalaList.map(doubler);
System.out.println("Doubled: " + doubledList); // Salida: Doubled: List(2, 4, 6)
```

Aquí, `Function1` es una interfaz de Scala que representa una función con un argumento, que se alinea con la sintaxis de lambdas de Java.

---

### **Consideraciones Clave**
- **Seguridad de Tipos**: Las colecciones de Scala están parametrizadas, pero los tipos de retorno de los métodos pueden aparecer como `Object` en Java debido al borrado de tipos. Realiza los casts necesarios (por ejemplo, `(Integer) scalaList.head()`).
- **Rendimiento**: Cruzar la frontera Java-Scala introduce algún sobrecosto, aunque generalmente es menor.
- **Cambio de Paradigma**: Las colecciones de Scala enfatizan la inmutabilidad y la programación funcional, lo que puede diferir del estilo imperativo de Java. Por ejemplo, no puedes "agregar" a una lista inmutable `List`—en su lugar, creas una nueva (por ejemplo, usando `:+` para anexar, lo que devuelve una nueva `List`).
- **Compatibilidad de Versiones**: Asegúrate de que la versión de la biblioteca Scala coincida con tus necesidades. Para Scala 2.13+, usa `scala.jdk.CollectionConverters`; para 2.12 o versiones anteriores, usa `scala.collection.JavaConverters`.

---

### **Resumen**
Puedes usar el paquete `scala.collection` en Java:
1. Agregando la biblioteca Scala al classpath de tu proyecto (por ejemplo, mediante Maven o Gradle).
2. Importando las clases de colecciones Scala deseadas (por ejemplo, `scala.collection.immutable.List`).
3. Creando colecciones Scala utilizando objetos acompañantes (por ejemplo, `List$.MODULE$.apply`) y convirtiendo colecciones Java a `Seq` de Scala con `CollectionConverters`.
4. Manipulando las colecciones con métodos de Scala, usando casts y lambdas según sea necesario.

Este enfoque te permite aprovechar la poderosa biblioteca de colecciones de Scala en Java, como sus estructuras de datos inmutables o operaciones funcionales, mientras trabajas dentro del ecosistema de Java.