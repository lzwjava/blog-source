---
audio: false
generated: false
lang: es
layout: post
title: Entrevista para Ingeniero de Backend Java
translated: true
type: note
---

**Java Core (20 puntos)**

1. Comprensión de los principios de POO: Encapsulación, Herencia, Polimorfismo, Abstracción.

2. Genéricos en Java: Uso de parámetros de tipo, tipos acotados y genéricos comodín.

3. Multihilo en Java: Creación de hilos, ciclo de vida del hilo y comunicación entre hilos.

4. Gestión de memoria de la JVM: Heap, Stack, espacios PermGen/Survivor, algoritmos de recolección de basura.

5. Manejo de excepciones: Excepciones verificadas y no verificadas, bloques try-catch, finally y multi-catch.

6. Serialización en Java: Interfaz Serializable, serialización personalizada con writeObject y readObject.

7. Java Collections Framework: Interfaces List, Set, Map, Queue y sus implementaciones.

8. Expresiones Lambda e interfaces funcionales: Uso de predicates, consumers, suppliers y functions.

9. Stream API: Operaciones intermedias y terminales, streams paralelos y pipeline de streams.

10. Reflection API: Acceso a clases, métodos y campos en tiempo de ejecución, procesamiento de anotaciones.

11. Java IO vs NIO: Diferencias en el manejo de archivos, E/S basada en canales y E/S no bloqueante.

12. Java Date and Time API: Trabajo con LocalDate, LocalDateTime y Duration.

13. Redes en Java: Programación de sockets, conexiones URL y clientes HTTP.

14. Seguridad en Java: Criptografía, firmas digitales y prácticas de codificación segura.

15. Módulos de Java: Comprensión de JPMS (Java Platform Module System) y modularidad.

16. Enumeraciones en Java: Uso de enums, valores ordinales y métodos personalizados en enums.

17. Anotaciones en Java: Anotaciones integradas, anotaciones personalizadas y procesamiento de anotaciones.

18. Utilidades de Concurrencia en Java: CountDownLatch, CyclicBarrier, Semaphore y Exchanger.

19. Fugas de Memoria en Java: Causas, detección y estrategias de prevención.

20. Optimización del Rendimiento en Java: Opciones de la JVM, herramientas de profiling y técnicas de optimización de memoria.

**Ecosistema Spring (20 puntos)**

21. Contenedor IoC de Spring: Inyección de dependencias, ciclo de vida del bean y alcance.

22. Auto-configuración de Spring Boot: Cómo Spring Boot configura automáticamente los beans.

23. Spring Data JPA: Patrones de repositorio, operaciones CRUD y métodos de consulta.

24. Spring Security: Autenticación, autorización y protección de APIs REST.

25. Spring MVC: Métodos del controlador, mapeo de solicitudes y resolución de vistas.

26. Spring Cloud: Descubrimiento de servicios con Eureka, balanceo de carga con Ribbon.

27. Spring AOP: Programación Orientada a Aspectos, preocupaciones transversales y tipos de advice.

28. Spring Boot Actuator: Endpoints de monitorización, comprobaciones de salud y recolección de métricas.

29. Perfiles de Spring: Configuraciones específicas del entorno y activación de perfiles.

30. Dependencias Spring Boot Starter: Uso de starters para simplificar la gestión de dependencias.

31. Spring Integration: Integración de diferentes sistemas, mensajería y adaptadores.

32. Spring Batch: Procesamiento por lotes, programación de trabajos e implementaciones de pasos.

33. Spring Cache: Estrategias de caché, anotaciones y gestores de caché.

34. Spring WebFlux: Programación reactiva, E/S no bloqueante y frameworks WebFlux.

35. Spring Cloud Config: Gestión centralizada de configuración para microservicios.

36. Spring Cloud Gateway: Patrones de API gateway, enrutamiento y filtrado.

37. Pruebas en Spring Boot: Uso de @SpringBootTest, MockMvc y TestRestClient.

38. Spring Data REST: Exponer repositorios como servicios RESTful.

39. Spring Cloud Stream: Integración con brokers de mensajes como RabbitMQ y Kafka.

