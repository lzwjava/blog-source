---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Matrices de Configuración del Agente de Usuario de CodeIgniter
translated: true
type: note
---

### Resumen
Este fragmento de código PHP es parte del framework CodeIgniter (un framework web para PHP), específicamente del archivo de configuración de la Clase User Agent. Define cuatro arrays (`$platforms`, `$browsers`, `$mobiles` y `$robots`) que mapean fragmentos de cadenas de agente de usuario a nombres legibles para humanos de navegadores, sistemas operativos, dispositivos móviles y rastreadores web/bots. El código se utiliza para analizar e identificar el tipo de dispositivo, navegador o bot que visita un sitio web basándose en la cabecera HTTP User-Agent enviada por los clientes.

Los arrays son asociativos (pares clave-valor), donde las claves son cadenas parciales de las cadenas de agente de usuario (coincidencias insensibles a mayúsculas y minúsculas), y los valores son los nombres de visualización correspondientes. La librería User Agent de CodeIgniter los utiliza para la detección, como determinar si un visitante está en Android, usa Chrome o es un bot de búsqueda.

### Array $platforms
Este array identifica sistemas operativos o plataformas. Las claves son subcadenas que pueden aparecer en la cabecera User-Agent, y los valores son nombres limpios para su visualización.

- **Ejemplos de entradas**:
  - `'windows nt 10.0'` → `'Windows 10'`
  - `'android'` → `'Android'`
  - `'os x'` → `'Mac OS X'`
- **Propósito**: Ayuda a detectar el sistema operativo del cliente (por ejemplo, Windows, iOS, Linux) para análisis, personalización de contenido o ajustes de características.
- **Nota**: El orden es importante para la precisión, ya que algunas subcadenas pueden superponerse (por ejemplo, `'windows'` es un comodín al final).

### Array $browsers
Identifica navegadores web. Los navegadores a menudo reportan múltiples identificadores, por lo que el orden prioriza primero los subtipos (según el comentario).

- **Ejemplos de entradas**:
  - `'Chrome'` → `'Chrome'`
  - `'MSIE'` → `'Internet Explorer'`
  - `'Firefox'` → `'Firefox'`
  - Caso especial: `'Opera.*?Version'` (coincidencia tipo regex) para Opera moderno que se reporta como "Opera/9.80" con una versión.
- **Propósito**: Determina el navegador (por ejemplo, Chrome, Safari) para ofrecer características específicas del navegador o redireccionamientos.
- **Nota sobre Regex**: Algunas claves utilizan patrones regex básicos (por ejemplo, `.*?` para coincidencias comodín), manejados en la librería.

### Array $mobiles
Mapea indicadores de agente de usuario para dispositivos móviles, teléfonos y dispositivos/navegadores relacionados. Es más grande e incluye teléfonos, tablets, consolas de juegos y categorías de respaldo.

- **Secciones estructuradas**:
  - Teléfonos/Fabricantes: `'iphone'` → `'Apple iPhone'`, `'samsung'` → `'Samsung'`.
  - Sistemas Operativos: `'android'` → `'Android'`, `'symbian'` → `'Symbian'`.
  - Navegadores: `'opera mini'` → `'Opera Mini'`, `'fennec'` → `'Firefox Mobile'`.
  - Otros/Respaldo: `'mobile'` → `'Generic Mobile'` para indicadores móviles no coincidentes.
- **Propósito**: Identifica dispositivos móviles para diseño responsivo, funciones exclusivas para móviles o redireccionamientos a aplicaciones. Incluye entradas heredadas (algunas comentadas como obsoletas).

### Array $robots
Enumera rastreadores web y bots comunes. Las claves son subcadenas de los agentes de usuario de los bots.

- **Ejemplos de entradas**:
  - `'googlebot'` → `'Googlebot'`
  - `'bingbot'` → `'Bing'`
  - `'yandex'` → `'YandexBot'`
- **Propósito**: Identifica rastreadores para el manejo de SEO, como servir contenido diferente a los bots (por ejemplo, sin anuncios) o registrar el tráfico de bots.

### Uso en CodeIgniter
- La Clase User Agent carga este archivo y utiliza métodos como `is_browser()`, `is_mobile()`, `is_robot()` y `platform()` para analizar la cadena User-Agent.
- Realiza búsquedas insensibles a mayúsculas y minúsculas a través de estos arrays para hacer coincidir las claves con la cadena.
- Para discrepancias (por ejemplo, dispositivos/navegadores nuevos no listados), se deben actualizar estos arrays manualmente o mediante extensiones de la comunidad.

### Notas Adicionales
- **Seguridad**: Esto es puramente para la recolección de datos; no ejecuta código dañino. Las cadenas User-Agent pueden ser falsificadas, así que no confíe en esto para comprobaciones de seguridad críticas.
- **Actualizaciones**: Las versiones de CodeIgniter pueden haber añadido/modificado entradas; esto parece una instantánea antigua (por ejemplo, Edge como 'Spartan' está obsoleto).
- **Cómo probar**: En un script PHP, podría cargar esto y usar `strpos` o regex para coincidir con una cadena User-Agent de ejemplo.

Si proporciona una parte específica o tiene una pregunta sobre la implementación, ¡hágamelo saber!