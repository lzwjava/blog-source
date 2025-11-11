---
audio: false
generated: true
lang: es
layout: post
title: Uso de CUDA en Windows
translated: true
type: note
---

Para usar NVIDIA CUDA en tu HP ZBook Studio 16 G11, deberás seguir estos pasos. CUDA permite a los desarrolladores acelerar aplicaciones aprovechando el poder de la GPU para el procesamiento paralelo. Así es como puedes comenzar:

### Paso 1: Verificar la Compatibilidad del Hardware
- Asegúrate de que tu HP ZBook Studio 16 G11 esté equipado con una GPU NVIDIA compatible. El ZBook Studio 16 G11 puede venir con GPU como la NVIDIA RTX 3000 Ada Generation o superior, que admiten CUDA.

### Paso 2: Instalar los Controladores NVIDIA
- **Descargar Controladores:** Visita la [página de descarga de controladores de NVIDIA](https://www.nvidia.com/Download/index.aspx) y descarga los controladores más recientes para tu modelo específico de GPU.
- **Instalar Controladores:** Ejecuta el instalador y sigue las instrucciones en pantalla para instalar los controladores en tu sistema.

### Paso 3: Instalar el CUDA Toolkit
- **Descargar CUDA Toolkit:** Ve al [sitio web de NVIDIA CUDA Toolkit](https://developer.nvidia.com/cuda-downloads) y descarga la versión del CUDA Toolkit que coincida con tu sistema operativo.
- **Instalar CUDA Toolkit:** Ejecuta el instalador del CUDA Toolkit y sigue las instrucciones. Asegúrate de seleccionar las opciones apropiadas para tu entorno de desarrollo.

### Paso 4: Configurar las Variables de Entorno
- Durante el proceso de instalación, el instalador debería configurar automáticamente las variables de entorno necesarias. Sin embargo, es posible que necesites agregar manualmente los binarios de CUDA al PATH de tu sistema si no se hace automáticamente.
- En Windows, puedes hacerlo yendo a `Panel de control > Sistema y seguridad > Sistema > Configuración avanzada del sistema > Variables de entorno` y agregando la ruta al directorio bin de CUDA (por ejemplo, `C:\Archivos de programa\NVIDIA GPU Computing Toolkit\CUDA\vX.X\bin`).

### Paso 5: Verificar la Instalación
- Abre un símbolo del sistema o terminal y escribe `nvidia-smi`. Este comando debería mostrar información sobre tu GPU, lo que confirma que los controladores están instalados correctamente.
- Escribe `nvcc --version` para verificar la versión del compilador de CUDA. Esto confirma que el CUDA Toolkit está instalado correctamente.

### Paso 6: Desarrollar y Ejecutar Aplicaciones CUDA
- **Escribir Código CUDA:** Puedes escribir programas CUDA usando C, C++, Python o Fortran. NVIDIA proporciona documentación extensa y códigos de ejemplo para ayudarte a comenzar.
- **Compilar Código CUDA:** Usa el compilador `nvcc` para compilar tus programas CUDA. Por ejemplo, si tienes un programa CUDA llamado `my_program.cu`, puedes compilarlo con el comando `nvcc my_program.cu -o my_program`.
- **Ejecutar Código CUDA:** Ejecuta tu programa compilado desde la línea de comandos. Por ejemplo, `./my_program` en Linux o `my_program.exe` en Windows.

### Paso 7: Usar las Librerías CUDA
- NVIDIA proporciona varias librerías optimizadas para CUDA, como cuBLAS para álgebra lineal, cuFFT para transformadas de Fourier y cuDNN para redes neuronales profundas. Puedes incluir estas librerías en tus proyectos para aprovechar funciones preconstruidas y optimizadas.

### Recursos Adicionales
- **NVIDIA Developer Zone:** Visita la [NVIDIA Developer Zone](https://developer.nvidia.com/) para obtener tutoriales, documentación y soporte comunitario.
- **Documentación de CUDA:** Consulta la [Documentación de CUDA](https://docs.nvidia.com/cuda/) para obtener información detallada sobre programación CUDA y mejores prácticas.

Siguiendo estos pasos, puedes configurar y comenzar a usar NVIDIA CUDA en tu HP ZBook Studio 16 G11 para acelerar tus aplicaciones y aprovechar la computación con GPU.