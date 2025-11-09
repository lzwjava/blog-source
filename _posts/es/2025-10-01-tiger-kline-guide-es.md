---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Guía de Indicadores K-Line para la App Tiger Trade
translated: true
type: note
---

En la aplicación móvil Tiger Trade Global (versión más reciente 9.4.0.2 a septiembre de 2025), el gráfico de K-line (velas japonesas) en las páginas de acciones muestra los datos de precios, pero no tiene marcadores de operaciones integrados ni indicadores de compra/venta para órdenes ejecutadas (a diferencia de la versión de escritorio, donde puedes activar la visualización de órdenes mediante Configuración del Gráfico > Trading). Sin embargo, puedes añadir indicadores técnicos personalizables al gráfico de K-line que analizan las tendencias de precios y generan señales de compra/venta, como medias móviles, RSI (Índice de Fuerza Relativa), MACD o Bandas de Bollinger. Estos pueden representar visualmente señales alcistas/bajistas en el gráfico (por ejemplo, cruces que indican puntos de compra/venta).

Si las señales de compra/venta desaparecieron después de clics accidentales (por ejemplo, desactivando indicadores), puede que necesites volver a activarlos o añadirlos de nuevo.

### Pasos para Mostrar/Añadir Indicadores de Compra/Venta en el Gráfico de K-Line:
1. **Abre la App y Selecciona una Acción**:
   - Busca una acción (por ejemplo, AAPL) y tócala para abrir la página de detalles.

2. **Accede al Gráfico**:
   - El gráfico de K-line está en la pestaña "Chart" o "K-Line" (vista por defecto en la página de la acción).
   - Toca el área del gráfico para que aparezca la barra de herramientas o el menú (normalmente en la parte superior o inferior).

3. **Añade Indicadores**:
   - Busca un icono con forma de llave inglesa, engranaje o "Editar" (⚙️) en el gráfico.
   - Tócalo para abrir la configuración. En la lista de indicadores, selecciona entre herramientas comunes de señales de compra/venta como:
     - **Medias Móviles (MA)**: Simple/EMA – Compra cuando la MA rápida cruza por encima de la MA lenta; venta en caídas.
     - **RSI**: Oscila entre 0-100; compra por debajo de 30 (sobreventa), venta por encima de 70 (sobrecompra).
     - **MACD**: Compra cuando las barras del histograma se vuelven positivas; venta cuando son negativas.
     - **Bandas de Bollinger**: Compra cuando el precio toca la banda inferior; venta en la banda superior.
   - Activa 1-3 indicadores a la vez para mayor claridad. Las señales aparecen como líneas, flechas o superposiciones en las velas.
   - Confirma y aplica los cambios para mostrarlos.

4. **Personaliza o Desactiva**:
   - Para eliminar/reactivar, vuelve a la configuración de indicadores y deselecciona o vuelve a seleccionar.
   - La última actualización 9.4.0.2 incluye suplementos de indicadores para K-line para una mejor visualización de señales [1][2][3].

Si esto no coincide con tu experiencia (por ejemplo, no hay icono de edición o los indicadores no funcionan), asegúrate de que la aplicación esté actualizada, ya que versiones anteriores pueden carecer de algunas funciones. Para más información sobre cómo leer K-lines y usar indicadores para el momento de compra/venta, consulta los tutoriales de Tiger Academy (por ejemplo, "10. Use technical indicators to determine the best buy and sell prices") [3][2]. Si estás usando la aplicación de escritorio Tiger Trade en su lugar, la configuración del gráfico permite activar los marcadores de órdenes (anclas con líneas para niveles de compra/venta) en Opciones > Configuración del Gráfico > Trading > Mostrar Órdenes [4].

Para ejemplos visuales, busca "Adding Indicators to the K Chart" en YouTube o los foros de Tiger Brokers. Si el problema persiste, contacta al soporte de la aplicación mediante Perfil > Ayuda.

Citas:
[1] https://www.youtube.com/watch?v=5xgmRavEkFE
[2] https://www.itiger.com/about/app/update
[3] https://www.itiger.com/sg/learn/detail/lnfogp3rckf7pksfpbd
[4] https://support.tiger.com/english/windows/chart/chart-settings