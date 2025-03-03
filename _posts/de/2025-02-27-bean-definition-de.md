---
audio: false
lang: de
layout: post
title: BeanDefinitionStoreException
translated: true
---

Basierend auf dem von Ihnen bereitgestellten Fehler tritt in Ihrer Java-Anwendung, die auf IBM WebSphere mit OSGi-Unterstützung läuft, während der Initialisierung des Spring-Framework-Anwendungscontexts eine `BeanDefinitionStoreException` auf. Diese Ausnahme deutet auf eine "Ungültige Bean-Definition" hin, die typischerweise auf eine falsche Konfiguration in Ihrer Spring-Einrichtung zurückzuführen ist. Im Folgenden finden Sie eine umfassende Anleitung zur Fehlerbehebung und Behebung des Problems.

---

## Verständnis des Problems
Der Fehler zeigt:
- **Ausnahme**: `org.springframework.beans.factory.BeanDefinitionStoreException: Ungültige Bean-Definition`
- **Wichtige Komponenten**: Erwähnungen von `PlaceholderConfigurerSupport`, `PropertySourcesPlaceholderConfigurer` und `AbstractApplicationContext` im Stacktrace.
- **Kontext**: Der Fehler tritt während des `refresh`-Prozesses des Spring-Anwendungscontexts auf, der durch den `ContextLoader` in einer Webanwendungsumgebung auf WebSphere ausgelöst wird.
- **Ursache**: Wahrscheinlich im Zusammenhang mit unaufgelösten Eigenschafts-Placeholdern, ungültigen Bean-Definitionen oder bereitstellungsspezifischen Problemen in der WebSphere/OSGi-Umgebung.

Dies deutet darauf hin, dass Spring eine oder mehrere Beans aufgrund von Konfigurationsfehlern nicht ordnungsgemäß definieren oder initialisieren kann. Lassen Sie uns dies schrittweise lösen.

---

## Schritt-für-Schritt-Fix

### 1. Überprüfen Sie Eigenschafts-Placeholder
**Warum**: Der Stacktrace hebt `PlaceholderConfigurerSupport` und `PropertySourcesPlaceholderConfigurer` hervor, die die Eigenschaftsauflösung handhaben. Wenn eine Bean-Definition einen Platzhalter wie `${admin.email}` verwendet und dieser nicht definiert ist, wird Spring fehlschlagen.

**Wie man es repariert**:
- **Eigenschaftsdateien finden**: Stellen Sie sicher, dass Ihre `application.properties` oder `application.yml`-Datei im Klassenpfad (z. B. `src/main/resources`) vorhanden ist.
- **Eigenschaften überprüfen**: Öffnen Sie die Datei und bestätigen Sie, dass alle in Ihren Bean-Definitionen verwendeten Platzhalter definiert sind. Zum Beispiel:
  ```properties
  admin.email=admin@example.com
  ```
- **Tippfehler beheben**: Suchen Sie nach Tippfehlern in Eigenschaftsnamen oder Dateipfaden.
- **Konfigurationsaufbau**:
  - **XML**: Wenn XML verwendet wird, überprüfen Sie das `<context:property-placeholder>`-Tag:
    ```xml
    <context:property-placeholder location="classpath:application.properties"/>
    ```
  - **Java-Konfiguration**: Wenn `@Configuration` verwendet wird, stellen Sie sicher, dass `PropertySourcesPlaceholderConfigurer` konfiguriert ist:
    ```java
    @Bean
    public static PropertySourcesPlaceholderConfigurer propertySourcesPlaceholderConfigurer() {
        return new PropertySourcesPlaceholderConfigurer();
    }
    ```

### 2. Bean-Definitionen überprüfen
**Warum**: Die Meldung "Ungültige Bean-Definition" deutet auf ein Problem bei der Definition von Beans in Ihrer Spring-Konfiguration hin.

**Wie man es repariert**:
- **XML-Konfiguration**:
  - Öffnen Sie Ihre Spring-XML-Datei (z. B. `applicationContext.xml`) und überprüfen Sie:
    - Bean-IDs und Klassenamen sind korrekt und vorhanden im Klassenpfad.
    - Eigenschaften sind gültig und stimmen mit Setter-Methoden oder Konstruktorargumenten überein.
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
  - Stellen Sie sicher, dass Rückgabewerte und Methodennamen gültig sind.
- **Komponentenscanning**:
  - Wenn `@Component`, `@Service` usw. verwendet werden, bestätigen Sie, dass das Basis-Paket gescannt wird:
    ```java
    @ComponentScan("com.example")
    ```

### 3. Kreisförmige Abhängigkeiten auflösen
**Warum**: Wenn zwei Beans voneinander abhängen (z. B. benötigt Bean A Bean B und Bean B benötigt Bean A), kann Spring deren Initialisierung möglicherweise nicht durchführen.

