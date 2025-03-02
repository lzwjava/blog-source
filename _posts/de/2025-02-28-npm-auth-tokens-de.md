---
audio: false
generated: true
lang: de
layout: post
title: Verwenden von Auth-Tokens mit npm-Registry-URLs
translated: true
---

### Wichtige Punkte
- Es scheint wahrscheinlich, dass man zum Verwenden eines Auth-Tokens mit einer npm-Registry-URL diese in der `.npmrc`-Datei konfiguriert, wobei das Token mit der Registry-URL verknüpft wird.
- Die Forschung deutet darauf hin, dass die Standardmethode darin besteht, `//registry.url.com/:_authToken=your_token` in die `.npmrc`-Datei einzufügen, wobei `registry.url.com` die Registry-URL und `your_token` Ihr Authentifizierungstoken ist.
- Die Beweise sprechen dafür, die `.npmrc`-Datei zur Authentifizierung zu verwenden, da das direkte Einfügen des Tokens in die URL (wie in der HTTP-Anfrage) nicht Standard für npm ist und möglicherweise nicht funktioniert.

### Direkte Antwort

#### Übersicht
Um ein Authentifizierungstoken mit einer npm-Registry-URL zu verwenden, konfiguriert man dies normalerweise in einer speziellen Datei namens `.npmrc`. Diese Datei weist das npm-Befehlszeilen-Tool an, wie es sich authentifizieren soll, wenn es auf bestimmte Paketregistrierungen zugreift, wie die öffentliche npm-Registry oder eine private. Hier ist, wie man es Schritt für Schritt macht, einfach für Anfänger.

#### Schritte zur Konfiguration
1. **Registry-URL finden**: Entscheiden Sie, welche Registry Sie verwenden möchten, wie `registry.npmjs.org` für die öffentliche npm-Registry oder eine URL wie `privateregistry.com` für eine private.
2. **Auth-Token erhalten**: Besorgen Sie sich das Authentifizierungstoken vom Registry-Anbieter, das ein persönliches Zugriffstoken oder ein anderes von Ihrer Organisation bereitgestelltes sein könnte.
3. **Die `.npmrc`-Datei bearbeiten**: Öffnen oder erstellen Sie die `.npmrc`-Datei. Diese Datei kann sich in Ihrem Projektordner für projektspezifische Einstellungen oder in Ihrem Home-Verzeichnis (wie `~/.npmrc` auf Unix-Systemen) für benutzerweite Einstellungen befinden.
   - Fügen Sie eine Zeile wie diese hinzu: `//registry.url.com/:_authToken=your_token`. Ersetzen Sie `registry.url.com` durch Ihre Registry-URL und `your_token` durch Ihr tatsächliches Token.
   - Zum Beispiel könnte es für die öffentliche npm-Registry so aussehen: `//registry.npmjs.org/:_authToken=abc123`.
4. **Datei sichern**: Stellen Sie sicher, dass die `.npmrc`-Datei nur von Ihnen lesbar und beschreibbar ist, um Ihr Token sicher zu halten. Auf Unix-Systemen können Sie die Berechtigungen mit `chmod 600 ~/.npmrc` setzen.
5. **Überprüfen, ob es funktioniert**: Versuchen Sie, einen npm-Befehl wie `npm install` auszuführen, um zu sehen, ob er auf die Registry zugreifen kann, ohne Probleme.

#### Unerwartetes Detail
Während Sie denken könnten, dass Sie das Auth-Token direkt in die URL einfügen können (wie `https://registry.url.com?token=your_token`), ist dies nicht die Standardmethode für npm. Stattdessen verwendet npm die `.npmrc`-Datei, um die Authentifizierung im Hintergrund zu handhaben, was sicherer und einfacher zu verwalten ist.

