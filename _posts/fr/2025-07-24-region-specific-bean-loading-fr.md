---
audio: false
generated: true
lang: fr
layout: post
title: Haricots Spécifiques à la Région Dynamique
translated: true
type: note
---

### Comprendre l'exigence

Il semble que vous développiez une application Spring Boot/Java Spring qui doit prendre en charge plusieurs régions (ou "nationalités") comme Singapour (SG), Hong Kong (HK) et Taïwan (TW). Vous souhaitez charger ou injecter dynamiquement différents beans, en particulier pour une classe `CoreController`, en utilisant des fonctionnalités comme `@Autowired` et la gestion des beans.

C'est un scénario courant pour les **configurations multi-locataires** ou **spécifiques à une région**, où le comportement (par exemple, les services, les configurations ou les contrôleurs) varie selon la région. Dans Spring, vous ne pouvez pas facilement basculer des classes de contrôleur entières au moment de l'exécution, mais vous pouvez :

1. Utiliser **Spring Profiles** pour le chargement de beans spécifiques à un environnement (par exemple, des déploiements ou des activations séparés pour chaque région). Cela se fait au moment de la compilation ou du démarrage.
2. Utiliser une **sélection au moment de l'exécution** avec le modèle Stratégie, où vous injectez plusieurs beans (par exemple, via une Map) et sélectionnez le bon en fonction d'un paramètre de requête, d'un en-tête ou d'un contexte (par exemple, la région de l'utilisateur).

Puisque vous avez mentionné le "développement multi-nationalité" et des exemples comme SG/HK/TW, je suppose qu'il faut gérer plusieurs régions dans une seule instance d'application (basculement au moment de l'exécution). S'il s'agit de déploiements séparés par région, les profils sont plus simples.

J'expliquerai les deux approches avec des exemples de code. Nous supposerons que `CoreController` dépend d'un service spécifique à une région (par exemple, l'interface `CoreService` avec des implémentations pour chaque région). Ainsi, le contrôleur reste le même, mais son comportement change via les beans injectés.

### Approche 1 : Utilisation de Spring Profiles pour le chargement de beans spécifiques à une région (au démarrage)

C'est idéal si vous déployez des instances séparées par région (par exemple, via des variables d'environnement ou des propriétés d'application). Les beans sont chargés conditionnellement en fonction du profil actif.

#### Étape 1 : Définir l'interface et les implémentations
Créez une interface pour la logique spécifique à la région :

```java
public interface CoreService {
    String getRegionMessage();
}
```

Implémentations pour chaque région :

```java
// SgCoreService.java
@Service
@Profile("sg")  // Charge ce bean uniquement si le profil 'sg' est actif
public class SgCoreService implements CoreService {
    @Override
    public String getRegionMessage() {
        return "Welcome from Singapore!";
    }
}

// HkCoreService.java
@Service
@Profile("hk")
public class HkCoreService implements CoreService {
    @Override
    public String getRegionMessage() {
        return "Welcome from Hong Kong!";
    }
}

// TwCoreService.java
@Service
@Profile("tw")
public class TwCoreService implements CoreService {
    @Override
    public String getRegionMessage() {
        return "Welcome from Taiwan!";
    }
}
```

#### Étape 2 : Injection dans CoreController
```java
@RestController
public class CoreController {
    private final CoreService coreService;

    @Autowired
    public CoreController(CoreService coreService) {
        this.coreService = coreService;
    }

    @GetMapping("/message")
    public String getMessage() {
        return coreService.getRegionMessage();
    }
}
```

#### Étape 3 : Activer les profils
- Dans `application.properties` ou via la ligne de commande :
  - Exécutez avec `--spring.profiles.active=sg` pour les beans de Singapour.
  - Cela garantit que seul le bean `SgCoreService` est créé et injecté.
- Pour des conditions personnalisées au-delà des profils, utilisez `@ConditionalOnProperty` (par exemple, `@ConditionalOnProperty(name = "app.region", havingValue = "sg")`).

Cette approche est simple mais nécessite un redémarrage ou des applications séparées par région. Ne convient pas pour gérer toutes les régions dans une seule instance d'exécution.

### Approche 2 : Sélection de bean au moment de l'exécution avec Map @Autowired (Modèle Stratégie)

Pour une application unique gérant dynamiquement plusieurs régions (par exemple, basée sur des en-têtes de requête HTTP comme `X-Region: sg`), utilisez une Map de beans. Spring peut injecter toutes les implémentations dans une Map<String, CoreService>, où la clé est le nom du bean.

#### Étape 1 : Définir l'interface et les implémentations
Identique à ci-dessus, mais sans `@Profile` :

```java
public interface CoreService {
    String getRegionMessage();
}

// SgCoreService.java
@Service("sgCoreService")  // Nom explicite du bean pour la clé de la Map
public class SgCoreService implements CoreService {
    @Override
    public String getRegionMessage() {
        return "Welcome from Singapore!";
    }
}

// HkCoreService.java
@Service("hkCoreService")
public class HkCoreService implements CoreService {
    @Override
    public String getRegionMessage() {
        return "Welcome from Hong Kong!";
    }
}

// TwCoreService.java
@Service("twCoreService")
public class TwCoreService implements CoreService {
    @Override
    public String getRegionMessage() {
        return "Welcome from Taiwan!";
    }
}
```

#### Étape 2 : Injecter une Map dans CoreController
```java
@RestController
public class CoreController {
    private final Map<String, CoreService> coreServices;

    @Autowired  // Spring peuple automatiquement la map avec tous les beans CoreService, indexés par nom de bean
    public CoreController(Map<String, CoreService> coreServices) {
        this.coreServices = coreServices;
    }

    @GetMapping("/message")
    public String getMessage(@RequestHeader("X-Region") String region) {  // Ou utilisez @RequestParam si c'est un paramètre de requête
        CoreService service = coreServices.get(region.toLowerCase() + "CoreService");
        if (service == null) {
            throw new IllegalArgumentException("Unsupported region: " + region);
        }
        return service.getRegionMessage();
    }
}
```

- Ici, `@Autowired` sur la Map injecte automatiquement toutes les implémentations de `CoreService`.
- Les noms des beans doivent correspondre à votre logique de clé (par exemple, "sgCoreService").
- Pour la sélection : Utilisez un en-tête/paramètre de requête pour déterminer la région. Cela rend la sélection dynamique par requête.

#### Optionnel : Utilisation de @Qualifier pour une injection spécifique
Si vous souhaitez injecter manuellement un bean spécifique :

```java
@RestController
public class CoreController {
    @Autowired
    @Qualifier("sgCoreService")  // Injecte uniquement le bean SG
    private CoreService sgCoreService;

    // ... idem pour les autres
}
```
Mais ce n'est pas dynamique ; utilisez la Map pour un basculement au moment de l'exécution.

#### Étape 3 : Configuration et bonnes pratiques
- Dans votre classe principale Spring Boot : `@SpringBootApplication` est suffisant ; Spring scanne les beans `@Service`.
- Gérez les valeurs par défaut : Ajoutez un service de repli si aucune région ne correspond.
- Pour des conditions plus complexes, utilisez `@ConditionalOnExpression` ou des annotations `@Conditional` personnalisées sur les beans.
- Sûreté du thread : Comme les contrôleurs sont des singletons par défaut, la Map est sûre tant que les services sont sans état.
- Tests : Utilisez `@SpringBootTest` avec des requêtes simulées pour tester différentes régions.

### Quelle approche choisir ?
- Utilisez les **Profiles** si les régions sont séparées par déploiement/environnement (par exemple, des serveurs différents pour SG/HK/TW).
- Utilisez la **Map/Stratégie** pour une application unifiée gérant toutes les régions au moment de l'exécution (plus flexible pour les microservices).

Si cela ne correspond pas exactement à votre configuration (par exemple, si `CoreController` lui-même doit être différent par région), vous pourriez utiliser plusieurs contrôleurs avec des conditions `@RequestMapping` ou une usine pour créer des contrôleurs dynamiquement—mais c'est plus rare et plus complexe.

Si vous fournissez plus de détails (par exemple, comment la région est déterminée), je peux affiner cela !