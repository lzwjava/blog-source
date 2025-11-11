---
audio: false
generated: false
lang: es
layout: post
title: Preguntas para Entrevista de Ingeniero Backend de Java
translated: true
type: note
---

### Java Core

1. ¿Cuáles son los cuatro principios principales de la POO en Java? Respuesta: Los cuatro principios principales son Encapsulación, Herencia, Polimorfismo y Abstracción. La Encapsulación oculta el estado interno de un objeto, la Herencia permite la herencia de clases, el Polimorfismo permite la sobreescritura y sobrecarga de métodos, y la Abstracción proporciona una forma de representar características esenciales sin incluir detalles de fondo.

2. Explica el propósito de los genéricos en Java y proporciona un ejemplo. Respuesta: Los genéricos permiten parametrizar tipos, permitiendo la reutilización de código y la seguridad de tipos. Por ejemplo, `ArrayList<T>` utiliza un parámetro de tipo `T` para almacenar elementos de cualquier tipo.

3. ¿Cómo se crea un hilo en Java y cuál es su ciclo de vida? Respuesta: Puedes crear un hilo extendiendo `Thread` o implementando `Runnable`. El ciclo de vida incluye los estados Nuevo, Ejecutable, En Ejecución, Bloqueado, En Espera, En Espera Temporizada y Terminado.

4. Describe las diferentes áreas de memoria gestionadas por la JVM. Respuesta: La JVM gestiona el Heap, la Pila, el Área de Métodos, la Pila de Métodos Nativos y el Registro del Contador de Programa. El Heap almacena objetos, mientras que cada hilo tiene su propia Pila para variables locales y llamadas a métodos.

5. ¿Cuál es la diferencia entre excepciones verificadas y no verificadas en Java? Respuesta: Las excepciones verificadas deben declararse o capturarse, mientras que las no verificadas no se comprueban en tiempo de compilación. Ejemplos incluyen `IOException` para verificadas y `NullPointerException` para no verificadas.

6. ¿Cómo se implementa la serialización en Java y por qué es importante? Respuesta: La serialización se implementa mediante la interfaz `Serializable`. Es importante para guardar y restaurar el estado de un objeto, útil en redes y persistencia.

7. Compara ArrayList y LinkedList en el Java Collections Framework. Respuesta: `ArrayList` es adecuado para acceso rápido y recorrido, mientras que `LinkedList` es mejor para inserciones y eliminaciones. `ArrayList` usa memoria contigua, mientras que `LinkedList` usa nodos con punteros.

8. ¿Qué son las expresiones lambda en Java y cómo se relacionan con las interfaces funcionales? Respuesta: Las expresiones lambda proporcionan una forma concisa de representar una interfaz de un método (interfaces funcionales). Se utilizan para implementar interfaces funcionales como `Runnable` o `Comparator`.

9. Explica las operaciones clave disponibles en Java Stream API. Respuesta: Stream API incluye operaciones intermedias (por ejemplo, `map`, `filter`) y operaciones terminales (por ejemplo, `forEach`, `collect`). Permiten operaciones de estilo funcional en colecciones.

10. ¿Cómo se usa la reflexión en Java para inspeccionar clases en tiempo de ejecución? Respuesta: La reflexión permite inspeccionar clases, métodos y campos usando `Class.forName()`, `getMethods()` y `getField()`. Se utiliza para comportamiento dinámico y frameworks.

---

### Ecosistema Spring

1. ¿Qué es el contenedor IoC de Spring y cómo funciona? Respuesta: El contenedor IoC gestiona los beans y sus ciclos de vida. Utiliza inyección de dependencias para gestionar las dependencias, reduciendo el acoplamiento.

2. Explica la auto-configuración de Spring Boot. Respuesta: La auto-configuración configura automáticamente los beans basándose en las dependencias del classpath, simplificando la configuración y reduciendo código repetitivo.

3. ¿Cómo simplifica Spring Data JPA el acceso a datos? Respuesta: Spring Data JPA proporciona repositorios con operaciones CRUD y métodos de consulta, abstraiendo las interacciones con la base de datos.

