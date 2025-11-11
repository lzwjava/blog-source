---
audio: false
generated: true
lang: de
layout: post
title: Instanziierungsausnahme
translated: true
type: note
---

Um den `java.lang.InstantiationException` in `LazyDynaBean.java` in Zeile 844 mit der Fehlermeldung "Error instantiating property of type" zu beheben, befolgen Sie diese Schritte. Diese Ausnahme tritt typischerweise auf, wenn die `LazyDynaBean` der Apache Commons BeanUtils-Bibliothek versucht, eine Instanz eines Eigenschaftstyps zu erstellen, dies jedoch fehlschlägt – höchstwahrscheinlich, weil es sich um eine abstrakte Klasse, eine Schnittstelle handelt oder ein öffentlicher parameterloser Konstruktor fehlt.

### Problemverständnis
`LazyDynaBean` ist eine dynamische Bean-Implementierung aus der Apache Commons BeanUtils-Bibliothek, die Eigenschaften bei Bedarf (lazy) initialisiert. Der Fehler deutet darauf hin, dass der Code in Zeile 844 von `LazyDynaBean.java` versucht, einen Eigenschaftstyp zu instanziieren (z.B. mit `Class.newInstance()`), der Vorgang jedoch fehlschlägt und eine `InstantiationException` auslöst. Häufige Ursachen sind:
- Der Eigenschaftstyp ist eine abstrakte Klasse oder Schnittstelle (z.B. `java.util.List` anstelle von `java.util.ArrayList`).
- Der Typ ist eine konkrete Klasse, aber es fehlt ein öffentlicher parameterloser Konstruktor, der von `newInstance()` benötigt wird.

### Schritte zur Problembehebung

#### 1. Identifizieren der problematischen Eigenschaft
- **Stack-Trace prüfen**: Der vollständige Stack-Trace oder die Fehlerprotokolle sollte anzeigen, welche Eigenschaft `LazyDynaBean` zu instanziieren versucht, wenn die Ausnahme auftritt. Wenn die Ausnahme beispielsweise während eines Aufrufs wie `dynaBean.get("someProperty")` ausgelöst wird, ist "someProperty" die Ursache.
- **Fehlermeldung prüfen**: Wenn die vollständige Fehlermeldung den Typ angibt (z.B. "Error instantiating property of type java.util.List"), notieren Sie den beteiligten Typ.

#### 2. Bestimmen des Eigenschaftstyps
- **`DynaClass`-Konfiguration prüfen**: `LazyDynaBean` verlässt sich auf eine `DynaClass` (oft eine `LazyDynaClass`), um ihre Eigenschaften und deren Typen zu definieren. Überprüfen Sie, wie die Eigenschaften definiert sind:
  - Wenn Sie explizit eine `LazyDynaClass` erstellt haben, suchen Sie im Code, wo Eigenschaften hinzugefügt werden, z.B. `dynaClass.add("propertyName", PropertyType.class)`.
  - Wenn `LazyDynaBean` ohne eine vordefinierte `DynaClass` erstellt wurde (z.B. `new LazyDynaBean()`), werden Eigenschaften dynamisch hinzugefügt, und der Typ kann vom ersten gesetzten Wert abgeleitet werden oder standardmäßig auf einen problematischen Typ gesetzt werden.
- **Debugging-Tipp**: Fügen Sie Logging hinzu oder verwenden Sie einen Debugger, um den Typ auszugeben, der von `dynaClass.getDynaProperty("propertyName").getType()` für die fehlerhafte Eigenschaft zurückgegeben wird.

#### 3. Sicherstellen, dass der Eigenschaftstyp instanziierbar ist
- **Konkrete Klasse verwenden**: Wenn der Typ eine abstrakte Klasse oder Schnittstelle ist (z.B. `List`, `Map` oder eine benutzerdefinierte Schnittstelle `MyInterface`), ersetzen Sie ihn durch eine konkrete Implementierung mit einem öffentlichen parameterlosen Konstruktor:
  - Für `List` verwenden Sie `ArrayList.class` anstelle von `List.class`.
  - Für `Map` verwenden Sie `HashMap.class` anstelle von `Map.class`.
  - Für eine benutzerdefinierte Schnittstelle oder abstrakte Klasse wählen Sie eine konkrete Unterklasse (z.B. `MyConcreteClass`, die `MyInterface` implementiert).
