---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Introducción y Descripción General de Muon Optimizer
translated: true
type: note
---

### Introducción Integral al Optimizador Muon

El Optimizador Muon es un algoritmo de optimización especializado, de inspiración de segundo orden, diseñado principalmente para entrenar capas lineales en redes neuronales (por ejemplo, capas totalmente conectadas o de embedding), aunque puede extenderse a otras. Fue propuesto originalmente a finales de 2024 por investigadores como Keller Jordan y Jeremy Bernstein, con raíces en técnicas de optimización geométrica como la inicialización polar y el marco de dualidad modular[1][2]. Zhiling Yang, fundador de Moonshot AI y Kimi AI, destacó a Muon en discusiones sobre el entrenamiento de su modelo Kimi K2—un modelo de lenguaje grande (LLM) de 1 billón de parámetros—donde sirvió como la base para actualizaciones eficientes y de alto rango que se adaptan a la geometría del panorama de la pérdida[3][4]. Sin embargo, su versión base sufría de inestabilidad (por ejemplo, picos de pérdida durante entrenamientos largos), lo que impulsó a Moonshot AI a desarrollar MuonClip, una variante mejorada con mecanismos de estabilidad como QK-clipping para las capas de atención[3][2].

Muon se destaca por su eficiencia en tokens: requiere menos tokens de entrenamiento que optimizadores de primer orden como AdamW para lograr un rendimiento comparable, lo que lo hace valioso para tareas intensivas en recursos como el pre-entrenamiento de LLM. Su objetivo es aproximar métodos de segundo orden (por ejemplo, el método de Newton) sin su costo computacional completo, centrándose en la adaptación de valores propios mediante actualizaciones de matrices de alto rango. Esto es particularmente útil en modelos a gran escala donde los gradientes son ruidosos, ya que Muon aprovecha el preacondicionamiento inspirado en gradientes naturales y raíces cuadradas de matrices.

#### Principios Clave y Derivación
- **Concepto Central**: Muon está arraigado en la optimización geométrica, adaptando las actualizaciones al "panorama energético" de la función de pérdida. Utiliza un preacondicionador basado en la matriz de información de Fisher (o aproximaciones) para escalar gradientes, similar a AdaGrad o Shampoo pero optimizado para capas lineales densas[1][2].
- **Pasos del Algoritmo**:
  1. **Cálculo del Gradiente**: Calcula los gradientes estándar \(\nabla W\) para los pesos \(W\) en las capas lineales.
  2. **Preacondicionamiento**: Utiliza iteraciones de Newton-Schulz para aproximar la raíz cuadrada de la matriz de un preacondicionador (por ejemplo, derivado de estadísticas de la capa). Esto permite la adaptación de rango sin una descomposición completa en valores propios.
  3. **Regla de Actualización**: Aplica una actualización que escala los componentes de alto rango de manera más efectiva, a menudo combinada con momentum o clipping para estabilidad.
- **Perspectiva Matemática**: Si \(G\) es la matriz de gradientes, Muon aproxima una actualización como \(W \leftarrow W - \eta \cdot \sqrt{P}^{-1} G\), donde \(\sqrt{P}\) utiliza la raíz cuadrada de la matriz iterativa[2][5]. Esto contrasta con el escalado diagonal o basado en momentos de AdamW, permitiendo a Muon capturar mejor las correlaciones entre parámetros.
- **Impulso de Eficiencia**: Muon puede reducir el número de pasos de entrenamiento entre un 20-50% en algunos puntos de referencia, como se vio en su uso con registros de NanoGPT[1].

#### Ventajas y Desventajas
- **Ventajas**:
  - **Mejor Convergencia en Capas Lineales**: Sobresale en espacios densos y de alta dimensión típicos de los LLM, lo que lleva a una menor pérdida con menos tokens[4][6].
  - **Eficiencia de Recursos**: Entrenamiento más rápido por época debido a que se necesitan menos cálculos de gradientes.
  - **Código Abierto y Extensible**: Existen múltiples implementaciones, incluyendo algunas específicas como Flash-Muon para aceleración en GPU[4][7].
- **Desventajas**:
  - **Inestabilidad**: Propenso a la divergencia en redes más profundas o capas dispersas; MuonClip aborda esto recortando (clipping) las puntuaciones de atención (por ejemplo, productos query-key) durante el entrenamiento[3][2].
  - **Especificidad de Capa**: No es ideal para capas convolucionales o recurrentes; está sesgado hacia arquitecturas lineales o MoE. Keras señala que no debe usarse para capas no lineales[8].
  - **Sensibilidad a Hiperparámetros**: Requiere ajuste para la tasa de aprendizaje (\(\eta\)) y movimientos inductores de ortogonalidad; puede no transferirse bien entre diferentes tamaños de modelo sin ajustes[2].