40. Spring Cloud Sleuth: Trazado distribuido y registro de logs en microservicios.

**Arquitectura de Microservicios (20 puntos)**

41. Descubrimiento de Servicios: Cómo funcionan Eureka, Consul y Zookeeper.

42. API Gateway: Patrones, enrutamiento y seguridad en API gateways.

43. Circuit Breaker: Implementación de resiliencia con Hystrix, Resilience4j.

44. Arquitectura Orientada a Eventos: Event sourcing, brokers de mensajes y manejadores de eventos.

45. Diseño de API RESTful: HATEOAS, diseño sin estado y restricciones REST.

46. GraphQL: Implementación de APIs GraphQL, definiciones de esquema y resolvers.

47. Comunicación entre Microservicios: Comunicación síncrona vs asíncrona.

48. Patrón Saga: Gestión de transacciones distribuidas entre servicios.

49. Comprobaciones de Salud: Implementación de sondas de vida y preparación.

50. Desarrollo Contract First: Uso de Swagger para contratos de API.

51. Versionado de APIs: Estrategias para versionar APIs RESTful.

52. Límite de Tasa: Implementación de límites de tasa para prevenir abusos.

53. Patrones de Circuit Breaker: Implementación de fallbacks y reintentos.

54. Despliegue de Microservicios: Uso de Docker, Kubernetes y plataformas cloud.

55. Service Mesh: Comprensión de Istio, Linkerd y sus beneficios.

56. Colaboración por Eventos: Patrones Saga vs Coreografía.

57. Seguridad en Microservicios: OAuth2, JWT y API gateways.

58. Monitorización y Trazado: Herramientas como Prometheus, Grafana y Jaeger.

59. Pruebas de Microservicios: Pruebas de integración, pruebas de contrato y pruebas end-to-end.

60. Base de Datos por Servicio: Gestión de datos y consistencia en microservicios.

**Bases de Datos y Caché (20 puntos)**

61. Joins SQL: Inner, outer, left, right y cross joins.

62. Propiedades ACID: Atomicidad, Consistencia, Aislamiento, Durabilidad en transacciones.

63. Bases de Datos NoSQL: Almacenes de documentos, almacenes clave-valor y bases de datos de grafos.

64. Caché con Redis: Almacén de datos en memoria, estructuras de datos y opciones de persistencia.

65. Memcached vs Redis: Comparación de soluciones de caché.

66. Particionamiento de Bases de Datos: Particionamiento horizontal y balanceo de carga.

67. Frameworks ORM: Hibernate, MyBatis y especificaciones JPA.

68. Pool de Conexiones JDBC: Implementaciones de DataSource y ciclo de vida de la conexión.

69. Búsqueda de Texto Completo: Implementación de búsqueda en bases de datos como Elasticsearch.

70. Bases de Datos de Series Temporales: InfluxDB, OpenTSDB para datos basados en tiempo.

71. Niveles de Aislamiento de Transacciones: Read uncommitted, read committed, repeatable read, serializable.

72. Estrategias de Indexación: Índices B-tree, hash e índices compuestos.

73. Replicación de Bases de Datos: Configuraciones maestro-esclavo, maestro-maestro.

74. Copia de Seguridad y Recuperación de Bases de Datos: Estrategias para la protección de datos.

75. Perfilado de Bases de Datos: Herramientas como SQL Profiler, registros de consultas lentas.

76. Modelos de Consistencia NoSQL: Consistencia eventual, teorema CAP.

77. Migraciones de Bases de Datos: Uso de Flyway, Liquibase para cambios de esquema.

78. Estrategias de Caché: Patrones cache-aside, read-through, write-through.

79. Invalidación de Caché: Gestión de la expiración e invalidación de la caché.

80. Pool de Conexiones de Bases de Datos: Configuraciones de HikariCP, Tomcat JDBC pool.

**Concurrencia y Multihilo (20 puntos)**

81. Ciclo de Vida del Hilo: Nuevo, ejecutable, en ejecución, bloqueado, en espera, terminado.

82. Mecanismos de Sincronización: Cerraduras, bloques sincronizados y cerraduras intrínsecas.

