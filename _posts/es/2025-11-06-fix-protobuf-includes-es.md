---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Corregir archivos de inclusión de Protobuf faltantes
translated: true
type: note
---

### Comprender el Error

Este fallo en `greptime-proto` (anclado al commit `14b9dc40` del repositorio GreptimeTeam) ocurre durante la compilación de protobuf. Específicamente, `protoc` no puede localizar el tipo estándar bien conocido de Google `google/protobuf/duration.proto` (y probablemente otros como `timestamp.proto`). Esto se propaga en errores de importación en los propios protos de GreptimeDB (por ejemplo, `ddl.proto` importa Duration, causando errores de tipo indefinido en `database.proto`).

La causa principal: Tu instalación de `protoc` (desde la actualización manual) solo incluye el binario (`/usr/local/bin/protoc`), pero no los archivos de inclusión que contienen los protos principales de Google. `prost-build` en el `build.rs` de la crate ejecuta `protoc` sin establecer explícitamente `--proto_path` hacia las inclusiones de Google, por lo que falla en importaciones relativas como `"google/protobuf/duration.proto"`.

Esto es común con instalaciones de protobuf que son solo binarias; el SDK completo proporciona `/usr/include/google/protobuf/` (o equivalente).

### Solución Rápida: Instalar las Inclusiones de Protobuf

Dado que ya tienes un binario `protoc` reciente, añade las inclusiones que faltan sin necesidad de degradar:

1. **Descargar la Versión Completa de Protobuf** (que coincida con tu versión de protoc, por ejemplo, 27.3 o la más reciente):
   ```
   wget https://github.com/protocolbuffers/protobuf/releases/download/v27.3/protoc-27.3-linux-x86_64.zip
   unzip protoc-27.3-linux-x86_64.zip -d protoc-full
   ```

2. **Instalar los Archivos de Inclusión**:
   ```
   sudo mkdir -p /usr/local/include/google/protobuf
   sudo cp -r protoc-full/include/google /usr/local/include/
   sudo chmod -R a+r /usr/local/include/google/protobuf  # Asegurar legibilidad
   rm -rf protoc-full protoc-*.zip  # Limpieza
   ```

3. **Verificar**:
   - Comprobar protoc: `protoc --version` (debería ser ≥3.21).
   - Probar inclusiones: `ls /usr/local/include/google/protobuf/duration.proto` (debería existir).
   - Prueba rápida: `protoc --proto_path=/usr/local/include proto/greptime/v1/ddl.proto --decode_raw=stdin < /dev/null` (desde tu directorio del proyecto; ignora la salida, solo verifica que no haya "Archivo no encontrado").

4. **Reintentar la Compilación**:
   ```
   make clean  # Limpia compilaciones parciales
   make
   ```

Si estás en una distribución con `apt` (por ejemplo, Ubuntu), una alternativa es `sudo apt install libprotobuf-dev`—pero esto podría instalar una versión anterior (por ejemplo, 3.12), entrando en conflicto con tu protoc manual. Si es así, mantente con la copia manual de inclusiones y establece `PROTOC=/usr/local/bin/protoc` explícitamente.

### Consejos Adicionales
- Si los errores persisten (por ejemplo, otros protos faltantes como `wrappers.proto`), la copia completa de `include/google/` debería cubrirlos.
- Para compilaciones en contenedores (Docker), añade estos pasos a tu Dockerfile.
- Después de la compilación, prueba con `cargo run --bin greptime -- standalone start` para asegurarte de que los protos se integran correctamente.
- Esta revisión de greptime-proto es reciente (aproximadamente Oct 2024); si los problemas continúan, verifica si hay correcciones upstream en el repositorio.

[Documentación de Compilación de GreptimeDB](https://github.com/GreptimeTeam/greptimedb#build-from-source)  
[Tipos Bien Conocidos de Protobuf](https://protobuf.dev/reference/protobuf/google.protobuf/)