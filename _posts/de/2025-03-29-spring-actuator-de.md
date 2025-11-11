---
audio: false
generated: true
lang: de
layout: post
title: Spring Actuator
translated: true
type: note
---

Spring Actuator ist eine leistungsstarke Funktion in Spring Boot, die produktionsreife Tools zur Überwachung und Verwaltung Ihrer Anwendung bereitstellt. Hier ist eine Schritt-für-Schritt-Anleitung zur Verwendung:

### 1. **Spring Actuator Abhängigkeit hinzufügen**
Um Spring Actuator zu verwenden, müssen Sie dessen Abhängigkeit in Ihr Projekt aufnehmen. Wenn Sie Maven verwenden, fügen Sie dies zu Ihrer `pom.xml` hinzu:

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-actuator</artifactId>
</dependency>
```

Für Gradle fügen Sie dies zu Ihrer `build.gradle` hinzu:

```gradle
implementation 'org.springframework.boot:spring-boot-starter-actuator'
```

### 2. **Starten Sie Ihre Spring Boot Anwendung**
Sobald die Abhängigkeit hinzugefügt wurde, starten Sie Ihre Spring Boot Anwendung. Spring Actuator aktiviert automatisch eine Reihe von Endpunkten, die Sie zur Überwachung und Interaktion mit Ihrer App verwenden können.

### 3. **Auf Standard-Endpunkte zugreifen**
Spring Actuator macht standardmäßig mehrere Endpunkte über HTTP verfügbar. Der Basispfad ist `/actuator`. Hier sind einige häufig verwendete (angenommen, Ihre App läuft auf `localhost:8080`):
- **Health Check**: `http://localhost:8080/actuator/health`
  - Gibt den Status Ihrer Anwendung zurück (z.B. `{"status":"UP"}`).
- **Anwendungsinfo**: `http://localhost:8080/actuator/info`
  - Zeigt beliebige Anwendungsinformationen an (konfigurierbar).
- **Metriken**: `http://localhost:8080/actuator/metrics`
  - Bietet detaillierte Metriken wie Speichernutzung, CPU und mehr.

Standardmäßig sind aus Sicherheitsgründen nur `/health` und `/info` aktiviert. Um weitere Endpunkte verfügbar zu machen, müssen Sie diese konfigurieren.

### 4. **Actuator-Endpunkte konfigurieren**
Sie können anpassen, welche Endpunkte in Ihrer `application.properties` oder `application.yml` Datei verfügbar gemacht werden. Zum Beispiel:

#### `application.properties`
```properties
# Bestimmte Endpunkte aktivieren
management.endpoints.web.exposure.include=health,info,metrics,beans

# Basispfad ändern (optional)
management.endpoints.web.base-path=/manage
```

#### `application.yml`
```yaml
management:
  endpoints:
    web:
      exposure:
        include: health, info, metrics, beans
      base-path: /manage
```

Mit dieser Konfiguration sind Endpunkte wie `/manage/metrics` oder `/manage/beans` verfügbar.

### 5. **Verfügbare Endpunkte erkunden**
Hier sind einige nützliche Actuator-Endpunkte, die Sie aktivieren können:
- `/actuator/beans`: Listet alle Spring Beans in Ihrer Anwendung auf.
- `/actuator/env`: Zeigt Umgebungseigenschaften an.
- `/actuator/loggers`: Zeigt Logger-Levels an und ermöglicht deren Änderung.
- `/actuator/shutdown`: Fährt die Anwendung ordnungsgemäß herunter (standardmäßig deaktiviert).

Um alle Endpunkte zum Testen zu aktivieren, verwenden Sie:
```properties
management.endpoints.web.exposure.include=*
```

### 6. **Actuator-Endpunkte sichern**
Da Actuator sensible Daten preisgibt, sollten Sie ihn in der Produktion sichern:
- Fügen Sie Spring Security hinzu:
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-security</artifactId>
</dependency>
```
- Konfigurieren Sie die Sicherheit in `application.properties`:
```properties
spring.security.user.name=admin
spring.security.user.password=secret
management.endpoints.web.exposure.include=health,metrics
```
Jetzt erfordert der Zugriff auf Endpunkte eine Authentifizierung (z.B. `admin:secret`).

### 7. **Benutzerdefinierte Health Checks hinzufügen (Optional)**
Sie können benutzerdefinierte Health Indicators erstellen, indem Sie das `HealthIndicator` Interface implementieren. Beispiel:

```java
import org.springframework.boot.actuate.health.Health;
import org.springframework.boot.actuate.health.HealthIndicator;
import org.springframework.stereotype.Component;

@Component
public class CustomHealthCheck implements HealthIndicator {
    @Override
    public Health health() {
        boolean isHealthy = checkSomeCondition();
        if (isHealthy) {
            return Health.up().withDetail("customCheck", "Alles in Ordnung!").build();
        }
        return Health.down().withDetail("customCheck", "Irgendetwas stimmt nicht").build();
    }

    private boolean checkSomeCondition() {
        // Ihre Logik hier
        return true;
    }
}
```

Dies erscheint im `/actuator/health` Endpunkt.

### 8. **Metriken überwachen**
Um tiefer in Metriken einzutauchen, aktivieren Sie `/metrics` und erkunden Sie spezifische wie:
- `http://localhost:8080/actuator/metrics/jvm.memory.used`
- `http://localhost:8080/actuator/metrics/http.server.requests`

Sie können sich mit Tools wie Prometheus oder Grafana für erweiterte Überwachung integrieren.

### 9. **Testen Sie es**
Starten Sie Ihre App und rufen Sie die Endpunkte mit einem Browser, `curl` oder Tools wie Postman auf. Zum Beispiel:
```bash
curl http://localhost:8080/actuator/health
```

### Tipps
- Verwenden Sie `/actuator/info`, um benutzerdefinierte Informationen (z.B. App-Version) verfügbar zu machen, indem Sie hinzufügen:
```properties
info.app.name=MyApp
info.app.version=1.0.0
```
- Starten Sie Ihre App nach Konfigurationsänderungen neu.

Das sind die Grundlagen! Lassen Sie mich wissen, wenn Sie Hilfe bei einem bestimmten Anwendungsfall oder bei der Fehlerbehebung benötigen.