4. ¿Para qué se utiliza Spring Security? Respuesta: Spring Security proporciona mecanismos de autenticación y autorización, protegiendo las aplicaciones del acceso no autorizado.

5. Describe la función de Spring MVC en aplicaciones web. Respuesta: Spring MVC maneja las peticiones web, mapeando URLs a controladores y gestionando vistas y modelos para las respuestas web.

6. ¿Qué es Spring Cloud y cuáles son sus componentes principales? Respuesta: Spring Cloud proporciona herramientas para construir aplicaciones nativas de la nube, incluyendo descubrimiento de servicios (Eureka), cortacircuitos (Hystrix) y puertas de enlace API.

7. ¿Cómo mejora Spring AOP la funcionalidad de la aplicación? Respuesta: AOP permite separar las preocupaciones transversales como el registro y la gestión de transacciones de la lógica de negocio, usando aspectos y consejos.

8. ¿Qué es Spring Boot Actuator y qué hace? Respuesta: Actuator proporciona endpoints para monitorizar y gestionar aplicaciones, como comprobaciones de salud, métricas e información del entorno.

9. Explica el uso de los perfiles de Spring. Respuesta: Los perfiles permiten diferentes configuraciones para distintos entornos (por ejemplo, desarrollo, producción), permitiendo ajustes específicos del entorno.

10. ¿Cómo simplifican los starters de Spring Boot la gestión de dependencias? Respuesta: Los starters incluyen todas las dependencias necesarias para una funcionalidad específica, reduciendo la necesidad de gestionar manualmente las dependencias.

---

### Arquitectura de Microservicios

1. ¿Qué es el descubrimiento de servicios y por qué es importante? Respuesta: El descubrimiento de servicios automatiza el proceso de localización de servicios, esencial para entornos dinámicos y escalado.

2. Explica la función de una puerta de enlace API en microservicios. Respuesta: Una puerta de enlace API actúa como un único punto de entrada, enrutando peticiones a los servicios apropiados, manejando seguridad y traducción de protocolos.

3. ¿Qué es el patrón Circuit Breaker y cómo ayuda? Respuesta: Circuit Breaker previene fallos en cascada interrumpiendo las peticiones a servicios que fallan, permitiéndoles recuperarse.

4. Describe los principios de diseño de API RESTful. Respuesta: Los principios REST incluyen ausencia de estado, arquitectura cliente-servidor, capacidad de caché e interfaz uniforme, asegurando APIs escalables y mantenibles.

5. ¿Qué es GraphQL y en qué se diferencia de REST? Respuesta: GraphQL es un lenguaje de consulta para APIs, permitiendo a los clientes solicitar exactamente lo que necesitan, reduciendo la sobrecarga y la falta de datos.

6. ¿Cómo se maneja la versionado de APIs en microservicios? Respuesta: El versionado puede hacerse a través de rutas URL, cabeceras o parámetros de consulta, asegurando compatibilidad hacia atrás y transiciones suaves.

7. Explica el patrón Saga en microservicios. Respuesta: Saga gestiona transacciones distribuidas entre servicios, usando una serie de transacciones locales y compensaciones para los fallos.

8. ¿Qué son las comprobaciones de salud en microservicios y por qué son importantes? Respuesta: Las comprobaciones de salud verifican la disponibilidad y el rendimiento de los servicios, cruciales para monitorizar y gestionar mallas de servicios.

9. Describe el desarrollo contract-first en microservicios. Respuesta: El desarrollo contract-first define las APIs antes de la implementación, asegurando compatibilidad y desacoplamiento entre servicios.

10. ¿Cómo se implementa la limitación de tasa en microservicios? Respuesta: La limitación de tasa puede implementarse usando middleware o APIs como Spring Cloud Gateway, controlando las tasas de petición para prevenir abusos.

---

### Bases de Datos y Caché

