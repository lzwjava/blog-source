---
audio: false
generated: true
image: false
lang: es
layout: post
title: Guía de RBAC de Jenkins con el Complemento de Roles
translated: true
type: note
---

En Jenkins, el **control de acceso basado en roles (RBAC)** se trata de definir quién puede hacer qué y dónde. Por defecto, Jenkins solo tiene un modelo básico de usuario/administrador, pero con el **plugin Role-Based Strategy** (o estrategias de autorización similares) puedes definir un acceso granular.

---

### Conceptos Básicos del RBAC en Jenkins

1. **Roles Globales**
   Estos se aplican a toda la instancia de Jenkins. Ejemplos:

   * **Admin**: control total.
   * **Solo lectura**: puede ver jobs pero no ejecutarlos.
   * **Developer**: puede crear y configurar jobs.

2. **Roles de Proyecto/Job**
   Puedes otorgar permisos por job o por carpeta. Por ejemplo:

   * El Usuario A puede construir *Proyecto X* pero no ver *Proyecto Y*.
   * Los contratistas pueden activar builds pero no pueden cambiar configuraciones.

3. **Permisos de Build**
   Los permisos se pueden dividir:

   * `Job/Read` (ver la definición del job y el historial de builds)
   * `Job/Build` (activar builds)
   * `Job/Configure` (cambiar el pipeline o la configuración)
   * `Job/Delete` (eliminar jobs o builds)
   * `Job/Cancel` (abortar builds en ejecución)

---

### Cómo Gestionar los Derechos de Acceso a Jobs o Builds

1. **Instalar el Plugin Role-Based Strategy**

   * Ve a **Manage Jenkins → Plugins → Available Plugins → Role-based Authorization Strategy**.
   * Después de la instalación, selecciónalo en **Manage Jenkins → Configure Global Security → Authorization**.

2. **Definir Roles**

   * Ve a **Manage Jenkins → Manage and Assign Roles**.
   * Crea roles globales (como *admin*, *viewer*, *developer*) y roles de proyecto (como *projectX-builder*).
   * Asigna a cada rol los permisos necesarios (`Job/Build`, `Job/Configure`, etc.).

3. **Asignar Roles a Usuarios/Grupos**

   * Todavía en **Manage and Assign Roles**, asigna tus usuarios de Jenkins (o grupos LDAP si está integrado) a los roles.
   * Por ejemplo:

     * Asignar *alice* → `developer`
     * Asignar *bob* → `viewer`
     * Asignar *qa-team* → `projectX-builder`

4. **Usar Carpetas para una Mejor Granularidad**

   * Organiza los jobs en **Carpetas** (a través del *Folders Plugin*).
   * Aplica restricciones de roles a nivel de carpeta para que solo el equipo correcto pueda ver/construir/modificar los jobs dentro.

---

### Escenarios de Ejemplo

* **Developers**: Pueden construir y configurar los jobs de su equipo, pero no pueden tocar la configuración de administrador.
* **QA Team**: Solo pueden activar builds (no reconfigurar pipelines).
* **External Users**: Pueden ver el estado del job pero no modificarlo o activar builds.

---

👉 En la práctica: mantienes **pocos administradores**, das a los **developers acceso de configuración y construcción** a sus propios jobs, y otorgas **derechos de solo lectura o solo construcción** a otros. Esto asegura consistencia, reduce errores y mantiene protegidos los jobs sensibles.

---

¿Quieres que te muestre una **configuración de ejemplo paso a paso** (con roles, permisos y mapeo de jobs) que se ajuste a una configuración empresarial típica?