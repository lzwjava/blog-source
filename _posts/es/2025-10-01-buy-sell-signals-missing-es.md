---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Señales de Compra y Venta Ausentes en los Gráficos Anuales
translated: true
type: note
---

### Problema con las señales de compra/venta en el gráfico de velas de la aplicación móvil Tiger Trade Global

Parece que estás experimentando un problema de visualización donde las señales de compra/venta (por ejemplo, indicadores técnicos para señales de trading como cruces del RSI o señales del MACD, o quizás marcadores del feed de operaciones para volúmenes/ejecuciones de compra/venta) aparecen en los gráficos de velas semanales o mensuales, pero desaparecen en la vista anual. En la aplicación Tiger Trade (versión 9.4.0.2 a septiembre de 2025), este comportamiento puede deberse a limitaciones de diseño de la aplicación: los períodos más largos como el anual tienen menos puntos de datos (ej. agregados en velas mensuales), lo que puede hacer que los indicadores no se calculen correctamente, aparezcan desordenados o se oculten por completo para evitar imprecisiones.

### Por qué sucede:
- **Granularidad de los datos**: En los gráficos anuales, las velas representan meses o años, por lo que los indicadores técnicos (ej. el RSI que requiere ~14 puntos de datos) pueden no activar señales debido a barras insuficientes. Los períodos más cortos (semanal/mensual) tienen más barras, lo que permite señales claras.
- **Configuración de la aplicación**: En las versiones móviles, las señales de compra/venta del "feed de operaciones" (tics de volumen de compra/venta en tiempo real o indicadores) están habilitadas para períodos más cortos en los gráficos de cotizaciones/páginas para evitar sobrecarga. Actualizaciones como la 9.2.4 añadieron señales del feed de operaciones, pero pueden aplicarse por defecto solo en vistas intradía/semana/mes [1].
- **Rendimiento/Razones de UI**: Mostrar señales densas en vistas anuales podría ralentizar la aplicación o confundir a los usuarios, por lo que se ocultan condicionalmente.

### Cómo resolverlo o solucionarlo:
1.  **Cambiar el marco temporal como ya has hecho**: Para obtener señales de compra/venta confiables, mantente en las vistas semanal o mensual en el gráfico de velas. En la pestaña del gráfico en la página de la acción, toca el selector de marco temporal (ej. "Semana" o "M" para mes) para alternar; las señales deberían reaparecer.

2.  **Verificar la configuración de los indicadores**:
    - Abre la página de la acción > Pestaña Gráfico/Velas.
    - Toca el icono de edición/configuración (⚙️ o llave inglesa) en el gráfico.
    - Asegúrate de que tus indicadores (ej. RSI, MACD) estén habilitados. Si las señales aún se ocultan en la vista anual, la aplicación podría restringirlas; intenta volver a añadirlos o borra la caché en Perfil > Configuración > Borrar caché.

3.  **Habilitar las señales del Feed de Operaciones (si aplica)**:
    - En la última versión 9.4.0.2, el feed de operaciones (indicadores de volumen de compra/venta superpuestos en las velas) puede no mostrarse en la vista anual. Ve a Perfil > Configuración > Configuración de Cotizaciones o Gráficos para activar/desactivar "Mostrar Feed de Operaciones" si está disponible (las actualizaciones más recientes enfatizan esto en los gráficos de marcos temporales [1]).
    - Si se trata de marcadores de operaciones ejecutadas (puntos/líneas en el gráfico), la aplicación móvil generalmente no los muestra en los gráficos; revisa la pestaña "Posiciones" u "Órdenes" para ver las compras/ventas ejecutadas.

4.  **Actualización de la aplicación y consejos**:
    - Asegúrate de tener la versión 9.4.0.2 (verifica en Perfil > Acerca de en la aplicación). Las versiones antiguas pueden tener errores; actualiza a través de la tienda de aplicaciones.
    - Si las señales desaparecen persistentemente, reinicia la aplicación o cierra y abre sesión. Para Tiger Trade en desktop, puedes habilitar la visualización completa de marcadores mediante la Configuración del Gráfico, pero la versión móvil carece de esta opción [2] [3].
    - Para indicadores personalizados como flechas de compra/venta, visita support.tiger.com para ver las preguntas frecuentes móviles; las aplicaciones no admiten indicadores escritos por el usuario en dispositivos móviles.

Si esto persiste o necesitas señales específicamente en gráficos anuales, contacta al soporte de Tiger Brokers a través de la aplicación (Perfil > Ayuda) o los foros, ya que podría ser un error en la versión móvil global. Para guías detalladas sobre indicadores, mira el video "Adding Indicators to the K Chart" en YouTube [4].

Citas:
[1] https://www.itiger.com/about/app/update
[2] https://support.tiger.com/english/frequently-asked-questions/questions-about-indicators
[3] https://support.tiger.com/english/windows/chart/chart-settings
[4] https://www.youtube.com/watch?v=5xgmRavEkFE