1. ¿Qué son las uniones SQL y cuándo se usan? Respuesta: Las uniones SQL combinan registros de dos o más tablas basándose en una columna relacionada, utilizadas para recuperar datos a través de tablas relacionadas.

2. Explica las propiedades ACID en transacciones de bases de datos. Respuesta: ACID significa Atomicidad, Consistencia, Aislamiento y Durabilidad, asegurando un procesamiento fiable de transacciones.

3. ¿Qué es Redis y cómo se usa en el almacenamiento en caché? Respuesta: Redis es un almacén clave-valor en memoria usado para almacenamiento en caché, proporcionando acceso rápido a datos de uso frecuente.

4. Compara Redis y Memcached para almacenamiento en caché. Respuesta: Redis soporta estructuras de datos y persistencia, mientras que Memcached es más simple y rápido para el almacenamiento en caché básico.

5. ¿Qué es la fragmentación en bases de datos y por qué se usa? Respuesta: La fragmentación particiona horizontalmente los datos a través de múltiples bases de datos, utilizada para escalabilidad y rendimiento en sistemas grandes.

6. ¿Cómo simplifica Hibernate las interacciones con la base de datos? Respuesta: Hibernate es un framework ORM que mapea clases Java a tablas de base de datos, simplificando las operaciones CRUD.

7. Explica la agrupación de conexiones JDBC. Respuesta: La agrupación de conexiones reutiliza las conexiones de base de datos, mejorando el rendimiento al reducir la sobrecarga de creación de conexiones.

8. ¿Qué es una base de datos de series temporales y cuándo se usa? Respuesta: Las bases de datos de series temporales como InfluxDB almacenan datos con marca de tiempo, ideales para monitorización, IoT y datos de sensores.

9. Describe los niveles de aislamiento de transacciones en bases de datos. Respuesta: Los niveles de aislamiento (Lectura No Comprometida, Lectura Comprometida, Lectura Repetible, Serializable) definen cómo interactúan las transacciones entre sí.

10. ¿Cómo se optimizan las estrategias de indexación en bases de datos? Respuesta: Elige índices basados en patrones de consulta, evita el sobre-indexado y usa índices compuestos para consultas de múltiples columnas.

---

### Concurrencia y Multihilo

1. ¿Qué es un interbloqueo en Java y cómo se puede evitar? Respuesta: El interbloqueo ocurre cuando los hilos esperan indefinidamente unos por otros. Se puede evitar evitando esperas circulares y usando tiempos de espera.

2. Explica el Framework Executor en Java. Respuesta: El Framework Executor gestiona la ejecución de hilos, proporcionando grupos de hilos y programación de tareas.

3. ¿Cuál es la diferencia entre Callable y Runnable? Respuesta: Callable puede devolver un resultado y lanzar excepciones, mientras que Runnable no puede, haciendo a Callable más flexible para tareas que devuelven resultados.

4. Describe el Modelo de Memoria de Java. Respuesta: El Modelo de Memoria de Java define cómo los hilos acceden a las variables, asegurando la visibilidad y el orden de las operaciones a través de los procesadores.

5. ¿Qué es la palabra clave volatile en Java y cuándo debe usarse? Respuesta: Volatile asegura que los cambios en una variable sean visibles para todos los hilos, usado en entornos multi-hilo para prevenir problemas de caché.

6. ¿Cómo se previenen las condiciones de carrera en aplicaciones multi-hilo? Respuesta: Usa sincronización, bloqueos u operaciones atómicas para asegurar el acceso exclusivo a recursos compartidos.

7. Explica el concepto de un bloqueo de lectura-escritura. Respuesta: Los bloqueos de lectura-escritura permiten múltiples lectores o un solo escritor, mejorando la concurrencia al permitir acceso compartido.

8. ¿Qué es un CountDownLatch y cómo se usa? Respuesta: CountDownLatch permite que un hilo espere a que un conjunto de hilos termine, usado para coordinar la ejecución de hilos.

