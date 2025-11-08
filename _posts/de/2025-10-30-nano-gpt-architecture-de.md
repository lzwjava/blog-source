---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Zusammenfassung der NanoGPT-Modellarchitektur
translated: true
type: note
---

### Überblick über die NanoGPT-Modellarchitektur

NanoGPT implementiert ein GPT-2-ähnliches, nur-Decoder-Transformer-Modell in PyTorch. Die Architektur ist in der Datei `model.py` definiert, mit einer konfigurierbaren `GPTConfig`, die die Hyperparameter festlegt. Die Standardkonfiguration (z.B. für die "gpt2"-Variante) verwendet:

- **Anzahl der Transformer-Blöcke**: 12 (`n_layer = 12`)
- **Einbettungsdimension (Schichtgröße)**: 768 (`n_embd = 768`)
- **Anzahl der Attention-Köpfe**: 12 (`n_head = 12`)
- **MLP-Zwischengröße**: 3072 (`n_embd * 4`, da der Expansionsfaktor 4 beträgt)

Jeder Transformer-Block (Klasse `Block`) ist ein standardmäßiger Decoder-Block mit Residual Connections und Layer Normalization. Er beinhaltet:
- **LayerNorm 1** (`ln1`): Wird vor der Self-Attention angewendet.
- **Multi-Head Self-Attention** (`attn`): Kausale (maskierte) Attention, um das Vorausschauen zu verhindern.
- Residual Addition nach der Attention.
- **LayerNorm 2** (`ln2`): Wird vor dem MLP angewendet.
- **MLP** (`mlp`): Ein einfaches Feed-Forward-Netzwerk.
- Residual Addition nach dem MLP.

Das Gesamtmodell (Klasse `GPT`) stapelt diese 12 Blöcke nach Token- und Positionseinbettungen, gefolgt von einer finalen LayerNorm (`ln_f`) und einer linearen Projektion auf die Vokabulargröße.

#### MLP-Struktur
Der MLP (Klasse `MLP` innerhalb von `Block`) ist ein zweischichtiges Feed-Forward-Netzwerk:
- Erste lineare Schicht (`c_fc`): Projiziert von `n_embd` (768) auf die Zwischengröße (3072).
- GELU-Aktivierung: Wird elementweise nach der ersten Projektion angewendet.
- Zweite lineare Schicht (`c_proj`): Projiziert zurück von 3072 auf `n_embd` (768).

Dies folgt dem von Ihnen erwähnten Muster "fc -> gelu -> projection".

#### Ablauf des Forward Pass
Die Forward Passes sind im Residual-Stil, mit Pre-Norm (LayerNorm vor den Unterschichten). Hier ist eine grobe Aufschlüsselung:

1. **Haupt-Forward (GPT.forward)**:
   - Token-Einbettungen: Eingabe-Tokens (Form `[B, T]`) → Einbettungen (Form `[B, T, n_embd]`).
   - Positionseinbettungen: Werden zu den Token-Einbettungen addiert.
   - Durchlauf durch den Stapel von `n_layer` (12) Transformer-Blöcken: `x = block(x)` für jeden Block.
   - Finale LayerNorm: `x = self.ln_f(x)`.
   - Lineare Projektion: `logits = self.lm_head(x)` → Ausgabeform `[B, T, vocab_size]`.

   Ausschnitt (vereinfacht):
   ```python
   def forward(self, idx, targets=None):
       # ... Einbettung + Position
       for block in self.blocks:
           x = block(x)
       x = self.ln_head(x)
       logits = self.head(x)
       # ... Verlust, falls targets vorhanden
       return logits
   ```

2. **Forward im Transformer-Block (Block.forward)**:
   - Wende `ln1` auf die Eingabe `x` an.
   - Self-Attention: `x = x + attn(ln1(x))` (Residual).
   - Wende `ln2` auf das Ergebnis an.
   - MLP: `x = x + mlp(ln2(x))` (Residual).

   Ausschnitt (vereinfacht):
   ```python
   def forward(self, x):
       x = x + self.attn(self.ln1(x))
       x = x + self.mlp(self.ln2(x))
       return x
   ```

3. **Forward in der Self-Attention (MultiheadAttention.forward)**:
   - LayerNorm-Eingabe → Berechne Q, K, V Projektionen (lineare Schichten `c_attn`).
   - Aufteilen in Köpfe, Anwenden der kausalen Maske, Skaliertes Dot-Product-Attention.
   - Köpfe zusammenführen, mit `c_proj` zurückprojizieren.
   - Residual Addition (wird jedoch im Block von außen addiert).

   Wichtig: Die kausale Maske stellt sicher, dass zukünftige Tokens ignoriert werden. Die Ausgabeform bleibt `[B, T, n_embd]`.

   Ausschnitt (Kern-Berechnung der Attention, vereinfacht):
   ```python
   def forward(self, x):
       B, T, C = x.shape
       qkv = self.c_attn(x).split(self.n_embd, dim=2)  # Q,K,V
       # ... Umformen zu Köpfen, Maske, attn = q @ k.transpose / sqrt
       # attn = attn.masked_fill(mask == 0, -1e9)
       # y = attn @ v
       # ... Zusammenführen und projizieren
       return self.c_proj(y.reshape(B, T, C))
   ```

4. **Forward im MLP (MLP.forward)**:
   - Erste Projektion: `x = self.c_fc(x)` → zur Zwischengröße.
   - GELU: `x = F.gelu(x)`.
   - Zweite Projektion: `x = self.c_proj(x)` → zurück zu `n_embd`.

   Ausschnitt:
   ```python
   def forward(self, x):
       x = self.c_fc(x)
       x = F.gelu(x)
       x = self.c_proj(x)
       return x
   ```

Dieser Aufbau spiegelt die Architektur von GPT-2 eng wider, mit ~124M Parametern in der Standardkonfiguration. Für den exakten Code, siehe das Repo.

[model.py Quelle](https://github.com/karpathy/nanoGPT/blob/master/model.py)