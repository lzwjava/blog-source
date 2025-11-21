---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Longueur de la plus longue sous-chaîne de caractères uniques
translated: true
type: note
---

**Problème** : Trouver la longueur de la plus longue sous-chaîne sans caractères répétés.

**Solution** : Fenêtre glissante + HashMap (ou tableau puisque lettres minuscules)

Nous utilisons deux pointeurs (`left` et `right`) pour maintenir une fenêtre `[left, right]`.  
Lorsque nous déplaçons `right`, nous vérifions si `s[right]` est déjà apparu dans la fenêtre courante :
- Si oui, déplacez `left` vers l'avant jusqu'à ce que le doublon soit supprimé.
- Suivez la position où chaque caractère a été vu pour la dernière fois pour déplacer `left` directement.

Cela s'exécute en temps **O(n)** et espace **O(1)** (au plus 26 ou 128 caractères).

```python
def lengthOfLongestSubstring(s: str) -> int:
    if not s:
        return 0
    
    # char -> dernier index vu
    last_seen = {}
    max_len = 0
    left = 0
    
    for right in range(len(s)):
        ch = s[right]
        
        # Si le caractère est déjà dans la fenêtre courante, réduire depuis la gauche
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1
        else:
            # Mettre à jour la longueur max lorsque la fenêtre est valide
            max_len = max(max_len, right - left + 1)
        
        # Enregistrer la dernière position de ce caractère
        last_seen[ch] = right
    
    return max_len
```

### Cas de test

```python
print(lengthOfLongestSubstring("abacabcbb"))  # 3 ("abc" ou "bac")
print(lengthOfLongestSubstring("bbbbb"))      # 1 ("b")
print(lengthOfLongestSubstring("pwwkew"))     # 3 ("wke")
```

**Explication des exemples** :
- "abacabcbb" → "abc" ou "bac" longueur = 3
- "bbbbb" → seulement "b" longueur = 1
- "pwwkew" → "wke" longueur = 3 (note : "pwke" est aussi valide, mais "ww" la casse plus tôt)

Vous pouvez aussi utiliser une liste de taille 128 au lieu d'un dict pour un temps constant légèrement plus rapide si vous savez que le jeu de caractères est ASCII.