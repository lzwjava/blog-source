---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Umfassender Leitfaden für MongoDB
translated: true
type: note
---

MongoDB ist eine beliebte Open-Source-NoSQL-Dokumentendatenbank, die für die moderne Anwendungsentwicklung konzipiert ist. Sie speichert Daten in flexiblen, JSON-ähnlichen Dokumenten, die BSON (Binary JSON) genannt werden, was sie ideal für die Verarbeitung unstrukturierter oder halbstrukturierter Daten macht. Im Gegensatz zu traditionellen relationalen Datenbanken verwendet MongoDB einen schemafreien Ansatz, der es Sammlungen (Gruppen von Dokumenten) ermöglicht, unterschiedliche Strukturen zu haben. Sie ist hochskalierbar, unterstützt horizontale Skalierung über Sharding und bietet hohe Verfügbarkeit durch Replikation. MongoDB kann On-Premises, in der Cloud über MongoDB Atlas (einen verwalteten Dienst) oder in Hybridumgebungen eingesetzt werden. Dieser Leitfaden behandelt alles von den Grundlagen bis zu fortgeschrittenen Themen, mit Beispielen unter Verwendung der MongoDB Shell (mongosh).

## Einführung

MongoDB glänzt in Szenarien, die schnelle Entwicklung, flexible Datenmodelle und hohe Leistung erfordern. Wichtige Funktionen sind:
- **Dokumentenmodell**: Daten als eigenständige Dokumente mit verschachtelten Strukturen.
- **Abfragesprache**: Umfangreiche Abfragen mit einer Syntax, die JavaScript-Objekten ähnelt.
- **Skalierbarkeit**: Eingebaute Unterstützung für verteilte Systeme.
- **Ökosystem**: Integration mit Sprachen wie Python, Node.js, Java über offizielle Treiber.

Sie wird von Unternehmen wie Adobe, eBay und Forbes für Anwendungen im Bereich Big Data, Echtzeitanalysen und Content-Management verwendet.

## Installation

MongoDB bietet Community- (kostenlos, Open-Source) und Enterprise-Editionen. Die Installation variiert je nach Plattform; laden Sie sie immer von der offiziellen Website herunter, um Sicherheit zu gewährleisten.

### Windows
- Laden Sie den MSI-Installer vom MongoDB Download Center herunter.
- Führen Sie den Installer aus, wählen Sie "Complete" Setup und schließen Sie MongoDB Compass (GUI-Tool) ein.
- Fügen Sie das `bin`-Verzeichnis von MongoDB (z.B. `C:\Program Files\MongoDB\Server\8.0\bin`) zu Ihrer PATH-Umgebungsvariable hinzu.
- Erstellen Sie ein Datenverzeichnis: `mkdir -p C:\data\db`.
- Starten Sie den Server: `mongod.exe --dbpath C:\data\db`.

Unterstützt: Windows 11, Server 2022/2019.

### macOS
- Verwenden Sie Homebrew: `brew tap mongodb/brew && brew install mongodb-community`.
- Oder laden Sie das TGZ-Archiv herunter, entpacken Sie es und fügen Sie es zum PATH hinzu.
- Erstellen Sie ein Datenverzeichnis: `mkdir -p /data/db`.
- Starten: `mongod --dbpath /data/db` (oder verwenden Sie `brew services start mongodb/brew/mongodb-community`).

Unterstützt: macOS 11–14 (x86_64 und arm64).

### Linux
- Für Ubuntu/Debian: Fügen Sie den MongoDB-Repo-Schlüssel und die Liste hinzu, dann `apt-get install -y mongodb-org`.
- Für RHEL/CentOS: Verwenden Sie yum/dnf mit der Repo-Datei.
- Erstellen Sie ein Datenverzeichnis: `sudo mkdir -p /data/db && sudo chown -R $USER /data/db`.
- Starten: `sudo systemctl start mongod`.

Unterstützt: Ubuntu 24.04, RHEL 9+, Debian 12, Amazon Linux 2023, etc. Verwenden Sie XFS/EXT4-Dateisysteme; vermeiden Sie 32-Bit.

