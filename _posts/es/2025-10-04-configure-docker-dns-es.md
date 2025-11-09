---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Configurar los Servidores DNS del Demonio de Docker
translated: true
type: note
---

Para configurar los servidores DNS del daemon de Docker (que serán utilizados por los contenedores a menos que se sobrescriban a nivel del contenedor), puedes editar el archivo `/etc/docker/daemon.json`. Este archivo te permite personalizar el comportamiento en tiempo de ejecución de Docker.

### Pasos para Configurar el DNS

1. **Editar el archivo daemon.json**:
   - Si el archivo no existe, créalo con privilegios de root (por ejemplo, usando `sudo nano /etc/docker/daemon.json` o tu editor preferido).
   - Añade o actualiza la clave `dns` como un array de direcciones IP para los servidores DNS. Por ejemplo, para usar el DNS público de Google (8.8.8.8 y 8.8.4.4):

     ```json
     {
       "dns": ["8.8.8.8", "8.8.4.4"]
     }
     ```

     - Puedes añadir más servidores si es necesario (por ejemplo, el 1.1.1.1 de Cloudflare).
     - Esta configuración se aplica a todos los contenedores creados con la red predeterminada, a menos que se especifique lo contrario.

2. **Validar el JSON**:
   - Asegúrate de que el archivo es un JSON válido. Puedes usar una herramienta como `jq` para comprobarlo: `jq . /etc/docker/daemon.json`. Si da error, corrige la sintaxis.

3. **Reiniciar el servicio de Docker**:
   - Aplica los cambios reiniciando Docker:
     ```
     sudo systemctl restart docker
     ```
     - En sistemas sin systemd (por ejemplo, distribuciones antiguas de Linux), usa `sudo service docker restart`.
   - Verifica el estado: `sudo systemctl status docker`.

4. **Probar la configuración**:
   - Ejecuta un contenedor de prueba y comprueba su resolución DNS:
     ```
     docker run --rm busybox nslookup google.com
     ```
     - Debería resolver usando tus servidores DNS configurados.

### Notas
- **Alcance**: Esto configura el DNS para el daemon de Docker en el host, afectando a la resolución de nombres saliente para los contenedores. No cambia el DNS del sistema del host.
- **Sobrescrituras**: Si un contenedor necesita un DNS diferente (por ejemplo, mediante el flag `--dns` en `docker run`), esto sobrescribirá la configuración a nivel de daemon.
- **Seguridad**: Usar DNS públicos como 8.8.8.8 está bien para la mayoría de los casos, pero considera DNS internos para entornos empresariales.
- **Documentación**: Para más opciones (por ejemplo, dominios de búsqueda DNS), consulta la [documentación oficial de Docker sobre daemon.json](https://docs.docker.com/engine/reference/commandline/dockerd/#daemon-configuration-file).

Si encuentras errores (por ejemplo, problemas de permisos o de análisis JSON), comparte los detalles para una solución más detallada.