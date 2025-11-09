---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Referencia de Declaraciones DOCTYPE de CodeIgniter
translated: true
type: note
---

### Resumen
Este es un array de PHP del framework CodeIgniter (un framework de aplicaciones web de código abierto), que define declaraciones DOCTYPE para varios lenguajes de marcado. Un DOCTYPE es una declaración de tipo de documento que informa a los navegadores y validadores sobre la versión y el estándar del lenguaje de marcado utilizado en un documento HTML. Garantiza una representación y validación adecuadas. Estas declaraciones se basan en los estándares oficiales del W3C. A continuación, explicaré cada una agrupándolas temáticamente, incluyendo su propósito y casos de uso típicos.

### Doctypes XHTML
XHTML (eXtensible HyperText Markup Language) es HTML reformulado como XML, que impone una sintaxis más estricta (por ejemplo, requiere etiquetas de cierre y elementos en minúsculas).
- **xhtml11**: Declara XHTML 1.1, la última versión de XHTML con características modulares para aplicaciones web avanzadas. Estricto, compatible con XML; utilizado para páginas web modernas y semánticas sin marcos o elementos heredados.
- **xhtml1-strict**: XHTML 1.0 Estricto; aplica un marcado limpio y semántico sin elementos obsoletos (por ejemplo, sin `<font>`). Ideal para sitios compatibles con estándares que necesitan compatibilidad con versiones anteriores.
- **xhtml1-trans**: XHTML 1.0 Transicional; permite algunos elementos HTML heredados para una migración más fácil desde HTML 3.2/4.0. Útil para sitios existentes que mezclan marcado antiguo y nuevo.
- **xhtml1-frame**: XHTML 1.0 Frameset; admite diseños con marcos usando `<frameset>`. Obsoleto en el diseño web moderno debido a problemas de usabilidad y desventajas para el SEO.
- **xhtml-basic11**: XHTML Basic 1.1; un perfil ligero para dispositivos móviles y aplicaciones simples, que excluye características avanzadas como formularios o hojas de estilo.

### Doctypes HTML
HTML es el marcado estándar para páginas web, que evoluciona desde estándares flexibles a estrictos.
- **html5**: El DOCTYPE moderno de HTML5; simple y preparado para el futuro, analizado en modo estándar por todos los navegadores. Admite multimedia, APIs y elementos semánticos (por ejemplo, `<article>`, `<header>`). Recomendado para nuevos sitios web.
- **html4-strict**: HTML 4.01 Estricto; aplica rigor semántico sin elementos obsoletos. Utilizado en proyectos heredados que requieren un cumplimiento estricto.
- **html4-trans**: HTML 4.01 Transicional; permisivo, permite etiquetas heredadas para actualizaciones graduales. Común en sitios antiguos en transición hacia estándares.
- **html4-frame**: HTML 4.01 Frameset; para páginas con marcos, ahora obsoleto debido a una carga lenta y problemas de accesibilidad.

### Doctypes MathML
MathML (Mathematical Markup Language) permite mostrar notaciones matemáticas en la web.
- **mathml1**: MathML 1.0; representación matemática básica en formato XML. Utilizado en herramientas educativas o documentos con ecuaciones simples.
- **mathml2**: MathML 2.0; soporte mejorado para matemáticas complejas, mejor integrado con otro marcado. Base para la visualización matemática web moderna.

### Doctypes SVG
SVG (Scalable Vector Graphics) define imágenes vectoriales en XML para gráficos web.
- **svg10**: SVG 1.0; gráficos vectoriales 2D básicos. Utilizado para ilustraciones estáticas.
- **svg11**: SVG 1.1; gráficos 2D completos con animaciones y filtros. Estándar para gráficos web dinámicos.
- **svg11-basic**: SVG 1.1 Basic; subconjunto centrado en dispositivos móviles con menos características. Para SVG ligero en dispositivos.
- **svg11-tiny**: SVG 1.1 Tiny; perfil mínimo para dispositivos de baja potencia como teléfonos. Admite formas básicas y animaciones.

### Doctypes Compuestos
Estos combinan múltiples estándares para contenido multimedia enriquecido.
- **xhtml-math-svg-xh**: XHTML 1.1 con MathML 2.0 y SVG 1.1; para documentos que mezclan texto, matemáticas y gráficos (por ejemplo, artículos científicos).
- **xhtml-math-svg-sh**: Similar al anterior pero basado en SVG (`<svg:svg>`), para documentos dominados por SVG con XHTML y MathML incrustados.
- **xhtml-rdfa-1**: XHTML con RDFa 1.0 (Resource Description Framework in attributes); mejora la incrustación de datos de la web semántica para sitios ricos en metadatos.
- **xhtml-rdfa-2**: XHTML con RDFa 1.1; RDFa mejorado para vincular datos en atributos HTML, utilizado en aplicaciones de la web de datos.

### Notas de Uso
- Estos están predefinidos en CodeIgniter para una fácil inserción a través de su función auxiliar `doctype()`.
- El desarrollo web moderno favorece HTML5 (`html5`) por su flexibilidad y soporte del navegador. Los doctypes más antiguos (por ejemplo, HTML 4 o versiones con marcos) están en gran parte obsoletos.
- Evidenciado por las especificaciones del W3C (por ejemplo, w3.org/TR/html5/, w3.org/TR/xhtml11/), estos aseguran un análisis consistente: los navegadores los usan para activar el modo estándar o quirks, afectando el diseño y los scripts. Elija según las necesidades de marcado de su proyecto para la mejor validación (a través de herramientas como el Validador del W3C). Si está trabajando en CodeIgniter, use la clave del array en sus vistas para generar la declaración.