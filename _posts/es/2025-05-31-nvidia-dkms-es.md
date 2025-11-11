---
audio: false
generated: true
lang: es
layout: post
title: Problema de compilación de NVIDIA DKMS
translated: true
type: note
---

Parece que estás encontrando un error donde el módulo NVIDIA DKMS (Dynamic Kernel Module Support) no se puede compilar para tu nuevo kernel, `6.8.0-60-generic`. Este es un problema común al actualizar kernels, ya que el módulo del controlador necesita recompilarse para la nueva versión del kernel, y a veces surgen incompatibilidades o problemas de compilación.

Los mensajes de error clave son:
* `Building module(s)......(bad exit status: 2)`
* `Error! Bad return status for module build on kernel: 6.8.0-60-generic (x86_64)`
* `Consult /var/lib/dkms/nvidia/535.183.06/build/make.log for more information.`
* `dpkg: error processing package linux-image-6.8.0-60-generic (--configure):`
* `E: Sub-process /usr/bin/dpkg returned an error code (1)`

Esto significa que la versión del controlador NVIDIA `535.183.06` no se pudo compilar correctamente para el kernel `6.8.0-60-generic`, lo que a su vez ha impedido que la imagen del kernel y los paquetes relacionados se configuren correctamente.

Aquí te mostramos cómo puedes intentar solucionarlo:

---

### 1. Examina el Registro de Compilación 🪵

El paso más crucial es revisar el registro de compilación detallado para encontrar mensajes de error específicos. Este registro te dirá *por qué* falló la compilación.
Abre una terminal y ejecuta:
```bash
cat /var/lib/dkms/nvidia/535.183.06/build/make.log
```
Busca líneas que comiencen con `error:` o `fatal error:`. Estas a menudo señalan archivos faltantes, problemas del compilador o incompatibilidades con el código fuente del kernel. El error `Applying patch disable_fstack-clash-protection_fcf-protection.patch... done.` seguido de un fallo de compilación sugiere que el parche podría no ser totalmente compatible, o que hay otros problemas que el parche no soluciona.

---

### 2. Limpia e Intenta Reparar los Paquetes Dañados 🛠️

Primero, puedes intentar dejar que `apt` repare las dependencias rotas y termine de configurar los paquetes.
```bash
sudo rm /var/crash/nvidia-dkms-535.0.crash # Elimina el informe de fallo anterior para permitir nuevos
sudo apt --fix-broken install
sudo dpkg --configure -a
```
Esto podría reactivar la compilación de DKMS. Si falla nuevamente, procede con los siguientes pasos.

---

### 3. Asegúrate de que los Headers del Kernel Estén Correctamente Instalados 🧠

El proceso de compilación de DKMS requiere los headers del kernel correctos para la versión del kernel contra la que intentas compilar.
```bash
sudo apt update
sudo apt install --reinstall linux-headers-6.8.0-60-generic linux-headers-generic-hwe-22.04
```
Si aún no estás ejecutando el kernel `6.8.0-60-generic` (por ejemplo, si la actualización se interrumpió), también puedes especificar los headers para tu kernel actualmente en ejecución, pero el objetivo principal aquí es `6.8.0-60-generic`.

---

### 4. Elimina el Módulo DKMS Problemático y Reconfigura ♻️

Puedes eliminar manualmente la versión problemática del módulo NVIDIA de DKMS y luego intentar dejar que el sistema lo reconstruya.
```bash
sudo dkms remove nvidia/535.183.06 --all
```
Luego, intenta reconfigurar los paquetes nuevamente:
```bash
sudo dpkg --configure -a
sudo apt update && sudo apt upgrade
```
Este proceso debería hacer que DKMS intente reconstruir el módulo para el kernel `6.8.0-60-generic`.

---

### 5. Reinstala el Controlador NVIDIA 💻

Si el módulo sigue sin compilarse, la versión del controlador `535.183.06` podría tener problemas de compatibilidad con el kernel `6.8.0-60-generic`.

