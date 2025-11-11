---
audio: false
generated: true
lang: es
layout: post
title: SDK de PHP de Qiniu
translated: true
type: note
---

Para usar `"qiniu/php-sdk": "^7.0"` en PHP, necesitarás integrar el Qiniu PHP SDK en tu proyecto. Este SDK te permite interactuar con los servicios de Qiniu Cloud Storage, como subir archivos, gestionar buckets y más. A continuación, encontrarás una guía paso a paso para comenzar:

---

### 1. Instalar el Qiniu PHP SDK
La forma recomendada de instalar el SDK es mediante Composer, un gestor de dependencias para PHP. Asegúrate de tener Composer instalado en tu sistema.

#### Pasos:
- Abre tu terminal y navega hasta el directorio de tu proyecto.
- Ejecuta el siguiente comando para agregar el Qiniu PHP SDK (versión 7.x) a tu proyecto:
  ```bash
  composer require qiniu/php-sdk "^7.0"
  ```
- Composer descargará el SDK y sus dependencias en el directorio `vendor/` y generará un archivo de autocarga.

Si no tienes Composer instalado, puedes descargarlo desde [getcomposer.org](https://getcomposer.org/).

---

### 2. Configurar tu proyecto
Después de la instalación, necesitas incluir el autocargador en tu script PHP para usar las clases del SDK.

#### Ejemplo:
Crea un archivo PHP (por ejemplo, `index.php`) en el directorio de tu proyecto y agrega la siguiente línea en la parte superior:
```php
require_once 'vendor/autoload.php';
```

Esto asegura que las clases del SDK se carguen automáticamente cuando sea necesario.

---

### 3. Configurar la autenticación
Para usar el SDK de Qiniu, necesitarás tu `AccessKey` y `SecretKey` de Qiniu, que puedes obtener desde el panel de control de tu cuenta de Qiniu.

#### Ejemplo:
```php
use Qiniu\Auth;

$accessKey = 'TU_ACCESS_KEY';
$secretKey = 'TU_SECRET_KEY';

$auth = new Auth($accessKey, $secretKey);
```

Reemplaza `'TU_ACCESS_KEY'` y `'TU_SECRET_KEY'` con tus credenciales reales.

---

### 4. Uso básico: Subir un archivo
Una de las tareas más comunes con el SDK de Qiniu es subir archivos a un bucket. Aquí tienes un ejemplo de cómo subir un archivo local.

#### Ejemplo:
```php
use Qiniu\Storage\UploadManager;

$bucket = 'NOMBRE_DE_TU_BUCKET'; // Reemplaza con el nombre de tu bucket de Qiniu
$filePath = '/ruta/a/tu/archivo.txt'; // Ruta al archivo que quieres subir
$key = 'archivo.txt'; // El nombre del archivo en el almacenamiento de Qiniu (puede ser null para usar el nombre original)

$token = $auth->uploadToken($bucket); // Genera un token de subida
$uploadMgr = new UploadManager();

list($ret, $error) = $uploadMgr->putFile($token, $key, $filePath);

if ($error !== null) {
    echo "La subida falló: " . $error->message();
} else {
    echo "¡Subida exitosa! Hash del archivo: " . $ret['hash'];
}
```

- `$bucket`: El nombre de tu bucket de Qiniu.
- `$filePath`: La ruta local al archivo que quieres subir.
- `$key`: La clave (nombre) del archivo bajo la cual se almacenará en Qiniu. Si se establece en `null`, Qiniu generará una clave basada en el hash del archivo.
- `$token`: Un token de subida generado usando tus credenciales y el nombre del bucket.
- El método `putFile` retorna un array: `$ret` (información de éxito) y `$error` (información de error, si la hay).

---

### 5. Funcionalidades adicionales
El Qiniu PHP SDK proporciona muchas otras funcionalidades, tales como:
- **Gestionar Buckets**: Usa `Qiniu\Storage\BucketManager` para listar archivos, eliminar archivos o gestionar la configuración del bucket.
- **Operaciones con archivos**: Copiar, mover o eliminar archivos en tu bucket.
- **Procesamiento de imágenes**: Generar URLs para imágenes redimensionadas o formateadas.

#### Ejemplo: Listar archivos en un bucket
```php
use Qiniu\Storage\BucketManager;

$bucketMgr = new BucketManager($auth);
list($ret, $error) = $bucketMgr->listFiles($bucket);

if ($error !== null) {
    echo "Error: " . $error->message();
} else {
    echo "Archivos en el bucket:\n";
    foreach ($ret['items'] as $item) {
        echo $item['key'] . "\n";
    }
}
```

---

### 6. Manejo de errores
Siempre verifica la variable `$error` después de las operaciones del SDK. Si una operación falla, `$error` contendrá detalles sobre lo que salió mal.

#### Ejemplo:
```php
if ($error !== null) {
    var_dump($error);
} else {
    var_dump($ret);
}
```

---

### 7. Requisitos
- Versión de PHP: La versión del SDK `^7.0` es compatible con PHP 5.3.3 y superior (hasta PHP 8.x en versiones posteriores).
- Extensiones: Asegúrate de que las extensiones `cURL` y `xml` de PHP estén habilitadas, ya que son requeridas por el SDK.

Puedes verificar tu versión de PHP y las extensiones con:
```bash
php -v
php -m
```

---

### 8. Qué hacer después
- **Documentación**: Para más detalles, consulta la [documentación oficial del Qiniu PHP SDK](https://developer.qiniu.com/kodo/sdk/php) o el [repositorio de GitHub](https://github.com/qiniu/php-sdk).
- **Ejemplos**: Revisa el directorio `examples/` en el repositorio de GitHub para más casos de uso.
- **Soporte**: Si encuentras problemas, envía un ticket al soporte de Qiniu (<support@qiniu.com>) o pregunta en sus foros comunitarios.

---

### Código de ejemplo completo
Aquí tienes un script completo para subir un archivo:
```php
<?php
require_once 'vendor/autoload.php';

use Qiniu\Auth;
use Qiniu\Storage\UploadManager;

$accessKey = 'TU_ACCESS_KEY';
$secretKey = 'TU_SECRET_KEY';
$bucket = 'NOMBRE_DE_TU_BUCKET';
$filePath = '/ruta/a/tu/archivo.txt';
$key = 'archivo.txt';

$auth = new Auth($accessKey, $secretKey);
$token = $auth->uploadToken($bucket);
$uploadMgr = new UploadManager();

list($ret, $error) = $uploadMgr->putFile($token, $key, $filePath);

if ($error !== null) {
    echo "La subida falló: " . $error->message();
} else {
    echo "¡Subida exitosa! Hash del archivo: " . $ret['hash'];
}
```

Reemplaza los valores de marcador de posición (`TU_ACCESS_KEY`, `TU_SECRET_KEY`, `NOMBRE_DE_TU_BUCKET`, `/ruta/a/tu/archivo.txt`) con tus datos reales, ¡y estarás listo!

¡Avísame si necesitas ayuda con una funcionalidad específica!