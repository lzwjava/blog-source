---
audio: false
generated: true
lang: es
layout: post
title: Fuente de Instalación de Paquetes npm
translated: true
---

Para cambiar la fuente de instalación del paquete `@ngx-formly/bootstrap` de un archivo `.tgz` local al registro npm, sigue estos pasos:

### 1. Desinstalar el Paquete Instalado Localmente
Dado que previamente instalaste `@ngx-formly/bootstrap` desde un archivo `.tgz` local, actualmente se encuentra en el directorio `node_modules` de tu proyecto. Para eliminarlo, ejecuta el siguiente comando en tu terminal:

```bash
npm uninstall @ngx-formly/bootstrap
```

Este comando elimina el paquete de `node_modules`. Si el paquete se agregó manualmente a tu archivo `package.json` bajo `dependencies` o `devDependencies`, también lo eliminará de allí. Si no estaba listado en `package.json` (común al instalar desde un archivo `.tgz` sin guardar), aún así se eliminará de tu proyecto.

### 2. Instalar el Paquete desde el Registro npm
Ahora, instala el paquete desde el registro npm ejecutando:

```bash
npm install @ngx-formly/bootstrap
```

Este comando obtiene la última versión de `@ngx-formly/bootstrap` desde el registro npm (generalmente `https://registry.npmjs.org/` a menos que hayas configurado un registro diferente) e instala en tu directorio `node_modules`. También agregará el paquete a tu archivo `package.json` bajo `dependencies` por defecto (en versiones recientes de npm), asegurando que se rastree como parte de tu proyecto.

### Opcional: Verificar el Registro (Si Es Necesario)
Si previamente cambiaste tu registro npm y deseas asegurarte de que esté configurado en el registro npm predeterminado, puedes verificarlo con:

```bash
npm config get registry
```

Si la salida es `https://registry.npmjs.org/`, estás utilizando el registro predeterminado y el comando `npm install` funcionará como se espera. Si está configurado en un registro diferente y deseas revertir al predeterminado, ejecuta:

```bash
npm config set registry https://registry.npmjs.org/
```

Sin embargo, dado que mencionaste que ya has configurado tu registro, este paso puede no ser necesario.

### Notas
- **Control de Versiones**: Si necesitas la misma versión que la que está en tu archivo `.tgz`, verifica el número de versión en `node_modules/@ngx-formly/bootstrap/package.json` antes de desinstalar. Luego, instala esa versión específica con:
  ```bash
  npm install @ngx-formly/bootstrap@<version>
  ```
  Si no especificas una versión, se instalará la última versión del registro.
- **Tipo de Dependencia**: Si deseas el paquete como una dependencia de desarrollo en lugar de una dependencia regular, usa:
  ```bash
  npm install @ngx-formly/bootstrap --save-dev
  ```

Siguiendo estos pasos, cambiarás con éxito `@ngx-formly/bootstrap` de ser instalado a través de un archivo `.tgz` local a ser instalado desde el registro npm.