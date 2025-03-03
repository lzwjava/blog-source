---
audio: false
generated: true
lang: es
layout: post
title: Usando RabbitMQ en PHP
translated: true
---

### Puntos Clave
- Parece probable que para usar "php-amqplib/php-amqplib" versión 2.6.*, necesites instalarlo a través de Composer y seguir los pasos básicos para enviar y recibir mensajes con RabbitMQ.
- El proceso implica configurar una conexión, declarar una cola y usar métodos como `basic_publish` para enviar y `basic_consume` con un bucle para recibir, lo cual puede diferir ligeramente de las versiones más recientes.
- La investigación sugiere que para la versión 2.6.*, el proceso de consumo requiere un bucle manual con `wait()`, a diferencia de las versiones más recientes que podrían usar un método `consume()`.

---

### Instalación y Configuración
Para comenzar con "php-amqplib/php-amqplib" versión 2.6.*, primero instálalo usando Composer ejecutando:

```bash
composer require "php-amqplib/php-amqplib:2.6.*"
```

Asegúrate de que RabbitMQ esté instalado y en funcionamiento en tu sistema, generalmente accesible en `localhost:5672` con las credenciales predeterminadas (`guest/guest`). Ajusta estos ajustes si tu configuración es diferente.

### Enviando Mensajes
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
echo " [x] Enviado 'Hello World!'\n";
```

Finalmente, cierra la conexión:

```php
$channel->close();
$connection->close();
```

### Recibiendo Mensajes
Para recibir, configúralo de manera similar pero define una devolución de llamada para el manejo de mensajes:

```php
require_once __DIR__ . '/vendor/autoload.php';
use PhpAmqpLib\Connection\AMQPStreamConnection;

$connection = new AMQPStreamConnection('localhost', 5672, 'guest', 'guest');
$channel = $connection->channel();
$channel->queue_declare('hello', false, false, false, false);

$callback = function ($msg) {
    echo ' [x] Recibido ', $msg->body, "\n";
};

$channel->basic_consume('hello', '', false, true, false, false, $callback);
while (count($channel->callbacks)) {
    $channel->wait();
}

