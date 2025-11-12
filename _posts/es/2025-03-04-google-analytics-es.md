---
audio: false
generated: true
lang: es
layout: post
title: Uso de Google Analytics
translated: true
type: note
---

Para usar Google Analytics, integrarlo en tu proyecto frontend y verificar los datos usando tanto la aplicación como el sitio web, sigue estos pasos. Esta guía asume que tu proyecto frontend es un sitio web o una aplicación móvil y utiliza **Google Analytics 4 (GA4)**, el estándar actual a partir de 2023, ya que Universal Analytics ya no es compatible para la recopilación de nuevos datos.

---

### 1. Configurar Google Analytics
Antes de integrar Google Analytics en tu proyecto, necesitas crear una cuenta y configurarla:

- **Crear una Cuenta**: Ve a [analytics.google.com](https://analytics.google.com) y regístrate con tu cuenta de Google si aún no tienes una.
- **Crear una Propiedad GA4**:
  - Haz clic en "Administrar" en la esquina inferior izquierda.
  - En "Propiedad", haz clic en "Crear propiedad", completa los detalles de tu proyecto y selecciona **Google Analytics 4**.
- **Añadir un Flujo de Datos**: Dependiendo del tipo de tu proyecto frontend:
  - **Para un Sitio Web**: Elige "Web", ingresa la URL de tu sitio web y nombra el flujo (ej., "Mi Sitio Web").
  - **Para una Aplicación Móvil**: Elige "App", selecciona iOS o Android y proporciona los detalles de tu aplicación (ej., nombre del paquete).

Después de configurar el flujo de datos, obtendrás un **ID de Medición** (ej., `G-XXXXXXXXXX`), que usarás para la integración.

---

### 2. Integrar Google Analytics en tu Proyecto Frontend
El proceso de integración depende de si tu proyecto frontend es un sitio web o una aplicación móvil.

#### Para un Sitio Web
- **Añadir la Etiqueta de Google**:
  - En tu propiedad GA4, ve a "Flujos de datos", selecciona tu flujo web y encuentra las "Instrucciones de Etiquetado".
  - Copia el script de la **Etiqueta de Google** proporcionado, que se ve así:
    ```html
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=YOUR_MEASUREMENT_ID"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'YOUR_MEASUREMENT_ID');
    </script>
    ```
  - Pega este código en la sección `<head>` del HTML de tu sitio web, reemplazando `YOUR_MEASUREMENT_ID` con tu ID de Medición real.
- **Para Aplicaciones de una sola Página (SPA)** (ej., React, Angular, Vue):
  - El script predeterminado solo rastrea la carga inicial de la página. Para las SPAs, donde las páginas no se recargan en los cambios de ruta, usa una librería para rastrear la navegación. Por ejemplo, en **React**:
    1. Instala la librería `react-ga4`:
       ```bash
       npm install react-ga4
       ```
    2. Inicialízala en tu aplicación (ej., en `index.js` o `App.js`):
       ```javascript
       import ReactGA from 'react-ga4';
       ReactGA.initialize('YOUR_MEASUREMENT_ID');
       ```
    3. Rastrea las vistas de página en los cambios de ruta (ej., usando React Router):
       ```javascript
       ReactGA.send({ hitType: "pageview", page: window.location.pathname });
       ```
       Llama a esto cada vez que cambie la ruta, como en un hook `useEffect` vinculado a la ubicación del router.
  - Existen librerías similares para otros frameworks (ej., `ngx-analytics` para Angular, `vue-ga` para Vue—verifica la compatibilidad con GA4).
- **Opcional**: Usa **Google Tag Manager** (GTM) en lugar de codificar la etiqueta directamente para una gestión más fácil de los scripts de rastreo.

#### Para una Aplicación Móvil
- **Usando Firebase (Recomendado)**:
  - Si tu aplicación usa Firebase, habilita **Google Analytics para Firebase**:
    1. Crea un proyecto de Firebase en [console.firebase.google.com](https://console.firebase.google.com).
    2. Añade tu aplicación al proyecto (iOS o Android).
    3. Sigue las indicaciones para descargar el archivo de configuración (ej., `GoogleService-Info.plist` para iOS, `google-services.json` para Android) y añádelo a tu aplicación.
    4. Instala el SDK de Firebase:
       - **iOS**: Usa CocoaPods (`pod 'Firebase/Analytics'`) e inicializa en `AppDelegate`.
       - **Android**: Añade las dependencias en `build.gradle` e inicializa en tu aplicación.
    5. Firebase se vincula automáticamente a tu propiedad GA4 y comienza a recopilar datos.
- **Sin Firebase**:
  - Usa el **SDK de Google Analytics** independiente para iOS o Android (menos común ahora con la integración de Firebase en GA4). Consulta la documentación oficial para la configuración, ya que varía según la plataforma.

---

### 3. Verificar la Integración
- **Para Sitios Web**: Después de añadir el código de rastreo:
  - Visita tu sitio web y abre el informe en **Tiempo real** en Google Analytics (en "Informes" > "Tiempo real").
  - Si ves tu visita registrada, la integración está funcionando.
  - Alternativamente, usa una herramienta del navegador como **GA Checker** o la consola de Chrome DevTools para confirmar las llamadas `gtag`.
- **Para Aplicaciones**: Verifica la Consola de Firebase o el informe de Tiempo real de GA4 después de lanzar tu aplicación con el SDK instalado. Puede tomar unos minutos para que aparezcan los datos.

---

### 4. Verificar los Datos Usando la Aplicación y el Sitio Web
Una vez que Google Analytics comience a recopilar datos, puedes verlos de dos maneras:
- **Interfaz Web de Google Analytics**:
  - Inicia sesión en [analytics.google.com](https://analytics.google.com).
  - Selecciona tu propiedad GA4.
  - Explora informes como:
    - **Tiempo real**: Ve la actividad del usuario en vivo.
    - **Audiencia**: Comprende la demografía de los usuarios.
    - **Adquisición**: Rastrea de dónde vienen los usuarios.
    - **Comportamiento**: Analiza las interacciones de los usuarios (ej., vistas de página, eventos).
- **Aplicación Móvil de Google Analytics**:
  - Descarga la **aplicación oficial de Google Analytics** desde la App Store (iOS) o Google Play Store (Android).
  - Inicia sesión con tu cuenta de Google y selecciona tu propiedad.
  - Ve un subconjunto de informes (ej., Tiempo real, Audiencia) desde tu móvil.

---

### Notas Adicionales
- **Si tu Proyecto Incluye tanto un Sitio Web como una Aplicación**: Puedes añadir múltiples flujos de datos (ej., uno para el sitio web, uno para la aplicación) bajo la misma propiedad GA4. Esto te permite ver análisis combinados o separados en la misma interfaz.
- **Rastreo de Eventos**: Más allá de las vistas de página, rastrea eventos personalizados (ej., clics en botones) usando `gtag('event', ...)` para sitios web o `logEvent` de Firebase para aplicaciones. Ejemplo para un sitio web:
  ```javascript
  gtag('event', 'click', {
    'event_category': 'Button',
    'event_label': 'Submit'
  });
  ```
- **GA4 vs. Universal Analytics**: Usa GA4 para nuevos proyectos, ya que Universal Analytics dejó de procesar datos después del 1 de julio de 2023.

Siguiendo estos pasos, integrarás exitosamente Google Analytics en tu proyecto frontend y podrás monitorear los datos del usuario usando tanto el sitio web como la aplicación móvil de Google Analytics. Si tu tipo de proyecto (sitio web o aplicación) requiere una aclaración específica, ¡ajusta los pasos de integración en consecuencia!