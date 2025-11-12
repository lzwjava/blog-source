---
audio: false
generated: true
lang: de
layout: post
title: Konstruieren Sie eine JDBC-URL
translated: true
type: note
---

Um eine JDBC-URL für die Verbindung mit einer DB2-Datenbank basierend auf dem `properties.db2.jcc`-Element in der `server.xml`-Datei eines WebSphere Liberty Profile zu erstellen, müssen Sie die für bestimmte Schlüsselattribute wie `databaseName`, `serverName` und `portNumber` angegebenen Werte verwenden. So gehen Sie vor:

### Grundlegendes JDBC-URL-Format für DB2
Das Standardformat für eine JDBC-URL mit dem DB2 JDBC Type 4-Treiber (der häufig in Liberty Profile-Setups verwendet wird) lautet:

```
jdbc:db2://<serverName>:<portNumber>/<databaseName>
```

- **`jdbc:db2://`** - Dies ist die Protokollkennung für eine DB2-Datenbank mit dem Type 4-Treiber und zeigt eine direkte Netzwerkverbindung an.
- **`<serverName>`** - Der Hostname oder die IP-Adresse des DB2-Servers, angegeben durch das Attribut `serverName` in `properties.db2.jcc`.
- **`<portNumber>`** - Der Port, auf dem die DB2-Instanz lauscht, angegeben durch das Attribut `portNumber` (Standard ist typischerweise `50000`, falls nicht angegeben).
- **`<databaseName>`** - Der Name der Datenbank, zu der eine Verbindung hergestellt werden soll, angegeben durch das Attribut `databaseName`.

### Schritte zum Erstellen der URL
1.  **Identifizieren Sie die erforderlichen Eigenschaften**: Extrahieren Sie aus dem `properties.db2.jcc`-Element in `server.xml` die Werte für `serverName`, `portNumber` und `databaseName`. Dies sind die wesentlichen Komponenten für die URL.
2.  **Setzen Sie die URL zusammen**: Kombinieren Sie diese Werte im oben gezeigten Format und achten Sie auf die korrekten Trennzeichen (`:` zwischen Server und Port, `/` vor dem Datenbanknamen).
3.  **Behandeln Sie zusätzliche Eigenschaften (falls vorhanden)**: Wenn `properties.db2.jcc` andere Attribute enthält (z.B. `currentSchema`, `sslConnection`), können diese manchmal an die URL angehängt werden, dies hängt jedoch von ihrer Art ab. Eigenschaften wie `user` und `password` werden typischerweise aus Sicherheitsgründen separat bei der Herstellung der Verbindung übergeben, nicht in der URL.

### Beispiel
Angenommen, Ihre `server.xml` enthält die folgende `properties.db2.jcc`-Konfiguration:

```xml
<properties.db2.jcc databaseName="SAMPLE" serverName="localhost" portNumber="50000" user="dbuser" password="dbpass"/>
```

- `serverName="localhost"`
- `portNumber="50000"`
- `databaseName="SAMPLE"`

Die JDBC-URL lautet:

```
jdbc:db2://localhost:50000/SAMPLE
```

- Der `user` und das `password` werden nicht in die URL aufgenommen; sie werden typischerweise separat bereitgestellt, wenn eine Verbindung über den JDBC-Treiber bezogen wird (z.B. über eine `DataSource` oder `DriverManager`).

### Einbeziehen zusätzlicher Eigenschaften (Optional)
Wenn in `properties.db2.jcc` zusätzliche Eigenschaften wie `currentSchema` oder `sslConnection` angegeben sind und Sie diese in die URL aufnehmen möchten (obwohl einige besser in Verbindungseigenschaften gesetzt werden), hängen Sie sie nach dem Datenbanknamen an, mit einem Doppelpunkt (`:`), gefolgt von durch Semikolons getrennten `property=value`-Paaren. Beispiel:

```xml
<properties.db2.jcc databaseName="SAMPLE" serverName="localhost" portNumber="50000" currentSchema="MYSCHEMA" sslConnection="true"/>
```

Die URL könnte lauten:

```
jdbc:db2://localhost:50000/SAMPLE:currentSchema=MYSCHEMA;sslConnection=true;
```

Allerdings gilt:
- Eigenschaften wie `sslConnection=true` werden oft in einem `Properties`-Objekt oder einer Data-Source-Konfiguration gesetzt, nicht in der URL.
- Prüfen Sie die DB2 JDBC-Treiberdokumentation, um zu bestätigen, welche Eigenschaften in der URL gültig sind und welche eine separate Konfiguration erfordern.

### Endgültige Antwort
Im Kontext Ihrer Anfrage, vorausgesetzt `properties.db2.jcc` stellt mindestens `databaseName`, `serverName` und `portNumber` bereit, wird die JDBC-URL wie folgt erstellt:

```
jdbc:db2://<serverName>:<portNumber>/<databaseName>
```

Ersetzen Sie `<serverName>`, `<portNumber>` und `<databaseName>` durch die tatsächlichen Werte aus Ihrer `properties.db2.jcc`-Konfiguration. Wenn zusätzliche Eigenschaften vorhanden und für die URL vorgesehen sind, hängen Sie sie als `:property1=value1;property2=value2;` an, aber typischerweise werden Eigenschaften wie `user`, `password` und `sslConnection` separat im Verbindungsaufbau behandelt.