* **Purgar el controlador problemático actual:**
    ```bash
    sudo apt-get purge nvidia-dkms-535 nvidia-driver-535
    sudo apt autoremove
    sudo apt clean
    ```

* **Instalar un controlador adecuado:**
    Puedes dejar que Ubuntu intente instalar el controlador recomendado:
    ```bash
    sudo ubuntu-drivers autoinstall
    ```
    Alternativamente, puedes intentar instalar la misma versión (si los repositorios la consideran compatible ahora) o una versión potencialmente más nueva y más compatible. Por ejemplo, para intentar instalar nuevamente el controlador de la serie 535:
    ```bash
    sudo apt update
    sudo apt install nvidia-driver-535
    ```
    (El gestor de paquetes debería elegir la versión DKMS apropiada).

    Después de esto, el sistema intentará compilar el módulo DKMS nuevamente.

---

### 6. Considera una Versión Más Nueva del Controlador NVIDIA 🚀

El kernel 6.8 es relativamente nuevo. Es posible que el controlador NVIDIA de la serie 535 tenga limitaciones con esta versión del kernel. Es posible que necesites una serie de controlador más nueva (por ejemplo, 545, 550 o más nueva, si está disponible en tus repositorios o a través de los canales oficiales/PPAs de NVIDIA).

* Consulta los controladores disponibles:
    ```bash
    sudo apt search nvidia-driver
    ```
* Si hay un controlador propietario más nuevo disponible (por ejemplo, `nvidia-driver-550`), podrías intentar instalarlo en lugar de `nvidia-driver-535`.
    ```bash
    sudo apt install nvidia-driver-VERSION_NUMBER # Reemplaza VERSION_NUMBER
    ```

---

### 7. Si Estás Atrapado en un Bucle de Arranque o No Tienes Interfaz Gráfica 📉

Si el sistema no puede arrancar en un entorno gráfico:
* Arranca en modo de recuperación o con un kernel anterior (generalmente accesible desde el menú GRUB durante el inicio).
* Una vez en un entorno de línea de comandos, puedes intentar los pasos anteriores.
* Si necesitas usar temporalmente un controlador de código abierto para recuperar la interfaz gráfica mientras solucionas el controlador NVIDIA:
    ```bash
    sudo apt-get purge nvidia*
    sudo apt autoremove
    sudo apt install xserver-xorg-video-nouveau
    sudo reboot
    ```
    Luego, intenta la instalación del controlador NVIDIA nuevamente.

---

**Conclusión clave:** El contenido de `/var/lib/dkms/nvidia/535.183.06/build/make.log` es muy importante. Si los pasos anteriores no funcionan, los errores en ese archivo proporcionarán pistas más específicas, y es posible que necesites buscar en línea esos errores específicos en conjunto con tu versión de kernel y la versión del controlador NVIDIA.

---

Esta salida indica una serie de problemas de dependencia y configuración en tu sistema Ubuntu, probablemente relacionados con actualizaciones del kernel y el controlador NVIDIA. Desglosemos los problemas y sugamos soluciones potenciales.

**Problemas Principales:**

1.  **Problemas de Dependencia con `linux-generic-hwe-22.04`:**
    * Depende de `linux-headers-generic-hwe-22.04` con una versión específica (`= 6.8.0-60.63~22.04.1`).
    * `linux-headers-generic-hwe-22.04` no está configurado aún, lo que provoca que la configuración de `linux-generic-hwe-22.04` falle.

2.  **Fallo al Configurar `linux-image-6.8.0-60-generic`:**
    * El script posterior a la instalación para esta imagen del kernel falló con un estado de salida 1.
    * El registro de errores sugiere que esto está relacionado con el controlador NVIDIA (`nvidia/535.183.06`) que no se pudo compilar para esta versión específica del kernel (`6.8.0-60-generic`).
    * El proceso de compilación de DKMS (Dynamic Kernel Module Support) para el controlador NVIDIA falló. El archivo de registro `/var/lib/dkms/nvidia/535.183.06/build/make.log` contendrá más detalles sobre el error de compilación.
    * También hay un error relacionado con la creación de un informe de fallos para el fallo de NVIDIA DKMS, lo que indica un problema potencial con el mecanismo de informes de fallos del sistema o los permisos del sistema de archivos.

