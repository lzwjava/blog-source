---
audio: false
generated: true
lang: fr
layout: post
title: Créer une base de données PostgreSQL
translated: true
type: note
---

Vous êtes déjà dans le terminal interactif PostgreSQL (`psql`) en tant qu'utilisateur `postgres`, ce qui est parfait ! Pour créer une bases de données dans PostgreSQL, vous pouvez utiliser la commande `CREATE DATABASE`. Voici un guide étape par étape :

1.  **Vérifiez que vous êtes dans `psql`** :
    Vous y êtes déjà, comme l'indique l'invite `postgres=#`.

2.  **Créez une base de données** :
    Utilisez la commande suivante pour créer une nouvelle base de données. Remplacez `mydatabase` par le nom de votre choix :

    ```sql
    CREATE DATABASE mydatabase;
    ```

    Cela crée une base de données nommée `mydatabase`.

3.  **Vérifiez que la base de données a été créée** :
    Listez toutes les bases de données pour confirmer :

    ```sql
    \l
    ```

    Cela affichera un tableau de toutes les bases de données, y compris `mydatabase`.

4.  **Connectez-vous à la nouvelle base de données** :
    Pour commencer à travailler dans la nouvelle base de données, connectez-vous avec :

    ```sql
    \c mydatabase
    ```

    Cela bascule votre session vers `mydatabase`.

5.  **Optionnel : Créez un utilisateur et accordez des permissions** :
    Si vous souhaitez qu'un utilisateur spécifique gère cette base de données, créez-en un et accordez-lui des privilèges :

    ```sql
    CREATE USER myuser WITH ENCRYPTED PASSWORD 'mypassword';
    GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;
    ```

    Remplacez `myuser` et `mypassword` par le nom d'utilisateur et le mot de passe de votre choix.

6.  **Quittez `psql`** :
    Une fois terminé, quittez avec :

    ```sql
    \q
    ```

### Notes :
- L'erreur `Permission denied` que vous avez vue (`could not change directory to "/home/lzw/projects/lzwjava.github.io"`) est due au fait que l'utilisateur `postgres` n'a pas accès à votre répertoire personnel. Cela n'affecte pas la création de la base de données mais peut apparaître lors de l'exécution de `psql` depuis un répertoire restreint. Vous pouvez éviter cela en exécutant `psql` depuis un répertoire auquel l'utilisateur `postgres` a accès ou en ne changeant pas de répertoire (par exemple, exécutez `sudo -u postgres psql` depuis `/tmp`).
- La commande `ls` que vous avez essayée dans `psql` n'est pas valide. Utilisez `\l` pour lister les bases de données ou `\dt` pour lister les tables dans une base de données.
- Assurez-vous que le service PostgreSQL est en cours d'exécution (`sudo systemctl start postgresql.service`), ce que vous avez déjà fait.

### Exemple de session :
```sql
postgres=# CREATE DATABASE mydatabase;
CREATE DATABASE
postgres=# \l
                                  List of databases
   Name      |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges   
-------------+----------+----------+-------------+-------------+-----------------------
 mydatabase  | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 postgres    | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 template0   | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
             |          |          |             |             | postgres=CTc/postgres
 template1   | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
             |          |          |             |             | postgres=CTc/postgres
(4 rows)

postgres=# \c mydatabase
You are now connected to database "mydatabase" as user "postgres".
mydatabase=# \q
```

Si vous avez besoin d'aide supplémentaire (par exemple, pour configurer des tables, des utilisateurs ou vous connecter depuis une application), n'hésitez pas à me le demander !