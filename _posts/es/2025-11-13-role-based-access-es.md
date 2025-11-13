---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Control de Acceso Basado en Roles en Jenkins
translated: true
type: note
---

### Control de Acceso Basado en Roles (RBAC) en Enterprise Jenkins (CloudBees CI)

Enterprise Jenkins, impulsado por CloudBees CI, utiliza el plugin CloudBees Role-Based Access Control (RBAC) para implementar permisos granulares basados en roles. Esto permite a los administradores definir roles personalizados, asignarlos a usuarios o grupos y controlar el acceso a nivel global, de carpeta o de trabajo. Se integra con el plugin Folders para el aislamiento basado en equipos y es compatible con proveedores de identidad externos como LDAP o Active Directory para la gestión de grupos. Los permisos se agregan de todos los roles asignados a los grupos de un usuario y pueden propagarse a objetos secundarios (por ejemplo, subcarpetas) a menos que estén fijados o filtrados.

RBAC reemplaza o mejora la autorización matricial integrada de Jenkins, permitiendo la delegación de la administración sin acceso total al sistema. Se configura en **Manage Jenkins > Manage Security > Authorization**, donde se selecciona la "Role-based matrix authorization strategy".

#### Permisos y Derechos de Acceso Clave
Los permisos definen acciones atómicas que los usuarios pueden realizar en objetos de Jenkins (por ejemplo, trabajos, carpetas, agentes, vistas). Enterprise Jenkins incluye los permisos principales de Jenkins más los extendidos por plugins. Los permisos son jerárquicos: algunos implican otros (por ejemplo, `Job/Configure` implica `Job/Read`).

Aquí hay una tabla de categorías de permisos comunes y ejemplos, centrándose en build/read como se mencionó:

| Categoría          | Ejemplos de Permisos                                                                 | Descripción |
|-------------------|-----------------------------------------------------------------------------------------|-------------|
| **Lectura/Solo Lectura** | - `Overall/Read`<br>- `Job/Read`<br>- `View/Read`<br>- `Agent/Read`                     | Otorga acceso de visualización a configuraciones, builds, logs y artefactos sin modificación. Útil para auditores o visualizadores. El plugin Extended Read Permission agrega controles de lectura granular (por ejemplo, ver el workspace sin derechos de build). |
| **Build/Ejecutar** | - `Job/Build`<br>- `Job/Cancel`<br>- `Job/Workspace`<br>- `Job/Read (for artifacts)`   | Permite iniciar, detener o acceder a los resultados del build. Puede tener alcance en trabajos/carpetas específicos. |
| **Configurar/Modificar** | - `Job/Configure`<br>- `Job/Create`<br>- `Job/Delete`<br>- `Folder/Configure`            | Permite editar parámetros del trabajo, agregar triggers o gestionar elementos secundarios. |
| **Administrativos** | - `Overall/Administer`<br>- `Overall/Configure`<br>- `Group/Manage`<br>- `Role/View`     | Control total del sistema o tareas delegadas como gestionar roles/grupos. `Overall/Administer` es el permiso de superusuario. |
| **Otros**         | - `SCM/Tag`<br>- `Credentials/View`<br>- `Agent/Launch`<br>- `RunScripts`                | Operaciones SCM, acceso a credenciales, gestión de nodos o ejecución de scripts. La negación (por ejemplo, `-Job/Build`) puede restringir derechos heredados. |

Los derechos de acceso se controlan en múltiples ámbitos:
- **Global**: Se aplica a toda la instancia (por ejemplo, a través de grupos a nivel raíz).
- **Específico del Objeto**: Se anula en trabajos, carpetas o agentes (por ejemplo, un equipo solo puede hacer build en su carpeta).
- **Propagación**: Los roles se heredan automáticamente a los elementos secundarios a menos que estén "fijados" (anulación local) o filtrados (por ejemplo, ocultar un proyecto de un rol).
- **Implicaciones**: Ciertos permisos otorgan automáticamente permisos subordinados (configurable en versiones recientes por seguridad).

Los administradores pueden filtrar roles para evitar la propagación (por ejemplo, a través de **Roles > Filter** en un trabajo) o usar roles no filtrables para forzar el acceso global.

#### Gestión de Roles de Usuario
Los roles son conjuntos predefinidos de permisos:
1. Ir a **Manage Jenkins > Manage Roles**.
2. Hacer clic en **Add Role** y nombrarlo (por ejemplo, "Developer").
3. Asignar permisos marcando casillas (usar "Check all" o "Clear all" para acciones en masa). Los roles del sistema como "anonymous" (para usuarios no autenticados) y "authenticated" (usuarios registrados) están preconstruidos y no se pueden eliminar.
4. Guardar. Los roles se pueden marcar como "non-filterable" para que siempre se apliquen globalmente.

Los usuarios heredan permisos de los roles asignados a sus grupos; no hay asignación directa de roles a usuarios, es basada en grupos para escalabilidad.

#### Asignación de Roles a Grupos y Usuarios
Los grupos agrupan usuarios y roles, permitiendo una delegación fácil:
1. En un objeto (por ejemplo, raíz, carpeta o trabajo), ir a **Groups > New Group**.
2. Ingresar un nombre de grupo (por ejemplo, "DevTeam").
3. Asignar roles marcándolos (se propagan a los elementos secundarios por defecto; desmarcar para fijar localmente).
4. Agregar miembros (ver más abajo).
5. Guardar.

Los grupos admiten anidamiento (por ejemplo, subgrupos) e integración externa (por ejemplo, grupos LDAP).

#### Cómo los Administradores Agregan un Usuario a un Grupo
Los administradores con permiso `Group/Manage` pueden editar las membresías:
1. Navegar a la configuración del grupo (por ejemplo, **Groups** en la raíz o el objeto).
2. En la sección "Members", hacer clic en **Add user** (o **Add group** para grupos externos/anidados).
3. Ingresar el ID de usuario (por ejemplo, nombre de usuario de la base de datos de usuarios de Jenkins, DN de LDAP o nombre de grupo externo). Usar `/whoAmI` para verificar los IDs.
4. Hacer clic en **Add** y guardar. Confirmar la eliminación con un mensaje si es necesario.
5. Para acciones masivas/automatización:
   - Usar CLI: `java -jar jenkins-cli.jar group-membership <object-path> <group-name> <user-id>` (lista/establece miembros).
   - REST API: POST a `/rbac/api/v1/groups/<group>/members` con carga útil JSON.

Evitar membresías de grupo circulares para prevenir bucles. Para entornos externos (por ejemplo, Active Directory), configurar primero el entorno de seguridad en **Manage Security > Security Realm**.

Esta configuración garantiza un control seguro y escalable; por ejemplo, los desarrolladores obtienen `Job/Build` + `Job/Read` en su carpeta, mientras que los administradores manejan todo.

[Restringir el acceso y delegar la administración con Control de Acceso Basado en Roles](https://docs.cloudbees.com/docs/cloudbees-ci/latest/secure/rbac)