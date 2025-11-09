---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Guía de SSH y SFTP con Paramiko
translated: true
type: note
---

### Instalación
Paramiko es una librería de Python para SSH y SFTP. Instálala mediante pip:

```bash
pip install paramiko
```

### Uso Básico
Paramiko te permite conectarte a servidores SSH, ejecutar comandos y transferir archivos. Maneja siempre las claves privadas de forma segura y utiliza contraseñas fuertes—Paramiko soporta autenticación por clave y por contraseña.

Conceptos clave:
- **Cliente**: Usa `paramiko.SSHClient()` para establecer una conexión.
- **Transporte**: Para un control de bajo nivel, usa `paramiko.Transport()`.
- Autentica mediante `client.connect()` con el nombre del host, el nombre de usuario y ya sea la contraseña o la clave (por ejemplo, mediante `paramiko.RSAKey.from_private_key_file()`).

### Ejemplo: Conectarse y Ejecutar un Comando
Aquí tienes un script completo para conectarse a un servidor SSH, ejecutar un comando e imprimir la salida. Reemplaza los marcadores de posición con tus datos.

```python
import paramiko

# Crear cliente SSH
client = paramiko.SSHClient()

# Añadir automáticamente la clave del host (ten cuidado en producción; carga known_hosts en su lugar)
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Conectar (usar contraseña o archivo de clave)
    client.connect(
        hostname='your.server.com',
        port=22,  # Puerto SSH por defecto
        username='your_username',
        password='your_password',  # O key_filename='ruta/a/clave_privada.pem'
    )

    # Ejecutar un comando
    stdin, stdout, stderr = client.exec_command('echo "Hello from SSH!"')

    # Leer la salida
    output = stdout.read().decode('utf-8')
    error = stderr.read().decode('utf-8')

    print("Salida:", output)
    print("Error:", error)

except paramiko.SSHException as e:
    print(f"Error SSH: {e}")
finally:
    client.close()
```

### Ejemplo Avanzado: Usar Autenticación Basada en Claves y Transferencia de Archivos
Para autenticación por clave, genera un par de claves si es necesario (por ejemplo, con `ssh-keygen`), añade la clave pública a `~/.ssh/authorized_keys` en el servidor, y luego usa:

```python
import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Conexión basada en clave
    client.connect(
        hostname='your.server.com',
        username='your_username',
        key_filename='~/.ssh/id_rsa',  # Ruta a la clave privada
    )

    # Ejecutar comando
    stdin, stdout, stderr = client.exec_command('ls -la')
    print(stdout.read().decode('utf-8'))

    # Ejemplo de SFTP: transferir archivo
    sftp = client.open_sftp()
    sftp.put('archivo_local.txt', 'archivo_remoto.txt')  # Subir
    sftp.get('archivo_remoto.txt', 'copia_local.txt')  # Descargar
    sftp.close()

except Exception as e:
    print(f"Error: {e}")
finally:
    client.close()
```

### Consejos y Buenas Prácticas
- **Seguridad**: Prefiere la autenticación por clave sobre las contraseñas. Deshabilita `AutoAddPolicy` en producción y verifica las claves del host mediante `client.load_host_keys()`.
- **Manejo de Errores**: Captura siempre `paramiko.SSHException` y verifica los códigos de salida con `exit_status = stdout.channel.recv_exit_status()`.
- **Hilos**: Paramiko no es seguro para hilos por defecto; usa bloqueos si es necesario.
- **Documentación**: Para más información, consulta la [documentación oficial de Paramiko](https://docs.paramiko.org/). Prueba con herramientas como `sshd` de OpenSSH o máquinas virtuales locales.

¡Esto debería servirte para empezar; adáptalo a tus necesidades