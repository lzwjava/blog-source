---
audio: false
generated: true
lang: es
layout: post
title: API de Java para RocksDB
translated: true
type: note
---

Para usar la biblioteca `org.rocksdb`, que es la API de Java para RocksDB—una base de datos embebida de alto rendimiento para datos clave-valor—deberás seguir estos pasos. RocksDB está optimizada para un almacenamiento y recuperación rápidos, lo que la hace ideal para aplicaciones que requieren acceso rápido a los datos mediante claves conocidas. A continuación, se presenta una guía completa para comenzar:

---

### 1. **Agregar la Dependencia**
Para usar `org.rocksdb` en tu proyecto Java, necesitas incluir la dependencia de RocksDB JNI (Java Native Interface). Si estás usando Maven, agrega esto a tu archivo `pom.xml`:

```xml
<dependency>
    <groupId>org.rocksdb</groupId>
    <artifactId>rocksdbjni</artifactId>
    <version>7.10.2</version>
</dependency>
```

Para Gradle, agrega esto a tu `build.gradle`:

```groovy
implementation 'org.rocksdb:rocksdbjni:7.10.2'
```

**Nota**: Consulta [Maven Central](https://search.maven.org/search?q=g:org.rocksdb%20AND%20a:rocksdbjni) para obtener la versión más reciente, ya que `7.10.2` podría no ser la actual.

---

### 2. **Cargar la Biblioteca Nativa**
RocksDB depende de código nativo en C++, por lo que debes cargar la biblioteca nativa antes de usarla. Agrega esta línea al inicio de tu código:

```java
RocksDB.loadLibrary();
```

Si no lo haces, se producirán errores en tiempo de ejecución.

---

### 3. **Abrir una Base de Datos**
Para comenzar a usar RocksDB, necesitas abrir una instancia de la base de datos especificando una ruta de archivo donde se almacenará. Usa la clase `Options` para configurar los ajustes, como crear la base de datos si no existe:

```java
import org.rocksdb.Options;
import org.rocksdb.RocksDB;

Options options = new Options().setCreateIfMissing(true);
RocksDB db = RocksDB.open(options, "/ruta/a/la/db");
```

- **`options`**: Configura el comportamiento de la base de datos (por ejemplo, `setCreateIfMissing(true)` asegura que la base de datos se cree si no existe).
- **`/ruta/a/la/db`**: Reemplaza esto con una ruta de directorio válida en tu sistema donde residirán los archivos de la base de datos.

---

### 4. **Realizar Operaciones Básicas**
RocksDB es un almacén clave-valor, y sus operaciones principales son `put`, `get` y `delete`. Las claves y los valores se almacenan como arrays de bytes, por lo que necesitarás convertir los datos (por ejemplo, cadenas) a bytes.

- **Put**: Insertar o actualizar un par clave-valor.
  ```java
  db.put("key".getBytes(), "value".getBytes());
  ```

- **Get**: Recuperar el valor asociado a una clave.
  ```java
  byte[] value = db.get("key".getBytes());
  if (value != null) {
      System.out.println(new String(value));  // Imprime "value"
  } else {
      System.out.println("Clave no encontrada");
  }
  ```

- **Delete**: Eliminar un par clave-valor.
  ```java
  db.delete("key".getBytes());
  ```

---

### 5. **Cerrar la Base de Datos**
Cerrar la base de datos correctamente es esencial para liberar recursos. La forma más fácil es usar un bloque try-with-resources, que cierra automáticamente la base de datos cuando terminas:

```java
try (RocksDB db = RocksDB.open(options, "/ruta/a/la/db")) {
    // Realizar operaciones aquí
} catch (Exception e) {
    e.printStackTrace();
}
```

---

### 6. **Manejar Excepciones**
Las operaciones de RocksDB pueden lanzar `RocksDBException`, así que siempre incluye el manejo de excepciones para evitar fugas de recursos o corrupción de datos:

```java
try {
    db.put("key".getBytes(), "value".getBytes());
} catch (RocksDBException e) {
    e.printStackTrace();
}
```

---

### 7. **Opciones de Configuración**
Puedes ajustar el rendimiento de RocksDB usando la clase `Options`. Por ejemplo:

```java
Options options = new Options()
    .setCreateIfMissing(true)
    .setWriteBufferSize(64 * 1024 * 1024);  // Búfer de escritura de 64MB
```

Las opciones comunes incluyen:
- `setWriteBufferSize`: Controla la memoria utilizada para escrituras.
- `setMaxOpenFiles`: Limita el número de archivos abiertos.
- `setCompactionStyle`: Ajusta cómo se compactan los datos en el disco.

Explora la [documentación de RocksDB](https://github.com/facebook/rocksdb/wiki) para más opciones.

---

### 8. **Ejemplo Sencillo**
Aquí tienes un ejemplo completo que demuestra abrir una base de datos, almacenar un par clave-valor y recuperarlo:

```java
import org.rocksdb.RocksDB;
import org.rocksdb.Options;

public class SimpleRocksDBExample {
    public static void main(String[] args) {
        RocksDB.loadLibrary();  // Cargar la biblioteca nativa
        Options options = new Options().setCreateIfMissing(true);
        
        try (RocksDB db = RocksDB.open(options, "/tmp/rocksdb_example")) {
            // Poner un par clave-valor
            db.put("hello".getBytes(), "world".getBytes());
            
            // Obtener el valor
            byte[] value = db.get("hello".getBytes());
            if (value != null) {
                System.out.println(new String(value));  // Imprime "world"
            } else {
                System.out.println("Clave no encontrada");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

**Salida**: `world`

---

### Consideraciones Clave
- **Naturaleza Embebida**: RocksDB se ejecuta dentro del proceso de tu aplicación, no como un servidor separado.
- **Arrays de Bytes**: Las claves y los valores son `byte[]`, por lo que necesitarás manejar la serialización/deserialización para objetos complejos.
- **Rendimiento**: RocksDB destaca con almacenamiento rápido (por ejemplo, SSD) y se usa en sistemas de alto rendimiento como los de Facebook, donde fue desarrollada.
- **No es Relacional**: Es un almacén clave-valor, no una base de datos relacional—no tiene SQL ni joins.

---

### Errores Comunes
- **Olvidar `RocksDB.loadLibrary()`**: Provoca `UnsatisfiedLinkError`.
- **Manejo Inadecuado de Recursos**: No cerrar la base de datos puede causar problemas, especialmente en sistemas con recursos limitados.
- **Errores de Tipo de Datos**: Pasar cadenas u objetos directamente en lugar de convertirlos a `byte[]`.

---

### Para Avanzar
- **Características Avanzadas**: Explora transacciones, snapshots o familias de columnas para casos de uso más complejos.
- **Recursos**: Consulta la [API de Java de RocksDB](https://github.com/facebook/rocksdb/tree/main/java) y el [Wiki de RocksDB](https://github.com/facebook/rocksdb/wiki) para documentación detallada y ejemplos.

Esta guía proporciona una base sólida para usar `org.rocksdb`. Si necesitas ayuda con características específicas o casos de uso, ¡no dudes en preguntar!