3.  **Fallo al Configurar `linux-headers-6.8.0-60-generic` y `linux-headers-generic-hwe-22.04`:**
    * Probablemente fallaron porque la configuración del paquete `linux-image-6.8.0-60-generic` falló, del cual podrían depender.

**Causas Potenciales:**

* **Actualización del kernel incompleta o interrumpida:** Es posible que el sistema se haya interrumpido durante una actualización del kernel, dejando algunos paquetes en un estado inconsistente.
* **Incompatibilidad del controlador NVIDIA:** La versión del controlador NVIDIA instalada (`535.183.06`) podría tener problemas para compilarse contra la nueva versión del kernel (`6.8.0-60-generic`).
* **Problemas de DKMS:** Podría haber problemas con el framework DKMS en sí, impidiendo que el controlador NVIDIA se compile.
* **Problemas del sistema de archivos:** El error sobre no poder crear un informe de fallos podría indicar un problema con el espacio en disco o los permisos de archivos en el directorio `/var/crash/`.

**Pasos para Solucionar el Problema:**

1.  **Intenta reconfigurar los paquetes:**
    Abre tu terminal y ejecuta el siguiente comando:
    ```bash
    sudo dpkg --configure -a
    ```
    Este comando intenta configurar todos los paquetes que están en un estado semi-configurado.

2.  **Revisa el registro de compilación de NVIDIA DKMS:**
    Examina el archivo de registro para obtener mensajes de error detallados durante la compilación del controlador NVIDIA:
    ```bash
    less /var/lib/dkms/nvidia/535.183.06/build/make.log
    ```
    Este registro podría proporcionar pistas sobre dependencias faltantes o errores de compilación.

3.  **Intenta reinstalar el controlador NVIDIA:**
    Puedes intentar eliminar y luego reinstalar el controlador NVIDIA. Primero, intenta purgarlo:
    ```bash
    sudo apt remove --purge nvidia-*
    sudo apt autoremove
    ```
    Luego, intenta reinstalarlo. Es posible que desees probar una versión diferente si la actual es problemática:
    ```bash
    sudo apt install nvidia-driver-535  # O una versión recomendada diferente
    ```
    Después de la instalación, reinicia tu sistema.

4.  **Limpia la caché de paquetes e intenta de nuevo:**
    ```bash
    sudo apt clean
    sudo apt update
    sudo apt upgrade
    sudo dpkg --configure -a
    ```

5.  **Reinstala el kernel problemático y los headers:**
    Puedes intentar reinstalar los paquetes específicos del kernel y los headers que están causando problemas:
    ```bash
    sudo apt install --reinstall linux-image-6.8.0-60-generic linux-headers-6.8.0-60-generic linux-headers-generic-hwe-22.04 linux-generic-hwe-22.04
    ```
    Después de esto, intenta configurar nuevamente:
    ```bash
    sudo dpkg --configure -a
    ```

6.  **Verifica el espacio en disco:**
    Asegúrate de tener suficiente espacio libre en tu partición raíz (`/`) ya que esto a veces puede causar problemas durante la instalación y configuración de paquetes.
    ```bash
    df -h /
    ```

7.  **Soluciona el error del informe de fallos (si es persistente):**
    Si el error sobre `/var/crash/nvidia-dkms-535.0.crash` persiste, puedes intentar eliminar el archivo (si existe y no lo necesitas para depuración) o verificar los permisos del directorio `/var/crash/`.
    ```bash
    sudo rm -f /var/crash/nvidia-dkms-535.0.crash
    sudo chmod 777 /var/crash  # Ten cuidado con los permisos amplios, revierte si no es necesario
    ```

