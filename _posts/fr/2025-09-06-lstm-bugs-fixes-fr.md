---
audio: false
date: 2025-09-06
generated: true
image: false
lang: fr
layout: post
title: Bogues et correctifs d'implémentation de LSTM
translated: true
type: note
---

Compris — voici une explication claire et complète de ce que fait ce script LSTM-from-scratch, ainsi que les bugs subtils qui vont compromettre l'entraînement et comment les corriger. Je vais garder cela linéaire et facile à parcourir (pas de tableaux larges).

# Ce que le code essaie de faire

Vous implémentez un modèle de langage LSTM minimal au niveau caractère/mot dans NumPy :

1.  **Configuration & tailles**

* `hidden_size`, `vocab_size`, jeux de données (`training_set`, `validation_set`, `test_set`), mappings token↔index, et fonctions comme `sigmoid`, `tanh`, `softmax`, `one_hot_encode_sequence` sont censés provenir de `data.py` / `utils.py`.
* L'entrée à chaque pas de temps est un vecteur one-hot `x ∈ R^{vocab_size×1}`.
* Vous concaténez l'état caché précédent et l'entrée courante :
  `z = [h_{t-1}; x_t] ∈ R^{(hidden_size+vocab_size)×1}`.
  C'est pourquoi `W_f, W_i, W_g, W_o ∈ R^{hidden_size×(hidden_size+vocab_size)}`.

2.  **Initialisation des paramètres**

* `init_lstm(...)` alloue les poids pour les quatre portes (forget f, input i, candidate g, output o), plus la projection de sortie `W_v` vers le vocabulaire.
* `init_orthogonal` rend chaque matrice de poids orthonormale (via QR). C'est un choix correct pour les RNNs/LSTMs.

3.  **Forward pass (par séquence)**
    Pour chaque pas de temps :

* Construire `z = [h_prev; x]`.
* Calculer les portes :

  * `f_t = σ(W_f z + b_f)`
  * `i_t = σ(W_i z + b_i)`
  * `g_t = tanh(W_g z + b_g)`
  * `C_t = f_t ⊙ C_{t-1} + i_t ⊙ g_t`
  * `o_t = σ(W_o z + b_o)`
  * `h_t = o_t ⊙ tanh(C_t)`
* Projeter vers le vocabulaire et softmax :

  * `v_t = W_v h_t + b_v`
  * `ŷ_t = softmax(v_t)`
* Le code stocke beaucoup d'intermédiaires (`z_s, f_s, i_s, g_s, C_s, o_s, h_s, v_s, output_s`) pour la rétropropagation.

4.  **Loss**

* Entropie croisée à chaque pas avec une cible one-hot :
  `L_t = − log ŷ_t[target]`
  (Le code utilise un `-mean(log(ŷ)*one_hot)` élément par élément, ce qui est équivalent à `-log(ŷ[target])` à une constante multiplicative près.)

5.  **Backward pass (BPTT through LSTM)**

* Gradients LSTM classiques, accumulés de `t = T−1 → 0`.
* Écrêtage de la norme du gradient global, puis mise à jour SGD.

6.  **Boucle d'entraînement**

* Pour chaque epoch : évaluation sur le jeu de validation (seulement la loss), puis entraînement sur le jeu d'entraînement (loss + grads + update). Enfin, tracé des losses d'entraînement/validation.

---

# Problèmes critiques (ceux-ci vont silencieusement casser l'apprentissage)

## 1) Indexation décalée de 1 pour `h` et `C` en backprop

Dans `forward`, vous poussez d'abord les états *initiaux* :

* `h_s[0] = h_init`, puis après l'étape 0 vous ajoutez `h_0` → donc `h_s` a une longueur `T+1` avec `h_s[t+1] = h_t`.
* Idem pour `C_s` : `C_s[0] = C_init`, puis `C_s[t+1] = C_t`.

Mais dans `backward(...)` vous utilisez `h[t]` et `C[t]` comme s'ils étaient `h_t` et `C_t`. Ce n'est pas le cas ; ils sont décalés de un.

**Correctif (règle simple) :**

* Utilisez `h[t+1]` où vous voulez `h_t`.
* Utilisez `C[t+1]` où vous voulez `C_t`.
* Pour "l'état de cellule précédent" vous voulez `C_prev = C[t]` (pas `C[t-1]`).

