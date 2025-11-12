---
audio: false
generated: true
lang: de
layout: post
title: Kombination historischer Daten mit LSTM
translated: true
type: note
---

Die Kombination historischer Aktiendaten von der TigerOpen API mit einem LSTM-Modell zur Analyse ist machbar und ein gängiger Ansatz in der finanziellen Zeitreihenvorhersage. Das zweite Skript ruft historische Aktiendaten ab (z.B. OHLCV-Bars), die verwendet werden können, um einen Datensatz für das Training eines LSTM-Modells ähnlich dem im ersten Skript zu erstellen. Nachfolgend skizziere ich, wie Sie diese beiden Komponenten integrieren können, gehe auf potenzielle Herausforderungen ein und liefere einen High-Level-Ansatz zur Analyse von Aktiendaten mit einem LSTM.

### High-Level-Ansatz zur Kombination der Beiden

1. **Historische Daten abrufen**:
   - Verwenden Sie die Funktion `get_history_data` aus dem zweiten Skript, um historische Aktiendaten abzurufen (z.B. für das Symbol '00700' oder andere).
   - Die Daten umfassen Open-, High-, Low-, Close-Preise, Volumen und Zeitstempel, die als Features für das LSTM verwendet werden können.

2. **Daten für das LSTM vorverarbeiten**:
   - Konvertieren Sie die historischen Daten in ein für das LSTM-Modell geeignetes Format. Dies beinhaltet:
     - Normalisieren der Daten (z.B. Skalieren der Preise und Volumina auf [0, 1]).
     - Erstellen von Sequenzen historischer Daten (z.B. Verwenden der letzten 60 Tage, um den Schlusskurs des nächsten Tages vorherzusagen).
     - Kodieren der Features (z.B. Schlusskurs, Volumen) in ein Tensor-Format, das mit dem LSTM-Input kompatibel ist.

3. **Das LSTM-Modell anpassen**:
   - Modifizieren Sie die `Net`-Klasse aus dem ersten Skript, um Finanzzeitreihendaten anstelle von Textsequenzen zu verarbeiten.
   - Passen Sie die Input-Größe an die Anzahl der Features an (z.B. Schlusskurs, Volumen, etc.) anstelle von `vocab_size`.
   - Aktualisieren Sie die Output-Layer, um einen kontinuierlichen Wert (z.B. den Schlusskurs des nächsten Tages) oder eine Klassifikation (z.B. Preisanstieg/-abfall) vorherzusagen.

4. **Das Modell trainieren**:
   - Teilen Sie die historischen Daten in Trainings-, Validierungs- und Test-Sets auf.
   - Trainieren Sie das LSTM mit den vorverarbeiteten Daten, ähnlich der Trainingsschleife im ersten Skript.
   - Verwenden Sie eine Loss-Funktion wie Mean Squared Error (MSE) für Regressionsaufgaben oder Cross-Entropy Loss für Klassifikation.

5. **Analysieren und Vorhersagen treffen**:
   - Verwenden Sie das trainierte LSTM, um zukünftige Aktienkurse oder Trends basierend auf recenten historischen Daten vorherzusagen.
   - Visualisieren Sie die Vorhersagen zusammen mit den tatsächlichen Daten mit `matplotlib`.

6. **Integration mit Trading**:
   - Verwenden Sie die Vorhersagen, um Handelsentscheidungen in der `place_order`-Funktion zu informieren.
   - Platzieren Sie beispielsweise eine Kauforder, wenn das LSTM einen Preisanstieg über einem bestimmten Schwellenwert vorhersagt.

### Code-Beispiel: Kombination historischer Daten mit LSTM

Nachfolgend finden Sie einen Beispiel-Code-Ausschnitt, der die beiden Skripte integriert, mit Fokus auf die Vorverarbeitung historischer Daten und die Anpassung des LSTM für Aktienkursvorhersagen.

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

# --- TigerOpen API Setup ---
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

# --- LSTM Model ---
class StockLSTM(nn.Module):
    def __init__(self, input_size, hidden_size=50, num_layers=1):
        super(StockLSTM, self).__init__()
        self.lstm = nn.LSTM(input_size=input_size, hidden_size=hidden_size, num_layers=num_layers, bidirectional=False)
        self.l_out = nn.Linear(in_features=hidden_size, out_features=1)  # Predict next close price

    def forward(self, x):
        x, (h, c) = self.lstm(x)
        x = x[:, -1, :]  # Take the last time step
        x = self.l_out(x)
        return x

