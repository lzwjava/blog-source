---
audio: false
generated: true
lang: de
layout: post
title: XML-Konfigurationsdateien für Beans
translated: true
---

Um Ihre Anfrage zu beantworten, wie beans XML funktioniert, einschließlich Bean-Eigenschaften mit props und keys, welche Klasse diese XML-Dateien verwendet und wie sie geladen werden, lassen Sie uns das klar und systematisch aufschlüsseln. Diese Erklärung setzt einen Kontext wie Spring voraus, in dem "beans XML" ein gängiger Begriff für die Konfiguration von Beans ist.

### Wie funktioniert Beans XML?

In Frameworks wie Spring ist eine **beans XML-Datei** eine Konfigurationsdatei, die verwendet wird, um Objekte zu definieren und zu verwalten, die als *Beans* bezeichnet werden. Diese Beans sind typischerweise Java-Objekte, die das Spring-Framework instanziiert, konfiguriert und verwaltet. Die XML-Datei spezifiziert:

- **Beans**: Jedes Bean wird mit einem `<bean>`-Tag definiert, das eine `id` (ein eindeutiger Bezeichner) und eine `class` (der vollständig qualifizierte Name der zu instanziierenden Java-Klasse) enthält.
- **Eigenschaften**: Beans können Eigenschaften haben, die Werte oder Verweise sind, die in das Bean gesetzt werden, um dessen Verhalten zu konfigurieren. Eigenschaften werden mit dem `<property>`-Tag definiert.
- **Props und Keys**: Innerhalb eines `<property>`-Tags können Sie ein `<props>`-Element verwenden, um einen Satz von Schlüssel-Wert-Paaren zu definieren. Dies ist nützlich, wenn ein Bean ein `java.util.Properties`-Objekt oder eine ähnliche Struktur wie ein `Map` erwartet. Das `<props>`-Element enthält mehrere `<prop>`-Tags, jedes mit einem `key`-Attribut und einem entsprechenden Wert.

Hier ist ein Beispiel, wie dies in einer beans XML-Datei aussieht:

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
- Ein Bean mit der ID `myBean` wird aus der Klasse `com.example.MyBean` erstellt.
- Das Bean hat eine Eigenschaft namens `someProperty`.
- Das `<props>`-Element definiert einen Satz von Schlüssel-Wert-Paaren (`key1=value1` und `key2=value2`), die Spring in ein `Properties`-Objekt umwandelt und über eine Setter-Methode wie `setSomeProperty(Properties props)` in `myBean` injiziert.

Der Begriff "es setzt Ressourcen ein" in Ihrer Anfrage ist etwas unklar, aber er bezieht sich wahrscheinlich darauf, dass die XML-Datei eine *Ressource* (eine Datei im Klassenspeicher oder Dateisystem) ist, die die Anwendung verwendet, oder es könnte bedeuten, dass die in der XML definierten Beans (wie eine Datenquelle) Ressourcen darstellen, die von der Anwendung verwendet werden. Vorerst gehen wir davon aus, dass es sich um die XML-Datei selbst handelt, die als Ressource von der Anwendung geladen wird.

### Welche Klasse verwendet diese XML-Dateien?

In Spring ist die Klasse, die für die Verwendung (d.h. das Laden und Verarbeiten) der beans XML-Datei verantwortlich ist, der **`ApplicationContext`**. Genauer gesagt handelt es sich um eine Implementierung der `ApplicationContext`-Schnittstelle, wie:

- **`ClassPathXmlApplicationContext`**: Lädt die XML-Datei aus dem Klassenspeicher.
- **`FileSystemXmlApplicationContext`**: Lädt die XML-Datei aus dem Dateisystem.

Der `ApplicationContext` ist die zentrale Schnittstelle von Spring zur Bereitstellung von Konfigurationsinformationen für eine Anwendung. Er liest die beans XML-Datei, parst sie und verwendet die Definitionen, um die Beans zu erstellen und zu verwalten. Während die Beans selbst (z.B. `com.example.MyBean`) die in der XML definierten Eigenschaften verwenden, ist der `ApplicationContext` die Klasse, die die XML-Datei direkt verarbeitet, um dies zu ermöglichen.

### Wie wird es geladen?

Die beans XML-Datei wird in die Anwendung geladen, indem eine Instanz einer `ApplicationContext`-Implementierung erstellt und der Speicherort der XML-Datei angegeben wird. Hier ist, wie es Schritt für Schritt funktioniert:

1. **XML-Datei-Speicherort angeben**: Wenn Sie den `ApplicationContext` instanziieren, geben Sie den Namen oder Pfad der XML-Datei an. Zum Beispiel:
   ```java
   ApplicationContext context = new ClassPathXmlApplicationContext("beans.xml");
   ```
   Hier wird angenommen, dass `"beans.xml"` sich im Klassenspeicher befindet (z.B. im `src/main/resources`-Verzeichnis in einem typischen Java-Projekt).

2. **Laden als Ressource**: Der `ApplicationContext` verwendet einen `ResourceLoader`, um die XML-Datei als `Resource` zu finden und zu laden. In diesem Fall sucht `ClassPathXmlApplicationContext` die Datei im Klassenspeicher.

3. **XML-Datei parsen**: Intern verwendet Spring einen `XmlBeanDefinitionReader`, um die XML-Datei zu parsen. Dieser Reader interpretiert die `<bean>`-Tags, Eigenschaften und `<props>`-Elemente und erstellt `BeanDefinition`-Objekte, die beschreiben, wie jedes Bean konstruiert werden soll.

4. **Bean-Erstellung**: Der `ApplicationContext` (der Spring’s `BeanFactory` erweitert) verwendet diese Bean-Definitionen, um die Beans zu instanziieren, ihre Eigenschaften (einschließlich der Injektion des `Properties`-Objekts aus `<props>`) zu setzen und ihren Lebenszyklus zu verwalten.

Sobald geladen, können Sie Beans aus dem `ApplicationContext` wie folgt abrufen:
```java
MyBean myBean = context.getBean("myBean", MyBean.class);
```

### Alles zusammenfassen

- **Wie Beans XML funktioniert**: Die XML definiert Beans und deren Eigenschaften, einschließlich Schlüssel-Wert-Paaren über `<props>`. Spring parst diese XML, um die Beans zu konfigurieren und zu instanziieren.
- **Klasse, die die XML verwendet**: Der `ApplicationContext` (z.B. `ClassPathXmlApplicationContext`) verwendet die XML-Datei, um die Anwendung einzurichten.
- **Wie es geladen wird**: Die XML wird als Ressource aus dem Klassenspeicher oder Dateisystem geladen, wenn Sie eine `ApplicationContext`-Instanz erstellen und den Dateispeicherort angeben.

Zum Beispiel, wenn Ihre `beans.xml` sich im Klassenspeicher befindet, laden Sie sie mit:
```java
ApplicationContext context = new ClassPathXmlApplicationContext("beans.xml");
```
Spring erledigt den Rest und stellt die konfigurierten Beans Ihrer Anwendung zur Verfügung.

Dieser Mechanismus ist leistungsstark und flexibel und ermöglicht es Ihnen, komplexe Konfigurationen in XML zu definieren, die Spring zur Laufzeit zum Leben erweckt.