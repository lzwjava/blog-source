---
audio: false
lang: de
layout: post
title: BeanDefinitionStoreException
translated: true
type: note
---

Basierend auf dem von Ihnen bereitgestellten Fehler tritt in Ihrer Java-Anwendung, die auf IBM WebSphere mit OSGi-Unterstützung läuft, eine `BeanDefinitionStoreException` während der Initialisierung des Spring Framework Application Context auf. Diese Exception weist auf eine "Ungültige Bean-Definition" hin, die typischerweise auf eine Fehlkonfiguration in Ihrem Spring-Setup zurückzuführen ist. Im Folgenden finden Sie eine umfassende Anleitung zur Fehlerbehebung und Lösung des Problems.

---

## Das Problem verstehen
Der Fehler zeigt:
- **Exception**: `org.springframework.beans.factory.BeanDefinitionStoreException: Ungültige Bean-Definition`
- **Schlüsselkomponenten**: Erwähnungen von `PlaceholderConfigurerSupport`, `PropertySourcesPlaceholderConfigurer` und `AbstractApplicationContext` im Stacktrace.
- **Kontext**: Der Fehler tritt während des `refresh`-Prozesses des Spring Application Context auf, ausgelöst durch den `ContextLoader` in einer Webanwendungsumgebung auf WebSphere.
- **Grundursache**: Wahrscheinlich im Zusammenhang mit nicht aufgelösten Property Placeholdern, ungültigen Bean-Definitionen oder deploymentspezifischen Problemen in der WebSphere/OSGi-Umgebung.

Dies deutet darauf hin, dass Spring eine oder mehrere Beans aufgrund von Konfigurationsfehlern nicht richtig definieren oder initialisieren kann. Lassen Sie uns dies Schritt für Schritt lösen.

---

## Schritt-für-Schritt-Lösung

### 1. Property Placeholder überprüfen
**Warum**: Der Stacktrace hebt `PlaceholderConfigurerSupport` und `PropertySourcesPlaceholderConfigurer` hervor, die für die Property-Auflösung zuständig sind. Wenn eine Bean-Definition einen Placeholder wie `${admin.email}` verwendet und dieser nicht definiert ist, schlägt Spring fehl.

**Lösung**:
- **Property-Dateien lokalisieren**: Stellen Sie sicher, dass Ihre `application.properties`- oder `application.yml`-Datei im Classpath liegt (z.B. `src/main/resources`).
- **Properties prüfen**: Öffnen Sie die Datei und bestätigen Sie, dass alle in Ihren Bean-Definitionen referenzierten Placeholder definiert sind. Zum Beispiel:
  ```properties
  admin.email=admin@example.com
  ```
- **Tippfehler korrigieren**: Suchen Sie nach Tippfehlern in Property-Namen oder Dateipfaden.
- **Konfiguration einrichten**:
  - **XML**: Wenn Sie XML verwenden, überprüfen Sie das `<context:property-placeholder>`-Tag:
    ```xml
    <context:property-placeholder location="classpath:application.properties"/>
    ```
  - **Java Config**: Wenn Sie `@Configuration` verwenden, stellen Sie sicher, dass `PropertySourcesPlaceholderConfigurer` konfiguriert ist:
    ```java
    @Bean
    public static PropertySourcesPlaceholderConfigurer propertySourcesPlaceholderConfigurer() {
        return new PropertySourcesPlaceholderConfigurer();
    }
    ```

### 2. Bean-Definitionen prüfen
**Warum**: Die Meldung "Ungültige Bean-Definition" weist auf ein Problem in der Definition Ihrer Beans in Ihrer Spring-Konfiguration hin.

**Lösung**:
- **XML-Konfiguration**:
  - Öffnen Sie Ihre Spring-XML-Datei (z.B. `applicationContext.xml`) und prüfen Sie:
    - Bean-IDs und Klassennamen sind korrekt und existieren im Classpath.
    - Properties sind gültig und entsprechen Setter-Methoden oder Konstruktorargumenten.
    - Beispiel einer korrekten Bean:
      ```xml
      <bean id="myBean" class="com.example.MyClass">
          <property name="email" value="${admin.email}"/>
      </bean>
      ```
  - Verwenden Sie eine IDE, um die XML-Syntax und das Schema zu validieren.
- **Java-Konfiguration**:
  - Überprüfen Sie `@Configuration`-Klassen auf `@Bean`-Methoden:
    ```java
    @Bean
    public MyClass myBean() {
        MyClass bean = new MyClass();
        bean.setEmail(env.getProperty("admin.email"));
        return bean;
    }
    ```
  - Stellen Sie sicher, dass Rückgabetypen und Methodennamen gültig sind.
- **Component Scanning**:
  - Wenn Sie `@Component`, `@Service` usw. verwenden, bestätigen Sie, dass das Basispaket gescannt wird:
    ```java
    @ComponentScan("com.example")
    ```

