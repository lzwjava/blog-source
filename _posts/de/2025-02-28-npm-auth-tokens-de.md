---
audio: false
generated: true
lang: de
layout: post
title: Verwendung von Auth-Token mit npm-Registry-URLs
translated: true
type: note
---

### Wichtige Punkte
- Es scheint wahrscheinlich, dass man zur Verwendung eines Auth-Tokens mit einer npm-Registry-URL diesen in der `.npmrc`-Datei konfiguriert und dabei den Token mit der Registry-URL verknüpft.
- Recherchen deuten darauf hin, dass der Standardweg darin besteht, `//registry.url.com/:_authToken=ihr_token` in der `.npmrc`-Datei hinzuzufügen, wobei `registry.url.com` die Registry-URL und `ihr_token` Ihr Authentifizierungs-Token ist.
- Die Beweislage spricht dafür, die `.npmrc`-Datei für die Authentifizierung zu verwenden, da das direkte Einfügen des Tokens in die URL (wie in der HTTP-Anfrage) für npm nicht standardkonform ist und möglicherweise nicht funktioniert.

### Direkte Antwort

#### Überblick
Um einen Authentifizierungs-Token mit einer npm-Registry-URL zu verwenden, konfigurieren Sie ihn typischerweise in einer speziellen Datei namens `.npmrc`. Diese Datei teilt dem npm-Kommandozeilenwerkzeug mit, wie es sich bei Zugriff auf bestimmte Paket-Registries, wie die öffentliche npm-Registry oder eine private, authentifizieren soll. Hier ist eine schrittweise Anleitung für Anfänger.

#### Schritte zur Konfiguration
1.  **Registry-URL finden**: Entscheiden Sie, welche Registry Sie verwenden möchten, z.B. `registry.npmjs.org` für die öffentliche npm-Registry oder eine URL wie `privateregistry.com` für eine private.
2.  **Auth-Token beschaffen**: Besorgen Sie sich den Authentifizierungs-Token vom Registry-Anbieter. Dies könnte ein persönlicher Zugangstoken oder ein anderer von Ihrer Organisation bereitgestellter Typ sein.
3.  **Die `.npmrc`-Datei bearbeiten**: Öffnen oder erstellen Sie die `.npmrc`-Datei. Diese Datei kann sich in Ihrem Projektordner für projektspezifische Einstellungen oder in Ihrem Home-Verzeichnis (z.B. `~/.npmrc` auf Unix-Systemen) für benutzerweite Einstellungen befinden.
    - Fügen Sie eine Zeile wie diese hinzu: `//registry.url.com/:_authToken=ihr_token`. Ersetzen Sie `registry.url.com` durch Ihre Registry-URL und `ihr_token` durch Ihren tatsächlichen Token.
    - Für die öffentliche npm-Registry könnte es beispielsweise so aussehen: `//registry.npmjs.org/:_authToken=abc123`.
4.  **Datei sichern**: Stellen Sie sicher, dass die `.npmrc`-Datei nur von Ihnen lesbar und beschreibbar ist, um Ihren Token sicher aufzubewahren. Auf Unix-Systemen können Sie die Berechtigungen mit `chmod 600 ~/.npmrc` setzen.
5.  **Funktion überprüfen**: Versuchen Sie, einen npm-Befehl wie `npm install` auszuführen, um zu sehen, ob er ohne Probleme auf die Registry zugreifen kann.

#### Unerwartetes Detail
Auch wenn man denken könnte, man könnte den Auth-Token direkt in die URL einfügen (wie `https://registry.url.com?token=ihr_token`), ist dies nicht der Standardweg für npm. Stattdessen verwendet npm die `.npmrc`-Datei, um die Authentifizierung im Hintergrund zu handhaben, was sie sicherer und einfacher zu verwalten macht.