9. Describe la segmentación de bloqueos en Java. Respuesta: La segmentación de bloqueos divide un bloqueo en múltiples partes (franjas), permitiendo acceso concurrente a diferentes partes, reduciendo la contención.

10. ¿Cómo se maneja la interrupción de hilos en Java? Respuesta: Los hilos pueden comprobar el estado de interrupción y lanzar `InterruptedException`, permitiendo una terminación controlada.

---

### Servidores Web y Balanceo de Carga

1. ¿Para qué se usa comúnmente Nginx? Respuesta: Nginx se utiliza como servidor web, proxy inverso, balanceador de carga y caché HTTP, conocido por su alto rendimiento y escalabilidad.

2. Explica la diferencia entre un balanceador de carga y un proxy inverso. Respuesta: Un balanceador de carga distribuye el tráfico entre servidores, mientras que un proxy inverso reenvía peticiones a servidores backend, a menudo proporcionando almacenamiento en caché y seguridad.

3. ¿Qué es HAProxy y por qué se usa? Respuesta: HAProxy es un balanceador de carga de alta disponibilidad y servidor proxy, utilizado para gestionar y distribuir conexiones de red.

4. ¿Cómo se configura SSL/TLS en un servidor web? Respuesta: SSL/TLS se configura obteniendo certificados y configurando listeners HTTPS, cifrando los datos en tránsito.

5. ¿Qué es el almacenamiento en caché del lado del servidor y cómo se implementa? Respuesta: El almacenamiento en caché del lado del servidor almacena datos de acceso frecuente en memoria, implementado usando herramientas como Varnish o Redis para mejorar el rendimiento.

6. Explica la importancia del registro en servidores web. Respuesta: El registro ayuda a monitorizar la actividad del servidor, solucionar problemas y auditar la seguridad, usando herramientas como ELK Stack para el análisis.

7. ¿Cuáles son las mejores prácticas para asegurar servidores web? Respuesta: Las mejores prácticas incluyen usar cabeceras de seguridad, mantener el software actualizado y configurar firewalls para protegerse contra amenazas.

8. ¿Cómo se maneja la persistencia de sesión en el balanceo de carga? Respuesta: La persistencia de sesión puede lograrse usando sesiones sticky o replicación de sesiones, asegurando que las sesiones de usuario permanezcan consistentes.

9. ¿Qué es la descarga SSL y por qué es beneficiosa? Respuesta: La descarga SSL descifra el tráfico SSL/TLS en un balanceador de carga, reduciendo la carga del servidor y mejorando el rendimiento.

10. Describe el proceso de escalar servidores web horizontalmente. Respuesta: El escalado horizontal implica añadir más servidores para manejar la carga aumentada, gestionado a través de balanceadores de carga y grupos de auto-escalado.

---

### CI/CD y DevOps

1. ¿Qué es GitOps y en qué se diferencia del CI/CD tradicional? Respuesta: GitOps trata la infraestructura como código, usando repositorios Git para gestionar configuraciones y despliegues, enfatizando definiciones declarativas.

2. Explica la estrategia de despliegue Blue/Green. Respuesta: El despliegue Blue/Green implica ejecutar dos entornos idénticos, cambiando el tráfico al nuevo entorno tras un despliegue exitoso.

3. ¿Qué es un pipeline de Jenkins y cómo se configura? Respuesta: Un pipeline de Jenkins es una serie de pasos para construir, probar y desplegar software, definido en un Jenkinsfile usando sintaxis declarativa o script.

4. ¿Cómo se implementa la integración continua en un pipeline CI/CD? Respuesta: La integración continua automatiza la construcción y prueba del código tras las confirmaciones, asegurando que el código esté siempre en un estado desplegable.

5. ¿Cuál es el papel de Docker en CI/CD? Respuesta: Los contenedores Docker proporcionan entornos consistentes para construir, probar y desplegar aplicaciones, asegurando paridad entre etapas.

6. Explica el concepto de Infraestructura como Código (IaC). Respuesta: IaC gestiona la infraestructura usando código, permitiendo control de versiones, automatización y consistencia en la configuración de entornos.

