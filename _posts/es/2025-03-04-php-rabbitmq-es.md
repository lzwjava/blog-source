---
audio: false
generated: true
lang: es
layout: post
title: Uso De RabbitMQ En PHP
translated: true
type: note
---

### Puntos Clave
- Parece probable que para usar "php-amqplib/php-amqplib" versión 2.6.*, necesitas instalarlo vía Composer y seguir los pasos básicos para enviar y recibir mensajes con RabbitMQ.
- El proceso implica configurar una conexión, declarar una cola y usar métodos como `basic_publish` para enviar y `basic_consume` con un bucle para recibir, lo cual puede diferir ligeramente de versiones más recientes.
- La investigación sugiere que para la versión 2.6.*, el proceso de consumo requiere un bucle manual con `wait()`, a diferencia de versiones más nuevas que podrían usar un método `consume()`.

---

### Instalación y Configuración
Para comenzar con "php-amqplib/php-amqplib" versión 2.6.*, primero instálalo usando Composer ejecutando:

```bash
composer require "php-amqplib/php-amqplib:2.6.*"
```

Asegúrate de que RabbitMQ esté instalado y ejecutándose en tu sistema, típicamente accesible en `localhost:5672` con las credenciales por defecto (`guest/guest`). Ajusta estos ajustes si tu configuración es diferente.

### Enviar Mensajes
Para enviar un mensaje, incluye los archivos PHP necesarios y crea una conexión:

```php
require_once __DIR__ . '/vendor/autoload.php';
use PhpAmqpLib\Connection\AMQPStreamConnection;
use PhpAmqpLib\Message\AMQPMessage;

$connection = new AMQPStreamConnection('localhost', 5672, 'guest', 'guest');
$channel = $connection->channel();
```

Declara una cola y publica tu mensaje:

```php
$channel->queue_declare('hello', false, false, false, false);
$msg = new AMQPMessage('Hello World!');
$channel->basic_publish($msg, '', 'hello');
echo " [x] Sent 'Hello World!'\n";
```

Finalmente, cierra la conexión:

```php
$channel->close();
$connection->close();
```

### Recibir Mensajes
Para recibir, configura de manera similar pero define un callback para el manejo de mensajes:

```php
require_once __DIR__ . '/vendor/autoload.php';
use PhpAmqpLib\Connection\AMQPStreamConnection;

$connection = new AMQPStreamConnection('localhost', 5672, 'guest', 'guest');
$channel = $connection->channel();
$channel->queue_declare('hello', false, false, false, false);

$callback = function ($msg) {
    echo ' [x] Received ', $msg->body, "\n";
};

$channel->basic_consume('hello', '', false, true, false, false, $callback);
while (count($channel->callbacks)) {
    $channel->wait();
}

$channel->close();
$connection->close();
```

Ten en cuenta que para la versión 2.6.*, necesitas el bucle con `wait()` para seguir consumiendo, lo cual es un detalle inesperado en comparación con versiones más nuevas que podrían usar un método `consume()` más simple.

---

### Nota de Estudio: Uso Detallado de "php-amqplib/php-amqplib" Versión 2.6.*

Esta sección proporciona una guía completa sobre el uso de la librería "php-amqplib/php-amqplib", específicamente la versión 2.6.*, para interactuar con RabbitMQ, un sistema de colas de mensajes popular. La información se deriva de documentación oficial, tutoriales y detalles específicos de la versión, asegurando una comprensión exhaustiva para los desarrolladores.

