---
audio: false
generated: true
lang: fr
layout: post
title: Utilisation d'un mot de passe chiffré AES dans WebSphere Liberty
translated: true
---

Pour utiliser un mot de passe chiffré AES provenant du fichier `server.xml` de WebSphere Liberty dans Squirrel SQL Client, suivez ces étapes :

---

### **1. Décrypter le mot de passe à l'aide des outils de WebSphere Liberty**
Le mot de passe chiffré (par exemple, `password="{aes}ABC123..."`) doit être décrypté en premier. L'outil `securityUtility` de Liberty peut le faire si vous avez accès au keystore utilisé pour le chiffrement.

#### **Commande pour décrypter :**
```bash
# Naviguer vers le répertoire bin de Liberty
cd /path/to/wlp/bin

# Exécuter la commande decode de securityUtility
./securityUtility decode \
  --server=<LibertyServerPath> \
  --key=<KeyAlias> \
  --keyPassword=<KeystorePassword> \
  --source="{aes}ABC123..."
```

Remplacez :
- `<LibertyServerPath>` : Chemin vers votre serveur Liberty (par exemple, `usr/servers/defaultServer`).
- `<KeyAlias>` : Alias de la clé dans le keystore (par défaut : `default`).
- `<KeystorePassword>` : Mot de passe pour le keystore (par défaut : `KeystorePass` s'il n'a pas été modifié).
- `{aes}ABC123...` : Le mot de passe chiffré provenant de `server.xml`.

---

### **2. Utiliser le mot de passe décrypté dans Squirrel**
1. Ouvrez Squirrel SQL Client.
2. Créez un nouvel alias de connexion.
3. Dans les propriétés de la connexion :
   - **Driver** : Choisissez votre pilote JDBC Oracle.
   - **URL** : Utilisez l'URL JDBC provenant de `server.xml` de Liberty (par exemple, `jdbc:oracle:thin:@//host:port/service`).
   - **Nom d'utilisateur** : Le nom d'utilisateur provenant de `<dataSource>` de Liberty.
   - **Mot de passe** : Entrez le **mot de passe décrypté** obtenu à l'étape 1.

---

### **Notes importantes**
- **Accès au keystore** : Vous avez besoin du fichier keystore (`key.jks` ou `key.p12`) et de son mot de passe. Par défaut, il se trouve dans le répertoire `resources/security` de Liberty.
- **Sécurité** : Ne stockez jamais le mot de passe décrypté en texte brut. Entrez-le directement dans Squirrel sans le sauvegarder dans un fichier.
- **Aide de l'administrateur** : Si vous n'avez pas les identifiants du keystore, contactez votre administrateur Liberty pour décrypter le mot de passe de manière sécurisée.

---

### **Approche alternative (non recommandée)**
Si le décryptage n'est pas faisable, remplacez temporairement le mot de passe chiffré dans `server.xml` par un mot de passe en texte brut (**pour les tests uniquement**). Redémarrez Liberty et utilisez le mot de passe en texte brut dans Squirrel. Revenez ensuite au mot de passe chiffré.

```xml
<!-- Exemple : Mot de passe en texte brut (à éviter en production) -->
<dataSource ...>
  <properties password="plaintextPassword" />
</dataSource>
```

---

En suivant ces étapes, vous pouvez utiliser le mot de passe décrypté dans Squirrel tout en respectant les meilleures pratiques de sécurité.

---

Pour connecter le client Squirrel SQL à une base de données Oracle en utilisant la configuration spécifiée dans un fichier `server.xml` de WebSphere Liberty Profile, en particulier lorsque les propriétés du pilote JDBC Oracle incluent un mot de passe chiffré AES, suivez ces étapes. Le processus implique l'extraction des détails de connexion du fichier `server.xml`, la gestion du mot de passe chiffré et la configuration appropriée de Squirrel SQL. Voici un guide complet :

### Étape 1 : Comprendre la configuration de `server.xml`
Dans WebSphere Liberty Profile, les connexions de base de données sont définies dans le fichier `server.xml` à l'aide d'un élément `<dataSource>`. Cet élément spécifie les propriétés de la source de données, y compris celles pour une base de données Oracle via un élément `<properties.oracle>` imbriqué. Une configuration d'exemple pourrait ressembler à ceci :

```xml
<dataSource jndiName="jdbc/myOracleDS">
    <jdbcDriver libraryRef="OracleLib"/>
    <properties.oracle url="jdbc:oracle:thin:@//localhost:1521/orcl" user="scott" password="{aes}encrypted_password"/>
</dataSource>
<library id="OracleLib">
    <fileset dir="${server.config.dir}/lib" includes="ojdbc6.jar"/>
</library>
```

