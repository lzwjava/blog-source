---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast:free
title: Lora-Code-Zerlegung und Erklärung
translated: true
type: note
---

Ich werde den LoRA-Demo-Code in wichtige Teile zerlegen und jeden Teil im Detail erklären, bevor ich zum nächsten übergehe. Dies wird helfen, die Funktionsweise von LoRA auf klare, schrittweise Weise zu veranschaulichen. Der Code basiert auf dem vorherigen Beispiel und verwendet PyTorch, um LoRA für eine einfache lineare Schicht zu implementieren.

### Code-Teil 1: Definition der LoRA-Schicht
```python
import torch
import torch.nn as nn

class LoRALayer(nn.Module):
    def __init__(self, in_features, out_features, rank=4):
        super(LoRALayer, self).__init__()
        # Ursprüngliche eingefrorene Gewichte
        self.linear = nn.Linear(in_features, out_features)
        self.linear.weight.requires_grad = False  # Ursprüngliche Gewichte einfrieren
        # LoRA-Parameter: Niedrigrang-Matrizen A und B
        self.lora_A = nn.Parameter(torch.randn(in_features, rank))
        self.lora_B = nn.Parameter(torch.randn(rank, out_features))
        self.scaling = 1.0  # Skalierungsfaktor für LoRA-Updates
```

#### Erklärung
Dieser Teil definiert die `LoRALayer`-Klasse, die die LoRA-Technik implementiert. Hier ist was passiert:

- **Imports und Klassen-Setup**: Wir importieren PyTorch (`torch`) und sein Neural Network Modul (`nn`). Die `LoRALayer`-Klasse erbt von `nn.Module`, wodurch sie ein PyTorch-Modul wird, das in größere Modelle integriert werden kann.
- **Ursprüngliche Lineare Schicht**: `self.linear = nn.Linear(in_features, out_features)` erstellt eine Standard-lineare Schicht (wie eine vollständig verbundene Schicht in einem neuronalen Netzwerk) mit `in_features` Eingängen und `out_features` Ausgängen. Diese repräsentiert die vortrainierten Gewichte, die wir anpassen möchten.
- **Einfrieren der Gewichte**: `self.linear.weight.requires_grad = False` friert die ursprünglichen Gewichte der linearen Schicht ein und stellt sicher, dass sie während des Trainings nicht aktualisiert werden. Dies ist entscheidend für die Effizienz von LoRA, da es die Änderung des großen vortrainierten Modells vermeidet.
- **LoRA-Parameter**: `self.lora_A` und `self.lora_B` sind Niedrigrang-Matrizen. `lora_A` hat die Form `(in_features, rank)` und `lora_B` hat die Form `(rank, out_features)`. Der `rank`-Parameter (Standard=4) kontrolliert die Größe dieser Matrizen und hält sie viel kleiner als die ursprüngliche Gewichtsmatrix (Form `in_features x out_features`). Diese Matrizen sind trainierbar (`nn.Parameter`) und mit Zufallswerten initialisiert (`torch.randn`).
- **Skalierungsfaktor**: `self.scaling = 1.0` ist ein Hyperparameter, um die LoRA-Anpassung zu skalieren und eine Feinabstimmung der Adaptionsstärke zu ermöglichen.

Dieses Setup stellt sicher, dass nur die kleinen `lora_A`- und `lora_B`-Matrizen während des Trainings aktualisiert werden, was die Anzahl der trainierbaren Parameter drastisch reduziert.

---

### Code-Teil 2: LoRA Forward Pass
```python
    def forward(self, x):
        # Ursprüngliche lineare Transformation + LoRA-Anpassung
        original = self.linear(x)
        lora_adjustment = self.scaling * torch.matmul(torch.matmul(x, self.lora_A), self.lora_B)
        return original + lora_adjustment
```

#### Erklärung
Dieser Teil definiert den Forward Pass der `LoRALayer`, der die Ausgabe der Schicht berechnet:

- **Eingabe**: Die Eingabe `x` ist ein Tensor der Form `(batch_size, in_features)` und repräsentiert einen Batch von Eingabedaten.
- **Ursprüngliche Ausgabe**: `original = self.linear(x)` berechnet die Ausgabe der eingefrorenen linearen Schicht, indem sie die vortrainierten Gewichte auf die Eingabe anwendet.
- **LoRA-Anpassung**: Der Term `torch.matmul(torch.matmul(x, self.lora_A), self.lora_B)` berechnet die Niedrigrang-Adaption. Zuerst wird `x` mit `lora_A` (Form `in_features x rank`) multipliziert, was einen Tensor der Form `(batch_size, rank)` erzeugt. Dann wird dies mit `lora_B` (Form `rank x out_features`) multipliziert, was einen Tensor der Form `(batch_size, out_features)` ergibt – die gleiche Form wie die ursprüngliche Ausgabe. Diese Anpassung repräsentiert die aufgabenspezifische Aktualisierung.
- **Skalierung und Kombination**: Die Anpassung wird mit `self.scaling` skaliert und zur ursprünglichen Ausgabe addiert, um die endgültige Ausgabe zu erzeugen. Dies stellt sicher, dass das Modell das vortrainierte Wissen beibehält, während es aufgabenspezifische Anpassungen einbezieht.

