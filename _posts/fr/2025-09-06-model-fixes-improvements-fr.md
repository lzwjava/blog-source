---
audio: false
date: 2025-09-06
generated: true
image: false
lang: fr
layout: post
title: Corrections et améliorations du modèle
translated: true
type: note
---

Voici ce que fait votre script, étape par étape, ainsi que quelques corrections importantes que vous voudrez probablement apporter.

# Qu'est-ce que le modèle

* Vous définissez un **prédicteur de token suivant au niveau caractère/mot** minimal :

  * `nn.LSTM(input_size=vocab_size, hidden_size=50, num_layers=1)` traite une séquence de vecteurs one-hot (taille = `vocab_size`) et produit un état caché de taille 50 à chaque pas de temps.
  * `nn.Linear(50, vocab_size, bias=False)` transforme l'état caché de chaque pas de temps en **logits sur le vocabulaire**.

# Formes de tenseur attendues (critique)

La forme d'entrée par défaut du LSTM PyTorch est **(seq\_len, batch\_size, input\_size)** car vous n'avez pas défini `batch_first=True`.

* Pour une seule séquence dans un lot de taille 1 :

  * Les entrées du LSTM doivent être `(seq_len, 1, vocab_size)`.
  * Le LSTM produit une sortie `x` de forme `(seq_len, 1, hidden_size)`.
  * Vous appliquez ensuite `view(-1, hidden_size)` → `(seq_len, hidden_size)` pour que la couche linéaire produise `(seq_len, vocab_size)`.
  * `CrossEntropyLoss` attend :

    * `outputs` : `(N, C)` = `(seq_len, vocab_size)`
    * `targets` : `(N,)` = `(seq_len,)` indices des tokens

# L'endroit où votre code risque de poser problème (forme)

Vous faites :

```python
inputs_one_hot = inputs_one_hot.permute(0, 2, 1)
```

Si `one_hot_encode_sequence` retourne `(batch, seq_len, vocab)`, la permutation correcte pour le LSTM par défaut est **`permute(1, 0, 2)`** (pour obtenir `(seq_len, batch, vocab)`). Votre `permute(0,2,1)` actuel donne `(batch, vocab, seq_len)`, ce qui est incompatible et provoquera soit une erreur, soit un apprentissage silencieusement incorrect si la forme initiale est différente de celle supposée.

Deux options propres (choisissez une) :

**A) Garder le LSTM par défaut (batch\_second) :**

```python
# veut (seq_len, batch, input_size)
inputs_one_hot = inputs_one_hot.permute(1, 0, 2)  # (seq_len, 1, vocab_size)
```

**B) Le mettre en batch-first (souvent plus simple) :**

```python
self.lstm = nn.LSTM(input_size=vocab_size, hidden_size=50, batch_first=True)
# veut (batch, seq_len, input_size)
# puis NE PAS permuter ; laisser tel quel (1, seq_len, vocab_size)
```

# Logique de la boucle d'entraînement

* Vous maintenez deux sommes courantes par époque : `epoch_training_loss` et `epoch_validation_loss`.
* **Phase de validation** (`net.eval()` + pas d'étape de gradient) :

  * Pour chaque (inputs, targets) dans `validation_set` :

    * encoder les entrées en one-hot, convertir les cibles en indices
    * passe forward → logits `(seq_len, vocab_size)` (en supposant les formes corrigées)
    * perte CE contre les indices cibles de forme `(seq_len,)`
    * accumulation de la perte
* **Phase d'entraînement** (`net.train()`) :

  * Même prétraitement
  * forward → perte → `optimizer.zero_grad()` → `loss.backward()` → `optimizer.step()`
* Vous enregistrez les pertes moyennes et les affichez tous les 5 epochs.

# Inférence et affichage

* Vous prenez un échantillon de `test_set`, exécutez le modèle, obtenez les logits pour chaque pas de temps, prenez `argmax` par pas de temps → tokens prédits.
* Vous affichez les mots d'entrée, les mots cibles et les mots prédits.
* Vous tracez la perte d'entraînement vs la perte de validation sur les époques.

# Petites améliorations à fort impact

1. **Corriger la forme d'entrée** (le plus important). Utilisez l'une des options A ou B ci-dessus. Si vous choisissez batch-first, modifiez la passe forward comme suit :

   ```python
   x, (h, c) = self.lstm(x)         # x: (batch, seq, hidden)
   x = x.reshape(-1, self.lstm.hidden_size)  # (batch*seq, hidden)
   ```
2. **Utiliser `with torch.no_grad()` pour l'évaluation/l'inférence** pour éviter le suivi des gradients et pour la vitesse/la mémoire :

   ```python
   net.eval()
   with torch.no_grad():
       outputs = net(inputs_one_hot)
       loss = criterion(outputs, targets_idx)
   ```

   Et pour la conversion numpy :

   ```python
   outputs = net(inputs_one_hot).detach().numpy()
   ```
3. **Grainer PyTorch aussi** pour la reproductibilité :

   ```python
   torch.manual_seed(42)
   ```
4. **Gestion du device** (si vous utilisez le GPU) :

   ```python
   device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
   net.to(device)
   inputs_one_hot = inputs_one_hot.to(device)
   targets_idx = targets_idx.to(device)
   ```
5. **Alignement des cibles** : assurez-vous que `targets` sont les **tokens suivants** alignés avec chaque pas de temps d'entrée. Si votre jeu de données associe `(inputs, targets)` de cette façon, c'est bon. Sinon, créez `targets = inputs[1:]` et supprimez la dernière entrée ou procédez de manière similaire.
6. **Supprimer `.bias=False` sauf raison particulière** ; un biais sur la couche de sortie est généralement inoffensif/utile.
7. **Remplissage/longueurs variables** (optionnel) : si les séquences ont des longueurs variables, envisagez `pack_padded_sequence` pour éviter l'entraînement sur les tokens de remplissage.
8. **Surveillance** : la précision sur les prédictions du token suivant peut être plus interprétable que la seule perte — calculez le `% de argmax correct` sur la validation.

# Extrait corrigé minimal (version batch-first)

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

# ... dans votre boucle, supprimez le permute ; assurez-vous que inputs_one_hot est (batch, seq, vocab)
# la validation/l'inférence utilisent `with torch.no_grad()` et `.detach()`
```

Si vous partagez la forme exacte que `one_hot_encode_sequence` retourne (par exemple, `(seq, vocab)` vs `(1, seq, vocab)`), je peux adapter précisément les lignes de permute/reshape pour votre cas.