Ici :
- **`url`** : L'URL JDBC pour se connecter à la base de données Oracle (par exemple, `jdbc:oracle:thin:@//localhost:1521/orcl`).
- **`user`** : Le nom d'utilisateur de la base de données (par exemple, `scott`).
- **`password`** : Le mot de passe, chiffré avec AES, précédé de `{aes}` (par exemple, `{aes}encrypted_password`).
- **`<jdbcDriver>`** : Fait référence au fichier JAR du pilote JDBC Oracle.

Puisque Squirrel SQL est un client autonome et ne peut pas accéder directement à la source de données gérée par WebSphere (par exemple, via une recherche JNDI), vous devez le configurer manuellement en utilisant les mêmes détails de connexion.

### Étape 2 : Extraire les détails de connexion de `server.xml`
Localisez l'élément `<dataSource>` dans votre fichier `server.xml` qui correspond à votre base de données Oracle. À partir de l'élément `<properties.oracle>`, notez les éléments suivants :
- **URL JDBC** : Trouvée dans l'attribut `url` (par exemple, `jdbc:oracle:thin:@//localhost:1521/orcl`).
- **Nom d'utilisateur** : Trouvé dans l'attribut `user` (par exemple, `scott`).
- **Mot de passe chiffré** : Trouvé dans l'attribut `password` (par exemple, `{aes}encrypted_password`).

L'URL JDBC spécifie comment se connecter à la base de données Oracle, généralement dans l'un de ces formats :
- `jdbc:oracle:thin:@//hostname:port/service_name` (en utilisant un nom de service)
- `jdbc:oracle:thin:@hostname:port:SID` (en utilisant un SID)

Vérifiez votre `server.xml` pour confirmer l'URL exacte.

### Étape 3 : Décoder le mot de passe chiffré AES
Le mot de passe dans le `server.xml` est chiffré avec AES, comme indiqué par le préfixe `{aes}`. WebSphere Liberty Profile chiffre les mots de passe pour des raisons de sécurité, mais Squirrel SQL nécessite le mot de passe en texte brut pour établir une connexion. Pour décoder le mot de passe chiffré :

1. **Utiliser l'outil `securityUtility` de WebSphere** :
   - Cet outil est inclus avec votre installation WebSphere Liberty, généralement situé dans le répertoire `bin` (par exemple, `<liberty_install_dir>/bin/`).
   - Exécutez la commande suivante dans un terminal ou une invite de commande à partir du répertoire `bin` :
     ```
     securityUtility decode --encoding=aes <encrypted_password>
     ```
     Remplacez `<encrypted_password>` par la chaîne chiffrée réelle provenant de l'attribut `password` (tout ce qui suit `{aes}`). Par exemple :
     ```
     securityUtility decode --encoding=aes encrypted_password
     ```
   - L'outil affichera le mot de passe en texte brut.

2. **Alternative** :
   - Si vous n'avez pas accès à l'installation WebSphere Liberty ou à l'outil `securityUtility`, vous devrez obtenir le mot de passe en texte brut auprès de votre administrateur système ou de la personne qui a configuré la source de données.

Enregistrez le mot de passe décodé en toute sécurité, car vous en aurez besoin pour Squirrel SQL.

### Étape 4 : Configurer le pilote JDBC Oracle dans Squirrel SQL
Squirrel SQL nécessite le pilote JDBC Oracle pour se connecter à la base de données. Vous aurez besoin du même fichier JAR du pilote référencé dans l'élément `<library>` du `server.xml` (par exemple, `ojdbc6.jar`).

1. **Obtenir le fichier JAR du pilote** :
   - Localisez le fichier JAR du pilote JDBC Oracle spécifié dans l'élément `<fileset>` du `server.xml` (par exemple, `ojdbc6.jar` dans `${server.config.dir}/lib`).
   - Si vous ne l'avez pas, téléchargez la version appropriée depuis le site web d'Oracle (par exemple, `ojdbc6.jar` ou `ojdbc8.jar`, correspondant à votre version de base de données).

2. **Ajouter le pilote à Squirrel SQL** :
   - Ouvrez Squirrel SQL.
   - Allez à l'onglet **Drivers** à gauche.
   - Cliquez sur le bouton **+** pour ajouter un nouveau pilote.
   - Configurez le pilote :
     - **Nom** : Entrez un nom (par exemple, « Pilote JDBC Oracle »).
     - **URL d'exemple** : Entrez une URL d'exemple (par exemple, `jdbc:oracle:thin:@//localhost:1521/orcl`).
     - **Nom de la classe** : Entrez `oracle.jdbc.OracleDriver`.
     - **Chemin de classe supplémentaire** : Cliquez sur **Add**, puis parcourez et sélectionnez le fichier JAR du pilote JDBC Oracle.
   - Cliquez sur **OK** pour enregistrer le pilote.

