---
audio: false
generated: true
lang: es
layout: post
title: AspectJ con Java y Spring Boot
translated: true
type: note
---

## Tabla de Contenidos
1. [Introducción a la Programación Orientada a Aspectos (AOP)](#introducción-a-la-programación-orientada-a-aspectos-aop)
2. [Descripción General de AspectJ](#descripción-general-de-aspectj)
3. [AspectJ con Java](#aspectj-con-java)
4. [AspectJ con Spring Boot](#aspectj-con-spring-boot)
5. [Casos de Uso Comunes](#casos-de-uso-comunes)
6. [Mejores Prácticas](#mejores-prácticas)
7. [Consideraciones de Rendimiento](#consideraciones-de-rendimiento)

## Introducción a la Programación Orientada a Aspectos (AOP)

AOP es un paradigma de programación que busca aumentar la modularidad permitiendo la separación de preocupaciones transversales. Las preocupaciones transversales son funcionalidades que abarcan múltiples partes de un sistema (como logging, seguridad, gestión de transacciones).

Conceptos clave de AOP:
- **Aspecto**: Una modularización de una preocupación que corta a través de múltiples clases
- **Punto de unión**: Un punto durante la ejecución del programa (llamada a método, acceso a campo, etc.)
- **Advice**: Acción tomada en un punto de unión particular
- **Pointcut**: Predicado que coincide con puntos de unión
- **Weaving**: Enlazar aspectos con otros tipos de aplicación

## Descripción General de AspectJ

AspectJ es la implementación de AOP más popular y completa para Java. Proporciona:
- Un lenguaje de pointcut potente
- Diferentes mecanismos de weaving (tiempo de compilación, post-compilación, tiempo de carga)
- Soporte completo de AOP más allá de lo que ofrece Spring AOP

### AspectJ vs Spring AOP

| Característica      | AspectJ | Spring AOP |
|---------------------|---------|------------|
| Puntos de Unión     | Ejecución de método, llamadas a constructor, acceso a campo, etc. | Solo ejecución de método |
| Weaving             | Tiempo de compilación, post-compilación, tiempo de carga | Proxy en tiempo de ejecución |
| Rendimiento         | Mejor (sin sobrecarga en tiempo de ejecución) | Ligeramente más lento (usa proxies) |
| Complejidad         | Más complejo | Más simple |
| Dependencias        | Requiere compilador/weaver de AspectJ | Integrado en Spring |

## AspectJ con Java

### Configuración

1. Agregar dependencias de AspectJ a tu `pom.xml` (Maven):

```xml
<dependency>
    <groupId>org.aspectj</groupId>
    <artifactId>aspectjrt</artifactId>
    <version>1.9.7</version>
</dependency>
<dependency>
    <groupId>org.aspectj</groupId>
    <artifactId>aspectjweaver</artifactId>
    <version>1.9.7</version>
</dependency>
```

2. Configurar el plugin Maven de AspectJ para weaving en tiempo de compilación:

```xml
<plugin>
    <groupId>org.codehaus.mojo</groupId>
    <artifactId>aspectj-maven-plugin</artifactId>
    <version>1.14.0</version>
    <configuration>
        <complianceLevel>11</complianceLevel>
        <source>11</source>
        <target>11</target>
        <showWeaveInfo>true</showWeaveInfo>
        <verbose>true</verbose>
        <Xlint>ignore</Xlint>
        <encoding>UTF-8</encoding>
    </configuration>
    <executions>
        <execution>
            <goals>
                <goal>compile</goal>
                <goal>test-compile</goal>
            </goals>
        </execution>
    </executions>
</plugin>
```

### Creación de Aspectos

```java
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;
import org.aspectj.lang.annotation.Pointcut;

@Aspect
public class LoggingAspect {

    // Definición de pointcut
    @Pointcut("execution(* com.example.service.*.*(..))")
    public void serviceMethods() {}

    // Advice
    @Before("serviceMethods()")
    public void logBeforeServiceMethods() {
        System.out.println("Un método de servicio está a punto de ejecutarse");
    }
}
```

### Tipos de Advice

1. **Before**: Se ejecuta antes de un punto de unión
2. **After**: Se ejecuta después de que un punto de unión se completa (normalmente o excepcionalmente)
3. **AfterReturning**: Se ejecuta después de que un punto de unión se completa normalmente
4. **AfterThrowing**: Se ejecuta si un método sale lanzando una excepción
5. **Around**: Rodea un punto de unión (advice más potente)

### Expresiones Pointcut

AspectJ proporciona un lenguaje de expresiones pointcut rico:

```java
// Ejecución de método en paquete
@Pointcut("execution(* com.example.service.*.*(..))")

// Ejecución de método en clase
@Pointcut("execution(* com.example.service.UserService.*(..))")

// Método con nombre específico
@Pointcut("execution(* *..find*(..))")

// Con tipo de retorno específico
@Pointcut("execution(public String com.example..*(..))")

// Con tipos de parámetros específicos
@Pointcut("execution(* *.*(String, int))")

// Combinando pointcuts
@Pointcut("serviceMethods() && findMethods()")
```

## AspectJ con Spring Boot

### Configuración

1. Agregar dependencias de Spring AOP y AspectJ:

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-aop</artifactId>
</dependency>
<dependency>
    <groupId>org.aspectj</groupId>
    <artifactId>aspectjweaver</artifactId>
    <version>1.9.7</version>
</dependency>
```

2. Habilitar soporte de AspectJ en tu aplicación Spring Boot:

```java
@SpringBootApplication
@EnableAspectJAutoProxy
public class MyApplication {
    public static void main(String[] args) {
        SpringApplication.run(MyApplication.class, args);
    }
}
```

### Ejemplo: Tiempo de Ejecución de Logging

```java
@Aspect
@Component
public class ExecutionTimeAspect {

    private static final Logger logger = LoggerFactory.getLogger(ExecutionTimeAspect.class);

    @Around("@annotation(com.example.annotation.LogExecutionTime)")
    public Object logExecutionTime(ProceedingJoinPoint joinPoint) throws Throwable {
        long startTime = System.currentTimeMillis();
        
        Object proceed = joinPoint.proceed();
        
        long executionTime = System.currentTimeMillis() - startTime;
        
        logger.info("{} ejecutado en {} ms", 
            joinPoint.getSignature(), executionTime);
        
        return proceed;
    }
}
```

Crear una anotación personalizada:

```java
@Target(ElementType.METHOD)
@Retention(RetentionPolicy.RUNTIME)
public @interface LogExecutionTime {
}
```

Usarla en métodos:

```java
@Service
public class UserService {
    
    @LogExecutionTime
    public List<User> getAllUsers() {
        // implementación
    }
}
```

### Ejemplo: Gestión de Transacciones

```java
@Aspect
@Component
public class TransactionAspect {

    @Autowired
    private PlatformTransactionManager transactionManager;

    @Around("@annotation(com.example.annotation.Transactional)")
    public Object manageTransaction(ProceedingJoinPoint joinPoint) throws Throwable {
        TransactionDefinition def = new DefaultTransactionDefinition();
        TransactionStatus status = transactionManager.getTransaction(def);
        
        try {
            Object result = joinPoint.proceed();
            transactionManager.commit(status);
            return result;
        } catch (Exception e) {
            transactionManager.rollback(status);
            throw e;
        }
    }
}
```

## Casos de Uso Comunes

1. **Logging**: Registro centralizado de entradas/excepciones de métodos
2. **Monitoreo de Rendimiento**: Seguimiento de tiempos de ejecución
3. **Gestión de Transacciones**: Límites de transacción declarativos
4. **Seguridad**: Verificaciones de autorización
5. **Manejo de Errores**: Manejo consistente de excepciones
6. **Caching**: Almacenamiento en caché automático de resultados de métodos
7. **Validación**: Validación de parámetros
8. **Auditoría**: Seguimiento de quién hizo qué y cuándo

## Mejores Prácticas

1. **Mantener los aspectos enfocados**: Cada aspecto debe manejar una preocupación
2. **Usar nombres significativos**: Nombres claros para aspectos y pointcuts
3. **Evitar lógica de negocio en aspectos**: Los aspectos deben manejar preocupaciones transversales, no lógica central
4. **Documentar aspectos**: Especialmente pointcuts complejos
5. **Considerar el rendimiento**: El advice Around puede afectar el rendimiento
6. **Probar aspectos**: Los aspectos necesitan pruebas como cualquier otro código
7. **Usar anotaciones**: Las anotaciones personalizadas hacen los aspectos más declarativos
8. **Tener cuidado con execution() vs @annotation()**: Saber cuándo usar cada uno

## Consideraciones de Rendimiento

1. **Weaving en tiempo de compilación** es generalmente la opción más rápida
2. **Weaving en tiempo de carga** añade cierta sobrecarga durante la carga de clases
3. **Weaving en tiempo de ejecución** (Spring AOP) tiene la mayor sobrecarga
4. **Pointcuts complejos** pueden impactar el rendimiento
5. **El advice Around** es más costoso que otros tipos de advice

Para el máximo rendimiento en producción:
- Usar weaving en tiempo de compilación cuando sea posible
- Mantener los pointcuts simples
- Evitar expresiones pointcut excesivamente amplias

## Conclusión

AspectJ proporciona una forma poderosa de implementar preocupaciones transversales en aplicaciones Java y Spring Boot. Si bien Spring AOP es más simple y suficiente para muchos casos, AspectJ ofrece más capacidades cuando necesitas ir más allá de la intercepción de métodos. Siguiendo los patrones y mejores prácticas descritas en esta guía, puedes usar AspectJ efectivamente para crear aplicaciones más modulares y mantenibles.