83. Cerraduras Reentrantes: Ventajas sobre los bloques sincronizados, equidad y tiempos de espera.

84. Framework Executor: ThreadPoolExecutor, ExecutorService y configuraciones de grupos de hilos.

85. Callable vs Runnable: Diferencias y casos de uso.

86. Modelo de Memoria de Java: Visibilidad, relaciones happens-before y consistencia de la memoria.

87. Palabra Clave Volatile: Garantizar la visibilidad de los cambios de variables entre hilos.

88. Prevención de Interbloqueos: Evitar y detectar interbloqueos.

89. Programación Asíncrona: Uso de CompletableFuture para operaciones no bloqueantes.

90. ScheduledExecutorService: Programación de tareas con tasas fijas y retrasos.

91. Grupos de Hilos: Grupos de hilos fijos, en caché y programados.

92. Segmentación de Cerraduras: Reducir la contención de cerraduras con cerraduras segmentadas.

93. Cerraduras de Lectura-Escritura: Permitir múltiples lectores o un solo escritor.

94. Mecanismos Wait y Notify: Comunicación entre hilos usando wait/notify.

95. Interrupción de Hilos: Manejo de interrupciones y diseño de tareas interrumpibles.

96. Clases Seguras para Hilos: Implementación de patrones singleton seguros para hilos.

97. Utilidades de Concurrencia: CountDownLatch, CyclicBarrier, Semaphore.

98. Características de Concurrencia en Java 8+: Streams paralelos, framework fork-join.

99. Programación Multicore: Desafíos y soluciones para el procesamiento paralelo.

100. Volcados de Hilos y Análisis: Identificación de problemas con volcados de hilos.

**Servidores Web y Balanceo de Carga (20 puntos)**

101. Configuración de Apache Tomcat: Configuración de conectores, context.xml y server.xml.

102. Nginx como Proxy Inverso: Configuración de proxy_pass, servidores upstream y balanceo de carga.

103. HAProxy para Alta Disponibilidad: Configuración de failover y persistencia de sesiones.

104. Seguridad del Servidor Web: Configuraciones SSL/TLS, cabeceras de seguridad y reglas de firewall.

105. Algoritmos de Balanceo de Carga: Round Robin, Mínimas Conexiones, Hash IP.

106. Caché del Lado del Servidor: Uso de Varnish, Redis o cachés en memoria.

107. Herramientas de Monitorización: Uso de Prometheus, Grafana y New Relic para la monitorización del servidor.

108. Registro en Producción: Registro centralizado con la pila ELK o Graylog.

109. Escalado Horizontal vs Vertical: Comprensión de las ventajas y desventajas y casos de uso.

110. Optimización del Rendimiento del Servidor Web: Ajuste de hilos de trabajo, tiempos de espera de conexión y búferes.

111. Caché de Proxy Inverso: Configuración de cabeceras de caché y expiración.

112. Pruebas de Carga del Servidor Web: Herramientas como Apache JMeter, Gatling para pruebas de rendimiento.

113. Descarga SSL: Manejo de la terminación SSL/TLS en el balanceador de carga.

114. Fortificación del Servidor Web: Mejores prácticas de seguridad y evaluaciones de vulnerabilidades.

115. Servicio de Contenido Dinámico vs Estático: Optimización de configuraciones del servidor.

116. Agrupamiento de Servidores Web: Configuración de clústeres para alta disponibilidad.

117. Autenticación del Servidor Web: Implementación de autenticación básica, digest y OAuth.

118. Formatos de Registro del Servidor Web: Formatos de registro comunes y herramientas de análisis.

119. Límites de Recursos del Servidor Web: Configuración de límites en conexiones, solicitudes y ancho de banda.

120. Copia de Seguridad y Recuperación del Servidor Web: Estrategias para recuperación ante desastres.

**CI/CD y DevOps (20 puntos)**

121. Jenkins Pipeline as Code: Escritura de Jenkinsfiles para pipelines CI/CD.

122. Containerización con Docker: Creación de Dockerfile, construcciones multi-etapa y orquestación de contenedores.

123. Orquestación con Kubernetes: Deployments, services, pods y estrategias de escalado.

