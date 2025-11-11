---
audio: false
generated: true
lang: es
layout: post
title: Solución para Arreglar que DBeaver No Cargue los Esquemas
translated: true
type: note
---

Si puedes ver esquemas en una base de datos IBM DB2 usando Squirrel SQL en Windows pero DBeaver se queda atascado en "cargando elemento 0%", el problema probablemente se deba a cómo DBeaver recupera los metadatos en comparación con Squirrel SQL. A continuación, se presenta una guía paso a paso para solucionar y resolver este problema:

---

#### 1. Verificar el Controlador DB2 en DBeaver
DBeaver requiere el controlador correcto para conectarse a tu base de datos IBM DB2. Usar el controlador incorrecto (por ejemplo, "Db2 for LUW" vs. "Db2 for z/OS") puede causar problemas con la carga de esquemas.

- **Pasos**:
  1. Abre DBeaver y haz clic derecho en tu conexión DB2 en el Navegador de Bases de Datos.
  2. Selecciona **Editar Conexión**.
  3. En la sección "Controlador", confirma que el controlador seleccionado coincida con tu entorno DB2 (por ejemplo, "Db2 for LUW" para Linux/Unix/Windows o "Db2 for z/OS" para mainframe).
  4. Si no estás seguro, consulta con tu administrador de bases de datos o la documentación para asegurarte de que se selecciona el controlador correcto.
  5. Haz clic en **Probar Conexión** para verificar que funciona.

---

#### 2. Ajustar la Propiedad "Metadata Source"
DBeaver utiliza una propiedad llamada "metadata source" para controlar cómo recupera la información de esquemas y tablas. Para DB2, ajustar esta configuración puede resolver los problemas de carga de esquemas.

- **Pasos**:
  1. Abre la configuración de tu conexión DB2 en DBeaver (haz clic derecho en la conexión > **Editar Conexión**).
  2. Ve a la pestaña **Propiedades del Controlador**.
  3. Encuentra la propiedad "metadata source" (o agrégalo si no está en la lista).
  4. Establece su valor en `0`.
  5. Haz clic en **Aceptar** para guardar los cambios.
  6. Vuelve a conectarte a la base de datos y comprueba si los esquemas se cargan.

- **Por qué funciona esto**: Establecer "metadata source" en `0` simplifica la forma en que DBeaver obtiene los metadatos, lo que puede evitar problemas específicos de la recuperación de esquemas en DB2.

---

#### 3. Verificar los Permisos de Usuario
Aunque Squirrel SQL muestra los esquemas, DBeaver podría consultar la base de datos de manera diferente, requiriendo permisos específicos para acceder a los metadatos.

- **Pasos**:
  1. Confirma con tu administrador de bases de datos que tu cuenta de usuario tiene privilegios para ver esquemas y metadatos en DB2 (por ejemplo, `SELECT` en las tablas del catálogo del sistema como `SYSCAT.SCHEMATA`).
  2. Si los permisos son insuficientes, pide a tu DBA que otorgue los derechos necesarios.
  3. Prueba la conexión nuevamente en DBeaver.

---

#### 4. Descartar Problemas de Red o Firewall
Una restricción de red o un firewall podría impedir que DBeaver recupere completamente los datos del esquema, incluso si Squirrel SQL funciona.

- **Pasos**:
  1. Asegúrate de que el servidor DB2 sea accesible desde tu máquina Windows (por ejemplo, haz ping al servidor o prueba el puerto).
  2. Consulta con tu equipo de red para confirmar que no hay reglas de firewall que bloqueen la conexión de DBeaver.
  3. Si es posible, prueba DBeaver desde una máquina diferente para aislar el problema.

---

#### 5. Actualizar DBeaver a la Última Versión
Las versiones antiguas de DBeaver pueden tener errores que afecten la carga de esquemas de DB2.

- **Pasos**:
  1. En DBeaver, ve a **Ayuda** > **Buscar Actualizaciones**.
  2. Instala cualquier actualización disponible.
  3. Reinicia DBeaver y vuelve a conectarte a la base de datos.

- **Alternativa**: Descarga la última versión desde el [sitio web de DBeaver](https://dbeaver.io/) y reinstala si no hay actualizaciones disponibles.

---

#### 6. Habilitar el Registro de Depuración para una Solución de Problemas Adicional
Si los pasos anteriores no resuelven el problema, habilita el registro de depuración para identificar errores específicos durante la carga del esquema.

- **Pasos**:
  1. Ve a **Ventana** > **Preferencias** > **DBeaver** > **Registro**.
  2. Habilita el registro detallado y guarda la configuración.
  3. Vuelve a conectarte a la base de datos e intenta cargar los esquemas.
  4. Revisa los archivos de registro (generalmente en la carpeta del espacio de trabajo de DBeaver) en busca de mensajes de error relacionados con la recuperación de esquemas de DB2.
  5. Si es necesario, comparte los registros con el soporte de DBeaver o en un foro para obtener más ayuda.

---

### Por Qué Ocurre Esto
- **DBeaver vs. Squirrel SQL**: DBeaver es una herramienta con más funciones y recupera metadatos adicionales en comparación con el enfoque más simple de Squirrel SQL. Esto puede generar problemas de compatibilidad con DB2 si la configuración no está optimizada.
- **Solución Común**: Ajustar "metadata source" a `0` es una solución conocida para los problemas de carga de esquemas de DB2 en DBeaver.

---

### Próximos Pasos
Comienza con los pasos 1 y 2 (verificación del controlador y ajuste de "metadata source"), ya que son las soluciones más probables. Si el problema persiste, procede con los pasos restantes. Si ninguno funciona, considera publicar tus registros de depuración en la [comunidad de DBeaver](https://github.com/dbeaver/dbeaver/issues) para obtener ayuda adicional.

¡Esto debería resolver el problema de "cargando elemento 0%" y permitirte ver los esquemas en DBeaver como lo haces en Squirrel SQL!