8.  **Arranca con un kernel anterior:**
    Si tienes una versión anterior del kernel instalada, puedes intentar arrancar con ella desde el menú GRUB. Esto puede permitirte realizar pasos de solución de problemas desde un entorno estable. Si el sistema funciona con un kernel más antiguo, es probable que el problema sea específico del kernel `6.8.0-60-generic` o su interacción con el controlador NVIDIA.

**Consideraciones Importantes:**

* **Copia de seguridad:** Antes de realizar cambios significativos, especialmente aquellos que impliquen la eliminación de paquetes, siempre es una buena idea tener una copia de seguridad de tus datos importantes.
* **Sé paciente:** La configuración e instalación de paquetes puede llevar algo de tiempo.
* **Consulta los registros:** Los mensajes de error y los archivos de registro (especialmente el registro de compilación de NVIDIA DKMS) son cruciales para diagnosticar la causa exacta del problema.

Comienza con los primeros pasos y observa si resuelven el problema. Si no, procede con las soluciones más complejas y examina cuidadosamente cualquier mensaje de error que encuentres. ¡Buena suerte!

---

Esta salida del registro de compilación de NVIDIA DKMS indica que la compilación está fallando debido a una **opción de línea de comandos no reconocida: `-ftrivial-auto-var-init=zero`**.

Esta opción del compilador es una adición relativamente reciente a GCC (probablemente versión 12 o posterior) y Clang. Parece que el compilador que se está utilizando para compilar el controlador NVIDIA para tu kernel (6.8.0-60-generic) no reconoce esta opción.

**Causas y Soluciones Posibles:**

1.  **Compilador Desactualizado:** Es posible que tu sistema tenga una versión anterior de GCC o Clang instalada como compilador predeterminado. Los headers del kernel podrían estar compilados con un compilador más nuevo que usa esta opción, pero el sistema de compilación del controlador NVIDIA está utilizando uno más antiguo.

    **Solución:**
    * **Instalar un compilador más nuevo:** Puedes intentar instalar una versión más reciente de GCC.
        ```bash
        sudo apt update
        sudo apt install gcc-12  # O una versión posterior como gcc-13
        ```
    * **Actualizar tu entorno de compilación:** Asegúrate de que tus herramientas de compilación estén actualizadas.
        ```bash
        sudo apt update
        sudo apt install build-essential
        ```
    * **Especificar el compilador (si es posible):** Algunos sistemas de compilación te permiten especificar el compilador a usar. Consulta las instrucciones o archivos de configuración de la compilación del controlador NVIDIA para encontrar opciones relacionadas con el compilador (por ejemplo, la variable de entorno `CC`).

2.  **Incompatibilidad con la Configuración de Compilación del Kernel:** El kernel que estás usando podría haber sido compilado con un compilador que habilitó esta opción, y el sistema de compilación del controlador NVIDIA la está heredando o encontrando de una manera que causa un fallo con su propio compilador.

    **Solución:**
    * **Probar una versión diferente del controlador NVIDIA:** Es posible que la última versión del controlador NVIDIA tenga mejor compatibilidad con kernels y características del compilador más nuevos. Podrías intentar instalar una versión estable más reciente.
        ```bash
        sudo apt update
        sudo apt install nvidia-driver-<latest-version>
        ```
        Reemplaza `<latest-version>` con el nombre del paquete de controlador más nuevo recomendado para tu sistema. Normalmente puedes encontrarlo buscando `apt search nvidia-driver`.
    * **Revertir tu kernel (como solución temporal):** Si tienes una versión anterior del kernel instalada que funcionaba con tu controlador NVIDIA, puedes arrancar con ese kernel desde el menú GRUB. Esta no es una solución permanente, pero puede darte un sistema funcional mientras solucionas el problema del controlador con el kernel más nuevo.

