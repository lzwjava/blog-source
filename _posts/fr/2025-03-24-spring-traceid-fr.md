---
audio: false
generated: true
lang: fr
layout: post
title: Traçage des Requêtes Spring Boot Log4j
translated: true
type: note
---

Dans une application Java Spring Boot utilisant Log4j sans conception intégrée d'ID de trace, il peut en effet être difficile de relier une entrée de journal spécifique à une requête initiée par le frontend. Vous avez raison que `%t` (nom du thread) dans Log4j peut aider à identifier les journaux liés à un thread spécifique, mais comme vous l'avez noté, cela devient moins fiable lorsque les requêtes s'étendent sur plusieurs threads (par exemple, en raison du traitement asynchrone, des pools de threads ou des appels en aval). Utiliser un intervalle de temps pour rechercher dans les journaux est une solution de contournement, mais elle est imprécise et fastidieuse, surtout dans les systèmes à fort trafic. Explorons quelques conseils pratiques pour améliorer cette situation sans refondre toute votre configuration.

### Suggestions rapides et pratiques
1. **Tirer parti du MDC (Mapped Diagnostic Context) avec Log4j**
   - Log4j prend en charge le MDC, qui permet d'attacher des paires clé-valeur contextuelles aux journaux dans un thread (et même de les propager à travers les limites des threads avec un peu de soin).
   - Générez un ID de requête unique lorsque la requête du frontend atteint votre application Spring Boot (par exemple, un UUID), et stockez-le dans le MDC. Ensuite, incluez cet ID dans votre modèle de journal.
   - **Comment implémenter :**
     - Dans un filtre ou intercepteur Spring Boot (par exemple, `OncePerRequestFilter`), générez l'ID :
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
                   MDC.clear(); // Nettoyer après la requête
               }
           }
       }
       ```
     - Enregistrez le filtre dans votre configuration Spring Boot :
       ```java
       @Bean
       public FilterRegistrationBean<RequestTracingFilter> tracingFilter() {
           FilterRegistrationBean<RequestTracingFilter> registrationBean = new FilterRegistrationBean<>();
           registrationBean.setFilter(new RequestTracingFilter());
           registrationBean.addUrlPatterns("/*");
           return registrationBean;
       }
       ```
     - Mettez à jour votre modèle Log4j dans `log4j.properties` ou `log4j.xml` pour inclure le `traceId` :
       ```properties
       log4j.appender.console.layout.ConversionPattern=%d{yyyy-MM-dd HH:mm:ss} [%t] %-5p %c{1} - %m [traceId=%X{traceId}]%n
       ```
     - Maintenant, chaque ligne de journal liée à cette requête inclura le `traceId`, ce qui facilite le retracement vers le clic de bouton du frontend.

2. **Propager l'ID de trace à travers les threads**
   - Si votre application utilise des pools de threads ou des appels asynchrones (par exemple, `@Async`), le contexte MDC peut ne pas se propager automatiquement. Pour gérer cela :
     - Enveloppez les tâches asynchrones avec un exécuteur personnalisé qui copie le contexte MDC :
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
     - Cela garantit que le `traceId` reste associé à la requête même au-delà des limites des threads.

3. **Ajouter une corrélation frontend**
   - Si possible, demandez au frontend d'envoyer un en-tête personnalisé (par exemple, `X-Request-ID`) avec un ID unique lorsque le bouton est cliqué. Votre backend peut le récupérer au lieu de générer son propre UUID. Cela lie directement le journal à l'action du frontend sans travail supplémentaire.

4. **Solution de secours : Améliorer la journalisation avec des données contextuelles**
   - Si le MDC semble trop lourd pour le moment, enrichissez vos journaux avec plus de contexte aux points clés (par exemple, ID utilisateur, ID de session ou nom du endpoint). Par exemple :
     ```java
     logger.info("Bouton cliqué, endpoint=/api/example, user={}", userId);
     ```
   - Combinez cela avec `%t` (nom du thread) et un intervalle de temps serré pour réduire manuellement les journaux. Ce n'est pas idéal mais cela fonctionne en dépannage.

### Pourquoi ne pas se contenter d'un intervalle de temps ?
Compter uniquement sur les horodatages est fragile car :
- Les journaux des requêtes concurrentes se chevauchent, surtout dans un système chargé.
- La précision temporelle (par exemple, les millisecondes) pourrait ne pas suffire pour isoler une seule requête.
- Il est fastidieux de corréler les journaux entre les services ou les piles d'appels profondes.

### Recommandation à long terme
Si ce besoin de traçabilité augmente, envisagez d'adopter la prise en charge intégrée de Spring Boot pour la traçabilité distribuée (par exemple, via Sleuth ou Micrometer avec Zipkin). Sleuth génère automatiquement des ID de trace et de span et s'intègre parfaitement avec Log4j, mais sa configuration est plus complexe. Pour l'instant, le MDC est un terrain d'entente léger et efficace.

### Conseil final
Commencez par l'approche MDC — elle est simple, tire parti des capacités natives de Log4j et vous offre un moyen clair de lier les journaux à une requête initiée par le frontend. Vous verrez quelque chose comme `[traceId=123e4567-e89b-12d3-a456-426614174000]` dans chaque ligne de journal pour cette requête, ce qui rendra la recherche et le traçage triviaux. Faites-moi savoir si vous avez besoin d'aide pour ajuster cela davantage !