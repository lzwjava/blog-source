---
audio: false
generated: true
lang: es
layout: post
title: Combinación de Datos Históricos con LSTM
translated: true
type: note
---

Combinar datos históricos de acciones de la TigerOpen API con un modelo LSTM para su análisis es factible y un enfoque común en la predicción de series temporales financieras. El segundo script recupera datos históricos de acciones (por ejemplo, barras OHLCV), que pueden utilizarse para construir un conjunto de datos para entrenar un modelo LSTM similar al del primer script. A continuación, describo cómo puedes integrar estos dos, abordar posibles desafíos y proporcionar un enfoque de alto nivel para analizar datos de acciones utilizando un LSTM.

### Enfoque de Alto Nivel para Combinar los Dos

1. **Recuperar Datos Históricos**:
   - Utiliza la función `get_history_data` del segundo script para obtener datos históricos de acciones (por ejemplo, para el símbolo '00700' u otros).
   - Los datos incluyen precios de apertura, máximo, mínimo, cierre, volumen y marcas de tiempo, que pueden usarse como características para el LSTM.

2. **Preprocesar Datos para LSTM**:
   - Convierte los datos históricos a un formato adecuado para el modelo LSTM. Esto implica:
     - Normalizar los datos (por ejemplo, escalar precios y volúmenes a [0, 1]).
     - Crear secuencias de datos históricos (por ejemplo, usar los últimos 60 días para predecir el precio de cierre del día siguiente).
     - Codificar características (por ejemplo, precio de cierre, volumen) en un formato de tensor compatible con la entrada del LSTM.

3. **Adaptar el Modelo LSTM**:
   - Modifica la clase `Net` del primer script para manejar datos de series temporales financieras en lugar de secuencias de texto.
   - Ajusta el tamaño de entrada para que coincida con el número de características (por ejemplo, precio de cierre, volumen, etc.) en lugar de `vocab_size`.
   - Actualiza la capa de salida para predecir un valor continuo (por ejemplo, el precio de cierre del día siguiente) o una clasificación (por ejemplo, aumento/disminución del precio).

4. **Entrenar el Modelo**:
   - Divide los datos históricos en conjuntos de entrenamiento, validación y prueba.
   - Entrena el LSTM utilizando los datos preprocesados, similar al bucle de entrenamiento del primer script.
   - Utiliza una función de pérdida como el Error Cuadrático Medio (MSE) para tareas de regresión o la Pérdida de Entropía Cruzada para clasificación.

5. **Analizar y Predecir**:
   - Utiliza el LSTM entrenado para predecir precios futuros de acciones o tendencias basadas en datos históricos recientes.
   - Visualiza las predicciones junto con los datos reales usando `matplotlib`.

6. **Integrar con Trading**:
   - Utiliza las predicciones para informar decisiones de trading en la función `place_order`.
   - Por ejemplo, coloca una orden de compra si el LSTM predice un aumento de precio por encima de un umbral.

### Ejemplo de Código: Combinando Datos Históricos con LSTM

A continuación se muestra un fragmento de código de ejemplo que integra los dos scripts, centrándose en el preprocesamiento de datos históricos y la adaptación del LSTM para la predicción del precio de las acciones.

