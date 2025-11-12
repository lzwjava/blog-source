---
audio: false
generated: true
lang: es
layout: post
title: Publicar una Aplicación de iOS en la App Store
translated: true
type: note
---

Para utilizar el Apple Developer Program y subir una aplicación iOS, ya sea para uso personal o corporativo, necesitas registrarte en el programa, preparar y empaquetar tu aplicación, subirla y gestionar las actualizaciones. A continuación, se presenta una guía paso a paso que aborda todos los aspectos de tu consulta, incluido el requisito del número Dun & Bradstreet (D-U-N-S) para uso corporativo, el empaquetado de la aplicación, la subida del archivo y la actualización de aplicaciones a través del sitio de Apple.

---

### 1. Registrarse en el Apple Developer Program

#### Para Personas Físicas (Uso Personal)
- **Crear un Apple ID**:  
  Si no tienes uno, ve a [appleid.apple.com](https://appleid.apple.com) y regístrate usando una dirección de correo electrónico personal.
- **Registrarse en el Programa**:  
  - Visita [developer.apple.com/programs/](https://developer.apple.com/programs/) y haz clic en "Enroll".
  - Inicia sesión con tu Apple ID.
  - Acepta los términos, proporciona tu nombre legal personal y tu dirección, y paga la tarifa anual de 99 USD.
- **Nota Importante**: Tu nombre personal aparecerá como el vendedor en la App Store.

#### Para Empresas (Uso Corporativo)
- **Obtener un Número D-U-N-S**:  
  - Un Número D-U-N-S es un identificador único de nueve dígitos asignado por Dun & Bradstreet para verificar el estado de entidad legal de tu organización. Apple lo requiere para cuentas corporativas.
  - Verifica si tu organización ya tiene uno en [dnb.com](https://www.dnb.com). Si no, solicítalo gratis a través de su sitio web; el proceso puede tardar hasta dos semanas.
- **Registrarse en el Programa**:  
  - Utiliza un Apple ID vinculado a tu organización (por ejemplo, un correo electrónico empresarial).
  - Ve a [developer.apple.com/programs/](https://developer.apple.com/programs/) y haz clic en "Enroll".
  - Selecciona "Organization" y proporciona:
    - Nombre de la entidad legal
    - Dirección de la sede central
    - Número D-U-N-S
  - La persona que se registra debe tener autoridad legal para aceptar los términos de Apple en nombre de la organización.
  - Paga la tarifa anual de 99 USD.
- **Nota Importante**: El nombre de tu organización aparecerá como el vendedor en la App Store.

---

### 2. Preparar y Empaquetar la Aplicación
- **Desarrolla tu Aplicación en Xcode**:  
  - Utiliza Xcode, la herramienta oficial de desarrollo de Apple, para construir tu aplicación iOS.
  - Asegúrate de que cumple con las [App Store Review Guidelines](https://developer.apple.com/app-store/review/guidelines/).
  - Establece el objetivo de despliegue y actualiza la versión de la aplicación y los números de compilación en la configuración del proyecto.
- **Archiva la Aplicación**:  
  - Abre tu proyecto en Xcode.
  - Selecciona "Generic iOS Device" (o cualquier simulador) como el objetivo de compilación.
  - Ve a **Product** > **Archive** en la barra de menús.
  - Xcode compilará tu aplicación y creará un archivo, que es una versión empaquetada lista para su distribución, incluyendo código, recursos e información de firma.

---

### 3. Subir el Archivo de la Aplicación
- **Usando Xcode**:  
  - Después de archivar, la ventana Organizer se abre automáticamente en Xcode.
  - Selecciona tu archivo y haz clic en **Distribute App**.
  - Elige **App Store Connect** como método de distribución.
  - Sigue las indicaciones para validar y subir el archivo a App Store Connect.
- **Usando Transporter (Alternativa)**:  
  - Descarga la aplicación [Transporter](https://apps.apple.com/us/app/transporter/id1450874784) desde la Mac App Store.
  - Inicia sesión con tu Apple ID.
  - Añade el archivo de la aplicación archivada (exportado como un archivo `.ipa` desde Xcode) y súbelo a App Store Connect.
  - Esta opción es útil para usuarios avanzados o subidas masivas.

---

### 4. Actualizar Aplicaciones Usando el Sitio de Apple (App Store Connect)
- **Acceder a App Store Connect**:  
  - Ve a [appstoreconnect.apple.com](https://appstoreconnect.apple.com) e inicia sesión con tu Apple ID.
- **Gestiona tu Aplicación**:  
  - Selecciona tu aplicación desde el panel de control.
  - Navega a la pestaña **App Store**.
  - Actualiza los metadatos (por ejemplo, descripción de la aplicación, capturas de pantalla, palabras clave).
  - En "Versions", selecciona la nueva compilación que subiste.
- **Enviar para Revisión**:  
  - Haz clic en **Submit for Review** para enviar la actualización al equipo de revisión de Apple.
  - Después de la aprobación, puedes lanzarla manualmente o programar un lanzamiento automático.

---

### Notas Adicionales
- **Detalles Específicos para Empresas**:  
  - Asegúrate de que tu Número D-U-N-S y la información de la organización sean precisos para evitar retrasos en el registro.
  - Puedes invitar a miembros del equipo (por ejemplo, desarrolladores, testers) a tu cuenta a través de App Store Connect y asignar roles como "Developer" o "Admin".
- **Desafíos Comunes y Consejos**:  
  - **Problemas de Firma de Código**: Verifica tus certificados y perfiles de provisión en Xcode en **Signing & Capabilities**. Utiliza la opción "Automatically manage signing" si no estás seguro.
  - **Rechazos en la Revisión de la Aplicación**: Prueba tu aplicación a fondo para cumplir con las directrices de Apple y evitar retrasos.
  - **Retrasos con el Número D-U-N-S**: Solicita tu Número D-U-N-S con anticipación si eres una corporación, ya que es un requisito previo para el registro.

---

Con estos pasos, puedes utilizar con éxito el Apple Developer Program para subir y actualizar tu aplicación iOS, ya sea como individuo o como corporación. Para más detalles, consulta la documentación oficial de Apple en [developer.apple.com](https://developer.apple.com).