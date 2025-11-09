---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Guía Integral de MongoDB
translated: true
type: note
---

MongoDB es una base de datos de documentos NoSQL de código abierto popular diseñada para el desarrollo moderno de aplicaciones. Almacena datos en documentos flexibles similares a JSON llamados BSON (Binary JSON), lo que la hace ideal para manejar datos no estructurados o semiestructurados. A diferencia de las bases de datos relacionales tradicionales, MongoDB utiliza un enfoque sin esquema, permitiendo que las colecciones (grupos de documentos) tengan estructuras variables. Es altamente escalable, soporta escalado horizontal mediante sharding, y proporciona alta disponibilidad mediante replicación. MongoDB puede desplegarse on-premise, en la nube a través de MongoDB Atlas (un servicio gestionado), o en entornos híbridos. Esta guía cubre todo desde lo básico hasta temas avanzados, con ejemplos usando MongoDB Shell (mongosh).

## Introducción

MongoDB sobresale en escenarios que requieren desarrollo rápido, modelos de datos flexibles y alto rendimiento. Las características clave incluyen:
- **Modelo de Documento**: Los datos como documentos autocontenidos con estructuras anidadas.
- **Lenguaje de Consulta**: Consultas ricas usando una sintaxis similar a objetos JavaScript.
- **Escalabilidad**: Soporte incorporado para sistemas distribuidos.
- **Ecosistema**: Se integra con lenguajes como Python, Node.js, Java a través de controladores oficiales.

Es utilizado por empresas como Adobe, eBay y Forbes para aplicaciones que involucran big data, análisis en tiempo real y gestión de contenidos.

## Instalación

MongoDB ofrece ediciones Community (gratuita, de código abierto) y Enterprise. La instalación varía según la plataforma; descargue siempre desde el sitio oficial por seguridad.

### Windows
- Descargue el instalador MSI desde el MongoDB Download Center.
- Ejecute el instalador, seleccione la configuración "Completa" e incluya MongoDB Compass (herramienta GUI).
- Agregue el directorio `bin` de MongoDB (ej., `C:\Program Files\MongoDB\Server\8.0\bin`) a su PATH.
- Cree un directorio de datos: `mkdir -p C:\data\db`.
- Inicie el servidor: `mongod.exe --dbpath C:\data\db`.

Soportado: Windows 11, Server 2022/2019.

### macOS
- Use Homebrew: `brew tap mongodb/brew && brew install mongodb-community`.
- O descargue el archivo TGZ, extráigalo y agréguelo al PATH.
- Cree el directorio de datos: `mkdir -p /data/db`.
- Inicie: `mongod --dbpath /data/db` (o use `brew services start mongodb/brew/mongodb-community`).

Soportado: macOS 11–14 (x86_64 y arm64).

### Linux
- Para Ubuntu/Debian: Agregue la clave del repositorio de MongoDB y la lista, luego `apt-get install -y mongodb-org`.
- Para RHEL/CentOS: Use yum/dnf con el archivo del repositorio.
- Cree el directorio de datos: `sudo mkdir -p /data/db && sudo chown -R $USER /data/db`.
- Inicie: `sudo systemctl start mongod`.

Soportado: Ubuntu 24.04, RHEL 9+, Debian 12, Amazon Linux 2023, etc. Use sistemas de archivos XFS/EXT4; evite 32 bits.

### Nube (MongoDB Atlas)
- Regístrese en mongodb.com/atlas.
- Cree un clúster gratuito mediante la UI o CLI: `atlas clusters create <nombre> --provider AWS --region us-east-1 --tier M0`.
- Incluya su IP en la lista blanca: `atlas network-access create <IP>`.
- Obtenga la cadena de conexión y conéctese: `mongosh "mongodb+srv://<usuario>:<contraseña>@cluster0.abcde.mongodb.net/"`.

Atlas maneja automáticamente las copias de seguridad, el escalado y el monitoreo.

## Conceptos Básicos

### Bases de Datos
Contenedores para colecciones, que separan lógicamente los datos. Se crean implícitamente en el primer uso: `use midb`. Cambie con `use midb`. Listar: `show dbs`.

### Colecciones
Grupos de documentos, como tablas pero con esquema flexible. Se crean implícitamente: `db.micoleccion.insertOne({})`. Listar: `show collections`.