### 3. Zirkuläre Abhängigkeiten auflösen
**Warum**: Wenn zwei Beans voneinander abhängen (z.B. Bean A benötigt Bean B und Bean B benötigt Bean A), kann Spring sie möglicherweise nicht initialisieren.

**Lösung**:
- **Verwenden Sie `@Lazy`**:
  - Versehen Sie eine Abhängigkeit mit `@Lazy`, um deren Initialisierung zu verzögern:
    ```java
    @Autowired
    @Lazy
    private BeanB beanB;
    ```
- **Refaktorisieren**: Gestalten Sie Ihre Beans nach Möglichkeit so um, dass zirkuläre Referenzen vermieden werden.

### 4. Abhängigkeiten und Classpath prüfen
**Warum**: Fehlende oder inkompatible Bibliotheken können dazu führen, dass in Bean-Definitionen referenzierte Klassen nicht verfügbar sind.

**Lösung**:
- **Maven/Gradle**:
  - Stellen Sie sicher, dass alle erforderlichen Spring-Abhängigkeiten in Ihrer `pom.xml` (Maven) oder `build.gradle` (Gradle) vorhanden sind. Beispiel für Maven:
    ```xml
    <dependency>
        <groupId>org.springframework</groupId>
        <artifactId>spring-context</artifactId>
        <version>5.3.23</version>
    </dependency>
    ```
  - Führen Sie `mvn dependency:tree` oder `gradle dependencies` aus, um auf Konflikte zu prüfen.
- **Classpath**: Bestätigen Sie, dass alle Klassen (z.B. `com.example.MyClass`) kompiliert und in der deployed Anwendung verfügbar sind.

### 5. Debug-Logging aktivieren
**Warum**: Detailliertere Logs können die genaue Bean oder Property identifizieren, die den Fehler verursacht.

**Lösung**:
- Fügen Sie `application.properties` hinzu:
  ```properties
  logging.level.org.springframework=DEBUG
  ```
- Starten Sie die Anwendung neu und überprüfen Sie die Logs auf spezifische Fehler zur Bean-Erstellung oder Property-Auflösung.

### 6. WebSphere/OSGi-Konfiguration validieren
**Warum**: Der Stacktrace zeigt WebSphere- und OSGi-Komponenten, die deploymentspezifische Probleme verursachen können.

**Lösung**:
- **Bundle-Auflösung**: Stellen Sie sicher, dass alle OSGi-Bundles korrekt deployed sind und ihre Abhängigkeiten in WebSphere aufgelöst werden.
- **Classpath**: Vergewissern Sie sich, dass der Classloader von WebSphere die JARs und Property-Dateien Ihrer Anwendung enthält.
- **Server-Logs**: Überprüfen Sie die WebSphere-Logs (z.B. `SystemOut.log`) auf zusätzliche Fehler oder Warnungen.

### 7. Frühere Logs überprüfen
**Warum**: Der Log-Ausschnitt beginnt mit einem erfolgreichen Property-Load um 10:15:57, aber der Fehler tritt um 16:56:57 auf. Frühere Probleme könnten den Fehler ausgelöst haben.

**Lösung**:
- Scrollen Sie in der Log-Datei nach oben oder überprüfen Sie archivierte Logs auf Warnungen oder Fehler vor der `BeanDefinitionStoreException`.

---

## Häufige Szenarien und Lösungen
- **Nicht aufgelöster Placeholder**:
  - **Problem**: `${admin.email}` in einer Bean-Definition, aber nicht in `application.properties`.
  - **Lösung**: Fügen Sie `admin.email=somevalue` zur Datei hinzu.
- **Fehlende Klasse**:
  - **Problem**: `<bean class="com.example.NonExistentClass">`
  - **Lösung**: Korrigieren Sie den Klassennamen oder fügen Sie die fehlende Abhängigkeit hinzu.
- **Syntaxfehler**:
  - **Problem**: Fehlerhaftes XML oder Java-Konfiguration.
  - **Lösung**: Validieren Sie mit einer IDE oder einem Tool wie `xmllint` für XML.

---

## Letzte Schritte
1. **Lösungen anwenden**: Beginnen Sie mit Property Placeholdern und Bean-Definitionen, da sie basierend auf dem Stacktrace die wahrscheinlichsten Ursachen sind.
2. **Lokal testen**: Deployen und testen Sie in Ihrer Entwicklungsumgebung.
3. **Auf WebSphere deployen**: Wenn es lokal funktioniert, deployen Sie erneut auf WebSphere und überwachen Sie die Logs.
4. **Iterieren**: Wenn der Fehler weiterhin besteht, verwenden Sie Debug-Logs, um die fehlerhafte Bean oder Property einzugrenzen.

Indem Sie diese Schritte befolgen, sollten Sie die `BeanDefinitionStoreException` beheben und Ihren Spring Application Context erfolgreich initialisieren können. Wenn das Problem weiterhin besteht, teilen Sie bitte spezifischere Details (z.B. Konfigurationsdateien oder vollständige Logs) für weitere Unterstützung mit.