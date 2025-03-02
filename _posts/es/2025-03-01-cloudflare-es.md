---
audio: false
generated: true
lang: es
layout: post
title: Empezando con Cloudflare
translated: true
---

Cloudflare es un servicio popular que ofrece una gama de herramientas para mejorar el rendimiento, la seguridad y la fiabilidad de tu sitio web. Ya sea que estés gestionando un pequeño blog o un gran sitio de comercio electrónico, las características de Cloudflare, como la gestión de DNS, la red de entrega de contenido (CDN) y las protecciones de seguridad, pueden marcar una gran diferencia. En esta publicación de blog, te guiaremos a través de tres tareas clave: configurar DNS, gestionar registros A y bloquear regiones de IP. Estas son esenciales para sacar el máximo provecho de Cloudflare y son más fáciles de configurar de lo que podrías pensar.

### **¿Por qué usar Cloudflare?**

Antes de sumergirnos en el cómo, echemos un vistazo rápido a lo que hace que Cloudflare sea tan valioso:
- **Gestión de DNS**: Cloudflare proporciona servicios de DNS rápidos y confiables, asegurando que tu sitio web siempre esté accesible.
- **CDN**: Acelera tu sitio almacenando en caché el contenido más cerca de tus visitantes.
- **Seguridad**: Cloudflare ofrece protección contra DDoS, cifrado SSL/TLS y herramientas para bloquear el tráfico malicioso.
- **Facilidad de uso**: Además, Cloudflare tiene un plan gratuito que es perfecto para pequeños sitios web y blogs.

Ahora, entremos en los detalles.

---

### **Paso 1: Configurar DNS en Cloudflare**

El DNS (Sistema de Nombres de Dominio) es como la guía telefónica de Internet: traduce tu nombre de dominio (por ejemplo, `example.com`) en una dirección IP que los servidores pueden entender. Cuando usas Cloudflare, gestionarás tus registros DNS a través de su plataforma, que ofrece velocidad y seguridad adicionales.