### Cloud (MongoDB Atlas)
- Registrieren Sie sich unter mongodb.com/atlas.
- Erstellen Sie einen kostenlosen Cluster über die Benutzeroberfläche oder CLI: `atlas clusters create <name> --provider AWS --region us-east-1 --tier M0`.
- Nehmen Sie Ihre IP in die Whitelist auf: `atlas network-access create <IP>`.
- Holen Sie sich den Connection String und verbinden Sie sich: `mongosh "mongodb+srv://<user>:<pass>@cluster0.abcde.mongodb.net/"`.

Atlas übernimmt automatisch Backups, Skalierung und Monitoring.

## Kernkonzepte

### Datenbanken
Container für Sammlungen, die Daten logisch trennen. Werden implizit bei der ersten Verwendung erstellt: `use mydb`. Wechseln mit `use mydb`. Auflisten: `show dbs`.

### Sammlungen
Gruppen von Dokumenten, ähnlich wie Tabellen, aber schemalos und flexibel. Werden implizit erstellt: `db.mycollection.insertOne({})`. Auflisten: `show collections`.

### Dokumente
Grundlegende Einheiten: BSON-Objekte mit Schlüssel-Wert-Paaren. Beispiel:
```javascript
{ "_id": ObjectId("..."), "name": "John", "age": 30, "address": { "city": "NYC", "zip": 10001 } }
```
Unterstützt Arrays, verschachtelte Objekte und Typen wie Datum, Binärdaten.

### BSON
Binärformat für effiziente Speicherung/Netzwerkkommunikation. Erweitert JSON um Typen wie ObjectId, Date, Binary.

### Namespaces
Eindeutige Bezeichner: `database.collection` (z.B. `mydb.orders`).

Beispiel-Setup:
```javascript
use test
db.orders.insertMany([
  { item: "almonds", price: 12, quantity: 2 },
  { item: "pecans", price: 20, quantity: 1 }
])
```

## CRUD-Operationen

Verwenden Sie `db.collection.method()` in mongosh. Transaktionen über Sessions für ACID-konforme Mehrfachdokument-Operationen.

### Erstellen (Einfügen)
- Einzeln: `db.users.insertOne({ name: "Alice", email: "alice@example.com" })`
- Mehrere: `db.users.insertMany([{ name: "Bob" }, { name: "Charlie" }])`
Gibt die eingefügten IDs zurück.

### Lesen (Finden)
- Alle: `db.users.find()`
- Gefiltert: `db.users.find({ age: { $gt: 25 } })`
- Übersichtliche Darstellung: `.pretty()`
- Begrenzen/Sortieren: `db.users.find().limit(5).sort({ age: -1 })`

### Aktualisieren
- Einzeln: `db.users.updateOne({ name: "Alice" }, { $set: { age: 31 } })`
- Mehrere: `db.users.updateMany({ age: { $lt: 20 } }, { $set: { status: "minor" } })`
- Erhöhen: `{ $inc: { score: 10 } }`

### Löschen
- Einzeln: `db.users.deleteOne({ name: "Bob" })`
- Mehrere: `db.users.deleteMany({ status: "inactive" })`
- Sammlung löschen: `db.users.drop()`

## Abfragen und Indizierung

### Abfragen
Verwenden Sie Prädikate für Bedingungen. Unterstützt Gleichheit, Bereiche, logische Operatoren.

- Einfach: `db.inventory.find({ status: "A" })` (SQL-Entsprechung: `WHERE status = 'A'`)
- $in: `db.inventory.find({ status: { $in: ["A", "D"] } })`
- $lt/$gt: `db.inventory.find({ qty: { $lt: 30 } })`
- $or: `db.inventory.find({ $or: [{ status: "A" }, { qty: { $lt: 30 } }] })`
- Regex: `db.inventory.find({ item: /^p/ })` (beginnt mit "p")
- Eingebettet: `db.users.find({ "address.city": "NYC" })`

Projektion (Felder auswählen): `db.users.find({ age: { $gt: 25 } }, { name: 1, _id: 0 })`

