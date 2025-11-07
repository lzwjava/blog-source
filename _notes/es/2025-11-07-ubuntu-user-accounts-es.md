---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Creación de Cuentas de Usuario en Ubuntu
translated: true
---

### Crear un nuevo usuario en Ubuntu Linux

Ubuntu proporciona métodos tanto por línea de comandos como gráficos para crear un usuario. El enfoque por línea de comandos es directo y funciona en todas las ediciones (incluyendo servidores), mientras que la interfaz gráfica está disponible en las versiones de escritorio.

#### Método por Línea de Comandos (Recomendado)
1.  Abre una terminal (Ctrl+Alt+T).
2.  Ejecuta el siguiente comando, reemplazando `username` con tu nombre de usuario deseado:
    ```
    sudo adduser username
    ```
    - Esto te pedirá que establezcas una contraseña segura para el nuevo usuario.
    - También se te preguntarán detalles opcionales como nombre completo, número de habitación, teléfono del trabajo, etc. Presiona Enter para omitirlos o proporciona la información según sea necesario.
3.  (Opcional) Para otorgar al nuevo usuario privilegios administrativos (sudo):
    ```
    sudo usermod -aG sudo username
    ```
    - Esto añade el usuario al grupo `sudo`, permitiéndole ejecutar comandos con permisos elevados.

El nuevo usuario tendrá un directorio personal en `/home/username` y podrá iniciar sesión inmediatamente.

#### Método Gráfico (Solo Escritorio)
1.  Abre la aplicación **Configuración** (búscala en la vista general de Actividades).
2.  Navega a **Usuarios** en la barra lateral.
3.  Haz clic en **Desbloquear** en la esquina superior derecha e introduce tu contraseña de administrador.
4.  Haz clic en **Añadir usuario**.
5.  Completa el tipo de cuenta (Estándar o Administrador), nombre completo, nombre de usuario y contraseña.
6.  Haz clic en **Añadir**.

#### Verificación
- Cambia al nuevo usuario con `su - username` o cierra sesión e inicia sesión de nuevo.
- Verifica los usuarios con `cat /etc/passwd | grep username`.

Este proceso funciona en Ubuntu 24.04 LTS y versiones posteriores.

[Gestión de usuarios - Documentación de Ubuntu Server](https://documentation.ubuntu.com/server/how-to/security/user-management/)  
[Añadir una nueva cuenta de usuario - Documentación de Ubuntu](https://help.ubuntu.com/stable/ubuntu-help/user-add.html.en)