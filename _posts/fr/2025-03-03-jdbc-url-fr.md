---
audio: false
generated: true
lang: fr
layout: post
title: Construction d'une URL JDBC
translated: true
type: note
---

Pour construire une URL JDBC permettant de se connecter à une base de données DB2 à partir de l'élément `properties.db2.jcc` dans le fichier `server.xml` d'un profil WebSphere Liberty, vous devez utiliser les valeurs fournies pour certains attributs clés, tels que `databaseName`, `serverName` et `portNumber`. Voici comment procéder :

### Format de base d'une URL JDBC pour DB2
Le format standard pour une URL JDBC utilisant le pilote JDBC DB2 Type 4 (couramment utilisé dans les configurations Liberty Profile) est :

```
jdbc:db2://<serverName>:<portNumber>/<databaseName>
```

- **`jdbc:db2://`** - Il s'agit de l'identifiant de protocole pour une base de données DB2 utilisant le pilote Type 4, indiquant une connexion réseau directe.
- **`<serverName>`** - Le nom d'hôte ou l'adresse IP du serveur DB2, spécifié par l'attribut `serverName` dans `properties.db2.jcc`.
- **`<portNumber>`** - Le port sur lequel l'instance DB2 écoute, spécifié par l'attribut `portNumber` (la valeur par défaut est généralement `50000` si elle n'est pas spécifiée).
- **`<databaseName>`** - Le nom de la base de données à laquelle se connecter, spécifié par l'attribut `databaseName`.

### Étapes pour construire l'URL
1. **Identifier les propriétés requises** : À partir de l'élément `properties.db2.jcc` dans `server.xml`, extrayez les valeurs pour `serverName`, `portNumber` et `databaseName`. Ce sont les composants essentiels nécessaires pour l'URL.
2. **Assembler l'URL** : Combinez ces valeurs dans le format ci-dessus, en veillant à utiliser les séparateurs appropriés (`:` entre le serveur et le port, `/` avant le nom de la base de données).
3. **Gérer les propriétés supplémentaires (si présentes)** : Si `properties.db2.jcc` inclut d'autres attributs (par exemple, `currentSchema`, `sslConnection`), ils peuvent parfois être ajoutés à l'URL, mais cela dépend de leur nature. Typiquement, les propriétés comme `user` et `password` sont transmises séparément lors de l'établissement de la connexion, et non dans l'URL, pour des raisons de sécurité.

### Exemple
Supposons que votre `server.xml` contienne la configuration `properties.db2.jcc` suivante :

```xml
<properties.db2.jcc databaseName="SAMPLE" serverName="localhost" portNumber="50000" user="dbuser" password="dbpass"/>
```

- `serverName="localhost"`
- `portNumber="50000"`
- `databaseName="SAMPLE"`

L'URL JDBC serait :

```
jdbc:db2://localhost:50000/SAMPLE
```

- Le `user` et le `password` ne sont pas inclus dans l'URL ; ils sont généralement fournis séparément lors de l'obtention d'une connexion via le pilote JDBC (par exemple, via une `DataSource` ou `DriverManager`).

### Inclusion de propriétés supplémentaires (Optionnel)
Si des propriétés supplémentaires sont spécifiées dans `properties.db2.jcc`, telles que `currentSchema` ou `sslConnection`, et que vous souhaitez les inclure dans l'URL (bien que certaines soient mieux définies dans les propriétés de connexion), ajoutez-les après le nom de la base de données avec un deux-points (`:`) suivi de paires `property=value` séparées par des points-virgules. Par exemple :

```xml
<properties.db2.jcc databaseName="SAMPLE" serverName="localhost" portNumber="50000" currentSchema="MYSCHEMA" sslConnection="true"/>
```

L'URL pourrait devenir :

```
jdbc:db2://localhost:50000/SAMPLE:currentSchema=MYSCHEMA;sslConnection=true;
```

Cependant :
- Les propriétés comme `sslConnection=true` sont souvent définies dans un objet `Properties` ou dans la configuration de la source de données plutôt que dans l'URL.
- Consultez la documentation du pilote JDBC DB2 pour confirmer quelles propriétés sont valides dans l'URL par rapport à celles nécessitant une configuration séparée.

### Réponse finale
Dans le contexte de votre requête, en supposant que `properties.db2.jcc` fournit au moins `databaseName`, `serverName` et `portNumber`, l'URL JDBC est construite comme suit :

```
jdbc:db2://<serverName>:<portNumber>/<databaseName>
```

Remplacez `<serverName>`, `<portNumber>` et `<databaseName>` par les valeurs réelles de votre configuration `properties.db2.jcc`. Si des propriétés supplémentaires sont présentes et destinées à l'URL, ajoutez-les sous la forme `:property1=value1;property2=value2;`, mais typiquement, les propriétés comme `user`, `password` et `sslConnection` sont gérées séparément lors de la configuration de la connexion.