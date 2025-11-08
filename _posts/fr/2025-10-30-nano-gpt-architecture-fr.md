---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Résumé de l'Architecture du Modèle NanoGPT
translated: true
type: note
---

### Aperçu de l'architecture du modèle NanoGPT

NanoGPT implémente un modèle de transformeur décodeur uniquement, similaire à GPT-2, en PyTorch. L'architecture est définie dans le fichier `model.py`, avec une configuration `GPTConfig` qui permet de définir les hyperparamètres. La configuration par défaut (par exemple, pour la variante "gpt2") utilise :

- **Nombre de blocs de transformeur** : 12 (`n_layer = 12`)
- **Dimension d'embedding (taille de couche)** : 768 (`n_embd = 768`)
- **Nombre de têtes d'attention** : 12 (`n_head = 12`)
- **Taille intermédiaire du MLP** : 3072 (`n_embd * 4`, car le facteur d'expansion est 4)

Chaque bloc de transformeur (classe `Block`) est un bloc décodeur standard avec des connexions résiduelles et une normalisation de couche. Il inclut :
- **LayerNorm 1** (`ln1`) : Appliqué avant l'auto-attention.
- **Auto-Attention Multi-Têtes** (`attn`) : Attention causale (masquée) pour empêcher de regarder les tokens futurs.
- Addition résiduelle après l'attention.
- **LayerNorm 2** (`ln2`) : Appliqué avant le MLP.
- **MLP** (`mlp`) : Un simple réseau feed-forward.
- Addition résiduelle après le MLP.

Le modèle global (classe `GPT`) empile ces 12 blocs après les embeddings de token et de position, suivis d'une LayerNorm finale (`ln_f`) et d'une projection linéaire vers la taille du vocabulaire.

#### Structure du MLP
Le MLP (classe `MLP` dans `Block`) est un réseau feed-forward à deux couches :
- Première couche linéaire (`c_fc`) : Projette de `n_embd` (768) à la taille intermédiaire (3072).
- Activation GELU : Appliquée élément par élément après la première projection.
- Deuxième couche linéaire (`c_proj`) : Reprojette de 3072 vers `n_embd` (768).

Cela suit le modèle "fc -> gelu -> projection" que vous avez mentionné.

#### Flux de la Passe Avant (Forward Pass)
Les passes avant sont de style résiduel, avec pre-norm (LayerNorm avant les sous-couches). Voici une description de haut niveau :

1. **Passe Avant Principale (GPT.forward)** :
   - Embeddings de token : Tokens d'entrée (forme `[B, T]`) → embeddings (forme `[B, T, n_embd]`).
   - Embeddings positionnels : Ajoutés aux embeddings de token.
   - Passage à travers la pile de `n_layer` (12) blocs de transformeur : `x = block(x)` pour chaque bloc.
   - LayerNorm finale : `x = self.ln_f(x)`.
   - Projection linéaire : `logits = self.lm_head(x)` → forme de sortie `[B, T, vocab_size]`.
   
   Extrait (simplifié) :
   ```python
   def forward(self, idx, targets=None):
       # ... embedding + positional
       for block in self.blocks:
           x = block(x)
       x = self.ln_head(x)
       logits = self.head(x)
       # ... loss if targets
       return logits
   ```

2. **Passe Avant dans le Bloc de Transformeur (Block.forward)** :
   - Appliquer `ln1` à l'entrée `x`.
   - Auto-attention : `x = x + attn(ln1(x))` (résiduel).
   - Appliquer `ln2` au résultat.
   - MLP : `x = x + mlp(ln2(x))` (résiduel).
   
   Extrait (simplifié) :
   ```python
   def forward(self, x):
       x = x + self.attn(self.ln1(x))
       x = x + self.mlp(self.ln2(x))
       return x
   ```

3. **Passe Avant dans l'Auto-Attention (MultiheadAttention.forward)** :
   - Entrée LayerNorm → calcul des projections Q, K, V (couches linéaires `c_attn`).
   - Séparer en têtes, appliquer le masque causal, attention scaled dot-product.
   - Concaténer les têtes, reprojeter avec `c_proj`.
   - Addition résiduelle (mais dans le bloc, elle est ajoutée à l'extérieur).
   
   Clé : Le masque causal garantit que les tokens futurs sont ignorés. La forme de sortie est préservée en `[B, T, n_embd]`.
   
   Extrait (calcul central de l'attention, simplifié) :
   ```python
   def forward(self, x):
       B, T, C = x.shape
       qkv = self.c_attn(x).split(self.n_embd, dim=2)  # Q,K,V
       # ... remodeler en têtes, masquer, attn = q @ k.transpose / sqrt
       # attn = attn.masked_fill(mask == 0, -1e9)
       # y = attn @ v
       # ... concaténer et projeter
       return self.c_proj(y.reshape(B, T, C))
   ```

4. **Passe Avant dans le MLP (MLP.forward)** :
   - Première projection : `x = self.c_fc(x)` → vers la taille intermédiaire.
   - GELU : `x = F.gelu(x)`.
   - Deuxième projection : `x = self.c_proj(x)` → retour vers `n_embd`.
   
   Extrait :
   ```python
   def forward(self, x):
       x = self.c_fc(x)
       x = F.gelu(x)
       x = self.c_proj(x)
       return x
   ```

Cette configuration reflète étroitement l'architecture de GPT-2, avec ~124M de paramètres dans la configuration par défaut. Pour le code exact, consultez le dépôt.

[source model.py](https://github.com/karpathy/nanoGPT/blob/master/model.py)