Für weitere Details, besuchen Sie die offizielle npm-Dokumentation zur Konfiguration der `.npmrc`-Datei [hier](https://docs.npmjs.com/configuring-npm/npmrc).

---

### Umfragehinweis: Detaillierte Untersuchung der Verwendung von Auth-Tokens mit npm-Registry-URLs

Dieser Abschnitt bietet eine umfassende Analyse, wie man Authentifizierungstokens mit npm-Registry-URLs verwendet, und erweitert die direkte Antwort mit zusätzlichem Kontext, technischen Details und Beispielen. Er zielt darauf ab, alle in der Forschung besprochenen Aspekte abzudecken und ein umfassendes Verständnis für Benutzer mit unterschiedlichen Erfahrungsebenen zu gewährleisten.

#### Einführung in npm und Authentifizierung
Der Node Package Manager (npm) ist ein wichtiges Werkzeug für JavaScript-Entwickler, das Pakete und Abhängigkeiten verwaltet. Er interagiert mit Paketregistrierungen wie der öffentlichen Registrierung unter [registry.npmjs.org](https://registry.npmjs.org) und privaten Registrierungen, die von Organisationen gehostet werden. Für private Registrierungen oder spezielle Aktionen wie das Veröffentlichen von Paketen ist oft eine Authentifizierung erforderlich, die in der Regel durch Authentifizierungstokens in Konfigurationsdateien gehandhabt wird.

Die `.npmrc`-Datei ist zentral für die npm-Konfiguration und ermöglicht die Anpassung von Einstellungen wie Registry-URLs, Authentifizierungsmethoden und mehr. Sie kann an mehreren Stellen existieren, wie pro Projekt (im Projektverzeichnis), pro Benutzer (im Home-Verzeichnis, z.B. `~/.npmrc`) oder global (z.B. `/etc/npmrc`). Diese Datei verwendet ein INI-Format, bei dem Schlüssel und Werte definieren, wie npm sich verhält, einschließlich der Authentifizierung mit Registrierungen.

#### Konfiguration von Auth-Tokens in `.npmrc`
Um ein Auth-Token mit einer bestimmten Registry-URL zu verwenden, konfigurieren Sie die `.npmrc`-Datei, um das Token mit dieser Registry zu verknüpfen. Das Standardformat lautet:

```
registry.url.com/:_authToken=your_token
```

Hierbei ist `registry.url.com` die Basis-URL der Registry (z.B. `registry.npmjs.org` für die öffentliche Registry oder `privateregistry.com` für eine private) und `your_token` das von der Registry bereitgestellte Authentifizierungstoken. Der Schlüssel `:_authToken` gibt an, dass es sich um eine tokenbasierte Authentifizierung handelt, die npm verwendet, um den `Authorization`-Header als `Bearer your_token` bei HTTP-Anfragen an die Registry zu setzen.

Zum Beispiel, wenn Sie ein Token `abc123` für die öffentliche npm-Registry haben, würde Ihr `.npmrc`-Eintrag so aussehen:

```
registry.npmjs.org/:_authToken=abc123
```

Diese Konfiguration stellt sicher, dass jeder npm-Befehl, der mit `registry.npmjs.org` interagiert, das Token zur Authentifizierung verwendet, was den Zugriff auf private Pakete oder Veröffentlichungsmöglichkeiten ermöglicht, je nach Umfang des Tokens.

#### Umgang mit gescopten Paketen
Für gescopte Pakete (Pakete, die mit `@` beginnen, wie `@mycompany/mypackage`) können Sie eine andere Registry für diesen Scope festlegen. Zuerst legen Sie die Registry für den Scope fest:

```
@mycompany:registry=https://mycompany.artifactory.com/
```

Dann verknüpfen Sie das Auth-Token mit dieser Registry:

```
mycompany.artifactory.com/:_authToken=your_token
```

Diese Einstellung leitet alle Anfragen für `@mycompany`-Pakete an die angegebene private Registry weiter und verwendet das bereitgestellte Token zur Authentifizierung. Dies ist besonders nützlich in Unternehmensumgebungen, in denen Organisationen ihre eigenen npm-Registrierungen für interne Pakete hosten.

#### Standort und Sicherheit der `.npmrc`
Die `.npmrc`-Datei kann sich an mehreren Stellen befinden, die jeweils unterschiedliche Zwecke erfüllen:
- **Pro Projekt**: Im Projektverzeichnis (z.B. neben `package.json`). Dies ist ideal für projektspezifische Konfigurationen und überschreibt globale Einstellungen.
- **Pro Benutzer**: Im Benutzer-Home-Verzeichnis (z.B. `~/.npmrc` auf Unix, `C:\Users\<Benutzername>\.npmrc` auf Windows). Dies betrifft alle npm-Vorgänge für diesen Benutzer.
- **Global**: An `/etc/npmrc` oder durch den `globalconfig`-Parameter angegeben, normalerweise für systemweite Einstellungen verwendet.

Da `.npmrc` sensible Informationen wie Auth-Tokens enthalten kann, ist Sicherheit entscheidend. Die Datei muss nur vom Benutzer lesbar und beschreibbar sein, um unbefugten Zugriff zu verhindern. Auf Unix-Systemen können Sie dies mit dem Befehl `chmod 600 ~/.npmrc` sicherstellen, der die Berechtigungen auf Lesen/Schreiben für den Besitzer setzt.

#### Alternative Authentifizierungsmethoden
Während die tokenbasierte Authentifizierung üblich ist, unterstützt npm auch die Basisauthentifizierung, bei der Benutzername und Passwort in der `.npmrc`-Datei enthalten sein können:

```
registry.url.com/:username=your_username
registry.url.com/:_password=your_password
```

Aus Sicherheitsgründen wird jedoch die tokenbasierte Authentifizierung bevorzugt, da Tokens widerrufen werden können und über eingeschränkte Berechtigungen verfügen, was das Risiko im Vergleich zur Speicherung von Klartext-Passwörtern verringert.

#### Direkte URL-Einfügung: Ist das möglich?
Die Frage erwähnt "Verwendung von auth oder authtoken in der npm-Registry-URL", was darauf hindeuten könnte, das Token direkt in die URL einzufügen, wie `https://registry.url.com?token=your_token`. Die Forschung zeigt jedoch, dass dies nicht die Standardpraxis für npm ist. Die npm-Registry-API-Dokumentation und verwandte Ressourcen, wie [NPM registry authentication | Rush](https://rushjs.io/pages/maintainer/npm_registry_auth/), betonen die Verwendung der `.npmrc`-Datei zur Authentifizierung, wobei das Token im `Authorization`-Header als `Bearer your_token` übermittelt wird.

Das Einfügen des Tokens in die URL als Abfrageparameter wird von der Standard-npm-Registry nicht unterstützt und funktioniert möglicherweise nicht, da die Authentifizierung auf Ebene des HTTP-Headers erfolgt. Einige private Registrierungen könnten möglicherweise eine benutzerdefinierte URL-basierte Authentifizierung unterstützen, dies ist jedoch nicht für die offizielle npm-Registry dokumentiert. Zum Beispiel unterstützt die Basisauthentifizierung URLs wie `https://username:password@registry.url.com`, dies ist jedoch veraltet und unsicher im Vergleich zu tokenbasierten Methoden.

#### Praktische Beispiele und Anwendungsfälle
Um dies zu veranschaulichen, betrachten Sie diese Szenarien:

- **Öffentliche Registry mit Token**: Wenn Sie ein Token benötigen, um auf die öffentliche npm-Registry zu veröffentlichen, fügen Sie hinzu:
  ```
  registry.npmjs.org/:_authToken=abc123
  ```
  Dann führen Sie `npm publish` aus, um Ihr Paket hochzuladen, und npm verwendet das Token zur Authentifizierung.

- **Private Registry für gescopte Pakete**: Für ein Unternehmen, das eine private Registry unter `https://company.registry.com` für `@company`-Pakete verwendet, konfigurieren Sie:
  ```
  @company:registry=https://company.registry.com/
  company.registry.com/:_authToken=def456
  ```
  Jetzt wird das Installieren von `@company/mypackage` mit der privaten Registry und dem Token authentifiziert.

- **CI/CD-Integration**: In kontinuierlichen Integrationsumgebungen speichern Sie das Token als Umgebungsvariable (z.B. `NPM_TOKEN`) und verwenden es dynamisch in der `.npmrc`-Datei:
  ```
  registry.npmjs.org/:_authToken=${NPM_TOKEN}
  ```
  Dieser Ansatz, der in [Using private packages in a CI/CD workflow | npm Docs](https://docs.npmjs.com/using-private-packages-in-a-ci-cd-workflow/) detailliert beschrieben wird, stellt sicher, dass Tokens nicht hartcodiert und sicher sind.

#### Fehlerbehebung und Best Practices
Wenn die Authentifizierung fehlschlägt, überprüfen Sie:
- Die Registry-URL ist korrekt und zugänglich.
- Das Token ist gültig und verfügt über die erforderlichen Berechtigungen (z.B. Lesen für die Installation, Schreiben für das Veröffentlichen).
- Die `.npmrc`-Datei befindet sich am richtigen Ort und hat die richtigen Berechtigungen.

Best Practices umfassen:
- `.npmrc` mit Tokens niemals in das Versionskontrollsystem einchecken; fügen Sie es zu `.gitignore` hinzu.
- Verwenden Sie Umgebungsvariablen für Tokens in CI/CD-Pipelines, um die Sicherheit zu erhöhen.
- Drehen Sie Tokens regelmäßig und widerrufen Sie nicht verwendete, um das Risiko zu minimieren.

#### Vergleichende Analyse der Authentifizierungsmethoden
Um eine strukturierte Übersicht zu bieten, hier ein Vergleich von tokenbasierter und Basisauthentifizierung in npm:

| **Methode**          | **Konfiguration in `.npmrc`**                          | **Sicherheit**                     | **Anwendungsfall**                     |
|---------------------|-------------------------------------------------------|-----------------------------------|-----------------------------------|
| Tokenbasiert (Bevorzugt) | `registry.url.com/:_authToken=your_token`            | Hoch (widerrufbar, eingeschränkt)         | Private Registrierungen, CI/CD        |
| Basisauthentifizierung| `registry.url.com/:username=your_username`<br>`registry.url.com/:_password=your_password` | Niedrig (Klartext-Passwort)         | Legacy-Systeme, öffentliche Registry  |

Diese Tabelle zeigt, warum die tokenbasierte Authentifizierung empfohlen wird, insbesondere für moderne Workflows.

#### Schlussfolgerung
Die Verwendung eines Auth-Tokens mit einer npm-Registry-URL erfolgt hauptsächlich durch die Konfiguration der `.npmrc`-Datei, um das Token mit der Registry zu verknüpfen. Diese Methode ist Standard, sicher und weit verbreitet, sodass npm Anfragen authentifizieren kann, ohne Tokens in URLs preiszugeben. Während das Einfügen von Tokens direkt in URLs nicht Standard für npm ist und möglicherweise nicht funktioniert, bietet die `.npmrc`-Methode eine robuste Lösung für Interaktionen mit öffentlichen und privaten Registrierungen.

Für weiterführende Lektüre, konsultieren Sie die offizielle npm-Dokumentation zu [Konfiguration von npmrc](https://docs.npmjs.com/configuring-npm/npmrc) und [Registry-Authentifizierung](https://docs.npmjs.com/using-private-packages-in-a-ci-cd-workflow/).

### Wichtige Zitate
- [NPM registry authentication Rush documentation](https://rushjs.io/pages/maintainer/npm_registry_auth/)
- [registry-auth-token npm package details](https://www.npmjs.com/package/registry-auth-token)
- [Globally configure NPM with token Stack Overflow question](https://stackoverflow.com/questions/38764714/globally-configure-npm-with-a-token-registry-to-a-specific-scope-organisation)
- [Configure authentication Artifact Registry Google Cloud](https://cloud.google.com/artifact-registry/docs/nodejs/authentication)
- [Official npm documentation for npmrc file](https://docs.npmjs.com/configuring-npm/npmrc)
- [Using private packages in CI/CD workflow npm Docs](https://docs.npmjs.com/using-private-packages-in-a-ci-cd-workflow/)