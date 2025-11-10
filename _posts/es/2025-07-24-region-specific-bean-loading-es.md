---
audio: false
generated: true
lang: es
layout: post
title: Granos Dinámicos Específicos de la Región
translated: true
type: note
---

### Comprender el Requisito

Parece que estás construyendo una aplicación Spring Boot/Java Spring que necesita soportar múltiples regiones (o "nacionalidades") como Singapur (SG), Hong Kong (HK) y Taiwán (TW). Quieres cargar o inyectar diferentes beans dinámicamente, particularmente para una clase `CoreController`, usando características como `@Autowired` y la gestión de beans.

Este es un escenario común para **multi-tenencia** o **configuraciones específicas por región**, donde el comportamiento (por ejemplo, servicios, configuraciones o controladores) varía según la región. En Spring, no puedes cambiar fácilmente clases de controlador completas en tiempo de ejecución, pero puedes:

1. Usar **Perfiles de Spring** para la carga de beans específicos del entorno (por ejemplo, despliegues o activaciones separadas para cada región). Esto es en tiempo de compilación o de inicio.
2. Usar **selección en tiempo de ejecución** con el Patrón Estrategia, donde inyectas múltiples beans (por ejemplo, a través de un Map) y seleccionas el correcto basándote en un parámetro de solicitud, cabecera o contexto (por ejemplo, la región del usuario).

Ya que mencionaste "desarrollo de múltiples nacionalidades" y ejemplos como SG/HK/TW, asumiré que esto necesita manejar múltiples regiones en una única instancia de la aplicación (cambio en tiempo de ejecución). Si son despliegues separados por región, los perfiles son más simples.

Explicaré ambos enfoques con ejemplos de código. Asumiremos que `CoreController` depende de un servicio específico por región (por ejemplo, una interfaz `CoreService` con implementaciones para cada región). De esta manera, el controlador permanece igual, pero su comportamiento cambia a través de los beans inyectados.

### Enfoque 1: Usar Perfiles de Spring para la Carga de Beans Específicos por Región (Tiempo de Inicio)

Ideal si despliegas instancias separadas por región (por ejemplo, a través de variables de entorno o propiedades de aplicación). Los beans se cargan condicionalmente basándose en el perfil activo.

#### Paso 1: Definir la Interfaz y las Implementaciones
Crea una interfaz para la lógica específica por región:

```java
public interface CoreService {
    String getRegionMessage();
}
```

Implementaciones para cada región:

```java
// SgCoreService.java
@Service
@Profile("sg")  // Solo carga este bean si el perfil 'sg' está activo
public class SgCoreService implements CoreService {
    @Override
    public String getRegionMessage() {
        return "¡Bienvenido desde Singapur!";
    }
}

// HkCoreService.java
@Service
@Profile("hk")
public class HkCoreService implements CoreService {
    @Override
    public String getRegionMessage() {
        return "¡Bienvenido desde Hong Kong!";
    }
}

// TwCoreService.java
@Service
@Profile("tw")
public class TwCoreService implements CoreService {
    @Override
    public String getRegionMessage() {
        return "¡Bienvenido desde Taiwán!";
    }
}
```

#### Paso 2: Autowire en CoreController
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

#### Paso 3: Activar Perfiles
- En `application.properties` o por línea de comandos:
  - Ejecuta con `--spring.profiles.active=sg` para los beans de Singapur.
  - Esto asegura que solo se cree y se inyecte el bean `SgCoreService`.
- Para condiciones personalizadas más allá de los perfiles, usa `@ConditionalOnProperty` (por ejemplo, `@ConditionalOnProperty(name = "app.region", havingValue = "sg")`).

Este enfoque es simple pero requiere reiniciar o aplicaciones separadas por región. No es adecuado para manejar todas las regiones en una única instancia en tiempo de ejecución.

### Enfoque 2: Selección de Beans en Tiempo de Ejecución con Map @Autowired (Patrón Estrategia)

