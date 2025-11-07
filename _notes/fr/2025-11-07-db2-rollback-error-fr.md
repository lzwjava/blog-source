---
audio: false
generated: true
image: false
lang: fr
layout: post
model: moonshotai/kimi-k2-thinking
title: Annulation de transaction DB2 et détection d'erreur
translated: true
---

## Quand DB2 effectue un rollback en raison d'erreurs système

IBM DB2 effectue automatiquement un rollback des transactions lorsqu'il rencontre des erreurs système critiques menaçant l'intégrité des données. Les scénarios courants incluent :

- **Deadlocks ou timeouts** : SQLCODE -911 avec SQLSTATE 40001, le code raison "2" indique un rollback de transaction dû à un deadlock
- **Process abend (fin anormale)** : Dans tous les environnements DB2, la terminaison d'un processus déclenche un rollback implicite
- **Pannes de ressources système** : Pannes mémoire, disque ou réseau empêchant la finalisation de la transaction
- **Conflits de timestamp** : SQLCODE -818 se produit lorsque les timestamps internes ne correspondent pas entre le module et le DBRM
- **Sécurités des pools de connexions** : Certaines implémentations effectuent automatiquement un rollback des connexions lors de leur libération pour éviter que des transactions non validées ne causent des problèmes de verrouillage

## Comment détecter des informations d'erreur détaillées

### 1. Mécanismes principaux de détection d'erreur

**SQLCODE et SQLSTATE**
Après chaque instruction SQL, DB2 définit ces variables :

```sql
-- Vérifier immédiatement après l'exécution de l'instruction
IF SQLCODE < 0 THEN
    -- Une erreur est survenue
    ROLLBACK;
END IF;
```

Les codes de classe SQLSTATE identifient spécifiquement les types d'erreur :
- **Classe 58** : Erreur système (ex. ressource indisponible, intervention de l'opérateur)
- **Classe 40** : Rollback de transaction
- **Classe 25** : État de transaction invalide

**Instruction GET DIAGNOSTICS**
Pour des informations d'erreur détaillées dans les stored procedures SQL PL :

```sql
DECLARE v_sqlcode INTEGER;
DECLARE v_sqlstate CHAR(5);
DECLARE v_sqlmessage VARCHAR(256);

GET DIAGNOSTICS CONDITION 1
    v_sqlcode = DB2_RETURNED_SQLCODE,
    v_sqlstate = RETURNED_SQLSTATE,
    v_sqlmessage = MESSAGE_TEXT;
```

### 2. Détection d'erreur en ligne de commande

Lors de l'exécution de scripts via la ligne de commande `db2`, vérifier les codes de sortie :

- **Code de sortie 8** : Erreur système
- **Code de sortie 4** : Erreur DB2 (violation de contrainte, objet non trouvé)
- **Code de sortie 2** : Avertissement DB2
- **Code de sortie 1** : Aucune ligne trouvée

**Modèle de script recommandé** :
```bash
db2 -l migration.log +c -stf migration.sql
if [ $? -ge 4 ]; then
    db2 rollback
    tail -10 migration.log  # Examiner l'erreur détaillée
else
    db2 commit
fi
```

### 3. Gestion des erreurs dans les stored procedures

Pour une détection complète des erreurs en SQL PL, utiliser des handlers déclarés :

```sql
CREATE PROCEDURE my_procedure()
BEGIN
    DECLARE v_sqlcode INTEGER DEFAULT 0;
    DECLARE v_sqlstate CHAR(5) DEFAULT '00000';
    DECLARE v_error_message VARCHAR(256);
    
    -- Déclarer un handler de sortie pour toute exception
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        GET DIAGNOSTICS CONDITION 1
            v_sqlcode = DB2_RETURNED_SQLCODE,
            v_sqlstate = RETURNED_SQLSTATE,
            v_error_message = MESSAGE_TEXT;
            
        -- Logger les détails de l'erreur dans une table ou un fichier
        INSERT INTO error_log (sqlcode, sqlstate, message, timestamp)
        VALUES (v_sqlcode, v_sqlstate, v_error_message, CURRENT_TIMESTAMP);
        
        ROLLBACK;
    END;
    
    -- Votre logique transactionnelle ici
    UPDATE employee SET salary = salary + 1000 WHERE job = 'MANAGER';
    INSERT INTO audit_log VALUES (CURRENT_TIMESTAMP, 'Salary update');
    
    COMMIT;
END
```

### 4. Fichiers de log de diagnostic DB2

Pour les erreurs au niveau système, toujours vérifier :

- **db2diag.log** : Log de diagnostic principal avec des informations détaillées sur les erreurs système
- **Notification log** : Contient des résumés d'erreurs
- **Logs de ligne de commande** : Utiliser l'option `-l logfile.txt` pour capturer les erreurs

## Bonnes pratiques pour la détection d'erreur

1. **Toujours vérifier SQLCODE/SQLSTATE immédiatement** après les opérations critiques
2. **Utiliser GET DIAGNOSTICS** pour un contexte d'erreur riche dans les stored procedures
3. **Implémenter une surveillance du pourcentage de rollbacks** - tout ce qui dépasse 1% justifie une investigation
4. **Activer les options de commande** pour l'exécution de scripts :
   ```bash
   db2 +c -s -v -l error.log -f script.sql
   ```
   Où `+c` désactive l'autocommit et `-s` s'arrête sur erreur
5. **Utiliser des savepoints** pour des rollbacks partiels dans des transactions complexes
6. **Logger les détails d'erreur** dans des tables persistantes avant le rollback pour préserver les informations de diagnostic

## SQLSTATEs d'erreur système clés à surveiller

| SQLSTATE | Description | Action |
|----------|-------------|--------|
| **58004** | Erreur système (diverses causes) | Vérifier db2diag.log immédiatement |
| **58008** | Erreur de communication | Vérifier réseau/connectivité |
| **HY000** | Erreur générale de driver | Vérifier les logs des drivers ODBC/JDBC |
| **40001** | Deadlock/timeout | Réessayer la transaction avec backoff |

Pour les environnements de production, les outils de monitoring doivent alerter sur **SQLCODE < 0** et **SQLSTATEs de Classe 58** pour détecter proactivement les problèmes au niveau système avant qu'ils ne se propagent.