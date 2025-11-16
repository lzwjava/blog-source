---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Formation sur une salade de mots aléatoire
translated: true
type: note
---

Si vous entraînez un petit modèle comme nanoGPT (ou n'importe quel transformateur similaire à GPT-2 small) sur 2–3 Go de **mots aléatoires ressemblant à de l'anglais** (c'est-à-dire des séquences de vrais mots anglais choisis uniformément au hasard, sans grammaire, sans signification, juste un salmigondis de mots), voici ce qui se passera réellement :

### Le modèle apprendra qu'il n'y a **aucune structure** à apprendre
- Il découvrira très rapidement la distribution des tokens (les fréquences unigrammes des mots).
- Il se rendra compte que le mot suivant est essentiellement indépendant des mots précédents (ou très proche de l'indépendance).
- La perplexité sur les données d'entraînement atteindra un plancher extrêmement rapidement (après quelques époques, elle sera déjà proche de l'entropie de la distribution uniforme des mots).
- Le modèle se transformera essentiellement en un **échantillonneur unigramme** — il produira simplement des mots selon leur fréquence marginale dans les données d'entraînement, avec une dépendance au contexte presque nulle.

### Le texte généré sera légèrement meilleur qu'un pur non-sens, mais restera complètement incohérent
Exemple de ce que vous obtiendrez après l'entraînement :

> the cat quickly under yesterday apple banana elephant running purple however tomorrow cheese lightning quickly zebra sandwich forever mountain bicycle orange elephant yesterday banana

Il va :
- Utiliser de vrais mots anglais ✓
- Respecter les fréquences des mots (les mots courants comme "the", "and", "to" apparaîtront souvent) ✓
- Avoir une orthographe parfaite ✓
- Être 100 % incohérent grammaticalement et sémantiquement ✗

Il n'apprendra **pas** :
- La grammaire ou la syntaxe
- La structure des phrases
- Le placement des mots fonctionnels
- Une quelconque forme de signification ou de cohérence thématique
- Même les bigrammes/trigrammes au-delà d'un faible bruit statistique

### Comparaison avec un entraînement sur du texte réel
Lorsque vous entraînez nanoGPT sur du texte réel (par exemple, Shakespeare ou OpenWebText), même avec seulement 2–3 Go, vous commencez à voir émerger de véritables phrases étonnamment rapidement parce qu'il existe une structure riche et prévisible.

Avec des mots purement aléatoires, vous ne franchirez jamais le seuil de la cohérence — peu importe la durée de l'entraînement. Le modèle converge presque immédiatement vers "le mot suivant est aléatoire selon la fréquence" et cesse de s'améliorer.

### Expérience amusante que vous pouvez réellement essayer
Vous pouvez générer un tel jeu de données facilement :

```python
import random
words = open('big-wordlist.txt').read().splitlines()  # par ex., 300k mots anglais
with open('random_3gb.txt', 'w') as f:
    for _ in range(500_000_000):  # ~3 Go
        f.write(random.choice(words) + ' ')
```

Entraînez nanoGPT dessus pendant quelques heures. Vous verrez la perte chuter à ~4–5 nats (ce qui est essentiellement l'entropie de la distribution des mots anglais) puis s'aplatir complètement. L'échantillonnage par la suite donnera exactement le salmigondis de mots ci-dessus.

### Conclusion
Oui, le texte généré sera un pur non-sens — juste un non-sens légèrement plus "naturel" que si vous échantillonniez des mots uniformément à partir d'un dictionnaire, car il correspondra aux fréquences réelles des mots. Mais il ne dira jamais rien de même vaguement significatif ou grammatical.

C'est en fait un excellent moyen de vous prouver à quel point le langage réel repose sur des dépendances à long terme et une structure — parce que lorsque vous retirez tout cela, même une architecture puissante comme GPT n'apprend essentiellement rien d'utile.