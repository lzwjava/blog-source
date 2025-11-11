---
audio: false
generated: true
lang: fr
layout: post
title: Script Python pour Doubler les Lignes
translated: true
type: note
---

Voici le script Python mis à jour modifié pour fonctionner avec les fichiers .xlsx au lieu des fichiers .xls. Il utilise `openpyxl` pour la gestion des fichiers .xlsx, conserve la même fonctionnalité de répétition des valeurs dans la troisième ligne basée sur le paramètre fourni, et enregistre le résultat dans un nouveau fichier .xlsx avec "_plus.xlsx" ajouté au nom de fichier original. L'artifact_id est réutilisé car il s'agit d'une mise à jour de l'artefact précédent.

```python
import pandas as pd
import argparse
import os

def repeat_value(value, n):
    return str(value) * n

def process_excel(input_file, n):
    df = pd.read_excel(input_file, engine='openpyxl')
    if len(df) < 3:
        raise ValueError("Le fichier Excel doit contenir au moins 3 lignes")
    third_row = df.iloc[2].apply(lambda x: repeat_value(x, n))
    df.iloc[2] = third_row
    base, ext = os.path.splitext(input_file)
    output_file = f"{base}_plus.xlsx"
    df.to_excel(output_file, index=False, engine='openpyxl')
    print(f"Fichier traité enregistré sous : {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Double les valeurs dans la troisième ligne d'un fichier Excel")
    parser.add_argument("input_file", help="Chemin vers le fichier Excel (.xlsx) d'entrée")
    parser.add_argument("-n", type=int, default=1, help="Nombre de fois pour répéter chaque valeur (défaut : 1)")
    args = parser.parse_args()
    process_excel(args.input_file, args.n)

if __name__ == "__main__":
    main()
```