---
audio: false
generated: true
lang: es
layout: post
title: Convenciones de Código Java Spring Boot
translated: true
type: note
---

## 1. Principios Fundamentales
- Seguir las convenciones estándar de código Java
- Priorizar la legibilidad y mantenibilidad
- Consistencia en todo el ecosistema Spring
- Alinearse con las mejores prácticas de Java

## 2. Formato de Código

### Directrices Generales
- Usar el formato por defecto de IntelliJ IDEA
- Indentación de 4 espacios (no tabs)
- Longitud máxima de línea de 120 caracteres
- Usar el estilo estándar de llaves de Java

### Reglas Específicas de Formato
- Línea en blanco entre métodos
- Sin espacios en blanco al final de las líneas
- Usar finales de línea estilo Unix (LF)

## 3. Convenciones de Nomenclatura

### Nomenclatura de Clases
- Usar nombres descriptivos y significativos
- Usar UpperCamelCase
- Ejemplos:
  - `ConfigurationProperties`
  - `AutoConfigurationImportSelector`
  - `SpringApplication`

### Nomenclatura de Métodos
- Usar lowerCamelCase
- Verbo o frases verbales
- Ejemplos:
  - `configure()`
  - `registerBeanDefinitions()`
  - `isEnabledByDefault()`

## 4. Prácticas de Anotaciones

### Orden de Anotaciones
- Orden estándar para anotaciones:
  1. Anotaciones de sobrescritura (`@Override`)
  2. Anotaciones de alcance (`@Component`, `@Service`)
  3. Anotaciones de inyección de dependencias
  4. Anotaciones transaccionales
  5. Anotaciones personalizadas del proyecto

### Ubicación de Anotaciones
```java
@Component
@Transactional
public class UserService {
    @Autowired
    private UserRepository repository;
}
```

## 5. Inyección de Dependencias

### Método de Inyección Preferido
- Inyección por constructor
- Evitar la inyección por campo
- Usar `@Autowired` en el constructor

```java
@Service
public class UserService {
    private final UserRepository repository;

    public UserService(UserRepository repository) {
        this.repository = repository;
    }
}
```

## 6. Registro de Logs
- Usar SLF4J para logs
- Usar `private static final Logger` o Lombok's `@Slf4j`

```java
@Slf4j
@Service
public class UserService {
    public void processUser(User user) {
        log.info("Processing user: {}", user.getUsername());
    }
}
```

## 7. Manejo de Errores
- Usar excepciones específicas
- Proporcionar mensajes de error significativos
- Usar `@ControllerAdvice` para manejo global de excepciones

## 8. Configuración
- Usar `application.yml` en lugar de `application.properties`
- Usar configuraciones específicas por perfil
- Externalizar valores de configuración

## 9. Pruebas
- Usar JUnit 5
- Aprovechar las utilidades de Spring Boot Test
- Seguir el patrón Arrange-Act-Assert

## 10. Recursos Adicionales
- [Spring Boot GitHub Coding Style](https://github.com/spring-projects/spring-boot/blob/main/CONTRIBUTING.md)
- [Spring Framework Guidelines](https://github.com/spring-projects/spring-framework/wiki/Code-Style)