```python
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tigeropen.common.consts import Language, Market, BarPeriod, QuoteRight
from tigeropen.tiger_open_config import TigerOpenClientConfig
from tigeropen.quote.quote_client import QuoteClient
from tigeropen.common.util.signature_utils import read_private_key
import os
from datetime import datetime

# --- Configuración de la API TigerOpen ---
def get_client_config(sandbox=False):
    client_config = TigerOpenClientConfig(sandbox_debug=sandbox)
    client_config.private_key = read_private_key(os.environ.get('TIGER_PEM'))
    client_config.tiger_id = os.environ.get('TIGER_TIGER_ID')
    client_config.account = os.environ.get('TIGER_ACCOUNT')
    client_config.language = Language.zh_CN
    return client_config

def get_history_data(symbol='00700', period=BarPeriod.DAY, begin_time='2024-01-01', end_time=None, limit=100):
    client_config = get_client_config()
    quote_client = QuoteClient(client_config)
    if not end_time:
        end_time = datetime.now().strftime('%Y-%m-%d')
    bars_dict = quote_client.get_bars(
        symbols=[symbol], period=period, begin_time=begin_time, end_time=end_time, limit=limit, right=QuoteRight.BR
    )
    bars = bars_dict.get(symbol, [])
    return pd.DataFrame([{
        'time': bar.time,
        'open': bar.open,
        'high': bar.high,
        'low': bar.low,
        'close': bar.close,
        'volume': bar.volume
    } for bar in bars])

# --- Modelo LSTM ---
class StockLSTM(nn.Module):
    def __init__(self, input_size, hidden_size=50, num_layers=1):
        super(StockLSTM, self).__init__()
        self.lstm = nn.LSTM(input_size=input_size, hidden_size=hidden_size, num_layers=num_layers, bidirectional=False)
        self.l_out = nn.Linear(in_features=hidden_size, out_features=1)  # Predecir próximo precio de cierre

    def forward(self, x):
        x, (h, c) = self.lstm(x)
        x = x[:, -1, :]  # Tomar el último paso de tiempo
        x = self.l_out(x)
        return x

# --- Preprocesamiento de Datos ---
def prepare_data(df, sequence_length=60, target_col='close'):
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(df[[target_col]].values)
    
    X, y = [], []
    for i in range(len(scaled_data) - sequence_length):
        X.append(scaled_data[i:i + sequence_length])
        y.append(scaled_data[i + sequence_length])
    
    X = np.array(X)
    y = np.array(y)
    
    # Dividir en entrenamiento y prueba
    train_size = int(0.8 * len(X))
    X_train, X_test = X[:train_size], X[train_size:]
    y_train, y_test = y[:train_size], y[train_size:]
    
    return torch.Tensor(X_train), torch.Tensor(y_train), torch.Tensor(X_test), torch.Tensor(y_test), scaler

# --- Bucle de Entrenamiento ---
def train_model(model, X_train, y_train, X_test, y_test, num_epochs=50, lr=3e-4):
    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    
    training_loss, validation_loss = [], []
    
    for epoch in range(num_epochs):
        model.train()
        outputs = model(X_train)
        loss = criterion(outputs, y_train)
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        training_loss.append(loss.item())
        
        model.eval()
        with torch.no_grad():
            val_outputs = model(X_test)
            val_loss = criterion(val_outputs, y_test)
            validation_loss.append(val_loss.item())
        
        if epoch % 5 == 0:
            print(f'Epoch {epoch}, Training Loss: {training_loss[-1]:.4f}, Validation Loss: {validation_loss[-1]:.4f}')
    
    return training_loss, validation_loss

# --- Ejecución Principal ---
if __name__ == '__main__':
    # Obtener datos históricos
    df = get_history_data(symbol='00700', limit=1000)
    
    # Preparar datos
    sequence_length = 60
    X_train, y_train, X_test, y_test, scaler = prepare_data(df, sequence_length=sequence_length, target_col='close')
    
    # Inicializar y entrenar LSTM
    model = StockLSTM(input_size=1, hidden_size=50, num_layers=1)
    training_loss, validation_loss = train_model(model, X_train, y_train, X_test, y_test, num_epochs=50)
    
    # Graficar pérdida de entrenamiento y validación
    plt.figure()
    plt.plot(training_loss, 'r', label='Pérdida de Entrenamiento')
    plt.plot(validation_loss, 'b', label='Pérdida de Validación')
    plt.legend()
    plt.xlabel('Época')
    plt.ylabel('Pérdida MSE')
    plt.show()
    
    # Hacer predicciones
    model.eval()
    with torch.no_grad():
        predicted = model(X_test).numpy()
    
    # Transformar inversamente las predicciones
    predicted = scaler.inverse_transform(predicted)
    y_test_actual = scaler.inverse_transform(y_test.numpy())
    
    # Graficar predicciones vs real
    plt.figure()
    plt.plot(y_test_actual, 'b', label='Precio de Cierre Real')
    plt.plot(predicted, 'r', label='Precio de Cierre Predicho')
    plt.legend()
    plt.xlabel('Tiempo')
    plt.ylabel('Precio de Cierre')
    plt.show()
```

### Modificaciones Clave y Notas

1. **Recuperación de Datos**:
   - La función `get_history_data` se utiliza para obtener datos históricos de acciones para un símbolo dado (por ejemplo, '00700' para Tencent).
   - Los datos se convierten en un DataFrame de pandas para una fácil manipulación.

2. **Preprocesamiento**:
   - Los datos se normalizan usando `MinMaxScaler` para escalar los precios de cierre a [0, 1].
   - Se crean secuencias de `sequence_length` (por ejemplo, 60 días) para predecir el precio de cierre del día siguiente.
   - Los datos se dividen en conjuntos de entrenamiento (80%) y prueba (20%).

3. **Modelo LSTM**:
   - La clase `StockLSTM` se adapta para manejar una sola característica (precio de cierre) o múltiples características (por ejemplo, cierre, volumen) ajustando `input_size`.
   - La capa de salida predice un solo valor (precio de cierre del día siguiente) usando una capa lineal.

