---
audio: false
generated: true
lang: es
layout: post
title: Simulación de Flip-Flops en Python
translated: true
type: note
---

Vamos a crear un programa simple en Python para simular el comportamiento de los diferentes tipos de flip-flops (RS, D, JK y T) descritos anteriormente. Dado que los flip-flops son componentes de hardware, modelaremos su lógica en clases de Python para imitar su comportamiento, incluyendo entradas, salidas y cambios de estado. El programa nos permitirá ingresar valores para los controles del flip-flop (como S, R, D, J, K, T y Clock) y mostrar la salida (Q) según sus reglas. Lo mantendremos simple y basado en texto, adecuado para que un principiante lo entienda, con una interfaz de línea de comandos para probar cada flip-flop.

Aquí está el plan:
- Crear una clase base `FlipFlop` para manejar atributos comunes como el estado actual (Q).
- Crear clases específicas para `RSFlipFlop`, `DFlipFlop`, `JKFlipFlop` y `TFlipFlop`, cada una implementando su comportamiento único.
- Simular el reloj requiriendo un "tick" para actualizar el estado, imitando cómo funcionan los flip-flops en pulsos de reloj.
- Proporcionar un bucle interactivo simple para probar cada flip-flop ingresando valores de entrada y viendo la salida.
- Usar declaraciones print para mostrar los cambios de estado, manteniéndolo claro y educativo.

El código no utilizará bibliotecas externas (como pygame) ya que solo estamos simulando lógica, y se ejecutará en un entorno estándar de Python. El artefacto será un script de Python que puedes ejecutar para experimentar con flip-flops.

```python
# Clase base para todos los flip-flops
class FlipFlop:
    def __init__(self):
        self.Q = 0  # Estado actual (salida)
        self.Q_next = 0  # Siguiente estado (a actualizar en el tick del reloj)

    def get_output(self):
        return self.Q

    def tick(self):
        self.Q = self.Q_next  # Actualizar estado en el tick del reloj

# Flip-Flop RS
class RSFlipFlop(FlipFlop):
    def update(self, S, R):
        if S == 1 and R == 1:
            print("Advertencia: Estado inválido (S=1, R=1) - Sin cambio")
            return
        elif S == 1 and R == 0:
            self.Q_next = 1  # Set
        elif S == 0 and R == 1:
            self.Q_next = 0  # Reset
        # Si S=0, R=0, mantener el estado anterior (sin cambio en Q_next)

# Flip-Flop D
class DFlipFlop(FlipFlop):
    def update(self, D):
        self.Q_next = D  # La salida se convertirá en D en el siguiente tick del reloj

# Flip-Flop JK
class JKFlipFlop(FlipFlop):
    def update(self, J, K):
        if J == 0 and K == 0:
            pass  # Sin cambio
        elif J == 0 and K == 1:
            self.Q_next = 0  # Reset
        elif J == 1 and K == 0:
            self.Q_next = 1  # Set
        elif J == 1 and K == 1:
            self.Q_next = 1 - self.Q  # Toggle

# Flip-Flop T
class TFlipFlop(FlipFlop):
    def update(self, T):
        if T == 0:
            pass  # Sin cambio
        elif T == 1:
            self.Q_next = 1 - self.Q  # Toggle

# Función para obtener entrada binaria válida (0 o 1)
def get_binary_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value in [0, 1]:
                return value
            print("Por favor, ingresa 0 o 1.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa 0 o 1.")

# Función principal de simulación
def simulate_flip_flop():
    print("¡Bienvenido al Simulador de Flip-Flops!")
    print("Elige un flip-flop para probar:")
    print("1. Flip-Flop RS")
    print("2. Flip-Flop D")
    print("3. Flip-Flop JK")
    print("4. Flip-Flop T")
    print("5. Salir")

    choice = input("Ingresa tu elección (1-5): ")

    if choice == "5":
        print("¡Hasta luego!")
        return

    if choice == "1":
        ff = RSFlipFlop()
        print("\nFlip-Flop RS: Ingresa S y R (0 o 1).")
        while True:
            S = get_binary_input("Ingresa S: ")
            R = get_binary_input("Ingresa R: ")
            ff.update(S, R)
            ff.tick()
            print(f"Salida Q: {ff.get_output()}")
            if input("¿Continuar? (y/n): ").lower() != 'y':
                break

    elif choice == "2":
        ff = DFlipFlop()
        print("\nFlip-Flop D: Ingresa D (0 o 1).")
        while True:
            D = get_binary_input("Ingresa D: ")
            ff.update(D)
            ff.tick()
            print(f"Salida Q: {ff.get_output()}")
            if input("¿Continuar? (y/n): ").lower() != 'y':
                break

    elif choice == "3":
        ff = JKFlipFlop()
        print("\nFlip-Flop JK: Ingresa J y K (0 o 1).")
        while True:
            J = get_binary_input("Ingresa J: ")
            K = get_binary_input("Ingresa K: ")
            ff.update(J, K)
            ff.tick()
            print(f"Salida Q: {ff.get_output()}")
            if input("¿Continuar? (y/n): ").lower() != 'y':
                break

    elif choice == "4":
        ff = TFlipFlop()
        print("\nFlip-Flop T: Ingresa T (0 o 1).")
        while True:
            T = get_binary_input("Ingresa T: ")
            ff.update(T)
            ff.tick()
            print(f"Salida Q: {ff.get_output()}")
            if input("¿Continuar? (y/n): ").lower() != 'y':
                break

    else:
        print("Elección inválida. Inténtalo de nuevo.")
    
    simulate_flip_flop()  # Reiniciar el menú

# Ejecutar el simulador
if __name__ == "__main__":
    simulate_flip_flop()
```

**Cómo Ejecutar el Código:**
1. Guarda el código en un archivo llamado `flip_flop_simulator.py`.
2. Ejecútalo usando Python (por ejemplo, `python flip_flop_simulator.py`).
3. Sigue las indicaciones para elegir un flip-flop (1-4) o salir (5).
4. Ingresa los valores de entrada (0 o 1) para las entradas del flip-flop seleccionado (por ejemplo, S y R para RS, D para D, etc.).
5. El programa mostrará la salida Q después de cada tick del reloj.
6. Elige si continuar probando el mismo flip-flop o salir al menú.

**Qué Hace:**
- El programa simula el comportamiento de cada tipo de flip-flop como se describió (RS, D, JK, T).
- Por ejemplo, en el Flip-Flop RS, ingresar S=1, R=0 establece Q en 1; ingresar S=1, R=1 advierte sobre el estado inválido.
- El Flip-Flop D copia la entrada D a Q en cada tick.
- El Flip-Flop JK maneja set, reset y toggle basado en J y K.
- El Flip-Flop T alterna Q cuando T=1.
- Es interactivo y se repite para que puedas seguir probando diferentes entradas.

¡Avísame si quieres modificar el código, agregar funciones (como un contador usando flip-flops T) o si tienes preguntas!