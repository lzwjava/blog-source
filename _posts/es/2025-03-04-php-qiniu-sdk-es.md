---
audio: false
generated: true
lang: es
layout: post
title: Qiniu PHP SDK
translated: true
---

Para usar `"qiniu/php-sdk": "^7.0"` en PHP, necesitarás integrar el SDK de PHP de Qiniu en tu proyecto. Este SDK te permite interactuar con los servicios de almacenamiento en la nube de Qiniu, como subir archivos, gestionar cubos y más. A continuación, se presenta una guía paso a paso para comenzar:

---

### 1. Instalar el SDK de PHP de Qiniu
La forma recomendada de instalar el SDK es a través de Composer, un gestor de dependencias para PHP. Asegúrate de tener Composer instalado en tu sistema.

#### Pasos:
- Abre tu terminal y navega hasta el directorio de tu proyecto.
- Ejecuta el siguiente comando para agregar el SDK de PHP de Qiniu (versión 7.x) a tu proyecto:
  ```bash
  composer require qiniu/php-sdk "^7.0"
  ```
- Composer descargará el SDK y sus dependencias en el directorio `vendor/` y generará un archivo de autocarga.

Si no tienes Composer instalado, puedes descargarlo desde [getcomposer.org](https://getcomposer.org/).

---

### 2. Configurar tu Proyecto
Después de la instalación, necesitarás incluir el autoloader en tu script de PHP para usar las clases del SDK.

#### Ejemplo:
Crea un archivo PHP (por ejemplo, `index.php`) en el directorio de tu proyecto y agrega la siguiente línea al principio:
```php
require_once 'vendor/autoload.php';
```

Esto asegura que las clases del SDK se carguen automáticamente cuando sea necesario.

---

### 3. Configurar la Autenticación
Para usar el SDK de Qiniu, necesitarás tu `AccessKey` y `SecretKey` de Qiniu, que puedes obtener desde el panel de control de tu cuenta de Qiniu.

#### Ejemplo:
```php
use Qiniu\Auth;

$accessKey = 'YOUR_ACCESS_KEY';
$secretKey = 'YOUR_SECRET_KEY';

$auth = new Auth($accessKey, $secretKey);
```

Reemplaza `'YOUR_ACCESS_KEY'` y `'YOUR_SECRET_KEY'` con tus credenciales reales.

---

### 4. Uso Básico: Subir un Archivo
Una de las tareas más comunes con el SDK de Qiniu es subir archivos a un cubo. Aquí tienes un ejemplo de cómo subir un archivo local.

#### Ejemplo:
```php
use Qiniu\Storage\UploadManager;

$bucket = 'YOUR_BUCKET_NAME'; // Reemplaza con el nombre de tu cubo de Qiniu
$filePath = '/ruta/a/tu/archivo.txt'; // Ruta al archivo que deseas subir
$key = 'archivo.txt'; // El nombre del archivo en el almacenamiento de Qiniu (puede ser nulo para usar el nombre del archivo original)

$token = $auth->uploadToken($bucket); // Generar un token de subida
$uploadMgr = new UploadManager();

list($ret, $error) = $uploadMgr->putFile($token, $key, $filePath);

if ($error !== null) {
    echo "La subida falló: " . $error->message();
} else {
    echo "Subida exitosa! Hash del archivo: " . $ret['hash'];
}
```

- `$bucket`: El nombre de tu cubo de Qiniu.
- `$filePath`: La ruta local al archivo que deseas subir.
- `$key`: La clave del archivo (nombre) bajo la cual se almacenará en Qiniu. Si se establece en `null`, Qiniu generará una clave basada en el hash del archivo.
- `$token`: Un token de subida generado usando tus credenciales y el nombre del cubo.
- El método `putFile` devuelve un array: `$ret` (información de éxito) y `$error` (información de error, si la hay).

---

### 5. Funcionalidades Adicionales
El SDK de PHP de Qiniu proporciona muchas otras funcionalidades, como:
- **Gestión de Cubos**: Usa `Qiniu\Storage\BucketManager` para listar archivos, eliminar archivos o gestionar la configuración del cubo.
- **Operaciones de Archivos**: Copiar, mover o eliminar archivos en tu cubo.
- **Procesamiento de Imágenes**: Generar URLs para imágenes redimensionadas o formateadas.

#### Ejemplo: Listar Archivos en un Cubo
```php
use Qiniu\Storage\BucketManager;

$bucketMgr = new BucketManager($auth);
list($ret, $error) = $bucketMgr->listFiles($bucket);

if ($error !== null) {
    echo "Error: " . $error->message();
} else {
    echo "Archivos en el cubo:\n";
    foreach ($ret['items'] as $item) {
        echo $item['key'] . "\n";
    }
}
```

---

### 6. Manejo de Errores
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
- Versión de PHP: La versión del SDK `^7.0` soporta PHP 5.3.3 y versiones superiores (hasta PHP 8.x en versiones posteriores).
- Extensiones: Asegúrate de que las extensiones `cURL` y `xml` de PHP estén habilitadas, ya que son requeridas por el SDK.

Puedes verificar tu versión de PHP y las extensiones con:
```bash
php -v
php -m
```

---

### 8. ¿A Dónde Ir a Continuación?
- **Documentación**: Para más detalles, consulta la [documentación oficial del SDK de PHP de Qiniu](https://developer.qiniu.com/kodo/sdk/php) o el [repositorio de GitHub](https://github.com/qiniu/php-sdk).
- **Ejemplos**: Verifica el directorio `examples/` en el repositorio de GitHub para más casos de uso.
- **Soporte**: Si encuentras problemas, envía un ticket al soporte de Qiniu (<support@qiniu.com>) o pregunta en sus foros comunitarios.

---

### Código Completo del Ejemplo
Aquí tienes un script completo para subir un archivo:
```php
<?php
require_once 'vendor/autoload.php';

use Qiniu\Auth;
use Qiniu\Storage\UploadManager;

$accessKey = 'YOUR_ACCESS_KEY';
$secretKey = 'YOUR_SECRET_KEY';
$bucket = 'YOUR_BUCKET_NAME';
$filePath = '/ruta/a/tu/archivo.txt';
$key = 'archivo.txt';

$auth = new Auth($accessKey, $secretKey);
$token = $auth->uploadToken($bucket);
$uploadMgr = new UploadManager();

list($ret, $error) = $uploadMgr->putFile($token, $key, $filePath);

if ($error !== null) {
    echo "La subida falló: " . $error->message();
} else {
    echo "Subida exitosa! Hash del archivo: " . $ret['hash'];
}
```

Reemplaza los valores de marcador de posición (`YOUR_ACCESS_KEY`, `YOUR_SECRET_KEY`, `YOUR_BUCKET_NAME`, `/ruta/a/tu/archivo.txt`) con tus datos reales, ¡y listo!

Hazme saber si necesitas ayuda con una funcionalidad específica.