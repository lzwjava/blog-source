---
audio: false
generated: true
lang: es
layout: post
title: Instalación de Arduino IDE en Ubuntu
translated: true
type: note
---

Para instalar el Arduino IDE en Ubuntu Linux, sigue estos pasos:

1. **Descargar el Arduino IDE**:
   - Visita el sitio web oficial de Arduino en [https://www.arduino.cc/en/software](https://www.arduino.cc/en/software).
   - En la sección "Arduino IDE", selecciona la opción de descarga "Linux 64 bits" (o la versión apropiada para tu sistema, por ejemplo, Linux ARM para Raspberry Pi).

2. **Extraer el archivo descargado**:
   - El archivo descargado es un archivo comprimido `.tar.xz` (por ejemplo, `arduino-1.8.19-linux64.tar.xz`).
   - Abre una terminal y navega al directorio de descargas (por ejemplo, `cd ~/Downloads`).
   - Extrae el archivo usando:
     ```bash
     tar -xf arduino-*.tar.xz
     ```
   - Esto crea una carpeta como `arduino-1.8.19`.

3. **Mover a un directorio apropiado (Opcional)**:
   - Para acceso a nivel del sistema, mueve la carpeta extraída a `/opt` (requiere privilegios de superusuario):
     ```bash
     sudo mv arduino-1.8.19 /opt/arduino
     ```

4. **Ejecutar el script de instalación**:
   - Navega a la carpeta de Arduino:
     ```bash
     cd /opt/arduino
     ```
   - Ejecuta el script de instalación:
     ```bash
     sudo ./install.sh
     ```
   - Esto crea un acceso directo en el escritorio y configura los permisos necesarios.

5. **Agregar tu usuario al grupo Dialout**:
   - Para acceder a la placa Arduino a través del puerto serie, agrega tu usuario al grupo `dialout`:
     ```bash
     sudo usermod -a -G dialout $USER
     ```
   - Cierra sesión y vuelve a iniciarla, o reinicia para que el cambio de grupo surta efecto.

6. **Iniciar el Arduino IDE**:
   - Si ejecutaste el script `install.sh`, puedes iniciar el IDE desde el menú de aplicaciones o buscando "Arduino IDE".
   - Alternativamente, ejecútalo directamente desde la terminal:
     ```bash
     /opt/arduino/arduino
     ```

7. **Actualizar permisos para la placa Arduino (si es necesario)**:
   - Al conectar tu Arduino, asegúrate de que sea detectado (por ejemplo, `/dev/ttyACM0` o `/dev/ttyUSB0`).
   - Si encuentras problemas de permisos, establece los permisos correctos:
     ```bash
     sudo chmod a+rw /dev/ttyACM0
     ```
   - Reemplaza `/dev/ttyACM0` con el puerto apropiado.

8. **Verificar la instalación**:
   - Conecta tu placa Arduino via USB.
   - Abre el IDE, ve a **Herramientas > Placa** y selecciona tu modelo de Arduino (por ejemplo, Arduino Uno).
   - Ve a **Herramientas > Puerto** y selecciona el puerto (por ejemplo, `/dev/ttyACM0`).
   - Intenta cargar un sketch de ejemplo (por ejemplo, **Archivo > Ejemplos > 01.Basics > Blink**) para confirmar que todo funciona.

**Alternativa: Instalar via Snap o Flatpak**:
- **Snap**:
  ```bash
  sudo snap install arduino
  ```
- **Flatpak**:
  ```bash
  sudo flatpak install flathub cc.arduino.ArduinoIDE
  ```
- Estos métodos simplifican la instalación pero pueden tener limitaciones con permisos o detección de placas.

**Notas**:
- Asegúrate de tener Java instalado, ya que el Arduino IDE lo requiere. Instálalo si es necesario:
  ```bash
  sudo apt update
  sudo apt install default-jre
  ```
- Para la última versión o solución de problemas, consulta los foros de Arduino o la [documentación oficial](https://www.arduino.cc/en/Guide/Linux).

Si encuentras problemas, ¡házmelo saber tu versión de Ubuntu o el error específico para una ayuda personalizada!

---

Dado que tu Arduino Uno es detectado en el Arduino IDE en Ubuntu y quieres un ejemplo simple sin usar una protoboard o componentes externos, aquí tienes un sketch básico que parpadea el LED integrado en el Arduino Uno (conectado al pin digital 13). Esto no requiere hardware adicional.

```cpp
void setup() {
  // put your setup code here, to run once:
  pinMode(LED_BUILTIN, OUTPUT); // Configurar el pin del LED integrado (pin 13) como salida
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(LED_BUILTIN, HIGH); // Encender el LED
  delay(1000);                     // Esperar 1 segundo
  digitalWrite(LED_BUILTIN, LOW);  // Apagar el LED
  delay(1000);                     // Esperar 1 segundo
}
```

### Cómo ejecutarlo:
1. Abre el Arduino IDE.
2. Copia y pega el código anterior en el IDE.
3. Asegúrate de que tu Arduino Uno esté conectado via USB y sea detectado:
   - Ve a **Herramientas > Placa** y selecciona **Arduino Uno**.
   - Ve a **Herramientas > Puerto** y selecciona el puerto (por ejemplo, `/dev/ttyACM0` o `/dev/ttyUSB0`).
4. Haz clic en el botón **Subir** (icono de flecha derecha) para compilar y cargar el sketch en tu Arduino Uno.
5. Una vez cargado, el LED integrado (etiquetado como "L" en la placa) debería parpadear, encendiéndose durante 1 segundo y apagándose durante 1 segundo, repetidamente.

### Qué hace:
- En `setup()`, la función `pinMode` configura el pin del LED integrado como una salida.
- En `loop()`, la función `digitalWrite` enciende (`HIGH`) y apaga (`LOW`) el LED, con `delay` pausando durante 1 segundo entre cada estado, creando un efecto de parpadeo.

### Notas:
- No se necesitan componentes externos ya que el Arduino Uno tiene un LED integrado en el pin 13.
- Si el LED no parpadea, verifica la selección del puerto o asegúrate de que la placa esté correctamente conectada. También puedes abrir el **Monitor Serie** (Herramientas > Monitor Serie) para depurar si agregas `Serial.begin(9600);` en `setup()` e imprimes mensajes como `Serial.println("Blink");` en `loop()`.
- Si quieres modificar la velocidad del parpadeo, ajusta los valores de `delay(1000)` (por ejemplo, `delay(500)` para un parpadeo más rápido).

¡Házmelo saber si tienes problemas o quieres otro ejemplo simple!

---

El mensaje de error indica un problema de permisos al intentar cargar el sketch a tu Arduino Uno en Ubuntu. El Arduino IDE no puede acceder al puerto serie `/dev/ttyUSB0` debido a permisos insuficientes. Aquí se explica cómo solucionarlo:

### Solución: Corregir los permisos del puerto serie

1. **Agregar tu usuario al grupo `dialout`**:
   - El grupo `dialout` típicamente controla el acceso a los puertos serie en Ubuntu. Agrega tu usuario a este grupo:
     ```bash
     sudo usermod -a -G dialout $USER
     ```
   - Después de ejecutar esto, cierra sesión y vuelve a iniciarla, o reinicia tu sistema para que el cambio surta efecto:
     ```bash
     sudo reboot
     ```

2. **Verificar el puerto**:
   - Después de reiniciar, reconecta tu Arduino Uno y abre el Arduino IDE.
   - Ve a **Herramientas > Puerto** y asegúrate de que `/dev/ttyUSB0` (o `/dev/ttyACM0` para algunas placas Arduino) esté seleccionado. Si no aparece ningún puerto, verifica la conexión USB o prueba con un cable/puerto diferente.

3. **Cambiar temporalmente los permisos del puerto (Opcional)**:
   - Si el problema persiste después de agregar tu usuario al grupo `dialout`, puedes establecer manualmente los permisos para el puerto (esta es una solución temporal, ya que los permisos se restablecen al reiniciar):
     ```bash
     sudo chmod a+rw /dev/ttyUSB0
     ```
   - Reemplaza `/dev/ttyUSB0` con el puerto correcto si es diferente (por ejemplo, `/dev/ttyACM0`).

4. **Intentar cargar de nuevo**:
   - En el Arduino IDE, haz clic en el botón **Subir** para cargar tu sketch (por ejemplo, el sketch del LED parpadeante de antes).
   - Si se carga correctamente, deberías ver el LED integrado en tu Arduino Uno comenzar a parpadear.

### Solución de problemas adicional

- **Verificar la placa Arduino y el cable**:
  - Asegúrate de que el Arduino Uno esté correctamente conectado via USB y reconocido por Ubuntu. Ejecuta este comando para listar los dispositivos conectados:
    ```bash
    ls /dev/tty*
    ```
    Busca `/dev/ttyUSB0` o `/dev/ttyACM0` cuando la placa esté enchufada.
  - Prueba un cable o puerto USB diferente si la placa no es detectada.

- **Verificar la configuración de la placa y el puerto**:
  - En el Arduino IDE, confirma que **Herramientas > Placa** esté configurado como **Arduino Uno**.
  - Si `/dev/ttyUSB0` no aparece, prueba **Herramientas > Puerto** después de desenchufar y volver a enchufar la placa.

- **Ejecutar Arduino IDE como Root (Solución temporal)**:
  - Si los pasos anteriores no funcionan, puedes ejecutar el IDE con privilegios de superusuario para evitar problemas de permisos (no recomendado a largo plazo):
    ```bash
    sudo arduino
    ```
    Reemplaza `arduino` con la ruta a tu ejecutable del Arduino IDE si no está en el PATH de tu sistema (por ejemplo, `/opt/arduino/arduino`).

- **Buscar software conflictivo**:
  - Otro software (por ejemplo, `brltty`, un controlador de pantalla braille) puede interferir con los puertos serie. Elimínalo si está instalado:
    ```bash
    sudo apt remove brltty
    ```

- **Problemas de controladores**:
  - Algunos clones de Arduino usan el chip CH340/CH341, que requiere un controlador. Instálalo si es necesario:
    ```bash
    sudo apt install linux-modules-extra-$(uname -r)
    ```
    Luego, reconecta la placa.

### Confirmar la solución
Una vez resueltos los permisos, intenta cargar el sketch de parpadeo anterior nuevamente:
```cpp
void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH);
  delay(1000);
  digitalWrite(LED_BUILTIN, LOW);
  delay(1000);
}
```

Si aún enfrentas problemas, comparte el nuevo mensaje de error o ejecuta `ls -l /dev/ttyUSB0` en la terminal y proporciona la salida para ayudar a diagnosticar más a fondo.

---

Parece que estás encontrando un problema al intentar cargar un sketch a tu Arduino Uno usando el Arduino IDE en Ubuntu. El mensaje de error que proporcionaste es:

```
avrdude: ser_open(): can't open device "/dev/ttyUSB0": Permission denied
Failed uploading: uploading error: exit status 1
```

Este error indica que el Arduino IDE no tiene los permisos necesarios para acceder al puerto serie (`/dev/ttyUSB0`) donde está conectado tu Arduino Uno. Este es un problema común en sistemas Linux como Ubuntu debido a cómo se gestiona el acceso a los puertos serie. A continuación, se presenta una guía paso a paso para solucionar este problema.

---

### Solución: Corregir el problema de permisos del puerto serie

#### 1. Agregar tu usuario al grupo `dialout`
En Ubuntu, el grupo `dialout` controla el acceso a los puertos serie. Para resolver el problema de permisos, necesitas agregar tu usuario a este grupo.

- Abre una terminal presionando `Ctrl + Alt + T`.
- Ejecuta el siguiente comando:
  ```bash
  sudo usermod -a -G dialout $USER
  ```
- Este comando agrega tu usuario actual al grupo `dialout`. La variable `$USER` usa automáticamente tu nombre de usuario.

#### 2. Cerrar sesión y volver a iniciarla
Para que el cambio de grupo surta efecto, necesitas cerrar sesión en tu sesión actual y volver a iniciarla. Alternativamente, puedes reiniciar tu sistema.

- **Para cerrar sesión y volver a iniciarla:**
  - Guarda cualquier trabajo abierto.
  - Haz clic en tu nombre de usuario en la esquina superior derecha del escritorio de Ubuntu y selecciona "Cerrar sesión".
  - Vuelve a iniciar sesión con tu nombre de usuario y contraseña.
- **Para reiniciar (opcional):**
  - Ejecuta este comando en la terminal:
    ```bash
    sudo reboot
    ```
  - Espera a que tu sistema se reinicie.

#### 3. Verificar el puerto serie
Después de volver a iniciar sesión, asegúrate de que tu Arduino Uno sea reconocido correctamente por el sistema.

- Reconecta tu Arduino Uno al puerto USB.
- Abre el Arduino IDE.
- Ve a **Herramientas > Puerto** en el menú y verifica si `/dev/ttyUSB0` (o `/dev/ttyACM0` para algunas placas Arduino) está listado y seleccionado.
- Si el puerto no aparece:
  - Desenchufa y vuelve a enchufar el Arduino Uno.
  - Verifica la conexión USB o prueba con un cable/puerto diferente.

#### 4. Cargar el sketch de nuevo
Con el puerto correcto seleccionado, intenta cargar tu sketch de nuevo:

```cpp
void setup() {
  pinMode(LED_BUILTIN, OUTPUT); // Configurar el pin del LED integrado (pin 13) como salida
}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH); // Encender el LED
  delay(1000);                     // Esperar 1 segundo
  digitalWrite(LED_BUILTIN, LOW);  // Apagar el LED
  delay(1000);                     // Esperar 1 segundo
}
```

- Haz clic en el botón **Subir** (el icono de flecha derecha) en el Arduino IDE.
- Si es exitoso, el LED integrado en tu Arduino Uno debería comenzar a parpadear (encendido durante 1 segundo, apagado durante 1 segundo).

---

### Solución de problemas adicional
Si los pasos anteriores no resuelven el problema, prueba estas comprobaciones adicionales:

#### Verificar la membresía del grupo
Verifica que tu usuario sea parte del grupo `dialout`:
- Ejecuta este comando en la terminal:
  ```bash
  groups $USER
  ```
- Busca `dialout` en la salida. Si falta, repite el Paso 1 y asegúrate de cerrar/volver a iniciar sesión o reiniciar.

#### Solución temporal de permisos (No recomendado a largo plazo)
Si necesitas una solución rápida, puedes cambiar manualmente los permisos del puerto serie:
- Ejecuta:
  ```bash
  sudo chmod a+rw /dev/ttyUSB0
  ```
- Luego intenta cargar de nuevo. Nota: Esto es temporal y se restablecerá después de desenchufar el Arduino o reiniciar.

#### Buscar software conflictivo
Algunos software, como `brltty` (un controlador de pantalla braille), pueden interferir con los puertos serie. Para eliminarlo:
- Ejecuta:
  ```bash
  sudo apt remove brltty
  ```
- Reconecta tu Arduino e intenta de nuevo.

#### Verificar la conexión del Arduino
Asegúrate de que Ubuntu reconozca tu Arduino:
- Ejecuta:
  ```bash
  ls /dev/tty*
  ```
- Busca `/dev/ttyUSB0` o `/dev/ttyACM0` cuando el Arduino esté enchufado. Si falta, verifica tu cable USB o puerto.

#### Ejecutar Arduino IDE como Root (Solución temporal)
Como último recurso, puedes ejecutar el IDE con privilegios de superusuario:
- Cierra el Arduino IDE.
- Abre una terminal y ejecuta:
  ```bash
  sudo arduino-ide
  ```
- Reemplaza `arduino-ide` con el comando o ruta correcta si es necesario (por ejemplo, `/home/lzw/arduino-ide_2.3.6_Linux_64bit/arduino-ide`).
- Intenta cargar de nuevo. Evita usar este método regularmente, ya que es menos seguro.

---

### Confirmar la solución
Después de seguir estos pasos, tu sketch debería cargarse correctamente y el LED en tu Arduino Uno debería parpadear como se esperaba. Si aún encuentras problemas, por favor proporciona detalles adicionales, tales como:
- La salida de `ls -l /dev/ttyUSB0` (para verificar los permisos).
- Cualquier nuevo mensaje de error del Arduino IDE.

¡Házmelo saber si necesitas más ayuda!