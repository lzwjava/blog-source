---
audio: false
generated: true
lang: es
layout: post
title: Problema de Proxy de Stable Diffusion
translated: true
type: note
---

Según el error y tu entorno, aquí tienes cómo solucionar el problema "Unknown scheme for proxy URL":

### Solución:
El error ocurre porque **`httpx` no admite proxies `socks://` por defecto**. Tienes dos opciones:

#### Opción 1: Eliminar la Referencia al Proxy SOCKS
1. Revisa tus variables de entorno en busca de configuraciones de proxy sobrantes:
   ```bash
   env | grep -i proxy
   ```
   Busca referencias a `socks://` (especialmente `ALL_PROXY` o `http_proxy`).

2. Anula la variable problemática (reemplaza `VAR_NAME` con el nombre real encontrado arriba):
   ```bash
   unset VAR_NAME  # ej., unset ALL_PROXY
   ```

#### Opción 2: Agregar Soporte SOCKS a `httpx`
1. Activa tu entorno virtual de Python:
   ```bash
   source /home/lzw/Projects/stable-diffusion-webui/venv/bin/activate
   ```

2. Instala las dependencias requeridas:
   ```bash
   pip install -U "httpx[socks]"
   ```

3. Desactiva el entorno:
   ```bash
   deactivate
   ```

### Por qué sucede esto:
- Tus proxies principales (`HTTP_PROXY/HTTPS_PROXY`) usan `http://` (compatible), pero algo (probablemente otra aplicación/script) está estableciendo un proxy `socks://` que `httpx` no puede manejar sin paquetes adicionales.
- El stack trace muestra que Gradio/`httpx` está intentando usar `socks://127.0.0.1:7891`, que no aparece en tu salida de `checkproxy`.

### Verificación:
Después de aplicar la solución, ejecuta:
```bash
./webui.sh
```
El error del proxy SOCKS debería desaparecer.

> 💡 **Nota**: Si no configuraste intencionalmente un proxy SOCKS, investiga qué aplicaciones podrían configurar proxies automáticamente (ej., VPNs, gestores de red o archivos de configuración del shell como `~/.bashrc`).

---

El error `Torch is not able to use GPU; add --skip-torch-cuda-test to COMMANDLINE_ARGS variable to disable this check` indica que PyTorch, utilizado por Stable Diffusion WebUI, no puede detectar o acceder a una GPU compatible. Esto probablemente se deba a bibliotecas CUDA faltantes, una GPU incompatible, problemas con los controladores o un problema de configuración. A continuación se presentan los pasos para solucionar este problema, adaptados a tu entorno (glibc 2.35, Python 3.10.12, GCC 11.4.0, probablemente basado en Ubuntu 22.04 según la versión de glibc).

### Pasos para Solucionar el Problema

#### 1. **Verificar la Compatibilidad de la GPU y CUDA**
   - **Comprobar si tienes una GPU NVIDIA**:
     Ejecuta:
     ```bash
     lspci | grep -i nvidia
     ```
     Esto lista el hardware NVIDIA. Si no aparece nada, es posible que tu sistema no tenga una GPU NVIDIA, y PyTorch requiere una GPU NVIDIA para el soporte CUDA.
   - **Comprobar la instalación del controlador NVIDIA**:
     Ejecuta:
     ```bash
     nvidia-smi
     ```
     Si está instalado, muestra una tabla con detalles de la GPU (ej., versión del controlador, versión de CUDA). Si no, instala el controlador NVIDIA:
     ```bash
     sudo apt-get update
     sudo apt-get install nvidia-driver-<version> nvidia-utils-<version> -y
     ```
     Reemplaza `<version>` con el controlador estable más reciente (ej., `535` o `550`). Encuentra la versión del controlador apropiada con:
     ```bash
     ubuntu-drivers devices
     sudo ubuntu-drivers autoinstall
     ```
   - **Comprobar la versión de CUDA**:
     PyTorch requiere bibliotecas CUDA. Comprueba la versión de CUDA instalada:
     ```bash
     nvcc --version
     ```
     Si no está instalado, instala CUDA Toolkit:
     ```bash
     sudo apt-get install nvidia-cuda-toolkit -y
     ```
     Alternativamente, descarga el último CUDA Toolkit del sitio web de NVIDIA (ej., CUDA 11.8 o 12.1) y sigue su guía de instalación.

#### 2. **Verificar la Instalación de PyTorch**
   El error sugiere que PyTorch está instalado pero no puede usar la GPU. Asegúrate de tener la versión correcta de PyTorch con soporte CUDA.
   - **Comprobar la instalación de PyTorch**:
     Ejecuta:
     ```bash
     python3 -c "import torch; print(torch.__version__); print(torch.cuda.is_available())"
     ```
     La salida esperada debe incluir una versión de PyTorch (ej., `2.0.1`) y `True` para `torch.cuda.is_available()`. Si es `False`, PyTorch no está detectando la GPU.
   - **Reinstalar PyTorch con soporte CUDA**:
     Para Python 3.10 y CUDA (ej., 11.8), instala PyTorch en tu entorno de Stable Diffusion:
     ```bash
     cd /home/lzw/Projects/stable-diffusion-webui
     source venv/bin/activate
     pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
     ```
     Reemplaza `cu118` con tu versión de CUDA (ej., `cu121` para CUDA 12.1). Consulta las versiones compatibles en el sitio oficial de PyTorch.
   - **Verificar después de la reinstalación**:
     Ejecuta la comprobación nuevamente:
     ```bash
     python3 -c "import torch; print(torch.cuda.is_available()); print(torch.cuda.get_device_name(0))"
     ```