### Documentos
Unidades básicas: objetos BSON con pares clave-valor. Ejemplo:
```javascript
{ "_id": ObjectId("..."), "nombre": "Juan", "edad": 30, "direccion": { "ciudad": "NYC", "codigo_postal": 10001 } }
```
Soporta arrays, objetos anidados y tipos como fechas, binarios.

### BSON
Formato binario para almacenamiento/red eficiente. Extiende JSON con tipos como ObjectId, Date, Binary.

### Espacios de Nombres
Identificadores únicos: `base_de_datos.coleccion` (ej., `midb.pedidos`).

Configuración de ejemplo:
```javascript
use test
db.pedidos.insertMany([
  { articulo: "almendras", precio: 12, cantidad: 2 },
  { articulo: "nueces", precio: 20, cantidad: 1 }
])
```

## Operaciones CRUD

Use `db.coleccion.metodo()` en mongosh. Transacciones mediante sesiones para ACID multi-documento.

### Crear (Insertar)
- Simple: `db.usuarios.insertOne({ nombre: "Alicia", email: "alicia@ejemplo.com" })`
- Múltiples: `db.usuarios.insertMany([{ nombre: "Roberto" }, { nombre: "Carlos" }])`
Devuelve los IDs insertados.

### Leer (Buscar)
- Todos: `db.usuarios.find()`
- Filtrados: `db.usuarios.find({ edad: { $gt: 25 } })`
- Impresión formateada: `.pretty()`
- Límite/ordenar: `db.usuarios.find().limit(5).sort({ edad: -1 })`

### Actualizar
- Simple: `db.usuarios.updateOne({ nombre: "Alicia" }, { $set: { edad: 31 } })`
- Múltiples: `db.usuarios.updateMany({ edad: { $lt: 20 } }, { $set: { estado: "menor" } })`
- Incrementar: `{ $inc: { puntuacion: 10 } }`

### Eliminar
- Simple: `db.usuarios.deleteOne({ nombre: "Roberto" })`
- Múltiples: `db.usuarios.deleteMany({ estado: "inactivo" })`
- Eliminar colección: `db.usuarios.drop()`

## Consultas e Indexación

### Consultas
Use predicados para condiciones. Soporta igualdad, rangos, operadores lógicos.

- Básica: `db.inventario.find({ estado: "A" })` (equivalente SQL: `WHERE estado = 'A'`)
- $in: `db.inventario.find({ estado: { $in: ["A", "D"] } })`
- $lt/$gt: `db.inventario.find({ cantidad: { $lt: 30 } })`
- $or: `db.inventario.find({ $or: [{ estado: "A" }, { cantidad: { $lt: 30 } }] })`
- Regex: `db.inventario.find({ articulo: /^p/ })` (comienza con "p")
- Incrustado: `db.usuarios.find({ "direccion.ciudad": "NYC" })`

Proyección (seleccionar campos): `db.usuarios.find({ edad: { $gt: 25 } }, { nombre: 1, _id: 0 })`

### Indexación
Mejora la velocidad de las consultas al evitar escaneos completos. Basado en B-tree.

- Tipos: Campo único (`db.usuarios.createIndex({ nombre: 1 })`), Compuesto (`{ nombre: 1, edad: -1 }`), Único (`{ email: 1 }`).
- Beneficios: Consultas de igualdad/rango más rápidas, resultados ordenados.
- Creación: `db.usuarios.createIndex({ edad: 1 })` (ascendente).
- Ver: `db.usuarios.getIndexes()`
- Eliminar: `db.usuarios.dropIndex("edad_1")`

Use Atlas Performance Advisor para recomendaciones. Contrapartida: Escrituras más lentas.

## Marco de Agregación

Procesa datos a través de etapas en un pipeline. Como SQL GROUP BY pero más potente.

