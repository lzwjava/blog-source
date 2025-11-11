---
audio: false
generated: true
lang: fr
layout: post
title: Fichiers de configuration XML pour les beans
translated: true
type: note
---

Pour répondre à votre question sur le fonctionnement du XML beans, y compris les propriétés de bean avec `props` et `keys`, quelle classe utilise ces fichiers XML et comment ils sont chargés, décomposons cela clairement et systématiquement. Cette explication suppose un contexte comme Spring, où "beans XML" est un terme courant pour la configuration des beans.

### Comment fonctionne le XML Beans ?

Dans des frameworks comme Spring, un **fichier XML beans** est un fichier de configuration utilisé pour définir et gérer des objets appelés *beans*. Ces beans sont typiquement des objets Java que le framework Spring instancie, configure et gère. Le fichier XML spécifie :

- **Beans** : Chaque bean est défini en utilisant une balise `<bean>`, qui inclut un `id` (un identifiant unique) et une `class` (le nom pleinement qualifié de la classe Java à instancier).
- **Propriétés** : Les beans peuvent avoir des propriétés, qui sont des valeurs ou des références définies dans le bean pour configurer son comportement. Les propriétés sont définies en utilisant la balise `<property>`.
- **Props et Keys** : Au sein d'une balise `<property>`, vous pouvez utiliser un élément `<props>` pour définir un ensemble de paires clé-valeur. Ceci est utile lorsqu'un bean attend un objet `java.util.Properties` ou une structure similaire comme une `Map`. L'élément `<props>` contient plusieurs balises `<prop>`, chacune avec un attribut `key` et une valeur correspondante.

Voici un exemple de ce à quoi cela ressemble dans un fichier XML beans :

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

Dans cet exemple :
- Un bean avec l'ID `myBean` est créé à partir de la classe `com.example.MyBean`.
- Le bean a une propriété nommée `someProperty`.
- L'élément `<props>` définit un ensemble de paires clé-valeur (`key1=value1` et `key2=value2`), que Spring convertit en un objet `Properties` et injecte dans `myBean` via une méthode setter comme `setSomeProperty(Properties props)`.

L'expression "it puts in resources" dans votre question est un peu floue, mais elle fait probablement référence au fichier XML étant une *ressource* (un fichier dans le classpath ou le système de fichiers de l'application) que l'application utilise, ou cela pourrait signifier que les beans définis dans le XML (comme une source de données) représentent des ressources utilisées par l'application. Pour l'instant, supposons qu'il s'agit du fichier XML lui-même étant une ressource chargée par l'application.

### Quelle classe utilisera ces fichiers XML ?

Dans Spring, la classe responsable de l'utilisation (c'est-à-dire du chargement et du traitement) du fichier XML beans est le **`ApplicationContext`**. Plus précisément, c'est une implémentation de l'interface `ApplicationContext`, telle que :

- **`ClassPathXmlApplicationContext`** : Charge le fichier XML depuis le classpath.
- **`FileSystemXmlApplicationContext`** : Charge le fichier XML depuis le système de fichiers.

Le `ApplicationContext` est l'interface centrale de Spring pour fournir des informations de configuration à une application. Il lit le fichier XML beans, l'analyse et utilise les définitions pour créer et gérer les beans. Bien que les beans eux-mêmes (par exemple, `com.example.MyBean`) utilisent les propriétés définies dans le XML, le `ApplicationContext` est la classe qui traite directement le fichier XML pour que cela se produise.

### Comment sera-t-il chargé ?

Le fichier XML beans est chargé dans l'application en créant une instance d'une implémentation d'`ApplicationContext` et en spécifiant l'emplacement du fichier XML. Voici comment cela fonctionne étape par étape :

1. **Spécifier l'emplacement du fichier XML** : Lorsque vous instanciez l'`ApplicationContext`, vous fournissez le nom ou le chemin du fichier XML. Par exemple :
   ```java
   ApplicationContext context = new ClassPathXmlApplicationContext("beans.xml");
   ```
   Ici, `"beans.xml"` est supposé être dans le classpath (par exemple, dans le répertoire `src/main/resources` dans un projet Java typique).

2. **Chargement en tant que ressource** : Le `ApplicationContext` utilise un `ResourceLoader` pour localiser et charger le fichier XML en tant que `Resource`. Dans ce cas, `ClassPathXmlApplicationContext` cherche le fichier dans le classpath.

3. **Analyse du XML** : En interne, Spring utilise un `XmlBeanDefinitionReader` pour analyser le fichier XML. Ce lecteur interprète les balises `<bean>`, les propriétés et les éléments `<props>`, créant des objets `BeanDefinition` qui décrivent comment chaque bean doit être construit.

4. **Création des beans** : Le `ApplicationContext` (qui étend le `BeanFactory` de Spring) utilise ces définitions de bean pour instancier les beans, définir leurs propriétés (y compris l'injection de l'objet `Properties` depuis `<props>`) et gérer leur cycle de vie.

Une fois chargé, vous pouvez récupérer les beans depuis l'`ApplicationContext` comme ceci :
```java
MyBean myBean = context.getBean("myBean", MyBean.class);
```

### Pour résumer

- **Comment fonctionne le XML Beans** : Le XML définit les beans et leurs propriétés, y compris les paires clé-valeur via `<props>`. Spring analyse ce XML pour configurer et instancier les beans.
- **Classe qui utilise le XML** : Le `ApplicationContext` (par exemple, `ClassPathXmlApplicationContext`) utilise le fichier XML pour configurer l'application.
- **Comment il est chargé** : Le XML est chargé en tant que ressource depuis le classpath ou le système de fichiers lorsque vous créez une instance d'`ApplicationContext`, en spécifiant l'emplacement du fichier.

Par exemple, si votre `beans.xml` est dans le classpath, vous le chargeriez avec :
```java
ApplicationContext context = new ClassPathXmlApplicationContext("beans.xml");
```
Spring gère ensuite le reste, rendant les beans configurés disponibles pour votre application.

Ce mécanisme est puissant et flexible, vous permettant de définir des configurations complexes en XML que Spring matérialise au moment de l'exécution.