- **Beispiel**:
  ```java
  LazyDynaClass dynaClass = new LazyDynaClass();
  dynaClass.add("myList", ArrayList.class); // Konkrete Klasse
  LazyDynaBean dynaBean = new LazyDynaBean(dynaClass);
  ```

#### 4. Konfiguration anpassen
- **Eigenschaften vorab definieren**: Wenn Sie die `DynaClass` kontrollieren, definieren Sie Eigenschaften explizit mit konkreten Typen, bevor die Bean verwendet wird:
  ```java
  LazyDynaClass dynaClass = new LazyDynaClass();
  dynaClass.add("myProperty", MyConcreteClass.class);
  LazyDynaBean dynaBean = new LazyDynaBean(dynaClass);
  ```
- **Initialwerte setzen**: Alternativ können Sie eine anfängliche Instanz einer konkreten Klasse setzen, bevor auf die Eigenschaft zugegriffen wird, um zu verhindern, dass `LazyDynaBean` versucht, sie zu instanziieren:
  ```java
  LazyDynaBean dynaBean = new LazyDynaBean();
  dynaBean.set("myProperty", new ArrayList<>()); // Konkrete Instanz setzen
  Object value = dynaBean.get("myProperty"); // Keine Instanziierung nötig
  ```

#### 5. Dynamische Eigenschaftserstellung behandeln
- Wenn Eigenschaften dynamisch erstellt werden (häufig bei `LazyDynaBean`), stellen Sie sicher, dass der erste für eine Eigenschaft gesetzte Wert eine Instanz einer konkreten Klasse ist. Dies setzt den Typ korrekt:
  ```java
  LazyDynaBean dynaBean = new LazyDynaBean();
  dynaBean.set("myList", new ArrayList<>()); // Setzt den Typ auf ArrayList
  ```
- Vermeiden Sie den Zugriff auf undefinierte Eigenschaften, ohne sie zuvor zu setzen, da `LazyDynaBean` möglicherweise versucht, einen Standardtyp zu instanziieren, der problematisch sein könnte.

#### 6. Konstruktorzugriff überprüfen
- Bestätigen Sie, dass die konkrete Klasse einen öffentlichen parameterlosen Konstruktor hat. Zum Beispiel:
  ```java
  public class MyConcreteClass {
      public MyConcreteClass() {
          // Öffentlicher parameterloser Konstruktor
      }
  }
  ```
- Wenn der Klasse dieser fehlt, fügen Sie den Konstruktor hinzu oder verwenden Sie eine andere Klasse, die diese Anforderung erfüllt.

### Beispielhafte Korrektur
Angenommen, der Fehler tritt auf, weil eine Eigenschaft `"items"` als `java.util.List` typisiert ist, eine Schnittstelle:
- **Problematischer Code**:
  ```java
  LazyDynaClass dynaClass = new LazyDynaClass();
  dynaClass.add("items", List.class); // Schnittstelle, kann nicht instanziiert werden
  LazyDynaBean dynaBean = new LazyDynaBean(dynaClass);
  dynaBean.get("items"); // Löst InstantiationException aus
  ```
- **Korrigierter Code**:
  ```java
  LazyDynaClass dynaClass = new LazyDynaClass();
  dynaClass.add("items", ArrayList.class); // Konkrete Klasse
  LazyDynaBean dynaBean = new LazyDynaBean(dynaClass);
  dynaBean.get("items"); // Gibt eine neue ArrayList zurück
  ```

### Zusätzliche Überlegungen
- **Benutzerdefinierte Typen**: Wenn der Eigenschaftstyp eine benutzerdefinierte abstrakte Klasse oder Schnittstelle ist, stellen Sie eine konkrete Unterklasse bereit, die auf Ihre Anwendung zugeschnitten ist.
- **Bibliotheksversion**: Stellen Sie sicher, dass Sie eine kompatible Version von Apache Commons BeanUtils verwenden, obwohl dieses Problem in der Regel nutzungsbedingt und kein Bug ist.
- **Alternativer Ansatz**: Wenn die Anpassung von Typen unpraktisch ist, erwägen Sie, alle Eigenschaften vor der Verwendung mit konkreten Instanzen zu initialisieren, oder erkunden Sie `WrapDynaBean` zum Umschließen vorhandener Beans ohne Instanziierungsversuche.