- Básico: `db.pedidos.aggregate([ { $match: { precio: { $lt: 15 } } } ])`
- Etapas: `$match` (filtrar), `$group` (agregar: `{ $sum: "$precio" }`), `$sort`, `$lookup` (unir: `{ from: "inventario", localField: "articulo", foreignField: "sku", as: "stock" }`), `$project` (remodelar).
- Ejemplo (unir y ordenar):
```javascript
db.pedidos.aggregate([
  { $match: { precio: { $lt: 15 } } },
  { $lookup: { from: "inventario", localField: "articulo", foreignField: "sku", as: "documentos_inventario" } },
  { $sort: { precio: 1 } }
])
```
Expresiones: `{ $add: [ "$precio", 10 ] }`. Vista previa en la UI de Atlas.

## Diseño de Esquema

La flexibilidad de MongoDB evita esquemas rígidos pero requiere un diseño reflexivo para el rendimiento.

- **Principios**: Modele para los patrones de acceso (lecturas/escrituras), use índices, mantenga el working set en RAM.
- **Incrustación**: Desnormalice datos relacionados en un documento para lecturas/escrituras atómicas. Ej., incruste comentarios en publicaciones. Pros: Consultas rápidas. Contras: Duplicación, documentos grandes.
- **Referenciación**: Normalice con IDs. Ej., `publicaciones` referencia `usuarios` via `userId`. Use `$lookup` para uniones. Pros: Menos duplicación. Contras: Múltiples consultas.
- Patrones: Uno-a-pocos (incrustar), uno-a-muchos (referencia o incrustar array), muchos-a-muchos (referencia).
- Validación: Imponga con `db.createCollection("usuarios", { validador: { $jsonSchema: { ... } } })`.

Considere las contrapartidas de duplicación y atomicidad (solo a nivel de documento).

## Replicación y Sharding

### Replicación
Proporciona redundancia/alta disponibilidad a través de conjuntos de réplicas (grupo de instancias `mongod`).

- Componentes: Primario (escrituras), Secundarios (replican via oplog, lecturas opcionales), Árbitro (vota, sin datos).
- Despliegue: Inicie con `rs.initiate({ _id: "rs0", miembros: [{ _id: 0, host: "host1:27017" }] })`. Agregue miembros: `rs.add("host2:27017")`.
- Elecciones: Si el primario falla, un secundario es elegido en ~10-12s.
- Preferencia de Lectura: `primary`, `secondary` (puede tener retraso).
- Úselo para failover, copias de seguridad. Habilite el control de flujo para gestionar el retraso.

### Sharding
Escalado horizontal: Distribuye datos a través de shards.

- Componentes: Shards (conjuntos de réplicas), Mongos (enrutadores), Servidores de configuración (metadatos).
- Clave de Shard: Campo(s) para particionar (ej., hashed para distribución uniforme). Cree el índice primero.
- Configuración: Habilite sharding `sh.enableSharding("midb")`, fragmente la colección `sh.shardCollection("midb.usuarios", { userId: "hashed" })`.
- Balanceador: Migra chunks para carga uniforme. Zonas para localidad geográfica.
- Estrategias: Hashed (uniforme), Por rangos (consultas dirigidas).

Conéctese via mongos; soporta transacciones.

## Seguridad

Proteja los despliegues con protecciones en capas.

- **Autenticación**: SCRAM, LDAP, OIDC, X.509. Cree usuarios: `db.createUser({ user: "admin", pwd: "pass", roles: ["root"] })`.
- **Autorización**: Control de Acceso Basado en Roles (RBAC). Roles incorporados: read, readWrite, dbAdmin.
- **Cifrado**: TLS/SSL para tránsito, Cifrado en Reposo (EAR) via AWS KMS/Google Cloud KMS/Azure Key Vault. Cifrado a Nivel de Campo del Lado del Cliente (CSFLE) para campos sensibles.
- Red: Listas de acceso IP, VPC peering en Atlas.
- Auditoría: Registre operaciones.

Habilite autenticación al inicio: `--auth`. Use Atlas para seguridad incorporada.

## Mejores Prácticas

- **Configuración de Producción**: Ejecute como servicio (systemctl/brew). Separe datos/journal/logs en SSDs. Use el motor WiredTiger (por defecto).
- **Monitoreo**: `mongostat`, `mongotop`, gráficos de Atlas. Vigile conexiones (`connPoolStats`), expulsiones de caché, I/O (`iostat`).
- **Copias de Seguridad**: `mongodump`/`mongorestore`, o instantáneas de Atlas. Lógicas (