# --- Data Preprocessing ---
def prepare_data(df, sequence_length=60, target_col='close'):
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(df[[target_col]].values)
    
    X, y = [], []
    for i in range(len(scaled_data) - sequence_length):
        X.append(scaled_data[i:i + sequence_length])
        y.append(scaled_data[i + sequence_length])
    
    X = np.array(X)
    y = np.array(y)
    
    # Split into train and test
    train_size = int(0.8 * len(X))
    X_train, X_test = X[:train_size], X[train_size:]
    y_train, y_test = y[:train_size], y[train_size:]
    
    return torch.Tensor(X_train), torch.Tensor(y_train), torch.Tensor(X_test), torch.Tensor(y_test), scaler

# --- Training Loop ---
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

# --- Main Execution ---
if __name__ == '__main__':
    # Fetch historical data
    df = get_history_data(symbol='00700', limit=1000)
    
    # Prepare data
    sequence_length = 60
    X_train, y_train, X_test, y_test, scaler = prepare_data(df, sequence_length=sequence_length, target_col='close')
    
    # Initialize and train LSTM
    model = StockLSTM(input_size=1, hidden_size=50, num_layers=1)
    training_loss, validation_loss = train_model(model, X_train, y_train, X_test, y_test, num_epochs=50)
    
    # Plot training and validation loss
    plt.figure()
    plt.plot(training_loss, 'r', label='Training Loss')
    plt.plot(validation_loss, 'b', label='Validation Loss')
    plt.legend()
    plt.xlabel('Epoch')
    plt.ylabel('MSE Loss')
    plt.show()
    
    # Make predictions
    model.eval()
    with torch.no_grad():
        predicted = model(X_test).numpy()
    
    # Inverse transform predictions
    predicted = scaler.inverse_transform(predicted)
    y_test_actual = scaler.inverse_transform(y_test.numpy())
    
    # Plot predictions vs actual
    plt.figure()
    plt.plot(y_test_actual, 'b', label='Actual Close Price')
    plt.plot(predicted, 'r', label='Predicted Close Price')
    plt.legend()
    plt.xlabel('Time')
    plt.ylabel('Close Price')
    plt.show()