4. **Entrenamiento**:
   - El bucle de entrenamiento utiliza la pérdida MSE para regresión, adecuada para predecir valores continuos como los precios de las acciones.
   - El modelo se evalúa en el conjunto de prueba para rastrear la pérdida de validación.

5. **Visualización**:
   - Las pérdidas de entrenamiento y validación se grafican para evaluar la convergencia del modelo.
   - Los precios de cierre predichos frente a los reales se grafican para evaluar el rendimiento del modelo.

### Posibles Desafíos y Consideraciones

1. **Calidad y Cantidad de Datos**:
   - La cantidad de datos históricos (por ejemplo, `limit=1000` barras) puede ser insuficiente para un entrenamiento robusto del LSTM. Considera obtener más datos o usar un `sequence_length` más pequeño.
   - Los datos de acciones pueden ser ruidosos, y los modelos LSTM pueden tener dificultades con dependencias a largo plazo o cambios bruscos del mercado.

2. **Ingeniería de Características**:
   - El ejemplo utiliza solo el precio de cierre. Incluir características adicionales (por ejemplo, volumen, medias móviles, indicadores técnicos como RSI) puede mejorar el rendimiento del modelo.
   - La selección de características y el preprocesamiento (por ejemplo, manejo de datos faltantes, valores atípicos) son críticos.

3. **Complejidad del Modelo**:
   - La arquitectura LSTM es simple (1 capa, 50 unidades ocultas). Para datos financieros complejos, considera modelos más profundos, dropout para regularización u otras arquitecturas como GRU o Transformer.

4. **Sobreajuste**:
   - Monitorea la pérdida de entrenamiento frente a la de validación para detectar sobreajuste. Añade dropout o decaimiento de pesos si es necesario.

5. **Integración en Tiempo Real**:
   - Para usar el modelo en tiempo real para trading, obtén datos recientes, preprocésalos y aliméntalos al LSTM entrenado para generar predicciones.
   - Combina las predicciones con una estrategia de trading (por ejemplo, comprar si el precio predicho > precio actual por X%).

6. **Limitaciones de la API**:
   - Asegúrate de que tus credenciales de la API TigerOpen estén correctamente establecidas en las variables de entorno (`TIGER_PEM`, `TIGER_TIGER_ID`, `TIGER_ACCOUNT`).
   - Ten en cuenta los límites de tasa de la API y la disponibilidad de datos para ciertos símbolos o períodos de tiempo.

### Ejemplo de Salida
Suponiendo que el código se ejecuta con éxito, podrías ver:
- Salida en la consola mostrando la pérdida de entrenamiento y validación por época (por ejemplo, `Epoch 0, Training Loss: 0.1234, Validation Loss: 0.1345`).
- Una gráfica de la pérdida de entrenamiento y validación a lo largo de las épocas, indicando convergencia.
- Una gráfica comparando los precios de cierre predichos frente a los reales para el conjunto de prueba, mostrando qué tan bien el LSTM captura las tendencias.

### Próximos Pasos
- **Mejorar Características**: Incorpora indicadores técnicos (por ejemplo, MACD, Bandas de Bollinger) o datos de sentimiento de publicaciones en X (si están disponibles mediante búsqueda).
- **Backtesting**: Prueba las predicciones del LSTM en un entorno de trading simulado utilizando datos históricos para evaluar la rentabilidad.
- **Integración de Trading**: Utiliza la función `place_order` para ejecutar operaciones basadas en las predicciones del LSTM, con una gestión de riesgos adecuada.
- **Ajuste de Hiperparámetros**: Experimenta con `sequence_length`, `hidden_size`, `num_layers` y la tasa de aprendizaje para optimizar el rendimiento.

### ¿Funcionaría?
Sí, combinar datos históricos de acciones con un LSTM para su análisis es un enfoque viable, ampliamente utilizado en el trading algorítmico. Sin embargo, el éxito depende de:
- Datos suficientes y limpios.
- Preprocesamiento e ingeniería de características adecuados.
- Un modelo LSTM bien ajustado.
- Una estrategia de trading robusta para actuar sobre las predicciones.

Los mercados financieros son inherentemente ruidosos y están influenciados por factores externos (por ejemplo, noticias, eventos macroeconómicos), por lo que las predicciones del LSTM deben usarse con precaución, idealmente como parte de una estrategia más amplia con controles de riesgo.

Si deseas profundizar en cualquier parte (por ejemplo, añadir características, backtesting o trading en tiempo real), ¡házmelo saber!