---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Corrección de Autenticación de Safari Localhost
translated: true
type: note
---

Este problema surge porque Safari en macOS aplica políticas de seguridad más estrictas que Chrome para las URLs de localhost. Específicamente, Safari requiere un contexto HTTPS seguro para permitir cookies persistentes y sesiones de autenticación, evitando posibles bucles de cierre de sesión o reautenticación en cada visita para aplicaciones como LibreChat que se ejecutan sobre HTTP. Chrome es más permisivo con HTTP en localhost, por lo que la autenticación persiste allí pero no en Safari.[1][2][3]

### Factores Gubernamentales
- **Políticas del Navegador**: Navegadores modernos como Safari exigen HTTPS para localhost para evitar advertencias de contenido mixto e inseguridades en las sesiones.
- **Comportamiento de LibreChat**: LibreChat utiliza cookies seguras o tokens basados en localStorage para la autenticación, que se rompen en HTTP en Safari debido a su manejo más estricto de orígenes no seguros.

### Soluciones (Clasificadas por Facilidad y Efectividad)
1. **Configurar HTTPS para Localhost (Recomendado)**:
   - La documentación y el blog de LibreChat recomiendan esto para prevenir cierres de sesión inducidos por HTTP.[1]
   - Usa `mkcert` (una herramienta gratuita) para generar y confiar en certificados SSL locales para localhost:
     - Instala `mkcert` via `brew install mkcert` o descárgalo desde GitHub.
     - Ejecuta `mkcert -install` para instalar la CA raíz.
     - Crea los certificados: `mkcert localhost 127.0.0.1`.
     - Configura LibreChat (ej., via variables de entorno de Docker o config) para usar estos certificados: Añade `HTTPS=true`, `SSL_CRT_FILE=/ruta/a/localhost.pem`, y `SSL_KEY_FILE=/ruta/a/localhost-key.pem` en tu archivo `.env` o entorno.
     - Reinicia LibreChat y accede via `https://localhost:3080`.
     - Safari ahora lo tratará como seguro, permitiendo inicios de sesión sin problemas.

2. **Alternativa: Usar 127.0.0.1 En Lugar de localhost**:
   - Safari a veces se comporta de manera diferente con `localhost` (debido a resolución IPv6 o DNS). Intenta acceder a `http://127.0.0.1:3080` – esto ha resuelto problemas de conexión similares en algunos casos, aunque puede no solucionar completamente la persistencia de la autenticación.[4][4][5]

3. **Borrar los Datos del Sitio Web de Safari para localhost**:
   - Ve a Safari > Preferencias > Privacidad > Administrar Datos del Sitio Web > Busca "localhost" > Elimina cualquier entrada.
   - Esto obliga a Safari a dejar de aplicar actualizaciones HTTPS o contextos inseguros en caché.[3][2]
   - Reinicia Safari y prueba; si LibreChat lo soporta, la autenticación debería mantenerse.

Si nada de esto funciona, revisa los registros de LibreChat en busca de errores de autenticación, asegúrate de que tu `.env` no tenga banderas conflictivas (ej., `ALLOW_ANONYMOUS=true` desactiva la autenticación por completo si se desea) y confirma que no estés en el modo de navegación privada de Safari, que bloquea el almacenamiento persistente.[6][7] Si el problema persiste, proporciona tu versión de LibreChat y la configuración de .env para una solución de problemas más profunda.

Citas:
[1] https://www.librechat.ai/blog/2024-05-16_unsecured_http
[2] https://github.com/danny-avila/LibreChat/discussions/529
[3] https://stackoverflow.com/questions/46394682/safari-keeps-forcing-https-on-localhost
[4] https://superuser.com/questions/30827/safari-is-unable-to-reach-localhost-127-0-0-1
[5] https://apple.stackexchange.com/questions/422556/localhost-has-stopped-working-on-chrome-and-safari-since-upgrading-to-big-sur
[6] https://www.librechat.ai/docs/configuration/authentication
[7] https://discussions.apple.com/thread/255906354