Weitere Details finden Sie in der offiziellen npm-Dokumentation zur Konfiguration der `.npmrc`-Datei [hier](https://docs.npmjs.com/configuring-npm/npmrc).

---

### Umfragehinweis: Detaillierte Untersuchung zur Verwendung von Auth-Tokens mit npm-Registry-URLs

Dieser Abschnitt bietet eine umfassende Analyse zur Verwendung von Authentifizierungs-Tokens mit npm-Registry-URLs und erweitert die direkte Antwort um zusätzlichen Kontext, technische Details und Beispiele. Ziel ist es, alle in der Recherche diskutierten Aspekte abzudecken, um ein gründliches Verständnis für Benutzer mit unterschiedlichem Kenntnisstand zu gewährleisten.

#### Einführung in npm und Authentifizierung
Der Node Package Manager (npm) ist ein entscheidendes Werkzeug für JavaScript-Entwickler, das Pakete und Abhängigkeiten verwaltet. Es interagiert mit Paket-Registries, wie der öffentlichen Registry unter [registry.npmjs.org](https://registry.npmjs.org), und privaten Registries, die von Organisationen gehostet werden. Für private Registries oder bestimmte Aktionen wie das Veröffentlichen von Paketen ist oft eine Authentifizierung erforderlich, die typischerweise über Authentifizierungs-Tokens in Konfigurationsdateien gehandhabt wird.

Die `.npmrc`-Datei ist zentral für die npm-Konfiguration und ermöglicht die Anpassung von Einstellungen wie Registry-URLs, Authentifizierungsmethoden und mehr. Sie kann an mehreren Orten existieren, z.B. pro Projekt (im Projektstamm), pro Benutzer (im Home-Verzeichnis, z.B. `~/.npmrc`) oder global (z.B. `/etc/npmrc`). Diese Datei verwendet ein INI-Format, in dem Schlüssel und Werte definieren, wie sich npm verhält, einschließlich der Authentifizierung bei Registries.

#### Konfigurieren von Auth-Tokens in `.npmrc`
Um einen Auth-Token mit einer bestimmten Registry-URL zu verwenden, konfigurieren Sie die `.npmrc`-Datei so, dass sie den Token mit dieser Registry verknüpft. Das Standardformat ist:

```
registry.url.com/:_authToken=ihr_token
```

Hier ist `registry.url.com` die Basis-URL der Registry (z.B. `registry.npmjs.org` für die öffentliche Registry oder `privateregistry.com` für eine private), und `ihr_token` ist der von der Registry bereitgestellte Authentifizierungs-Token. Der Schlüssel `:_authToken` zeigt an, dass es sich um eine tokenbasierte Authentifizierung handelt, die npm verwendet, um den `Authorization`-Header als `Bearer ihr_token` zu setzen, wenn HTTP-Anfragen an die Registry gestellt werden.

Wenn Sie beispielsweise einen Token `abc123` für die öffentliche npm-Registry haben, würde Ihr `.npmrc`-Eintrag lauten:

```
registry.npmjs.org/:_authToken=abc123
```

Diese Konfiguration stellt sicher, dass jeder npm-Befehl, der mit `registry.npmjs.org` interagiert, den Token zur Authentifizierung enthält, was den Zugriff auf private Pakete oder Veröffentlichungsfähigkeiten ermöglicht, abhängig vom Geltungsbereich des Tokens.

#### Umgang mit Scoped Packages
Für Scoped Packages (Pakete, die mit `@` beginnen, wie `@mycompany/mypackage`) können Sie eine andere Registry für diesen Scope angeben. Setzen Sie zunächst die Registry für den Scope:

```
@mycompany:registry=https://mycompany.artifactory.com/
```

Verknüpfen Sie dann den Auth-Token mit dieser Registry:

```
mycompany.artifactory.com/:_authToken=ihr_token
```

Dieses Setup leitet alle Anfragen für `@mycompany`-Pakete an die angegebene private Registry weiter und verwendet den bereitgestellten Token für die Authentifizierung. Dies ist besonders nützlich in Unternehmensumgebungen, in denen Organisationen ihre eigenen npm-Registries für interne Pakete hosten.

#### Ort und Sicherheit von `.npmrc`
Die `.npmrc`-Datei kann sich an mehreren Orten befinden, die jeweils unterschiedlichen Zwecken dienen:
-   **Pro Projekt**: Befindet sich im Projektstamm (z.B. neben `package.json`). Ideal für projektspezifische Konfigurationen, die globale Einstellungen überschreiben.
-   **Pro Benutzer**: Befindet sich im Home-Verzeichnis des Benutzers (z.B. `~/.npmrc` auf Unix, `C:\Users\<Benutzername>\.npmrc` unter Windows). Betrifft alle npm-Operationen für diesen Benutzer.
-   **Global**: Befindet sich unter `/etc/npmrc` oder wird durch den `globalconfig`-Parameter angegeben, typischerweise für systemweite Einstellungen verwendet.

Da `.npmrc` sensible Informationen wie Auth-Tokens enthalten kann, ist Sicherheit entscheidend. Die Datei muss nur vom Benutzer lesbar und beschreibbar sein, um unbefugten Zugriff zu verhindern. Auf Unix-Systemen können Sie dies mit dem Befehl `chmod 600 ~/.npmrc` sicherstellen, wodurch die Berechtigungen auf Lesen/Schreiben nur für den Eigentümer gesetzt werden.

#### Alternative Authentifizierungsmethoden
Während tokenbasierte Authentifizierung üblich ist, unterstützt npm auch Basic Authentication, bei der Sie Benutzername und Passwort in der `.npmrc`-Datei angeben können:

```
registry.url.com/:username=ihr_benutzername
registry.url.com/:_password=ihr_passwort
```

Aus Sicherheitsgründen ist die tokenbasierte Authentifizierung jedoch zu bevorzugen, da Token widerrufen werden können und eingeschränkte Berechtigungen haben, was das Risiko im Vergleich zur Speicherung von Klartext-Passwörtern verringert.

#### Direkte URLEinbindung: Ist es möglich?
Die Frage erwähnt "using auth or authtoken in npm registry url", was darauf hindeuten könnte, den Token direkt in die URL einzufügen, wie `https://registry.url.com?token=ihr_token`. Recherchen zeigen jedoch, dass dies keine Standardpraxis für npm ist. Die npm-Registry-API-Dokumentation und verwandte Ressourcen, wie [NPM registry authentication | Rush](https://rushjs.io/pages/maintainer/npm_registry_auth/), betonen die Verwendung der `.npmrc`-Datei für die Authentifizierung, wobei der Token im `Authorization`-Header als `Bearer ihr_token` übermittelt wird.

Der Versuch, den Token als Abfrageparameter in die URL einzufügen, wird von der standardmäßigen npm-Registry nicht unterstützt und funktioniert möglicherweise nicht, da die Authentifizierung auf der Ebene der HTTP-Header erfolgt. Einige private Registries könnten benutzerdefinierte URL-basierte Authentifizierung unterstützen, aber dies ist für die offizielle npm-Registry nicht dokumentiert. Beispielsweise erlaubt Basic Authentication URLs wie `https://benutzername:passwort@registry.url.com`, aber dies ist veraltet und unsicher im Vergleich zu tokenbasierten Methoden.

#### Praktische Beispiele und Anwendungsfälle
Zur Veranschaulichung betrachten Sie diese Szenarien:

-   **Öffentliche Registry mit Token**: Wenn Sie für die öffentliche npm-Registry einen Token zum Veröffentlichen benötigen, fügen Sie hinzu:
    ```
    registry.npmjs.org/:_authToken=abc123
    ```
    Führen Sie dann `npm publish` aus, um Ihr Paket hochzuladen. npm verwendet den Token für die Authentifizierung.

-   **Private Registry für Scoped Packages**: Für ein Unternehmen, das eine private Registry unter `https://company.registry.com` für `@company`-Pakete verwendet, konfigurieren Sie:
    ```
    @company:registry=https://company.registry.com/
    company.registry.com/:_authToken=def456
    ```
    Jetzt wird die Installation von `@company/mypackage` bei der privaten Registry mit dem Token authentifiziert.

-   **CI/CD-Integration**: In Continuous-Integration-Umgebungen speichern Sie den Token als Umgebungsvariable (z.B. `NPM_TOKEN`) und verwenden ihn dynamisch in der `.npmrc`-Datei:
    ```
    registry.npmjs.org/:_authToken=${NPM_TOKEN}
    ```
    Dieser Ansatz, detailliert in [Using private packages in a CI/CD workflow | npm Docs](https://docs.npmjs.com/using-private-packages-in-a-ci-cd-workflow/), stellt sicher, dass Token nicht hartkodiert und sicher sind.

#### Fehlerbehebung und Best Practices
Wenn die Authentifizierung fehlschlägt, überprüfen Sie:
-   Die Registry-URL ist korrekt und erreichbar.
-   Der Token ist gültig und hat die notwendigen Berechtigungen (z.B. Lesen für Installation, Schreiben für Veröffentlichung).
-   Die `.npmrc`-Datei befindet sich am richtigen Ort und hat die richtigen Berechtigungen.

Best Practices umfassen:
-   Committen Sie `.npmrc` niemals mit Tokens in die Versionskontrolle; fügen Sie sie zu `.gitignore` hinzu.
-   Verwenden Sie Umgebungsvariablen für Tokens in CI/CD-Pipelines, um die Sicherheit zu erhöhen.
-   Rotieren Sie Token regelmäßig und widerrufen Sie ungenutzte, um das Risiko zu minimieren.

#### Vergleichende Analyse der Authentifizierungsmethoden
Um einen strukturierten Überblick zu bieten, hier eine Tabelle, die tokenbasierte und Basic Authentication in npm vergleicht:

| **Methode**               | **Konfiguration in `.npmrc`**                                                   | **Sicherheit**                          | **Anwendungsfall**                |
|---------------------------|---------------------------------------------------------------------------------|-----------------------------------------|-----------------------------------|
| Token-basiert (Bevorzugt) | `registry.url.com/:_authToken=ihr_token`                                       | Hoch (widerrufbar, eingeschränkt)       | Private Registries, CI/CD         |
| Basic Authentication      | `registry.url.com/:username=ihr_benutzername`<br>`registry.url.com/:_password=ihr_passwort` | Niedrig (Klartext-Passwort)             | Altsysteme, öffentliche Registry  |

Diese Tabelle hebt hervor, warum die tokenbasierte Authentifizierung besonders für moderne Workflows empfohlen wird.

#### Fazit
Die Verwendung eines Auth-Tokens mit einer npm-Registry-URL beinhaltet in erster Linie die Konfiguration der `.npmrc`-Datei, um den Token mit der Registry zu verknüpfen. Dieser Ansatz ist standardkonform, sicher und weitgehend unterstützt, sodass npm Anfragen authentifizieren kann, ohne Tokens in URLs preiszugeben. Während das direkte Einfügen von Tokens in URLs für npm nicht standardkonform ist und möglicherweise nicht funktioniert, bietet die `.npmrc`-Methode eine robuste Lösung für sowohl öffentliche als auch private Registry-Interaktionen.

Weitere Informationen finden Sie in der offiziellen npm-Dokumentation zu [configuring npmrc](https://docs.npmjs.com/configuring-npm/npmrc) und [registry authentication](https://docs.npmjs.com/using-private-packages-in-a-ci-cd-workflow/).

### Wichtige Zitate
-   [NPM registry authentication Rush documentation](https://rushjs.io/pages/maintainer/npm_registry_auth/)
-   [registry-auth-token npm package details](https://www.npmjs.com/package/registry-auth-token)
-   [Globally configure NPM with token Stack Overflow question](https://stackoverflow.com/questions/38764714/globally-configure-npm-with-a-token-registry-to-a-specific-scope-organisation)
-   [Configure authentication Artifact Registry Google Cloud](https://cloud.google.com/artifact-registry/docs/nodejs/authentication)
-   [Official npm documentation for npmrc file](https://docs.npmjs.com/configuring-npm/npmrc)
-   [Using private packages in CI/CD workflow npm Docs](https://docs.npmjs.com/using-private-packages-in-a-ci-cd-workflow/)