#### **Cómo configurar DNS de Cloudflare:**
1. **Registrarse en Cloudflare**: Si aún no tienes una cuenta, ve al [sitio web de Cloudflare](https://www.cloudflare.com/) y registrate para una cuenta gratuita.
2. **Agregar tu dominio**: Una vez iniciada la sesión, haz clic en “Agregar un sitio” e ingresa tu nombre de dominio (por ejemplo, `example.com`). Cloudflare escaneará tus registros DNS existentes.
3. **Revisar registros DNS**: Después del escaneo, Cloudflare te mostrará una lista de tus registros DNS actuales. Puedes revisarlos para asegurarte de que todo esté correcto.
4. **Cambiar tus servidores de nombres**: Para usar el DNS de Cloudflare, necesitas actualizar los servidores de nombres de tu dominio en tu registrador de dominios (por ejemplo, GoDaddy, Namecheap). Cloudflare te proporcionará dos servidores de nombres (por ejemplo, `ns1.cloudflare.com` y `ns2.cloudflare.com`). Inicia sesión en el panel de control de tu registrador, encuentra la configuración de servidores de nombres para tu dominio y reemplaza los servidores de nombres existentes con los de Cloudflare.
5. **Esperar la propagación**: Los cambios en DNS pueden tardar hasta 24 horas en propagarse, pero generalmente es mucho más rápido. Una vez completado, tu dominio estará utilizando el DNS de Cloudflare.

**Nota importante**: Asegúrate de copiar los servidores de nombres exactamente como se proporcionan en Cloudflare. Servidores de nombres incorrectos pueden hacer que tu sitio se caiga.

---

### **Paso 2: Gestionar registros A en Cloudflare**

Un registro A es un tipo de registro DNS que mappa tu dominio (o subdominio) a una dirección IPv4. Por ejemplo, indica a Internet que `example.com` debe apuntar a `192.0.2.1`. Cloudflare facilita la adición, edición o eliminación de registros A.

#### **Cómo gestionar registros A:**
1. **Iniciar sesión en Cloudflare**: Ve a tu panel de Cloudflare y selecciona el dominio que deseas gestionar.
2. **Navegar a DNS**: Haz clic en la pestaña “DNS” en el menú superior.
3. **Agregar un registro A**:
   - Haz clic en “Agregar registro.”
   - Selecciona “A” del menú desplegable de tipo.
   - Ingresa el nombre (por ejemplo, `www` para `www.example.com` o déjalo en blanco para el dominio raíz).
   - Ingresa la dirección IPv4 a la que deseas apuntar.
   - Elige si deseas proxyar el registro a través de Cloudflare (más sobre esto a continuación).
   - Establece el TTL (Time to Live). Para registros proxyados, se establece por defecto en 300 segundos.
   - Haz clic en “Guardar.”
4. **Editar un registro A**: Encuentra el registro A existente en la lista, haz clic en “Editar”, realiza tus cambios y haz clic en “Guardar.”
5. **Eliminar un registro A**: Haz clic en “Editar” junto al registro y luego en “Eliminar.” Confirma la eliminación.

**Proxy vs. Solo DNS**:
- **Proxy (Nube Naranja)**: El tráfico pasa a través de Cloudflare, habilitando características de CDN, seguridad y rendimiento.
- **Solo DNS (Nube Gris)**: El tráfico va directamente a tu servidor, omitiendo las protecciones de Cloudflare. Usa esto para registros que no necesitan las características de Cloudflare (por ejemplo, servidores de correo).

**Consejo rápido**: Cloudflare también admite registros AAAA para direcciones IPv6. El proceso para gestionarlos es el mismo que para los registros A.

---

### **Paso 3: Bloquear regiones de IP en Cloudflare**

Cloudflare te permite bloquear el tráfico de países o regiones específicos, lo que puede ayudar a reducir el spam, los bots y los ataques maliciosos. Esta característica es especialmente útil si notas tráfico no deseado de ciertas áreas.

#### **Cómo bloquear regiones de IP:**
1. **Iniciar sesión en Cloudflare**: Ve a tu panel de Cloudflare y selecciona tu dominio.
2. **Navegar a Seguridad**: Haz clic en la pestaña “Seguridad”, luego selecciona “WAF” (Firewall de Aplicación Web).
3. **Crear una regla**:
   - Haz clic en “Crear regla de firewall.”
   - Dale un nombre a tu regla (por ejemplo, “Bloquear países específicos”).
   - Configura la regla para bloquear el tráfico basado en el país del visitante. Por ejemplo:
     - Campo: “País”
     - Operador: “está en”
     - Valor: Selecciona los países que deseas bloquear.
   - Elige la acción: “Bloquear.”
   - Haz clic en “Desplegar.”
4. **Monitorear tráfico bloqueado**: Puedes ver las solicitudes bloqueadas en la pestaña “Seguridad” bajo “Eventos.”

**Nota importante**: Usa esta característica con cuidado. Bloquear regiones enteras puede impedir que usuarios legítimos accedan a tu sitio. Es mejor monitorear tu tráfico y solo bloquear regiones si estás seguro de que es necesario.

---

### **Consejos adicionales y mejores prácticas**

- **Usar el plan gratuito de Cloudflare**: Es perfecto para pequeños sitios web e incluye características esenciales como la gestión de DNS, CDN y seguridad básica.
- **Proxyar tus registros**: Para un rendimiento y seguridad óptimos, proxya tus registros A y AAAA a través de Cloudflare siempre que sea posible.
- **Configurar SSL/TLS**: Cloudflare ofrece certificados SSL gratuitos para cifrar el tráfico entre tus visitantes y tu sitio. Puedes habilitar esto en la pestaña “SSL/TLS”.
- **Explorar la caché**: La caché de Cloudflare puede acelerar significativamente tu sitio. Echa un vistazo a la pestaña “Caché” para configurarla.
- **Monitorear tu sitio**: Usa las analíticas de Cloudflare para mantener un ojo en el tráfico, amenazas y rendimiento.

---

### **Conclusión**

Cloudflare es una herramienta poderosa que puede mejorar la velocidad, seguridad y fiabilidad de tu sitio web. Siguiendo los pasos de esta guía, puedes configurar fácilmente DNS, gestionar registros A y bloquear regiones de IP para proteger tu sitio. Recuerda:
- **Configuración de DNS**: Actualiza tus servidores de nombres correctamente para evitar la inactividad.
- **Registros A**: Úsalos para mappear tu dominio a la dirección IP de tu servidor y considera proxyarlos para obtener beneficios adicionales.
- **Bloqueo de regiones de IP**: Usa esta característica con moderación para evitar bloquear a usuarios legítimos.

Cloudflare ofrece muchas más características, como cifrado SSL/TLS, caché y herramientas de seguridad avanzadas. Una vez que te sientas cómodo con los conceptos básicos, explora estas opciones para obtener aún más de la plataforma.