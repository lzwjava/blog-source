---
audio: false
generated: true
lang: fr
layout: post
title: 'Vérification de Fichier qBittorrent : Hachage SHA-1'
translated: true
type: note
---

Lorsque vous déplacez des fichiers dans qBittorrent et qu'il vérifie à nouveau les fichiers avant de partager (seeding), il s'assure que les fichiers dans le nouvel emplacement sont identiques à ceux avec lesquels il travaillait à l'origine. Cette vérification est essentielle dans le torrenting pour éviter de partager des données incorrectes ou corrompues. Voici comment le processus fonctionne et quel algorithme il utilise :

### Comment qBittorrent vérifie les fichiers
qBittorrent ne fait pas simplement confiance au fait que les fichiers déplacés sont corrects — il vérifie leur intégrité en les comparant aux informations stockées dans le fichier torrent. Dans le torrenting, les données sont divisées en petits morceaux appelés **pieces**, et chaque pièce a une valeur de hachage unique. Ces hachages sont inclus dans le fichier torrent et servent d'empreinte digitale pour chaque morceau de données. Lorsque vous déplacez des fichiers vers un nouvel emplacement, qBittorrent utilise ces hachages de pièces pour confirmer que les fichiers n'ont pas changé.

Le processus peut être décomposé en ces étapes :

1. **Spécifier le nouvel emplacement** : Vous indiquez à qBittorrent où se trouvent désormais les fichiers en définissant le nouveau chemin d'accès.
2. **Mapper les fichiers au torrent** : qBittorrent fait correspondre les fichiers du nouvel emplacement aux fichiers listés dans le torrent, généralement en utilisant les noms et les tailles des fichiers (car ces informations sont dans le fichier torrent).
3. **Vérifier les hachages des pièces** : qBittorrent lit les données des nouveaux fichiers pièce par pièce, calcule un hachage pour chaque pièce et le compare au hachage correspondant stocké dans le fichier torrent.
4. **Confirmer l'intégrité** : Si tous les hachages calculés correspondent aux hachages du torrent, les fichiers sont confirmés comme étant identiques et qBittorrent peut reprendre le partage. Si le hachage d'une pièce ne correspond pas, cette pièce est marquée comme incomplète ou manquante, et qBittorrent devra peut-être la retélécharger.

### Quel algorithme utilise-t-il ?
qBittorrent n'utilise pas une somme de contrôle (checksum) de fichier complet (comme MD5 ou SHA-256 pour l'ensemble du fichier), car cela serait lent et inefficace, surtout pour les gros fichiers. Au lieu de cela, il s'appuie sur les **hachages de pièces** définis par le protocole BitTorrent. L'algorithme utilisé pour ces hachages de pièces est **SHA-1**, une fonction de hachage cryptographique largement utilisée. Chaque morceau de données (qui peut faire quelques kilo-octets à quelques mégaoctets, selon le torrent) est haché avec SHA-1, et ce sont ces hachages que qBittorrent vérifie.

L'utilisation de hachages de pièces au lieu d'une somme de contrôle de fichier complet présente deux grands avantages :
- **Efficacité** : Vérifier de petites pièces est plus rapide que de hacher un fichier entier.
- **Granularité** : Si quelque chose ne va pas, qBittorrent peut identifier exactement quelles pièces doivent être réparées, plutôt que de rejeter l'ensemble du fichier.

### Pourquoi c'est important
Cette vérification basée sur le hachage garantit que les données que vous partagez depuis le nouvel emplacement correspondent à ce que les autres pairs attendent, préservant ainsi l'intégrité de l'essaim (swarm) torrent. Sans cette vérification, le déplacement de fichiers pourrait entraîner le partage de données corrompues ou non concordantes, ce qui perturberait le processus de torrenting.

En bref, lorsque vous déplacez des fichiers dans qBittorrent, il revérifie les fichiers en calculant les **hachages SHA-1** de chaque pièce et en les comparant aux hachages du fichier torrent. C'est ainsi qu'il confirme que tout est correct avant que le partage ne reprenne.

---

Pour démontrer comment qBittorrent vérifie l'intégrité des fichiers en utilisant les hachages de pièces (spécifiquement les hachages SHA-1) lors du déplacement de fichiers, voici un script Python simple. qBittorrent, suivant le protocole BitTorrent, divise les fichiers en pièces, calcule les hachages SHA-1 pour chaque pièce et utilise ces hachages pour s'assurer que le contenu du fichier reste inchangé, quel que soit son emplacement. Ce script simule ce processus en créant un fichier d'exemple, en calculant les hachages de ses pièces, en vérifiant une copie identique, puis en montrant comment une modification entraîne un échec de la vérification.