### Endgültige Lösung
Um die `java.lang.InstantiationException` in `LazyDynaBean.java` Zeile 844 zu beheben:
1. Lokalisieren Sie die Eigenschaft, die den Fehler verursacht, über den Stack-Trace oder die Protokolle.
2. Überprüfen Sie ihren definierten Typ in der `DynaClass` oder ihren abgeleiteten Typ aus der Verwendung.
3. Ersetzen Sie jede abstrakte Klasse oder Schnittstelle durch eine konkrete Klasse (z.B. `ArrayList` für `List`), die einen öffentlichen parameterlosen Konstruktor hat.
4. Aktualisieren Sie die `DynaClass`-Definition oder setzen Sie eine anfängliche konkrete Instanz, um die automatische Instanziierung zu vermeiden.

Ohne den spezifischen Eigenschaftsnamen oder Typ aus der Fehlermeldung stellen Sie sicher, dass alle Eigenschaftstypen in Ihrer `LazyDynaBean`-Verwendung konkret und instanziierbar sind. Dies sollte die Ausnahme beseitigen.

---

Ich verstehe, dass Sie in Ihrer Filterklasse während der `init(FilterConfig filterConfig)`-Methode auf einen `java.lang.InstantiationException` stoßen und nach einer Lösung suchen. Dieser Fehler tritt typischerweise auf, wenn der Code versucht, eine Instanz einer Klasse zu erstellen, die nicht instanziiert werden kann, wie eine abstrakte Klasse oder Schnittstelle, oft verbunden mit der Verwendung von `LazyDynaBean` aus Apache Commons BeanUtils in Zeile 844. Da Sie erwähnt haben, dass Sie nur eine Filterklasse mit einer `init`-Methode haben, gehen wir das Schritt für Schritt durch, um das Problem zu lösen.

### Problemverständnis
In einer Java-Webanwendung wird die `init`-Methode eines Filters vom Servlet-Container aufgerufen, um den Filter unter Verwendung eines `FilterConfig`-Objekts zu initialisieren. Der Fehler deutet darauf hin, dass während dieser Initialisierung etwas (wahrscheinlich `LazyDynaBean`) versucht, einen Eigenschaftstyp zu instanziieren, der keine konkrete Klasse ist oder dem ein öffentlicher parameterloser Konstruktor fehlt. Da Sie `LazyDynaBean` verwenden (durch die Fehlermeldung impliziert), wird es wahrscheinlich dynamisch verwendet, um Eigenschaften zu handhaben, vielleicht aus den `FilterConfig`-Parametern, und eine dieser Eigenschaften verursacht die Ausnahme.

### Schritte zur Problembehebung

1. **Überprüfen Sie Ihre `init`-Methode**
   Beginnen Sie, indem Sie den Code in Ihrer `init(FilterConfig filterConfig)`-Methode untersuchen. Möglicherweise erstellen Sie eine `LazyDynaBean`, um Konfigurationsdaten zu speichern oder Initialisierungsparameter zu verarbeiten. Hier ist ein Beispiel, wie Ihr Code aussehen könnte:

   ```java
   import org.apache.commons.beanutils.LazyDynaBean;
   import javax.servlet.*;

   public class MyFilter implements Filter {
       private LazyDynaBean configBean;

       @Override
       public void init(FilterConfig filterConfig) throws ServletException {
           configBean = new LazyDynaBean();
           Enumeration<String> initParams = filterConfig.getInitParameterNames();
           while (initParams.hasMoreElements()) {
               String paramName = initParams.nextElement();
               String paramValue = filterConfig.getInitParameter(paramName);
               configBean.set(paramName, paramValue);
           }
           // Zugriff auf eine Eigenschaft, die die Instanziierung auslösen könnte
           Object someProperty = configBean.get("someProperty");
       }

       @Override
       public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
               throws IOException, ServletException {
           chain.doFilter(request, response);
       }

       @Override
       public void destroy() {}
   }
   ```

   In diesem Beispiel: Wenn `"someProperty"` nicht vorher mit einem Wert gesetzt wurde und ihr Typ abstrakt ist (z.B. `List` anstelle von `ArrayList`), wird `LazyDynaBean` versuchen, sie zu instanziieren und scheitern, was die `InstantiationException` verursacht.

