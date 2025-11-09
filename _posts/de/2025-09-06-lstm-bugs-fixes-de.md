---
audio: false
date: 2025-09-06
generated: true
image: false
lang: de
layout: post
title: Fehler und Korrekturen bei der LSTM-Implementierung
translated: true
type: note
---

Verstanden – hier ist eine klare, end-to-end Erklärung, was dieses LSTM-from-scratch-Skript macht, plus die subtilen Fehler, die das Training kaputtmachen, und wie man sie behebt. Ich halte es linear und einfach zu überfliegen (keine breiten Tabellen).

# Was der Code versucht zu tun

Du implementierst ein minimales Character-/Word-Level LSTM Language Model in NumPy:

1. **Setup & Größen**

* `hidden_size`, `vocab_size`, Datensätze (`training_set`, `validation_set`, `test_set`), Token↔Index-Mappings und Funktionen wie `sigmoid`, `tanh`, `softmax`, `one_hot_encode_sequence` werden voraussichtlich aus `data.py` / `utils.py` kommen.
* Der Input jedes Zeitschritts ist ein One-Hot-Vektor `x ∈ R^{vocab_size×1}`.
* Du verkettest den vorherigen Hidden State und den aktuellen Input:
  `z = [h_{t-1}; x_t] ∈ R^{(hidden_size+vocab_size)×1}`.
  Deshalb sind `W_f, W_i, W_g, W_o ∈ R^{hidden_size×(hidden_size+vocab_size)}`.

2. **Parameter-Initialisierung**

* `init_lstm(...)` alloziert Gewichte für die vier Gates (Forget f, Input i, Candidate g, Output o), plus die Output-Projektion `W_v` auf den Vokabularraum.
* `init_orthogonal` macht jede Gewichtsmatrix orthonormal (via QR). Das ist eine gute Wahl für RNNs/LSTMs.

3. **Forward Pass (pro Sequenz)**
   Für jeden Zeitschritt:

* Baue `z = [h_prev; x]`.
* Berechne die Gates:

  * `f_t = σ(W_f z + b_f)`
  * `i_t = σ(W_i z + b_i)`
  * `g_t = tanh(W_g z + b_g)`
  * `C_t = f_t ⊙ C_{t-1} + i_t ⊙ g_t`
  * `o_t = σ(W_o z + b_o)`
  * `h_t = o_t ⊙ tanh(C_t)`
* Projiziere auf Vokabular und Softmax:

  * `v_t = W_v h_t + b_v`
  * `ŷ_t = softmax(v_t)`
* Der Code speichert viele Zwischenwerte (`z_s, f_s, i_s, g_s, C_s, o_s, h_s, v_s, output_s`) für Backprop.

4. **Loss**

* Cross-Entropy bei jedem Schritt mit einem One-Hot-Target:
  `L_t = − log ŷ_t[target]`
  (Der Code verwendet ein elementweises `-mean(log(ŷ)*one_hot)`, was bis auf einen konstanten Skalierungsfaktor äquivalent zu `-log(ŷ[target])` ist.)

5. **Backward Pass (BPTT durch LSTM)**

* Klassische LSTM-Gradienten, akkumuliert von `t = T−1 → 0`.
* Clippe die globale Gradientennorm, dann SGD-Update.

6. **Training Loop**

* Für jede Epoche: Evaluation auf dem Validation Set (nur Loss), dann Training auf dem Training Set (Loss + Grads + Update). Schließlich Plotten der Trainings-/Validation-Losses.

---

# Kritische Probleme (diese werden das Lernen stillschweigend kaputtmachen)

## 1) Off-by-one-Indexierung für `h` und `C` im Backprop

Im `forward` schiebst du zuerst die *initialen* States:

* `h_s[0] = h_init`, dann nach Schritt 0 hängst du `h_0` an → also hat `h_s` die Länge `T+1` mit `h_s[t+1] = h_t`.
* Dasselbe für `C_s`: `C_s[0] = C_init`, dann `C_s[t+1] = C_t`.

Aber in `backward(...)` verwendest du `h[t]` und `C[t]` so, als wären sie `h_t` und `C_t`. Das sind sie nicht; sie sind um eins verschoben.

**Fix (einfache Daumenregel):**

* Verwende `h[t+1]`, wenn du `h_t` willst.
* Verwende `C[t+1]`, wenn du `C_t` willst.
* Für den "vorherigen Zellzustand" willst du `C_prev = C[t]` (nicht `C[t-1]`).