Donc à l'intérieur de la boucle `for t in reversed(range(T)):` :

* État courant : `h_t = h[t+1]`, `C_t = C[t+1]`
* État précédent : `C_{t-1} = C[t]`

Votre ligne actuelle :

```python
C_prev = C[t - 1]
```

est fausse pour `t==0` (accède au dernier élément) et décalée en général. Cela doit être :

```python
C_prev = C[t]       # état de cellule précédent
# et utiliser C_t = C[t+1] comme "courant"
```

Et partout où vous utilisez `h[t]` en voulant l'état caché courant, changez pour `h[t+1]`.

## 2) Dérivées incorrectes pour plusieurs portes

Vous réappliquez parfois la non-linéarité au lieu de sa dérivée, ou oubliez le flag de dérivée.

* **Chemin de l'état de cellule :**
  Correct :
  `dC_t += dh_t ⊙ o_t ⊙ (1 - tanh(C_t)^2)`
  Votre code :

  ```python
  dC += dh * o[t] * tanh(tanh(C[t]), derivative=True)
  ```

  C'est `tanh` appliqué deux fois. Remplacez par :

  ```python
  dC += dh * o_t * (1 - np.tanh(C_t)**2)
  ```

* **Porte d'oubli :**
  Correct : `df = dC_t ⊙ C_{t-1} ⊙ f_t ⊙ (1 - f_t)`
  Votre code :

  ```python
  df = dC * C_prev
  df = sigmoid(f[t]) * df
  ```

  Il manque le terme de dérivée. Devrait être :

  ```python
  df = dC * C_prev
  df *= f[t] * (1 - f[t])      # si f[t] stocke la sortie post-σ
  ```

* **Porte d'entrée :**
  Vous avez fait :

  ```python
  di = dC * g[t]
  di = sigmoid(i[t], True) * di
  ```

  C'est correct **si** `sigmoid(x, True)` retourne σ'(x) *et non pas* σ(x). Plus robuste (en cohérence avec le fait que vous stockez `i[t]` comme la sortie de la porte) est :

  ```python
  di = dC * g[t]
  di *= i[t] * (1 - i[t])
  ```

* **Porte candidate :**
  Vous avez fait :

  ```python
  dg = dC * i[t]
  dg = tanh(g[t], derivative=True) * dg
  ```

  Si `g[t]` stocke `tanh(preact)`, alors `tanh’(preact) = 1 - g[t]^2`. Donc :

  ```python
  dg = dC * i[t]
  dg *= (1 - g[t]**2)
  ```

* **Porte de sortie :**
  Vous avez fait :

  ```python
  do = dh * tanh(C[t])
  do = sigmoid(o[t], derivative=True) * do
  ```

  Avec la correction d'indexation (`C_t = C[t+1]`, `o_t = o[t]`) et la dérivée comme ci-dessus :

  ```python
  do = dh * np.tanh(C_t)
  do *= o[t] * (1 - o[t])
  ```

* **Gradient de cellule suivant :**
  Correct :

  ```python
  dC_next = dC * f[t]
  ```

## 3) Utiliser `h[0]` / `C[0]` pour dimensionner `dh_next` et `dC_next`

Vous voulez les formes de h/C **courants** (fin de séquence), pas les zéros initiaux. Utilisez :

```python
dh_next = np.zeros_like(h[-1])
dC_next = np.zeros_like(C[-1])
```

## 4) Stabilité numérique de l'entropie croisée

`loss += -np.mean(np.log(outputs[t]) * targets[t])` sera correct si `softmax` utilise un clamping/epsilon interne. Sinon, ajoutez un petit epsilon :

```python
eps = 1e-12
loss += -np.sum(targets[t] * np.log(outputs[t] + eps))
```

## 5) Ajustements pour la stabilité de l'entraînement

* **Biais de la porte d'oubli :** initialisez `b_f` à une valeur positive (p.ex. `1.0`) pour qu'au début de l'entraînement le LSTM ait tendance à garder la mémoire :

  ```python
  b_f = np.ones((hidden_size, 1)) * 1.0
  ```
