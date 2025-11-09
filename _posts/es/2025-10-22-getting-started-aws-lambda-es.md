---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Primeros Pasos con AWS Lambda
translated: true
type: note
---

### Introducción a AWS Lambda

AWS Lambda es un servicio de computación sin servidor que ejecuta tu código en respuesta a eventos sin que tengas que gestionar servidores. Aquí tienes una guía paso a paso para principiantes sobre cómo crear, implementar y usar tu primera función Lambda. Esta guía está basada en la documentación oficial de AWS.

#### Prerrequisitos
- Una cuenta activa de AWS. Regístrate en [aws.amazon.com](https://aws.amazon.com/) si no tienes una.
- Familiaridad básica con un lenguaje de programación como Node.js o Python (Lambda admite muchos entornos de ejecución).

#### Paso 1: Crear una función Lambda
1. Inicia sesión en la Consola de Administración de AWS y navega hasta el servicio Lambda (busca "Lambda" en el menú de servicios).
2. En la página de Funciones, haz clic en **Crear función**.
3. Elige **Crear desde cero**.
4. Introduce un **Nombre de función** (por ejemplo, `mi-primera-funcion`).
5. Selecciona un **Entorno de ejecución** (por ejemplo, Node.js 22.x o Python 3.13).
6. Deja la arquitectura por defecto (x86_64) y haz clic en **Crear función**.

Esto crea automáticamente un rol de ejecución (un rol de IAM) con permisos básicos, como escribir registros en Amazon CloudWatch.

#### Paso 2: Escribir tu código
En el editor de código de la consola de Lambda (en la pestaña **Código**), reemplaza el código predeterminado "Hola Mundo" con algo simple. Aquí tienes un ejemplo que calcula el área de un rectángulo basándose en un JSON de entrada con claves `length` y `width`.

- **Ejemplo en Node.js**:
  ```javascript
  exports.handler = async (event) => {
    const length = event.length;
    const width = event.width;
    const area = length * width;
    console.log(`The area is ${area}`);
    console.log('Log group: /aws/lambda/' + process.env.AWS_LAMBDA_FUNCTION_NAME);
    return { area: area };
  };
  ```

- **Ejemplo en Python**:
  ```python
  import json

  def lambda_handler(event, context):
    length = event['length']
    width = event['width']
    area = length * width
    print(f"The area is {area}")
    print(f"Log group: /aws/lambda/{context.function_name}")
    return {
        'statusCode': 200,
        'body': json.dumps({'area': area})
    }
  ```

Guarda los cambios: la implementación ocurre automáticamente para los lenguajes interpretados.

Para lenguajes compilados (por ejemplo, Java), crea un paquete de implementación localmente y súbelo a través de la consola o la AWS CLI.

#### Paso 3: Probar tu función
1. En la pestaña **Test**, haz clic en **Crear nuevo evento de prueba**.
2. Ponle un nombre (por ejemplo, `calcular-area-prueba`).
3. Pega una entrada JSON de ejemplo:
   ```json
   {
     "length": 6,
     "width": 7
   }
   ```
4. Guarda y haz clic en **Test**.

Verás los resultados en la sección **Resultados de la ejecución** (por ejemplo, `{"area": 42}`). Consulta los registros en CloudWatch para obtener detalles como la duración y el uso de memoria.

#### Paso 4: Invocar y supervisar
- **Invocación manual**: Usa el botón Test de la consola o la AWS CLI: `aws lambda invoke --function-name mi-primera-funcion output.json`.
- **Invocación basada en eventos**: Conecta desencadenadores como API Gateway, buckets S3 o streams de DynamoDB. Ve a la pestaña **Configuración** > **Desencadenadores** para añadirlos.
- **Registros**: Se envían automáticamente a CloudWatch Logs. Puedes verlos en [console.aws.amazon.com/cloudwatch/home#logsV2:log-groups](https://console.aws.amazon.com/cloudwatch/home#logsV2:log-groups) bajo `/aws/lambda/tu-nombre-de-funcion`.

Conceptos clave:
- **Fuentes de eventos/desencadenadores**: Servicios (por ejemplo, una subida a S3) que invocan tu función con datos del evento (carga útil JSON).
- **Manejador (Handler)**: El punto de entrada (por ejemplo, `index.handler` para Node.js) que procesa el evento.

#### Paso 5: Limpiar (Opcional)
Elimina la función a través de la consola: Acciones > Eliminar. También elimina los registros asociados y los roles de IAM para evitar cargos.

#### Consejos
- Empieza con el nivel gratuito (1 millón de solicitudes/mes).
- Usa AWS SAM o Serverless Framework para implementaciones avanzadas.
- Para producción, configura las variables de entorno, las capas (layers) y los ajustes de VPC en la pestaña **Configuración**.

[Crear tu primera función Lambda](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html)