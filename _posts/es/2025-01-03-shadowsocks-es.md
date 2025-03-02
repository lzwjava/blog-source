---
audio: false
generated: false
lang: es
layout: post
title: Problemas con el Proxy de Shadowsocks
translated: true
---

Zhiwei:

Salí a hacer una barbacoa con un amigo y usé Shadowsocks con un servidor basado en Singapur como proxy para sortear el Gran Cortafuegos (GFW). Mientras usaba 5G en el exterior, no pude conectarme, y la prueba se agotó al intentar acceder a YouTube. Sin embargo, cuando estoy en casa usando 4G o mi red doméstica de China Telecom, Shadowsocks funciona bien. ¿Por qué está pasando esto?

Mistral:

Parece que estás experimentando problemas de conectividad con tu proxy de Shadowsocks cuando usas 5G en el exterior, pero no cuando usas 4G o tu red doméstica. Podría haber varias razones para esto:

1. Diferencias en la configuración de la red:
   - Red 5G: La red 5G podría tener configuraciones o restricciones diferentes en comparación con la 4G. Algunos operadores podrían tener reglas de cortafuegos más estrictas o un enrutamiento de red diferente para la 5G, lo que podría afectar el rendimiento de tu proxy de Shadowsocks.
   - Red 4G: La red 4G podría tener configuraciones más relajadas o un enrutamiento mejor que permite que tu proxy de Shadowsocks funcione correctamente.

2. Restricciones del ISP:
   - Políticas del operador: Diferentes operadores podrían tener políticas distintas respecto al uso de VPNs o proxies. Tu operador de 5G podría tener políticas más estrictas que bloqueen o limiten el tráfico de VPN, incluyendo Shadowsocks.
   - Red doméstica: Tu red doméstica, proporcionada por China Telecom, podría tener menos restricciones, permitiendo que Shadowsocks funcione sin problemas.

3. Fortaleza y estabilidad de la señal:
   - Señal 5G: La estabilidad y fortaleza de la señal 5G pueden variar, especialmente en entornos exteriores. Señales débiles o inestables pueden causar problemas de conectividad, incluyendo tiempos de espera agotados.
   - Señal 4G: La señal 4G podría ser más estable y consistente, proporcionando una mejor conexión para tu proxy de Shadowsocks.

4. Ubicación del servidor proxy:
   - Servidor en Singapur: La ubicación de tu servidor de Shadowsocks en Singapur podría afectar la latencia y la conectividad. La red 5G podría tener una latencia más alta o un enrutamiento menos óptimo hacia el servidor de Singapur en comparación con la red 4G o tu red doméstica.

5. Configuración del dispositivo:
   - Configuración: Asegúrate de que la configuración de tu dispositivo esté correctamente configurada para usar Shadowsocks. A veces, cambiar de red (de 5G a 4G o Wi-Fi doméstico) puede hacer que los ajustes se reinicien o cambien.
   - Permisos de la aplicación: Asegúrate de que la aplicación de Shadowsocks tenga los permisos necesarios para operar en diferentes redes.

### Pasos para solucionar el problema:

1. Verifica la configuración de la red:
   - Asegúrate de que la configuración de Shadowsocks esté correctamente configurada tanto para redes 5G como 4G.
   - Verifica que no haya restricciones o configuraciones específicas en tu red 5G que puedan estar bloqueando el proxy.

2. Prueba diferentes servidores:
   - Intenta conectarte a diferentes servidores de Shadowsocks para ver si el problema es específico del servidor de Singapur.
   - Verifica la latencia y la estabilidad de la conexión al servidor.

3. Contacta a tu operador:
   - Si el problema persiste, contacta a tu operador de 5G para preguntar sobre cualquier restricción o configuración que pueda estar afectando tu conexión de Shadowsocks.

4. Actualiza el software:
   - Asegúrate de que la aplicación de Shadowsocks y el software de tu dispositivo estén actualizados. A veces, las actualizaciones pueden resolver problemas de conectividad.

5. Usa proxies alternativos:
   - Considera usar servicios de proxy o VPN alternativos que puedan tener mejor compatibilidad con tu red 5G.

Al verificar sistemáticamente estos factores, deberías poder identificar la causa del problema de conectividad y encontrar una solución adecuada.

-- 

Actualización:

En realidad, mi Wi-Fi doméstico usa China Mobile Communications Corporation, y su dirección es algo como 120.235.8.xx.

Curiosamente, he observado patrones de conectividad inconsistentes: mientras que mi servidor proxy funciona normalmente en datos móviles y redes de China Telecom, ocasionalmente no se conecta cuando uso mi red Wi-Fi doméstica.