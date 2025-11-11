---
audio: false
generated: true
lang: fr
layout: post
title: Messages de journal propres
translated: true
type: note
---

```python
import sys
import argparse
from difflib import SequenceMatcher

def clean_log(input_path=None, output_path=None, similarity_threshold=1.0, lines_to_compare=1):
    """
    Lit un fichier journal, supprime les lignes de journal standard consécutives dupliquées basées sur la similarité,
    et écrit le journal nettoyé dans un fichier spécifié, en écrasant par défaut le fichier d'entrée.

    Args:
        input_path (str, optional): Chemin vers le fichier journal d'entrée. Si None, lit depuis stdin.
        output_path (str, optional): Chemin vers le fichier journal de sortie. Si None, écrase le fichier d'entrée.
        similarity_threshold (float, optional): Ratio de similarité (0.0 à 1.0) pour considérer les lignes comme dupliquées. Par défaut 1.0 (correspondance exacte).
        lines_to_compare (int, optional): Nombre de lignes consécutives à comparer. Par défaut 1.
    """

    if not isinstance(lines_to_compare, int) or lines_to_compare < 1:
        raise ValueError("lines_to_compare doit être un entier supérieur ou égal à 1.")

    # Déterminer la source d'entrée
    if input_path:
        try:
            with open(input_path, 'r') as infile:
                lines = infile.readlines()
        except FileNotFoundError:
            print(f"Erreur : Fichier non trouvé au chemin : {input_path}", file=sys.stderr)
            sys.exit(1)
    else:
        lines = sys.stdin.readlines()  # Lire toutes les lignes depuis stdin

    # Déterminer la destination de sortie
    if output_path:
        try:
            outfile = open(output_path, 'w')
        except IOError:
            print(f"Erreur : Impossible d'ouvrir le fichier en écriture : {output_path}", file=sys.stderr)
            sys.exit(1)
    elif input_path:
        try:
            outfile = open(input_path, 'w')  # Écraser le fichier d'entrée
        except IOError:
            print(f"Erreur : Impossible d'ouvrir le fichier en écriture : {input_path}", file=sys.stderr)
            sys.exit(1)
    else:
        outfile = sys.stdout  # Par défaut stdout si pas de input_path

    num_lines = len(lines)
    i = 0
    removed_lines = 0
    while i < num_lines:
        # Collecter 'lines_to_compare' lignes ou les lignes restantes si moins de 'lines_to_compare'
        current_lines = lines[i:min(i + lines_to_compare, num_lines)]

        # Traiter seulement si nous avons assez de lignes à comparer
        if len(current_lines) == lines_to_compare:
            # Extraire les informations standard de la première série de lignes
            current_standards = []
            all_standard = True
            for line in current_lines:
                parts = line.split(" | ", 3)
                if len(parts) == 4:
                    level, _, thread, message = parts
                    current_standards.append((thread, message))
                else:
                    print(f"Ligne non standard : {line.strip()}")
                    print(line, end='', file=outfile)
                    all_standard = False
                    break  # Arrêter le traitement de ce groupe si une ligne non standard est trouvée

            if all_standard:
                # Extraire les informations standard de la deuxième série de lignes (si disponible)
                next_lines_start_index = i + lines_to_compare
                next_lines_end_index = min(next_lines_start_index + lines_to_compare, num_lines)
                next_lines = lines[next_lines_start_index:next_lines_end_index]

                if len(next_lines) == lines_to_compare:
                    next_standards = []
                    for line in next_lines:
                        parts = line.split(" | ", 3)
                        if len(parts) == 4:
                            level, _, thread, message = parts
                            next_standards.append((thread, message))
                        else:
                            # Traiter les lignes suivantes comme non standard si l'une d'elles est non standard
                            next_standards = None
                            break

                    if next_standards:
                        similarity = SequenceMatcher(None, ' '.join([' '.join(x) for x in current_standards]), ' '.join([' '.join(x) for x in next_standards])).ratio()
                        print(f"Similarité : {similarity:.4f}, Seuil : {similarity_threshold:.4f}")

                        if similarity < similarity_threshold:
                            for line in current_lines:
                                print(line, end='', file=outfile)
                        else:
                            print(f"Ignorer les lignes dupliquées : { ''.join([line.strip() for line in current_lines])}")
                            removed_lines += len(current_lines)
                    else:
                        for line in current_lines:
                            print(line, end='', file=outfile)
                else:
                    for line in current_lines:
                        print(line, end='', file=outfile)
            i += lines_to_compare  # Passer à la série de lignes suivante
        else:
            # Gérer les lignes restantes (moins de 'lines_to_compare')
            for line in current_lines:
                parts = line.split(" | ", 3)
                if len(parts) == 4:
                    print(line, end='', file=outfile)
                else:
                    print(f"Ligne non standard : {line.strip()}")
                    print(line, end='', file=outfile)
            i += len(current_lines)

    if output_path or input_path:
        outfile.close()

    print(f"Supprimé {removed_lines} lignes dupliquées.")


def is_valid_similarity_threshold(value):
    """
    Vérifier si la valeur donnée est un seuil de similarité valide.
    """
    try:
        value = float(value)
    except ValueError:
        raise argparse.ArgumentTypeError("Le seuil de similarité doit être un nombre à virgule flottante.")
    if 0.0 <= value <= 1.0:
        return value
    else:
        raise argparse.ArgumentTypeError("Le seuil de similarité doit être entre 0.0 et 1.0.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Nettoyer les lignes de journal dupliquées d'un fichier ou stdin et écrire dans un fichier, en écrasant par défaut le fichier d'entrée.")
    parser.add_argument("input_path", nargs="?", type=str, help="Chemin vers le fichier journal d'entrée (optionnel, par défaut stdin)")
    parser.add_argument("-o", "--output_path", type=str, help="Chemin vers le fichier journal de sortie (optionnel, par défaut écrase le fichier d'entrée)")
    parser.add_argument("-s", "--similarity", type=is_valid_similarity_threshold, default=1.0, help="Seuil de similarité (0.0-1.0) pour considérer les lignes comme dupliquées (défaut : 1.0)")
    parser.add_argument("-l", "--lines", type=int, default=1, help="Nombre de lignes consécutives à comparer (défaut : 1)")

    args = parser.parse_args()

    clean_log(args.input_path, args.output_path, args.similarity, args.lines)
```

