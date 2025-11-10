---
audio: false
generated: true
lang: de
layout: post
title: Dynamische regionsspezifische Beans
translated: true
type: note
---

### Verstehen der Anforderungen

Es klingt so, als würden Sie eine Spring Boot/Java Spring Anwendung entwickeln, die mehrere Regionen (oder "Nationalitäten") wie Singapur (SG), Hongkong (HK) und Taiwan (TW) unterstützen muss. Sie möchten verschiedene Beans dynamisch laden oder injizieren, insbesondere für eine `CoreController`-Klasse, und dabei Funktionen wie `@Autowired` und Bean-Management verwenden.

Dies ist ein häufiges Szenario für **Multi-Tenancy** oder **regionsspezifische Konfigurationen**, bei denen das Verhalten (z.B. Services, Konfigurationen oder Controller) je nach Region variiert. In Spring kann man Controller-Klassen zur Laufzeit nicht einfach austauschen, aber man kann:

1. **Spring Profiles** für umgebungsspezifisches Laden von Beans verwenden (z.B. separate Deployments oder Aktivierungen für jede Region). Dies geschieht zur Kompilierzeit oder Startzeit.
2. **Laufzeitauswahl** mit dem Strategie-Muster verwenden, bei dem mehrere Beans (z.B. über eine Map) injiziert werden und die richtige basierend auf einem Request-Parameter, Header oder Kontext (z.B. Region des Benutzers) ausgewählt wird.

Da Sie "mehrnationale Entwicklung" und Beispiele wie SG/HK/TW erwähnt haben, gehe ich davon aus, dass mehrere Regionen in einer einzelnen Anwendungsinstanz behandelt werden müssen (Laufzeitumschaltung). Wenn es separate Deployments pro Region sind, sind Profile einfacher.

Ich werde beide Ansätze mit Codebeispielen erklären. Wir gehen davon aus, dass `CoreController` von einem regionsspezifischen Service abhängt (z.B. `CoreService`-Interface mit Implementierungen für jede Region). Auf diese Weise bleibt der Controller gleich, aber sein Verhalten ändert sich über die injizierten Beans.

### Ansatz 1: Verwenden von Spring Profiles für regionsspezifisches Laden von Beans (Startzeit)

Dies ist ideal, wenn Sie separate Instanzen pro Region bereitstellen (z.B. über Umgebungsvariablen oder Application Properties). Beans werden bedingt basierend auf dem aktiven Profil geladen.

#### Schritt 1: Interface und Implementierungen definieren
Erstellen Sie ein Interface für die regionsspezifische Logik:

```java
public interface CoreService {
    String getRegionMessage();
}
```

Implementierungen für jede Region:

```java
// SgCoreService.java
@Service
@Profile("sg")  // Diese Bean nur laden, wenn das Profil 'sg' aktiv ist
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

#### Schritt 2: Autowire in CoreController
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

#### Schritt 3: Profile aktivieren
- In `application.properties` oder über die Kommandozeile:
  - Ausführen mit `--spring.profiles.active=sg` für Singapore-Beans.
  - Dies stellt sicher, dass nur die `SgCoreService`-Bean erstellt und autowired wird.
- Für benutzerdefinierte Bedingungen jenseits von Profilen, verwenden Sie `@ConditionalOnProperty` (z.B. `@ConditionalOnProperty(name = "app.region", havingValue = "sg")`).

Dieser Ansatz ist einfach, erfordert aber Neustarts oder separate Apps pro Region. Nicht geeignet für die Behandlung aller Regionen in einer Laufzeitinstanz.

### Ansatz 2: Laufzeit-Bean-Auswahl mit @Autowired Map (Strategie-Muster)

Für eine einzelne Anwendung, die mehrere Regionen dynamisch behandelt (z.B. basierend auf HTTP-Request-Headern wie `X-Region: sg`), verwenden Sie eine Map von Beans. Spring kann alle Implementierungen in eine Map<String, CoreService> autowiren, wobei der Schlüssel der Bean-Name ist.

#### Schritt 1: Interface und Implementierungen definieren
Gleich wie oben, aber ohne `@Profile`:

```java
public interface CoreService {
    String getRegionMessage();
}

// SgCoreService.java
@Service("sgCoreService")  // Expliziter Bean-Name für Map-Schlüssel
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

#### Schritt 2: Autowire einer Map in CoreController
```java
@RestController
public class CoreController {
    private final Map<String, CoreService> coreServices;

    @Autowired  // Spring füllt die Map automatisch mit allen CoreService-Beans, mit Bean-Namen als Schlüssel
    public CoreController(Map<String, CoreService> coreServices) {
        this.coreServices = coreServices;
    }

    @GetMapping("/message")
    public String getMessage(@RequestHeader("X-Region") String region) {  // Oder @RequestParam verwenden, wenn es ein Query-Parameter ist
        CoreService service = coreServices.get(region.toLowerCase() + "CoreService");
        if (service == null) {
            throw new IllegalArgumentException("Unsupported region: " + region);
        }
        return service.getRegionMessage();
    }
}
```

- Hier injiziert `@Autowired` auf der Map automatisch alle `CoreService`-Implementierungen.
- Bean-Namen müssen Ihrer Schlüssellogik entsprechen (z.B. "sgCoreService").
- Für die Auswahl: Verwenden Sie einen Request-Header/Parameter, um die Region zu bestimmen. Dies macht es dynamisch pro Request.

#### Optional: Verwenden von @Qualifier für spezifische Injection
Wenn Sie eine bestimmte Bean manuell injizieren möchten:

```java
@RestController
public class CoreController {
    @Autowired
    @Qualifier("sgCoreService")  // Injiziert nur die SG-Bean
    private CoreService sgCoreService;

    // ... ähnlich für andere
}
```
Aber dies ist nicht dynamisch; verwenden Sie die Map für Laufzeitumschaltung.

#### Schritt 3: Konfiguration und Best Practices
- In Ihrer Spring Boot Hauptklasse: `@SpringBootApplication` ist ausreichend; Spring scannt nach `@Service`-Beans.
- Standardbehandlung hinzufügen: Fügen Sie einen Fallback-Service hinzu, wenn keine Region übereinstimmt.
- Für komplexere Bedingungen, verwenden Sie `@ConditionalOnExpression` oder benutzerdefinierte `@Conditional`-Annotationen auf Beans.
- Thread-Sicherheit: Da Controller standardmäßig Singletons sind, ist die Map sicher, solange die Services zustandslos sind.
- Tests: Verwenden Sie `@SpringBootTest` mit Mock-Requests, um verschiedene Regionen zu testen.

### Welchen Ansatz sollte man wählen?
- Verwenden Sie **Profile**, wenn Regionen durch Deployment/Umgebung getrennt sind (z.B. verschiedene Server für SG/HK/TW).
- Verwenden Sie **Map/Strategie** für eine vereinheitlichte App, die alle Regionen zur Laufzeit behandelt (flexibler für Microservices).

Wenn dies nicht Ihrer genauen Einrichtung entspricht (z.B. wenn `CoreController` selbst je Region unterschiedlich sein muss), könnten Sie mehrere Controller mit `@RequestMapping`-Bedingungen oder eine Factory zur dynamischen Erstellung von Controllern verwenden – aber das ist seltener und komplexer.

Wenn Sie mehr Details liefern (z.B. wie die Region bestimmt wird), kann ich das verfeinern!