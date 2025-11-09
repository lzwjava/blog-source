---
audio: false
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Calcul du hachage Bitcoin et minage
translated: true
type: note
---

### Comment Bitcoin calcule les hachages

Bitcoin utilise une fonction de hachage cryptographique appelée **SHA-256** (Secure Hash Algorithm 256-bit) pour calculer les hachages. C'est une fonction à sens unique qui prend des données d'entrée (comme l'en-tête d'un bloc) et produit une sortie fixe de 256 bits (32 octets) qui est unique et imprévisible.

- **Qu'est-ce qui est haché ?** Principalement l'en-tête du bloc, qui comprend :
  - Le numéro de version
  - Le hachage du bloc précédent
  - La racine de Merkle (un résumé de toutes les transactions dans le bloc)
  - L'horodatage
  - La cible de difficulté (bits)
  - Le nonce (un nombre que les mineurs ajustent)

- **Le processus :**
  1. Le mineur assemble l'en-tête du bloc.
  2. Applique SHA-256 deux fois : `hachage = SHA256(SHA256(en-tête))`.
  3. Vérifie si le hachage résultant est inférieur à la cible actuelle (par exemple, commence par suffisamment de zéros, comme 000000...).
  4. Sinon, il incrémente le nonce et répète l'opération. C'est la partie de "recherche par essais et erreurs" de la Preuve de Travail (PoW).

Les hachages sont déterministes — la même entrée donne toujours la même sortie — mais de minuscules changements (comme +1 au nonce) produisent des sorties radicalement différentes. Cela rend impossible la rétro-ingénierie des entrées à partir des sorties.

### Pourquoi miner du Bitcoin ? (Et comment cela garantit un plafond d'offre de 21 millions)

Je pense que vous vouliez dire "pourquoi miner" au lieu de "pourquoi frapper" — le minage est le processus de validation des transactions et d'ajout de blocs à la blockchain, récompensé par de nouveaux bitcoins.

- **Pourquoi miner ?**
  - **Sécurité :** Les mineurs sécurisent le réseau en rivalisant pour résoudre les énigmes de la PoW, empêchant des attaques comme la double dépense (dépenser le même BTC deux fois).
  - **Décentralisation :** N'importe qui peut miner, distribuant le contrôle — aucune autorité centrale.
  - **Incitation :** Les mineurs gagnent des **récompenses de bloc** (nouveaux BTC frappés) + les frais de transaction. Cela amorce le réseau et compense les coûts énergétiques.

- **Garantir le plafond d'offre (c'est en fait 21 millions, pas 10 millions) :**
  Le protocole de Bitcoin code en dur une offre totale de **21 millions de BTC**, créés par le biais de récompenses de minage qui **diminuent de moitié** tous les 210 000 blocs (~4 ans).
  - A commencé à 50 BTC par bloc en 2009.
  - Réduit de moitié à 25 en 2012, 12,5 en 2016, 6,25 en 2020, 3,125 en 2024, et ainsi de suite.
  - Le dernier bitcoin sera miné vers 2140 ; après cela, seuls les frais subsisteront.
  - Ceci est appliqué par le code : La formule de récompense est `récompense = 50 * 0.5^(plancher(hauteur_du_bloc / 210000))`. Personne ne peut la changer sans un consensus de 95 % du réseau, rendant l'inflation prévisible et plafonnée.

Cette rareté imite l'or, stimulant la valeur.

### Comment fonctionne la Preuve de Travail (PoW)

La PoW est le mécanisme de consensus de Bitcoin — une énigme computationnelle qui prouve qu'un mineur a investi du "travail" (de la puissance de calcul CPU/GPU/ASIC) pour ajouter un bloc.

- **Étape par étape :**
  1. **Collecter les transactions :** Les mineurs rassemblent les transactions en attente dans un bloc (jusqu'à ~1-4 Mo, selon SegWit).
  2. **Construire l'en-tête :** Inclure la racine de Merkle des transactions, le lien vers le bloc précédent, etc.
  3. **Définir la cible :** Le réseau ajuste la difficulté tous les 2016 blocs pour maintenir un temps de bloc moyen à 10 minutes. Cible = un très petit nombre (par exemple, le hachage doit être < 0x00000000FFFF...).
  4. **Trouver le nonce :** Deviner le nonce par force brute (de 0 à 2^32-1). Pour chaque essai, hacher l'en-tête. Si le hachage < cible, c'est valide !
  5. **Diffuser le bloc :** Les autres nœuds vérifient (facile — il suffit de re-hacher une fois). Si valide, l'ajoutent à la chaîne ; les mineurs commencent le bloc suivant.
  6. **Règle de la chaîne :** La chaîne valide la plus longue l'emporte (résout les fourches).

La PoW rend la vérification des blocs peu coûteuse mais la création de blocs coûteuse, sécurisant contre les attaques à 51 % (contrôler >50 % du taux de hachage pour réécrire l'historique).

### Pourquoi autant de calculs pour une transaction ?

Les transactions ne nécessitent pas directement des calculs massifs de la part des utilisateurs — juste une signature avec votre clé privée (cryptographie à courbe elliptique, rapide). Le gros du travail se fait lors du **minage** :

- **Par bloc, pas par transaction :** Un bloc regroupe ~2 000-3 000 transactions. Les mineurs hachent des billions de fois par bloc pour résoudre la PoW.
- **Ajustement de la difficulté :** Plus de mineurs rejoignent le réseau (taux de hachage total plus élevé), plus la difficulté augmente exponentiellement pour maintenir des blocs de 10 minutes. Le taux de hachage global actuel est d'environ ~600 EH/s (exahachages/seconde) — c'est 600 quintillions de hachages par seconde !
- **Pourquoi ce "gaspillage" ?**
  - **Coût de la sécurité :** Une forte computation rend les attaques non rentables. Réécrire un bloc coûte le re-calcul de toute la PoW suivante.
  - **Résistance Sybil :** Empêche l'inondation du réseau avec de fausses identités.
  - **Compromis :** Gourmand en énergie (Bitcoin utilise ~150 TWh/an, comme un pays de taille moyenne), mais les partisans soutiennent que c'est une caractéristique nécessaire pour une monnaie sans confiance.

Les utilisateurs paient des frais pour prioriser leurs transactions dans les blocs ; celles avec des frais faibles attendent.

Si vous pensiez à quelque chose de spécifique (comme le matériel pour le minage), faites-le moi savoir !

**Références :**  
[Livre Blanc de Bitcoin](https://bitcoin.org/bitcoin.pdf)  
[Bitcoin Wiki : Preuve de Travail](https://en.bitcoin.it/wiki/Proof_of_work)  
[Blockchain.com : Réduction de moitié du Bitcoin](https://www.blockchain.com/learning-crypto/bitcoin-halving)