Ce script Python `clean_log.py` est conçu pour supprimer les lignes de journal dupliquées d'un fichier ou de l'entrée standard. Il utilise un seuil de similarité pour déterminer si les lignes de journal consécutives sont suffisamment similaires pour être considérées comme des doublons.

Voici une analyse du code :

**1. Imports :**

- `sys` : Utilisé pour interagir avec l'interpréteur Python, comme lire depuis stdin et écrire vers stderr.
- `argparse` : Utilisé pour créer une interface en ligne de commande.
- `difflib.SequenceMatcher` : Utilisé pour comparer la similarité entre des séquences de chaînes de caractères.

**2. Fonction `clean_log` :**

- Prend `input_path`, `output_path`, `similarity_threshold` et `lines_to_compare` comme arguments.
- `input_path` : Spécifie le fichier journal d'entrée. Si `None`, il lit depuis stdin.
- `output_path` : Spécifie le fichier de sortie. Si `None` et `input_path` est donné, il écrase le fichier d'entrée. Si les deux sont `None`, il écrit vers stdout.
- `similarity_threshold` : Un float entre 0.0 et 1.0 qui détermine le ratio de similarité minimum pour que les lignes soient considérées comme des doublons. Une valeur de 1.0 signifie que seules les lignes identiques sont supprimées.
- `lines_to_compare` : Un entier spécifiant le nombre de lignes consécutives à comparer pour la similarité.

- **Gestion de l'entrée :**
    - Lit les lignes depuis le fichier d'entrée ou stdin.
    - Gère `FileNotFoundError` si le fichier d'entrée n'existe pas.

- **Gestion de la sortie :**
    - Ouvre le fichier de sortie en écriture ou utilise stdout.
    - Gère `IOError` si le fichier de sortie ne peut pas être ouvert.

- **Logique de suppression des doublons :**
    - Itère à travers les lignes du fichier journal par blocs de `lines_to_compare`.
    - Pour chaque bloc :
        - Divise chaque ligne en parties basées sur le délimiteur " | ", en attendant quatre parties : niveau, horodatage, thread et message.
        - Si une ligne n'a pas quatre parties, elle est considérée comme une ligne "non standard" et est imprimée dans la sortie sans comparaison.
        - Si toutes les lignes du bloc courant sont standard, il les compare aux `lines_to_compare` lignes suivantes.
        - Il utilise `SequenceMatcher` pour calculer le ratio de similarité entre les chaînes jointes des parties thread et message des blocs courant et suivant.
        - Si le ratio de similarité est inférieur au `similarity_threshold`, le bloc de lignes courant est imprimé dans la sortie.
        - Si le ratio de similarité est supérieur ou égal au `similarity_threshold`, le bloc de lignes courant est considéré comme un doublon et est ignoré.
    - Gère les lignes restantes à la fin du fichier (moins de `lines_to_compare` lignes).

- **Statistiques :**
    - Garde une trace du nombre de lignes supprimées.
    - Imprime le nombre de lignes supprimées dans la console.

- **Fermeture du fichier :**
    - Ferme le fichier de sortie s'il a été ouvert.

**3. Fonction `is_valid_similarity_threshold` :**

- Une fonction d'aide utilisée par `argparse` pour valider l'argument du seuil de similarité.
- Elle vérifie si la valeur d'entrée est un float entre 0.0 et 1.0.

**4. Bloc `if __name__ == "__main__":` :**

- Ce bloc est exécuté lorsque le script est lancé depuis la ligne de commande.
- Il utilise `argparse` pour créer un analyseur d'arguments en ligne de commande.
- Il définit les arguments suivants :
    - `input_path` : Le chemin vers le fichier journal d'entrée (optionnel).
    - `-o` ou `--output_path` : Le chemin vers le fichier journal de sortie (optionnel).
    - `-s` ou `--similarity` : Le seuil de similarité (défaut : 1.0).
    - `-l` ou `--lines` : Le nombre de lignes à comparer (défaut : 1).
- Il analyse les arguments de ligne de commande en utilisant `parser.parse_args()`.
- Il appelle la fonction `clean_log` avec les arguments analysés.

**En résumé, le script fournit un moyen flexible de nettoyer les fichiers journal en supprimant les lignes dupliquées basées sur un seuil de similarité configurable et un nombre de lignes à comparer. Il supporte la lecture depuis stdin, l'écriture vers stdout, et l'écrasement du fichier d'entrée.**