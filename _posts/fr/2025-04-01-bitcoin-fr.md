---
audio: false
generated: true
lang: fr
layout: post
title: Comment fonctionne le Bitcoin
translated: true
type: note
---

D'un point de vue technique, Bitcoin fonctionne grâce à une combinaison de cryptographie, d'un réseau pair-à-pair et d'un mécanisme de consensus appelé Preuve de Travail (PoW). Voici une explication des composants et processus clés :

**1. Fondations cryptographiques :**

* **Hachage (SHA-256) :** Bitcoin repose largement sur la fonction de hachage cryptographique SHA-256. Cette fonction prend n'importe quelle donnée en entrée et produit une sortie de taille fixe de 256 bits (le hash). Les propriétés clés de SHA-256 utilisées dans Bitcoin incluent :
    * **Déterministe :** La même entrée produit toujours la même sortie.
    * **À sens unique :** Il est informatiquement impossible d'inverser le processus et de retrouver l'entrée à partir de la sortie.
    * **Résistant aux collisions :** Il est extrêmement difficile de trouver deux entrées différentes qui produisent la même sortie de hachage.
* **Signatures numériques (ECDSA) :** Bitcoin utilise l'Algorithme de Signature Numérique à Courbe Elliptique (ECDSA) pour sécuriser les transactions. Chaque utilisateur de Bitcoin possède une paire de clés cryptographiques :
    * **Clé privée :** Une clé secrète qui permet à l'utilisateur d'autoriser (signer) les transactions.
    * **Clé publique :** Une clé dérivée de la clé privée qui peut être partagée avec d'autres. Elle est utilisée pour vérifier l'authenticité des transactions signées par la clé privée correspondante.
* **Adresses Bitcoin :** Elles sont dérivées des clés publiques via une série d'étapes de hachage et d'encodage. Ce sont les « adresses » que les utilisateurs partagent pour recevoir des Bitcoins.

**2. La Blockchain :**

* **Registre distribué :** Bitcoin maintient un registre public et décentralisé appelé la blockchain. Ce registre enregistre chaque transaction Bitcoin de manière chronologique et transparente.
* **Blocs :** Les transactions sont regroupées en blocs. Chaque bloc contient :
    * Un ensemble de transactions vérifiées.
    * Une référence au hash du **bloc précédent** dans la chaîne. Cela crée la structure en chaîne.
    * Un **nonce** : Un nombre aléatoire utilisé dans le processus de minage.
    * Un **horodatage**.
    * Le hash du bloc actuel lui-même.
* **Immuabilité :** Une fois qu'un bloc est ajouté à la blockchain, il devient extrêmement difficile de le modifier car cela nécessiterait de recalculer les hashs de ce bloc et de tous les blocs suivants, ce qui serait informatiquement impossible pour un attaquant contrôlant moins de 51 % de la puissance de calcul du réseau.

**3. Transactions :**

* **Structure :** Une transaction Bitcoin comprend généralement :
    * **Inputs (Entrées) :** Des références à des transactions précédentes où l'expéditeur a reçu les Bitcoins qu'il dépense maintenant. Ce sont essentiellement des pointeurs vers des « sorties de transaction non dépensées » spécifiques (UTXO).
    * **Outputs (Sorties) :** Spécifient l'adresse Bitcoin du ou des destinataires et le montant de Bitcoin envoyé à chacun. Une transaction peut avoir plusieurs sorties.
    * **Signature :** Une signature numérique créée à l'aide de la clé privée de l'expéditeur. Cela prouve que le propriétaire des Bitcoins a autorisé la transaction.
* **Diffusion :** Une fois qu'une transaction est créée et signée, elle est diffusée sur le réseau pair-à-pair Bitcoin.

**4. Minage et Preuve de Travail :**