### Explication
- **Hachages de pièces** : Le script divise un fichier en pièces de taille fixe (par exemple, 10 octets) et calcule les hachages SHA-1 pour chaque pièce, imitant la façon dont un fichier torrent stocke ces hachages.
- **Vérification** : Il vérifie si les hachages calculés d'un fichier correspondent aux hachages attendus, garantissant ainsi l'intégrité.
- **Simulation** : Il crée un fichier, le copie (simulant un déplacement), le vérifie, puis modifie la copie et vérifie à nouveau pour montrer comment les changements sont détectés.

Voici le script avec des commentaires pour plus de clarté :

```python
import hashlib
import shutil
import os

def compute_piece_hashes(file_path, piece_size):
    """Calcule les hachages SHA-1 pour chaque pièce du fichier."""
    hashes = []
    with open(file_path, 'rb') as f:
        while True:
            piece = f.read(piece_size)
            if not piece:
                break
            hash_obj = hashlib.sha1(piece)
            hashes.append(hash_obj.hexdigest())
    return hashes

def verify_file_integrity(file_path, piece_size, expected_hashes):
    """Vérifie l'intégrité du fichier en comparant les hachages des pièces."""
    current_hashes = compute_piece_hashes(file_path, piece_size)
    if len(current_hashes) != len(expected_hashes):
        return False
    for current, expected in zip(current_hashes, expected_hashes):
        if current != expected:
            return False
    return True

# Créer un fichier d'exemple avec un contenu connu
with open('file1.txt', 'w') as f:
    f.write("Hello, this is a test file.")

piece_size = 10  # octets, petit pour la démonstration

# Calculer les hachages attendus à partir de file1.txt (simule les hachages du torrent)
expected_hashes = compute_piece_hashes('file1.txt', piece_size)
print("Hachages attendus :", [h[:8] for h in expected_hashes])  # Affiche les 8 premiers caractères pour la lisibilité

# Copier file1.txt vers file2.txt pour simuler le déplacement du fichier
shutil.copyfile('file1.txt', 'file2.txt')

# Vérifier file2.txt par rapport aux hachages attendus (devrait réussir)
is_valid = verify_file_integrity('file2.txt', piece_size, expected_hashes)
print("Vérification de file2.txt (inchangé) :", "Valide" if is_valid else "Invalide")

# Modifier file2.txt pour simuler une corruption ou un changement
with open('file2.txt', 'a') as f:
    f.write(" Modified")

# Vérifier à nouveau (devrait échouer en raison du contenu modifié)
is_valid = verify_file_integrity('file2.txt', piece_size, expected_hashes)
print("Vérification de file2.txt (modifié) :", "Valide" if is_valid else "Invalide")

# Nettoyer les fichiers créés
os.remove('file1.txt')
os.remove('file2.txt')
```

### Comment cela fonctionne
1. **Création du fichier** : Écrit "Hello, this is a test file." (25 octets) dans `file1.txt`.
2. **Calcul du hachage** : Divise `file1.txt` en pièces de 10 octets chacune (par exemple, "Hello, thi", "s is a tes", "t file."), calcule les hachages SHA-1 et les stocke comme `expected_hashes`.
3. **Simuler un déplacement** : Copie `file1.txt` vers `file2.txt`, représentant un fichier déplacé vers un nouvel emplacement.
4. **Vérification initiale** : Vérifie `file2.txt` par rapport à `expected_hashes`. Comme le contenu est identique, il affiche "Valide".
5. **Modification** : Ajoute " Modified" à `file2.txt`, modifiant son contenu et sa taille (maintenant 34 octets, divisés en 4 pièces).
6. **Deuxième vérification** : Vérifie le `file2.txt` modifié. Le nombre de pièces ou leurs hachages diffèrent, donc il affiche "Invalide".
7. **Nettoyage** : Supprime les fichiers temporaires.

### Exemple de sortie
```
Hachages attendus : ['dffd6021', 'a2b3c4d5', 'e6f789ab']  # Exemples de préfixes de hachage
Vérification de file2.txt (inchangé) : Valide
Vérification de file2.txt (modifié) : Invalide
```
(Les valeurs de hachage réelles varieront mais suivront ce modèle.)

Ce script illustre comment qBittorrent assure l'intégrité des fichiers en comparant les hachages des pièces, détectant tout changement même après le déplacement d'un fichier, ce qui en fait une démonstration simple mais efficace du processus.