### Indizierung
Verbessert die Abfragegeschwindigkeit, indem Vollständige Scans vermieden werden. Basiert auf B-Bäumen.

- Typen: Einzelfeld (`db.users.createIndex({ name: 1 })`), Zusammengesetzt (`{ name: 1, age: -1 }`), Eindeutig (`{ email: 1 }`).
- Vorteile: Schnellere Gleichheits-/Bereichsabfragen, sortierte Ergebnisse.
- Erstellung: `db.users.createIndex({ age: 1 })` (aufsteigend).
- Anzeigen: `db.users.getIndexes()`
- Löschen: `db.users.dropIndex("age_1")`

Verwenden Sie den Atlas Performance Advisor für Empfehlungen. Kompromiss: Langsamere Schreibvorgänge.

## Aggregation Framework

Verarbeitet Daten durch Stufen in einer Pipeline. Ähnlich wie SQL GROUP BY, aber leistungsfähiger.

- Einfach: `db.orders.aggregate([ { $match: { price: { $lt: 15 } } } ])`
- Stufen: `$match` (Filtern), `$group` (Aggregieren: `{ $sum: "$price" }`), `$sort`, `$lookup` (Verknüpfen: `{ from: "inventory", localField: "item", foreignField: "sku", as: "stock" }`), `$project` (Umgestalten).
- Beispiel (Verknüpfen und Sortieren):
```javascript
db.orders.aggregate([
  { $match: { price: { $lt: 15 } } },
  { $lookup: { from: "inventory", localField: "item", foreignField: "sku", as: "inventory_docs" } },
  { $sort: { price: 1 } }
])
```
Ausdrücke: `{ $add: [ "$price", 10 ] }`. Vorschau in der Atlas-UI.

## Schema-Design

Die Flexibilität von MongoDB vermeidet starre Schemata, erfordert aber ein durchdachtes Design für Leistung.

- **Prinzipien**: Modellieren Sie für Zugriffsmuster (Lese-/Schreibvorgänge), verwenden Sie Indizes, halten Sie den Working Set im RAM.
- **Einbetten**: Denormalisieren Sie verwandte Daten in einem Dokument für atomare Lese-/Schreibvorgänge. Z.B. Kommentare in Beiträge einbetten. Vorteile: Schnelle Abfragen. Nachteile: Duplizierung, große Dokumente.
- **Referenzieren**: Normalisieren Sie mit IDs. Z.B. `posts` verweist auf `users` via `userId`. Verwenden Sie `$lookup` für Joins. Vorteile: Weniger Duplizierung. Nachteile: Mehrere Abfragen.
- Muster: Eins-zu-wenige (einbetten), Eins-zu-viele (referenzieren oder Array einbetten), Viele-zu-viele (referenzieren).
- Validierung: Erzwingen mit `db.createCollection("users", { validator: { $jsonSchema: { ... } } })`.

Berücksichtigen Sie Kompromisse bei der Duplizierung und Atomarität (nur auf Dokumentebene).

## Replikation und Sharding

### Replikation
Bietet Redundanz/hohe Verfügbarkeit über Replica Sets (Gruppe von `mongod`-Instanzen).

- Komponenten: Primary (Schreibvorgänge), Secondaries (replizieren über Oplog, Lesevorgänge optional), Arbiter (stimmt ab, keine Daten).
- Bereitstellung: Initialisieren mit `rs.initiate({ _id: "rs0", members: [{ _id: 0, host: "host1:27017" }] })`. Mitglieder hinzufügen: `rs.add("host2:27017")`.
- Wahlen: Wenn der Primary ausfällt, wird ein Secondary in ~10-12s gewählt.
- Lese-Präferenz: `primary`, `secondary` (kann verzögert sein).
- Verwenden Sie dies für Failover, Backups. Aktivieren Sie Flow Control, um Verzögerung zu verwalten.

### Sharding
Horizontale Skalierung: Verteilt Daten über Shards.