7. ¿Cuáles son los beneficios de usar Kubernetes en CI/CD? Respuesta: Kubernetes orquesta aplicaciones containerizadas, proporcionando escalabilidad, auto-reparación y capacidades de despliegue declarativo.

8. ¿Cómo se maneja el escaneo de seguridad en un pipeline CI/CD? Respuesta: Las herramientas de escaneo de seguridad como SonarQube o OWASP Dependency Check se integran en los pipelines para detectar vulnerabilidades temprano.

9. Describe el proceso de revertir un despliegue fallido. Respuesta: Las reversiones pueden automatizarse usando control de versiones o herramientas CI/CD, volviendo a una versión estable conocida ante un fallo.

10. ¿Cuál es la importancia de la gestión de entornos en DevOps? Respuesta: La gestión de entornos asegura la consistencia entre desarrollo, pruebas y producción, reduciendo problemas específicos del entorno.

---

### Patrones de Diseño y Mejores Prácticas

1. ¿Qué es el patrón Singleton y cuándo debe usarse? Respuesta: Singleton asegura que una clase tenga solo una instancia, útil para gestionar recursos compartidos como bases de datos o configuraciones.

2. Explica el patrón Factory y sus beneficios. Respuesta: El patrón Factory proporciona una interfaz para crear objetos sin especificar sus clases, promoviendo el bajo acoplamiento.

3. ¿Qué es el patrón Strategy y cómo promueve la flexibilidad? Respuesta: El patrón Strategy permite seleccionar un algoritmo en tiempo de ejecución, permitiendo cambios de comportamiento flexibles sin modificar el código.

4. Describe los principios SOLID y su significado. Respuesta: Los principios SOLID (Responsabilidad Única, Abierto/Cerrado, Sustitución de Liskov, Segregación de Interfaces, Inversión de Dependencias) guían el diseño para un código mantenible y escalable.

5. ¿Cómo mejora la inyección de dependencias la calidad del código? Respuesta: La inyección de dependencias reduce el acoplamiento externalizando la creación de objetos, haciendo el código más modular y testeable.

6. ¿Qué es el event sourcing y en qué se diferencia del almacenamiento de datos tradicional? Respuesta: El event sourcing almacena una secuencia de eventos que describen cambios de estado, permitiendo la reconstrucción del estado y trazas de auditoría.

7. Explica el patrón de arquitectura CQRS. Respuesta: CQRS separa los comandos (operaciones de escritura) y las consultas (operaciones de lectura), optimizando por separado las preocupaciones de escritura y lectura.

8. ¿Cuáles son las mejores prácticas para la refactorización de código? Respuesta: Las mejores prácticas incluyen cambios pequeños e incrementales, mantener las pruebas y usar herramientas para refactorizaciones automatizadas.

9. ¿Cómo se aseguran las prácticas de código limpio? Respuesta: Las prácticas de código limpio incluyen nomenclatura significativa, adherencia a estándares y escribir código auto-documentado.

10. ¿Cuál es la importancia de TDD (Desarrollo Guiado por Pruebas)? Respuesta: TDD implica escribir pruebas antes que el código, asegurando que el código cumple los requisitos y mejorando la mantenibilidad mediante pruebas continuas.

---

### Seguridad

1. ¿Qué es OAuth2 y cómo se usa para la autorización? Respuesta: OAuth2 es un framework de autorización que permite a aplicaciones de terceros acceder a recursos sin compartir credenciales.

2. Explica JWT (JSON Web Tokens) y su papel en la seguridad. Respuesta: JWT proporciona una forma compacta y autocontenida de transmitir información de forma segura entre partes, usado para autenticación e intercambio de información.

3. ¿Qué es RBAC y cómo simplifica el control de acceso? Respuesta: El Control de Acceso Basado en Roles asigna permisos a roles, simplificando la gestión de acceso de usuarios asignando roles a los usuarios.