2. **Identifizieren der problematischen Eigenschaft**
   Da der Fehler in `LazyDynaBean.java` in Zeile 844 auftritt, ist er wahrscheinlich mit einem `get`- oder `set`-Vorgang auf der `LazyDynaBean` verbunden. Um den Verursacher zu finden:
   - Fügen Sie Logging- oder Print-Anweisungen vor jedem `configBean.get()`- oder `configBean.set()`-Aufruf hinzu, um zu sehen, welche Eigenschaft die Ausnahme auslöst.
   - Beispiel:
     ```java
     System.out.println("Getting property: someProperty");
     Object someProperty = configBean.get("someProperty");
     ```

3. **Konkrete Typen oder Initialwerte sicherstellen**
   `LazyDynaBean` erstellt Eigenschaften lazy, aber wenn Sie auf eine Eigenschaft zugreifen, ohne sie zuvor zu setzen, versucht sie, ihren Typ zu instanziieren. Wenn dieser Typ abstrakt oder eine Schnittstelle ist (z.B. `List`, `Map`), wird eine `InstantiationException` ausgelöst. Um dies zu beheben:
   - **Initialwert setzen**: Stellen Sie eine konkrete Instanz bereit, bevor auf die Eigenschaft zugegriffen wird.
     ```java
     configBean.set("someProperty", new ArrayList<String>()); // Konkrete Klasse
     Object someProperty = configBean.get("someProperty");    // Jetzt sicher
     ```
   - **Konkreten Typ angeben**: Wenn Sie Eigenschaftstypen definieren, verwenden Sie konkrete Klassen.
     ```java
     configBean.setType("someProperty", ArrayList.class); // Nicht List.class
     ```

4. **Konstruktoren überprüfen**
   Wenn Sie eine Eigenschaft mit einer benutzerdefinierten Klasse setzen (z.B. `MyCustomClass`), stellen Sie sicher, dass sie einen öffentlichen parameterlosen Konstruktor hat:
   ```java
   public class MyCustomClass {
       public MyCustomClass() {} // Von LazyDynaBean benötigt
   }
   ```
   Verwenden Sie sie dann:
   ```java
   configBean.set("someProperty", new MyCustomClass());
   ```

5. **Vereinfachen, falls möglich**
   Wenn Sie `LazyDynaBean` nur zum Speichern von `FilterConfig`-Parametern verwenden, erwägen Sie, es ganz zu vermeiden und stattdessen eine `Map` oder direkten `FilterConfig`-Zugriff zu verwenden:
   ```java
   public class MyFilter implements Filter {
       private Map<String, String> configMap;

       @Override
       public void init(FilterConfig filterConfig) throws ServletException {
           configMap = new HashMap<>();
           Enumeration<String> initParams = filterConfig.getInitParameterNames();
           while (initParams.hasMoreElements()) {
               String paramName = initParams.nextElement();
               configMap.put(paramName, filterConfig.getInitParameter(paramName));
           }
       }
       // Andere Methoden...
   }
   ```
   Dies umgeht die Komplexitäten von `LazyDynaBean` vollständig.