3.  **Problema con el Paquete del Controlador NVIDIA:** Podría haber un problema con el paquete específico del controlador NVIDIA que estás intentando instalar en relación con la configuración de tu kernel y compilador.

    **Solución:**
    * **Probar un método de instalación diferente:** Si instalaste el controlador a través de `apt`, podrías intentar descargar el controlador directamente desde el sitio web de NVIDIA e instalarlo usando el archivo `.run`. Sigue cuidadosamente las instrucciones proporcionadas por NVIDIA.
    * **Buscar problemas conocidos:** Busca en foros en línea o en el sitio web de soporte de NVIDIA para encontrar problemas conocidos con la combinación específica de versión de controlador y kernel que estás usando.

**Pasos a Intentar:**

1.  **Verifica tu versión de GCC:**
    ```bash
    gcc --version
    ```
    Compara esto con la versión de GCC que podría haberse usado para compilar el kernel (puedes encontrar información sobre el entorno de compilación del kernel en línea para tu versión de Ubuntu).

2.  **Intenta instalar un controlador NVIDIA más nuevo:**
    ```bash
    sudo apt update
    sudo apt install nvidia-driver-550  # Ejemplo: probar una versión más nueva
    sudo reboot
    ```

3.  **Si lo anterior no funciona, intenta purgar y reinstalar el controlador recomendado:**
    ```bash
    sudo apt remove --purge nvidia-*
    sudo apt autoremove
    sudo apt update
    sudo ubuntu-drivers autoinstall  # Instala los controladores recomendados
    sudo reboot
    ```

4.  **Si aún enfrentas problemas, considera instalar una versión más nueva de GCC (ten cuidado, ya que esto a veces puede tener efectos secundarios no deseados):**
    ```bash
    sudo apt install gcc-12 g++-12
    sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-12 12
    sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-12 12
    # Quizás quieras mantener la versión anterior también y volver a cambiarla si es necesario
    # Para volver a cambiar: sudo update-alternatives --config gcc y sudo update-alternatives --config g++
    sudo apt install build-essential # Asegúrate de que las herramientas de compilación estén actualizadas después del cambio de compilador
    sudo dpkg --configure -a # Reconfigura los paquetes
    sudo reboot
    ```

Recuerda reiniciar tu sistema después de intentar cualquier instalación de controlador o cambio significativo en el sistema. Supervisa cuidadosamente la salida para detectar cualquier nuevo mensaje de error. Si continúas teniendo problemas, proporcionar más detalles sobre tu versión de Ubuntu podría ayudar a encontrar una solución más específica.

---

Parece que estás encontrando problemas de dependencia y de DKMS (Dynamic Kernel Module Support) al intentar configurar los paquetes del kernel de Linux, particularmente con el módulo del controlador NVIDIA que falla al compilarse para el nuevo kernel (6.8.0-60-generic).

### Aquí te mostramos cómo resolver esto:

---

### **1. Corrige las Dependencias y Configura los Paquetes**
Primero, intenta corregir los problemas de dependencia y configurar los paquetes:

```bash
sudo apt --fix-broken install
sudo dpkg --configure -a
```

Si eso no funciona, fuerza manualmente la configuración de los paquetes problemáticos:

```bash
sudo apt install -f linux-headers-generic-hwe-22.04 linux-generic-hwe-22.04
```

---

### **2. Reinstala los Controladores NVIDIA**
El error muestra que el módulo NVIDIA DKMS (`nvidia/535.183.06`) falló al compilarse para el kernel `6.8.0-60-generic`. Para solucionarlo:

#### **Opción A: Reinstalar el controlador NVIDIA**
```bash
sudo apt install --reinstall nvidia-dkms-535 nvidia-driver-535
```

#### **Opción B: Purgar y Reinstalar los controladores NVIDIA**
Si reinstalar no funciona, intenta una reinstalación limpia:
```bash
sudo apt purge nvidia-*
sudo apt autoremove
sudo apt install nvidia-driver-535
```

#### **Opción C: Arrancar temporalmente con un kernel anterior**
Si el sistema no es arrancable, reinicia en un kernel anterior (selecciónalo en GRUB) y luego:
```bash
sudo apt remove linux-image-6.8.0-60-generic linux-headers-6.8.0-60-generic
sudo update-grub
```

---

