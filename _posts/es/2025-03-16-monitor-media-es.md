---
audio: false
generated: true
lang: es
layout: post
title: Supervisar la Reproducción de Medios en Ubuntu mediante VLC
translated: true
type: note
---

Para ver películas en tu monitor usando tu segunda laptop (con Ubuntu y un servidor Nginx) sin muchas complicaciones, aquí está el mejor enfoque basado en lo que ya tienes. Quieres evitar comprar dispositivos adicionales como un Fire TV Stick o Apple TV, y aunque un cable HDMI largo funciona, preferirías no tener que interactuar constantemente con la laptop para seleccionar y reproducir videos. Configuremos una solución que sea simple y conveniente usando tu configuración actual.

Dado que tus películas están almacenadas en tu laptop con Ubuntu y ya está ejecutando un servidor Nginx, la forma más fácil es conectar esa laptop directamente a tu monitor via HDMI y hacer que el control de reproducción sea sencillo. Así es como puedes hacerlo:

### Solución: Conectar la Laptop al Monitor y Usar VLC con Control Remoto

#### Qué Necesitarás
- **Cable HDMI**: Para conectar tu laptop con Ubuntu al monitor.
- **Reproductor multimedia VLC**: Probablemente ya está instalado en Ubuntu, o es fácil de instalar.
- **Teléfono inteligente u otro dispositivo**: Para controlar la reproducción de forma remota a través de tu red doméstica.

#### Pasos para Configurar
1. **Conectar la Laptop al Monitor**
   - Enchufa un extremo del cable HDMI en el puerto HDMI de tu laptop con Ubuntu y el otro en la entrada HDMI de tu monitor.
   - Enciende el monitor y selecciona la entrada HDMI correcta. La pantalla de la laptop ahora debería aparecer en el monitor, incluyendo video y audio (si tu monitor tiene altavoces; de lo contrario, usa los altavoces de la laptop o conecta unos externos).

2. **Instalar VLC (si no está instalado)**
   - Abre una terminal en tu laptop con Ubuntu y ejecuta:
     ```
     sudo apt update
     sudo apt install vlc
     ```
   - Esto asegura que VLC, un reproductor multimedia versátil, esté listo para usar.

3. **Habilitar la Interfaz Web de VLC para Control Remoto**
   - Abre VLC en tu laptop con Ubuntu.
   - Ve a **Herramientas > Preferencias**.
   - En la parte inferior izquierda, haz clic en **"Todo"** para mostrar la configuración avanzada.
   - Navega a **Interfaz > Interfaces principales**, y marca la casilla **"Web"** para habilitar la interfaz HTTP.
   - Ve a **Interfaz > Interfaces principales > Lua**, y establece una contraseña (por ejemplo, "micontraseña") en el campo **Contraseña HTTP de Lua**.
   - Haz clic en **Guardar**, luego reinicia VLC.

4. **Cargar Tus Películas en VLC**
   - En VLC, ve a **Reproducción > Lista de reproducción**.
   - Arrastra y suelta tus archivos de película desde su carpeta (donde están almacenados en la laptop) a la lista de reproducción de VLC, o usa **Medios > Abrir archivo** para agregarlos uno por uno.
   - Guarda la lista de reproducción (por ejemplo, "Mis Películas") mediante **Ctrl+Y** para un acceso rápido después.

5. **Encontrar la Dirección IP de tu Laptop**
   - En la terminal, escribe:
     ```
     ip addr show
     ```
   - Busca la dirección IP bajo tu conexión de red (por ejemplo, `192.168.1.100` bajo `wlan0` para Wi-Fi). Así es como tu teléfono se conectará a la laptop.

6. **Controlar la Reproducción desde tu Teléfono**
   - Asegúrate de que tu teléfono y la laptop estén en la misma red Wi-Fi.
   - Abre un navegador web en tu teléfono e ingresa: `http://<ip-de-la-laptop>:8080` (por ejemplo, `http://192.168.1.100:8080`).
   - Cuando te lo pida, deja el nombre de usuario en blanco e ingresa la contraseña que estableciste (por ejemplo, "micontraseña").
   - Verás la interfaz web de VLC. Úsala para reproducir, pausar, detener o seleccionar la siguiente película de tu lista de reproducción.

7. **Comenzar a Ver**
   - En la laptop, comienza a reproducir una película en VLC (haz doble clic en un elemento de la lista de reproducción).
   - Cambia VLC al modo de pantalla completa (**Ver > Pantalla completa** o presiona `F`).
   - Siéntate y usa tu teléfono para controlar la reproducción sin tocar la laptop.

#### Por Qué Esto Funciona para Ti
- **Sin Costo Adicional**: Usa tu laptop, monitor y teléfono existentes—no necesitas comprar nada nuevo.
- **Mínimas Molestias**: Después de la configuración inicial, solo enciendes la laptop y el monitor, abres VLC y controlas todo desde tu teléfono.
- **Reproducción Local**: Dado que las películas están en la laptop conectada al monitor, no necesitas transmitirlas por la red (aunque Nginx está configurado, no es necesario aquí). VLC reproduce los archivos directamente, garantizando un rendimiento fluido.

#### Mejoras Opcionales
- **Control Inalámbrico**: Si tienes un mouse o teclado inalámbrico, podrías usarlo en lugar de tu teléfono, pero el teléfono es más conveniente a distancia.
- **Inicio Automático**: Para hacerlo aún más fácil, configura VLC para que inicie tu lista de reproducción automáticamente cuando la laptop se encienda:
  - Agrega VLC con tu lista de reproducción a las **Aplicaciones de inicio** de Ubuntu (busca "Aplicaciones de inicio" en Ubuntu, haz clic en "Agregar", e ingresa: `vlc /ruta/a/tu/lista.m3u`).
- **Verificación de Audio**: Si a tu monitor le faltan altavoces, asegúrate de que el audio salga a través de la laptop o conecta altavoces externos via la toma de audio de la laptop.

### Alternativa: Usar Nginx y un Navegador (si lo Prefieres)
Si prefieres usar el servidor Nginx:
- Configura una página HTML simple en tu directorio de Nginx (por ejemplo, `/var/www/html/peliculas`) con enlaces a tus archivos de película (por ejemplo, `<a href="pelicula1.mp4">Película 1</a>`).
- Conecta la laptop al monitor, abre un navegador y ve a `http://localhost/peliculas`.
- Haz clic en un enlace para reproducir una película en el navegador y usa el modo de pantalla completa.
- Sin embargo, esto no permite fácilmente el control desde el teléfono a menos que accedas a la misma página desde tu teléfono y transmitas, lo que podría requerir configuración o hardware adicional.

### Recomendación Final
El método de VLC es el más adecuado. Es directo, aprovecha tu configuración actual y te permite "abrir el monitor, y luego ver sin muchas complicaciones" controlando todo desde tu teléfono. Después de configurarlo una vez, solo necesitarás iniciar VLC y usar tu teléfono para elegir películas—¡simple y efectivo