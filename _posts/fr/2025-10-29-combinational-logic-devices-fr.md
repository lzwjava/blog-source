---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Vue d'ensemble des dispositifs de logique combinatoire
translated: true
type: note
---

### Aperçu
La vidéo de "The Learning Circuit" explique les dispositifs logiques combinatoires, qui génèrent des sorties uniquement en fonction des entrées actuelles (aucune mémoire des états passés). Elle couvre quatre types clés : les multiplexeurs (MUX), les démultiplexeurs (DEMUX), les encodeurs et les décodeurs. Ceux-ci sont essentiels pour le routage des signaux, la compression/expansion des données et le contrôle numérique en électronique.

### Multiplexeurs (MUX)
- **Objectif** : Comme un standard téléphonique numérique — sélectionne une entrée parmi plusieurs pour l'envoyer vers une seule sortie, contrôlé par des lignes de sélection.
- **Exemple de base (74LS157 Quad 2-to-1 MUX)** :
  - 4 canaux, chacun avec des entrées A et B, une broche de sélection (S) et une broche d'activation (E).
  - S haut : Sélectionne les entrées A ; S bas : Sélectionne les entrées B.
  - E bas : Active la sortie ; E haut : Désactive (les sorties passent à l'état bas).
- **Exemples plus grands** :
  - MUX 4-vers-1 : 2 lignes de sélection choisissent parmi 4 entrées.
  - MUX 8-vers-1 : 3 lignes de sélection ; une seule entrée passe.
- **Astuce** : La forme générale est \\(2^n\\)-vers-1, où \\(n\\) est le nombre de lignes de sélection.

### Démultiplexeurs (DEMUX)
- **Objectif** : Opposé du MUX — achemine une entrée vers une sortie parmi plusieurs, en fonction des lignes de sélection.
- **Exemple de base (DEMUX 1-vers-2)** :
  - Une ligne de sélection (S) : S bas → entrée vers Y0 ; S haut → entrée vers Y1.
- **Règle générale** : \\(1\\)-vers-\\(2^n\\) sorties, correspondant aux lignes de sélection du MUX (par exemple, 2 sélections → 4 sorties).

### Encodeurs
- **Objectif** : Compresse plusieurs entrées en une sortie codée (par exemple, binaire).
- **Encodeur binaire de base** :
  - Exemple : 4 entrées → sortie binaire 2 bits (par exemple, entrée 3 active → sortie 11).
  - Problème : Plusieurs entrées actives peuvent causer des conflits (sortie ambiguë).
- **Encodeur de priorité** (Corrige les Conflits) :
  - Attribue une priorité (la plus haute prime sur les autres).
  - Exemple (8 entrées, actif à l'état bas) : Entrée 7 (la plus haute) active → sortie 111, ignore les entrées inférieures.
  - Aucune entrée active → sortie 000.

### Décodeurs
- **Objectif** : Développe une entrée codée en plusieurs sorties (par exemple, active des lignes spécifiques).
- **Décodeur binaire de base** :
  - Comme un DEMUX : Une entrée binaire sélectionne une sortie (par exemple, entrée 2 bits 10 → active la sortie 2).
- **Décodeur BCD vers 7 segments** :
  - Entrée BCD 4 bits (0–9) → Contrôle 7 segments LED pour l'affichage des chiffres.
  - Exemples : "0" allume 6 segments ; "1" allume 2 (barres de droite).
- **Décodeur BCD vers Décimal** :
  - Entrée 4 bits → Active une sortie parmi 10 (pour les chiffres 0–9).

### Points Clés à Retenir
- **MUX/DEMUX** : Routeurs de données (directeurs de trafic).
- **Encodeurs** : Plus d'entrées que de sorties (compression de données, comme zipper).
- **Décodeurs** : Plus de sorties que d'entrées (expansion de données, comme dézipper).
- Tous sont "combinatoires" — la sortie change instantanément avec les entrées, pas d'horloge ni de stockage.

[How Combinational Logic Devices Work - The Learning Circuit](https://www.youtube.com/watch?v=gsmB7J72Tgc)