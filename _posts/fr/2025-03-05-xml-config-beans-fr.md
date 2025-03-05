---
audio: true
generated: true
lang: fr
layout: post
title: Fichiers de configuration XML pour les beans
translated: true
---

Pour répondre à votre question sur le fonctionnement des fichiers XML de beans, y compris les propriétés des beans avec les props et les clés, la classe qui utilise ces fichiers XML, et comment ils sont chargés, décomposons cela clairement et systématiquement. Cette explication suppose un contexte comme Spring, où "beans XML" est un terme courant pour configurer les beans.

### Comment fonctionne Beans XML ?

Dans des frameworks comme Spring, un **fichier XML de beans** est un fichier de configuration utilisé pour définir et gérer des objets appelés *beans*. Ces beans sont généralement des objets Java que le framework Spring instancie, configure et gère. Le fichier XML spécifie :

- **Beans** : Chaque bean est défini à l'aide d'une balise `<bean>`, qui inclut un `id` (un identifiant unique) et une `class` (le nom complet de la classe Java à instancier).
- **Propriétés** : Les beans peuvent avoir des propriétés, qui sont des valeurs ou des références définies dans le bean pour configurer son comportement. Les propriétés sont définies à l'aide de la balise `<property>`.
- **Props et Clés** : À l'intérieur d'une balise `<property>`, vous pouvez utiliser un élément `<props>` pour définir un ensemble de paires clé-valeur. Cela est utile lorsqu'un bean attend un objet `java.util.Properties` ou une structure similaire comme un `Map`. L'élément `<props>` contient plusieurs balises `<prop>`, chacune avec un attribut `key` et une valeur correspondante.

Voici à quoi cela ressemble dans un fichier XML de beans :

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

La phrase "il met en ressources" dans votre question est un peu floue, mais elle fait probablement référence au fichier XML étant une *ressource* (un fichier dans le classpath ou le système de fichiers de l'application) que l'application utilise, ou elle pourrait signifier que les beans définis dans le XML (comme une source de données) représentent des ressources utilisées par l'application. Pour l'instant, supposons qu'il s'agit du fichier XML lui-même étant une ressource chargée par l'application.

### Quelle Classe Utilisera Ces Fichiers XML ?

Dans Spring, la classe responsable de l'utilisation (c'est-à-dire le chargement et le traitement) du fichier XML de beans est le **`ApplicationContext`**. Plus précisément, il s'agit d'une implémentation de l'interface `ApplicationContext`, telle que :

- **`ClassPathXmlApplicationContext`** : Charge le fichier XML à partir du classpath.
- **`FileSystemXmlApplicationContext`** : Charge le fichier XML à partir du système de fichiers.

L'`ApplicationContext` est l'interface centrale de Spring pour fournir des informations de configuration à une application. Il lit le fichier XML de beans, le parse et utilise les définitions pour créer et gérer les beans. Bien que les beans eux-mêmes (par exemple, `com.example.MyBean`) utilisent les propriétés définies dans le XML, l'`ApplicationContext` est la classe qui traite directement le fichier XML pour que cela se produise.

### Comment Sera-t-il Chargé ?

Le fichier XML de beans est chargé dans l'application en créant une instance d'une implémentation de `ApplicationContext` et en spécifiant l'emplacement du fichier XML. Voici comment cela fonctionne étape par étape :

1. **Spécifier l'Emplacement du Fichier XML** : Lorsque vous instanciez l'`ApplicationContext`, vous fournissez le nom ou le chemin du fichier XML. Par exemple :
   ```java
   ApplicationContext context = new ClassPathXmlApplicationContext("beans.xml");
   ```
   Ici, `"beans.xml"` est supposé être dans le classpath (par exemple, dans le répertoire `src/main/resources` dans un projet Java typique).

2. **Chargement en tant que Ressource** : L'`ApplicationContext` utilise un `ResourceLoader` pour localiser et charger le fichier XML en tant que `Resource`. Dans ce cas, `ClassPathXmlApplicationContext` recherche le fichier dans le classpath.

3. **Analyse du XML** : En interne, Spring utilise un `XmlBeanDefinitionReader` pour analyser le fichier XML. Ce lecteur interprète les balises `<bean>`, les propriétés et les éléments `<props>`, créant des objets `BeanDefinition` qui décrivent comment chaque bean doit être construit.

4. **Création de Bean** : L'`ApplicationContext` (qui étend le `BeanFactory` de Spring) utilise ces définitions de beans pour instancier les beans, définir leurs propriétés (y compris l'injection de l'objet `Properties` à partir de `<props>`), et gérer leur cycle de vie.

Une fois chargé, vous pouvez récupérer des beans à partir de l'`ApplicationContext` comme ceci :
```java
MyBean myBean = context.getBean("myBean", MyBean.class);
```

### Tout Mettre Ensemble

- **Comment fonctionne Beans XML** : Le XML définit les beans et leurs propriétés, y compris les paires clé-valeur via `<props>`. Spring analyse ce XML pour configurer et instancier les beans.
- **Classe qui utilise le XML** : L'`ApplicationContext` (par exemple, `ClassPathXmlApplicationContext`) utilise le fichier XML pour configurer l'application.
- **Comment il est chargé** : Le XML est chargé en tant que ressource à partir du classpath ou du système de fichiers lorsque vous créez une instance d'`ApplicationContext`, en spécifiant l'emplacement du fichier.

Par exemple, si votre `beans.xml` est dans le classpath, vous le chargerez avec :
```java
ApplicationContext context = new ClassPathXmlApplicationContext("beans.xml");
```
Spring gère ensuite le reste, rendant les beans configurés disponibles pour votre application.

Ce mécanisme est puissant et flexible, permettant de définir des configurations complexes en XML que Spring met en œuvre à l'exécution.