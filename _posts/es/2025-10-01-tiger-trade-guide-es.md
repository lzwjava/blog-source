---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Guía de Compra y Venta de la Aplicación Tiger Trade
translated: true
type: note
---

### Cómo Mostrar Compra/Venta en la App Móvil Global de Tiger Trade

La app Tiger Trade (publicada por Tiger Brokers, también conocida como Tiger Trade: Invest Globally en Google Play o similar en tiendas de aplicaciones regionales) permite operar con acciones estadounidenses, opciones, ETFs, futuros y más. La versión más reciente a septiembre de 2025 es la 9.4.0.2, que introdujo mejoras en TigerAI para análisis y funciones para accionistas que muestran tendencias de compra/venta [1].

Para mostrar las opciones de compra/venta en la app (asumiendo que te refieres a las páginas de trading de acciones u opciones):

1.  **Abre la App y Navega a una Acción**:
    - Busca una acción (ej. AAPL) en la pestaña de inicio o de mercados.
    - Toca la acción para abrir su página de detalles, que incluye pestañas de gráfico, noticias y análisis.

2.  **Mostrar Botones de Compra/Venta para Acciones**:
    - En la página de la acción, desplázate hacia abajo o toca el ícono "Trade".
    - Aparecerán los botones de Compra y Venta, permitiéndote ingresar los detalles de la orden (ej. cantidad, tipo de orden como mercado o límite).
    - No existen superposiciones persistentes de compra/venta en el gráfico en la app móvil (a diferencia de la versión de escritorio, que tiene configuraciones de trading en el gráfico con botones [2] [2]).

3.  **Mostrar Compra/Venta para Opciones**:
    - En la página de la acción, toca la pestaña "Options" para ver la cadena de opciones.
    - Desplázate para seleccionar fechas de vencimiento. Cada opción muestra precios bid/ask con acciones de compra/venta implícitas al ser tocada (buy to open para calls/puts, o sell si tienes una posición larga [3] [4]).
    - Si no se muestra compra/venta en las opciones (ej. la lista aparece vacía después de hacer clic en algo), puede que hayas cambiado al filtro "My Positions", que solo muestra las opciones que posees. Cambia de nuevo a "All Options" en la parte superior de la cadena [4].

### Respecto a la Función "Weekly Invest"
No existe una función explícitamente llamada "Weekly Invest" o "AI Weekly Invest", pero esto probablemente se refiere a **Auto-Invest** (también llamado Tiger Invest), una herramienta de inversión regular para acciones y ETFs estadounidenses:
- Admite compras automatizadas (no ventas) en intervalos fijos, como semanales, comenzando desde $2 USD (o equivalente en HKD/otras monedas) usando acciones fraccionarias [5] [5].
- Acceso: Ve a Portfolio > Auto-Invest (o busca en los menús de la app).
- No afecta la visibilidad de compra/venta en las páginas de acciones—el trading sigue siendo independiente. Si los botones de compra/venta desaparecieron después de interactuar con Auto-Invest, reinicia la app o cierra y abre sesión, ya que puede ser un fallo de la interfaz de usuario en la versión 9.4.0.2.

Si los botones siguen ocultos después de la aventura (ej. después de hacer clic en un filtro, alternar el gráfico o una función de IA), verifica:
- Asegúrate de que tu cuenta esté fondeada y sea elegible para operar (Tiger admite acciones fraccionarias y opciones para usuarios elegibles [6]).
- Desactiva las superposiciones de TigerAI o cambia los marcos de tiempo del gráfico si interfieren visualmente.
- Para la configuración de la app: Toca Profile > Settings > busca opciones de visualización (no hay un interruptor específico de compra/venta en el móvil).

Para más ayuda, visita el centro de ayuda de Tiger Trade o contacta al soporte. Si esto es para Tiger Trade en escritorio Windows/Mac, los botones de trading en el gráfico se pueden habilitar mediante Options > Chart Settings > Trading [2].

Citas:
[1] https://apps.apple.com/nz/app/tiger-trade-buy-us-asx-shares/id1023600494
[2] https://support.tiger.com/english/windows/chart/chart-trading
[3] https://www.itiger.com/sg/help/detail/option-trading
[4] https://www.youtube.com/watch?v=5JKam5MP-nc
[5] https://www.itiger.com/nz/help/detail/15849694
[6] https://play.google.com/store/apps/details?id=com.tigerbrokers.stock&hl=en_US