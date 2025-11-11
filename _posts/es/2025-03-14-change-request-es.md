---
audio: false
generated: true
lang: es
layout: post
title: Cómo Usar una Solicitud de Cambio
translated: true
type: note
---

Para agregar un grupo a una Solicitud de Cambio en ServiceNow, debe asignar un grupo al campo **Grupo de asignación** dentro del formulario de Solicitud de Cambio. A continuación, se presenta una guía detallada paso a paso para ayudarle en el proceso.

---

### Guía Paso a Paso

1. **Navegar al Módulo de Solicitud de Cambio**  
   - Inicie sesión en su instancia de ServiceNow.  
   - En el panel de navegación izquierdo, escriba "Change" en el filtro de navegación.  
   - Seleccione **Change > All** para ver la lista de todas las Solicitudes de Cambio.

2. **Abrir la Solicitud de Cambio**  
   - Localice la Solicitud de Cambio específica a la que desea asignar un grupo. Puede usar la barra de búsqueda o los filtros (por ejemplo, por número de Solicitud de Cambio o descripción breve).  
   - Haga clic en la Solicitud de Cambio para abrir su formulario.

3. **Localizar el Campo Grupo de Asignación**  
   - En el formulario de la Solicitud de Cambio, busque el campo **Assignment group**. Este campo normalmente se encuentra en la sección "Planning" o "Assignment" del formulario, dependiendo de la configuración de su instancia.

4. **Seleccionar el Grupo**  
   - Haga clic en el icono de lupa (búsqueda de referencia) junto al campo **Assignment group**.  
   - Aparecerá una ventana emergente que muestra una lista de grupos disponibles.  
   - Escriba el nombre del grupo en el cuadro de búsqueda para filtrar la lista, luego seleccione el grupo deseado haciendo clic en él.  
   - Si conoce el nombre exacto del grupo, también puede empezar a escribirlo directamente en el campo, y ServiceNow sugerirá grupos coincidentes.

5. **Guardar los Cambios**  
   - Después de seleccionar el grupo, haga clic en **Update** o **Save** (normalmente se encuentra en la parte superior o inferior del formulario) para guardar los cambios en la Solicitud de Cambio.

---

### Consideraciones Importantes

- **Tipo de Grupo**  
   Asegúrese de que el grupo que desea asignar esté configurado con un tipo de grupo apropiado (por ejemplo, "Change" o "ITIL"). Algunas instancias de ServiceNow restringen los grupos disponibles en el campo **Assignment group** según su tipo. Para verificar o actualizar el tipo de un grupo:  
   - Vaya a **User Administration > Groups**, busque el grupo y verifique su campo "Type".

- **Permisos**  
   Necesita permisos suficientes para asignar grupos a una Solicitud de Cambio. Normalmente, se requieren roles como `change_manager` o equivalentes. Si no puede asignar un grupo, contacte a su administrador de ServiceNow para confirmar su acceso.

- **Calificadores de Referencia**  
   El campo **Assignment group** podría tener filtros (calificadores de referencia) que limitan qué grupos aparecen. Si el grupo que desea no aparece en la lista, podría deberse a una configuración en los ajustes del diccionario del campo. Un administrador puede verificar esto en **System Definition > Dictionary**.

- **Asignación Automatizada (Opcional)**  
   Si bien esta guía cubre la asignación manual, tenga en cuenta que los grupos también se pueden asignar automáticamente utilizando flujos de trabajo o reglas de asignación configuradas por su organización.

---

### Resolución de Problemas
- **¿El Grupo No Aparece?**  
   - Verifique que el grupo exista en **User Administration > Groups**.  
   - Verifique su tipo de grupo y cualquier calificador de referencia en el campo **Assignment group**.  
- **¿Sin Permiso para Guardar?**  
   - Asegúrese de tener el rol necesario para editar Solicitudes de Cambio.

Siguiendo estos pasos y considerando los puntos anteriores, debería poder agregar exitosamente un grupo a una Solicitud de Cambio en ServiceNow. Si encuentra problemas, consulte a su administrador de ServiceNow para obtener asistencia adaptada a la configuración de su instancia.

---

Para abordar su problema donde su Solicitud de Cambio en ServiceNow aparece vacía—con secciones como enlaces relacionados, planificación, CIs afectados, aprobadores y la lista de solicitudes de cambio sin mostrar datos—necesita completar estas áreas con la información necesaria. Parece que, aunque el formulario de Solicitud de Cambio en sí existe, sus listas relacionadas y campos carecen de entradas. A continuación, se presenta una guía paso a paso para ayudarle a completar los detalles requeridos y las listas relacionadas.

---

### Paso 1: Verificar y Completar la Información Básica
Aunque su Solicitud de Cambio existe, puede carecer de detalles esenciales. Comience asegurándose de que los campos fundamentales estén completados:

- **Abra la Solicitud de Cambio**: Navegue a la Solicitud de Cambio específica en ServiceNow (por ejemplo, a través del módulo Change > All o buscando su número).
- **Verifique los Campos Obligatorios**:
  - **Short Description**: Agregue un resumen breve del cambio (por ejemplo, "Actualizar memoria del servidor").
  - **Description**: Proporcione una explicación detallada de lo que implica el cambio.
  - **Requester**: Especifique quién solicita el cambio (esto podría asignarse a usted por defecto si lo creó).
  - **Assignment Group**: Asigne el equipo responsable del cambio (por ejemplo, "Server Team").
  - **Assigned To**: Opcionalmente, asigne a un individuo específico dentro del grupo.
- **Guarde el Formulario**: Haga clic en **Save** o **Update** para asegurarse de que estos detalles se registren. Algunos campos pueden ser obligatorios (marcados con un asterisco rojo), y es posible que no se pueda guardar hasta que se completen.