#### 3. **Omitir la Comprobación CUDA (Solución Temporal)**
   Si deseas ejecutar Stable Diffusion sin soporte de GPU (ej., para pruebas en CPU), omite la comprobación CUDA agregando `--skip-torch-cuda-test` a los argumentos de la línea de comandos.
   - Edita `webui-user.sh` (o créalo si no existe):
     ```bash
     nano /home/lzw/Projects/stable-diffusion-webui/webui-user.sh
     ```
     Agrega o modifica la línea `COMMANDLINE_ARGS`:
     ```bash
     export COMMANDLINE_ARGS="--skip-torch-cuda-test"
     ```
     Guarda y sale.
   - Ejecuta el script:
     ```bash
     ./webui.sh
     ```
     Esto permite que Stable Diffusion se ejecute en CPU, pero el rendimiento será significativamente más lento.

#### 4. **Asegurar que TCMalloc esté Configurado Correctamente**
   Tu salida muestra que TCMalloc (`libtcmalloc_minimal.so.4`) está detectado y enlazado con `LD_PRELOAD`. Confirma que funciona:
   ```bash
   echo $LD_PRELOAD
   ```
   Si muestra `/lib/x86_64-linux-gnu/libtcmalloc_minimal.so.4`, está listo. Si no, configúralo manualmente:
   ```bash
   export LD_PRELOAD=/lib/x86_64-linux-gnu/libtcmalloc_minimal.so.4
   ```
   O agrégalo a `webui-user.sh`:
   ```bash
   export LD_PRELOAD=/lib/x86_64-linux-gnu/libtcmalloc_minimal.so.4
   ```

#### 5. **Comprobar Variables de Entorno y Rutas**
   Asegúrate de que tu entorno esté configurado correctamente:
   - **Comprobar LD_LIBRARY_PATH**:
     Las bibliotecas CUDA deben ser accesibles. Agrégalas si es necesario:
     ```bash
     export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
     ```
     Agrega esto a `~/.bashrc` o `webui-user.sh` para que sea persistente.
   - **Activar el entorno virtual**:
     Siempre activa el entorno virtual de Stable Diffusion antes de ejecutar:
     ```bash
     cd /home/lzw/Projects/stable-diffusion-webui
     source venv/bin/activate
     ```

#### 6. **Actualizar Stable Diffusion WebUI**
   Tu versión (`v1.10.1`, commit `82a973c`) podría tener problemas de compatibilidad. Actualiza a la última versión:
   ```bash
   cd /home/lzw/Projects/stable-diffusion-webui
   git pull
   ```
   Luego, reinstala las dependencias:
   ```bash
   ./webui.sh
   ```

#### 7. **Resolución de Problemas**
   - **Si `nvidia-smi` falla**: Reinstala el controlador NVIDIA o comprueba si hay problemas de hardware con la GPU.
   - **Si PyTorch aún no detecta la GPU**:
     - Asegúrate de que CUDA y cuDNN estén instalados correctamente. Instala cuDNN si falta:
       ```bash
       sudo apt-get install libcudnn8
       ```
     - Verifica la compatibilidad de la versión de CUDA con tu GPU y PyTorch. Por ejemplo, las GPU antiguas (ej., serie Kepler) pueden no ser compatibles con CUDA 12.
   - **Si los errores persisten**: Revisa los logs de Stable Diffusion para obtener errores detallados:
     ```bash
     cat /home/lzw/Projects/stable-diffusion-webui/log/webui.log
     ```
     Comparte cualquier error específico para obtener más ayuda.
   - **Limitaciones de hardware**: Si tu GPU es demasiado antigua (ej., GPU NVIDIA anteriores a 2016), puede que no sea compatible con versiones modernas de CUDA. En este caso, usa `--skip-torch-cuda-test` o actualiza tu GPU.

#### 8. **Ejecutar la Aplicación**
   Después de aplicar las soluciones, ejecuta la WebUI:
   ```bash
   cd /home/lzw/Projects/stable-diffusion-webui
   ./webui.sh
   ```
   Si solucionaste el problema de la GPU, el error debería desaparecer. Si usas `--skip-torch-cuda-test`, se ejecutará en CPU.

### Notas
- **Información del Sistema**: Tu configuración (glibc 2.35, Python 3.10.12, GCC 11.4.0) sugiere Ubuntu 22.04, que es compatible con CUDA 11.8 o 12.1 y versiones recientes de PyTorch.
- **Rendimiento**: Ejecutar en CPU (con `--skip-torch-cuda-test`) es un recurso, pero será lento. Se recomienda solucionar el soporte de la GPU para Stable Diffusion.
- **TCMalloc**: El problema de TCMalloc parece resuelto según tu salida. Asegúrate de que `LD_PRELOAD` permanezca configurado si encuentras problemas relacionados con la memoria.

Si aún enfrentas problemas o necesitas ayuda con mensajes de error específicos, ¡proporciona detalles adicionales (ej., modelo de GPU, versión de CUDA o logs completos) y puedo refinar la solución!