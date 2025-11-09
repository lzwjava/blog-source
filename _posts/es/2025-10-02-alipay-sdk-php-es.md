---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Guía de integración de Alipay SDK para PHP
translated: true
type: note
---

### Requisitos Previos
Para integrar el SDK de Alipay en PHP, necesitarás:
- Una cuenta de comerciante de Alipay válida (regístrate en https://open.alipay.com).
- Pares de claves RSA: Genera una clave privada para tu servidor y carga la clave pública en Alipay para firmar transacciones.
- PHP 5.6+ (preferiblemente 7.x para mayor seguridad), con extensiones como cURL y OpenSSL habilitadas.
- Descarga el SDK de Alipay desde su GitHub oficial (por ejemplo, https://github.com/alipay/alipay-sdk-php) – ten en cuenta que el fragmento de código proporcionado parece ser para una versión anterior (~2016); el SDK más reciente utiliza API más nuevas como las Alipay Trade APIs. Si estás utilizando el legacy mobile security pay, puede que aún funcione pero está obsoleto.

### Configuración del SDK
1. **Descargar e Incluir**: Descarga el ZIP del SDK desde el portal para desarrolladores de Alipay o GitHub. Extráelo en el directorio de tu proyecto (por ejemplo, `vendor/alipay-sdk`).
2. **Incluir Archivos**: En tu script PHP, incluye el archivo principal del SDK, por ejemplo:
   ```php
   require_once 'ruta/al/alipay-sdk/AopClient.php'; // Para el SDK moderno
   ```
   Para la versión legacy en tu fragmento, podrías necesitar inclusiones personalizadas como `AopSdk.php`.

3. **Configurar Claves y Cuenta**:
   - Genera claves RSA (2048-bit) usando comandos OpenSSL o herramientas en línea. Ejemplo:
     ```bash
     openssl genrsa -out private_key.pem 2048
     openssl rsa -in private_key.pem -pubout -out public_key.pem
     ```
   - Rellena el array `$config` como se muestra en tu fragmento:
     - `partner`: Tu ID de partner de Alipay (16 dígitos que comienzan con 2088).
     - `private_key`: Tu clave privada codificada en PEM (en crudo, sin cabeceras como -----BEGIN PRIVATE KEY-----).
     - `alipay_public_key`: La clave pública de Alipay (cópiala desde tu consola de Alipay).
     - Otros campos: Usa HTTPS para `transport`, y coloca `cacert.pem` (descárgalo desde la documentación de Alipay) en el directorio del script para la verificación SSL.

### Inicializando el SDK
Crea una instancia de AopClient y pasa la configuración:
```php
use Orvibo\AopSdk\AopClient; // Ajusta el namespace para tu versión del SDK

$aopClient = new AopClient();
$aopClient->gatewayUrl = 'https://openapi.alipay.com/gateway.do'; // URL de producción
$aopClient->appId = 'tu_app_id'; // El SDK más nuevo usa appId en lugar de partner
$aopClient->rsaPrivateKey = $config['private_key'];
$aopClient->alipayrsaPublicKey = $config['alipay_public_key'];
$aopClient->apiVersion = '1.0';
$aopClient->signType = 'RSA2'; // El SDK moderno prefiere RSA2
$aopClient->postCharset = $config['input_charset'];
$aopClient->format = 'json';
```

Para el legacy mobile pay como en tu fragmento, usarías clases más antiguas como `AlipaySign`.

### Haciendo una Solicitud de Pago
1. **Construir Parámetros de la Solicitud**:
   ```php
   $request = new AlipayTradeAppPayRequest(); // O similar para tu versión del SDK
   $request->setBizContent("{" .
       "\"body\":\"Transacción de prueba\"," .
       "\"subject\":\"Asunto de prueba\"," .
       "\"out_trade_no\":\"123456789\"," .
       "\"timeout_express\":\"30m\"," .
       "\"total_amount\":\"0.01\"," .
       "\"product_code\":\"QUICK_MSECURITY_PAY\"" .
       "}");
   $request->setNotifyUrl($config['service']); // Tu URL de notificación
   ```

2. **Ejecutar la Solicitud**:
   ```php
   $response = $aopClient->sdkExecute($request);
   echo $response; // Esta cadena firmada se usa en el SDK de Alipay de tu app
   ```

3. **En Tu Aplicación Móvil (si se integra con una app)**: Pasa la respuesta al SDK nativo de Alipay de tu app (por ejemplo, Android/iOS) para completar el pago.

### Manejo de Notificaciones y Respuestas
- **Notificaciones Asíncronas**: Configura un script PHP de callback en la `notify_url` para verificar las notificaciones de Alipay.
  ```php
  $aopClient->rsaCheckV1($_POST, $alipayPublicKey, 'RSA2'); // Verificar firma
  // Procesa el estado del pago (por ejemplo, actualiza la base de datos)
  ```
- **Retorno Síncrono**: Después del pago, Alipay redirige a tu `return_url` (si está configurada).

### Pruebas y Despliegue
- Usa el entorno sandbox de Alipay para pruebas: https://openhome.alipay.com/platform/devEnv.htm.
- Problemas comunes: Asegúrate de que las claves estén formateadas correctamente (sin líneas extra). Usa RSA2 para mayor seguridad.
- Consejos de Seguridad: Almacena las claves de forma segura (no en el control de versiones). Verifica siempre las firmas para prevenir manipulaciones.

Si esto es para el SDK antiguo, considera actualizarte al último SDK de PHP de Alipay (por ejemplo, vía Composer: `composer require alipay/openapisdk`) para obtener mejores características y seguridad. Para documentación detallada, visita https://docs.open.alipay.com/. Si encuentras errores, comparte tu código y registros para solucionar problemas.