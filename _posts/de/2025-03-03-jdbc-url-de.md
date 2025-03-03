---
audio: false
generated: true
lang: de
layout: post
title: jdbc:mysql://localhost:3306/mydatabase
translated: true
---

Um eine JDBC-URL zum Verbinden mit einer DB2-Datenbank basierend auf dem `properties.db2.jcc`-Element in der `server.xml`-Datei eines WebSphere Liberty Profils zu erstellen, müssen Sie die Werte verwenden, die für bestimmte Schlüsselattribute wie `databaseName`, `serverName` und `portNumber` bereitgestellt werden. Hier ist, wie Sie dies tun können:

### Grundlegendes JDBC-URL-Format für DB2
Das Standardformat für eine JDBC-URL unter Verwendung des DB2 JDBC Type 4 Treibers (der häufig in Liberty Profile-Einstellungen verwendet wird) lautet:

```
jdbc:db2://<serverName>:<portNumber>/<databaseName>
```

- **`jdbc:db2://`** - Dies ist der Protokoll-Identifier für eine DB2-Datenbank unter Verwendung des Type 4 Treibers, der eine direkte Netzwerkverbindung anzeigt.
- **`<serverName>`** - Der Hostname oder die IP-Adresse des DB2-Servers, angegeben durch das Attribut `serverName` in `properties.db2.jcc`.
- **`<portNumber>`** - Der Port, auf dem die DB2-Instanz hört, angegeben durch das Attribut `portNumber` (Standardwert ist in der Regel `50000`, wenn nicht angegeben).
- **`<databaseName>`** - Der Name der Datenbank, mit der verbunden werden soll, angegeben durch das Attribut `databaseName`.

### Schritte zum Erstellen der URL
1. **Identifizieren Sie die erforderlichen Eigenschaften**: Extrahieren Sie aus dem `properties.db2.jcc`-Element in `server.xml` die Werte für `serverName`, `portNumber` und `databaseName`. Dies sind die wesentlichen Komponenten, die für die URL benötigt werden.
2. **URL zusammenstellen**: Kombinieren Sie diese Werte im obigen Format, wobei Sie sicherstellen, dass die richtigen Trennzeichen (`:` zwischen Server und Port, `/` vor dem Datenbanknamen) verwendet werden.
3. **Zusätzliche Eigenschaften (falls vorhanden) berücksichtigen**: Wenn `properties.db2.jcc` weitere Attribute enthält (z. B. `currentSchema`, `sslConnection`), können diese manchmal an die URL angehängt werden, dies hängt jedoch von ihrer Natur ab. Eigenschaften wie `user` und `password` werden in der Regel separat beim Herstellen der Verbindung übergeben und nicht in der URL, aus Sicherheitsgründen.

### Beispiel
Angenommen, Ihre `server.xml` enthält die folgende `properties.db2.jcc`-Konfiguration:

```xml
<properties.db2.jcc databaseName="SAMPLE" serverName="localhost" portNumber="50000" user="dbuser" password="dbpass"/>
```

- `serverName="localhost"`
- `portNumber="50000"`
- `databaseName="SAMPLE"`

Die JDBC-URL wäre:

```
jdbc:db2://localhost:50000/SAMPLE
```

- Der `user` und das `password` sind nicht in der URL enthalten; sie werden in der Regel separat bereitgestellt, wenn eine Verbindung über den JDBC-Treiber hergestellt wird (z. B. über eine `DataSource` oder `DriverManager`).

### Einbeziehung zusätzlicher Eigenschaften (optional)
Wenn in `properties.db2.jcc` zusätzliche Eigenschaften wie `currentSchema` oder `sslConnection` angegeben sind und Sie diese in der URL einbeziehen möchten (obwohl einige besser in den Verbindungs-Eigenschaften gesetzt werden), hängen Sie sie nach dem Datenbanknamen mit einem Doppelpunkt (`:`) gefolgt von semikolon-getrennten `property=value`-Paaren an. Zum Beispiel:

```xml
<properties.db2.jcc databaseName="SAMPLE" serverName="localhost" portNumber="50000" currentSchema="MYSCHEMA" sslConnection="true"/>
```

Die URL könnte dann so aussehen:

```
jdbc:db2://localhost:50000/SAMPLE:currentSchema=MYSCHEMA;sslConnection=true;
```

Allerdings:
- Eigenschaften wie `sslConnection=true` werden oft in einem `Properties`-Objekt oder einer Datenquellenkonfiguration anstatt in der URL gesetzt.
- Überprüfen Sie die DB2 JDBC-Treiberdokumentation, um zu bestätigen, welche Eigenschaften in der URL gültig sind und welche eine separate Konfiguration erfordern.

### Endgültige Antwort
Im Kontext Ihrer Anfrage, vorausgesetzt, `properties.db2.jcc` stellt mindestens `databaseName`, `serverName` und `portNumber` bereit, wird die JDBC-URL wie folgt erstellt:

```
jdbc:db2://<serverName>:<portNumber>/<databaseName>
```

Ersetzen Sie `<serverName>`, `<portNumber>` und `<databaseName>` durch die tatsächlichen Werte aus Ihrer `properties.db2.jcc`-Konfiguration. Wenn zusätzliche Eigenschaften vorhanden sind und für die URL vorgesehen sind, hängen Sie sie als `:property1=value1;property2=value2;` an, aber in der Regel werden Eigenschaften wie `user`, `password` und `sslConnection` separat in der Verbindungsaufstellung behandelt.