$channel->close();
$connection->close();
```

Ten en cuenta que para la versión 2.6.*, necesitas el bucle con `wait()` para seguir consumiendo, lo cual es un detalle inesperado en comparación con las versiones más recientes que podrían usar un método `consume()` más sencillo.

---

### Nota de Encuesta: Uso Detallado de "php-amqplib/php-amqplib" Versión 2.6.*

Esta sección proporciona una guía exhaustiva sobre el uso de la biblioteca "php-amqplib/php-amqplib", específicamente la versión 2.6.*, para interactuar con RabbitMQ, un popular sistema de colas de mensajes. La información se deriva de la documentación oficial, tutoriales y detalles específicos de la versión, asegurando una comprensión exhaustiva para los desarrolladores.

#### Antecedentes y Contexto
"php-amqplib/php-amqplib" es una biblioteca de PHP para comunicarse con RabbitMQ, implementando el protocolo AMQP 0.9.1. La versión 2.6.* es un lanzamiento más antiguo, y aunque la biblioteca ha evolucionado a la versión 3.x.x para marzo de 2025, entender su uso en esta versión específica es crucial para sistemas heredados o requisitos específicos de proyectos. La biblioteca es mantenida por contribuidores que incluyen a Ramūnas Dronga y Luke Bakken, con una participación significativa de ingenieros de VMware que trabajan en RabbitMQ ([GitHub - php-amqplib/php-amqplib](https://github.com/php-amqplib/php-amqplib)).

Los tutoriales de RabbitMQ, como los que se encuentran en el sitio web oficial de RabbitMQ, proporcionan ejemplos que son generalmente aplicables pero pueden reflejar versiones más recientes. Para la versión 2.6.*, se necesitan ajustes, especialmente en el proceso de consumo, como se detalla a continuación.

#### Proceso de Instalación
Para comenzar, instala la biblioteca usando Composer, el administrador de dependencias de PHP. Ejecuta el siguiente comando en el directorio de tu proyecto:

```bash
composer require "php-amqplib/php-amqplib:2.6.*"
```

Este comando asegura que la biblioteca se descargue y configure para su uso, con Composer gestionando las dependencias. Asegúrate de que RabbitMQ esté instalado y en funcionamiento, generalmente accesible en `localhost:5672` con las credenciales predeterminadas (`guest/guest`). Para producción, ajusta el host, el puerto y las credenciales según sea necesario, y consulta la [Documentación de CloudAMQP PHP](https://www.cloudamqp.com/docs/php.html) para configuraciones de brokers gestionados.

#### Enviando Mensajes: Paso a Paso
Enviar mensajes implica establecer una conexión y publicar en una cola. Aquí está el proceso:

1. **Incluir Archivos Requeridos:**
   Usa el autocargador de Composer para incluir la biblioteca:

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

   Los parámetros son el host, el puerto, el nombre de usuario y la contraseña, con los valores predeterminados mostrados. Para SSL u otras configuraciones, consulta el [Tutorial de RabbitMQ PHP](https://www.rabbitmq.com/tutorials/tutorial-one-php).

3. **Declarar Cola y Publicar:**
   Declara una cola para asegurarte de que exista, luego publica un mensaje:

   ```php
   $channel->queue_declare('hello', false, false, false, false);
   $msg = new AMQPMessage('Hello World!');
   $channel->basic_publish($msg, '', 'hello');
   echo " [x] Enviado 'Hello World!'\n";
   ```

   Aquí, `queue_declare` crea una cola llamada 'hello' con la configuración predeterminada (no duradera, no exclusiva, autoeliminación). `basic_publish` envía el mensaje a la cola.

4. **Cerrar Conexión:**
   Después de enviar, cierra el canal y la conexión para liberar recursos:

   ```php
   $channel->close();
   $connection->close();
   ```

Este proceso es estándar en todas las versiones, sin cambios significativos notados en el registro de cambios para la versión 2.6.* en comparación con los lanzamientos posteriores.

#### Recibiendo Mensajes: Detalles Específicos de la Versión
Recibir mensajes en la versión 2.6.* requiere atención cuidadosa, ya que el mecanismo de consumo difiere de las versiones más recientes. Aquí está el proceso detallado:

1. **Incluir Archivos Requeridos:**
   Similar al envío, incluye el autocargador y las clases necesarias:

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
   Asegúrate de que la cola exista, coincidiendo con la declaración del remitente:

   ```php
   $channel->queue_declare('hello', false, false, false, false);
   ```

4. **Definir Devuelta de Llamada:**
   Crea una función de devolución de llamada para manejar los mensajes recibidos:

   ```php
   $callback = function ($msg) {
       echo ' [x] Recibido ', $msg->body, "\n";
   };
   ```

   Esta función se llamará para cada mensaje, imprimiendo el cuerpo en este ejemplo.

5. **Consumir Mensajes:**
   Para la versión 2.6.*, usa `basic_consume` para registrar la devolución de llamada, luego entra en un bucle para seguir consumiendo:

   ```php
   $channel->basic_consume('hello', '', false, true, false, false, $callback);
   while (count($channel->callbacks)) {
       $channel->wait();
   }
   ```

   El método `basic_consume` toma parámetros para el nombre de la cola, la etiqueta del consumidor, no-local, no-ack, exclusiva, no-wait y la devolución de llamada. El bucle con `wait()` mantiene al consumidor en funcionamiento, verificando mensajes. Este es un detalle importante, ya que las versiones más recientes (por ejemplo, 3.2) podrían usar un método `consume()`, que no estaba disponible en 2.6.* según la revisión de la documentación de la API.

6. **Cerrar Conexión:**
   Después de consumir, cierra los recursos:

   ```php
   $channel->close();
   $connection->close();
   ```

Un detalle inesperado es la necesidad del bucle manual en la versión 2.6.*, lo cual puede requerir manejo adicional de errores para su uso en producción, como capturar excepciones para problemas de conexión.

#### Consideraciones Específicas de la Versión
La versión 2.6.* es parte de los lanzamientos más antiguos, y aunque el registro de cambios no lo enumera explícitamente, las versiones alrededor de 2.5 a 2.7 muestran mejoras como el soporte de latido y la compatibilidad con PHP 5.3. Para mensajes grandes, la versión 2.6.* admite `setBodySizeLimit` en el canal para manejar límites de memoria, truncando mensajes si es necesario, con detalles en [GitHub - php-amqplib/php-amqplib](https://github.com/php-amqplib/php-amqplib).

Comparando con la versión 3.2, los cambios incluyen soporte para PHP 8 y nuevos métodos como `consume()`, pero la funcionalidad básica para enviar y consumir de manera básica sigue siendo similar. Los usuarios deben probar la compatibilidad, especialmente con las versiones de PHP, ya que la versión 2.6.* probablemente admite PHP 5.3 a 7.x, según las entradas del registro de cambios.

#### Solución de Problemas y Mejores Prácticas
- Si el envío falla, verifica los registros de RabbitMQ en busca de alarmas de recursos, como el espacio en disco por debajo de 50 MB, y ajusta los ajustes a través de la [Guía de Configuración de RabbitMQ](https://www.rabbitmq.com/configure.html#config-items).
- Para el consumo, asegúrate de que el consumidor se ejecute continuamente; usa herramientas como Supervisor para demonizar en producción.
- Lista las colas usando `rabbitmqctl list_queues` en Linux o `rabbitmqctl.bat list_queues` en Windows como usuario privilegiado, según las [Herramientas de Línea de Comandos de RabbitMQ](https://www.rabbitmq.com/cli.html).

#### Tabla: Comparación de Versiones para Métodos Clave

| Método             | Comportamiento de la Versión 2.6.*                          | Comportamiento de la Versión 3.2                          |
|--------------------|------------------------------------------------|----------------------------------------------|
| `basic_publish`    | Estándar, publica en la cola                    | Sin cambios, mismo uso                        |
| `basic_consume`    | Requiere bucle con `wait()` para consumir       | Similar, pero método `consume()` disponible     |
| `setBodySizeLimit` | Soporte para mensajes grandes, trunca si se establece | Soporte, misma funcionalidad                |
| Compatibilidad con PHP  | Probablemente 5.3 a 7.x                               | Soporte para PHP 7.x y 8.x                     |

Esta tabla destaca la diferencia clave en el consumo, que es crucial para los usuarios de la versión 2.6.*.

#### Conclusión
Usar "php-amqplib/php-amqplib" versión 2.6.* implica una instalación estándar de Composer, con el envío de mensajes a través de `basic_publish` y la recepción a través de `basic_consume` con un bucle manual. Aunque es similar a las versiones más recientes, el proceso de consumo requiere atención adicional, haciendo esencial que los desarrolladores prueben y ajusten para sistemas heredados. Para más detalles, consulta los tutoriales oficiales de RabbitMQ y el repositorio de GitHub.

---

### Citaciones Clave
- [GitHub - php-amqplib/php-amqplib El cliente de PHP más utilizado para RabbitMQ](https://github.com/php-amqplib/php-amqplib)
- [Tutorial de RabbitMQ - Ejemplo de PHP "Hello World!"](https://www.rabbitmq.com/tutorials/tutorial-one-php)
- [Documentación de CloudAMQP PHP Comienza con CloudAMQP y PHP](https://www.cloudamqp.com/docs/php.html)
- [php-amqplib/php-amqplib Packagist Anteriormente videlalvaro/php-amqplib](https://packagist.org/packages/php-amqplib/php-amqplib)
- [GitHub - php-amqplib/php-amqplib Archivo CHANGELOG](https://github.com/php-amqplib/php-amqplib/blob/master/CHANGELOG.md)
- [Guía de Configuración de RabbitMQ Elementos de configuración y ajustes](https://www.rabbitmq.com/configure.html#config-items)
- [Herramientas de Línea de Comandos de RabbitMQ Referencia y uso de CLI](https://www.rabbitmq.com/cli.html)