### Endgültige Lösung
Hier ist eine korrigierte Version des Filters, unter der Annahme, dass `LazyDynaBean` notwendig ist:
```java
import org.apache.commons.beanutils.LazyDynaBean;
import javax.servlet.*;
import java.util.ArrayList;
import java.util.Enumeration;

public class MyFilter implements Filter {
    private LazyDynaBean configBean;

    @Override
    public void init(FilterConfig filterConfig) throws ServletException {
        configBean = new LazyDynaBean();
        Enumeration<String> initParams = filterConfig.getInitParameterNames();
        while (initParams.hasMoreElements()) {
            String paramName = initParams.nextElement();
            String paramValue = filterConfig.getInitParameter(paramName);
            configBean.set(paramName, paramValue); // String-Werte sicher setzen
        }
        // Setzen Sie alle Eigenschaften, die später abgerufen werden, vorab mit konkreten Typen
        if (configBean.get("someProperty") == null) {
            configBean.set("someProperty", new ArrayList<String>());
        }
        Object someProperty = configBean.get("someProperty"); // Jetzt sicher
    }

    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
            throws IOException, ServletException {
        chain.doFilter(request, response);
    }

    @Override
    public void destroy() {}
}
```

### Testen der Korrektur
- Stellen Sie den aktualisierten Filter in Ihrem Servlet-Container bereit (z.B. Tomcat).
- Überprüfen Sie die Protokolle, um sicherzustellen, dass die `InstantiationException` nicht mehr auftritt.
- Wenn sie weiterhin besteht, teilen Sie den vollständigen Stack-Trace oder weitere Codedetails mit, um weitere Unterstützung zu erhalten.

Dieser Ansatz stellt sicher, dass alle über `LazyDynaBean` abgerufenen Eigenschaften entweder mit konkreten Instanzen gesetzt oder vermieden werden, was die `InstantiationException` in der `init`-Methode Ihres Filters behebt.

---

Ich verstehe, dass Sie auf ein Problem stoßen, bei dem `LazyDynaBean` in einer Fehlermeldung auftaucht (insbesondere eine `java.lang.InstantiationException` in `LazyDynaBean.java:844`), obwohl Sie `LazyDynaBean` in Ihrem Code nie explizit erwähnen oder verwenden. Diese Situation tritt typischerweise auf, wenn eine Bibliothek oder ein Framework, die Sie verwenden, indirekt auf `LazyDynaBean` angewiesen ist. Lassen Sie uns das Schritt für Schritt aufschlüsseln und lösen.

### Warum ist `LazyDynaBean` beteiligt?
Da Sie nicht direkt auf `LazyDynaBean` verweisen, wird es wahrscheinlich von einer Abhängigkeit in Ihrem Projekt aufgerufen, wie z.B.:
- **Apache Commons BeanUtils**: Diese Bibliothek verwendet `LazyDynaBean` intern für dynamischen Eigenschaftszugriff oder Bean-Manipulation.
- **Spring Framework**: Wenn Ihr Code in Spring integriert ist (z.B. in einem Filter oder einer Bean-Konfiguration), könnte es BeanUtils oder ähnliche Utilities verwenden, die `LazyDynaBean` involvieren.
- **Andere Frameworks**: Jedes Tool, das mit dynamischen Eigenschaften, Konfigurationen oder Bean-Instanziierung zu tun hat, könnte der Verursacher sein.

Die `InstantiationException` deutet darauf hin, dass `LazyDynaBean` versucht, eine Instanz einer Klasse zu erstellen, aber scheitert, möglicherweise weil es auf eine abstrakte Klasse, Schnittstelle oder einen Typ ohne öffentlichen parameterlosen Konstruktor stößt.

### Wie das Problem behoben wird
Hier ist ein strukturierter Ansatz, um das Problem zu identifizieren und zu lösen:

#### 1. Stack-Trace prüfen
- Sehen Sie sich den vollständigen Stack-Trace der `InstantiationException` an. Er zeigt die Abfolge der Aufrufe, die zu `LazyDynaBean.java:844` führen.
- Identifizieren Sie die Bibliothek oder das Framework in Ihrem Code, das diesen Aufruf auslöst. Sie könnten beispielsweise Verweise auf `org.apache.commons.beanutils` oder `org.springframework.beans` sehen.

#### 2. Code und Abhängigkeiten überprüfen
- Überprüfen Sie Ihren Filter (oder die Klasse, in der der Fehler auftritt) auf Abhängigkeiten. Wenn es sich um einen Servlet-Filter handelt, prüfen Sie:
  - Die `init`-Methode.
  - Alle verwendeten Eigenschaften oder Beans.
  - Die in Ihrem Projekt importierten Bibliotheken (z.B. über Maven/Gradle).