### Étape 5 : Créer une connexion (alias) dans Squirrel SQL
Maintenant, créez un alias de connexion en utilisant les détails extraits :

1. **Ajouter un nouvel alias** :
   - Allez à l'onglet **Aliases** dans Squirrel SQL.
   - Cliquez sur le bouton **+** pour ajouter un nouvel alias.
   - Configurez l'alias :
     - **Nom** : Entrez un nom pour la connexion (par exemple, « Oracle DB via WebSphere »).
     - **Pilote** : Sélectionnez le pilote JDBC Oracle que vous venez de configurer.
     - **URL** : Entrez l'URL JDBC provenant de l'élément `<properties.oracle>` du `server.xml` (par exemple, `jdbc:oracle:thin:@//localhost:1521/orcl`).
     - **Nom d'utilisateur** : Entrez le nom d'utilisateur provenant du `server.xml` (par exemple, `scott`).
     - **Mot de passe** : Entrez le mot de passe en texte brut décodé de l'Étape 3.

2. **Propriétés supplémentaires (facultatif)** :
   - Si l'élément `<properties.oracle>` dans `server.xml` inclut des attributs supplémentaires (par exemple, `ssl="true"` ou `connectionTimeout="30000"`), cliquez sur l'onglet **Propriétés** dans la configuration de l'alias et ajoutez-les sous forme de paires clé-valeur.

3. **Tester la connexion** :
   - Cliquez sur **Test Connection** pour vérifier que Squirrel SQL peut se connecter à la base de données.
   - Si le test est réussi, cliquez sur **OK** pour enregistrer l'alias.

### L'URL JDBC
L'URL à utiliser dans Squirrel SQL est la valeur spécifiée dans l'attribut `url` de l'élément `<properties.oracle>` dans le fichier `server.xml`. Par exemple :
- Si `server.xml` a `<properties.oracle url="jdbc:oracle:thin:@//localhost:1521/orcl" .../>`, alors utilisez :
  ```
  jdbc:oracle:thin:@//localhost:1521/orcl
  ```

Cette URL, combinée avec le nom d'utilisateur et le mot de passe décodé, permet à Squirrel SQL de se connecter à la base de données Oracle.

### Notes
- **Mot de passe chiffré** : Vous ne pouvez pas utiliser le mot de passe chiffré directement dans Squirrel SQL ; il doit être décodé en texte brut.
- **Portée de la source de données** : L'élément `<dataSource>` dans `server.xml` est conçu pour les applications s'exécutant dans WebSphere Liberty. Squirrel SQL, en tant que client externe, nécessite une configuration manuelle reflétant ces paramètres.
- **Compatibilité du JAR** : Assurez-vous que la version du fichier JAR du pilote JDBC Oracle correspond à votre version de base de données pour la compatibilité.

En suivant ces étapes, vous pouvez configurer Squirrel SQL pour se connecter à la base de données Oracle en utilisant les propriétés définies dans le fichier `server.xml` de WebSphere Liberty Profile.

---

Puisque la commande `securityUtility` dans WebSphere Liberty ne fournit pas d'option de décodage pour les mots de passe chiffrés AES (par exemple, ceux précédés de `{aes}` dans le fichier `server.xml`), vous devez utiliser une approche programmatique pour les décoder. La méthode recommandée consiste à utiliser la classe `com.ibm.websphere.crypto.PasswordUtil`, qui fait partie du runtime Liberty et peut décoder de tels mots de passe. Voici deux solutions pratiques pour y parvenir :

### Option 1 : Utiliser une application web temporaire (recommandée)
Déployer une application web simple sur votre serveur Liberty vous permet d'exécuter la logique de décodage dans l'environnement du serveur, garantissant ainsi l'accès à la bonne clé de chiffrement (par défaut ou personnalisée, telle que définie dans `server.xml`).

#### Étapes :
1. **Créer un fichier JSP**
   Créez un fichier nommé `decode.jsp` avec le contenu suivant :
   ```jsp
   <%@ page import="com.ibm.websphere.crypto.PasswordUtil" %>
   <%
       String encoded = request.getParameter("encoded");
       if (encoded != null) {
           try {
               String decoded = PasswordUtil.decode(encoded);
               out.println("Mot de passe décodé : " + decoded);
           } catch (Exception e) {
               out.println("Erreur de décodage du mot de passe : " + e.getMessage());
           }
       }
   %>
   ```

2. **Déployer le JSP**
   - Placez `decode.jsp` dans un répertoire d'application web, tel que `wlp/usr/servers/yourServer/apps/myApp.war/WEB-INF/`.
   - Si nécessaire, créez un fichier WAR de base avec ce JSP et déployez-le en utilisant la console d'administration de Liberty ou en le déposant dans le répertoire `dropins`.

