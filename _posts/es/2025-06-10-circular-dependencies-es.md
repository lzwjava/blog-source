---
audio: false
generated: true
lang: es
layout: post
title: Dependencias Circulares en Spring
translated: true
type: note
---

Las dependencias circulares en Spring o Spring Boot ocurren cuando dos o más beans dependen uno del otro, ya sea directa o indirectamente, durante la inicialización. Esto crea un ciclo donde el mecanismo de inyección de dependencias de Spring no puede resolver las dependencias porque cada bean requiere que el otro esté completamente inicializado primero. Este problema típicamente surge durante la creación de beans en el Spring Application Context, llevando a una `BeanCurrentlyInCreationException`.

### Por qué ocurren las dependencias circulares
Spring gestiona los beans en un contenedor de inyección de dependencias, y los beans normalmente se crean en un orden específico basado en sus dependencias. Cuando los beans se referencian entre sí de manera cíclica (ej., el Bean A depende del Bean B, y el Bean B depende del Bean A), Spring no puede instanciarlos porque se queda atascado en un bucle infinito durante la inicialización. Esto es especialmente común en aplicaciones complejas con componentes fuertemente acoplados.

El problema es más probable que ocurra en los siguientes escenarios:
1. **Inyección por Constructor**: Cuando los beans se conectan a través de constructores, Spring debe resolver las dependencias en el momento de la instanciación, lo que puede llevar a problemas de circularidad si los beans se referencian entre sí.
2. **Inyección por Campo o Setter con Inicialización Eager**: Si los beans se inicializan de forma eager (comportamiento por defecto para beans singleton), Spring intenta resolver las dependencias inmediatamente, exponiendo dependencias circulares.
3. **Relaciones de Beans Mal Configuradas o Excesivamente Complejas**: Un diseño pobre o la falta de separación de concerns puede llevar a ciclos no intencionados.
4. **Anotaciones como `@Autowired` o `@Component`**: La inyección automática de dependencias en componentes fuertemente acoplados puede crear ciclos inadvertidamente.

### Ejemplos Comunes de Dependencias Circulares

#### Ejemplo 1: Ciclo por Inyección de Constructor
```java
@Component
public class BeanA {
    private final BeanB beanB;

    @Autowired
    public BeanA(BeanB beanB) {
        this.beanB = beanB;
    }
}

@Component
public class BeanB {
    private final BeanA beanA;

    @Autowired
    public BeanB(BeanA beanA) {
        this.beanA = beanA;
    }
}
```
**Problema**: `BeanA` requiere `BeanB` en su constructor, y `BeanB` requiere `BeanA` en su constructor. Spring no puede crear ningún bean porque cada uno depende de que el otro esté completamente inicializado primero.

**Error**: `BeanCurrentlyInCreationException: Error creating bean with name 'beanA': Requested bean is currently in creation: Is there an unresolvable circular reference?`

#### Ejemplo 2: Ciclo por Inyección de Campo
```java
@Component
public class BeanA {
    @Autowired
    private BeanB beanB;
}

@Component
public class BeanB {
    @Autowired
    private BeanA beanA;
}
```
**Problema**: Tanto `BeanA` como `BeanB` usan `@Autowired` para inyectarse mutuamente a través de campos. Aunque la inyección por campo es más flexible que la inyección por constructor, Spring aún detecta el ciclo durante la inicialización del bean si ambos son beans singleton (alcance por defecto).

#### Ejemplo 3: Dependencia Circular Indirecta
```java
@Component
public class BeanA {
    @Autowired
    private BeanB beanB;
}

@Component
public class BeanB {
    @Autowired
    private BeanC beanC;
}

@Component
public class BeanC {
    @Autowired
    private BeanA beanA;
}
```
**Problema**: `BeanA` depende de `BeanB`, `BeanB` depende de `BeanC`, y `BeanC` depende de `BeanA`, formando un ciclo. Esta dependencia indirecta es más difícil de detectar pero aún causa el mismo problema.

#### Ejemplo 4: Clases `@Configuration` con Referencias Circulares
```java
@Configuration
public class ConfigA {
    @Autowired
    private ConfigB configB;

    @Bean
    public ServiceA serviceA() {
        return new ServiceA(configB);
    }
}

@Configuration
public class ConfigB {
    @Autowired
    private ConfigA configA;

    @Bean
    public ServiceB serviceB() {
        return new ServiceB(configA);
    }
}
```
**Problema**: Las clases `@Configuration` `ConfigA` y `ConfigB` dependen una de la otra, creando un ciclo cuando Spring intenta inicializar los beans definidos en estas clases.