- Häufige verdächtige Bibliotheken:
  - `commons-beanutils` (wird für dynamische Eigenschaftsbehandlung verwendet).
  - Spring oder andere Frameworks, die Beans verwalten.

#### 3. Konfiguration prüfen
- Wenn Ihr Filter über XML konfiguriert ist (z.B. in einer `web.xml` oder Spring-Kontextdatei), stellen Sie sicher, dass alle referenzierten Objekte korrekt definiert sind.
- Zum Beispiel, wenn eine Eigenschaft dynamisch gesetzt wird:
  ```xml
  <bean id="myFilter" class="com.example.MyFilter">
      <property name="someProperty" ref="someBean"/>
  </bean>
  ```
  Vergewissern Sie sich, dass `someBean` eine konkrete Klasse ist, wie:
  ```xml
  <bean id="someBean" class="com.example.ConcreteClass"/>
  ```

#### 4. Konkrete Typen sicherstellen
- Die Ausnahme tritt oft auf, wenn eine Bibliothek erwartet, einen Typ zu instanziieren, aber eine Schnittstelle oder abstrakte Klasse erhält (z.B. `List` anstelle von `ArrayList`).
- Wenn Sie Eigenschaften definieren, stellen Sie sicher, dass sie konkrete Implementierungen mit öffentlichen parameterlosen Konstruktoren verwenden:
  ```java
  private List<String> myList = new ArrayList<>(); // Gut
  private List<String> myList; // Riskant, wenn dynamisch gesetzt
  ```

#### 5. Das Problem debuggen
- Fügen Sie Logging hinzu oder verwenden Sie einen Debugger in der `init`-Methode Ihres Filters (oder wo immer der Fehler auftritt), um die exakte Zeile zu identifizieren, die die Ausnahme verursacht.
- Beispiel:
  ```java
  public class MyFilter implements Filter {
      private List<String> myList;

      public void setMyList(List<String> myList) {
          this.myList = myList;
      }

      @Override
      public void init(FilterConfig config) throws ServletException {
          System.out.println("Initializing filter...");
          if (myList == null) {
              myList = new ArrayList<>(); // Manuell initialisieren, falls nötig
          }
      }
  }
  ```

#### 6. Manuelle Initialisierung (falls nötig)
- Wenn die Bibliothek Eigenschaften dynamisch setzt und fehlschlägt, erwägen Sie, sie selbst zu initialisieren, um das Problem zu umgehen:
  ```java
  public class MyFilter implements Filter {
      private SomeClass myObject = new SomeClass(); // Konkrete Instanz

      @Override
      public void init(FilterConfig config) throws ServletException {
          // Filter-Initialisierungslogik
      }
  }
  ```

### Beispielszenario
Angenommen, Sie verwenden Springs `GenericFilterBean` und haben:
```xml
<bean id="myFilter" class="com.example.MyFilter">
    <property name="myList" ref="listBean"/>
</bean>
<bean id="listBean" class="java.util.List"/> <!-- Problem: Schnittstelle -->
```
Die Korrektur wäre:
```xml
<bean id="listBean" class="java.util.ArrayList"/> <!-- Konkrete Klasse -->
```

Oder im Code:
```java
public class MyFilter extends GenericFilterBean {
    private List<String> myList = new ArrayList<>(); // Standard konkrete Instanz

    public void setMyList(List<String> myList) {
        this.myList = myList;
    }
}
```

### Endgültige Schritte
- **Quelle identifizieren**: Eingrenzen, welche Bibliothek oder Konfiguration `LazyDynaBean` aufruft.
- **Konfigurationen korrigieren**: Sicherstellen, dass alle Typen konkret und instanziierbar sind.
- **Testen**: Erneut bereitstellen und überprüfen, ob die Ausnahme behoben ist.

Wenn das Problem weiterhin besteht, teilen Sie weitere Details mit (z.B. den Stack-Trace, Ihren Filtercode oder Abhängigkeiten), und ich kann eine spezifischere Lösung bereitstellen. Dieser Ansatz sollte Ihnen helfen, die `InstantiationException` zu beseitigen, ohne `LazyDynaBean` direkt handhaben zu müssen.