**Wie man es repariert**:
- **Verwenden Sie `@Lazy`**:
  - Kennzeichnen Sie eine Abhängigkeit mit `@Lazy`, um deren Initialisierung zu verzögern:
    ```java
    @Autowired
    @Lazy
    private BeanB beanB;
    ```
- **Neugestaltung**: Entwerfen Sie Ihre Beans neu, um kreisförmige Verweise zu vermeiden, wenn möglich.

### 4. Abhängigkeiten und Klassenpfad überprüfen
**Warum**: Fehlende oder inkompatible Bibliotheken können dazu führen, dass in Bean-Definitionen referenzierte Klassen nicht verfügbar sind.

**Wie man es repariert**:
- **Maven/Gradle**:
  - Stellen Sie sicher, dass alle erforderlichen Spring-Abhängigkeiten in Ihrer `pom.xml` (Maven) oder `build.gradle` (Gradle) vorhanden sind. Beispiel für Maven:
    ```xml
    <dependency>
        <groupId>org.springframework</groupId>
        <artifactId>spring-context</artifactId>
        <version>5.3.23</version>
    </dependency>
    ```
  - Führen Sie `mvn dependency:tree` oder `gradle dependencies` aus, um Konflikte zu überprüfen.
- **Klassenpfad**: Stellen Sie sicher, dass alle Klassen (z. B. `com.example.MyClass`) kompiliert und in der bereitgestellten Anwendung verfügbar sind.

### 5. Debug-Logging aktivieren
**Warum**: Ausführlichere Protokolle können den genauen Bean oder die Eigenschaft, die zum Fehler führt, eingrenzen.

**Wie man es repariert**:
- Fügen Sie zu `application.properties` hinzu:
  ```properties
  logging.level.org.springframework=DEBUG
  ```
- Starten Sie die Anwendung neu und überprüfen Sie die Protokolle auf spezifische Fehler bei der Bean-Erstellung oder Eigenschaftsauflösung.

### 6. WebSphere/OSGi-Konfiguration überprüfen
**Warum**: Der Stacktrace zeigt WebSphere- und OSGi-Komponenten, die bereitstellungsspezifische Probleme einführen können.

**Wie man es repariert**:
- **Bundle-Auflösung**: Stellen Sie sicher, dass alle OSGi-Bundles korrekt bereitgestellt sind und ihre Abhängigkeiten in WebSphere aufgelöst sind.
- **Klassenpfad**: Überprüfen Sie, ob der WebSphere-Classloader Ihre Anwendungs-JARs und Eigenschaftsdateien enthält.
- **Serverprotokolle**: Überprüfen Sie die WebSphere-Protokolle (z. B. `SystemOut.log`) auf zusätzliche Fehler oder Warnungen.

### 7. Frühere Protokolle überprüfen
**Warum**: Der Protokollausschnitt beginnt mit einem erfolgreichen Eigenschaftsladen um 10:15:57, aber der Fehler tritt um 16:56:57 auf. Frühere Probleme könnten den Fehler ausgelöst haben.

**Wie man es repariert**:
- Blättern Sie im Protokolldatei nach oben oder überprüfen Sie archivierte Protokolle auf Warnungen oder Fehler vor der `BeanDefinitionStoreException`.

---

## Gängige Szenarien und Lösungen
- **Unaufgelöster Platzhalter**:
  - **Problem**: `${admin.email}` in einer Bean-Definition, aber nicht in `application.properties`.
  - **Fix**: Fügen Sie `admin.email=somevalue` zur Datei hinzu.
- **Fehlende Klasse**:
  - **Problem**: `<bean class="com.example.NonExistentClass">`
  - **Fix**: Korrigieren Sie den Klassenamen oder fügen Sie die fehlende Abhängigkeit hinzu.
- **Syntaxfehler**:
  - **Problem**: Fehlgebildetes XML oder Java-Konfiguration.
  - **Fix**: Validieren Sie mit einer IDE oder einem Tool wie `xmllint` für XML.

---

## Endschritte
1. **Fixes anwenden**: Beginnen Sie mit Eigenschafts-Placeholdern und Bean-Definitionen, da sie die wahrscheinlichsten Übeltäter basierend auf dem Stacktrace sind.
2. **Lokal testen**: Neu bereitstellen und in Ihrer Entwicklungsumgebung testen.
3. **Bereitstellen auf WebSphere**: Wenn es lokal funktioniert, neu bereitstellen auf WebSphere und die Protokolle überwachen.
4. **Iterieren**: Wenn der Fehler weiterhin besteht, verwenden Sie Debug-Protokolle, um den fehlenden Bean oder die Eigenschaft einzuschränken.

Durch die Befolgung dieser Schritte sollten Sie die `BeanDefinitionStoreException` beheben und Ihren Spring-Anwendungscontext erfolgreich initialisieren. Wenn das Problem weiterhin besteht, teilen Sie weitere spezifische Details (z. B. Konfigurationsdateien oder vollständige Protokolle) für weitere Unterstützung.