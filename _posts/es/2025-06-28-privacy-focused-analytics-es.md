---
audio: false
generated: true
lang: es
layout: post
title: Guía de Análisis Web Centrado en la Privacidad
translated: true
type: note
---

Cloudflare Web Analytics es una herramienta gratuita centrada en la privacidad, diseñada para ayudar a los propietarios de sitios web a rastrear y comprender el rendimiento del sitio y el comportamiento de los visitantes sin comprometer la privacidad del usuario. A continuación, se presenta una guía completa para configurar y usar Cloudflare Web Analytics, basada en la información más reciente disponible.

### Descripción general de Cloudflare Web Analytics
Cloudflare Web Analytics proporciona información sobre el tráfico del sitio web, las vistas de página y las métricas de rendimiento, priorizando la privacidad del usuario. A diferencia de las herramientas de análisis tradicionales que pueden rastrear datos personales o usar cookies, la solución de Cloudflare evita métodos de rastreo invasivos como la creación de huellas digitales (fingerprinting), las cookies o el almacenamiento local con fines analíticos. Es adecuada para sitios web de todos los tamaños y puede usarse con o sin los servicios proxy de Cloudflare.[](https://www.cloudflare.com/web-analytics/)[](https://www.cloudflare.com/en-in/web-analytics/)[](https://blog.cloudflare.com/privacy-first-web-analytics/)

### Características principales
- **Privacidad Primero**: No recopila datos personales, no usa cookies ni rastrea a los usuarios mediante direcciones IP o agentes de usuario, garantizando el cumplimiento de normativas de privacidad como el GDPR.[](https://www.cloudflare.com/en-in/web-analytics/)[](https://blog.cloudflare.com/privacy-first-web-analytics/)
- **Dos Métodos de Recolección de Datos**:
  - **Baliza JavaScript (JavaScript Beacon)**: Un fragmento de código JavaScript ligero que recopila métricas del lado del cliente utilizando la API de Rendimiento del navegador. Ideal para datos detallados de Real User Monitoring (RUM), como los tiempos de carga de página y las Core Web Vitals.[](https://www.cloudflare.com/web-analytics/)[](https://developers.cloudflare.com/web-analytics/about/)
  - **Analíticas desde el Edge (Edge Analytics)**: Recopila datos del lado del servidor desde los servidores perimetrales (edge) de Cloudflare para sitios proxyados a través de Cloudflare. No se requieren cambios en el código y captura todas las solicitudes, incluidas las de bots o usuarios con JavaScript deshabilitado.[](https://www.cloudflare.com/web-analytics/)[](https://developers.cloudflare.com/web-analytics/faq/)
- **Métricas Proporcionadas**: Rastrea vistas de página, visitas, páginas principales, referentes, países, tipos de dispositivos, códigos de estado y métricas de rendimiento como los tiempos de carga de página.[](https://www.cloudflare.com/en-in/web-analytics/)[](https://blog.cloudflare.com/privacy-first-web-analytics/)[](https://usefathom.com/features/vs-cloudflare-web-analytics)
- **Tasa de Bits Adaptable (Adaptive Bit Rate - ABR)**: Ajusta automáticamente la resolución de los datos según el tamaño de los datos, el rango de fechas y las condiciones de la red para un rendimiento óptimo.[](https://developers.cloudflare.com/web-analytics/about/)
- **Gratuito**: Disponible para cualquier persona con una cuenta de Cloudflare, incluso sin cambiar el DNS o usar el proxy de Cloudflare.[](https://www.cloudflare.com/en-in/web-analytics/)[](https://blog.cloudflare.com/privacy-first-web-analytics/)
- **Panel de Control y Filtros**: Ofrece un panel de control intuitivo para ver y filtrar datos por nombre de host, URL, país y rango de tiempo. Puede hacer zoom en períodos específicos o agrupar datos para un análisis más profundo.[](https://www.cloudflare.com/web-analytics/)[](https://www.cloudflare.com/en-in/web-analytics/)
- **Soporte para Single Page Application (SPA)**: Rastrea automáticamente los cambios de ruta en las SPA al anular la función `pushState` de la History API (los enrutadores basados en hash no son compatibles).[](https://scripts.nuxt.com/scripts/analytics/cloudflare-web-analytics)

### Limitaciones
- **Retención de Datos**: Limitada a 30 días de datos históricos, lo que puede no ser adecuado para usuarios que necesitan análisis a largo plazo.[](https://plausible.io/vs-cloudflare-web-analytics)
- **Muestreo de Datos (Data Sampling)**: Las métricas se basan en una muestra del 10% de los eventos de carga de página, lo que puede conducir a imprecisiones en comparación con herramientas como Plausible o Fathom Analytics.[](https://plausible.io/vs-cloudflare-web-analytics)
- **Preocupaciones sobre Precisión**: Las analíticas del lado del servidor (edge analytics) pueden incluir tráfico de bots, inflando los números en comparación con las analíticas del lado del cliente como Google Analytics. Las analíticas del lado del cliente pueden perder datos de usuarios con JavaScript deshabilitado o bloqueadores de anuncios.[](https://developers.cloudflare.com/analytics/faq/about-analytics/)[](https://plausible.io/vs-cloudflare-web-analytics)[](https://markosaric.com/cloudflare-analytics-review/)
- **Sin Soporte para Parámetros UTM**: Actualmente, las cadenas de consulta como los parámetros UTM no se registran para evitar la recopilación de datos sensibles.[](https://developers.cloudflare.com/web-analytics/faq/)
- **Limitaciones de Exportación**: No hay una forma directa de exportar datos (por ejemplo, a CSV), a diferencia de algunos competidores como Fathom Analytics.[](https://usefathom.com/features/vs-cloudflare-web-analytics)
- **Analíticas Básicas**: Carece de funciones avanzadas como el seguimiento de conversiones o el análisis detallado del recorrido del usuario en comparación con Google Analytics.[](https://www.reddit.com/r/webdev/comments/ka8gxv/cloudflares_privacyfirst_web_analytics_is_now/)

### Configuración de Cloudflare Web Analytics
#### Prerrequisitos
- Una cuenta de Cloudflare (gratuita para crear en cloudflare.com).
- Acceso al código de su sitio web (para la baliza JavaScript) o a la configuración DNS (para edge analytics si usa el proxy de Cloudflare).

#### Pasos de Configuración
1. **Iniciar sesión en el Panel de Control de Cloudflare**:
   - Vaya a [cloudflare.com](https://www.cloudflare.com) e inicie sesión o cree una cuenta.
   - Desde la Página Principal de la Cuenta, navegue a **Analytics & Logs** > **Web Analytics**.[](https://developers.cloudflare.com/web-analytics/get-started/)

2. **Agregar un Sitio**:
   - Haga clic en **Add a site** en la sección Web Analytics.
   - Ingrese el nombre de host de su sitio web (por ejemplo, `example.com`) y seleccione **Done**.[](https://developers.cloudflare.com/web-analytics/get-started/)

3. **Elegir el Método de Recolección de Datos**:
   - **Baliza JavaScript (Recomendado para Sitios No Proxyados)**:
     - Copie el fragmento de código JavaScript proporcionado en la sección **Manage site**.
     - Péguelo en el HTML de su sitio web antes de la etiqueta de cierre `</body>`. Asegúrese de que su sitio tenga un HTML válido para que el fragmento funcione.[](https://developers.cloudflare.com/web-analytics/get-started/)[](https://developers.cloudflare.com/web-analytics/faq/)
     - Para Single Page Applications, asegúrese de que `spa: true` esté en la configuración para el seguimiento automático de rutas (los enrutadores basados en hash no son compatibles).[](https://scripts.nuxt.com/scripts/analytics/cloudflare-web-analytics)
     - Ejemplo para aplicaciones Nuxt: Use el composable `useScriptCloudflareWebAnalytics` o agregue el token a su configuración de Nuxt para la carga global.[](https://scripts.nuxt.com/scripts/analytics/cloudflare-web-analytics)
   - **Analíticas desde el Edge (Para Sitios Proxyados)**:
     - Proxyee su sitio web a través de Cloudflare actualizando su configuración DNS para que apunte a los nameservers de Cloudflare. Esto se puede hacer en minutos y no requiere cambios en el código.[](https://www.cloudflare.com/en-in/web-analytics/)
     - Las métricas aparecerán en el panel de control de Cloudflare en **Analytics & Logs**.[](https://developers.cloudflare.com/web-analytics/faq/)
   - **Cloudflare Pages**:
     - Para proyectos de Pages, habilite Web Analytics con un clic: Desde **Workers & Pages**, seleccione su proyecto, vaya a **Metrics** y haga clic en **Enable** en Web Analytics.[](https://developers.cloudflare.com/pages/how-to/web-analytics/)[](https://developers.cloudflare.com/web-analytics/get-started/)

4. **Verificar la Configuración**:
   - Los datos pueden tardar unos minutos en aparecer en el panel de control. Verifique la sección **Web Analytics Sites** para confirmar que el sitio se ha agregado.[](https://developers.cloudflare.com/web-analytics/get-started/)
   - Si usa edge analytics, asegúrese de que la propagación DNS esté completa (puede tardar 24-72 horas).[](https://developers.cloudflare.com/analytics/faq/about-analytics/)

5. **Configurar Reglas (Opcional)**:
   - Configure reglas para rastrear sitios web o rutas específicas. Use dimensiones para categorizar métricas (por ejemplo, por nombre de host o URL).[](https://developers.cloudflare.com/web-analytics/)

#### Notas
- Si su sitio tiene una cabecera `Cache-Control: public, no-transform`, la baliza JavaScript no se inyectará automáticamente y Web Analytics podría no funcionar. Ajuste su configuración de caché o agregue el fragmento manualmente.[](https://developers.cloudflare.com/web-analytics/get-started/)[](https://developers.cloudflare.com/web-analytics/faq/)
- Algunos bloqueadores de anuncios pueden bloquear la baliza JavaScript, pero las edge analytics no se ven afectadas ya que dependen de los registros del servidor.[](https://developers.cloudflare.com/web-analytics/faq/)
- Para la configuración manual, la baliza reporta a `cloudflareinsights.com/cdn-cgi/rum`; para sitios proxyados, usa el endpoint `/cdn-cgi/rum` de su dominio.[](https://developers.cloudflare.com/web-analytics/faq/)

### Uso de Cloudflare Web Analytics
1. **Acceder al Panel de Control**:
   - Inicie sesión en el panel de control de Cloudflare, seleccione su cuenta y dominio, y vaya a **Analytics & Logs** > **Web Analytics**.[](https://developers.cloudflare.com/pages/how-to/web-analytics/)[](https://developers.cloudflare.com/analytics/types-of-analytics/)
   - Vea métricas como vistas de página, visitas, páginas principales, referentes, países, tipos de dispositivos y datos de rendimiento (por ejemplo, tiempos de carga de página, Core Web Vitals).[](https://www.cloudflare.com/en-in/web-analytics/)[](https://usefathom.com/features/vs-cloudflare-web-analytics)

2. **Filtrar y Analizar Datos**:
   - Use filtros para centrarse en métricas específicas (por ejemplo, por nombre de host, URL o país).
   - Haga zoom en los rangos de tiempo para investigar picos de tráfico o agrupe datos por métricas como referentes o páginas.[](https://www.cloudflare.com/en-in/web-analytics/)[](https://blog.cloudflare.com/privacy-first-web-analytics/)
   - Para usuarios avanzados, consulte los datos a través de la **GraphQL Analytics API** para crear paneles de control personalizados.[](https://www.cloudflare.com/application-services/products/analytics/)[](https://www.cloudflare.com/en-in/application-services/products/analytics/)

3. **Comprender las Métricas Clave**:
   - **Vistas de Página (Page Views)**: Total de veces que se carga una página (tipo de contenido HTML con respuesta HTTP exitosa).[](https://developers.cloudflare.com/analytics/account-and-zone-analytics/zone-analytics/)
   - **Visitas (Visits)**: Vistas de página desde un referente diferente (que no coincide con el nombre de host) o enlaces directos.[](https://developers.cloudflare.com/analytics/account-and-zone-analytics/zone-analytics/)[](https://blog.cloudflare.com/privacy-first-web-analytics/)
   - **Visitantes Únicos (Unique Visitors)**: Se basa en direcciones IP, pero no se almacenan por razones de privacidad. Puede ser mayor que en otras herramientas debido al tráfico de bots o a la falta de deduplicación basada en JavaScript.[](https://developers.cloudflare.com/analytics/faq/about-analytics/)[](https://plausible.io/vs-cloudflare-web-analytics)
   - **Métricas de Rendimiento**: Incluye tiempos de carga de página, first paint y Core Web Vitals (solo del lado del cliente).[](https://usefathom.com/features/vs-cloudflare-web-analytics)

4. **Comparar con Otras Herramientas**:
   - A diferencia de Google Analytics, Cloudflare no rastrea los recorridos de los usuarios o las conversiones, pero incluye tráfico de bots y amenazas, lo que puede inflar los números (20-50% del tráfico para la mayoría de los sitios).[](https://developers.cloudflare.com/analytics/faq/about-analytics/)[](https://www.cloudflare.com/insights/)
   - En comparación con Plausible o Fathom Analytics, los datos de Cloudflare son menos detallados debido al muestreo y la retención limitada.[](https://plausible.io/vs-cloudflare-web-analytics)[](https://usefathom.com/features/vs-cloudflare-web-analytics)
   - Las edge analytics pueden mostrar números más altos que las herramientas del lado del cliente como Google Analytics, que excluyen las solicitudes de bots y las que no son de JavaScript.[](https://developers.cloudflare.com/analytics/faq/about-analytics/)[](https://www.reddit.com/r/CloudFlare/comments/1alzkwm/why_are_my_cloudflare_traffic_stats_so_different/)

### Mejores Prácticas
- **Elija el Método Correcto**: Use la baliza JavaScript para métricas centradas en la privacidad del lado del cliente o edge analytics para datos integrales del lado del servidor si su sitio está proxyado.[](https://www.cloudflare.com/web-analytics/)
- **Combine con Otras Herramientas**: Combine con Google Analytics o alternativas centradas en la privacidad como Plausible o Fathom para obtener información más profunda, ya que las analíticas de Cloudflare son básicas.[](https://www.cloudflare.com/insights/)[](https://www.reddit.com/r/webdev/comments/ka8gxv/cloudflares_privacyfirst_web_analytics_is_now/)
- **Monitoree el Rendimiento**: Use las métricas de rendimiento para identificar páginas de carga lenta y aproveche las recomendaciones de Cloudflare (por ejemplo, optimizaciones de caché).[](https://developers.cloudflare.com/web-analytics/)
- **Verifique Problemas con Bloqueadores de Anuncios**: Si usa la baliza JavaScript, informe a los usuarios que permitan `cloudflare.com` o deshabiliten los bloqueadores de anuncios para garantizar la recopilación de datos.[](https://developers.cloudflare.com/analytics/faq/about-analytics/)
- **Revise los Datos Regularmente**: Consulte el panel de control con frecuencia para detectar tendencias o anomalías, ya que los datos solo se retienen durante 30 días.[](https://plausible.io/vs-cloudflare-web-analytics)

### Resolución de Problemas
- **No Se Muestran Datos**:
  - Verifique que el fragmento de JavaScript esté colocado correctamente y que el sitio tenga un HTML válido.[](https://developers.cloudflare.com/pages/how-to/web-analytics/)[](https://developers.cloudflare.com/web-analytics/faq/)
  - Para edge analytics, asegúrese de que el DNS apunte a Cloudflare (la propagación puede tardar 24-72 horas).[](https://developers.cloudflare.com/analytics/faq/about-analytics/)
  - Compruebe si las cabeceras `Cache-Control: no-transform` están bloqueando la inyección automática de la baliza.[](https://developers.cloudflare.com/web-analytics/get-started/)
- **Estadísticas Imprecisas**:
  - Las edge analytics incluyen tráfico de bots, lo que infla los números. Use analíticas del lado del cliente para recuentos de visitantes más precisos.[](https://plausible.io/vs-cloudflare-web-analytics)[](https://markosaric.com/cloudflare-analytics-review/)
  - El muestreo de datos (10%) puede causar discrepancias. Téngalo en cuenta al comparar con otras herramientas.[](https://plausible.io/vs-cloudflare-web-analytics)
- **Problemas con Bloqueadores de Anuncios**: Algunas extensiones del navegador bloquean la baliza JavaScript. Las edge analytics son inmunes a esto.[](https://developers.cloudflare.com/web-analytics/faq/)
- **Faltan Métricas de SPA**: Asegúrese de que el soporte para SPA esté habilitado (`spa: true`) y evite los enrutadores basados en hash.[](https://scripts.nuxt.com/scripts/analytics/cloudflare-web-analytics)

### Uso Avanzado
- **GraphQL Analytics API**: Para análisis personalizados, consulte la API de Cloudflare para crear paneles de control a medida o integrarlos con otros sistemas. Requiere conocimientos técnicos.[](https://www.cloudflare.com/application-services/products/analytics/)[](https://www.cloudflare.com/en-in/application-services/products/analytics/)
- **Cloudflare Workers**: Envíe datos de análisis a una base de datos de series temporales para su procesamiento personalizado o use Workers para análisis serverless avanzados.[](https://developers.cloudflare.com/analytics/)
- **Información de Seguridad**: Combine con Security Analytics de Cloudflare para monitorear amenazas y bots junto con los datos de visitantes.[](https://www.cloudflare.com/insights/)[](https://developers.cloudflare.com/waf/analytics/security-analytics/)

### Comparación con Alternativas
- **Google Analytics**: Ofrece un seguimiento detallado del recorrido del usuario y las conversiones, pero depende de cookies y JavaScript, que pueden ser bloqueados. Cloudflare es más simple y está centrado en la privacidad, pero tiene menos funciones.[](https://developers.cloudflare.com/analytics/faq/about-analytics/)[](https://www.reddit.com/r/webdev/comments/ka8gxv/cloudflares_privacyfirst_web_analytics_is_now/)
- **Plausible Analytics**: De código abierto, centrado en la privacidad, con retención de datos ilimitada y sin muestreo. Más preciso para visitantes únicos, pero requiere un plan de pago.[](https://plausible.io/vs-cloudflare-web-analytics)
- **Fathom Analytics**: Similar a Plausible, con datos exportables y funciones avanzadas como el seguimiento de campañas. La oferta gratuita de Cloudflare es menos sólida pero más fácil de configurar para necesidades básicas.[](https://usefathom.com/features/vs-cloudflare-web-analytics)
- **Jetpack Stats**: Específico para WordPress, con retención de datos limitada (28 días) y sin seguimiento a nivel de usuario. Enfoque de privacidad similar pero menos flexible que Cloudflare.[](https://wordpress.com/support/stats/)

### Recursos Adicionales
- **Documentación Oficial**: [Cloudflare Web Analytics Docs](https://developers.cloudflare.com/web-analytics/)[](https://developers.cloudflare.com/web-analytics/about/)
- **Guía de Configuración**: [Enabling Cloudflare Web Analytics](https://developers.cloudflare.com/web-analytics/get-started/)[](https://developers.cloudflare.com/web-analytics/get-started/)
- **Preguntas Frecuentes**: [Cloudflare Web Analytics FAQs](https://developers.cloudflare.com/web-analytics/faq/)[](https://developers.cloudflare.com/web-analytics/faq/)
- **Publicación de Blog**: [Cloudflare’s Privacy-First Web Analytics](https://blog.cloudflare.com/privacy-first-web-analytics/)[](https://blog.cloudflare.com/privacy-first-web-analytics/)
- **Soporte de la Comunidad**: Consulte los foros de la comunidad de Cloudflare para obtener ayuda adicional.[](https://developers.cloudflare.com/web-analytics/faq/)

### Conclusión
Cloudflare Web Analytics es una excelente opción para los propietarios de sitios web que buscan una herramienta de análisis gratuita, centrada en la privacidad y con una configuración mínima. Es ideal para el monitoreo básico de tráfico y rendimiento, pero puede quedarse corta para necesidades avanzadas debido al muestreo de datos, la retención limitada y la falta de funciones como el seguimiento de conversiones. Para obtener información más profunda, considere combinarla con herramientas como Plausible o Fathom Analytics. Siempre verifique la precisión de la configuración y tenga en cuenta las limitaciones al interpretar los datos.

Si necesita ayuda específica con la configuración o tiene preguntas sobre la integración de Cloudflare Web Analytics con su sitio, ¡avíseme!