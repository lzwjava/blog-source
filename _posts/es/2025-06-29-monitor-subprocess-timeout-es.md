---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Monitorear la Salida de Subprocesos con Tiempo de Espera
translated: true
type: note
---

```python
import subprocess
import threading
import queue
import time
import sys

def read_output(proc, output_queue):
    """Función del hilo para leer stdout y stderr, poner en cola."""
    try:
        for line in iter(proc.stdout.readline, b''):
            if not line:
                break
            output_queue.put(line.decode('utf-8', errors='ignore').rstrip())
        # También verificar stderr si es necesario
        for line in iter(proc.stderr.readline, b''):
            if not line:
                break
            output_queue.put(line.decode('utf-8', errors='ignore').rstrip())
    except Exception as e:
        output_queue.put(f"Error leyendo salida: {e}")

def main():
    # Comando a ejecutar (ej. 'mvn clean compile' en Windows)
    cmd = ['mvn', 'clean', 'compile']  # Ajustar según sea necesario, ej. ['cmd', '/c', 'mvn build']
    timeout_seconds = 10

    # Iniciar el subproceso
    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        bufsize=1,  # Búfer por línea
        universal_newlines=False,  # Manejar bytes
        cwd=None  # Establecer directorio de trabajo si es necesario
    )

    # Cola para la salida
    output_queue = queue.Queue()

    # Iniciar hilo para leer la salida
    output_thread = threading.Thread(target=read_output, args=(proc, output_queue))
    output_thread.daemon = True
    output_thread.start()

    print("Comando iniciado. Monitoreando la salida cada 10 segundos...")

    while proc.poll() is None:
        try:
            # Esperar por salida con timeout
            output = output_queue.get(timeout=timeout_seconds)
            print(f"Salida: {output}")  # Opcional: imprimir o procesar salida
        except queue.Empty:
            print(f"Sin salida por {timeout_seconds} segundos. Terminando comando y saliendo.")
            proc.terminate()  # o proc.kill() para terminación forzosa
            try:
                proc.wait(timeout=5)  # Esperar un poco para cierre graceful
            except subprocess.TimeoutExpired:
                proc.kill()
            sys.exit(1)

    # El proceso ha terminado normalmente
    print("Comando completado.")
    output_thread.join()  # Esperar a que el hilo de salida termine

if __name__ == "__main__":
    main()
```

### Explicación
- **Subproceso**: Usa `subprocess.Popen` para ejecutar `mvn clean compile` (ajustar el comando según sea necesario; para un simple `mvn build`, podría ser `['mvn', 'build']` o envuelto en `cmd /c` si es necesario). Se ejecuta de forma asíncrona con pipes para stdout y stderr.
- **Hilos y Colas**: Un hilo separado lee de stdout y stderr línea por línea (para evitar leer toda la salida de una vez), la decodifica y pone las líneas en una `queue.Queue`. Esto permite lecturas no bloqueantes.
- **Monitoreo de Timeout**: En el hilo principal, verificar la cola para nueva salida con `get(timeout=10)`. Si no llega salida en 10 segundos, terminar el subproceso y salir.
- **Compatibilidad con Windows**: `subprocess` funciona en Windows. Si el comando requiere un shell (ej. para `mvn` si no está en PATH), se podría establecer `shell=True` y pasar el comando como string: `proc = subprocess.Popen("mvn clean compile", shell=True, ...)`.
- **Casos Extremos**: Si el proceso termina normalmente mientras se espera, el bucle se detiene y hacemos join del hilo. El hilo es daemónico para evitar bloqueos al salir.
- **Personalización**: Se puede modificar para procesar las salidas de manera diferente (ej. registrar en archivo en lugar de imprimir). Para stderr, se combina en la misma cola; se podría separar si es necesario. Si las salidas son binarias, ajustar la decodificación.