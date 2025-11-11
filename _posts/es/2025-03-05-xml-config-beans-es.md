---
audio: false
generated: true
lang: es
layout: post
title: Archivos de Configuración XML para Beans
translated: true
type: note
---

Para abordar tu consulta sobre cómo funciona el XML de beans, incluyendo las propiedades de los beans con props y keys, qué clase utiliza estos archivos XML y cómo se cargan, vamos a desglosarlo de forma clara y sistemática. Esta explicación asume un contexto como Spring, donde "beans XML" es un término común para configurar beans.

### ¿Cómo funciona el XML de Beans?

En frameworks como Spring, un **archivo XML de beans** es un archivo de configuración utilizado para definir y gestionar objetos llamados *beans*. Estos beans son típicamente objetos Java que el framework Spring instancia, configura y gestiona. El archivo XML especifica:

- **Beans**: Cada bean se define usando una etiqueta `<bean>`, que incluye un `id` (un identificador único) y un `class` (el nombre completo de la clase Java a instanciar).
- **Propiedades**: Los beans pueden tener propiedades, que son valores o referencias que se establecen en el bean para configurar su comportamiento. Las propiedades se definen usando la etiqueta `<property>`.
- **Props y Keys**: Dentro de una etiqueta `<property>`, puedes usar un elemento `<props>` para definir un conjunto de pares clave-valor. Esto es útil cuando un bean espera un objeto `java.util.Properties` o una estructura similar como un `Map`. El elemento `<props>` contiene múltiples etiquetas `<prop>`, cada una con un atributo `key` y un valor correspondiente.

Aquí tienes un ejemplo de cómo se ve esto en un archivo XML de beans:

```xml
<bean id="myBean" class="com.example.MyBean">
    <property name="someProperty">
        <props>
            <prop key="key1">value1</prop>
            <prop key="key2">value2</prop>
        </props>
    </property>
</bean>
```

En este ejemplo:
- Se crea un bean con el ID `myBean` a partir de la clase `com.example.MyBean`.
- El bean tiene una propiedad llamada `someProperty`.
- El elemento `<props>` define un conjunto de pares clave-valor (`key1=value1` y `key2=value2`), que Spring convierte en un objeto `Properties` y lo inyecta en `myBean` mediante un método setter como `setSomeProperty(Properties props)`.

La frase "it puts in resources" en tu consulta es un poco ambigua, pero probablemente se refiera a que el archivo XML es un *recurso* (un archivo en el classpath o sistema de archivos de la aplicación) que la aplicación utiliza, o podría significar que los beans definidos en el XML (como un origen de datos) representan recursos utilizados por la aplicación. Por ahora, asumamos que se trata del propio archivo XML siendo un recurso cargado por la aplicación.

### ¿Qué clase utilizará estos archivos XML?

En Spring, la clase responsable de utilizar (es decir, cargar y procesar) el archivo XML de beans es el **`ApplicationContext`**. Más precisamente, es una implementación de la interfaz `ApplicationContext`, como:

- **`ClassPathXmlApplicationContext`**: Carga el archivo XML desde el classpath.
- **`FileSystemXmlApplicationContext`**: Carga el archivo XML desde el sistema de archivos.

El `ApplicationContext` es la interfaz central de Spring para proporcionar información de configuración a una aplicación. Lee el archivo XML de beans, lo analiza y utiliza las definiciones para crear y gestionar los beans. Mientras que los beans mismos (por ejemplo, `com.example.MyBean`) utilizan las propiedades definidas en el XML, el `ApplicationContext` es la clase que procesa directamente el archivo XML para que esto suceda.

### ¿Cómo se cargará?

El archivo XML de beans se carga en la aplicación creando una instancia de una implementación de `ApplicationContext` y especificando la ubicación del archivo XML. Así es como funciona paso a paso:

1. **Especificar la Ubicación del Archivo XML**: Cuando instancias el `ApplicationContext`, proporcionas el nombre o la ruta del archivo XML. Por ejemplo:
   ```java
   ApplicationContext context = new ClassPathXmlApplicationContext("beans.xml");
   ```
   Aquí, `"beans.xml"` se asume que está en el classpath (por ejemplo, en el directorio `src/main/resources` en un proyecto Java típico).

2. **Carga como un Recurso**: El `ApplicationContext` utiliza un `ResourceLoader` para localizar y cargar el archivo XML como un `Resource`. En este caso, `ClassPathXmlApplicationContext` busca el archivo en el classpath.

3. **Análisis del XML**: Internamente, Spring utiliza un `XmlBeanDefinitionReader` para analizar el archivo XML. Este lector interpreta las etiquetas `<bean>`, las propiedades y los elementos `<props>`, creando objetos `BeanDefinition` que describen cómo debe construirse cada bean.

4. **Creación del Bean**: El `ApplicationContext` (que extiende la `BeanFactory` de Spring) utiliza estas definiciones de bean para instanciar los beans, establecer sus propiedades (incluyendo la inyección del objeto `Properties` desde `<props>`) y gestionar su ciclo de vida.

Una vez cargado, puedes recuperar beans del `ApplicationContext` así:
```java
MyBean myBean = context.getBean("myBean", MyBean.class);
```

### Resumiendo todo

- **Cómo funciona el XML de Beans**: El XML define los beans y sus propiedades, incluyendo pares clave-valor mediante `<props>`. Spring analiza este XML para configurar e instanciar los beans.
- **Clase que utiliza el XML**: El `ApplicationContext` (por ejemplo, `ClassPathXmlApplicationContext`) utiliza el archivo XML para configurar la aplicación.
- **Cómo se carga**: El XML se carga como un recurso desde el classpath o el sistema de archivos cuando creas una instancia de `ApplicationContext`, especificando la ubicación del archivo.

Por ejemplo, si tu `beans.xml` está en el classpath, lo cargarías con:
```java
ApplicationContext context = new ClassPathXmlApplicationContext("beans.xml");
```
Spring luego se encarga del resto, haciendo que los beans configurados estén disponibles para tu aplicación.

Este mecanismo es potente y flexible, permitiéndote definir configuraciones complejas en XML que Spring da vida en tiempo de ejecución.