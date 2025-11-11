---
audio: false
generated: true
lang: fr
layout: post
title: Comparaison de deux fichiers CSV à ligne unique
translated: true
type: note
---

Voici un script Python qui compare deux fichiers CSV à une seule ligne contenant des chaînes de caractères (par exemple, "P0001") et identifie :
- Les éléments communs (présents dans les deux fichiers)
- Les éléments uniques au premier fichier
- Les éléments uniques au deuxième fichier

Le script utilise `argparse` pour accepter deux chemins de fichiers CSV, lit la première ligne de chacun, effectue une comparaison basée sur des ensembles et écrit les résultats dans `comparison.txt`.

```python
#!/usr/bin/env python3
import argparse
import csv
import os

def main():
    # Configuration de l'analyseur d'arguments
    parser = argparse.ArgumentParser(description='Compare deux fichiers CSV à une seule ligne pour identifier les éléments communs et uniques')
    parser.add_argument('file1_path', help='Chemin vers le premier fichier CSV')
    parser.add_argument('file2_path', help='Chemin vers le deuxième fichier CSV')
    
    # Analyse des arguments
    args = parser.parse_args()
    
    try:
        # Lire la première ligne du premier fichier CSV
        with open(args.file1_path, 'r') as file1:
            reader1 = csv.reader(file1)
            for row in reader1:
                values1 = row
                break
        
        # Lire la première ligne du deuxième fichier CSV
        with open(args.file2_path, 'r') as file2:
            reader2 = csv.reader(file2)
            for row in reader2:
                values2 = row
                break
        
        # Conversion en ensembles pour la comparaison
        set1 = set(values1)
        set2 = set(values2)
        
        # Trouver les éléments communs et uniques
        common_items = set1.intersection(set2)
        unique_to_file1 = set1.difference(set2)
        unique_to_file2 = set2.difference(set1)
        
        # Déterminer le répertoire de sortie (utiliser le répertoire du premier fichier)
        output_dir = os.path.dirname(args.file1_path) or '.'
        output_file = os.path.join(output_dir, 'comparison.txt')
        
        # Écrire les résultats dans le fichier de sortie
        with open(output_file, 'w') as file:
            file.write("Résultats de la comparaison :\n\n")
            
            file.write("Éléments communs (dans les deux fichiers) :\n")
            if common_items:
                for item in sorted(common_items):
                    file.write(f"{item}\n")
            else:
                file.write("Aucun\n")
                
            file.write("\nÉléments uniquement dans le premier fichier :\n")
            if unique_to_file1:
                for item in sorted(unique_to_file1):
                    file.write(f"{item}\n")
            else:
                file.write("Aucun\n")
                
            file.write("\nÉléments uniquement dans le deuxième fichier :\n")
            if unique_to_file2:
                for item in sorted(unique_to_file2):
                    file.write(f"{item}\n")
            else:
                file.write("Aucun\n")
        
        print(f"Comparaison terminée. Résultats sauvegardés dans {output_file}")
        
    except FileNotFoundError as e:
        print(f"Erreur : Fichier non trouvé - {e}")
    except Exception as e:
        print(f"Erreur : {e}")

if __name__ == "__main__":
    main()
```

### Fonctionnement :
1. **Entrée** : Prend deux chemins de fichiers CSV via des arguments de ligne de commande.
2. **Lecture** : Lit uniquement la première ligne de chaque fichier CSV.
3. **Comparaison** :
   - Convertit les lignes en ensembles pour une comparaison efficace.
   - Trouve :
     - **Éléments communs** : Éléments présents dans les deux lignes (intersection d'ensembles).
     - **Uniques au premier fichier** : Éléments uniquement dans la première ligne (différence d'ensembles : fichier1 - fichier2).
     - **Uniques au deuxième fichier** : Éléments uniquement dans la deuxième ligne (différence d'ensembles : fichier2 - fichier1).
4. **Sortie** : Écrit les résultats dans `comparison.txt` dans le répertoire du premier fichier, listant :
   - Les éléments communs
   - Les éléments uniquement dans le premier fichier
   - Les éléments uniquement dans le deuxième fichier
   - Chaque section est triée par ordre alphabétique ; "Aucun" est écrit si une section est vide.
5. **Gestion des erreurs** : Capture les erreurs de fichier non trouvé et autres exceptions.

### Exemple d'utilisation :
Sauvegardez le script sous `compare_csv.py`. Créez deux fichiers CSV, par exemple :
- `file1.csv` : `P0001,P0002,P0003`
- `file2.csv` : `P0001,P0004,P0003`

Exécutez le script :
```
python compare_csv.py file1.csv file2.csv
```

**Sortie** (`comparison.txt`) :
```
Résultats de la comparaison :

Éléments communs (dans les deux fichiers) :
P0001
P0003

Éléments uniquement dans le premier fichier :
P0002

Éléments uniquement dans le deuxième fichier :
P0004
```

### Notes :
- Le script ignore la position des éléments et se concentre uniquement sur la présence/absence.
- Les éléments en double dans une ligne sont automatiquement gérés (les ensembles suppriment les doublons).
- La sortie est écrite dans `comparison.txt` dans le répertoire du premier fichier d'entrée.
- Si un fichier est vide ou n'a pas de ligne, le script le traitera comme un ensemble vide.

Souhaitez-vous que je modifie le script (par exemple, changer le format de sortie ou ajouter plus de détails) ?