3. **Accéder au JSP**
   - Démarrez votre serveur Liberty (`server start yourServer`).
   - Ouvrez un navigateur et accédez à :
     `http://localhost:9080/myApp/decode.jsp?encoded={aes}your_encrypted_password`
     Remplacez `{aes}your_encrypted_password` par le mot de passe chiffré réel provenant de `server.xml`.

4. **Récupérer le mot de passe décodé**
   La page affichera le mot de passe décrypté, que vous pourrez ensuite utiliser (par exemple, dans Squirrel SQL pour vous connecter à une base de données).

5. **Sécuriser l'application**
   Après avoir obtenu le mot de passe, supprimez ou restreignez l'accès au JSP pour éviter une utilisation non autorisée.

#### Pourquoi cela fonctionne :
Exécuter dans l'environnement du serveur Liberty garantit que `PasswordUtil.decode()` utilise la même clé de chiffrement (par défaut ou personnalisée, spécifiée via `wlp.password.encryption.key` dans `server.xml`) qui a été utilisée pour coder le mot de passe.

---

### Option 2 : Utiliser un programme Java autonome
Si le déploiement d'une application web n'est pas faisable, vous pouvez écrire un programme Java autonome et l'exécuter avec les bibliothèques de runtime Liberty dans le classpath. Cette approche est plus délicate car elle nécessite une gestion manuelle de la clé de chiffrement, surtout si une clé personnalisée a été utilisée.

#### Code d'exemple :
```java
import com.ibm.websphere.crypto.PasswordUtil;

public class PasswordDecoder {
    public static void main(String[] args) {
        if (args.length < 1 || args.length > 2) {
            System.out.println("Utilisation : java PasswordDecoder <encoded_password> [crypto_key]");
            return;
        }
        String encoded = args[0];
        String cryptoKey = args.length == 2 ? args[1] : null;
        try {
            String decoded;
            if (cryptoKey != null) {
                decoded = PasswordUtil.decode(encoded, cryptoKey);
            } else {
                decoded = PasswordUtil.decode(encoded);
            }
            System.out.println("Mot de passe décodé : " + decoded);
        } catch (Exception e) {
            System.err.println("Erreur de décodage du mot de passe : " + e.getMessage());
        }
    }
}
```

#### Étapes :
1. **Compiler le programme**
   - Enregistrez le code sous le nom `PasswordDecoder.java`.
   - Compilez-le en utilisant les jars de Liberty :
     ```bash
     javac -cp /path/to/wlp/lib/* PasswordDecoder.java
     ```
     Remplacez `/path/to/wlp` par votre répertoire d'installation Liberty (par exemple, `/opt/ibm/wlp`).

2. **Exécuter le programme**
   - Si le mot de passe a été chiffré avec la clé par défaut :
     ```bash
     java -cp /path/to/wlp/lib/*:. PasswordDecoder "{aes}your_encrypted_password"
     ```
   - Si une clé personnalisée a été utilisée (par exemple, définie dans `server.xml` comme `<variable name="wlp.password.encryption.key" value="yourKey"/>`) :
     ```bash
     java -cp /path/to/wlp/lib/*:. PasswordDecoder "{aes}your_encrypted_password" "yourKey"
     ```

3. **Gérer la sortie**
   Le programme affichera le mot de passe décodé ou une erreur si la clé est incorrecte.

#### Notes :
- Les jars de Liberty (par exemple, dans `wlp/lib`) contiennent `com.ibm.websphere.crypto.PasswordUtil` et ses dépendances.
- Si une clé personnalisée a été utilisée et que vous ne la fournissez pas, le décodage échouera. Vérifiez `server.xml` ou les fichiers de configuration inclus pour la clé.

---

### Considérations clés
- **Clé par défaut contre clé personnalisée** :
  - Si aucune `wlp.password.encryption.key` n'est spécifiée dans `server.xml`, la clé par défaut est utilisée, et `PasswordUtil.decode(encoded)` devrait fonctionner sans paramètres supplémentaires.
  - Si une clé personnalisée est définie, vous devez la fournir explicitement lors du décodage en dehors du serveur (Option 2) ou vous fier au contexte du serveur (Option 1).

- **Sécurité** :
  Gérez le mot de passe décodé avec précaution, car il sera en texte brut. Évitez de le logger ou de l'exposer inutilement.

- **Préférence** :
  L'Option 1 (application web) est généralement plus fiable car elle s'exécute dans l'environnement Liberty, gérant automatiquement la clé et les dépendances.

En suivant l'une ou l'autre approche, vous pouvez décoder avec succès le mot de passe chiffré AES de `server.xml` malgré l'absence d'une option de décodage dans `securityUtility`.