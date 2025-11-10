---
audio: false
generated: true
lang: es
layout: post
title: Eliminar modelos personalizados en GitHub Copilot
translated: true
type: note
---

Para eliminar un modelo en la extensión GitHub Copilot para Visual Studio Code (VS Code), ten en cuenta que los modelos integrados (como el modelo predeterminado de GitHub Copilot) no se pueden eliminar, ya que forman parte de la extensión. Sin embargo, si te refieres a un modelo personalizado que hayas agregado a través de un proveedor de terceros (por ejemplo, Anthropic, OpenAI, Google Gemini u otros) utilizando tu propia clave API, puedes eliminarlo efectivamente borrando la clave API asociada y los detalles del proveedor. Esta función está en vista previa y puede que aún no esté disponible para usuarios de Copilot Business o Enterprise.

Estos son los pasos basados en la documentación oficial:

1.  Abre la vista de Chat en VS Code (si no está abierta, usa la Paleta de comandos con `Ctrl+Mayús+P` o `Cmd+Mayús+P` en macOS, luego busca "Copilot: Open Chat").
2.  En la vista de Chat, haz clic en el menú desplegable de selección de modelos (junto al campo de entrada) y selecciona **Manage Models**. Alternativamente, abre la Paleta de comandos y ejecuta el comando **GitHub Copilot: Manage Models**.
3.  En la interfaz Manage Models, pasa el cursor sobre el proveedor del modelo que deseas eliminar y haz clic en el icono de engranaje para editar sus detalles.
4.  Borra la clave API (y cualquier URL de endpoint si es aplicable) de los campos, luego guarda los cambios. Esto debería eliminar la disponibilidad del modelo del selector.

Si encuentras problemas (por ejemplo, el campo de la clave API no se actualiza o no se borra correctamente, lo cual se ha reportado como un error en algunos casos), prueba primero esta solución alternativa:
-   Selecciona un modelo diferente del selector de modelos en la vista de Chat para anular la selección del que intentas eliminar.
-   Vuelve a Manage Models, edita el proveedor y luego borra la clave API.

Requisitos previos y notas:
-   Esto solo se aplica a las funciones de chat; no afecta a las finalizaciones de código ni a otras herramientas.
-   Asegúrate de que tu suscripción a Copilot permita el acceso a múltiples modelos (por ejemplo, Individual, Pro, o las funciones de vista previa habilitadas para organizaciones).
-   Si el modelo persiste o encuentras errores, reinicia VS Code o busca actualizaciones de la extensión.

Si esto no coincide con lo que querías decir con "eliminar un modelo" (por ejemplo, si estás intentando deshabilitar la extensión completa u ocultar las funciones de Copilot), acláralo para obtener pasos más específicos.