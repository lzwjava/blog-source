---
audio: false
generated: true
lang: fr
layout: post
title: Base de données Oracle - Compte utilisateur
translated: true
type: note
---

L'erreur `ORA-28000: The account is locked` se produit lors d'une tentative de connexion à une base de données Oracle (par exemple, via un pilote JDBC thin) et le compte utilisateur que vous essayez d'utiliser a été verrouillé. Cela se produit généralement en raison d'un trop grand nombre de tentatives de connexion infructueuses, d'un verrouillage manuel par un administrateur ou d'une politique d'expiration de compte. Pour résoudre ce problème, vous devez déverrouiller le compte et, si nécessaire, réinitialiser le mot de passe ou vérifier l'état du compte. Vous trouverez ci-dessous les étapes pour corriger ce problème lors de la connexion à une base de données Oracle.

---

### Étapes pour corriger ORA-28000

#### 1. **Vérifier l'erreur**
   Lorsque vous rencontrez cette erreur dans une connexion JDBC, elle peut ressembler à ceci :
   ```
   java.sql.SQLException: ORA-28000: The account is locked
   ```
   Cela confirme que le problème vient du compte de base de données, et non de la configuration JDBC elle-même (par exemple, l'URL, le pilote ou les paramètres de source de données WebSphere).

#### 2. **Se connecter en tant qu'utilisateur privilégié**
   Pour déverrouiller le compte, vous avez besoin d'un accès à un utilisateur de base de données disposant de privilèges administratifs (par exemple, `SYS`, `SYSTEM` ou un utilisateur avec le rôle `DBA`). Connectez-vous à la base de données en utilisant un outil comme SQL*Plus, SQL Developer ou un client JDBC :
   ```bash
   sqlplus / as sysdba
   ```
   OU
   ```bash
   sqlplus system/<mot_de_passe>@<nom_du_service>
   ```
   Remplacez `<mot_de_passe>` et `<nom_du_service>` par vos identifiants réels et le nom de service de la base de données (par exemple, `ORCL`).

#### 3. **Vérifier l'état du compte**
   Exécutez la requête SQL suivante pour vérifier l'état du compte verrouillé :
   ```sql
   SELECT username, account_status, lock_date 
   FROM dba_users 
   WHERE username = 'VOTRE_NOM_UTILISATEUR';
   ```
   - Remplacez `VOTRE_NOM_UTILISATEUR` par le nom d'utilisateur que vous essayez d'utiliser (par exemple, `monutilisateur`).
   - Regardez la colonne `ACCOUNT_STATUS`. Si elle indique `LOCKED` ou `LOCKED(TIMED)`, le compte est verrouillé.

   Exemple de résultat :
   ```
   USERNAME   ACCOUNT_STATUS   LOCK_DATE
   ---------- ---------------- -------------------
   MONUTILISATEUR     LOCKED           24-MARS-25 10:00:00
   ```

#### 4. **Déverrouiller le compte**
   Pour déverrouiller le compte, exécutez cette commande SQL en tant qu'utilisateur privilégié :
   ```sql
   ALTER USER votre_nom_utilisateur ACCOUNT UNLOCK;
   ```
   Exemple :
   ```sql
   ALTER USER monutilisateur ACCOUNT UNLOCK;
   ```

#### 5. **(Optionnel) Réinitialiser le mot de passe**
   Si le mot de passe a peut-être expiré ou si vous soupçonnez qu'il est incorrect, réinitialisez-le pendant que vous y êtes :
   ```sql
   ALTER USER votre_nom_utilisateur IDENTIFIED BY nouveau_mot_de_passe;
   ```
   Exemple :
   ```sql
   ALTER USER monutilisateur IDENTIFIED BY monnouveaumdp123;
   ```
   - Après la réinitialisation, mettez à jour le mot de passe dans votre `server.xml` WebSphere (ou là où la source de données JDBC est configurée) et rechiffrez-le si nécessaire (reportez-vous à votre question précédente pour les étapes de codage AES).

#### 6. **Valider les modifications (si nécessaire)**
   Dans la plupart des cas, les commandes `ALTER USER` prennent effet immédiatement et ne nécessitent pas de `COMMIT`. Cependant, si vous êtes dans un environnement à forte charge transactionnelle, assurez-vous qu'aucun rollback ne se produit en redémarrant la session ou la base de données si nécessaire.

#### 7. **Tester la connexion**
   Essayez de vous connecter à nouveau en utilisant votre application JDBC ou un test simple :
   ```java
   import java.sql.Connection;
   import java.sql.DriverManager;

   public class TestJDBC {
       public static void main(String[] args) throws Exception {
           String url = "jdbc:oracle:thin:@//localhost:1521/ORCL";
           String user = "monutilisateur";
           String password = "monnouveaumdp123";
           Connection conn = DriverManager.getConnection(url, user, password);
           System.out.println("Connexion réussie !");
           conn.close();
       }
   }
   ```
   - Mettez à jour l'`url`, `user` et `password` pour qu'ils correspondent à votre environnement.
   - Si cela fonctionne, mettez à jour la configuration de votre source de données WebSphere en conséquence.

#### 8. **Vérifier les politiques de profil (pour éviter les verrouillages futurs)**
   Le compte a pu être verrouillé en raison d'une politique de sécurité dans le profil de l'utilisateur (par exemple, `FAILED_LOGIN_ATTEMPTS` ou `PASSWORD_LOCK_TIME`). Vérifiez le profil attribué à l'utilisateur :
   ```sql
   SELECT profile 
   FROM dba_users 
   WHERE username = 'VOTRE_NOM_UTILISATEUR';
   ```
   Ensuite, inspectez les limites du profil :
   ```sql
   SELECT resource_name, limit 
   FROM dba_profiles 
   WHERE profile = 'VOTRE_NOM_DE_PROFIL';
   ```
   Recherchez :
   - `FAILED_LOGIN_ATTEMPTS` : Nombre de tentatives infructueuses avant verrouillage (par exemple, `10`).
   - `PASSWORD_LOCK_TIME` : Durée du verrouillage (par exemple, `1` jour).

   Pour assouplir ces paramètres (si cela est approprié), modifiez le profil :
   ```sql
   ALTER PROFILE votre_nom_de_profil LIMIT 
       FAILED_LOGIN_ATTEMPTS UNLIMITED 
       PASSWORD_LOCK_TIME UNLIMITED;
   ```
   Exemple :
   ```sql
   ALTER PROFILE DEFAULT LIMIT FAILED_LOGIN_ATTEMPTS UNLIMITED;
   ```

#### 9. **Redémarrer WebSphere (si nécessaire)**
   Si vous utilisez WebSphere et avez mis à jour le mot de passe de la source de données, redémarrez le serveur d'applications pour que les modifications prennent effet :
   - Pour Liberty : `./bin/server stop` et `./bin/server start`.
   - Pour WebSphere traditionnel : Utilisez la Console d'administration ou `stopServer.sh`/`startServer.sh`.

---

### Causes courantes de ORA-28000
- **Trop de tentatives de connexion infructueuses** : Vérifiez les logs de l'application ou les logs WebSphere (par exemple, `SystemOut.log`) pour détecter des erreurs de connexion antérieures.
- **Verrouillage manuel** : Un administrateur a peut-être verrouillé le compte intentionnellement (`ALTER USER monutilisateur ACCOUNT LOCK`).
- **Compte expiré** : Certains environnements verrouillent les comptes lorsque les mots de passe expirent. Vérifiez `EXPIRY_DATE` dans `dba_users`.

---

### Conseils de dépannage
- Si vous n'avez pas accès à `SYS` ou `SYSTEM`, contactez votre administrateur de base de données pour déverrouiller le compte.
- Assurez-vous que l'URL JDBC, le nom d'utilisateur et le mot de passe dans `server.xml` sont corrects avant de réessayer.
- Si le problème persiste, vérifiez que l'écouteur Oracle est en cours d'exécution :
  ```bash
  lsnrctl status
  ```

N'hésitez pas à me faire savoir si vous rencontrez des erreurs supplémentaires ou si vous avez besoin d'aide pour une étape spécifique !