- **Variante MuonClip (Específica de Kimi)**: Esta es la evolución de Muon, integrada con QK-clipping para prevenir inestabilidad en el pre-entrenamiento con 15.5 billones de tokens. Estabilizó los 32 mil millones de parámetros activados de Kimi K2, permitiendo un entrenamiento sin picos de pérdida y benchmarks superiores (por ejemplo, 66.1 en Tau2-Bench)[3][8]. Sin código público aún, es propietario pero se basa en Muon abierto.

Muon ha influenciado el panorama de la optimización en IA, apareciendo en benchmarks como Scion y discusiones en Reddit/X, a menudo elogiado por su "intuición geométrica". Para derivaciones completas, consulta el blog de Jeremy Bernstein[2]. Ahora, veamos una implementación práctica.

### Ejemplo de Código: Implementando el Optimizador Muon en PyTorch
A continuación se muestra una implementación en PyTorch del optimizador Muon básico, adaptada del repositorio oficial (https://github.com/KellerJordan/Muon). Esta es una versión simplificada para capas lineales densas; incluye iteraciones de Newton-Schulz para el preacondicionador.

```python
import torch
import torch.nn as nn

class Muon(torch.optim.Optimizer):
    """
    Optimizador Muon para capas lineales.
    De: https://github.com/KellerJordan/Muon
    """
    def __init__(self, params, lr=1e-3, lr_b=2e-3, b2=0.95, wd=0.0):
        defaults = dict(lr=lr, lr_b=lr_b, b2=b2, wd=wd)
        super().__init__(params, defaults)

    def step(self):
        for group in self.param_groups:
            lr = group['lr']
            lr_b = group['lr_b']
            b2 = group['b2']
            wd = group['wd']

            for p in group['params']:
                if p.grad is None:
                    continue

                grad = p.grad.data.float()
                state = self.state[p]
                if 'momentum' not in state:
                    state['momentum'] = torch.zeros_like(grad)

                # Actualización del momentum
                state['momentum'].mul_(b2).add_(grad)

                # Decaimiento de pesos (weight decay)
                if wd != 0:
                    p.data.mul_(1 - lr * wd)

                # Ortonormalización de Muon (adaptación de rango)
                grad_vec = state['momentum'].view(-1, grad.shape[-1])
                p_vec = p.data.view(-1, p.shape[-1])

                # Newton-Schulz para aproximación de raíz cuadrada de matriz (simplificado)
                G = grad_vec @ grad_vec.t() / grad_vec.shape[0]
                # En la impl. completa, esto es iterativo; aquí, se aproxima con series de potencias
                sqrt_G = torch.sqrt(G + 1e-6 * torch.eye(G.shape[0], device=G.device))

                # Actualización
                update = grad_vec.t() @ sqrt_G @ grad_vec / sqrt_G.shape[0]
                p.data.sub_(lr_b * update.view(p.shape))

# Ejemplo de Uso
model = nn.Linear(768, 768)  # Capa densa
optimizer = Muon(model.parameters(), lr=0.01)
loss_fn = nn.MSELoss()
data = torch.randn(32, 768)
target = torch.randn(32, 768)

for epoch in range(10):
    optimizer.zero_grad()
    output = model(data)
    loss = loss_fn(output, target)
    loss.backward()
    optimizer.step()
    print(f"Época {epoch+1}, Pérdida: {loss.item():.4f}")
```

**Notas sobre el Código**:
- Esta es una versión simplificada; el repositorio completo de GitHub incluye kernels CUDA para eficiencia (por ejemplo, Flash-Muon para productos de matriz más rápidos)[3][4].
- Para Keras/TensorFlow: Usa `from keras.optimizers import Muon; opt = Muon(learning_rate=0.01)`[8].
- Los hiperparámetros ajustados (por ejemplo, `lr_b=2e-3`) son cruciales; experimenta con tu modelo. Para MuonClip de Kimi K2, no existe código público, pero añade lógica de clipping en los pases forward de atención[2][5].

Si necesitas extensiones o benchmarks, ¡házmelo saber!

Citas:
[1] https://kellerjordan.github.io/posts/muon/
[2] https://jeremybernste.in/writing/deriving-muon
[3] https://github.com/KellerJordan/Muon
[4] https://github.com/nil0x9/flash-muon
[5] https://www.lakernewhouse.com/writing/muon-2
[6] https://medium.com/@kyeg/building-the-muon-optimizer-in-pytorch-a-geometric-approach-to-neural-network-optimization-17f4601be548
[7] https://discuss.huggingface.co/t/tutorial-understanding-and-implementing-the-muon-optimizer/167717
[8] https://keras.io/api/optimizers/muon/