Also innerhalb der `for t in reversed(range(T)):` Schleife:

* Aktueller State: `h_t = h[t+1]`, `C_t = C[t+1]`
* Vorheriger State: `C_{t-1} = C[t]`

Deine aktuelle Zeile:

```python
C_prev = C[t - 1]
```

ist falsch für `t==0` (greift auf das letzte Element zu) und im Allgemeinen um eins daneben. Es muss sein:

```python
C_prev = C[t]       # vorheriger Zellzustand
# und verwende C_t = C[t+1] als "aktuell"
```

Und überall, wo du `h[t]` verwendest und den aktuellen Hidden State meinst, ändere es zu `h[t+1]`.

## 2) Falsche Ableitungen für mehrere Gates

Du wendest manchmal die Nichtlinearität erneut an statt ihrer Ableitung oder vergisst das Derivative-Flag.

* **Zellzustand-Pfad:**
  Korrekt:
  `dC_t += dh_t ⊙ o_t ⊙ (1 - tanh(C_t)^2)`
  Dein Code:

  ```python
  dC += dh * o[t] * tanh(tanh(C[t]), derivative=True)
  ```

  Das ist `tanh` angewendet zweimal. Ersetze mit:

  ```python
  dC += dh * o_t * (1 - np.tanh(C_t)**2)
  ```

* **Forget Gate:**
  Korrekt: `df = dC_t ⊙ C_{t-1} ⊙ f_t ⊙ (1 - f_t)`
  Dein Code:

  ```python
  df = dC * C_prev
  df = sigmoid(f[t]) * df
  ```

  Fehlender Ableitungsterm. Sollte sein:

  ```python
  df = dC * C_prev
  df *= f[t] * (1 - f[t])      # wenn f[t] die σ Pre-Activation Output speichert
  ```

* **Input Gate:**
  Du hast gemacht:

  ```python
  di = dC * g[t]
  di = sigmoid(i[t], True) * di
  ```

  Das ist in Ordnung, **wenn** `sigmoid(x, True)` σ’(x) zurückgibt *nicht* σ(x). Robuster (und wie du `i[t]` als Gate-Output gespeichert hast) ist:

  ```python
  di = dC * g[t]
  di *= i[t] * (1 - i[t])
  ```

* **Candidate Gate:**
  Du hast gemacht:

  ```python
  dg = dC * i[t]
  dg = tanh(g[t], derivative=True) * dg
  ```

  Wenn `g[t]` `tanh(preact)` speichert, dann ist `tanh’(preact) = 1 - g[t]^2`. Also:

  ```python
  dg = dC * i[t]
  dg *= (1 - g[t]**2)
  ```

* **Output Gate:**
  Du hast gemacht:

  ```python
  do = dh * tanh(C[t])
  do = sigmoid(o[t], derivative=True) * do
  ```

  Mit dem Index-Fix (`C_t = C[t+1]`, `o_t = o[t]`) und der Ableitung wie oben:

  ```python
  do = dh * np.tanh(C_t)
  do *= o[t] * (1 - o[t])
  ```

* **Nächster Zell-Gradient:**
  Korrekt:

  ```python
  dC_next = dC * f[t]
  ```

## 3) Verwenden von `h[0]` / `C[0]` zum Dimensionieren von `dh_next` und `dC_next`

Du willst die Shapes des **aktuellen** h/C (Ende-der-Sequenz), nicht die initialen Nullen. Verwende:

```python
dh_next = np.zeros_like(h[-1])
dC_next = np.zeros_like(C[-1])
```

## 4) Arithmetische Stabilität der Cross-Entropy

`loss += -np.mean(np.log(outputs[t]) * targets[t])` ist in Ordnung, wenn `softmax` intern klemmt/epsilons verwendet. Wenn nicht, füge ein kleines Epsilon hinzu:

```python
eps = 1e-12
loss += -np.sum(targets[t] * np.log(outputs[t] + eps))
```

## 5) Training-Stabilitäts-Tweaks

* **Forget-Gate-Bias:** initialisiere `b_f` mit einem positiven Wert (z.B. `1.0`), so dass das LSTM früh im Training dazu neigt, den Speicher zu behalten:

  ```python
  b_f = np.ones((hidden_size, 1)) * 1.0
  ```
