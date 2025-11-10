---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Indicateur du fournisseur hérité OpenSSL de Node.js
translated: true
type: note
---

### Comprendre le problème
Node.js 16 (et les versions antérieures) utilise OpenSSL 1.x, tandis que Node.js 22 introduit OpenSSL 3.x, qui a des paramètres de sécurité plus stricts. Cela peut provoquer des erreurs dans certaines applications, en particulier celles qui dépendent de fournisseurs cryptographiques hérités ou d'algorithmes obsolètes (par exemple, les hachages MD4). Le flag `--openssl-legacy-provider` permet temporairement la compatibilité avec le comportement d'OpenSSL 1.x pour résoudre ces problèmes pendant la mise à niveau.

**Note** : Ce flag est une solution de contournement et pourrait être supprimé dans les futures versions de Node.js. Il est préférable pour les corrections à court terme — mettez à jour votre code pour utiliser les API modernes d'OpenSSL 3.x lorsque c'est possible.

### Comment utiliser le flag
Vous pouvez appliquer ce flag lors de l'exécution directe de Node.js ou via les scripts npm/yarn. C'est une option d'exécution, pas une configuration permanente.

#### Pour les commandes Node directes
Ajoutez le flag avant votre script ou commande. Exemples :
- Exécution de script basique : `node --openssl-legacy-provider app.js`
- REPL (mode interactif) : `node --openssl-legacy-provider`
- Si vous exécutez un module : `node --openssl-legacy-provider --input-type=module index.mjs`
- Avec des flags supplémentaires : `node --openssl-legacy-provider --max-old-space-size=4096 script.js`

Cela active le support du fournisseur hérité, évitant les erreurs courantes comme "digital envelope routines unsupported" (liées à des hachages ou chiffrements obsolètes).

#### Pour les scripts npm/Yarn
Modifiez votre `package.json` dans la section `"scripts"` pour inclure le flag dans les commandes concernées. Exemple :
```json
{
  "scripts": {
    "start": "node --openssl-legacy-provider app.js",
    "dev": "node --openssl-legacy-provider --watch app.js"
  }
}
```
Puis exécutez comme d'habitude : `npm start` ou `yarn dev`.

Si vous utilisez un outil comme nodemon ou vite qui génère des processus Node, ajoutez le flag en préfixe dans sa configuration (par exemple, dans nodemon.json : `"exec": "node --openssl-legacy-provider"`).

#### Pour les commandes globales (par exemple, via nvm ou Node système)
Si vous gérez les versions de Node avec nvm, passez à Node 22 et exécutez les commandes avec le flag comme indiqué. Pour Docker ou CI/CD, ajoutez-le à vos scripts d'exécution (par exemple, `CMD ["node", "--openssl-legacy-provider", "app.js"]`).

### Dépannage et alternatives
- **Vérifiez que le flag fonctionne** : Exécutez `node --openssl-legacy-provider --version` — cela devrait afficher la version de Node 22 sans erreurs.
- **Problèmes courants résolus** : Erreurs avec `require()` de modules crypto, builds webpack ou démarrages d'applications. Si cela persiste, vérifiez la présence de code spécifique à OpenSSL (par exemple, utilisez des alternatives à `crypto.createCipher` comme `crypto.createCipheriv`).
- **Solutions à long terme** : Recherchez l'utilisation de crypto obsolète (utilisez des outils comme les plugins ESLint) et mettez à jour vers des méthodes compatibles OpenSSL 3.x. La documentation de Node 22 recommande des bibliothèques comme `bcrypt` ou `crypto.scrypt` pour le hachage.
- **Note sur les performances/la compatibilité** : Le mode fournisseur hérité peut avoir un léger impact sur la sécurité/les fonctionnalités mais aide pendant la migration. Testez minutieusement, car certaines fonctionnalités d'OpenSSL 3 (par exemple, les sources d'entropie améliorées) ne seront pas disponibles.

Pour plus de détails, consultez la documentation OpenSSL de Node.js à l'adresse nodejs.org/api/crypto.html. Si vous partagez des messages d'erreur spécifiques, je peux fournir des conseils plus ciblés !