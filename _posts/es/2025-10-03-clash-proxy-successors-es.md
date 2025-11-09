---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Sucesores de Clash Proxy y Soporte para Linux
translated: true
type: note
---

Clash, una herramienta de proxy basada en reglas similar a Shadowsocks, tuvo su repositorio original eliminado por el autor en 2023 debido a presiones regulatorias en China. La comunidad ha continuado el desarrollo a través de forks y sucesores como Clash.Meta (ahora llamado oficialmente Mihomo), que es ampliamente considerado el reemplazo más confiable y mantenido activamente. Es compatible con binarios para Linux, incluido Ubuntu, e incluye funciones como DNS sobre HTTPS (DoH), tunneling y enrutamiento basado en reglas.

Para un repositorio de GitHub confiable para Linux/Ubuntu, recomiendo el proyecto de continuación principal. Aquí hay un resumen de las mejores opciones basadas en la adopción por la comunidad, las actualizaciones y el soporte para Linux:

### Repositorios Recomendados
- **MetaCubeX/mihomo (Clash.Meta Core)**: Este es el sucesor principal de Clash, bifurcado y mantenido por la comunidad después de la eliminación original. Ofrece funcionalidad completa de proxy, actualizaciones frecuentes y binarios precompilados para Linux (x86_64 y arm64). La compatibilidad con Ubuntu es excelente, con binarios probados en versiones 18.04+. Es de código abierto, sin publicidad y altamente personalizable a través de archivos de configuración YAML.  
  - GitHub: https://github.com/MetaCubeX/mihomo  
  - Por qué es confiable: Más de 14k estrellas, comunidad activa y los binarios incluyen bases de datos GeoIP para el enrutamiento. Enlaces de descarga directa para binarios CLI de Linux en la sección de releases.  
  - Instalación para Ubuntu: Descarga el último binario "mihomo-linux-amd64" de los releases, hazlo ejecutable (`chmod +x mihomo`) y ejecútalo. Requiere un archivo config.yaml con reglas de proxy. [1][2]  
  - Alternativas si el core no se adapta a tus necesidades: 
    - **CarlDegio/verge**: Un wrapper GUI basado en Tauri para Clash.Meta, que proporciona un panel intuitivo para Linux (incluido Ubuntu). Se basa en Mihomo internamente para mayor estabilidad.  
      - GitHub: https://github.com/CarlDegio/verge  
      - Por qué es confiable: Soporte GUI para escritorio, más de 2k estrellas, cambio fácil de perfiles e icono en la bandeja del sistema. Descarga AppImage para Ubuntu. [3]  
    - **chen08209/FlClash**: Cliente multiplataforma (incluyendo binarios para Linux) basado en Clash.Meta. Se centra en la simplicidad y un diseño sin publicidad, con una interfaz sencilla para la configuración.  
      - GitHub: https://github.com/chen08209/FlClash  
      - Por qué es confiable: Ligero, compatible con Ubuntu a través de builds deb/AppImage e integra bindings de Mihomo. [4]  
  - Para copias de seguridad heredadas: Kuingsmile/clash-core ofrece builds archivados del core previo a la eliminación, con releases para descargas en Linux si prefieres una versión histórica no mantenida. [5]  

### Notas Adicionales
- **Consejos de Instalación**: Asegúrate de tener libc (glibc 2.17+) para Ubuntu. Usa herramientas como `systemd` o `screen` para ejecutarlo como un servicio en segundo plano. Verifica las descargas con los hashes SHA256 para mayor seguridad.
- **Criterios de Confiabilidad**: Estos repositorios tienen contribuciones activas, grandes bases de usuarios (muchas estrellas/forks) y evitan los riesgos de proyectos abandonados posteriores a 2023. Clash.Premin (probablemente un error tipográfico de Premium) es un fork de pago pero no está tan centrado en el código abierto.
- **Recordatorio Legal/de Uso**: Clash es para eludir la censura; asegúrate de cumplir con las leyes locales, ya que su uso puede atraer atención en regiones restringidas.
- Si necesitas una interfaz de usuario o características específicas (por ejemplo, multiplataforma), verge o FlClash son más fáciles de usar que el CLI core de Mihomo. Para más detalles, consulta el README de cada repositorio. Si surgen problemas, el repositorio de Mihomo tiene documentación extensa. [6][7][1][8]  

¡Si ninguno se adapta o necesitas una guía paso a paso para Ubuntu, proporciona más detalles!

Citas:
[1] https://github.com/djoeni/Clash.Meta
[2] https://discussion.fedoraproject.org/t/rhbz-2305079-review-request-clash-meta-a-rule-based-network-proxy-tool-aka-mihomo/146312
[3] https://github.com/CarlDegio/verge
[4] https://github.com/chen08209/FlClash
[5] https://github.com/Kuingsmile/clash-core/releases
[6] https://github.com/fengwz17/Clash-For-Ubuntu
[7] https://news.ycombinator.com/item?id=38126160
[8] https://github.com/hiddify/Clash.Meta