---
audio: false
generated: true
lang: es
layout: post
title: Guía de Redis
translated: true
type: note
---

Aquí tienes una guía completa de Redis, un almacén de estructuras de datos en memoria de código abierto ampliamente utilizado como base de datos, caché y agente de mensajes. Esta guía cubrirá sus fundamentos, características, casos de uso, instalación, operaciones básicas y conceptos avanzados.

---

### ¿Qué es Redis?
Redis (Remote Dictionary Server) es un almacén de clave-valor de alto rendimiento que opera principalmente en memoria, lo que lo hace excepcionalmente rápido. Soporta varias estructuras de datos como cadenas, hashes, listas, conjuntos, conjuntos ordenados, mapas de bits, hyperloglogs e índices geoespaciales. Creado por Salvatore Sanfilippo en 2009, Redis ahora es mantenido por una comunidad y patrocinado por Redis Inc.

Características clave:
- **En memoria**: Los datos se almacenan en RAM para acceso de baja latencia.
- **Persistente**: Ofrece persistencia opcional en disco para durabilidad.
- **Versátil**: Soporta estructuras de datos complejas más allá de simples pares clave-valor.
- **Escalable**: Proporciona clustering y replicación para alta disponibilidad.

---

### ¿Por qué usar Redis?
Redis es popular por su velocidad y flexibilidad. Los casos de uso comunes incluyen:
1. **Caché**: Acelera las aplicaciones almacenando datos de acceso frecuente (ej., respuestas de API, páginas web).
2. **Gestión de Sesiones**: Almacena datos de sesión de usuario en aplicaciones web.
3. **Análisis en Tiempo Real**: Realiza seguimiento de métricas, tablas de clasificación o contadores de eventos.
4. **Mensajería Pub/Sub**: Permite la mensajería en tiempo real entre procesos o servicios.
5. **Colas de Tareas**: Gestiona trabajos en segundo plano (ej., con herramientas como Celery).
6. **Aplicaciones Geoespaciales**: Maneja consultas basadas en ubicación (ej., encontrar puntos de interés cercanos).

---

### Características Clave
1. **Estructuras de Datos**:
   - **Cadenas**: Pares simples clave-valor (ej., `SET clave "valor"`).
   - **Listas**: Colecciones ordenadas (ej., `LPUSH milista "elemento"`).
   - **Conjuntos**: Colecciones no ordenadas y únicas (ej., `SADD miconjunto "elemento"`).
   - **Conjuntos Ordenados**: Conjuntos con puntuaciones para clasificación (ej., `ZADD tabla_clasificación 100 "jugador1"`).
   - **Hashes**: Mapeos clave-valor (ej., `HSET usuario:1 nombre "Alicia"`).
   - **Mapas de Bits, HyperLogLogs, Streams**: Para casos de uso especializados como contar usuarios únicos o streaming de eventos.

2. **Persistencia**:
   - **RDB (Snapshotting)**: Guarda periódicamente los datos en disco como una instantánea en un momento dado.
   - **AOF (Archivo de Sólo Añadir)**: Registra cada operación de escritura para durabilidad; se puede reproducir para reconstruir el conjunto de datos.

3. **Replicación**: Replicación maestro-esclavo para alta disponibilidad y escalabilidad de lectura.
4. **Clustering**: Distribuye datos a través de múltiples nodos para escalado horizontal.
5. **Operaciones Atómicas**: Garantiza un acceso concurrente seguro con comandos como `INCR` o `MULTI`.
6. **Scripting Lua**: Permite lógica personalizada en el servidor.
7. **Pub/Sub**: Sistema de mensajería ligero para comunicación en tiempo real.

---

### Instalación
Redis está disponible en Linux, macOS y Windows (vía WSL o compilaciones no oficiales). Así es como instalarlo en un sistema Linux:

1. **Mediante el Gestor de Paquetes** (Ubuntu/Debian):
   ```bash
   sudo apt update
   sudo apt install redis-server
   ```

2. **Desde el Código Fuente**:
   ```bash
   wget http://download.redis.io/releases/redis-7.0.15.tar.gz
   tar xzf redis-7.0.15.tar.gz
   cd redis-7.0.15
   make
   sudo make install
   ```

3. **Iniciar Redis**:
   ```bash
   redis-server
   ```

4. **Verificar la Instalación**:
   ```bash
   redis-cli ping
   ```
   Salida: `PONG`

5. **Configuración**: Edita `/etc/redis/redis.conf` (o equivalente) para ajustar configuraciones como persistencia, límites de memoria o enlace a IPs específicas.

---

### Operaciones Básicas
Redis utiliza una interfaz simple basada en comandos a través de `redis-cli` o bibliotecas cliente. Aquí hay algunos ejemplos:

#### Cadenas
- Establecer un valor: `SET nombre "Alicia"`
- Obtener un valor: `GET nombre` → `"Alicia"`
- Incrementar: `INCR contador` → `1` (incrementa a 2, 3, etc.)

