---
audio: false
generated: true
lang: es
layout: post
title: Fuente de Instalación de Paquetes npm
translated: true
type: note
---

Para cambiar la fuente de instalación del paquete `@ngx-formly/bootstrap` de un archivo local `.tgz` al registro de npm, sigue estos pasos:

### 1. Desinstalar el Paquete Instalado Localmente
Dado que previamente instalaste `@ngx-formly/bootstrap` desde un archivo local `.tgz`, actualmente se encuentra en el directorio `node_modules` de tu proyecto. Para eliminarlo, ejecuta el siguiente comando en tu terminal:

```bash
npm uninstall @ngx-formly/bootstrap
```

Este comando elimina el paquete de `node_modules`. Si el paquete fue agregado manualmente a tu archivo `package.json` bajo `dependencies` o `devDependencies`, esto también lo eliminará de allí. Si no estaba listado en `package.json` (común cuando se instala desde un archivo `.tgz` sin guardar), igualmente será eliminado de tu proyecto.

### 2. Instalar el Paquete desde el Registro de npm
Ahora, instala el paquete desde el registro de npm ejecutando:

```bash
npm install @ngx-formly/bootstrap
```

Este comando obtiene la última versión de `@ngx-formly/bootstrap` del registro de npm (normalmente `https://registry.npmjs.org/` a menos que hayas configurado un registro diferente) y la instala en tu directorio `node_modules`. También agregará el paquete a tu archivo `package.json` bajo `dependencies` por defecto (en versiones recientes de npm), asegurando que sea rastreado como parte de tu proyecto.

### Opcional: Verificar el Registro (Si es Necesario)
Si previamente cambiaste tu registro de npm y quieres asegurarte de que esté configurado al registro de npm por defecto, puedes verificarlo con:

```bash
npm config get registry
```

Si el resultado es `https://registry.npmjs.org/`, estás usando el registro por defecto y el comando `npm install` funcionará como se espera. Si está configurado a un registro diferente y quieres revertirlo al por defecto, ejecuta:

```bash
npm config set registry https://registry.npmjs.org/
```

Sin embargo, dado que mencionaste que ya has configurado tu registro, este paso puede no ser necesario.

### Notas
- **Control de Versiones**: Si necesitas la misma versión que la de tu archivo `.tgz`, verifica el número de versión en `node_modules/@ngx-formly/bootstrap/package.json` antes de desinstalar. Luego, instala esa versión específica con:
  ```bash
  npm install @ngx-formly/bootstrap@<versión>
  ```
  Si no especificas una versión, se instalará la última versión del registro.
- **Tipo de Dependencia**: Si quieres el paquete como una dependencia de desarrollo en lugar de una dependencia regular, usa:
  ```bash
  npm install @ngx-formly/bootstrap --save-dev
  ```

Siguiendo estos pasos, cambiarás exitosamente `@ngx-formly/bootstrap` de estar instalado mediante un archivo local `.tgz` a estar instalado desde el registro de npm.