4. ¿Cómo se previenen los ataques de inyección SQL? Respuesta: Usa sentencias preparadas y consultas parametrizadas para separar código y datos, previniendo la ejecución de SQL malicioso.

5. ¿Qué es XSS (Cross-Site Scripting) y cómo puede prevenirse? Respuesta: XSS permite a atacantes inyectar scripts en páginas web; puede prevenirse sanitizando entradas y salidas y usando cabeceras de seguridad.

6. Explica la importancia del cifrado en la seguridad de datos. Respuesta: El cifrado protege la confidencialidad de los datos convirtiéndolos en un formato ilegible, asegurando que solo las partes autorizadas puedan acceder a ellos.

7. ¿Cuáles son las mejores prácticas para la codificación segura en Java? Respuesta: Las prácticas incluyen validación de entradas, uso de librerías seguras y adherencia a guías de seguridad como OWASP.

8. ¿Cómo se implementan trazas de auditoría en aplicaciones? Respuesta: Las trazas de auditoría registran las acciones del usuario y eventos del sistema, proporcionando visibilidad y responsabilidad para seguridad y cumplimiento.

9. ¿Qué es la autenticación de dos factores y por qué es importante? Respuesta: La autenticación de dos factores añade una capa extra de seguridad requiriendo dos formas de verificación, reduciendo los riesgos de acceso no autorizado.

10. Describe la función de un Firewall de Aplicaciones Web (WAF). Respuesta: Un WAF protege las aplicaciones web de ataques como inyección SQL y XSS filtrando y monitorizando el tráfico HTTP.

---

### Ajuste de Rendimiento y Optimización

1. ¿Cómo se perfilan las aplicaciones Java para problemas de rendimiento? Respuesta: Usa herramientas de profiling como VisualVM o JProfiler para analizar el uso de CPU, memoria e hilos, identificando cuellos de botella.

2. ¿Qué es la optimización de la recolección de basura y por qué es importante? Respuesta: La optimización de la recolección de basura ajusta los parámetros de la JVM para optimizar la gestión de memoria, reduciendo pausas y mejorando el rendimiento.

3. Explica las técnicas de optimización de consultas de bases de datos. Respuesta: Las técnicas incluyen indexación, reescritura de consultas y usar planes de explicación para mejorar el rendimiento de las consultas.

4. ¿Qué estrategias de almacenamiento en caché son efectivas en aplicaciones Java? Respuesta: Las estrategias incluyen caché local, caché distribuida (por ejemplo, Redis) y políticas de expiración de caché para equilibrar rendimiento y consistencia.

5. ¿Cómo se realizan pruebas de carga y estrés para aplicaciones? Respuesta: Usa herramientas como JMeter o Gatling para simular cargas altas, identificando límites de rendimiento y cuellos de botella.

6. ¿Cuáles son las mejores prácticas para optimizar APIs RESTful? Respuesta: Las mejores prácticas incluyen minimizar la transferencia de datos, usar serialización eficiente y almacenar respuestas en caché para reducir la latencia.

7. ¿Cómo se reduce la latencia de red en sistemas distribuidos? Respuesta: Las técnicas incluyen usar CDNs, optimizar centros de datos y comprimir datos para minimizar el tiempo de transmisión.

8. ¿Qué es el dimensionamiento de la agrupación de conexiones y cómo se determinan los ajustes óptimos? Respuesta: El dimensionamiento de la agrupación de conexiones equilibra el rendimiento y el uso de recursos, determinado analizando patrones de tráfico y restricciones de recursos.

9. Explica la importancia de la monitorización y las alertas en la gestión del rendimiento. Respuesta: La monitorización rastrea la salud y el rendimiento de la aplicación, mientras que las alertas aseguran respuestas oportunas a los problemas, previniendo tiempo de inactividad.

10. ¿Cuáles son los signos comunes de cuellos de botella de rendimiento en aplicaciones Java? Respuesta: Los signos incluyen alto uso de CPU, fugas de memoria, tiempos de respuesta lentos y aumento de la actividad de recolección de basura.