#### Listas
- Añadir a la izquierda: `LPUSH milista "elemento1"`
- Añadir a la derecha: `RPUSH milista "elemento2"`
- Sacar de la izquierda: `LPOP milista` → `"elemento1"`

#### Conjuntos
- Añadir elementos: `SADD miconjunto "manzana" "plátano"`
- Listar miembros: `SMEMBERS miconjunto` → `"manzana" "plátano"`
- Verificar membresía: `SISMEMBER miconjunto "manzana"` → `1` (verdadero)

#### Hashes
- Establecer campos: `HSET usuario:1 nombre "Bob" edad "30"`
- Obtener campo: `HGET usuario:1 nombre` → `"Bob"`
- Obtener todos los campos: `HGETALL usuario:1`

#### Conjuntos Ordenados
- Añadir con puntuación: `ZADD tabla_clasificación 100 "jugador1" 200 "jugador2"`
- Obtener las mejores puntuaciones: `ZRANGE tabla_clasificación 0 1 WITHSCORES` → `"jugador1" "100" "jugador2" "200"`

---

### Conceptos Avanzados
1. **Configuración de Persistencia**:
   - Habilitar RDB: Establecer `save 60 1000` en `redis.conf` (guardar cada 60s si 1000 claves cambian).
   - Habilitar AOF: Establecer `appendonly yes` para el registro de escrituras.

2. **Replicación**:
   - Configurar un esclavo: `SLAVEOF ip_maestro puerto_maestro`.
   - Verificar estado: `INFO REPLICATION`.

3. **Clustering**:
   - Habilitar con `cluster-enabled yes` en `redis.conf`.
   - Usar `redis-cli --cluster create` para configurar nodos.

4. **Políticas de Expulsión**:
   - Controlar el uso de memoria con `maxmemory` y políticas como `LRU` (menos usado recientemente) o `LFU` (menos usado frecuentemente).
   - Ejemplo: `maxmemory-policy allkeys-lru`.

5. **Transacciones**:
   - Agrupar comandos: `MULTI`, seguido de comandos, luego `EXEC`.
   - Ejemplo:
     ```
     MULTI
     SET clave1 "valor1"
     SET clave2 "valor2"
     EXEC
     ```

6. **Pub/Sub**:
   - Suscribirse: `SUBSCRIBE canal1`
   - Publicar: `PUBLISH canal1 "Hola"`

---

### Bibliotecas Cliente
Redis soporta muchos lenguajes de programación. Ejemplos:
- **Python**: `redis-py` (`pip install redis`)
  ```python
  import redis
  r = redis.Redis(host='localhost', port=6379, db=0)
  r.set('clave', 'valor')
  print(r.get('clave'))  # b'valor'
  ```
- **Node.js**: `ioredis`
  ```javascript
  const Redis = require('ioredis');
  const redis = new Redis();
  redis.set('clave', 'valor');
  redis.get('clave').then(console.log); // 'valor'
  ```

---

### Consejos de Rendimiento
1. **Usar Pipelining**: Agrupa comandos para reducir la latencia de ida y vuelta.
2. **Optimizar Estructuras de Datos**: Elige la estructura correcta (ej., usa hashes para objetos pequeños en lugar de múltiples claves).
3. **Monitorear la Memoria**: Usa `INFO MEMORY` para rastrear el uso.
4. **Ajustar la Persistencia**: Equilibra velocidad (RDB) y durabilidad (AOF).

---

### Seguridad
- **Vincular a localhost**: Establece `bind 127.0.0.1` en `redis.conf` para restringir el acceso.
- **Establecer una Contraseña**: Usa `requirepass tupassword`.
- **Deshabilitar Comandos Peligrosos**: Usa `rename-command` (ej., `rename-command FLUSHALL ""`).

---

### Limitaciones
- **Limitado por la Memoria**: El tamaño de los datos está limitado por la RAM disponible.
- **Monohilo**: Las operaciones principales se ejecutan en un solo hilo (aunque la E/S y la persistencia pueden usar múltiples hilos en versiones más nuevas).
- **Sin Consultas Complejas**: Carece de consultas tipo SQL; se basa en el acceso por clave.

---

### Redis vs. Otras Bases de Datos
- **Redis vs. Memcached**: Redis ofrece estructuras de datos más ricas y persistencia; Memcached es más simple y puramente en memoria.
- **Redis vs. MongoDB**: Redis es más rápido para el caché pero menos adecuado para el almacenamiento persistente complejo de documentos.
- **Redis vs. PostgreSQL**: Redis sobresale en tareas en tiempo real y de baja latencia; PostgreSQL es mejor para datos relacionales y cumplimiento ACID.

---

### Recursos
- **Documentación Oficial**: [redis.io](https://redis.io)
- **Probar Redis**: [try.redis.io](https://try.redis.io) (tutorial interactivo)
- **GitHub**: [github.com/redis/redis](https://github.com/redis/redis)

---

Esta guía proporciona una base sólida para comprender y usar Redis. ¡Házme saber si te gustaría una inmersión más profunda en algún aspecto específico!