---

### Paso 2: Completar los Detalles de Planificación
La sección "planning" que mencionó probablemente se refiere a campos que definen el alcance y el cronograma del cambio. Complételos para proporcionar contexto:

- **Change Type**: Seleccione el tipo (por ejemplo, Normal, Emergency, Standard).
- **Category**: Elija una categoría apropiada (por ejemplo, Hardware, Software, Network).
- **Priority**: Establezca según la urgencia y el impacto (por ejemplo, Low, Medium, High).
- **Risk and Impact**: Evalúe e ingrese los niveles de riesgo e impacto potenciales.
- **Planned Start and End Dates**: Especifique cuándo comenzará y terminará el cambio.
- **Guarde los Cambios**: Asegúrese de que estos campos se guarden para actualizar la Solicitud de Cambio.

---

### Paso 3: Agregar CIs Afectados
La lista de "affected CIs" está vacía porque no se han vinculado Elementos de Configuración (CIs). Así es como puede completarla:

- **Localice la Lista Relacionada**: Desplácese a la sección **Affected CIs** en la parte inferior del formulario.
- **Agregue CIs**:
  - Haga clic en **Edit** o **New** (dependiendo de la configuración de su instancia).
  - Aparecerá una ventana de selección que le permitirá buscar y seleccionar CIs de la Base de Datos de Gestión de Configuración (CMDB).
  - Elija los CIs relevantes (por ejemplo, servidores, aplicaciones) impactados por el cambio.
- **Guarde**: Haga clic en **Save** para vincular estos CIs a la Solicitud de Cambio.

---

### Paso 4: Gestionar los Aprobadores
La lista de "approvers" está vacía porque aún no existen registros de aprobación. Dependiendo del proceso de su organización, los aprobadores pueden agregarse automáticamente o manualmente:

- **Verifique el Proceso de Aprobación**:
  - Busque un botón **Request Approval** o una acción de UI en el formulario. Al hacer clic en él, puede activar un flujo de trabajo de aprobación basado en reglas predefinidas (por ejemplo, tipo de cambio o nivel de riesgo).
- **Agregar Aprobadores Manualmente** (si es necesario):
  - Vaya a la lista relacionada **Approvals**.
  - Haga clic en **New** para crear un registro de aprobación.
  - Seleccione el aprobador (por ejemplo, un gerente o miembro del Change Advisory Board) y guarde.
- **Monitoree el Estado**: Una vez agregados, los aprobadores deberán aprobar o rechazar el cambio.

---

### Paso 5: Completar la Lista de Solicitudes de Cambio (Cambios Hijos o Tareas)
Usted mencionó que una "lista de solicitudes de cambio" está vacía, lo que podría referirse a Solicitudes de Cambio hijas o **Change Tasks**. Así es como puede abordar esto:

- **Change Tasks** (más probable):
  - Desplácese a la lista relacionada **Change Tasks**.
  - Haga clic en **New** para crear una tarea.
  - Complete detalles como la descripción de la tarea, grupo de asignación, asignado a y fecha de vencimiento.
  - Guarde la tarea. Repita para todas las tareas requeridas.
- **Child Change Requests** (si aplica):
  - Si su organización utiliza Solicitudes de Cambio padre-hijo, busque una lista relacionada como **Child Changes**.
  - Haga clic en **New** para crear una Solicitud de Cambio vinculada y complete sus detalles.
- **Guarde los Cambios**: Asegúrese de que todas las tareas o solicitudes hijas se guarden.

---

### Paso 6: Abordar los "Enlaces Relacionados"
Usted mencionó que los "related links" están vacíos. Esto podría ser una mala comunicación para las listas relacionadas (como incidentes o problemas) en lugar de la sección de UI "Related Links". Para completar registros relacionados:

- **Vincular Registros Relacionados**:
  - Busque listas relacionadas como **Related Incidents**, **Related Problems** o **Caused by Change**.
  - Haga clic en **Edit** o **New** en estas listas.
  - Busque y vincule registros relevantes (por ejemplo, un incidente que desencadenó este cambio).
- **Guarde**: Actualice el formulario después de agregar estos enlaces.

---

### Paso 7: Progresar la Solicitud de Cambio
Una vez que la información básica y las listas relacionadas estén completadas, avance la Solicitud de Cambio:

- **Verifique el Estado**: Verifique el estado actual (probablemente "New").
- **Pase al Siguiente Estado**: Use el menú desplegable **State** o las acciones de UI (por ejemplo, **Assess**, **Authorize**) para avanzarlo. Algunos campos o listas pueden volverse relevantes solo en estados posteriores (por ejemplo, fechas reales en "Implement").
- **Siga el Flujo de Trabajo**: El flujo de trabajo de su instancia guiará el proceso—complete los campos requeridos en cada etapa.

---

### Notas Importantes
- **Permisos**: Asegúrese de tener el acceso necesario (por ejemplo, el rol `change_manager`) para editar estos campos y listas. Si no es así, contacte a su administrador de ServiceNow.
- **Configuración Personalizada**: Su instancia podría usar plantillas, modelos de cambio o flujos de trabajo automatizados que completen previamente algunos datos. Consulte con su administrador si los campos no se comportan como se espera.
- **Visibilidad**: Algunas secciones podrían estar ocultas o bloqueadas según el estado o sus permisos—avanzar el estado puede revelar más opciones.

Siguiendo estos pasos, transformará su Solicitud de Cambio vacía en un registro completamente completo listo para su procesamiento. Si los problemas persisten, proporcione a su administrador de ServiceNow los detalles (por ejemplo, el número de la Solicitud de Cambio) para una investigación más profunda.