Die Niedrigrang-Struktur (`rank` ist klein, z.B. 4) stellt sicher, dass die Anpassung im Vergleich zur Aktualisierung der vollständigen Gewichtsmatrix recheneffizient und parameter-effizient ist.

---

### Code-Teil 3: Toy-Datensatz und Training
```python
def create_toy_dataset(n_samples=1000):
    X = torch.randn(n_samples, 64)  # Zufällige Eingabemerkmale
    y = torch.randn(n_samples, 10)  # Zufällige Zielausgaben
    return X, y

def train_model(model, X, y, epochs=10, lr=0.01):
    criterion = nn.MSELoss()
    optimizer = optim.Adam([param for param in model.parameters() if param.requires_grad], lr=lr)
    
    for epoch in range(epochs):
        model.train()
        optimizer.zero_grad()
        outputs = model(X)
        loss = criterion(outputs, y)
        loss.backward()
        optimizer.step()
        print(f"Epoch {epoch+1}/{epochs}, Loss: {loss.item():.4f}")
```

#### Erklärung
Dieser Teil erstellt einen Toy-Datensatz und trainiert das LoRA-adaptierte Modell:

- **Toy-Datensatz**: Die Funktion `create_toy_dataset` erzeugt synthetische Daten zur Demonstration. `X` ist ein Tensor der Form `(1000, 64)` (1000 Samples, 64 Merkmale) und `y` ist ein Tensor der Form `(1000, 10)` (1000 Samples, 10 Ausgabedimensionen). Dies sind zufällige Tensoren, um Eingabe-Ausgabe-Paare zu simulieren.
- **Trainingsfunktion**: Die Funktion `train_model` richtet eine einfache Trainingsschleife ein:
  - **Verlustfunktion**: `nn.MSELoss()` definiert den mittleren quadratischen Fehler als Verlust, geeignet für diese regressionsähnliche Toy-Aufgabe.
  - **Optimierer**: `optim.Adam` optimiert nur die trainierbaren Parameter (für die `param.requires_grad` `True` ist), also `lora_A` und `lora_B`. Das eingefrorene `linear.weight` ist ausgeschlossen, was Effizienz gewährleistet.
  - **Trainingsschleife**: Für jede Epoche berechnet das Modell die Ausgaben, berechnet den Verlust, führt Backpropagation durch (`loss.backward()`) und aktualisiert die LoRA-Parameter (`optimizer.step()`). Der Verlust wird ausgegeben, um den Trainingsfortschritt zu überwachen.

Dieses Setup demonstriert, wie LoRA nur die Niedrigrang-Matrizen feinabstimmt und den Prozess damit leichtgewichtig hält.

---

### Code-Teil 4: Hauptausführung und Parameterzählung
```python
def main():
    # Setze Zufallssaat für Reproduzierbarkeit
    torch.manual_seed(42)
    
    # Erstelle Toy-Datensatz
    X, y = create_toy_dataset()
    
    # Initialisiere Modell mit LoRA
    model = LoRALayer(in_features=64, out_features=10, rank=4)
    
    # Zähle trainierbare Parameter
    trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    total_params = sum(p.numel() for p in model.parameters())
    print(f"Trainable parameters: {trainable_params}")
    print(f"Total parameters: {total_params}")
    
    # Trainiere das Modell
    train_model(model, X, y)

if __name__ == "__main__":
    main()
```

#### Erklärung
Dieser Teil verbindet alles und hebt die Effizienz von LoRA hervor:

- **Zufallssaat**: `torch.manual_seed(42)` stellt die Reproduzierbarkeit der Zufallsinitialisierungen sicher.
- **Datensatz und Modell**: Der Toy-Datensatz wird erstellt und eine `LoRALayer` mit `in_features=64`, `out_features=10` und `rank=4` initialisiert.
- **Parameterzählung**: Der Code berechnet:
  - **Trainierbare Parameter**: Nur `lora_A` (64 × 4 = 256) und `lora_B` (4 × 10 = 40), insgesamt 296 Parameter.
  - **Gesamtparameter**: Beinhaltet das eingefrorene `linear.weight` (64 × 10 = 640) und `linear.bias` (10), plus die LoRA-Parameter, insgesamt 946.
  - Dies zeigt die Effizienz von LoRA: Nur ~31% (296/946) der Parameter sind trainierbar, verglichen mit 100% beim vollständigen Fine-Tuning.
- **Training**: Die Funktion `train_model` wird aufgerufen, um die LoRA-Parameter auf dem Toy-Datensatz feinabzustimmen.

Wenn Sie dies ausführen, werden Sie sehen, dass die Anzahl der trainierbaren Parameter viel kleiner ist als die Gesamtanzahl und dass das Modell aufgrund der Niedrigrang-Updates schnell trainiert.

---

### Ausführen des Codes
Um dies auszuführen, benötigen Sie PyTorch installiert (`pip install torch`). Speichern Sie den vollständigen Code als `.py`-Datei und führen Sie sie aus. Die Ausgabe zeigt die Anzahl der Parameter und den Trainingsverlust über 10 Epochen und demonstriert so die Effizienz von LoRA beim Fine-Tuning.

[LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685)

Lassen Sie mich wissen, wenn Sie tiefer in einen Teil eintauchen oder das Beispiel modifizieren möchten!