124. Principios de GitOps: Uso de Git para la gestión de infraestructura y configuración.

125. Herramientas de Construcción Maven y Gradle: Gestión de dependencias, plugins y ciclo de vida de construcción.

126. Pruebas Unitarias y de Integración: Escritura de pruebas con JUnit, Mockito y TestNG.

127. Herramientas de Cobertura de Código: Uso de Jacoco para medir la cobertura de código.

128. Análisis Estático de Código: Herramientas como SonarQube para comprobaciones de calidad de código.

129. Infraestructura como Código (IaC): Uso de Terraform, CloudFormation para el aprovisionamiento de infraestructura.

130. Despliegues Blue/Green: Minimizar el tiempo de inactividad durante los despliegues.

131. Despliegues Canary: Lanzamiento gradual de nuevas características.

132. Pruebas Automatizadas en Pipelines CI: Integración de pruebas con etapas de construcción.

133. Gestión de Entornos: Uso de Ansible, Chef o Puppet para la gestión de configuración.

134. Mejores Prácticas de CI/CD: Integración continua, despliegue continuo y entrega continua.

135. Estrategias de Rollback: Implementación de rollbacks automáticos en fallos de despliegue.

136. Escaneo de Seguridad: Incorporación de comprobaciones de seguridad como SAST, DAST en los pipelines.

137. Pipelines CI/CD para Microservicios: Gestión de pipelines para múltiples servicios.

138. Monitorización de Pipelines CI/CD: Alertas sobre fallos de pipeline y problemas de rendimiento.

139. Ecosistema de Herramientas DevOps: Comprensión de herramientas como Docker, Kubernetes, Jenkins, Ansible.

140. CI/CD para Aplicaciones Cloud-Native: Despliegue de aplicaciones en plataformas cloud.

**Patrones de Diseño y Mejores Prácticas (20 puntos)**

141. Patrón Singleton: Implementación de singletons seguros para hilos.

142. Patrón Factory: Creación de objetos sin especificar la clase exacta.

143. Patrón Strategy: Encapsulación de algoritmos y cambio entre ellos.

144. Principios SOLID: Comprensión y aplicación de Responsabilidad Única, Abierto/Cerrado, Sustitución de Liskov, Segregación de Interfaces, Inversión de Dependencias.

145. Inyección de Dependencias: Reducción del acoplamiento y aumento de la mantenibilidad del código.

146. Patrón Event Sourcing: Almacenamiento de eventos para reconstruir el estado de la aplicación.

147. Arquitectura CQRS: Separación de responsabilidades de comando y consulta.

148. Diseño para Escalabilidad: Uso de escalado horizontal, particionamiento y balanceo de carga.

149. Técnicas de Refactorización de Código: Extracción de métodos, renombrado de variables y simplificación de condicionales.

150. Prácticas de Código Limpio: Escritura de código legible, mantenible y autodocumentado.

151. Desarrollo Guiado por Pruebas (TDD): Escritura de pruebas antes de la implementación.

152. Control de Versiones de Código: Uso de estrategias de ramificación de Git como GitFlow, Desarrollo Basado en Troncal.

153. Diseño para Mantenibilidad: Uso de diseño modular, separación de preocupaciones.

154. Anti-patrones a Evitar: Clases Dios, código espagueti y acoplamiento fuerte.

155. Diseño para Seguridad: Implementación de privilegio mínimo, defensa en profundidad.

156. Diseño para Rendimiento: Optimización de algoritmos, reducción de operaciones de E/S.

157. Diseño para Fiabilidad: Implementación de redundancia, tolerancia a fallos y manejo de errores.

158. Diseño para Extensibilidad: Uso de plugins, extensiones y APIs abiertas.

159. Diseño para Usabilidad: Garantizar que las APIs sean intuitivas y estén bien documentadas.

160. Diseño para Capacidad de Prueba: Escritura de código que sea fácil de probar y simular.

**Seguridad (20 puntos)**

161. OAuth2 y JWT: Implementación de autenticación basada en tokens.

162. Control de Acceso Basado en Roles (RBAC): Asignación de roles y permisos a usuarios.

