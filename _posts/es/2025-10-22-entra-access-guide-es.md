---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Guía de Administración de Acceso de Microsoft Entra ID
translated: true
type: note
---

Microsoft Entra ID es un servicio de gestión de identidades y acceso basado en la nube que ayuda a proteger el acceso a recursos como aplicaciones, datos y dispositivos. Admite autenticación (por ejemplo, métodos de inicio de sesión, MFA), autorización (por ejemplo, acceso basado en roles) e integración con servicios de Azure. Para comenzar, necesitará una suscripción a Azure y permisos apropiados (por ejemplo, el rol de Administrador global).

## Comenzar
1. **Iniciar sesión en Azure Portal**: Vaya a [portal.azure.com](https://portal.azure.com) e inicie sesión con su cuenta de Microsoft.
2. **Navegar a Microsoft Entra ID**: Busque "Microsoft Entra ID" en la barra de búsqueda superior o encuéntrelo en "Servicios de Azure".
3. **Explorar el Panel**: Revise la información general de su inquilino, incluyendo usuarios, grupos y aplicaciones. Configure aspectos básicos como dominios personalizados si es necesario.
4. **Habilitar Características Clave**:
   - **Autenticación**: Configure el restablecimiento de contraseña de autoservicio o la autenticación multifactor (MFA) en "Métodos de autenticación".
   - **Acceso condicional**: Cree políticas en "Seguridad" > "Acceso condicional" para aplicar reglas basadas en el usuario, dispositivo o ubicación.

## Gestión de Usuarios y Grupos
- **Agregar Usuarios**: Vaya a "Usuarios" > "Nuevo usuario". Ingrese detalles como nombre, nombre de usuario (por ejemplo, usuario@sudominio.com) y asigne roles o licencias.
- **Crear Grupos**: En "Grupos" > "Nuevo grupo", elija el tipo de seguridad o Microsoft 365, agregue miembros y utilícelo para asignaciones de acceso.
- **Asignar Licencias**: En los detalles del usuario/grupo, vaya a "Licencias" para asignar Entra ID P1/P2 para características avanzadas como Privileged Identity Management (PIM).
- **Mejor Práctica**: Siga el principio de privilegio mínimo—asigne permisos mínimos y utilice grupos para la gestión masiva.

## Gestión de Aplicaciones
- **Registrar una Aplicación**: En "Registros de aplicaciones" > "Nuevo registro", proporcione el nombre, URI de redirección y tipos de cuenta admitidos (inquilino único, multiinquilino, etc.).
- **Agregar Aplicaciones Empresariales**: Para aplicaciones de terceros, vaya a "Aplicaciones empresariales" > "Nueva aplicación" para explorar la galería o crear aplicaciones que no están en la galería.
- **Configurar Acceso**: Asigne usuarios/grupos a la aplicación en "Usuarios y grupos", y configure el inicio de sesión único (SSO) mediante SAML u OAuth.
- **Aprovisionar Identidades**: Automatice la sincronización de usuarios con las aplicaciones en "Aprovisionamiento" para acceso justo a tiempo.

Para configuraciones híbridas (AD local), use Microsoft Entra Connect para sincronizar identidades. Monitoree el uso mediante los registros en "Supervisión" > "Registros de inicio de sesión".

# Cómo Verificar el Acceso a una Base de Datos, Kubernetes (AKS) u Otro Recurso

El acceso en Azure se gestiona mediante el Control de acceso basado en roles (RBAC), integrado con Entra ID. Los usuarios se autentican con las credenciales de Entra, y los roles definen los permisos. Para verificar el acceso, use las herramientas IAM (Identity and Access Management) de Azure Portal. Esto enumera las asignaciones directas, heredadas de ámbitos principales (por ejemplo, suscripción) y las asignaciones de denegación.

## Pasos Generales para Cualquier Recurso de Azure
1. **Abrir el Recurso**: En Azure Portal, navegue hasta el recurso (por ejemplo, grupo de recursos, VM, cuenta de almacenamiento).
2. **Ir a Control de acceso (IAM)**: Seleccione "Control de acceso (IAM)" en el menú de la izquierda.
3. **Verificar Acceso**:
   - Para su propio acceso: Haga clic en "Verificar acceso" > "Ver mi acceso" para ver las asignaciones en este ámbito y las heredadas.
   - Para un usuario/grupo/entidad de servicio específico:
     - Haga clic en "Verificar acceso" > "Verificar acceso".
     - Seleccione "Usuario, grupo o entidad de servicio".
     - Busque por nombre o correo electrónico.
     - Vea el panel de resultados para las asignaciones de roles (por ejemplo, Propietario, Colaborador) y los permisos efectivos.
4. **Ver Asignaciones Elegibles** (si usa PIM): Cambie a la pestaña "Asignaciones elegibles" para roles justo a tiempo.
5. **Alternativa con PowerShell/CLI**: Use `az role assignment list --assignee <usuario> --scope <id-del-recurso>` para verificaciones mediante scripts.

Nota: Esto no incluye las asignaciones de ámbitos secundarios; profundice si es necesario.

## Verificar el Acceso a Azure SQL Database
Azure SQL utiliza la autenticación de Entra para usuarios de base de datos contenidos (vinculados a identidades de Entra, no a inicios de sesión de SQL).
1. **Configurar Administrador de Entra (si no está establecido)**: En la información general del servidor SQL > "Microsoft Entra ID" en Configuración > "Establecer administrador". Busque y seleccione un usuario/grupo, luego guarde. Esto habilita la autenticación de Entra en todo el clúster.
2. **Verificar Acceso a Nivel de Servidor**:
   - En el panel del servidor SQL > "Microsoft Entra ID", vea el campo de administrador para ver la identidad asignada.
   - Consulte la base de datos `master`: `SELECT name, type_desc FROM sys.database_principals WHERE type IN ('E', 'X');` (E para usuarios externos, X para grupos externos).
3. **Verificar Acceso a Nivel de Base de Datos**:
   - Conéctese a la base de datos usando SSMS con autenticación de Entra (seleccione "Microsoft Entra - Universal con MFA" en el diálogo de conexión).
   - Ejecute `SELECT * FROM sys.database_principals;` o `EXEC sp_helprolemember;` para listar usuarios y roles.
4. **Solución de Problemas**: Si el inicio de sesión falla (por ejemplo, error 33134), verifique que las políticas de Acceso Condicional de Entra permitan el acceso a Microsoft Graph API.

Los usuarios obtienen `CONNECT` por defecto; otorgue roles como `db_datareader` mediante T-SQL: `ALTER ROLE db_datareader ADD MEMBER [usuario@dominio.com];`.

## Verificar el Acceso a AKS (Clúster de Kubernetes)
AKS integra Entra ID para la autenticación y utiliza Azure RBAC o Kubernetes RBAC para la autorización.
1. **Acceso a Nivel de Azure (al Recurso AKS)**:
   - Siga los pasos generales anteriores en el recurso del clúster AKS.
   - Roles comunes: "Administrador del clúster de Azure Kubernetes Service" para acceso completo a kubeconfig; "Lector" para solo lectura.
2. **Acceso a la API de Kubernetes**:
   - Autentíquese mediante `az login` (utiliza token de Entra).
   - Obtenga kubeconfig: `az aks get-credentials --resource-group <grupo-de-recursos> --name <clúster>`.
   - Verifique enlaces: `kubectl auth can-i <verbo> <recurso> --as <usuario@dominio.com> -n <espacio-de-nombres>`.
   - Enumere los roles del clúster: `kubectl get clusterrolebindings | grep <usuario-o-grupo>`.
3. **Usando Grupos de Entra**: Asigne Roles/Enlaces de Kubernetes a grupos para escalabilidad. YAML de ejemplo para un rol de espacio de nombres (aplique con `kubectl apply -f archivo.yaml`):
   ```
   apiVersion: rbac.authorization.k8s.io/v1
   kind: RoleBinding
   metadata:
     name: example-binding
     namespace: default
   subjects:
   - kind: Group
     name: finance-group  # Grupo de Entra
     apiGroup: rbac.authorization.k8s.io
   roleRef:
     kind: Role
     name: example-role
     apiGroup: rbac.authorization.k8s.io
   ```
4. **Mejores Prácticas**: Use roles de privilegio mínimo, integre con PIM para elevación justo a tiempo y evite credenciales fijas—use identidades de carga de trabajo para los pods.

Para pods que acceden a recursos (por ejemplo, SQL desde AKS), asigne identidades administradas y verifique mediante Azure RBAC en esas identidades.

[Documentación de Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/)  
[Verificar el Acceso a un Único Recurso de Azure](https://learn.microsoft.com/en-us/azure/role-based-access-control/check-access)  
[Configurar la Autenticación de Entra para Azure SQL](https://learn.microsoft.com/en-us/azure/azure-sql/database/authentication-aad-configure?view=azuresql)  
[Mejores Prácticas de Identidad y Acceso para AKS](https://learn.microsoft.com/en-us/azure/aks/operator-best-practices-identity)