* **Lernrate:** `lr=1e-1` mit purem SGD ist aggressiv. Starte mit `1e-2` oder verwende Adam.
* **Gradient Clipping:** Gut. Ziehe pro-Matrix-Normen in Betracht, falls nötig.

---

# Ein korrigierter Kern für die Backprop-Schleife

Diese Skizze zeigt die Indexierungs- und Ableitungsfixes. Sie nimmt an, dass `f[t], i[t], g[t], o[t]` die *Outputs* ihrer Nichtlinearitäten sind (wie in deinem Forward):

```python
T = len(outputs)
dh_next = np.zeros_like(h[-1])
dC_next = np.zeros_like(C[-1])

for t in reversed(range(T)):
    # Kurze Namen mit korrekter Indexierung
    y_hat = outputs[t]                 # softmax output
    y_true = targets[t]
    h_t   = h[t+1]
    C_t   = C[t+1]
    C_tm1 = C[t]

    # Output Layer
    dv = y_hat.copy()
    dv[np.argmax(y_true)] -= 1
    W_v_d += dv @ h_t.T
    b_v_d += dv

    # Backprop in h
    dh = W_v.T @ dv
    dh += dh_next

    # Output Gate
    do = dh * np.tanh(C_t)
    do *= o[t] * (1 - o[t])
    W_o_d += do @ z[t].T
    b_o_d += do

    # Zellzustand
    dC = dC_next + dh * o[t] * (1 - np.tanh(C_t)**2)

    # Candidate (g), Input (i), Forget (f)
    dg = dC * i[t]
    dg *= (1 - g[t]**2)               # da g[t] = tanh(preact)

    di = dC * g[t]
    di *= i[t] * (1 - i[t])

    df = dC * C_tm1
    df *= f[t] * (1 - f[t])

    # Akkumuliere Gate-Gewichts-/Bias-Grads
    W_g_d += dg @ z[t].T;  b_g_d += dg
    W_i_d += di @ z[t].T;  b_i_d += di
    W_f_d += df @ z[t].T;  b_f_d += df

    # Propagiere zu z und splitte zum h_{t-1} Teil
    dz = (W_f.T @ df) + (W_i.T @ di) + (W_g.T @ dg) + (W_o.T @ do)
    dh_next = dz[:hidden_size, :]
    dC_next = dC * f[t]
```

---

# Kleinere aber wichtige Details & Empfehlungen

* **Orthogonale Init:** Gut für rekurrente Gewichte. Für die Input-Teile könntest du auch mit `1/√fan_in` skalieren. Hier nicht kritisch.
* **Batching:** Der Code trainiert mit 1 Sequenz auf einmal (kein Batching). In Ordnung für Klarheit, aber langsam/verrauscht. Mini-Batching würde sorgfältige Shape-Änderungen erfordern.
* **Teacher Forcing:** Du verwendest den Ground-Truth-Next-Token als Target; alles gut. Wenn du jemals Free-Running-Generation machst, sample aus den `softmax`-Outputs und speise sie zurück ins Modell.
* **Loss Reporting:** Du summierst pro-Zeitschritt-Losses über Sequenzen und mittelst dann durch Dataset-Länge; das vermischt Skalen, wenn Sequenzen variabler Länge sind. Ziehe in Betracht, durch totale Tokens zu normalisieren.
* **Plotting:** Funktioniert lokal. In headless Umgebungen, denke daran, Backends zu wechseln oder savefig zu verwenden.

---

# TL;DR der Fixes, die du sofort machen solltest

1. **Indexierung**: Ersetze jedes `h[t]` mit `h[t+1]`, jedes `C[t]` mit `C[t+1]`, und setze `C_prev = C[t]` im Backprop.
2. **Ableitungen**:

   * Verwende `(1 - tanh(C_t)**2)` für den Zellzustandspfad.
   * Verwende `gate * (1 - gate)` für die σ-Gates, da du die Gate-Outputs gespeichert hast.
   * Verwende `(1 - g[t]**2)` für das Candidate Gate, da `g[t]=tanh(preact)`.
3. **Init**: Setze `b_f` auf \~`1.0`.
4. **LR**: Senke auf `1e-2` (oder wechsle zu Adam).
5. **Stabilität**: Füge `eps` in `log` hinzu.

Nimm diese Änderungen vor und dein Loss sollte anfangen, auf eine viel sinnvollere Weise zu sinken. Wenn du willst, poste deinen aktualisierten `backward(...)` und ich mache einen Sanity-Check.