- Komponenten: Shards (Replica Sets), Mongos (Router), Config-Server (Metadaten).
- Shard-Schlüssel: Feld(er) für die Partitionierung (z.B. gehasht für gleichmäßige Verteilung). Erstellen Sie zuerst einen Index.
- Setup: Sharding aktivieren `sh.enableSharding("mydb")`, Sammlung sharden `sh.shardCollection("mydb.users", { userId: "hashed" })`.
- Balancer: Migriert Chunks für gleichmäßige Last. Zonen für Geo-Lokalität.
- Strategien: Gehasht (gleichmäßig), Bereichsbasiert (gezielte Abfragen).

Verbinden Sie sich über mongos; unterstützt Transaktionen.

## Sicherheit

Sichern Sie Bereitstellungen mit mehrschichtigen Schutzmaßnahmen.

- **Authentifizierung**: SCRAM, LDAP, OIDC, X.509. Benutzer erstellen: `db.createUser({ user: "admin", pwd: "pass", roles: ["root"] })`.
- **Autorisierung**: Rollenbasierte Zugriffskontrolle (RBAC). Eingebaute Rollen: read, readWrite, dbAdmin.
- **Verschlüsselung**: TLS/SSL für die Übertragung, Verschlüsselung ruhender Daten (EAR) über AWS KMS/Google Cloud KMS/Azure Key Vault. Client-seitige Feldverschlüsselung (CSFLE) für sensible Felder.
- Netzwerk: IP-Zugriffslisten, VPC-Peering in Atlas.
- Überwachung: Protokollieren von Operationen.

Aktivieren Sie Auth beim Start: `--auth`. Verwenden Sie Atlas für eingebaute Sicherheit.

## Best Practices

- **Produktions-Setup**: Führen Sie es als Service aus (systemctl/brew). Trennen Sie Daten/Journal/Logs auf SSDs. Verwenden Sie die WiredTiger-Engine (Standard).
- **Monitoring**: `mongostat`, `mongotop`, Atlas-Diagramme. Überwachen Sie Verbindungen (`connPoolStats`), Cache-Verdrängungen, I/O (`iostat`).
- **Backups**: `mongodump`/`mongorestore`, oder Atlas-Snapshots. Logisch (JSON) vs. physisch (Dateien).
- **Leistung**: Indizieren Sie weise, begrenzen Sie Projektionen, vermeiden Sie große Arrays. Setzen Sie `ulimit -n 64000`, deaktivieren Sie Swap (`vm.swappiness=0`), optimieren Sie TCP-Keepalive.
- **Skalierung**: Beginnen Sie mit Replica Sets; sharden Sie bei >100GB oder hohem Durchsatz.
- **Datenimport**: `mongoimport --db test --collection users --file users.json`.
- **Tools**: MongoDB Compass (GUI), mongosh (Shell), Treiber für Apps.
- **Häufige Fallstricke**: Übermäßiges Einbetten (Dokumentgrößenlimit 16MB), Ignorieren von Indizes, Nichtbeachten von Replikationsverzögerung.

Verwenden Sie für die Entwicklung den Atlas M0 Free Tier. Testen Sie Workloads mit `mongoperf`.

## Referenzen
- [MongoDB Manual](https://www.mongodb.com/docs/manual/)
- [MongoDB Installation](https://www.mongodb.com/docs/manual/installation/)
- [MongoDB Core Concepts](https://www.mongodb.com/docs/manual/core/)
- [MongoDB CRUD](https://www.mongodb.com/docs/manual/crud/)
- [MongoDB Querying](https://www.mongodb.com/docs/manual/tutorial/query-documents/)
- [MongoDB Indexes](https://www.mongodb.com/docs/manual/indexes/)
- [MongoDB Aggregation](https://www.mongodb.com/docs/manual/core/aggregation-pipeline/)
- [MongoDB Schema Design](https://www.mongodb.com/docs/manual/core/data-model-design/)
- [MongoDB Replication](https://www.mongodb.com/docs/manual/replication/)
- [MongoDB Sharding](https://www.mongodb.com/docs/manual/sharding/)
- [MongoDB Security](https://www.mongodb.com/docs/manual/core/security/)
- [MongoDB Production Notes](https://www.mongodb.com/docs/manual/administration/production-notes/)