* **Taux d'apprentissage :** `lr=1e-1` avec du SGD brut est agressif. Commencez à `1e-2` ou utilisez Adam.
* **Écrêtage du gradient :** Bon. Envisagez des normes par matrice si nécessaire.

---

# Un cœur corrigé pour la boucle de backprop

Cet aperçu montre les corrections d'indexation et de dérivées. Il suppose que `f[t], i[t], g[t], o[t]` sont les *sorties* de leurs non-linéarités (comme dans votre forward) :

```python
T = len(outputs)
dh_next = np.zeros_like(h[-1])
dC_next = np.zeros_like(C[-1])

for t in reversed(range(T)):
    # Noms courts avec indexation correcte
    y_hat = outputs[t]                 # sortie softmax
    y_true = targets[t]
    h_t   = h[t+1]
    C_t   = C[t+1]
    C_tm1 = C[t]

    # Couche de sortie
    dv = y_hat.copy()
    dv[np.argmax(y_true)] -= 1
    W_v_d += dv @ h_t.T
    b_v_d += dv

    # Rétropropagation dans h
    dh = W_v.T @ dv
    dh += dh_next

    # Porte de sortie
    do = dh * np.tanh(C_t)
    do *= o[t] * (1 - o[t])
    W_o_d += do @ z[t].T
    b_o_d += do

    # État de cellule
    dC = dC_next + dh * o[t] * (1 - np.tanh(C_t)**2)

    # Candidate (g), Entrée (i), Oubli (f)
    dg = dC * i[t]
    dg *= (1 - g[t]**2)               # puisque g[t] = tanh(preact)

    di = dC * g[t]
    di *= i[t] * (1 - i[t])

    df = dC * C_tm1
    df *= f[t] * (1 - f[t])

    # Accumuler les grads des poids/biais des portes
    W_g_d += dg @ z[t].T;  b_g_d += dg
    W_i_d += di @ z[t].T;  b_i_d += di
    W_f_d += df @ z[t].T;  b_f_d += df

    # Propager vers z et séparer la partie h_{t-1}
    dz = (W_f.T @ df) + (W_i.T @ di) + (W_g.T @ dg) + (W_o.T @ do)
    dh_next = dz[:hidden_size, :]
    dC_next = dC * f[t]
```

---

# Détails plus petits mais importants & recommandations

* **Initialisation orthogonale :** Bonne pour les poids récurrents. Pour les parties entrée, vous pourriez aussi mettre à l'échelle par `1/√fan_in`. Pas critique ici.
* **Batching :** Le code entraîne sur 1 séquence à la fois (pas de batching). Correct pour la clarté, mais lent/bruyant. Le mini-batching nécessiterait des changements de forme minutieux.
* **Teacher forcing :** Vous utilisez le token suivant vérité terrain comme cible ; tout est bon. Si vous faites de la génération libre, échantillonnez à partir des sorties `softmax` et réinjectez dans le modèle.
* **Reporting de la loss :** Vous sommez les losses par pas de temps à travers les séquences puis moyennez par la longueur du jeu de données ; cela mélange les échelles si les séquences varient en longueur. Envisagez de normaliser par le nombre total de tokens.
* **Tracé des courbes :** Fonctionne localement. Dans les environnements sans interface graphique, pensez à changer de backend ou à utiliser `savefig`.

---

# TL;DR des correctifs à appliquer immédiatement

1.  **Indexation** : Remplacez chaque `h[t]` par `h[t+1]`, chaque `C[t]` par `C[t+1]`, et définissez `C_prev = C[t]` dans le backprop.
2.  **Dérivées** :

    * Utilisez `(1 - tanh(C_t)**2)` pour le chemin de l'état de cellule.
    * Utilisez `gate * (1 - gate)` pour les portes σ puisque vous avez stocké les sorties des portes.
    * Utilisez `(1 - g[t]**2)` pour la porte candidate puisque `g[t]=tanh(preact)`.
3.  **Init** : Définissez `b_f` à \~`1.0`.
4.  **LR** : Descendez à `1e-2` (ou passez à Adam).
5.  **Stabilité** : Ajoutez `eps` dans `log`.

Apportez ces modifications et votre loss devrait commencer à décroître de manière bien plus sensée. Si vous voulez, collez votre `backward(...)` mise à jour et je la vérifierai rapidement.