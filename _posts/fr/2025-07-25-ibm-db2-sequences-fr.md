---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast:free
title: Guide d'utilisation des séquences IBM DB2
translated: true
type: note
---

### Utilisation des séquences IBM DB2 avec NEXT VALUE FOR

Dans IBM DB2, `NEXT VALUE FOR` est utilisé pour récupérer la valeur suivante d'une séquence, qui génère des numéros uniques et incrémentiels. Les séquences sont utiles pour générer des clés primaires ou d'autres identifiants uniques.

#### Exemple : Création et utilisation d'une séquence
1. **Créer la séquence** (exécuter ceci une seule fois dans votre environnement DB2) :
   ```sql
   CREATE SEQUENCE my_sequence
   START WITH 1
   INCREMENT BY 1
   NO CYCLE;
   ```
   - Ceci crée une séquence nommée `my_sequence` commençant à 1 et s'incrémentant de 1 à chaque fois.

2. **Utiliser la séquence dans une instruction INSERT** pour obtenir la valeur suivante :
   ```sql
   INSERT INTO employees (id, name, department)
   VALUES (NEXT VALUE FOR my_sequence, 'Alice Johnson', 'Engineering');
   ```
   - Ceci insère une nouvelle ligne avec `id` comme valeur suivante de la séquence (par exemple, 1 pour le premier usage, 2 pour le suivant, etc.).

#### Notes importantes
- Vous pouvez également l'utiliser dans des requêtes SELECT : `SELECT NEXT VALUE FOR my_sequence FROM SYSIBM.SYSDUMMY1;`
- Les séquences sont indépendantes des tables et peuvent être partagées entre plusieurs tables si nécessaire.
- Pour plus de détails, consultez la documentation IBM DB2 sur les séquences. Si vous avez besoin d'exemples pour d'autres fonctions de séquence comme `PREVIOUS VALUE FOR`, faites-le-moi savoir !