### Causas Comunes en Spring Boot
- **Auto-Configuration**: La auto-configuración de Spring Boot a veces puede introducir dependencias que llevan a ciclos, especialmente cuando los beans personalizados interactúan con los auto-configurados.
- **Component Scanning**: El uso excesivo de `@ComponentScan` o paquetes mal configurados pueden capturar beans no intencionados, llevando a dependencias cíclicas.
- **Diseño Fuertemente Acoplado**: Lógica de negocio que acopla fuertemente servicios, repositorios o controladores puede crear ciclos inadvertidamente.
- **Uso Incorrecto del Alcance Prototype**: Aunque los beans con alcance prototype a veces pueden evitar dependencias circulares, combinarlos con beans singleton de manera cíclica aún puede causar problemas.

### Cómo Resolver Dependencias Circulares
1. **Usar la Anotación `@Lazy`**:
   - Anota una de las dependencias con `@Lazy` para retrasar su inicialización hasta que sea realmente necesaria.
   ```java
   @Component
   public class BeanA {
       @Autowired
       @Lazy
       private BeanB beanB;
   }
   ```
   Esto rompe el ciclo permitiendo que `BeanA` se inicialice parcialmente antes de que se resuelva `BeanB`.

2. **Cambiar a Inyección por Setter o Campo**:
   - En lugar de la inyección por constructor, usa inyección por setter o campo para uno de los beans para permitir que Spring inicialice el bean primero e inyecte las dependencias después.
   ```java
   @Component
   public class BeanA {
       private BeanB beanB;

       @Autowired
       public void setBeanB(BeanB beanB) {
           this.beanB = beanB;
       }
   }
   ```

3. **Refactorizar el Código para Romper el Ciclo**:
   - Introduce una interfaz o un componente intermedio para desacoplar los beans.
   - Ejemplo: Extrae una dependencia común en un tercer bean o usa una capa de servicio para mediar las interacciones.
   ```java
   public interface Service {
       void performAction();
   }

   @Component
   public class BeanA implements Service {
       @Autowired
       private BeanB beanB;

       public void performAction() {
           // Lógica
       }
   }

   @Component
   public class BeanB {
       @Autowired
       private Service service; // Depende de la interfaz, no de BeanA directamente
   }
   ```

4. **Usar la Anotación `@DependsOn`**:
   - Controla explícitamente el orden de inicialización de los beans para evitar ciclos en casos específicos.
   ```java
   @Component
   @DependsOn("beanB")
   public class BeanA {
       @Autowired
       private BeanB beanB;
   }
   ```

5. **Habilitar Proxies con `@EnableAspectJAutoProxy`**:
   - Asegúrate de que Spring use proxies (CGLIB o JDK dynamic proxies) para manejar dependencias, lo que puede resolver algunos problemas de circularidad inyectando un proxy en lugar del bean real.

6. **Reevaluar el Diseño**:
   - Las dependencias circulares a menudo indican un fallo de diseño. Considera refactorizar para adherirse al Principio de Responsabilidad Única o al Principio de Inversión de Dependencias.

### Cómo Depurar Dependencias Circulares
- **Revisar el Stack Trace**: El stack trace de `BeanCurrentlyInCreationException` indicará los beans involucrados en el ciclo.
- **Habilitar Debug Logging**: Configura `spring.main.lazy-initialization=true` o habilita el registro debug para `org.springframework` para ver los detalles de la creación de beans.
- **Usar Herramientas**: Herramientas como Spring Boot Actuator o plugins de IDE (ej., Spring Tools Suite) pueden visualizar las dependencias de los beans.

### Prevención de Dependencias Circulares
- **Seguir Mejores Prácticas**: Usa patrones de inyección de dependencias como interfaces o abstracciones para reducir el acoplamiento fuerte.
- **Modularizar el Código**: Divide aplicaciones grandes en módulos más pequeños y débilmente acoplados.
- **Probar Temprano**: Ejecuta pruebas de integración para detectar dependencias circulares durante el desarrollo.
- **Limitar Component Scanning**: Sé específico con `@ComponentScan` para evitar capturar beans innecesarios.

### Cuándo las Dependencias Circulares son Menos Probables
- **Alcance Prototype**: Los beans con alcance prototype se crean bajo demanda, reduciendo la probabilidad de circularidad (pero no eliminándola por completo).
- **Inicialización Lazy**: Habilitar la inicialización lazy global (`spring.main.lazy-initialization=true`) puede diferir la creación de beans, aunque puede solo enmascarar el problema.

### Conclusión
Las dependencias circulares en Spring/Spring Boot surgen del acoplamiento fuerte entre beans, a menudo exacerbado por la inyección por constructor o configuraciones complejas. Las soluciones comunes incluyen usar `@Lazy`, cambiar a inyección por setter/campo, o refactorizar para romper el ciclo. Al entender la causa raíz y aplicar las mejores prácticas, puedes prevenir o resolver estos problemas efectivamente. Si encuentras una dependencia circular específica, ¡comparte el código relevante o los detalles del error y puedo ayudarte a analizarlo más a fondo!