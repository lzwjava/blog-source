---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Indicador del Proveedor Heredado de OpenSSL para Node.js
translated: true
type: note
---

### Comprender el problema
Node.js 16 (y versiones anteriores) utiliza OpenSSL 1.x, mientras que Node.js 22 introduce OpenSSL 3.x, que tiene configuraciones de seguridad más estrictas. Esto puede causar errores en algunas aplicaciones, especialmente aquellas que dependen de proveedores criptográficos heredados o algoritmos obsoletos (por ejemplo, hashes MD4). El flag `--openssl-legacy-provider` habilita temporalmente la compatibilidad con el comportamiento de OpenSSL 1.x para solucionar estos problemas durante la actualización.

**Nota**: Este flag es una solución temporal y podría eliminarse en futuras versiones de Node.js. Es mejor para soluciones a corto plazo; actualiza tu código para usar las APIs modernas de OpenSSL 3.x cuando sea posible.

### Cómo usar el flag
Puedes aplicar este flag al ejecutar Node.js directamente o a través de scripts de npm/yarn. Es una opción de runtime, no una configuración permanente.

#### Para comandos directos de Node
Añade el flag antes de tu script o comando. Ejemplos:
- Ejecución básica de script: `node --openssl-legacy-provider app.js`
- REPL (modo interactivo): `node --openssl-legacy-provider`
- Si ejecutas un módulo: `node --openssl-legacy-provider --input-type=module index.mjs`
- Con flags adicionales: `node --openssl-legacy-provider --max-old-space-size=4096 script.js`

Esto habilita el soporte del proveedor heredado, evitando errores comunes como "digital envelope routines unsupported" (relacionado con hashes o cifrados obsoletos).

#### Para scripts de npm/Yarn
Modifica tu `package.json` en la sección `"scripts"` para incluir el flag en los comandos relevantes. Ejemplo:
```json
{
  "scripts": {
    "start": "node --openssl-legacy-provider app.js",
    "dev": "node --openssl-legacy-provider --watch app.js"
  }
}
```
Luego ejecuta como de costumbre: `npm start` o `yarn dev`.

Si usas una herramienta como nodemon o vite que genera procesos de Node, antepone el flag en su configuración (por ejemplo, en nodemon.json: `"exec": "node --openssl-legacy-provider"`).

#### Para comandos globales (por ejemplo, mediante nvm o Node del sistema)
Si gestionas versiones de Node con nvm, cambia a Node 22 y ejecuta los comandos con el flag como se muestra. Para Docker o CI/CD, añádelo a tus scripts de ejecución (por ejemplo, `CMD ["node", "--openssl-legacy-provider", "app.js"]`).

### Resolución de problemas y alternativas
- **Verifica que el flag funciona**: Ejecuta `node --openssl-legacy-provider --version`—debería mostrar la versión de Node 22 sin errores.
- **Problemas comunes solucionados**: Errores con `require()` de módulos crypto, builds de webpack o inicios de aplicación. Si persiste, verifica si hay código específico de OpenSSL (por ejemplo, usa alternativas a `crypto.createCipher` como `crypto.createCipheriv`).
- **Soluciones a largo plazo**: Escanea el uso de crypto obsoleto (usa herramientas como plugins de ESLint) y actualiza a métodos compatibles con OpenSSL 3.x. La documentación de Node 22 recomienda bibliotecas como `bcrypt` o `crypto.scrypt` para hashing.
- **Nota sobre rendimiento/compatibilidad**: El modo de proveedor heredado puede afectar ligeramente la seguridad/funcionalidades, pero ayuda durante la migración. Prueba exhaustivamente, ya que algunas características de OpenSSL 3 (por ejemplo, fuentes de entropía mejoradas) no estarán disponibles.

Para más detalles, consulta la documentación de OpenSSL de Node.js en nodejs.org/api/crypto.html. ¡Si compartes mensajes de error específicos, puedo ofrecer consejos más dirigidos!