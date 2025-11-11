---
audio: false
generated: true
lang: es
layout: post
title: Guía de Spring AOP
translated: true
type: note
---

## 1. Introducción a Spring AOP

Spring AOP (Programación Orientada a Aspectos) es un componente clave del Spring Framework que proporciona una forma de implementar preocupaciones transversales (como logging, seguridad, gestión de transacciones) de forma separada a la lógica de negocio.

### Conceptos Clave:
- **Preocupaciones transversales**: Funcionalidad que abarca múltiples capas (logging, seguridad, etc.)
- **Aspecto**: Una modularización de una preocupación que cruza múltiples clases
- **Punto de ejecución**: Un punto durante la ejecución del programa (ejecución de método, manejo de excepciones, etc.)
- **Advice**: Acción tomada por un aspecto en un punto de ejecución particular
- **Pointcut**: Predicado que coincide con puntos de ejecución
- **Weaving**: Vincular aspectos con otros tipos de aplicación para crear un objeto aconsejado

## 2. Spring AOP vs AspectJ

| Característica          | Spring AOP | AspectJ |
|-------------------------|-----------|---------|
| Implementación          | Proxy en tiempo de ejecución | Weaving en tiempo de compilación/carga |
| Rendimiento             | Más lento | Más rápido |
| Puntos de ejecución soportados | Solo ejecución de método | Todos (método, constructor, acceso a campo, etc.) |
| Complejidad             | Más simple | Más complejo |
| Dependencia             | Sin dependencias extra | Requiere compilador/weaver de AspectJ |

## 3. Componentes Principales de AOP

### 3.1 Aspectos
Una clase anotada con `@Aspect` que contiene advices y pointcuts.

```java
@Aspect
@Component
public class LoggingAspect {
    // los advices y pointcuts irán aquí
}
```

### 3.2 Tipos de Advice

1. **Before**: Se ejecuta antes de un punto de ejecución
   ```java
   @Before("execution(* com.example.service.*.*(..))")
   public void beforeAdvice() {
       System.out.println("Antes de la ejecución del método");
   }
   ```

2. **AfterReturning**: Se ejecuta después de que un punto de ejecución completa normalmente
   ```java
   @AfterReturning(pointcut = "execution(* com.example.service.*.*(..))", returning = "result")
   public void afterReturningAdvice(Object result) {
       System.out.println("Método retornó: " + result);
   }
   ```

3. **AfterThrowing**: Se ejecuta si un método sale lanzando una excepción
   ```java
   @AfterThrowing(pointcut = "execution(* com.example.service.*.*(..))", throwing = "ex")
   public void afterThrowingAdvice(Exception ex) {
       System.out.println("Excepción lanzada: " + ex.getMessage());
   }
   ```

4. **After (Finally)**: Se ejecuta después de un punto de ejecución sin importar el resultado
   ```java
   @After("execution(* com.example.service.*.*(..))")
   public void afterAdvice() {
       System.out.println("Después de la ejecución del método (finally)");
   }
   ```

5. **Around**: Envuelve un punto de ejecución, el advice más poderoso
   ```java
   @Around("execution(* com.example.service.*.*(..))")
   public Object aroundAdvice(ProceedingJoinPoint joinPoint) throws Throwable {
       System.out.println("Antes de proceder");
       Object result = joinPoint.proceed();
       System.out.println("Después de proceder");
       return result;
   }
   ```

### 3.3 Expresiones Pointcut

Los pointcuts definen dónde debe aplicarse el advice usando expresiones:

- **Execution**: Coincide con la ejecución de métodos
  ```java
  @Pointcut("execution(public * com.example.service.*.*(..))")
  public void serviceMethods() {}
  ```

- **Within**: Coincide con todos los puntos de ejecución dentro de ciertos tipos
  ```java
  @Pointcut("within(com.example.service..*)")
  public void inServiceLayer() {}
  ```

- **this**: Coincide con beans que son instancias de un tipo dado
- **target**: Coincide con beans que son asignables a un tipo dado
- **args**: Coincide con métodos con tipos de argumentos específicos
- **@annotation**: Coincide con métodos con anotaciones específicas

### 3.4 Combinando Pointcuts

Los pointcuts pueden combinarse usando operadores lógicos:
```java
@Pointcut("execution(* com.example.service.*.*(..)) && !execution(* com.example.service.UserService.*(..))")
public void serviceMethodsExceptUserService() {}
```

## 4. Pasos de Implementación

### 4.1 Configuración

