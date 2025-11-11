---
audio: false
generated: true
lang: fr
layout: post
title: Actuateur Spring
translated: true
type: note
---

Spring Actuator est une fonctionnalité puissante de Spring Boot qui fournit des outils prêts pour la production pour surveiller et gérer votre application. Voici un guide étape par étape pour l'utiliser :

### 1. **Ajouter la dépendance Spring Actuator**
Pour utiliser Spring Actuator, vous devez inclure sa dépendance dans votre projet. Si vous utilisez Maven, ajoutez ceci à votre `pom.xml` :

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-actuator</artifactId>
</dependency>
```

Pour Gradle, ajoutez ceci à votre `build.gradle` :

```gradle
implementation 'org.springframework.boot:spring-boot-starter-actuator'
```

### 2. **Démarrer votre application Spring Boot**
Une fois la dépendance ajoutée, démarrez votre application Spring Boot. Spring Actuator activera automatiquement un ensemble de points de terminaison que vous pourrez utiliser pour surveiller et interagir avec votre application.

### 3. **Accéder aux points de terminaison par défaut**
Spring Actuator expose plusieurs points de terminaison via HTTP par défaut. Le chemin de base est `/actuator`. Voici quelques-uns des plus couramment utilisés (en supposant que votre application s'exécute sur `localhost:8080`) :
- **Vérification de santé** : `http://localhost:8080/actuator/health`
  - Retourne le statut de votre application (par exemple, `{"status":"UP"}`).
- **Informations de l'application** : `http://localhost:8080/actuator/info`
  - Affiche des informations arbitraires sur l'application (configurables).
- **Métriques** : `http://localhost:8080/actuator/metrics`
  - Fournit des métriques détaillées comme l'utilisation de la mémoire, le CPU, et plus encore.

Par défaut, seuls `/health` et `/info` sont activés pour des raisons de sécurité. Pour exposer plus de points de terminaison, vous devez les configurer.

### 4. **Configurer les points de terminaison d'Actuator**
Vous pouvez personnaliser les points de terminaison exposés dans votre fichier `application.properties` ou `application.yml`. Par exemple :

#### `application.properties`
```properties
# Activer des points de terminaison spécifiques
management.endpoints.web.exposure.include=health,info,metrics,beans

# Changer le chemin de base (optionnel)
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

Avec cette configuration, des points de terminaison comme `/manage/metrics` ou `/manage/beans` seront disponibles.

### 5. **Explorer les points de terminaison disponibles**
Voici quelques points de terminaison Actuator utiles que vous pouvez activer :
- `/actuator/beans` : Liste tous les beans Spring de votre application.
- `/actuator/env` : Affiche les propriétés de l'environnement.
- `/actuator/loggers` : Affiche et modifie les niveaux des loggers.
- `/actuator/shutdown` : Arrête gracieusement l'application (désactivé par défaut).

Pour activer tous les points de terminaison pour les tests, utilisez :
```properties
management.endpoints.web.exposure.include=*
```

### 6. **Sécuriser les points de terminaison d'Actuator**
Étant donné qu'Actuator expose des données sensibles, vous devriez le sécuriser en production :
- Ajoutez Spring Security :
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-security</artifactId>
</dependency>
```
- Configurez la sécurité dans `application.properties` :
```properties
spring.security.user.name=admin
spring.security.user.password=secret
management.endpoints.web.exposure.include=health,metrics
```
Maintenant, l'accès aux points de terminaison nécessitera une authentification (par exemple, `admin:secret`).

### 7. **Ajouter des vérifications de santé personnalisées (Optionnel)**
Vous pouvez créer des indicateurs de santé personnalisés en implémentant l'interface `HealthIndicator`. Exemple :

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
            return Health.up().withDetail("customCheck", "Tout va bien !").build();
        }
        return Health.down().withDetail("customCheck", "Quelque chose ne va pas").build();
    }

    private boolean checkSomeCondition() {
        // Votre logique ici
        return true;
    }
}
```

Ceci apparaîtra dans le point de terminaison `/actuator/health`.

### 8. **Surveiller les métriques**
Pour approfondir les métriques, activez `/metrics` et explorez des métriques spécifiques comme :
- `http://localhost:8080/actuator/metrics/jvm.memory.used`
- `http://localhost:8080/actuator/metrics/http.server.requests`

Vous pouvez intégrer des outils comme Prometheus ou Grafana pour une surveillance avancée.

### 9. **Tester**
Exécutez votre application et interrogez les points de terminaison en utilisant un navigateur, `curl`, ou des outils comme Postman. Par exemple :
```bash
curl http://localhost:8080/actuator/health
```

### Conseils
- Utilisez `/actuator/info` pour exposer des informations personnalisées (par exemple, la version de l'application) en ajoutant :
```properties
info.app.name=MyApp
info.app.version=1.0.0
```
- Redémarrez votre application après avoir effectué des changements de configuration.

Ce sont les bases ! Faites-moi savoir si vous avez besoin d'aide pour un cas d'utilisation spécifique ou pour résoudre un problème.