163. Cabeceras de Seguridad: Implementación de Política de Seguridad de Contenido, X-Frame-Options.

164. Prevención de Inyección SQL: Uso de sentencias preparadas y consultas parametrizadas.

165. Protección contra Cross-Site Scripting (XSS): Saneamiento de entradas y salidas.

166. Cifrado y Descifrado: Uso de AES, RSA para la protección de datos.

167. Prácticas de Codificación Segura: Evitar vulnerabilidades comunes como desbordamientos de búfer.

168. Implementación de Auditorías: Registro de acciones de usuario y eventos del sistema.

169. Manejo de Datos Sensibles: Almacenamiento seguro de contraseñas con algoritmos de hash.

170. Cumplimiento de Regulaciones: GDPR, PCI-DSS y leyes de protección de datos.

171. Implementación de Autenticación de Dos Factores (2FA): Adición de una capa extra de seguridad.

172. Pruebas de Seguridad: Pruebas de penetración, evaluaciones de vulnerabilidad.

173. Protocolos de Comunicación Seguros: Implementación de SSL/TLS para el cifrado de datos.

174. Gestión Segura de Sesiones: Gestión de tokens de sesión y tiempos de espera.

175. Implementación de Firewalls de Aplicaciones Web (WAF): Protección contra ataques comunes.

176. Monitorización y Alertas de Seguridad: Uso de herramientas como SIEM para la detección de amenazas.

177. Mejores Prácticas de Seguridad en Microservicios: Protección de la comunicación entre servicios.

178. Implementación de CAPTCHA para Protección contra Bots: Prevención de ataques automatizados.

179. Seguridad en Pipelines CI/CD: Escaneo de vulnerabilidades durante las construcciones.

180. Implementación de Seguridad por Diseño: Incorporación de la seguridad desde el inicio del proceso de desarrollo.

**Optimización y Ajuste del Rendimiento (20 puntos)**

181. Perfilado de Aplicaciones Java: Uso de herramientas como JProfiler, VisualVM para análisis de rendimiento.

182. Ajuste de la Recolección de Basura: Ajuste de parámetros de GC para el rendimiento.

183. Optimización de Consultas de Bases de Datos: Indexación, reescritura de consultas y uso de explain plans.

184. Estrategias de Caché: Uso de cachés distribuidas, mecanismos de invalidación de caché.

185. Pruebas de Carga y Estrés: Identificación de cuellos de botella de rendimiento.

186. Optimización de APIs RESTful: Reducción de tiempos de respuesta, minimización de la transferencia de datos.

187. Reducción de la Latencia de Red: Uso de CDNs, optimización de llamadas API.

188. Dimensionamiento del Pool de Conexiones: Determinación de tamaños óptimos de pool para bases de datos y conexiones.

189. Configuraciones de Monitorización y Alertas: Uso de Prometheus, Grafana para monitorización en tiempo real.

190. Identificación y Resolución de Cuellos de Botella: Perfilado de uso de CPU, memoria y E/S.

191. Optimización de Configuraciones del Heap de Java: Establecimiento de tamaños de heap apropiados para diferentes entornos.

192. Reducción de Pausas de la Recolección de Basura: Uso de G1GC, ZGC para aplicaciones de baja latencia.

193. Optimización de E/S de Disco: Uso de SSDs, configuraciones RAID y optimizaciones del sistema de archivos.

194. Caché vs Almacenamiento: Decidir cuándo almacenar en caché los datos versus guardarlos en una base de datos.

195. Optimización del Registro de Logs: Reducción de la sobrecarga de registro y gestión de volúmenes de log.

196. Optimización del Acceso Concurrente: Uso eficiente de cerraduras y minimización de la contención.

197. Perfilado del Uso de Memoria: Identificación de fugas de memoria y optimización de asignaciones de objetos.

198. Optimización de los Tamaños de los Grupos de Hilos: Equilibrio entre demasiados y muy pocos hilos.

199. Optimización de Estructuras de Datos: Elección de las estructuras de datos correctas para casos de uso específicos.

200. Métricas e Indicadores Clave de Rendimiento: Definición y seguimiento de indicadores clave de rendimiento para aplicaciones.