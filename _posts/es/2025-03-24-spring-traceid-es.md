---
audio: false
generated: true
lang: es
layout: post
title: Seguimiento de Solicitudes Spring Boot Log4j
translated: true
type: note
---

En una aplicación Java Spring Boot que utiliza Log4j sin un diseño incorporado de ID de traza, rastrear una entrada de registro específica hasta una solicitud iniciada desde el frontend puede ser realmente un desafío. Tienes razón en que `%t` (nombre del hilo) en Log4j puede ayudar a identificar registros vinculados a un hilo específico, pero como has señalado, esto se vuelve menos confiable cuando las solicitudes abarcan múltiples hilos (por ejemplo, debido a procesamiento asíncrono, grupos de hilos o llamadas a servicios posteriores). Usar un rango de tiempo para buscar en los registros es una solución alternativa, pero es imprecisa y engorrosa, especialmente en sistemas con mucho tráfico. Exploremos algunos consejos prácticos para mejorar esta situación sin tener que rediseñar toda tu configuración.

### Sugerencias Rápidas y Prácticas
1.  **Aprovechar MDC (Mapped Diagnostic Context) con Log4j**
    - Log4j admite MDC, que te permite adjuntar pares clave-valor contextuales a los registros dentro de un hilo (e incluso propagarlos a través de los límites de los hilos con cierto cuidado).
    - Genera un ID de solicitud único cuando la solicitud del frontend llega a tu aplicación Spring Boot (por ejemplo, un UUID) y almacénalo en el MDC. Luego, incluye este ID en tu patrón de registro.
    - **Cómo implementarlo:**
        - En un filtro o interceptor de Spring Boot (por ejemplo, `OncePerRequestFilter`), genera el ID:
          ```java
          import org.slf4j.MDC;
          import javax.servlet.FilterChain;
          import javax.servlet.http.HttpServletRequest;
          import javax.servlet.http.HttpServletResponse;
          import java.util.UUID;

          public class RequestTracingFilter extends OncePerRequestFilter {
              @Override
              protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain) {
                  try {
                      String traceId = UUID.randomUUID().toString();
                      MDC.put("traceId", traceId);
                      filterChain.doFilter(request, response);
                  } finally {
                      MDC.clear(); // Limpiar después de la solicitud
                  }
              }
          }
          ```
        - Registra el filtro en tu configuración de Spring Boot:
          ```java
          @Bean
          public FilterRegistrationBean<RequestTracingFilter> tracingFilter() {
              FilterRegistrationBean<RequestTracingFilter> registrationBean = new FilterRegistrationBean<>();
              registrationBean.setFilter(new RequestTracingFilter());
              registrationBean.addUrlPatterns("/*");
              return registrationBean;
          }
          ```
        - Actualiza tu patrón de Log4j en `log4j.properties` o `log4j.xml` para incluir el `traceId`:
          ```properties
          log4j.appender.console.layout.ConversionPattern=%d{yyyy-MM-dd HH:mm:ss} [%t] %-5p %c{1} - %m [traceId=%X{traceId}]%n
          ```
        - Ahora, cada línea de registro vinculada a esa solicitud incluirá el `traceId`, haciendo que sea fácil rastrearla hasta el clic del botón en el frontend.

2.  **Propagar el ID de Traza a través de los Hilos**
    - Si tu aplicación utiliza grupos de hilos o llamadas asíncronas (por ejemplo, `@Async`), el contexto MDC puede no propagarse automáticamente. Para manejar esto:
        - Envuelve las tareas asíncronas con un ejecutor personalizado que copie el contexto MDC:
          ```java
          import java.util.concurrent.Executor;
          import org.springframework.context.annotation.Bean;
          import org.springframework.context.annotation.Configuration;
          import org.springframework.scheduling.concurrent.ThreadPoolTaskExecutor;

          @Configuration
          public class AsyncConfig {
              @Bean(name = "taskExecutor")
              public Executor taskExecutor() {
                  ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
                  executor.setCorePoolSize(10);
                  executor.setMaxPoolSize(20);
                  executor.setQueueCapacity(100);
                  executor.setTaskDecorator(task -> {
                      Map<String, String> context = MDC.getCopyOfContextMap();
                      return () -> {
                          try {
                              if (context != null) MDC.setContextMap(context);
                              task.run();
                          } finally {
                              MDC.clear();
                          }
                      };
                  });
                  executor.initialize();
                  return executor;
              }
          }
          ```
        - Esto asegura que el `traceId` permanezca con la solicitud incluso a través de los límites de los hilos.

3.  **Agregar Correlación con el Frontend**
    - Si es posible, haz que el frontend envíe un encabezado personalizado (por ejemplo, `X-Request-ID`) con un ID único cuando se haga clic en el botón. Tu backend puede tomar este ID en lugar de generar su propio UUID. Esto vincula el registro directamente con la acción del frontend sin necesidad de conjeturas adicionales.

4.  **Plan de Respaldo: Mejorar el Registro con Datos Contextuales**
    - Si MDC parece tener demasiada sobrecarga en este momento, enriquece tus registros con más contexto en puntos clave (por ejemplo, ID de usuario, ID de sesión o nombre del endpoint). Por ejemplo:
      ```java
      logger.info("Botón clickeado, endpoint=/api/example, user={}", userId);
      ```
    - Combina esto con `%t` (nombre del hilo) y un rango de tiempo ajustado para delimitar los registros manualmente. No es lo ideal, pero funciona en caso de necesidad.

### ¿Por Qué No Simplemente un Rango de Tiempo?
Depender únicamente de las marcas de tiempo es frágil porque:
- Los registros de solicitudes concurrentes se superponen, especialmente en un sistema ocupado.
- La precisión del tiempo (por ejemplo, milisegundos) podría no ser suficiente para aislar una sola solicitud.
- Es tedioso correlacionar registros entre servicios o a través de pilas de llamadas profundas.

### Recomendación a Largo Plazo
Si esta necesidad de rastreo crece, considera adoptar el soporte incorporado de Spring Boot para el rastreo distribuido (por ejemplo, mediante Sleuth o Micrometer con Zipkin). Sleuth genera automáticamente IDs de traza y span y se integra perfectamente con Log4j, pero es más complejo de configurar. Por ahora, MDC es un término medio efectivo y ligero.

### Consejo Final
Comienza con el enfoque MDC: es simple, aprovecha las capacidades nativas de Log4j y te ofrece una manera clara de vincular los registros a una solicitud iniciada desde el frontend. Verás algo como `[traceId=123e4567-e89b-12d3-a456-426614174000]` en cada línea de registro para esa solicitud, haciendo que sea trivial buscar y rastrear. ¡Avísame si necesitas ayuda para ajustar esto aún más!