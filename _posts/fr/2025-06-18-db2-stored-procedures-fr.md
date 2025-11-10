---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Appel de procédures stockées DB2 avec paramètres
translated: true
type: note
---

### Hypothèses et Contexte
Votre requête semble faire référence à l'appel d'une *procédure stockée* (probablement une faute de frappe pour "stored procedure") dans un système de base de données IBM, tel qu'IBM DB2 (sur Linux/Unix/Windows, z/OS ou iSeries). Les procédures stockées sont des scripts exécutables stockés dans la base de données qui peuvent accepter des paramètres d'entrée, effectuer des opérations et renvoyer des résultats ou des sorties. La syntaxe exacte dépend du langage de programmation et de l'environnement IBM (par exemple, SQL, COBOL, RPG ou Java via JDBC). Je me concentrerai sur le cas le plus courant : les instructions CALL basées sur SQL dans DB2, car c'est la norme pour les bases de données relationnelles.

Si vous utilisez une autre plateforme IBM (par exemple, les commandes CL d'IBM i, MQ ou Watson Query), fournissez plus de détails pour un conseil personnalisé.

### Comment Passer des Paramètres dans un Appel de Procédure Stockée DB2
Les procédures stockées dans DB2 sont appelées en utilisant l'instruction `CALL` en SQL. Les paramètres sont passés dans une liste séparée par des virgules entre parenthèses, correspondant à la définition de la procédure (par exemple, IN pour l'entrée, OUT pour la sortie, INOUT pour les deux).

#### Guide Étape par Étape
1. **Définir ou Connaître la Signature de la Procédure** : Assurez-vous de connaître le nom de la procédure et ses paramètres. Par exemple, une procédure peut être définie comme :
   ```sql
   CREATE PROCEDURE update_employee (IN emp_id INT, IN new_salary DECIMAL(10,2), OUT status_msg VARCHAR(100))
   ```
   - Ici, `emp_id` est une entrée (IN), `new_salary` est une entrée, et `status_msg` est une sortie (OUT).

2. **Utiliser l'Instruction CALL** : Dans un environnement SQL (par exemple, DB2 Command Line Processor, ou intégré dans des programmes comme Java), appelez la procédure comme ceci :
   ```sql
   CALL update_employee(12345, 75000.00, ?);
   ```
   - Le `?` est un espace réservé pour les paramètres OUT. Dans les appels programmatiques, gérez les sorties avec des jeux de résultats ou des variables hôtes.
   - Les entrées sont passées sous forme de littéraux ou de variables ; les sorties sont capturées via des espaces réservés ou des variables liées.

3. **Gestion des Types de Paramètres** :
   - **Paramètres IN** : Passez les valeurs directement (par exemple, des nombres, des chaînes entre guillemets).
   - **Paramètres OUT/INOUT** : Utilisez `?` dans l'appel CALL, puis liez-les dans votre code pour récupérer les valeurs après l'exécution.
   - Respectez exactement l'ordre et les types ; les incompatibilités provoquent des erreurs (par exemple, SQLCODE -440 pour des paramètres invalides).

4. **Exemples en Code** :
   - **Via DB2 CLP (Ligne de Commande)** : Exécution SQL directe.
     ```sql
     CALL my_proc('input_value', ?);
     ```
     Récupérez les paramètres OUT avec `FETCH FIRST FROM` ou dans des scripts.
   - **Via JDBC (Java)** :
     ```java
     CallableStatement stmt = conn.prepareCall("{CALL update_employee(?, ?, ?)}");
     stmt.setInt(1, 12345);          // Paramètre IN
     stmt.setBigDecimal(2, new java.math.BigDecimal("75000.00")); // Paramètre IN
     stmt.registerOutParameter(3, Types.VARCHAR); // Paramètre OUT
     stmt.execute();
     String status = stmt.getString(3); // Récupérer le paramètre OUT
     ```
   - **Via RPG sur IBM i** : Utilisez `CALLP` avec des déclarations de variables correspondant aux types de paramètres.
     ```rpg
     D PROC_PARAM    S                   LIKE(PARAM_TYPE)
     PROC_PARAM = 'value';
     CALLP MY_PROC(PROC_PARAM);
     ```
   - **Gestion des Erreurs** : Vérifiez SQLSTATE ou SQLCODE après l'appel ; par exemple, '00000' signifie succès.

#### Conseils Clés et Preuves
- **Preuve de la Documentation DB2** : Selon la référence SQL officielle d'IBM DB2 (par exemple, pour LUW v11.5 ou z/OS), l'instruction `CALL` est définie avec des listes de paramètres optionnelles. Par exemple, la syntaxe est : `CALL procedure-name [(parameter [, parameter] ...)]`. Cela correspond aux normes de l'industrie pour les bases de données relationnelles et est pris en charge dans les variantes DB2 pour la cohérence (voir IBM Knowledge Center).
- **Variations** : Dans IBM i (AS400), les procédures peuvent utiliser des appels CL (Command Language) comme `CALL PGM(MYPROC) PARM('value')` pour les programmes RPG. Pour COBOL sur mainframe, intégrez `EXEC SQL CALL...` avec des variables hôtes.
- **Test** : Utilisez `db2 describe routine procedure_name` pour inspecter les paramètres avant l'appel.
- **Limitations** : Les ensembles de paramètres volumineux peuvent nécessiter des tableaux ou des jeux de résultats ; les types complexes nécessitent une gestion spécifique.

Si cela ne correspond pas à votre configuration (par exemple, s'il s'agit d'IBM Watson ou d'un autre outil), partagez plus de contexte comme la plateforme ou le langage pour des instructions précises.