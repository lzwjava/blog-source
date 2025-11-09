---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Guía de Gestión de Acceso de AWS IAM
translated: true
type: note
---

AWS Identity and Access Management (IAM) es un servicio gratuito que te ayuda a controlar de forma segura el acceso a los recursos de AWS. Te permite gestionar usuarios y sus permisos, garantizando que las personas y aplicaciones correctas tengan el acceso adecuado a los recursos correctos. IAM maneja la autenticación (quién puede iniciar sesión) y la autorización (qué acciones pueden realizar).

## Componentes principales de IAM

- **Usuarios**: Representan a individuos o aplicaciones que necesitan acceso a AWS. Cada usuario tiene credenciales de seguridad únicas (por ejemplo, contraseñas o claves de acceso).
- **Grupos**: Colecciones de usuarios para una gestión más sencilla de permisos. Los permisos se adjuntan a los grupos, no directamente a usuarios individuales.
- **Roles**: Identidades temporales con permisos que pueden ser asumidas por usuarios, servicios o aplicaciones. Los roles no tienen credenciales permanentes; proporcionan tokens de seguridad de corta duración.
- **Políticas**: Documentos JSON que definen permisos. Especifican acciones (por ejemplo, lectura, escritura), recursos (por ejemplo, buckets de S3) y condiciones (por ejemplo, restricciones de IP). Existen políticas administradas por AWS, administradas por el cliente y políticas en línea.

## Primeros pasos: Guía paso a paso

### Prerrequisitos
- Inicia sesión en la Consola de administración de AWS como usuario root (el correo electrónico y la contraseña de tu cuenta). **Importante**: Evita usar el usuario root para tareas diarias; crea un usuario administrador inmediatamente.
- Habilita la autenticación multifactor (MFA) para el usuario root para mayor seguridad.

### 1. Crear un usuario de IAM
Utiliza la Consola de administración de AWS por simplicidad (las opciones de CLI o API están disponibles para automatización).

1. Abre la consola de IAM en https://console.aws.amazon.com/iam/.
2. En el panel de navegación, elige **Usuarios** > **Crear usuario**.
3. Ingresa un nombre de usuario (por ejemplo, "admin-user") y selecciona **Siguiente**.
4. En **Establecer permisos**, elige **Adjuntar políticas directamente** y selecciona una política administrada por AWS como "AdministratorAccess" para acceso completo (en producción, comienza con el principio de privilegio mínimo).
5. (Opcional) Establece una contraseña de consola: Elige **Contraseña personalizada** y habilita **Requerir restablecimiento de contraseña**.
6. Revisa y elige **Crear usuario**.
7. Proporciona al usuario su URL de inicio de sesión (por ejemplo, https://[alias-de-cuenta].signin.aws.amazon.com/console), nombre de usuario y contraseña temporal.

Para acceso programático, genera claves de acceso (pero prefiere los roles para las aplicaciones).

### 2. Crear y gestionar grupos
Los grupos simplifican la escalabilidad de los permisos.

1. En la consola de IAM, elige **Grupos de usuarios** > **Crear grupo**.
2. Ingresa un nombre para el grupo (por ejemplo, "Developers").
3. Adjunta políticas (por ejemplo, "AmazonEC2ReadOnlyAccess").
4. Elige **Crear grupo**.
5. Para agregar usuarios: Selecciona el grupo > **Agregar usuarios al grupo** > Elige usuarios existentes.

Los usuarios heredan todos los permisos del grupo. Un usuario puede pertenecer a múltiples grupos.

### 3. Crear y adjuntar políticas
Las políticas definen qué acciones están permitidas.

- **Tipos**:
  - Administradas por AWS: Preconstruidas para trabajos comunes (por ejemplo, "ReadOnlyAccess").
  - Administradas por el cliente: JSON personalizado para tus necesidades.
  - En línea: Incrustadas directamente en un usuario/grupo/rol (úsalas con moderación).

Para crear una política personalizada:
1. En la consola de IAM, elige **Políticas** > **Crear política**.
2. Usa el editor visual o la pestaña JSON (por ejemplo, permitir "s3:GetObject" en un bucket específico).
3. Nómbrala y elige **Crear política**.
4. Adjúntala a usuarios/grupos/roles mediante **Adjuntar política**.

Mejor práctica: Otorga el principio de privilegio mínimo—comienza de forma amplia, luego refina usando herramientas como IAM Access Analyzer.

### 4. Usar roles de IAM
Los roles son ideales para acceso temporal, evitando credenciales a largo plazo.

1. En la consola de IAM, elige **Roles** > **Crear rol**.
2. Selecciona la entidad de confianza (por ejemplo, "Servicio de AWS" para EC2, u "Otra cuenta de AWS" para acceso entre cuentas).
3. Adjunta políticas de permisos.
4. Agrega una política de confianza (JSON que define quién puede asumir el rol, por ejemplo, la entidad principal del servicio EC2).
5. Nómbralo y elige **Crear rol**.

**Escenarios comunes**:
- **Instancias de EC2**: Adjunta un rol a una instancia para acceso seguro a otros servicios (por ejemplo, S3) sin incrustar claves.
- **Acceso entre cuentas**: En la Cuenta A (que confía), crea un rol con una política de confianza que permita a entidades principales de la Cuenta B. Los usuarios en B asumen el rol a través de AWS STS para acceder a los recursos de A.

Asume un rol a través de la consola, CLI (`aws sts assume-role`) o SDKs para obtener credenciales temporales.

### 5. Habilitar MFA y seguridad adicional
- Para usuarios: En la consola de IAM > Usuarios > Selecciona usuario > **Credenciales de seguridad** > Administrar MFA.
- Usa dispositivos MFA virtuales (basados en app) o hardware.

## Mejores prácticas para la seguridad
- **Bloquea el Usuario Root**: Úsalo solo para tareas que lo requieran (por ejemplo, cambiar la configuración de la cuenta). Habilita MFA y no crees claves de acceso.
- **Usa Credenciales Temporales**: Prefiere la federación (por ejemplo, a través de IAM Identity Center) y los roles sobre las claves a largo plazo. Rota las claves si se usan.
- **Principio de Privilegio Mínimo**: Otorga permisos mínimos; usa condiciones (por ejemplo, límites de tiempo/IP) en las políticas.
- **Monitorea y Audita**: Habilita AWS CloudTrail, usa IAM Access Analyzer para detectar permisos no utilizados o acceso no intencionado, y revisa la información de último uso.
- **Elimina Recursos No Utilizados**: Elimina regularmente usuarios/roles/políticas inactivos.
- **Para Múltiples Cuentas**: Usa AWS Organizations con políticas de control de servicios (SCPs) como barreras de protección.
- **Valida las Políticas**: Usa las comprobaciones de políticas de IAM Access Analyzer antes de aplicarlas.

Para aprendizaje práctico, explora los tutoriales de IAM en la consola o la documentación para escenarios como el control de acceso basado en atributos (ABAC).

## Referencias
- [¿Qué es IAM?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html)
- [Crear un usuario de IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html)
- [Grupos de IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups.html)
- [Roles de IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)
- [Mejores prácticas de IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
- [Tutoriales de IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorials.html)