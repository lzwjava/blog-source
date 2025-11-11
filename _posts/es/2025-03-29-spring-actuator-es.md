---
audio: false
generated: true
lang: es
layout: post
title: Actuador de Spring
translated: true
type: note
---

Spring Actuator es una característica poderosa en Spring Boot que proporciona herramientas listas para producción para monitorear y gestionar tu aplicación. Aquí tienes una guía paso a paso sobre cómo usarlo:

### 1. **Agregar la Dependencia de Spring Actuator**
Para usar Spring Actuator, necesitas incluir su dependencia en tu proyecto. Si estás usando Maven, agrega esto a tu `pom.xml`:

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-actuator</artifactId>
</dependency>
```

Para Gradle, agrega esto a tu `build.gradle`:

```gradle
implementation 'org.springframework.boot:spring-boot-starter-actuator'
```

### 2. **Iniciar tu Aplicación Spring Boot**
Una vez agregada la dependencia, inicia tu aplicación Spring Boot. Spring Actuator habilitará automáticamente un conjunto de endpoints que puedes usar para monitorear e interactuar con tu aplicación.

### 3. **Acceder a los Endpoints Predeterminados**
Spring Actuator expone varios endpoints a través de HTTP por defecto. La ruta base es `/actuator`. Aquí hay algunos de los más comunes (asumiendo que tu aplicación se ejecuta en `localhost:8080`):
- **Health Check**: `http://localhost:8080/actuator/health`
  - Devuelve el estado de tu aplicación (ej., `{"status":"UP"}`).
- **Application Info**: `http://localhost:8080/actuator/info`
  - Muestra información arbitraria de la aplicación (configurable).
- **Metrics**: `http://localhost:8080/actuator/metrics`
  - Proporciona métricas detalladas como uso de memoria, CPU y más.

Por defecto, solo `/health` e `/info` están habilitados por razones de seguridad. Para exponer más endpoints, necesitas configurarlos.

### 4. **Configurar los Endpoints de Actuator**
Puedes personalizar qué endpoints se exponen en tu archivo `application.properties` o `application.yml`. Por ejemplo:

#### `application.properties`
```properties
# Habilitar endpoints específicos
management.endpoints.web.exposure.include=health,info,metrics,beans

# Cambiar la ruta base (opcional)
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

Con esta configuración, endpoints como `/manage/metrics` o `/manage/beans` estarán disponibles.

### 5. **Explorar los Endpoints Disponibles**
Aquí hay algunos endpoints útiles de Actuator que puedes habilitar:
- `/actuator/beans`: Lista todos los beans de Spring en tu aplicación.
- `/actuator/env`: Muestra las propiedades del entorno.
- `/actuator/loggers`: Muestra y modifica los niveles del logger.
- `/actuator/shutdown`: Apaga la aplicación de manera controlada (deshabilitado por defecto).

Para habilitar todos los endpoints para pruebas, usa:
```properties
management.endpoints.web.exposure.include=*
```

### 6. **Proteger los Endpoints de Actuator**
Dado que Actuator expone datos sensibles, debes protegerlo en producción:
- Agrega Spring Security:
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-security</artifactId>
</dependency>
```
- Configura la seguridad en `application.properties`:
```properties
spring.security.user.name=admin
spring.security.user.password=secret
management.endpoints.web.exposure.include=health,metrics
```
Ahora, acceder a los endpoints requerirá autenticación (ej., `admin:secret`).

### 7. **Agregar Comprobaciones de Salud Personalizadas (Opcional)**
Puedes crear indicadores de salud personalizados implementando la interfaz `HealthIndicator`. Ejemplo:

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
            return Health.up().withDetail("customCheck", "¡Todo bien!").build();
        }
        return Health.down().withDetail("customCheck", "Algo va mal").build();
    }

    private boolean checkSomeCondition() {
        // Tu lógica aquí
        return true;
    }
}
```

Esto aparecerá en el endpoint `/actuator/health`.

### 8. **Monitorear Métricas**
Para profundizar en las métricas, habilita `/metrics` y explora algunas específicas como:
- `http://localhost:8080/actuator/metrics/jvm.memory.used`
- `http://localhost:8080/actuator/metrics/http.server.requests`

Puedes integrar con herramientas como Prometheus o Grafana para un monitoreo avanzado.

### 9. **Probar**
Ejecuta tu aplicación y accede a los endpoints usando un navegador, `curl` o herramientas como Postman. Por ejemplo:
```bash
curl http://localhost:8080/actuator/health
```

### Consejos
- Usa `/actuator/info` para exponer información personalizada (ej., versión de la aplicación) agregando:
```properties
info.app.name=MyApp
info.app.version=1.0.0
```
- Reinicia tu aplicación después de hacer cambios en la configuración.

¡Esos son los conceptos básicos! Avísame si necesitas ayuda con un caso de uso específico o para resolver problemas.