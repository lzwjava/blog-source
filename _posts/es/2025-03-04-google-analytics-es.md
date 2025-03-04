---
audio: false
generated: true
lang: es
layout: post
title: Usando Google Analytics
translated: true
---

Para usar Google Analytics, intégrelo en su proyecto de frontend y verifique los datos utilizando tanto la aplicación como el sitio web, siga estos pasos. Esta guía asume que su proyecto de frontend es un sitio web o una aplicación móvil y utiliza **Google Analytics 4 (GA4)**, el estándar actual a partir de 2023, ya que Universal Analytics ya no es compatible para la nueva recopilación de datos.

---

### 1. Configurar Google Analytics
Antes de integrar Google Analytics en su proyecto, debe crear una cuenta y configurarla:

- **Crear una cuenta**: Vaya a [analytics.google.com](https://analytics.google.com) e inicie sesión con su cuenta de Google si aún no tiene una.
- **Crear una propiedad GA4**:
  - Haga clic en "Admin" en la esquina inferior izquierda.
  - Bajo "Propiedad", haga clic en "Crear propiedad", complete los detalles de su proyecto y seleccione **Google Analytics 4**.
- **Agregar un flujo de datos**: Dependiendo del tipo de proyecto de frontend:
  - **Para un sitio web**: Elija "Web", ingrese la URL de su sitio web y nombre el flujo (por ejemplo, "Mi sitio web").
  - **Para una aplicación móvil**: Elija "App", seleccione iOS o Android y proporcione los detalles de su aplicación (por ejemplo, nombre del paquete).

Después de configurar el flujo de datos, obtendrá un **ID de medición** (por ejemplo, `G-XXXXXXXXXX`), que utilizará para la integración.

---

### 2. Integrar Google Analytics en su proyecto de frontend
El proceso de integración depende de si su proyecto de frontend es un sitio web o una aplicación móvil.

#### Para un sitio web
- **Agregar la etiqueta de Google**:
  - En su propiedad GA4, vaya a "Flujos de datos", seleccione su flujo web y encuentre las "Instrucciones de etiquetado".
  - Copie el script de **Google Tag** proporcionado, que se verá así:
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
  - Pegue este código en la sección `<head>` del HTML de su sitio web, reemplazando `YOUR_MEASUREMENT_ID` con su ID de medición real.
- **Para aplicaciones de una sola página (SPAs)** (por ejemplo, React, Angular, Vue):
  - El script predeterminado solo rastrea la carga inicial de la página. Para SPAs, donde las páginas no se recargan en los cambios de ruta, use una biblioteca para rastrear la navegación. Por ejemplo, en **React**:
    1. Instale la biblioteca `react-ga4`:
       ```bash
       npm install react-ga4
       ```
    2. Inicialícelo en su aplicación (por ejemplo, en `index.js` o `App.js`):
       ```javascript
       import ReactGA from 'react-ga4';
       ReactGA.initialize('YOUR_MEASUREMENT_ID');
       ```
    3. Rastrear vistas de página en cambios de ruta (por ejemplo, usando React Router):
       ```javascript
       ReactGA.send({ hitType: "pageview", page: window.location.pathname });
       ```
       Llame a esto cada vez que cambie la ruta, como en un gancho `useEffect` vinculado a la ubicación del enrutador.
  - Existen bibliotecas similares para otros marcos (por ejemplo, `ngx-analytics` para Angular, `vue-ga` para Vue—verifique la compatibilidad con GA4).
- **Opcional**: Use **Google Tag Manager** (GTM) en lugar de codificar la etiqueta para una gestión más fácil de los scripts de seguimiento.

#### Para una aplicación móvil
- **Usando Firebase (Recomendado)**:
  - Si su aplicación usa Firebase, habilite **Google Analytics for Firebase**:
    1. Cree un proyecto de Firebase en [console.firebase.google.com](https://console.firebase.google.com).
    2. Agregue su aplicación al proyecto (iOS o Android).
    3. Siga las instrucciones para descargar el archivo de configuración (por ejemplo, `GoogleService-Info.plist` para iOS, `google-services.json` para Android) y agréguelo a su aplicación.
    4. Instale el SDK de Firebase:
       - **iOS**: Use CocoaPods (`pod 'Firebase/Analytics'`) e inicialícelo en `AppDelegate`.
       - **Android**: Agregue dependencias en `build.gradle` e inicialícelo en su aplicación.
    5. Firebase se vincula automáticamente a su propiedad GA4 y comienza a recopilar datos.
- **Sin Firebase**:
  - Use el **SDK de Google Analytics independiente** para iOS o Android (menos común ahora con la integración de Firebase de GA4). Consulte la documentación oficial para la configuración, ya que varía según la plataforma.

---

### 3. Verificar la integración
- **Para sitios web**: Después de agregar el código de seguimiento:
  - Visite su sitio web y abra el informe **en tiempo real** en Google Analytics (en "Informes" > "En tiempo real").
  - Si ve su visita registrada, la integración está funcionando.
  - Alternativamente, use una herramienta del navegador como **GA Checker** o la consola de Chrome DevTools para confirmar las llamadas `gtag`.
- **Para aplicaciones**: Verifique la consola de Firebase o el informe en tiempo real de GA4 después de lanzar su aplicación con el SDK instalado. Puede tardar unos minutos en aparecer los datos.

---

### 4. Verificar los datos utilizando la aplicación y el sitio web
Una vez que Google Analytics comience a recopilar datos, puede verlos de dos maneras:
- **Interfaz web de Google Analytics**:
  - Inicie sesión en [analytics.google.com](https://analytics.google.com).
  - Seleccione su propiedad GA4.
  - Explore informes como:
    - **En tiempo real**: Vea la actividad del usuario en vivo.
    - **Audiencia**: Entienda la demografía de los usuarios.
    - **Adquisición**: Rastrear de dónde vienen los usuarios.
    - **Comportamiento**: Analice las interacciones de los usuarios (por ejemplo, vistas de página, eventos).
- **Aplicación móvil de Google Analytics**:
  - Descargue la aplicación oficial **Google Analytics** desde la App Store (iOS) o Google Play Store (Android).
  - Inicie sesión con su cuenta de Google y seleccione su propiedad.
  - Vea un subconjunto de informes (por ejemplo, En tiempo real, Audiencia) sobre la marcha.

---

### Notas adicionales
- **Si su proyecto incluye tanto un sitio web como una aplicación**: Puede agregar múltiples flujos de datos (por ejemplo, uno para el sitio web, uno para la aplicación) bajo la misma propiedad GA4. Esto le permite ver análisis combinados o separados en la misma interfaz.
- **Rastrear eventos**: Más allá de las vistas de página, rastree eventos personalizados (por ejemplo, clics en botones) usando `gtag('event', ...)` para sitios web o `logEvent` de Firebase para aplicaciones. Ejemplo para un sitio web:
  ```javascript
  gtag('event', 'click', {
    'event_category': 'Button',
    'event_label': 'Submit'
  });
  ```
- **GA4 vs. Universal Analytics**: Use GA4 para nuevos proyectos, ya que Universal Analytics dejó de procesar datos después del 1 de julio de 2023.

Siguiendo estos pasos, integrará Google Analytics en su proyecto de frontend y podrá monitorear los datos de los usuarios utilizando tanto el sitio web como la aplicación móvil de Google Analytics. ¡Si el tipo de proyecto (sitio web o aplicación) requiere una aclaración específica, ajuste los pasos de integración en consecuencia!