---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: TinyGrad Biblioteca de Aprendizaje Automático Ligera
translated: true
type: note
---

### Introducción a TinyGrad
TinyGrad es una biblioteca de aprendizaje automático y aprendizaje profundo en Python, ligera y minimalista, diseñada para la educación y la simplicidad. Implementa diferenciación automática (autograd) como PyTorch, pero es mucho más pequeña—alrededor de 1,000 líneas de código. Es ideal para aprender conceptos de ML o construir modelos pequeños sin la complejidad de bibliotecas más grandes. Soporta tensores, redes neuronales y operaciones básicas, incluyendo aceleración por GPU vía PyTorch o Metal.

Puedes encontrar el repositorio oficial en: [tinygrad GitHub](https://github.com/geohot/tinygrad). Nota: Es experimental y no es tan robusto como PyTorch o TensorFlow para uso en producción.

### Instalación
Instala TinyGrad vía pip:

```bash
pip install tinygrad
```

Tiene dependencias mínimas, pero opcionalmente usa PyTorch para algunos backends. Para soporte de GPU, asegúrate de tener PyTorch instalado.

### Uso Básico
Comienza importando y configurando el contexto (TinyGrad requiere especificar si estás entrenando o haciendo inferencia, ya que los gradientes se calculan de forma diferente).

#### Importación y Contexto
```python
from tinygrad import Tensor
from tinygrad.nn import Linear, BatchNorm2d  # Para redes neuronales

# Configurar contexto: entrenamiento (para gradientes) o inferencia
Tensor.training = True  # Habilitar el seguimiento de gradientes
```

#### Creación y Manipulación de Tensores
Los tensores son la estructura de datos central, similar a los arrays de NumPy o los tensores de PyTorch.

```python
# Crear tensores desde listas, arrays de NumPy o por forma
a = Tensor([1, 2, 3])          # Desde lista
b = Tensor.zeros(3)            # Tensor de ceros de forma (3,)
c = Tensor.rand(2, 3)          # Tensor aleatorio de forma (2, 3)

# Operaciones básicas
d = a + b                      # Suma elemento por elemento
e = d * 2                      # Multiplicación escalar
f = a @ Tensor([[1], [2], [3]])  # Multiplicación de matrices (a es 1D, transpuesta implícitamente)

print(e.numpy())               # Convertir a NumPy para imprimir o usar después
```

#### Diferenciación Automática (Retropropagación)
TinyGrad calcula automáticamente los gradientes usando la regla de la cadena.

```python
# Habilitar el seguimiento de gradientes
Tensor.training = True

x = Tensor([1.0, 2.0, 3.0])
y = (x * 2).sum()             # Alguna operación; y es un escalar

y.backward()                  # Calcular gradientes
print(x.grad.numpy())         # Gradientes con respecto a x: debería ser [2, 2, 2]
```

Para exportar a NumPy, usa `.numpy()`—los gradientes se acumulan a menos que se reinicien.

#### Redes Neuronales y Entrenamiento
TinyGrad incluye capas básicas y optimizadores. Aquí hay un ejemplo simple de MLP:

```python
from tinygrad.nn import Linear, optim

# Definir un modelo simple (por ejemplo, capa lineal)
model = Linear(3, 1)          # Entrada 3, salida 1

# Datos dummy
x = Tensor.rand(4, 3)         # Lote de 4 muestras, 3 características
y_true = Tensor.rand(4, 1)    # Objetivo

# Paso forward
pred = model(x).sigmoid()      # Asumiendo clasificación binaria

# Pérdida (por ejemplo, MSE)
loss = ((pred - y_true) ** 2).mean()

# Retropropagación y optimización
loss.backward()
optim.Adam([model], lr=0.01).step()
```

Para redes de convolución, usa `Conv2d` de `tinygrad.nn`.

### Características Avanzadas
- **Funciones de Pérdida y Activaciones**: Disponibles en `tinygrad.nn` (por ejemplo, `sigmoid`, `relu`, `cross_entropy`).
- **Optimizadores**: `SGD`, `Adam` en `tinygrad.nn.optim`.
- **Capas**: `Linear`, `Conv2d`, `BatchNorm`, etc.
- **Guardar/Cargar**: Los modelos se pueden guardar como diccionarios de estado (similar a PyTorch).
- **GPU/Aceleración**: TinyGrad puede ejecutarse en GPU vía el backend de PyTorch: `TESOR_SET_DEVICE='cuda:0'`. También soporta Metal en macOS.
- **Ejemplos de Visión/Reducción de Ruido**: El repositorio tiene ejemplos como entrenar una ResNet en MNIST.

Para ejemplos completos, revisa la carpeta `examples/` en el repositorio de GitHub, como clasificación de imágenes o aprendizaje por refuerzo.

### Ejemplo: Entrenando una Red Neuronal
Aquí hay un script completo y simple para entrenar una red en XOR:

```python
from tinygrad import Tensor
from tinygrad.nn import Linear, optim

# Datos
X = Tensor([[0,0], [0,1], [1,0], [1,1]])
Y = Tensor([[0], [1], [1], [0]])

# Modelo
model = Linear(2, 1)
opt = optim.Adam([model], lr=0.1)

Tensor.training = True

for epoch in range(1000):
    pred = model(X).sigmoid()
    loss = ((pred - Y) ** 2).mean()
    loss.backward()
    opt.step()
    opt.zero_grad()

# Prueba
print(model(Tensor([[0,0]])))  # Debería ser ~0
```

### Consejos y Advertencias
- **Cambio de Modo**: Siempre configura `Tensor.training = True` para entrenamiento; cambia a `False` para inferencia para evitar el cálculo de gradientes.
- **Manejo de Formas**: Los tensores siguen la transmisión (broadcasting) al estilo NumPy, pero cuidado con los desbordamientos en modelos pequeños.
- **Depuración**: Usa `.numpy()` para inspeccionar valores. Si algo falla, verifica discrepancias en las formas.
- **Rendimiento**: Es lento para modelos grandes—usa PyTorch para producción.
- **Actualizaciones**: TinyGrad evoluciona rápidamente; revisa el repositorio para la versión más reciente.

Para más detalles, visita la [docs/README.md](https://github.com/geohot/tinygrad/blob/master/README.md) o ejecuta los ejemplos localmente. Si tienes un caso de uso específico, ¡proporciona más detalles para un consejo más personalizado!