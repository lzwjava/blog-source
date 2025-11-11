---
audio: false
generated: true
lang: es
layout: post
title: Primeros Pasos con Cloudflare
translated: true
type: note
---

Cloudflare es un servicio popular que ofrece una variedad de herramientas para mejorar el rendimiento, la seguridad y la confiabilidad de tu sitio web. Ya sea que administres un blog pequeño o un gran sitio de comercio electrónico, las funciones de Cloudflare—como la gestión de DNS, la red de entrega de contenido (CDN) y las protecciones de seguridad—pueden marcar una diferencia significativa. En esta publicación de blog, repasaremos tres tareas clave: configurar DNS, gestionar registros A y prohibir regiones IP. ¡Estas son esenciales para sacar el máximo provecho de Cloudflare y son más fáciles de configurar de lo que podrías pensar!

### **¿Por qué usar Cloudflare?**

Antes de profundizar en el cómo, cubramos rápidamente qué hace que Cloudflare sea tan valioso:
- **Gestión de DNS**: Cloudflare proporciona servicios DNS rápidos y confiables, garantizando que tu sitio web sea siempre accesible.
- **CDN**: Acelera tu sitio almacenando en caché el contenido más cerca de tus visitantes.
- **Seguridad**: Cloudflare ofrece protección DDoS, cifrado SSL/TLS y herramientas para bloquear tráfico malicioso.
- **Facilidad de uso**: Aún mejor, Cloudflare tiene un plan gratuito que es perfecto para sitios web y blogs pequeños.

Ahora, entremos en los detalles.

---

### **Paso 1: Configurar DNS en Cloudflare**

DNS (Sistema de Nombres de Dominio) es como la guía telefónica de Internet—traduce tu nombre de dominio (por ejemplo, `example.com`) a una dirección IP que los servidores puedan entender. Cuando usas Cloudflare, gestionarás tus registros DNS a través de su plataforma, que ofrece velocidad y seguridad adicionales.