### **3. Revisa el Registro de Compilación de DKMS**
El error menciona `/var/lib/dkms/nvidia/535.183.06/build/make.log`. Revísalo para obtener detalles:
```bash
cat /var/lib/dkms/nvidia/535.183.06/build/make.log
```

Esto puede revelar por qué falló la compilación del módulo (por ejemplo, dependencias faltantes, problemas del compilador).

---

### **4. Instala Manualmente las Dependencias Faltantes**
Si el registro muestra dependencias faltantes, instálalas:
```bash
sudo apt install build-essential linux-headers-generic
```

---

### **5. Recompila los Módulos DKMS**
Después de corregir las dependencias, recompila manualmente los módulos:
```bash
sudo dkms remove nvidia/535.183.06 --all
sudo dkms install nvidia/535.183.06
```

---

### **6. Actualiza Initramfs**
Después de solucionar el controlador NVIDIA, actualiza el initramfs:
```bash
sudo update-initramfs -u -k all
```

---

### **7. Intento de Reparación Final**
Si todo lo demás falla, elimina el kernel problemático y quédate con uno anterior:
```bash
sudo apt purge linux-image-6.8.0-60-generic linux-headers-6.8.0-60-generic
sudo apt autoremove
sudo update-grub
```

Luego, espera a que haya un controlador NVIDIA o kernel actualizado antes de intentarlo nuevamente.

---

### **8. Previene Problemas Futuros**
Para evitar problemas similares, considera:
- **Deshabilitar las actualizaciones automáticas del kernel** (si dependes de los controladores NVIDIA):
  ```bash
  sudo apt-mark hold linux-image-generic linux-headers-generic
  ```
- **Usar el controlador oficial de NVIDIA** (en lugar del paquete de Ubuntu) si la compatibilidad es un problema recurrente.

---

### **Notas Finales**
- Si el sistema se vuelve no arrancable, usa **GRUB** para seleccionar un kernel anterior.
- Si los controladores NVIDIA son críticos para tu flujo de trabajo, considera usar **kernels LTS** (no HWE) para una mejor estabilidad.

Déjame saber si necesitas más ayuda.

---

Si solo quieres proceder con `apt upgrade` y **omitir los paquetes problemáticos**, puedes excluirlos temporalmente del proceso de actualización. Aquí te mostramos cómo:

### **Opción 1: Omitir Paquetes Rotos y Continuar la Actualización**
Ejecuta:
```bash
sudo apt --fix-broken install
sudo apt upgrade -y --ignore-missing --allow-downgrades
```
- `--ignore-missing` omite los paquetes no disponibles.
- `--allow-downgrades` permite que APT degrade paquetes si es necesario.

### **Opción 2: Bloquear (Mantener) los Paquetes Problemáticos**
Si el problema persiste, **bloquea** (mantén) los paquetes problemáticos para evitar que se actualicen:
```bash
sudo apt-mark hold linux-generic-hwe-22.04 linux-headers-generic-hwe-22.04 linux-image-6.8.0-60-generic
```
Luego, vuelve a intentar:
```bash
sudo apt upgrade -y
```

### **Opción 3: Forzar la Actualización (No Recomendado)**
Si estás de acuerdo con la posibilidad de empeorar las cosas, fuerza la actualización:
```bash
sudo apt -o Dpkg::Options::="--force-overwrite" --fix-broken install
sudo apt upgrade -y
```
⚠️ **Advertencia:** Esto puede causar inestabilidad si las dependencias no coinciden.

### **Después de Omitir:**
- El sistema seguirá funcionando, pero el **controlador NVIDIA podría no funcionar** en el kernel `6.8.0-60`.
- Puedes **arrancar con un kernel anterior** (selecciónalo en GRUB) si es necesario.
- Una vez que NVIDIA lance una actualización compatible, puedes **desbloquear** los paquetes:
  ```bash
  sudo apt-mark unhold linux-generic-hwe-22.04 linux-headers-generic-hwe-22.04
  ```

¿Te gustaría ayuda para verificar qué kernel está actualmente activo después de la actualización?