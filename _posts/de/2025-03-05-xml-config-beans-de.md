---
audio: false
generated: true
lang: de
layout: post
title: XML-Konfigurationsdateien für Beans
translated: true
type: note
---

Um Ihre Frage zu beantworten, wie Beans-XML funktioniert, einschließlich Bean-Eigenschaften mit Props und Keys, welche Klasse diese XML-Dateien verwendet und wie sie geladen werden, lassen Sie uns das klar und systematisch aufschlüsseln. Diese Erklärung geht von einem Kontext wie Spring aus, in dem "Beans XML" ein gängiger Begriff für die Konfiguration von Beans ist.

### Wie funktioniert Beans XML?

In Frameworks wie Spring ist eine **Beans-XML-Datei** eine Konfigurationsdatei, die verwendet wird, um Objekte, sogenannte *Beans*, zu definieren und zu verwalten. Diese Beans sind typischerweise Java-Objekte, die das Spring-Framework instanziiert, konfiguriert und verwaltet. Die XML-Datei gibt Folgendes an:

- **Beans**: Jede Bean wird mit einem `<bean>`-Tag definiert, das eine `id` (einen eindeutigen Bezeichner) und eine `class` (den vollqualifizierten Namen der zu instanziierenden Java-Klasse) enthält.
- **Eigenschaften**: Beans können Eigenschaften haben, also Werte oder Referenzen, die in die Bean gesetzt werden, um ihr Verhalten zu konfigurieren. Eigenschaften werden mit dem `<property>`-Tag definiert.
- **Props und Keys**: Innerhalb eines `<property>`-Tags können Sie ein `<props>`-Element verwenden, um eine Reihe von Schlüssel-Wert-Paaren zu definieren. Dies ist nützlich, wenn eine Bean ein `java.util.Properties`-Objekt oder eine ähnliche Struktur wie eine `Map` erwartet. Das `<props>`-Element enthält mehrere `<prop>`-Tags, jedes mit einem `key`-Attribut und einem entsprechenden Wert.

So sieht das in einer Beans-XML-Datei aus:

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

In diesem Beispiel:
- Eine Bean mit der ID `myBean` wird aus der Klasse `com.example.MyBean` erstellt.
- Die Bean hat eine Eigenschaft namens `someProperty`.
- Das `<props>`-Element definiert eine Reihe von Schlüssel-Wert-Paaren (`key1=value1` und `key2=value2`), die Spring in ein `Properties`-Objekt umwandelt und über eine Setter-Methode wie `setSomeProperty(Properties props)` in `myBean` injiziert.

Der Ausdruck "it puts in resources" in Ihrer Frage ist etwas unklar, aber er bezieht sich wahrscheinlich darauf, dass die XML-Datei eine *Ressource* ist (eine Datei im Classpath oder Dateisystem der Anwendung), die die Anwendung verwendet, oder es könnte bedeuten, dass die in der XML definierten Beans (wie eine Datenquelle) Ressourcen darstellen, die von der Anwendung verwendet werden. Nehmen wir vorerst an, es geht um die XML-Datei selbst, die als Ressource von der Anwendung geladen wird.

### Welche Klasse wird diese XML-Dateien verwenden?

In Spring ist die Klasse, die für die Verwendung (d.h. das Laden und Verarbeiten) der Beans-XML-Datei verantwortlich ist, der **`ApplicationContext`**. Genauer gesagt, ist es eine Implementierung der `ApplicationContext`-Schnittstelle, wie zum Beispiel:

- **`ClassPathXmlApplicationContext`**: Lädt die XML-Datei aus dem Classpath.
- **`FileSystemXmlApplicationContext`**: Lädt die XML-Datei aus dem Dateisystem.

Der `ApplicationContext` ist die zentrale Schnittstelle von Spring, um einer Anwendung Konfigurationsinformationen bereitzustellen. Er liest die Beans-XML-Datei, parsed sie und verwendet die Definitionen, um die Beans zu erstellen und zu verwalten. Während die Beans selbst (z.B. `com.example.MyBean`) die in der XML definierten Eigenschaften verwenden, ist der `ApplicationContext` die Klasse, die die XML-Datei direkt verarbeitet, um dies zu ermöglichen.

### Wie wird es geladen?

Die Beans-XML-Datei wird in die Anwendung geladen, indem eine Instanz einer `ApplicationContext`-Implementierung erstellt und der Speicherort der XML-Datei angegeben wird. So funktioniert es Schritt für Schritt:

1. **Speicherort der XML-Datei angeben**: Wenn Sie den `ApplicationContext` instanziieren, geben Sie den Namen oder Pfad der XML-Datei an. Zum Beispiel:
   ```java
   ApplicationContext context = new ClassPathXmlApplicationContext("beans.xml");
   ```
   Hier wird angenommen, dass `"beans.xml"` im Classpath liegt (z.B. im Verzeichnis `src/main/resources` in einem typischen Java-Projekt).

2. **Laden als Ressource**: Der `ApplicationContext` verwendet einen `ResourceLoader`, um die XML-Datei zu lokalisieren und als `Resource` zu laden. In diesem Fall sucht `ClassPathXmlApplicationContext` nach der Datei im Classpath.

3. **Parsen der XML**: Intern verwendet Spring einen `XmlBeanDefinitionReader`, um die XML-Datei zu parsen. Dieser Reader interpretiert die `<bean>`-Tags, Eigenschaften und `<props>`-Elemente und erstellt `BeanDefinition`-Objekte, die beschreiben, wie jede Bean erstellt werden soll.

4. **Bean-Erstellung**: Der `ApplicationContext` (der die `BeanFactory` von Spring erweitert) verwendet diese Bean-Definitionen, um die Beans zu instanziieren, ihre Eigenschaften zu setzen (einschließlich der Injektion des `Properties`-Objekts aus `<props>`) und ihren Lebenszyklus zu verwalten.

Sobald geladen, können Sie Beans wie folgt aus dem `ApplicationContext` abrufen:
```java
MyBean myBean = context.getBean("myBean", MyBean.class);
```

### Alles zusammengefasst

- **Wie Beans XML funktioniert**: Die XML definiert Beans und ihre Eigenschaften, einschließlich Schlüssel-Wert-Paaren über `<props>`. Spring parsed diese XML, um die Beans zu konfigurieren und zu instanziieren.
- **Klasse, die die XML verwendet**: Der `ApplicationContext` (z.B. `ClassPathXmlApplicationContext`) verwendet die XML-Datei, um die Anwendung einzurichten.
- **Wie sie geladen wird**: Die XML wird als Ressource aus dem Classpath oder Dateisystem geladen, wenn Sie eine `ApplicationContext`-Instanz erstellen und den Speicherort der Datei angeben.

Wenn sich Ihre `beans.xml` beispielsweise im Classpath befindet, würden Sie sie mit folgendem Code laden:
```java
ApplicationContext context = new ClassPathXmlApplicationContext("beans.xml");
```
Spring übernimmt dann den Rest und macht die konfigurierten Beans für Ihre Anwendung verfügbar.

Dieser Mechanismus ist leistungsstark und flexibel und ermöglicht es Ihnen, komplexe Konfigurationen in XML zu definieren, die Spring zur Laufzeit zum Leben erweckt.