1. Agregar dependencia de Spring AOP (si no se usa Spring Boot):
   ```xml
   <dependency>
       <groupId>org.springframework</groupId>
       <artifactId>spring-aop</artifactId>
       <version>${spring.version}</version>
   </dependency>
   <dependency>
       <groupId>org.aspectj</groupId>
       <artifactId>aspectjweaver</artifactId>
       <version>${aspectj.version}</version>
   </dependency>
   ```

2. Para Spring Boot, solo incluir `spring-boot-starter-aop`:
   ```xml
   <dependency>
       <groupId>org.springframework.boot</groupId>
       <artifactId>spring-boot-starter-aop</artifactId>
   </dependency>
   ```

3. Habilitar AOP en tu configuración:
   ```java
   @Configuration
   @EnableAspectJAutoProxy
   public class AppConfig {
   }
   ```

### 4.2 Creando Aspectos

```java
@Aspect
@Component
public class LoggingAspect {
    
    private final Logger logger = LoggerFactory.getLogger(this.getClass());
    
    @Before("execution(* com.example.service.*.*(..))")
    public void logBefore(JoinPoint joinPoint) {
        logger.info("Entrando: {}.{}() con argumentos = {}", 
            joinPoint.getSignature().getDeclaringTypeName(),
            joinPoint.getSignature().getName(),
            Arrays.toString(joinPoint.getArgs()));
    }
    
    @AfterReturning(pointcut = "execution(* com.example.service.*.*(..))", 
                   returning = "result")
    public void logAfterReturning(JoinPoint joinPoint, Object result) {
        logger.info("Saliendo: {}.{}() con resultado = {}", 
            joinPoint.getSignature().getDeclaringTypeName(),
            joinPoint.getSignature().getName(),
            result);
    }
    
    @Around("@annotation(com.example.annotations.LogExecutionTime)")
    public Object logExecutionTime(ProceedingJoinPoint joinPoint) throws Throwable {
        long start = System.currentTimeMillis();
        Object proceed = joinPoint.proceed();
        long executionTime = System.currentTimeMillis() - start;
        logger.info("{} ejecutado en {} ms", 
            joinPoint.getSignature(), executionTime);
        return proceed;
    }
}
```

### 4.3 Anotaciones Personalizadas

Crear anotaciones personalizadas para marcar métodos con comportamientos AOP específicos:

```java
@Target(ElementType.METHOD)
@Retention(RetentionPolicy.RUNTIME)
public @interface LogExecutionTime {
}
```

Luego usarlo en métodos:
```java
@Service
public class UserService {
    
    @LogExecutionTime
    public User getUser(Long id) {
        // implementación
    }
}
```

## 5. Temas Avanzados

### 5.1 Orden de Aspectos

Controlar el orden de ejecución de aspectos con `@Order`:
```java
@Aspect
@Component
@Order(1)
public class LoggingAspect {
    // ...
}

@Aspect
@Component
@Order(2)
public class ValidationAspect {
    // ...
}
```

### 5.2 Accediendo a Información del Método

En los métodos advice, puedes acceder a:
- `JoinPoint` (para Before, After, AfterReturning, AfterThrowing)
- `ProceedingJoinPoint` (para Around)

```java
@Before("execution(* com.example.service.*.*(..))")
public void beforeAdvice(JoinPoint joinPoint) {
    String methodName = joinPoint.getSignature().getName();
    String className = joinPoint.getTarget().getClass().getName();
    Object[] args = joinPoint.getArgs();
    // ...
}
```

### 5.3 Manejo de Excepciones

```java
@AfterThrowing(pointcut = "execution(* com.example.service.*.*(..))", 
               throwing = "ex")
public void handleException(JoinPoint joinPoint, Exception ex) {
    // Registrar excepción, enviar alerta, etc.
}
```

### 5.4 Mecanismos de Proxy

Spring AOP usa dos tipos de proxies:
- **JDK Dynamic Proxy**: Por defecto para interfaces
- **CGLIB Proxy**: Usado cuando no hay interfaz disponible (puede forzarse con `proxyTargetClass=true`)

## 6. Mejores Prácticas

1. **Mantener aspectos enfocados**: Cada aspecto debe manejar una preocupación transversal específica
2. **Usar nombres de pointcut significativos**: Hace el código más legible
3. **Evitar operaciones costosas en aspectos**: Se ejecutan para cada punto de ejecución coincidente
4. **Ser cauteloso con el advice Around**: Siempre llamar `proceed()` a menos que se impida intencionalmente la ejecución
5. **Probar aspectos exhaustivamente**: Afectan múltiples partes de tu aplicación
6. **Documentar aspectos**: Especialmente si modifican el comportamiento significativamente
7. **Considerar el rendimiento**: Pointcuts complejos o muchos aspectos pueden impactar el rendimiento

