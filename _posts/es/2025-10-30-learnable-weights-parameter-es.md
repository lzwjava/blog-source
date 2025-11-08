---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Parámetro de PyTorch para Pesos Aprendibles
translated: true
type: note
---

`torch.nn.Parameter` es una subclase de `torch.Tensor` en PyTorch, diseñada específicamente para representar parámetros aprendibles en módulos de redes neuronales. Su propósito principal es registrar automáticamente los tensores como parámetros del módulo cuando se asignan como atributos a un `torch.nn.Module`, haciéndolos accesibles mediante métodos como `module.parameters()` o `module.named_parameters()`. Esto ayuda a distinguir los pesos entrenables (por ejemplo, para capas) de los tensores regulares, evitando que cálculos temporales (como estados en caché en RNNs) sean tratados erróneamente como parámetros.

### Características Clave
- **Registro Automático**: Cuando asignas un `Parameter` a un módulo (por ejemplo, `self.weight = nn.Parameter(torch.randn(3, 3))` en el `__init__` de un módulo personalizado), se añade a la lista de parámetros del módulo sin código adicional.
- **Seguimiento de Gradientes**: Por defecto, `requires_grad=True`, por lo que participa en la retropropagación. Esto se mantiene incluso dentro de un contexto `torch.no_grad()`—usa la desactivación local de autograd para un control más fino.
- **Atributos**: Hereda todas las propiedades de `Tensor` pero no añade ninguna nueva más allá de su comportamiento especial con los módulos.

### Uso Básico
Aquí hay un ejemplo simple en un módulo personalizado:

```python
import torch
import torch.nn as nn

class MyModule(nn.Module):
    def __init__(self):
        super().__init__()
        # Esto se registra automáticamente como un parámetro
        self.weight = nn.Parameter(torch.randn(2, 3))
        # Un tensor normal no se registrará
        self.bias = torch.zeros(3)

    def forward(self, x):
        return x @ self.weight + self.bias

model = MyModule()
print(list(model.parameters()))  # Salida: [Parameter containing: tensor(...)]
```

Para más detalles, consulta la documentación oficial: [Parameter — PyTorch 2.9 documentation](https://pytorch.org/docs/stable/generated/torch.nn.parameter.Parameter.html)