#### Antecedentes y Contexto
"php-amqplib/php-amqplib" es una librería PHP para comunicarse con RabbitMQ, implementando el protocolo AMQP 0.9.1. La versión 2.6.* es una versión antigua, y aunque la librería ha evolucionado a la versión 3.x.x para marzo de 2025, entender su uso en esta versión específica es crucial para sistemas heredados o requisitos de proyecto específicos. La librería es mantenida por colaboradores incluyendo a Ramūnas Dronga y Luke Bakken, con participación significativa de ingenieros de VMware trabajando en RabbitMQ ([GitHub - php-amqplib/php-amqplib](https://github.com/php-amqplib/php-amqplib)).

Los tutoriales de RabbitMQ, como aquellos en el sitio web oficial de RabbitMQ, proporcionan ejemplos que son generalmente aplicables pero pueden reflejar versiones más nuevas. Para la versión 2.6.*, son necesarios ajustes, particularmente en el proceso de consumo, como se detalla a continuación.

#### Proceso de Instalación
Para comenzar, instala la librería usando Composer, el gestor de dependencias de PHP. Ejecuta el siguiente comando en el directorio de tu proyecto:

```bash
composer require "php-amqplib/php-amqplib:2.6.*"
```

Este comando asegura que la librería sea descargada y configurada para su uso, con Composer gestionando las dependencias. Asegúrate de que RabbitMQ esté instalado y ejecutándose, típicamente accesible en `localhost:5672` con las credenciales por defecto (`guest/guest`). Para producción, ajusta el host, puerto y credenciales según sea necesario, y consulta la [Documentación de CloudAMQP para PHP](https://www.cloudamqp.com/docs/php.html) para configuraciones de broker gestionado.

#### Enviar Mensajes: Paso a Paso
Enviar mensajes implica establecer una conexión y publicar en una cola. Aquí está el proceso:

1. **Incluir Archivos Requeridos:**
   Usa el autoloader de Composer para incluir la librería:

   ```php
   require_once __DIR__ . '/vendor/autoload.php';
   use PhpAmqpLib\Connection\AMQPStreamConnection;
   use PhpAmqpLib\Message\AMQPMessage;
   ```

2. **Crear Conexión y Canal:**
   Inicializa una conexión a RabbitMQ y abre un canal:

   ```php
   $connection = new AMQPStreamConnection('localhost', 5672, 'guest', 'guest');
   $channel = $connection->channel();
   ```

   Los parámetros son host, puerto, nombre de usuario y contraseña, con los valores por defecto como se muestra. Para configuraciones SSL u otras, consulta el [Tutorial de RabbitMQ para PHP](https://www.rabbitmq.com/tutorials/tutorial-one-php).

3. **Declarar Cola y Publicar:**
   Declara una cola para asegurar que existe, luego publica un mensaje:

   ```php
   $channel->queue_declare('hello', false, false, false, false);
   $msg = new AMQPMessage('Hello World!');
   $channel->basic_publish($msg, '', 'hello');
   echo " [x] Sent 'Hello World!'\n";
   ```

   Aquí, `queue_declare` crea una cola llamada 'hello' con ajustes por defecto (no duradera, no exclusiva, auto-eliminar). `basic_publish` envía el mensaje a la cola.

4. **Cerrar Conexión:**
   Después de enviar, cierra el canal y la conexión para liberar recursos:

   ```php
   $channel->close();
   $connection->close();
   ```

Este proceso es estándar entre versiones, sin cambios significativos notados en el registro de cambios para la versión 2.6.* en comparación con lanzamientos posteriores.

#### Recibir Mensajes: Detalles Específicos de la Versión
Recibir mensajes en la versión 2.6.* requiere atención cuidadosa, ya que el mecanismo de consumo difiere de versiones más nuevas. Aquí está el proceso detallado:

1. **Incluir Archivos Requeridos:**
   Similar al envío, incluye el autoloader y las clases necesarias:

   ```php
   require_once __DIR__ . '/vendor/autoload.php';
   use PhpAmqpLib\Connection\AMQPStreamConnection;
   ```

2. **Crear Conexión y Canal:**
   Establece la conexión y el canal como antes:

   ```php
   $connection = new AMQPStreamConnection('localhost', 5672, 'guest', 'guest');
   $channel = $connection->channel();
   ```

3. **Declarar Cola:**
   Asegura que la cola exista, coincidiendo con la declaración del emisor:

   ```php
   $channel->queue_declare('hello', false, false, false, false);
   ```

4. **Definir Callback:**
   Crea una función callback para manejar los mensajes recibidos:

   ```php
   $callback = function ($msg) {
       echo ' [x] Received ', $msg->body, "\n";
   };
   ```

   Esta función será llamada para cada mensaje, imprimiendo el cuerpo en este ejemplo.

5. **Consumir Mensajes:**
   Para la versión 2.6.*, usa `basic_consume` para registrar el callback, luego entra en un bucle para seguir consumiendo:

   ```php
   $channel->basic_consume('hello', '', false, true, false, false, $callback);
   while (count($channel->callbacks)) {
       $channel->wait();
   }
   ```

   El método `basic_consume` toma parámetros para el nombre de la cola, etiqueta del consumidor, no-local, no-ack, exclusivo, no-wait y callback. El bucle con `wait()` mantiene el consumidor ejecutándose, verificando mensajes. Este es un detalle importante, ya que versiones más nuevas (ej., 3.2) podrían usar un método `consume()`, que no estaba disponible en 2.6.* basado en la revisión de la documentación de la API.

6. **Cerrar Conexión:**
   Después de consumir, cierra los recursos:

   ```php
   $channel->close();
   $connection->close();
   ```

Un detalle inesperado es la necesidad del bucle manual en la versión 2.6.*, lo cual puede requerir manejo de errores adicional para uso en producción, como capturar excepciones por problemas de conexión.

#### Consideraciones Específicas de la Versión
La versión 2.6.* es parte de los lanzamientos antiguos, y aunque el registro de cambios no la lista explícitamente, versiones alrededor de 2.5 a 2.7 muestran mejoras como soporte de heartbeat y compatibilidad con PHP 5.3. Para mensajes grandes, la versión 2.6.* soporta `setBodySizeLimit` en el canal para manejar límites de memoria, truncando mensajes si es necesario, con detalles en [GitHub - php-amqplib/php-amqplib](https://github.com/php-amqplib/php-amqplib).

Comparando con la versión 3.2, los cambios incluyen soporte para PHP 8 y nuevos métodos como `consume()`, pero la funcionalidad central para enviar y consumo básico permanece similar. Los usuarios deben probar la compatibilidad, especialmente con versiones de PHP, ya que 2.6.* probablemente soporta PHP 5.3 a 7.x, según entradas del registro de cambios.

#### Resolución de Problemas y Mejores Prácticas
- Si el envío falla, revisa los registros de RabbitMQ en busca de alarmas de recursos, como espacio en disco por debajo de 50 MB, y ajusta los ajustes vía [Guía de Configuración de RabbitMQ](https://www.rabbitmq.com/configure.html#config-items).
- Para el consumo, asegúrate de que el consumidor se ejecute continuamente; usa herramientas como Supervisor para demonizar en producción.
- Lista las colas usando `rabbitmqctl list_queues` en Linux o `rabbitmqctl.bat list_queues` en Windows como un usuario privilegiado, según [Herramientas de Línea de Comandos de RabbitMQ](https://www.rabbitmq.com/cli.html).

#### Tabla: Comparación de Versiones para Métodos Clave

| Método             | Comportamiento en Versión 2.6.*                 | Comportamiento en Versión 3.2                 |
|--------------------|------------------------------------------------|----------------------------------------------|
| `basic_publish`    | Estándar, publica en la cola                   | Sin cambios, mismo uso                       |
| `basic_consume`    | Requiere bucle con `wait()` para consumir      | Similar, pero método `consume()` disponible  |
| `setBodySizeLimit` | Soportado para mensajes grandes, trunca si se establece | Soportado, misma funcionalidad             |
| Compatibilidad con PHP | Probablemente 5.3 a 7.x                      | Soporta PHP 7.x y 8.x                        |

Esta tabla resalta la diferencia clave en el consumo, lo cual es crítico para los usuarios de la versión 2.6.*.

#### Conclusión
Usar "php-amqplib/php-amqplib" versión 2.6.* implica una instalación estándar con Composer, con envío de mensajes vía `basic_publish` y recepción vía `basic_consume` con un bucle manual. Aunque es similar a versiones más nuevas, el proceso de consumo requiere atención adicional, haciéndolo esencial para que los desarrolladores prueben y ajusten para sistemas heredados. Para más detalles, consulta los tutoriales oficiales de RabbitMQ y el repositorio de GitHub.

---

### Citas Clave
- [GitHub - php-amqplib/php-amqplib El cliente PHP más usado para RabbitMQ](https://github.com/php-amqplib/php-amqplib)
- [Tutorial de RabbitMQ - Ejemplo PHP "Hello World!"](https://www.rabbitmq.com/tutorials/tutorial-one-php)
- [Documentación de CloudAMQP para PHP Comienza con CloudAMQP y PHP](https://www.cloudamqp.com/docs/php.html)
- [php-amqplib/php-amqplib Packagist Anteriormente videlalvaro/php-amqplib](https://packagist.org/packages/php-amqplib/php-amqplib)
- [GitHub - php-amqplib/php-amqplib Archivo CHANGELOG](https://github.com/php-amqplib/php-amqplib/blob/master/CHANGELOG.md)
- [Guía de Configuración de RabbitMQ Elementos de configuración y ajustes](https://www.rabbitmq.com/configure.html#config-items)
- [Herramientas de Línea de Comandos de RabbitMQ Referencia CLI y uso](https://www.rabbitmq.com/cli.html)