## 7. Casos de Uso Comunes

1. **Logging**: Entrada/salida de métodos, parámetros, valores de retorno
2. **Monitoreo de Rendimiento**: Medir tiempo de ejecución
3. **Gestión de Transacciones**: (Aunque típicamente manejado por `@Transactional` de Spring)
4. **Seguridad**: Verificaciones de autorización
5. **Validación**: Validación de parámetros
6. **Manejo de Errores**: Manejo consistente de excepciones
7. **Caching**: Cacheo de resultados de métodos
8. **Auditoría**: Rastrear quién llamó qué y cuándo

## 8. Limitaciones

1. Solo funciona con beans gestionados por Spring
2. Solo se soportan puntos de ejecución de métodos
3. No puede aconsejar clases o métodos finales
4. La auto-invocación (método dentro de una clase llamando a otro método de la misma clase) evita el proxy
5. Expresiones pointcut limitadas comparadas con AspectJ

## 9. Solución de Problemas

**Problema**: Advice no se ejecuta
- Verificar si el bean es gestionado por Spring
- Confirmar que la expresión pointcut coincide con los métodos deseados
- Asegurar que `@EnableAspectJAutoProxy` esté presente

**Problema**: Advice Around no procede
- Asegurarse de llamar `proceed()` en `ProceedingJoinPoint`

**Problema**: Tipo de proxy incorrecto
- Usar `@EnableAspectJAutoProxy(proxyTargetClass=true)` para forzar CGLIB

## 10. Conclusión

Spring AOP proporciona una forma poderosa pero simple de implementar preocupaciones transversales en tu aplicación. Aunque tiene algunas limitaciones comparado con AspectJ completo, se integra perfectamente con Spring y cubre la mayoría de los casos de uso comunes. Siguiendo los patrones y mejores prácticas descritas en esta guía, puedes modularizar efectivamente las preocupaciones transversales y mantener tu lógica de negocio limpia y enfocada.

---

Aunque Spring AOP no usa las capacidades de weaving de AspectJ (en su lugar usa AOP basado en proxy), aún necesitas la dependencia `aspectjweaver` por varias razones importantes:

### 1. **Soporte de Anotaciones AspectJ**
Spring AOP usa las **anotaciones** de AspectJ (como `@Aspect`, `@Pointcut`, `@Before`, `@After`, etc.) para definir aspectos y advices. Estas anotaciones vienen de la librería `aspectjweaver`.

- Sin ella, obtendrías errores de compilación al usar `@Aspect` u otras anotaciones AOP.

### 2. **Lenguaje de Expresión Pointcut**
Spring AOP toma prestado el **lenguaje de expresión pointcut** de AspectJ para definir dónde debe aplicarse el advice (ej., `execution(* com.example.service.*.*(..))`).

- El `aspectjweaver` proporciona el parser y la lógica de coincidencia para estas expresiones.

### 3. **Soporte para Puntos de Ejecución Adicionales (Limitado)**
Aunque Spring AOP solo soporta puntos de ejecución de **ejecución de método** (a diferencia de AspectJ, que soporta constructores, acceso a campo, etc.), aún depende del mecanismo subyacente de coincidencia de pointcuts de AspectJ.

### 4. **Load-Time Weaving (Opcional)**
Si decides usar **Load-Time Weaving (LTW)** con Spring AOP (lo cual es raro pero posible), `aspectjweaver` es requerido. LTW permite tejer aspectos en tiempo de carga de clases en lugar de usar proxies.

```java
@EnableLoadTimeWeaving
public class AppConfig { ... }
```

### 5. **Compatibilidad con @EnableAspectJAutoProxy**
Cuando usas `@EnableAspectJAutoProxy`, Spring internamente usa la infraestructura de AspectJ para procesar las anotaciones AOP, aunque no realiza el weaving completo de AspectJ.

---

### **¿Siempre lo Necesitas?**
- **Si usas Spring Boot (`spring-boot-starter-aop`)**: No, porque incluye transitivamente `aspectjweaver`.
- **Si usas Spring AOP plano**: Sí, debes incluirlo explícitamente.

### **¿Alternativas?**
- Si estuvieras usando **AspectJ completo** (weaving en tiempo de compilación o carga), necesitarías `aspectjrt` y `aspectjtools` también.
- Pero para **Spring AOP**, solo `aspectjweaver` es suficiente.

### **Conclusión**
Spring AOP está **basado en proxy**, pero **reutiliza las anotaciones y sintaxis pointcut de AspectJ**, por lo que `aspectjweaver` es requerido. Sirve de puente entre el enfoque de proxy de Spring y el modelo AOP más poderoso de AspectJ.