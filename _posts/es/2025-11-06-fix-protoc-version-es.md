---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Corrección del Error de Versión de Protoc en la Compilación de Substrait
translated: true
type: note
---

### Comprender el Error

Este fallo de compilación ocurre en la crate `substrait` (v0.58.0), de la cual GreptimeDB depende para la planificación de consultas multiplataforma. El error surge porque el compilador de protobuf (`protoc`) rechaza el archivo `substrait/algebra.proto` al usar campos "opcionales" en la sintaxis proto3—una característica que requiere:

- Versión de Protoc ≥3.21 (donde la compatibilidad es estable y no se necesita una bandera especial), o
- Un protoc más antiguo (ej. 3.15–3.20) con la bandera `--experimental_allow_proto3_optional` pasada durante la compilación.

La herramienta `prost-build` en el script de compilación de `substrait` no pasa esta bandera, por lo que asume una versión de protoc compatible. El `protobuf-compiler` de tu sistema (probablemente de `apt` en Ubuntu 22.04 o anterior, dando ~3.12.4) es demasiado antiguo y carece de la bandera, causando el pánico.

La documentación de GreptimeDB especifica protoc ≥3.15, pero para esta dependencia, se requiere efectivamente ≥3.21.

### Solución Rápida: Actualizar Protoc a ≥3.21

La forma más fácil, sin necesidad de permisos de root, es descargar e instalar la versión binaria oficial (no se necesita compilar). Así es cómo:

1. **Descarga la Última Versión de Protoc**:
   - Ve a [Protocol Buffers Releases](https://github.com/protocolbuffers/protobuf/releases).
   - Toma la última versión de `protoc-<version>-linux-x86_64.zip` (ej. `protoc-28.1-linux-x86_64.zip` o la que sea actual—cualquier versión ≥3.21 funciona).
   - Enlace directo de ejemplo (ajusta la versión):  
     `wget https://github.com/protocolbuffers/protobuf/releases/download/v27.3/protoc-27.3-linux-x86_64.zip`

2. **Instálalo**:
   ```
   unzip protoc-*.zip -d protoc-install
   sudo mv protoc-install/bin/protoc /usr/local/bin/
   sudo chmod +x /usr/local/bin/protoc
   rm -rf protoc-install protoc-*.zip  # Limpieza
   ```

3. **Verifica**:
   ```
   protoc --version
   ```
   Debería mostrar `libprotoc 27.3` (o superior). Si todavía es la versión antigua, verifica tu PATH (`echo $PATH`)—`/usr/local/bin` debería estar antes que `/usr/bin`.

4. **Reintenta la Compilación**:
   ```
   make clean  # Limpia objetivos obsoletos
   make
   ```

Esto sobrescribe el `protoc` del sistema sin conflictos con los paquetes de `apt`. Si estás en una distro más nueva como Ubuntu 24.04+, `apt install protobuf-compiler` podría dar ya ≥3.21—verifica tu versión primero.

### Si No Puedes Actualizar (Casos Raros)
- Si estás atascado en un sistema antiguo, necesitarías parchear el `build.rs` de `substrait` para agregar la bandera (vía `Command::new(protoc).arg("--experimental_allow_proto3_optional")`), pero esto requiere hacer un fork de la crate y actualizar el `Cargo.toml` de GreptimeDB—complicado y no recomendado.
- Alternativamente, algunas crates ofrecen una característica `protobuf-src` para incluir un protoc reciente, pero `substrait` no la habilita por defecto.

### Consejos Adicionales
- Asegura otros prerrequisitos: `build-essential` (para GCC), `libc6-dev` (cabeceras de glibc).
- Si la compilación pasa pero luego falla en dependencias de C++ (ej. Arrow), instala `libarrow-dev` vía conda o apt.
- Para CI/CD o Docker: Añade el paso de descarga a tu entorno.

Esto debería resolverlo—`substrait` se compila limpiamente en configuraciones modernas. Si encuentras otro problema, comparte `protoc --version` y tu distro.

[Documentación de Compilación de GreptimeDB](https://github.com/GreptimeTeam/greptimedb#build-from-source)  
[Lanzamientos de Protobuf](https://github.com/protocolbuffers/protobuf/releases)  
[Campos Opcionales en Proto3](https://protobuf.dev/programming-guides/proto3/#optional)