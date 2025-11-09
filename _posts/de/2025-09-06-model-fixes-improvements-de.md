---
audio: false
date: 2025-09-06
generated: true
image: false
lang: de
layout: post
title: Modellform-Korrekturen und Verbesserungen
translated: true
type: note
---

Hier ist eine Aufschlüsselung dessen, was dein Skript Schritt für Schritt macht, sowie ein paar wichtige Korrekturen, die du wahrscheinlich vornehmen solltest.

# Was das Modell ist

* Du definierst einen kleinen **Zeichen-/Wort-Level-Next-Token-Prädiktor**:

  * `nn.LSTM(input_size=vocab_size, hidden_size=50, num_layers=1)` verarbeitet eine Sequenz von One-Hot-Vektoren (Größe = `vocab_size`) und erzeugt einen Hidden State der Größe 50 zu jedem Zeitpunkt.
  * `nn.Linear(50, vocab_size, bias=False)` bildet den Hidden State jedes Zeitschritts auf **Logits über das Vokabular** ab.

# Erwartete Tensorformen (kritisch)

Die Standard-Eingabeform für PyTorch LSTM ist **(seq\_len, batch\_size, input\_size)**, da du `batch_first=True` nicht gesetzt hast.

* Für eine einzelne Sequenz in einem Batch der Größe 1:

  * Eingaben für das LSTM sollten `(seq_len, 1, vocab_size)` sein.
  * LSTM gibt `x` mit der Form `(seq_len, 1, hidden_size)` aus.
  * Du verwendest dann `view(-1, hidden_size)` → `(seq_len, hidden_size)`, sodass die lineare Schicht `(seq_len, vocab_size)` erzeugt.
  * `CrossEntropyLoss` erwartet:

    * `outputs`: `(N, C)` = `(seq_len, vocab_size)`
    * `targets`: `(N,)` = `(seq_len,)` Token-Indizes

# Wo dein Code wahrscheinlich falsch liegt (Form)

Du machst:

```python
inputs_one_hot = inputs_one_hot.permute(0, 2, 1)
```

Wenn `one_hot_encode_sequence` `(batch, seq_len, vocab)` zurückgibt, ist die korrekte Permute für das Standard-LSTM **`permute(1, 0, 2)`** (um `(seq_len, batch, vocab)` zu erhalten). Deine aktuelle `permute(0,2,1)` ergibt `(batch, vocab, seq_len)`, was nicht übereinstimmt und entweder zu einem Fehler führt oder stillschweigend Unsinn lernt, wenn die frühere Form anders ist als angenommen.

Zwei saubere Optionen (wähle eine):

**A) Behalte das Standard-LSTM (batch\_second):**

```python
# will (seq_len, batch, input_size)
inputs_one_hot = inputs_one_hot.permute(1, 0, 2)  # (seq_len, 1, vocab_size)
```

**B) Mache es batch-first (oft einfacher):**

```python
self.lstm = nn.LSTM(input_size=vocab_size, hidden_size=50, batch_first=True)
# will (batch, seq_len, input_size)
# dann NICHT permuten; belasse es als (1, seq_len, vocab_size)
```

# Trainingsschleifen-Logik

* Du führst zwei laufende Summen pro Epoche: `epoch_training_loss` und `epoch_validation_loss`.
* **Validierungsphase** (`net.eval()` + keine Gradientenschritte):

  * Für jedes (inputs, targets) in `validation_set`:

    * One-Hot-Kodiere Eingaben, konvertiere Targets in Indizes
    * Forward Pass → Logits `(seq_len, vocab_size)` (angenommen, Formen sind korrigiert)
    * CE Loss gegen Target-Indizes der Form `(seq_len,)`
    * Akkumuliere Loss
* **Trainingsphase** (`net.train()`):

  * Gleiche Vorverarbeitung
  * Forward → Loss → `optimizer.zero_grad()` → `loss.backward()` → `optimizer.step()`
* Du zeichnest die durchschnittlichen Losses auf und gibst sie alle 5 Epochen aus.

# Inferenz & Ausgabe

* Du wählst eine Stichprobe aus `test_set`, führst das Modell aus, erhältst Logits für jeden Zeitschritt, nimmst `argmax` pro Zeitschritt → vorhergesagte Tokens.
* Du gibst Eingabewörter, Zielwörter und vorhergesagte Wörter aus.
* Du plottest Training vs. Validation Loss über die Epochen.

# Kleine, wirkungsvolle Verbesserungen

1. **Korrigiere die Eingabeform** (am wichtigsten). Verwende eine der Optionen A oder B oben. Wenn du batch-first wählst, ändere den Forward Pass zu:

   ```python
   x, (h, c) = self.lstm(x)         # x: (batch, seq, hidden)
   x = x.reshape(-1, self.lstm.hidden_size)  # (batch*seq, hidden)
   ```
2. **Verwende `with torch.no_grad()` für Eval/Inferenz**, um das Verfolgen von Gradienten zu vermeiden und für Geschwindigkeit/Speicher:

   ```python
   net.eval()
   with torch.no_grad():
       outputs = net(inputs_one_hot)
       loss = criterion(outputs, targets_idx)
   ```

   Und für die NumPy-Konvertierung:

   ```python
   outputs = net(inputs_one_hot).detach().numpy()
   ```
3. **Setze auch den Seed für PyTorch** für Reproduzierbarkeit:

   ```python
   torch.manual_seed(42)
   ```
4. **Device-Handling** (falls du GPU verwendest):

   ```python
   device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
   net.to(device)
   inputs_one_hot = inputs_one_hot.to(device)
   targets_idx = targets_idx.to(device)
   ```
5. **Target-Ausrichtung**: Stelle sicher, dass `targets` die **nächsten Tokens** sind, die mit jedem Eingabe-Zeitschritt ausgerichtet sind. Wenn dein Datensatz `(inputs, targets)` auf diese Weise paart, ist es gut. Andernfalls erstelle `targets = inputs[1:]` und lasse die letzte Eingabe weg oder ähnliches.
6. **Lasse `.bias=False` weg, es sei denn, du hast einen Grund**; ein Bias auf der Ausgabeschicht ist normalerweise harmlos/hilfreich.
7. **Padding/variable Längen** (optional): Wenn Sequenzen unterschiedliche Längen haben, ziehe `pack_padded_sequence` in Betracht, um das Training auf Padding-Tokens zu vermeiden.
8. **Monitoring**: Accuracy über die Next-Token-Vorhersagen kann interpretierbarer sein als der Loss allein – berechne `% correct argmax` auf der Validation.

# Minimaler korrigierter Ausschnitt (Batch-First-Version)

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

# ... in deiner Schleife, entferne die permute; stelle sicher, dass inputs_one_hot (batch, seq, vocab) ist
# validation/inference verwenden `with torch.no_grad()` und `.detach()`
```

Wenn du die genaue Form teilst, die `one_hot_encode_sequence` zurückgibt (z.B. `(seq, vocab)` vs `(1, seq, vocab)`), kann ich die Permute/Reshape-Zeilen genau auf deinen Fall zuschneiden.