* **Mineurs :** Ce sont des nœuds du réseau Bitcoin qui effectuent le travail de vérification et d'ajout de nouvelles transactions à la blockchain.
* **Vérification des transactions :** Les mineurs collectent les transactions en attente et non confirmées sur le réseau et vérifient leur validité (par exemple, en s'assurant que l'expéditeur a suffisamment de Bitcoins à dépenser et que les signatures numériques sont valides).
* **Création d'un bloc :** Les mineurs regroupent ces transactions vérifiées dans un nouveau bloc. Ils incluent également une transaction spéciale appelée « transaction coinbase » qui leur attribue des Bitcoins nouvellement créés ainsi que les frais de transaction payés par les expéditeurs des transactions incluses dans le bloc.
* **Preuve de Travail (PoW) :** Pour ajouter un nouveau bloc à la blockchain, les mineurs doivent résoudre un puzzle informatiquement difficile en utilisant l'algorithme SHA-256. Ce processus est appelé « minage ».
    * Les mineurs modifient de manière répétée le **nonce** (un nombre aléatoire) dans l'en-tête du bloc.
    * Pour chaque nonce, ils calculent le hash SHA-256 de l'ensemble de l'en-tête du bloc.
    * L'objectif est de trouver un nonce qui donne un hash commençant par un certain nombre de zéros. Le nombre de zéros requis est déterminé par la **difficulté** du réseau Bitcoin.
    * Trouver un tel hash est une question d'essais et d'erreurs et nécessite une puissance de calcul importante.
* **Validation du bloc et consensus :** Une fois qu'un mineur trouve un hash valide (la « preuve de travail »), il diffuse le nouveau bloc au reste du réseau. Les autres nœuds du réseau vérifient ensuite :
    * Que les transactions dans le bloc sont valides.
    * Que le hash du bloc est correct.
    * Que le hash respecte l'objectif de difficulté actuel.
    * Que la référence au hash du bloc précédent est correcte.
* **Ajout à la Blockchain :** Si le bloc est valide, les autres nœuds l'acceptent et l'ajoutent à leur copie de la blockchain, prolongeant ainsi la chaîne. Ce processus garantit que tous les nœuds s'accordent sur l'ordre et la validité des transactions. La chaîne la plus longue est considérée comme la version faisant autorité.

**5. Incitations :**

* **Récompense de bloc :** Les mineurs qui réussissent à miner un nouveau bloc sont récompensés par une certaine quantité de Bitcoin nouvellement créé (actuellement 3,125 BTC, qui est divisée par deux environ tous les quatre ans lors d'un événement appelé « halving »).
* **Frais de transaction :** Les mineurs perçoivent également les frais de transaction que les utilisateurs incluent volontairement lors de l'envoi de Bitcoins. Ces frais incitent les mineurs à prioriser certaines transactions.

**6. Décentralisation et Sécurité :**

* **Réseau Pair-à-Pair :** Bitcoin fonctionne sur un réseau pair-à-pair décentralisé, ce qui signifie qu'il n'y a aucune autorité centrale qui le contrôle. Les transactions et les blocs sont propagés sur de nombreux ordinateurs à travers le monde.
* **Résistance à la censure :** Parce que la blockchain est distribuée et nécessite une puissance de calcul importante pour être modifiée, il est très difficile pour une seule entité de censurer des transactions ou de contrôler le réseau.
* **Sécurité par la cryptographie :** L'utilisation d'une cryptographie robuste garantit la sécurité et l'intégrité des transactions et de la blockchain. Les clés privées permettent aux utilisateurs de contrôler leurs Bitcoins, et les signatures numériques empêchent la falsification des transactions. Le mécanisme de Preuve de Travail rend très coûteux, en termes de calcul, pour des acteurs malveillants de réécrire l'historique des transactions.

**En résumé, le fonctionnement technique de Bitcoin repose sur une interaction sophistiquée de techniques cryptographiques, d'un registre distribué et transparent, et d'un mécanisme de consensus informatiquement intensif pour assurer la sécurité, l'immuabilité et la décentralisation.**