---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Creación de una Instancia de Azure API Management
translated: true
type: note
---

### Creación de una puerta de enlace de API en Azure mediante API Management

Azure API Management (APIM) es el servicio completamente administrado que actúa como puerta de enlace de API, proporcionando funciones como publicación de API, seguridad, análisis y portales para desarrolladores. A continuación se presenta una guía paso a paso para crear una instancia de APIM a través del portal de Azure.

#### Prerrequisitos
- Una suscripción activa de Azure. Si no tiene una, cree una [cuenta gratuita de Azure](https://azure.microsoft.com/es-es/free/).

#### Pasos para crear una instancia de API Management

1. **Iniciar sesión en el Portal de Azure**  
   Vaya al [portal de Azure](https://portal.azure.com) e inicie sesión con su cuenta de Azure.

2. **Crear un nuevo recurso**  
   - Desde el menú del portal de Azure, seleccione **Crear un recurso**. (Alternativamente, seleccione **Crear un recurso** desde la página de inicio de Azure).  
   - En la página **Crear un recurso**, busque y seleccione **API Management** en la categoría **Integración**.  
   - Haga clic en **Crear**.

3. **Configurar los aspectos básicos**  
   En la página **Crear API Management**, cambie a la pestaña **Aspectos básicos** y complete los detalles:  
   | Configuración         | Descripción                                                                 |
   |-----------------------|-----------------------------------------------------------------------------|
   | Suscripción          | Seleccione la suscripción de Azure para esta instancia.                    |
   | Grupo de recursos    | Elija un grupo de recursos existente o cree uno nuevo (ej. "APIM-RG").     |
   | Región               | Elija una región cercana a sus usuarios o servicios backend (ej. Este de EE. UU.). |
   | Nombre del recurso   | Ingrese un nombre único (ej. "mi-instancia-apim"). Esto se convierte en parte del dominio predeterminado: `<nombre>.azure-api.net`. No se puede cambiar posteriormente. |
   | Nombre de la organización | El nombre de su organización (se utiliza en el portal para desarrolladores y correos electrónicos). |
   | Email del administrador | Su correo electrónico para notificaciones del sistema.                     |
   | Plan de tarifa       | Comience con **Básico v2** para desarrollo/pruebas (implementación rápida, ~30-40 minutos). Otros niveles como Desarrollador o Estándar ofrecen más características. |
   | Unidades             | Por defecto 1 para evaluación.                                             |  
   Revise y continúe.

4. **Opcional: Configurar supervisión y seguridad**  
   En la pestaña **Supervisar + proteger**:  
   - Habilite complementos opcionales como Log Analytics para el registro (esto puede generar costos adicionales).  
   - Omita por ahora si está comenzando.

5. **Revisar y crear**  
   - En la pestaña **Revisar + crear**, valide su configuración.  
   - Haga clic en **Crear**. La implementación tarda 30-40 minutos o más.  
   - Consejo: Ancle el recurso a su panel para un acceso fácil una vez creado.

6. **Verificar la instancia**  
   - En el portal de Azure, busque **Servicios de API Management**.  
   - Seleccione su nueva instancia.  
   - En la página **Información general**, confirme que el estado sea "En línea". Ya está listo para importar API, configurar políticas o configurar el portal para desarrolladores.

#### Próximos pasos
- Importe su primera API: Siga el [tutorial para importar y publicar una API](https://learn.microsoft.com/es-es/azure/api-management/import-and-publish).  
- Asegúrela: Agregue políticas para autenticación, limitación de tasa, etc.  
- Limpieza: Si está probando, elimine el grupo de recursos a través del portal para evitar cargos (busque **Grupos de recursos** > seleccione el grupo > **Eliminar grupo de recursos**).  

Para dominios personalizados o configuraciones avanzadas, consulte la [documentación de APIM](https://learn.microsoft.com/es-es/azure/api-management/).

[Inicio rápido: Creación de una instancia de Azure API Management - Portal](https://learn.microsoft.com/es-es/azure/api-management/get-started-create-service-instance)  
[Información general de Azure API Management](https://learn.microsoft.com/es-es/azure/api-management/api-management-key-concepts)