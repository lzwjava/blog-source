---
audio: false
generated: true
lang: es
layout: post
title: Publicar una aplicación iOS en la App Store
translated: true
---

Para usar el Programa para Desarrolladores de Apple para subir una aplicación iOS, ya sea para uso personal o corporativo, debes inscribirte en el programa, preparar y empaquetar tu aplicación, subirla y gestionar las actualizaciones. A continuación, se presenta una guía paso a paso que aborda todos los aspectos de tu consulta, incluyendo el requisito del número D-U-N-S de Dun & Bradstreet para uso corporativo, el empaquetado de la aplicación, la carga del archivo y la actualización de aplicaciones a través del sitio de Apple.

---

### 1. Inscribirse en el Programa para Desarrolladores de Apple

#### Para Individuos (Uso Personal)
- **Crear una Apple ID**:
  Si no tienes una, ve a [appleid.apple.com](https://appleid.apple.com) e inscríbete usando una dirección de correo electrónico personal.
- **Inscribirse en el Programa**:
  - Visita [developer.apple.com/programs/](https://developer.apple.com/programs/) y haz clic en "Inscribirse."
  - Inicia sesión con tu Apple ID.
  - Acepta los términos, proporciona tu nombre legal personal y dirección, y paga la cuota anual de $99 USD.
- **Nota Clave**: Tu nombre personal aparecerá como vendedor en la App Store.

#### Para Corporaciones (Uso Organizacional)
- **Obtener un Número D-U-N-S**:
  - Un Número D-U-N-S es un identificador único de nueve dígitos asignado por Dun & Bradstreet para verificar el estado de entidad legal de tu organización. Apple lo requiere para cuentas corporativas.
  - Verifica si tu organización ya tiene uno en [dnb.com](https://www.dnb.com). Si no, solicítalo gratuitamente a través de su sitio web; el procesamiento puede tardar hasta dos semanas.
- **Inscribirse en el Programa**:
  - Usa una Apple ID vinculada a tu organización (por ejemplo, un correo electrónico de negocios).
  - Ve a [developer.apple.com/programs/](https://developer.apple.com/programs/) y haz clic en "Inscribirse."
  - Selecciona "Organización" y proporciona:
    - Nombre de la entidad legal
    - Dirección de la sede
    - Número D-U-N-S
  - La persona que se inscribe debe tener la autoridad legal para aceptar los términos de Apple en nombre de la organización.
  - Paga la cuota anual de $99 USD.
- **Nota Clave**: El nombre de tu organización aparecerá como vendedor en la App Store.

---

### 2. Preparar y Empaquetar la Aplicación
- **Desarrollar tu Aplicación en Xcode**:
  - Usa Xcode, la herramienta de desarrollo oficial de Apple, para construir tu aplicación iOS.
  - Asegúrate de que cumpla con las [Directrices de Revisión de la App Store](https://developer.apple.com/app-store/review/guidelines/).
  - Establece el objetivo de implementación y actualiza los números de versión y compilación de la aplicación en la configuración del proyecto.
- **Archivar la Aplicación**:
  - Abre tu proyecto en Xcode.
  - Selecciona "Dispositivo iOS Genérico" (o cualquier simulador) como el objetivo de compilación.
  - Ve a **Producto** > **Archivar** en la barra de menú.
  - Xcode compilará tu aplicación y creará un archivo, que es una versión empaquetada lista para distribución, incluyendo código, recursos e información de firma.

---

### 3. Subir el Archivo de la Aplicación
- **Usando Xcode**:
  - Después de archivar, se abrirá automáticamente la ventana del Organizador en Xcode.
  - Selecciona tu archivo y haz clic en **Distribuir Aplicación**.
  - Elige **App Store Connect** como el método de distribución.
  - Sigue las indicaciones para validar y subir el archivo a App Store Connect.
- **Usando Transporter (Alternativa)**:
  - Descarga la [aplicación Transporter](https://apps.apple.com/us/app/transporter/id1450874784) desde la Mac App Store.
  - Inicia sesión con tu Apple ID.
  - Añade el archivo de la aplicación archivada (exportado como un archivo `.ipa` desde Xcode) y súbelo a App Store Connect.
  - Esta opción es útil para usuarios avanzados o subidas masivas.

---

### 4. Actualizar Aplicaciones Usando el Sitio de Apple (App Store Connect)
- **Acceder a App Store Connect**:
  - Ve a [appstoreconnect.apple.com](https://appstoreconnect.apple.com) e inicia sesión con tu Apple ID.
- **Gestionar tu Aplicación**:
  - Selecciona tu aplicación desde el tablero.
  - Navega a la pestaña **App Store**.
  - Actualiza los metadatos (por ejemplo, descripción de la aplicación, capturas de pantalla, palabras clave).
  - En "Versiones," selecciona la nueva compilación que subiste.
- **Enviar para Revisión**:
  - Haz clic en **Enviar para Revisión** para enviar la actualización al equipo de revisión de Apple.
  - Después de la aprobación, puedes liberarla manualmente o programar una liberación automática.

---

### Notas Adicionales
- **Detalles Específicos para Corporaciones**:
  - Asegúrate de que tu Número D-U-N-S y la información de la organización sean precisos para evitar retrasos en la inscripción.
  - Puedes invitar a miembros del equipo (por ejemplo, desarrolladores, probadores) a tu cuenta a través de App Store Connect y asignar roles como "Desarrollador" o "Administrador."
- **Desafíos Comunes y Consejos**:
  - **Problemas de Firma de Código**: Verifica tus certificados y perfiles de aprovisionamiento en Xcode bajo **Firma y Capacidades**. Usa la opción "Gestionar firma automáticamente" si no estás seguro.
  - **Rechazos de Revisión de Aplicaciones**: Prueba tu aplicación a fondo para cumplir con las directrices de Apple y evitar retrasos.
  - **Retrasos en D-U-N-S**: Solicita tu Número D-U-N-S con antelación si eres una corporación, ya que es un requisito previo para la inscripción.

---

Con estos pasos, puedes usar el Programa para Desarrolladores de Apple para subir y actualizar tu aplicación iOS, ya sea como individuo o como corporación. Para obtener más detalles, consulta la documentación oficial de Apple en [developer.apple.com](https://developer.apple.com).