```

### Wichtige Modifikationen und Hinweise

1. **Datenabruf**:
   - Die Funktion `get_history_data` wird verwendet, um historische Aktiendaten für ein gegebenes Symbol (z.B. '00700' für Tencent) abzurufen.
   - Die Daten werden in einen pandas DataFrame zur einfachen Manipulation konvertiert.

2. **Vorverarbeitung**:
   - Die Daten werden mit `MinMaxScaler` normalisiert, um die Schlusskurse auf [0, 1] zu skalieren.
   - Sequenzen der Länge `sequence_length` (z.B. 60 Tage) werden erstellt, um den Schlusskurs des nächsten Tages vorherzusagen.
   - Die Daten werden in Trainings- (80%) und Test-Sets (20%) aufgeteilt.

3. **LSTM-Modell**:
   - Die `StockLSTM`-Klasse wird angepasst, um ein einzelnes Feature (Schlusskurs) oder mehrere Features (z.B. Close, Volumen) durch Anpassen der `input_size` zu verarbeiten.
   - Die Output-Layer sagt einen einzelnen Wert (Schlusskurs des nächsten Tages) unter Verwendung einer linearen Schicht vorher.

4. **Training**:
   - Die Trainingsschleife verwendet MSE Loss für die Regression, geeignet für die Vorhersage kontinuierlicher Werte wie Aktienkurse.
   - Das Modell wird auf dem Test-Set evaluiert, um den Validation Loss zu verfolgen.

5. **Visualisierung**:
   - Trainings- und Validation-Loss werden geplottet, um die Modellkonvergenz zu beurteilen.
   - Vorhergesagte vs. tatsächliche Schlusskurse werden geplottet, um die Modellleistung zu bewerten.

### Potenzielle Herausforderungen und Überlegungen

1. **Datenqualität und -menge**:
   - Die Menge an historischen Daten (z.B. `limit=1000` Bars) könnte für ein robustes LSTM-Training unzureichend sein. Erwägen Sie, mehr Daten abzurufen oder eine kleinere `sequence_length` zu verwenden.
   - Aktiendaten können verrauscht sein, und LSTM-Modelle könnten mit langfristigen Abhängigkeiten oder plötzlichen Marktverschiebungen kämpfen.

2. **Feature-Engineering**:
   - Das Beispiel verwendet nur den Schlusskurs. Das Einbeziehen zusätzlicher Features (z.B. Volumen, gleitende Durchschnitte, technische Indikatoren wie RSI) kann die Modellleistung verbessern.
   - Feature-Auswahl und Vorverarbeitung (z.B. Handhabung fehlender Daten, Ausreißer) sind kritisch.

3. **Modellkomplexität**:
   - Die LSTM-Architektur ist einfach (1 Layer, 50 Hidden Units). Für komplexe Finanzdaten sollten Sie tiefere Modelle, Dropout zur Regularisierung oder andere Architekturen wie GRU oder Transformer in Betracht ziehen.

4. **Overfitting**:
   - Überwachen Sie Training vs. Validation Loss, um Overfitting zu erkennen. Fügen Sie bei Bedarf Dropout oder Weight Decay hinzu.

5. **Echtzeit-Integration**:
   - Um das Modell für Echtzeit-Trading zu verwenden, rufen Sie recente Daten ab, verarbeiten Sie sie vor und speisen Sie sie in das trainierte LSTM ein, um Vorhersagen zu generieren.
   - Kombinieren Sie Vorhersagen mit einer Trading-Strategie (z.B. kaufen, wenn vorhergesagter Preis > aktueller Preis um X %).

6. **API-Limitationen**:
   - Stellen Sie sicher, dass Ihre TigerOpen API-Zugangsdaten korrekt in den Environment-Variablen (`TIGER_PEM`, `TIGER_TIGER_ID`, `TIGER_ACCOUNT`) gesetzt sind.
   - Seien Sie sich der API-Ratenlimits und Datenverfügbarkeit für bestimmte Symbole oder Zeitperioden bewusst.

### Beispielausgabe
Vorausgesetzt der Code läuft erfolgreich, könnten Sie sehen:
- Konsolenausgabe, die Trainings- und Validation-Loss pro Epoche anzeigt (z.B. `Epoch 0, Training Loss: 0.1234, Validation Loss: 0.1345`).
- Ein Plot des Trainings- und Validation-Loss über die Epochen, der die Konvergenz anzeigt.
- Ein Plot, der vorhergesagte vs. tatsächliche Schlusskurse für den Test-Set vergleicht und zeigt, wie gut das LSTM Trends erfasst.

### Nächste Schritte
- **Features erweitern**: Beziehen Sie technische Indikatoren (z.B. MACD, Bollinger Bands) oder Sentiment-Daten von X-Posts (falls verfügbar über die Suche) ein.
- **Backtesting**: Testen Sie die LSTM-Vorhersagen in einer simulierten Trading-Umgebung mit historischen Daten, um die Profitabilität zu bewerten.
- **Trading-Integration**: Verwenden Sie die `place_order`-Funktion, um Trades basierend auf LSTM-Vorhersagen auszuführen, mit angemessenem Risikomanagement.
- **Hyperparameter-Tuning**: Experimentieren Sie mit `sequence_length`, `hidden_size`, `num_layers` und Lernrate, um die Performance zu optimieren.

### Würde es funktionieren?
Ja, die Kombination historischer Aktiendaten mit einem LSTM zur Analyse ist ein praktikabler Ansatz, der im algorithmischen Handel weit verbreitet ist. Der Erfolg hängt jedoch ab von:
- Ausreichenden und sauberen Daten.
- Korrekter Vorverarbeitung und Feature-Engineering.
- Einem gut abgestimmten LSTM-Modell.
- Einer robusten Trading-Strategie, um auf Vorhersagen zu reagieren.

Finanzmärkte sind inhärent verrauscht und werden von externen Faktoren beeinflusst (z.B. Nachrichten, makroökonomische Ereignisse), daher sollten LSTM-Vorhersagen mit Vorsicht verwendet werden, idealerweise als Teil einer breiteren Strategie mit Risikokontrollen.

Wenn Sie tiefer in einen bestimmten Teil eintauchen möchten (z.B. Hinzufügen von Features, Backtesting oder Echtzeit-Trading), lassen Sie es mich wissen!