#### **Cómo configurar DNS de Cloudflare:**
1. **Regístrate en Cloudflare**: Si aún no tienes una cuenta, ve al [sitio web de Cloudflare](https://www.cloudflare.com/) y regístrate para obtener una cuenta gratuita.
2. **Añade tu dominio**: Una vez que hayas iniciado sesión, haz clic en "Añadir un sitio" e ingresa tu nombre de dominio (por ejemplo, `example.com`). Cloudflare escaneará tus registros DNS existentes.
3. **Revisa los registros DNS**: Después del escaneo, Cloudflare te mostrará una lista de tus registros DNS actuales. Puedes revisarlos para asegurarte de que todo se vea correcto.
4. **Cambia tus nameservers**: Para usar el DNS de Cloudflare, necesitas actualizar los nameservers de tu dominio en tu registrador de dominio (por ejemplo, GoDaddy, Namecheap). Cloudflare te proporcionará dos nameservers (por ejemplo, `ns1.cloudflare.com` y `ns2.cloudflare.com`). Inicia sesión en el panel de control de tu registrador, encuentra la configuración de nameservers para tu dominio y reemplaza los nameservers existentes con los de Cloudflare.
5. **Espera a la propagación**: Los cambios de DNS pueden tardar hasta 24 horas en propagarse, pero usualmente es mucho más rápido. Una vez completado, tu dominio estará usando el DNS de Cloudflare.

**Nota importante**: Asegúrate de copiar los nameservers exactamente como los proporciona Cloudflare. Los nameservers incorrectos pueden hacer que tu sitio deje de estar en línea.

---

### **Paso 2: Gestionar registros A en Cloudflare**

Un registro A es un tipo de registro DNS que asigna tu dominio (o subdominio) a una dirección IPv4. Por ejemplo, le indica a Internet que `example.com` debe apuntar a `192.0.2.1`. Cloudflare facilita añadir, editar o eliminar registros A.

#### **Cómo gestionar registros A:**
1. **Inicia sesión en Cloudflare**: Ve a tu panel de control de Cloudflare y selecciona el dominio que deseas gestionar.
2. **Navega a DNS**: Haz clic en la pestaña "DNS" en el menú superior.
3. **Añade un registro A**:
   - Haz clic en "Añadir registro".
   - Selecciona "A" del menú desplegable de tipo.
   - Ingresa el nombre (por ejemplo, `www` para `www.example.com` o déjalo en blanco para el dominio raíz).
   - Ingresa la dirección IPv4 a la que deseas apuntar.
   - Elige si deseas proxy el registro a través de Cloudflare (más sobre esto a continuación).
   - Establece el TTL (Tiempo de Vida). Para registros con proxy, el valor predeterminado es 300 segundos.
   - Haz clic en "Guardar".
4. **Edita un registro A**: Encuentra el registro A existente en la lista, haz clic en "Editar", realiza tus cambios y haz clic en "Guardar".
5. **Elimina un registro A**: Haz clic en "Editar" junto al registro y luego en "Eliminar". Confirma la eliminación.

**Con Proxy vs. Solo DNS**:
- **Con Proxy (Nube Naranja)**: El tráfico pasa a través de Cloudflare, permitiendo las funciones de CDN, seguridad y rendimiento.
- **Solo DNS (Nube Gris)**: El tráfico va directamente a tu servidor, evitando las protecciones de Cloudflare. Usa esto para registros que no necesitan las funciones de Cloudflare (por ejemplo, servidores de correo).

**Consejo rápido**: Cloudflare también admite registros AAAA para direcciones IPv6. El proceso para gestionarlos es el mismo que para los registros A.

---

### **Paso 3: Prohibir regiones IP en Cloudflare**

Cloudflare te permite bloquear el tráfico de países o regiones específicos, lo que puede ayudar a reducir spam, bots y ataques maliciosos. Esta función es especialmente útil si notas tráfico no deseado desde ciertas áreas.

#### **Cómo prohibir regiones IP:**
1. **Inicia sesión en Cloudflare**: Ve a tu panel de control de Cloudflare y selecciona tu dominio.
2. **Navega a Seguridad**: Haz clic en la pestaña "Seguridad", luego selecciona "WAF" (Web Application Firewall).
3. **Crea una regla**:
   - Haz clic en "Crear regla de firewall".
   - Asigna un nombre a tu regla (por ejemplo, "Bloquear países específicos").
   - Configura la regla para bloquear el tráfico basado en el país del visitante. Por ejemplo:
     - Campo: "País"
     - Operador: "está en"
     - Valor: Selecciona los países que deseas bloquear.
   - Elige la acción: "Bloquear".
   - Haz clic en "Implementar".
4. **Monitorea el tráfico bloqueado**: Puedes ver las solicitudes bloqueadas en la pestaña "Seguridad" bajo "Eventos".

**Nota importante**: Usa esta función con cuidado. Bloquear regiones enteras puede evitar involuntariamente que usuarios legítimos accedan a tu sitio. Es mejor monitorear tu tráfico y solo bloquear regiones si estás seguro de que es necesario.

---

### **Consejos y mejores prácticas adicionales**

- **Usa el Plan Gratuito de Cloudflare**: Es perfecto para sitios web pequeños e incluye funciones esenciales como gestión de DNS, CDN y seguridad básica.
- **Usa Proxy en tus Registros**: Para un rendimiento y seguridad óptimos, utiliza el proxy de Cloudflare en tus registros A y AAAA siempre que sea posible.
- **Configura SSL/TLS**: Cloudflare ofrece certificados SSL gratuitos para cifrar el tráfico entre tus visitantes y tu sitio. Puedes activarlo en la pestaña "SSL/TLS".
- **Explora el Almacenamiento en Caché**: El almacenamiento en caché de Cloudflare puede acelerar significativamente tu sitio. Revisa la pestaña "Caching" para configurarlo.
- **Monitorea tu Sitio**: Usa las analíticas de Cloudflare para mantener un ojo en el tráfico, las amenazas y el rendimiento.

---

### **Conclusión**

Cloudflare es una herramienta poderosa que puede mejorar la velocidad, la seguridad y la confiabilidad de tu sitio web. Siguiendo los pasos de esta guía, puedes configurar fácilmente el DNS, gestionar registros A y prohibir regiones IP para proteger tu sitio. Recuerda:
- **Configuración de DNS**: Actualiza tus nameservers correctamente para evitar tiempo de inactividad.
- **Registros A**: Úsalos para asignar tu dominio a la dirección IP de tu servidor, y considera usar el proxy para obtener beneficios adicionales.
- **Bloqueo de Regiones IP**: Usa esta función con moderación para evitar bloquear usuarios legítimos.

Cloudflare ofrece muchas más funciones, como cifrado SSL/TLS, almacenamiento en caché y herramientas de seguridad avanzadas. Una vez que te sientas cómodo con lo básico, explora estas opciones para sacar aún más provecho de la plataforma.