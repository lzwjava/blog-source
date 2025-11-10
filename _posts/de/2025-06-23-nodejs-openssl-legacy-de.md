---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: Node.js OpenSSL Legacy Provider Flag
translated: true
type: note
---

### Das Problem verstehen
Node.js 16 (und frühere Versionen) verwendet OpenSSL 1.x, während Node.js 22 OpenSSL 3.x einführt, das strengere Sicherheitsstandards hat. Dies kann bei einigen Anwendungen zu Fehlern führen, insbesondere bei solchen, die auf veraltete Kryptografie-Provider oder abgekündigte Algorithmen (z. B. MD4-Hashes) angewiesen sind. Das Flag `--openssl-legacy-provider` aktiviert vorübergehend die Kompatibilität mit dem Verhalten von OpenSSL 1.x, um diese Probleme während des Upgrades zu beheben.

**Hinweis**: Dieses Flag ist eine Problemumgehung und könnte in zukünftigen Node.js-Versionen entfernt werden. Es eignet sich am besten für kurzfristige Lösungen – aktualisieren Sie Ihren Code nach Möglichkeit auf die modernen OpenSSL 3.x-APIs.

### Verwendung des Flags
Sie können dieses Flag anwenden, wenn Sie Node.js direkt oder über npm/Yarn-Skripte ausführen. Es handelt sich um eine Laufzeitoption, nicht um eine permanente Konfiguration.

#### Für direkte Node-Befehle
Fügen Sie das Flag vor Ihrem Skript oder Befehl hinzu. Beispiele:
- Einfache Skriptausführung: `node --openssl-legacy-provider app.js`
- REPL (interaktiver Modus): `node --openssl-legacy-provider`
- Bei Ausführung eines Moduls: `node --openssl-legacy-provider --input-type=module index.mjs`
- Mit zusätzlichen Flags: `node --openssl-legacy-provider --max-old-space-size=4096 script.js`

Dies aktiviert die Unterstützung für den Legacy-Provider und vermeidet häufige Fehler wie "digital envelope routines unsupported" (im Zusammenhang mit veralteten Hashes oder Chiffren).

#### Für npm/Yarn-Skripte
Ändern Sie Ihre `package.json` unter `"scripts"`, um das Flag in den relevanten Befehlen einzufügen. Beispiel:
```json
{
  "scripts": {
    "start": "node --openssl-legacy-provider app.js",
    "dev": "node --openssl-legacy-provider --watch app.js"
  }
}
```
Führen Sie es dann wie gewohnt aus: `npm start` oder `yarn dev`.

Wenn Sie ein Tool wie nodemon oder vite verwenden, das Node-Prozesse startet, setzen Sie das Flag in dessen Konfiguration voran (z. B. in nodemon.json: `"exec": "node --openssl-legacy-provider"`).

#### Für globale Befehle (z. B. über nvm oder System-Node)
Wenn Sie Node-Versionen mit nvm verwalten, wechseln Sie zu Node 22 und führen Sie Befehle wie gezeigt mit dem Flag aus. Für Docker oder CI/CD fügen Sie es Ihren Ausführungsskripts hinzu (z. B. `CMD ["node", "--openssl-legacy-provider", "app.js"]`).

### Fehlerbehebung und Alternativen
- **Überprüfen Sie, ob das Flag funktioniert**: Führen Sie `node --openssl-legacy-provider --version` aus – es sollte die Version von Node 22 ohne Fehler ausgeben.
- **Häufige behobene Probleme**: Fehler bei `require()` von Crypto-Modulen, Webpack-Builds oder App-Starts. Falls das Problem weiterhin besteht, überprüfen Sie den Code auf OpenSSL-spezifische Funktionen (z. B. verwenden Sie Alternativen zu `crypto.createCipher` wie `crypto.createCipheriv`).
- **Langfristige Lösungen**: Suchen Sie nach veralteter Crypto-Nutzung (verwenden Sie Tools wie ESLint-Plugins) und aktualisieren Sie auf OpenSSL 3.x-kompatible Methoden. Die Node 22-Dokumentation empfiehlt Bibliotheken wie `bcrypt` oder `crypto.scrypt` für Hashing.
- **Hinweis zu Leistung/Kompatibilität**: Der Legacy-Provider-Modus kann Sicherheit/Funktionen geringfügig beeinträchtigen, hilft aber während der Migration. Testen Sie gründlich, da einige OpenSSL 3-Funktionen (z. B. verbesserte Entropiequellen) nicht verfügbar sind.

Weitere Details finden Sie in der Node.js OpenSSL-Dokumentation unter nodejs.org/api/crypto.html. Wenn Sie spezifische Fehlermeldungen teilen, kann ich gezieltere Ratschläge geben!