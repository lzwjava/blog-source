---
audio: false
generated: true
lang: es
layout: post
title: Administrador de Credenciales de Git Diagnóstico
translated: true
type: note
---

La salida de `git credential-manager diagnose` ahora indica claramente un **fallo de red**, además de la advertencia de verificación del certificado TLS. Analicemos el error y cómo solucionarlo:

**Hallazgos Clave:**

*   **Fallo de Red:**
    * La prueba de diagnóstico falló con el error: `System.Net.Http.HttpRequestException: nodename nor servname provided, or not known (example.com:443)`.
    * Este error significa que Git Credential Manager no pudo resolver el nombre de host `example.com` a una dirección IP, o no pudo conectarse al puerto 443 en ese host.
    * El registro de diagnóstico muestra que la solicitud HEAD a `https://example.com` falló.
*   **Interferencia del Proxy (Causa Probable):**
    * La presencia de `HTTP_PROXY: http://127.0.0.1:7890` y `HTTPS_PROXY: http://127.0.0.1:7890` sugiere fuertemente que el proxy es la causa principal del fallo de red.
    * El hecho de que el diagnóstico pueda acceder a [http://httpforever.com](http://httpforever.com), pero no a [https://example.com](https://example.com), indica que el proxy está teniendo problemas con las solicitudes https.
*   **Verificación de Certificado TLS Desactivada (Riesgo de Seguridad):**
    * Como antes, la verificación del certificado TLS está desactivada, lo cual es una gran preocupación de seguridad.

**Pasos para Solucionar el Problema:**

1.  **Verificación del Proxy:**
    * **Probar el Proxy:** Abre un navegador web e intenta acceder a `https://example.com` directamente. Si encuentras un error de "no se puede conectar" o "nombre de host no encontrado", es probable que tu proxy esté mal configurado.
    * **Problemas del Software del Proxy:**
        * Reinicia tu software de proxy (Shadowsocks, Clash, etc.).
        * Revisa los registros del software del proxy en busca de mensajes de error.
        * Asegúrate de que el proxy esté configurado para manejar correctamente el tráfico HTTPS.
        * Asegúrate de que el software del proxy esté en ejecución.
    * **Configuración del Proxy:**
        * Verifica nuevamente la configuración de tu proxy en las preferencias de red del sistema operativo y en cualquier archivo de configuración de Git.
        * Verifica que la dirección del proxy (`127.0.0.1`) y el puerto (`7890`) sean correctos.
        * Desactiva temporalmente el proxy en la configuración de red de tu sistema operativo y vuelve a ejecutar `git credential-manager diagnose`.
2.  **Resolución DNS:**
    * Aunque el mensaje de error sugiere un problema de resolución de nombre de host, el proxy es el culpable más probable. Sin embargo, aún vale la pena verificar la configuración de tu DNS.
    * Intenta usar un servidor DNS público (por ejemplo, 8.8.8.8, 1.1.1.1).
3.  **Verificación del Certificado TLS:**
    * **Reactivar la Verificación de Certificados:** Esto es crucial para la seguridad. Sigue las instrucciones proporcionadas en el enlace `https://aka.ms/gcm/tlsverify`.
    * Si tu software de proxy está diseñado para interceptar tráfico HTTPS, asegúrate de instalar el certificado raíz del proxy en el almacén de certificados raíz de confianza de tu sistema operativo. Esta es la forma segura de permitir que el proxy funcione.
4.  **Configuración de Git:**
    * Ejecuta `git config --global --list` para examinar tu configuración de Git.
    * Elimina temporalmente la configuración del proxy de Git para aislar el problema:
        ```bash
        git config --global --unset http.proxy
        git config --global --unset https.proxy
        ```
    * Después de eliminar la configuración del proxy, vuelve a ejecutar el comando `git credential-manager diagnose`.
5.  **Firewall:**
    * Desactiva temporalmente cualquier firewall en tu computadora, para descartar interferencias del firewall.
6.  **Conexión de Red:**
    * Prueba tu conexión de red usando otras aplicaciones de red, para asegurarte de que la red en sí sea estable.
    * Si estás usando un punto de acceso móvil, muévete a un lugar con mejor intensidad de señal.

**Conclusión Principal:** El proxy es casi con certeza la causa de los fallos de red. Configurar correctamente el proxy y reactivar la verificación de certificados TLS son los pasos más importantes.