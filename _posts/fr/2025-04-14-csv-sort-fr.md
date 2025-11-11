---
audio: false
generated: true
lang: fr
layout: post
title: Script de Tri CSV
translated: true
type: note
---

Je vais créer un script Python qui utilise argparse pour analyser un chemin de fichier CSV, trier une seule ligne de valeurs séparées par des virgules par ordre alphabétique, et sortir le résultat dans un fichier nommé "name_sorted.csv".

```python
#!/usr/bin/env python3
import argparse
import csv
import os

def main():
    # Configurer l'analyseur d'arguments
    parser = argparse.ArgumentParser(description='Trier un fichier CSV à une seule ligne par ordre alphabétique')
    parser.add_argument('file_path', help='Chemin vers le fichier CSV d\'entrée')
    
    # Analyser les arguments
    args = parser.parse_args()
    
    try:
        # Obtenir le répertoire et le nom du fichier
        file_dir = os.path.dirname(args.file_path)
        file_name = os.path.basename(args.file_path)
        
        # Créer le nom du fichier de sortie
        base_name, ext = os.path.splitext(file_name)
        output_file = os.path.join(file_dir, f"{base_name}_sorted{ext}")
        
        # Lire le fichier CSV d'entrée
        with open(args.file_path, 'r') as file:
            reader = csv.reader(file)
            # Obtenir seulement la première ligne
            for row in reader:
                values = row
                break
        
        # Trier les valeurs par ordre alphabétique
        sorted_values = sorted(values)
        
        # Écrire dans le fichier de sortie
        with open(output_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(sorted_values)
        
        print(f"Valeurs triées avec succès et sauvegardées dans {output_file}")
        
    except FileNotFoundError:
        print(f"Erreur : Fichier '{args.file_path}' non trouvé")
    except Exception as e:
        print(f"Erreur : {e}")

if __name__ == "__main__":
    main()
```

Ce script :
1. Utilise argparse pour obtenir le chemin du fichier d'entrée
2. Ouvre le fichier CSV et lit seulement la première ligne
3. Trie les valeurs par ordre alphabétique
4. Écrit les valeurs triées dans "name_sorted.csv"

Pour exécuter le script, sauvegardez-le dans un fichier (par exemple "sort_csv.py"), rendez-le exécutable si nécessaire, et exécutez-le avec le chemin vers votre fichier CSV :

```
python sort_csv.py chemin/vers/votre/fichier.csv
```

Souhaitez-vous que j'explique une partie du code plus en détail ?