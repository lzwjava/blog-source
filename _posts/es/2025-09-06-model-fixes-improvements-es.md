---
audio: false
date: 2025-09-06
generated: true
image: false
lang: es
layout: post
title: Correcciones y Mejoras del Modelo de Forma
translated: true
type: note
---

Esto es lo que hace tu script, pieza por pieza, más un par de correcciones importantes que probablemente querrás hacer.

# Qué es el modelo

* Defines un pequeño **predictor del siguiente token a nivel de carácter/palabra**:

  * `nn.LSTM(input_size=vocab_size, hidden_size=50, num_layers=1)` procesa una secuencia de vectores one-hot (tamaño = `vocab_size`) y produce un estado oculto de tamaño 50 en cada paso de tiempo.
  * `nn.Linear(50, vocab_size, bias=False)` mapea el estado oculto de cada paso de tiempo a **logits sobre el vocabulario**.

# Formas esperadas de los tensores (crítico)

La forma de entrada predeterminada de LSTM en PyTorch es **(seq_len, batch_size, input_size)** porque no configuraste `batch_first=True`.

* Para una sola secuencia en un lote de 1:

  * Las entradas al LSTM deben ser `(seq_len, 1, vocab_size)`.
  * La salida del LSTM `x` tiene forma `(seq_len, 1, hidden_size)`.
  * Luego aplicas `view(-1, hidden_size)` → `(seq_len, hidden_size)` para que la capa lineal produzca `(seq_len, vocab_size)`.
  * `CrossEntropyLoss` espera:

    * `outputs`: `(N, C)` = `(seq_len, vocab_size)`
    * `targets`: `(N,)` = `(seq_len,)` índices de los tokens

# Donde tu código probablemente falla (forma)

Haces:

```python
inputs_one_hot = inputs_one_hot.permute(0, 2, 1)
```

Si `one_hot_encode_sequence` retorna `(batch, seq_len, vocab)`, el permute correcto para el LSTM por defecto es **`permute(1, 0, 2)`** (para obtener `(seq_len, batch, vocab)`). Tu `permute(0,2,1)` actual da `(batch, vocab, seq_len)`, lo cual no coincide y producirá un error o aprenderá silenciosamente sin sentido si la forma anterior es diferente a la asumida.

Dos opciones limpias (elige una):

**A) Mantener LSTM por defecto (batch_second):**

```python
# queremos (seq_len, batch, input_size)
inputs_one_hot = inputs_one_hot.permute(1, 0, 2)  # (seq_len, 1, vocab_size)
```

**B) Hacerlo batch-first (a menudo más simple):**

```python
self.lstm = nn.LSTM(input_size=vocab_size, hidden_size=50, batch_first=True)
# queremos (batch, seq_len, input_size)
# luego NO permutes; déjalo como (1, seq_len, vocab_size)
```

# Lógica del bucle de entrenamiento

* Mantienes dos sumas acumuladas por época: `epoch_training_loss` y `epoch_validation_loss`.
* **Fase de validación** (`net.eval()` + sin pasos de gradiente):

  * Para cada (inputs, targets) en `validation_set`:

    * codificar inputs en one-hot, convertir targets a índices
    * pase forward → logits `(seq_len, vocab_size)` (asumiendo formas corregidas)
    * pérdida CE contra índices objetivo de forma `(seq_len,)`
    * acumular pérdida
* **Fase de entrenamiento** (`net.train()`):

  * Mismo preprocesamiento
  * forward → pérdida → `optimizer.zero_grad()` → `loss.backward()` → `optimizer.step()`
* Registras las pérdidas promedio y las imprimes cada 5 épocas.

# Inferencia e impresión

* Tomas una muestra de `test_set`, ejecutas el modelo, obtienes logits para cada paso de tiempo, aplicas `argmax` por paso de tiempo → tokens predichos.
* Imprimes las palabras de entrada, las palabras objetivo y las palabras predichas.
* Graficas la pérdida de entrenamiento vs la de validación a lo largo de las épocas.

# Mejoras pequeñas y de alto impacto

1. **Corrige la forma de entrada** (lo más importante). Usa una de las opciones A o B anteriores. Si eliges batch-first, cambia el pase forward a:

   ```python
   x, (h, c) = self.lstm(x)         # x: (batch, seq, hidden)
   x = x.reshape(-1, self.lstm.hidden_size)  # (batch*seq, hidden)
   ```
2. **Usa `with torch.no_grad()` para eval/inferencia** para evitar rastrear gradientes y por velocidad/memoria:

   ```python
   net.eval()
   with torch.no_grad():
       outputs = net(inputs_one_hot)
       loss = criterion(outputs, targets_idx)
   ```

   Y para la conversión a numpy:

   ```python
   outputs = net(inputs_one_hot).detach().numpy()
   ```
3. **Semilla para PyTorch también** para reproducibilidad:

   ```python
   torch.manual_seed(42)
   ```
4. **Manejo de dispositivo** (si usas GPU):

   ```python
   device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
   net.to(device)
   inputs_one_hot = inputs_one_hot.to(device)
   targets_idx = targets_idx.to(device)
   ```
5. **Alineación del objetivo**: asegúrate de que `targets` sean los **siguientes tokens** alineados con cada paso de tiempo de entrada. Si tu conjunto de datos empareja `(inputs, targets)` de esa manera, estás bien. De lo contrario, crea `targets = inputs[1:]` y descarta la última entrada o algo similar.
6. **Elimina `.bias=False` a menos que tengas una razón**; un sesgo en la capa de salida usualmente es inofensivo/útil.
7. **Relleno/longitudes variables** (opcional): si las secuencias tienen longitudes variables, considera `pack_padded_sequence` para evitar entrenar en tokens de relleno.
8. **Monitoreo**: la precisión sobre las predicciones del siguiente token puede ser más interpretable que solo la pérdida—calcula `% de aciertos en argmax` en la validación.

# Fragmento corregido mínimo (versión batch-first)

```python
class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.lstm = nn.LSTM(input_size=vocab_size, hidden_size=50, num_layers=1, batch_first=True)
        self.l_out = nn.Linear(50, vocab_size)

    def forward(self, x):
        # x: (batch, seq, vocab_size)
        x, _ = self.lstm(x)                    # (batch, seq, hidden)
        x = x.reshape(-1, self.lstm.hidden_size)  # (batch*seq, hidden)
        x = self.l_out(x)                      # (batch*seq, vocab)
        return x

# ... en tu bucle, elimina el permute; asegura que inputs_one_hot sea (batch, seq, vocab)
# validación/inferencia usan `with torch.no_grad()` y `.detach()`
```

Si compartes la forma exacta que retorna `one_hot_encode_sequence` (ej., `(seq, vocab)` vs `(1, seq, vocab)`), puedo adaptar las líneas de permute/reshape precisamente para tu caso.