Para una única aplicación que maneje múltiples regiones dinámicamente (por ejemplo, basándose en cabeceras HTTP como `X-Region: sg`), usa un Map de beans. Spring puede inyectar todas las implementaciones en un Map<String, CoreService>, donde la clave es el nombre del bean.

#### Paso 1: Definir la Interfaz y las Implementaciones
Igual que antes, pero sin `@Profile`:

```java
public interface CoreService {
    String getRegionMessage();
}

// SgCoreService.java
@Service("sgCoreService")  // Nombre explícito del bean para la clave del Map
public class SgCoreService implements CoreService {
    @Override
    public String getRegionMessage() {
        return "¡Bienvenido desde Singapur!";
    }
}

// HkCoreService.java
@Service("hkCoreService")
public class HkCoreService implements CoreService {
    @Override
    public String getRegionMessage() {
        return "¡Bienvenido desde Hong Kong!";
    }
}

// TwCoreService.java
@Service("twCoreService")
public class TwCoreService implements CoreService {
    @Override
    public String getRegionMessage() {
        return "¡Bienvenido desde Taiwán!";
    }
}
```

#### Paso 2: Autowire un Map en CoreController
```java
@RestController
public class CoreController {
    private final Map<String, CoreService> coreServices;

    @Autowired  // Spring auto-popula el map con todos los beans CoreService, indexados por nombre de bean
    public CoreController(Map<String, CoreService> coreServices) {
        this.coreServices = coreServices;
    }

    @GetMapping("/message")
    public String getMessage(@RequestHeader("X-Region") String region) {  // O usa @RequestParam si es un parámetro de consulta
        CoreService service = coreServices.get(region.toLowerCase() + "CoreService");
        if (service == null) {
            throw new IllegalArgumentException("Región no soportada: " + region);
        }
        return service.getRegionMessage();
    }
}
```

- Aquí, `@Autowired` en el Map inyecta automáticamente todas las implementaciones de `CoreService`.
- Los nombres de los beans deben coincidir con tu lógica de clave (por ejemplo, "sgCoreService").
- Para la selección: Usa una cabecera/parámetro de solicitud para determinar la región. Esto lo hace dinámico por solicitud.

#### Opcional: Usar @Qualifier para Inyección Específica
Si quieres inyectar un bean específico manualmente:

```java
@RestController
public class CoreController {
    @Autowired
    @Qualifier("sgCoreService")  // Inyecta solo el bean SG
    private CoreService sgCoreService;

    // ... similar para otros
}
```
Pero esto no es dinámico; usa el Map para el cambio en tiempo de ejecución.

#### Paso 3: Configuración y Mejores Prácticas
- En tu clase principal de Spring Boot: `@SpringBootApplication` es suficiente; Spring escanea los beans `@Service`.
- Maneja valores por defecto: Añade un servicio de reserva (fallback) si ninguna región coincide.
- Para condiciones más complejas, usa `@ConditionalOnExpression` o anotaciones `@Conditional` personalizadas en los beans.
- Seguridad en hilos: Dado que los controladores son singleton por defecto, el Map es seguro siempre que los servicios no tengan estado (stateless).
- Pruebas: Usa `@SpringBootTest` con solicitudes simuladas (mock) para probar diferentes regiones.

### ¿Qué Enfoque Elegir?
- Usa **Perfiles** si las regiones están separadas por despliegue/entorno (por ejemplo, servidores diferentes para SG/HK/TW).
- Usa **Map/Estrategia** para una aplicación unificada que maneje todas las regiones en tiempo de ejecución (más flexible para microservicios).

Si esto no coincide con tu configuración exacta (por ejemplo, si el `CoreController` mismo necesita ser diferente por región), podrías usar múltiples controladores con condiciones `@RequestMapping` o una fábrica para crear controladores dinámicamente, pero eso es más raro y complejo.

¡Si proporcionas más detalles (por ejemplo, cómo se determina la región), puedo refinar esto!