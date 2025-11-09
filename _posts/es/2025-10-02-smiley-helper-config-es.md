---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Configuración del Asistente de Emoticonos de CodeIgniter
translated: true
type: note
---

### Resumen
Este es un archivo de configuración de PHP del framework web CodeIgniter, específicamente para su **helper de emoticones/smileys**. CodeIgniter es un framework MVC de PHP para construir aplicaciones web. Este archivo define un conjunto de mapeos de smileys/emoticonos utilizados por el `smiley_helper` del framework para reemplazar automáticamente emoticonos basados en texto (como `:-)`) con etiquetas HTML `<img>` que muestran las imágenes GIF correspondientes.

El archivo asegura que el acceso directo sea bloqueado mediante `defined('BASEPATH') OR exit('No direct script access allowed');`, una medida de seguridad en CodeIgniter para prevenir la ejecución directa no autorizada de scripts.

### Componentes Clave
- **Propósito**: Convierte emoticonos de texto plano en contenido generado por el usuario (ej., publicaciones en foros o comentarios) en imágenes visuales para una mejor experiencia de usuario.
- **Estructura de Datos**: `$smileys` es un array asociativo de PHP con la estructura formal:
  ```
  $smileys = array(
      'smiley_code' => array('image_file', 'width', 'height', 'alt_text'),
      // ...
  );
  ```
  - **smiley_code**: El patrón de texto a coincidir (ej., `:-)`, `:lol:`, `>:(`).
  - **image_file**: Nombre de la imagen GIF en el directorio de smileys (por defecto en `application/views/smileys/` en CodeIgniter).
  - **width/height**: Dimensiones en píxeles para la etiqueta `<img>` (todas son `'19'` aquí, indicando GIFs de 19x19px).
  - **alt_text**: Texto alternativo para accesibilidad/lectores de pantalla, que describe la emoción.

- **Uso en CodeIgniter**: Carga el helper con `$this->load->helper('smiley');`, luego llama a funciones como `parse_smileys($text)` en cadenas que contengan códigos de emoticonos. Esto reemplaza los códigos con etiquetas `<img>`, ej.:
  - Entrada: `I'm happy :)`  
    Salida: `I'm happy <img src="http://example.com/smileys/smile.gif" width="19" height="19" alt="smile">`

### Desglose de las Entradas
El array incluye 40+ mapeos agrupados por tipo de emoción. La mayoría de las imágenes son GIFs de 19x19px. Aquí hay una vista resumida (con ejemplos):

| Código(s) de Smiley | Imagen | Texto Alt | Notas |
|---------------|-------|----------|-------|
| `:-)`, `:)` | grin.gif, smile.gif | grin, smile | Sonrisas y risas positivas. |
| `:lol:`, `:cheese:` | lol.gif, cheese.gif | LOL, cheese | Riendo a carcajadas/pulgar arriba, sonrisa exagerada. |
| `;-)`, `;)` | wink.gif | wink | Guiño. |
| `:smirk:`, `:roll:` | smirk.gif, rolleyes.gif | smirk, rolleyes | Sarcasmo/asentimiento sabio. |
| `:-S`, `:wow:`, `:bug:` | confused.gif, surprise.gif, bigsurprise.gif | confused, surprised, big surprise | Confusión/sorpresa. |
| `:-P`, `%-P`, `;-P`, `:P` | tongue_laugh.gif, etc. | tongue laugh, etc. | Variantes con la lengua fuera (riendo, guiñando, pedorreta). |
| `:blank:`, `:long:`, `:ohh:`, `:grrr:`, `:gulp:`, `8-/` | Varios | blank stare, long face, ohh, grrr, gulp, oh oh | Expresiones neutrales o molestas. |
| `:down:`, `:red:`, `:sick:`, `:shut:` | Varios | downer, red face, sick, shut eye | Triste, avergonzado, enfermo. |
| `:-/`, `>:(` (`:mad:`), `>:-(` (`:angry:`) | hmm.gif, mad.gif, angry.gif | hmmm, mad, angry | Confundido, enfadado, furioso. |
| `:zip:`, `:kiss:` | zip.gif, kiss.gif | zipper, kiss | Silencio (cremallera), beso. |
| `:ahhh:`, `:coolsmile:`, `-:coolsmirk:`, `:coolgrin:`, `:coolhmm:`, `:coolmad:`, `:coolcheese:` | shock.gif, shade_smile.gif, etc. | shock, cool smile, cool smirk, cool grin, cool hmm, cool mad, cool cheese | Variantes de sorprendido o "cool"/con gafas de sol. |
| `:vampire:`, `:snake:` | vampire.gif, snake.gif | vampire, snake | Emoticonos temáticos. |
| `:exclaim:`, `:question:` | exclaim.gif, question.gif | exclaim, question | Equivalentes de puntuación (!, ?). |

### Extensión y Personalización
- **Añadir Smileys**: Añade nuevas entradas, ej., `':fire:' => array('fire.gif', '19', '19', 'fire');`.
- **Cambiar Imágenes**: Actualiza los nombres de archivo si reemplazas GIFs con PNGs/JPGs (ajusta el width/height en consecuencia).
- **Directorio**: Asegúrate de que las imágenes existen en la ruta de smileys de CodeIgniter.
- **Limitaciones**: Todas las imágenes aquí son del mismo tamaño; las implementaciones reales podrían variar. Este array solo define los mapeos—la lógica de reemplazo está en el helper mismo.

Si tienes una pregunta específica sobre personalizar o usar esto en CodeIgniter, ¡proporciona más detalles!