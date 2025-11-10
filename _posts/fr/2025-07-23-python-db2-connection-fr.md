---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Connexion de Python à IBM DB2
translated: true
type: note
---

### Aperçu
IBM DB2 est un système de gestion de base de données relationnelle, et Python peut interagir avec lui en utilisant le package `ibm_db`, qui fournit une interface de bas niveau, et `ibm_db_dbi`, un wrapper conforme à DB-API 2.0 qui s'appuie sur `ibm_db` pour une utilisation plus simple et plus Pythonique. `ibm_db` est plus direct et puissant mais nécessite une connaissance plus approfondie, tandis que `ibm_db_dbi` imite le module `sqlite3` de Python, le rendant plus simple pour les opérations de base de données standard. Les deux font partie des pilotes Python IBM DB2.

### Installation
Installez les packages en utilisant pip :
```
pip install ibm_db
pip install ibm_db_dbi
```
Remarque : Ceux-ci nécessitent une bibliothèque cliente DB2. Pour Windows/Linux, téléchargez et installez le IBM Data Server Driver Package depuis le site d'IBM. Sur macOS, une configuration supplémentaire peut être nécessaire. Assurez-vous que votre serveur DB2 est accessible (par exemple, qu'il fonctionne sur un hôte avec des identifiants).

### Utilisation de ibm_db
`ibm_db` fournit des fonctions pour se connecter, exécuter des instructions et gérer les résultats. Il n'est pas conforme à DB-API mais offre plus de contrôle.

#### Connexion de base et requête
```python
import ibm_db

# Format de la chaîne de connexion : DATABASE=<db_name>;HOSTNAME=<host>;PORT=<port>;PROTOCOL=TCPIP;UID=<user>;PWD=<password>;
conn_str = "DATABASE=mydb;HOSTNAME=192.168.1.100;PORT=50000;PROTOCOL=TCPIP;UID=myuser;PWD=mypassword;"

# Connexion
conn = ibm_db.connect(conn_str, "", "")

# Exécuter une requête
stmt = ibm_db.exec_immediate(conn, "SELECT * FROM MYTABLE")

# Récupérer les résultats (un par un)
row = ibm_db.fetch_assoc(stmt)
while row:
    print(row)  # Retourne un dictionnaire
    row = ibm_db.fetch_assoc(stmt)

# Fermer
ibm_db.close(conn)
```
- **Fonctions clés** : `connect()`, `exec_immediate()` pour les requêtes simples, `prepare()` et `execute()` pour les requêtes paramétrées afin de prévenir les injections.
- **Instructions préparées** : Utilisez `prepare()` pour compiler une requête et `execute()` avec des paramètres.

#### Gestion des erreurs
```python
try:
    conn = ibm_db.connect(conn_str, "", "")
except Exception as e:
    print(f"Échec de la connexion : {str(e)}")
```

### Utilisation de ibm_db_dbi
`ibm_db_dbi` implémente DB-API 2.0, le rendant interchangeable avec des modules comme `sqlite3` ou `psycopg2`.

#### Connexion de base et requête
```python
import ibm_db_dbi

# Chaîne de connexion similaire à ibm_db
conn_str = "DATABASE=mydb;HOSTNAME=192.168.1.100;PORT=50000;PROTOCOL=TCPIP;UID=myuser;PWD=mypassword;"

# Connexion
conn = ibm_db_dbi.connect(conn_str)

# Créer un curseur
cursor = conn.cursor()

# Exécuter une requête
cursor.execute("SELECT * FROM MYTABLE")

# Récupérer les résultats
rows = cursor.fetchall()  # Retourne une liste de tuples
for row in rows:
    print(row)

# Fermer
cursor.close()
conn.close()
```
- **Requêtes paramétrées** : `cursor.execute("SELECT * FROM MYTABLE WHERE ID = ?", (id_value,))` – utilise les marqueurs ?.
- **Transactions** : `conn.commit()` ou `conn.rollback()` ; l'autocommit est désactivé par défaut.

### Différences clés et choix d'utilisation

| Caractéristique      | ibm_db                          | ibm_db_dbi                      |
|----------------------|---------------------------------|---------------------------------|
| Conformité           | Non DB-API (bas niveau)         | Conforme DB-API 2.0            |
| Facilité d'utilisation| Nécessite plus de code ; accès direct | Syntaxe plus simple, de type Python |
| Performance          | Potentiellement plus rapide pour les opérations complexes | Surcharge due au wrapper       |
| Fonctionnalités      | Toutes les fonctionnalités DB2  | Sous-ensemble via l'interface DB-API |
| Cas d'utilisation    | Applications personnalisées nécessitant un contrôle brut | Opérations CRUD standard       |

Utilisez `ibm_db_dbi` pour la familiarité si vous avez l'habitude d'autres pilotes DB-API. Passez à `ibm_db` pour les fonctionnalités avancées spécifiques à DB2 comme les procédures stockées ou les opérations en bloc.

### Bonnes pratiques
- Toujours gérer les exceptions et fermer les connexions dans un bloc `try-finally` ou `with` pour éviter les fuites de ressources.
- Pour les grands ensembles de résultats, utilisez `fetchmany(size)` au lieu de `fetchall()` pour limiter l'utilisation de la mémoire.
- Vérifiez la compatibilité de la version de DB2 ; les packages prennent en charge DB2 LUW, z/OS, iSeries.
- Reportez-vous à la documentation d'IBM pour les sujets avancés comme les connexions SSL ou l'intégration CLPPlus.

Pour plus d'exemples, visitez le [dépôt IBM db2 Python driver](https://github.com/ibmdb/python-ibmdb). Si vous rencontrez des problèmes, assurez-vous que votre instance DB2 est en cours d'exécution et que les identifiants sont corrects.