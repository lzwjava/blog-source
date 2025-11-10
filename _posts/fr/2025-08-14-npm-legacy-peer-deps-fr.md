---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Comprendre l'option npm --legacy-peer-deps
translated: true
type: note
---

### Présentation
L'option `--legacy-peer-deps` est un drapeau utilisé avec npm (Node Package Manager) pour contrôler la façon dont les dépendances peer sont gérées lors de l'installation d'un package. Les dépendances peer sont des dépendances qu'un package s'attend à ce qu'un autre fournisse, mais elles ne sont pas installées automatiquement dans les versions récentes de npm.

### Comportement
- **npm standard (v7+)** : Par défaut, il applique strictement les exigences des dépendances peer. Si un package déclare une dépendance peer qui n'est pas satisfaite, npm avertit ou échoue l'installation pour éviter les conflits.
- **Avec --legacy-peer-deps** : Il revient au comportement plus ancien (de npm v3~v6), où les dépendances peer manquantes sont automatiquement installées, même si cela entraîne des doublons ou des incompatibilités. Cela peut résoudre certains problèmes avec des packages legacy mais peut causer des bugs.

### Exemple d'utilisation
Dans un terminal, vous exécuteriez :
```
npm install some-package --legacy-peer-deps
```
Ceci est souvent utilisé pour les projets qui dépendent de bibliothèques plus anciennes qui n'ont pas mis à jour leurs déclarations de dépendances peer, comme on pouvait le voir dans de nombreuses configurations React ou Angular avant la gestion stricte des peers par npm.

### Quand l'utiliser
Utilisez-la avec parcimonie, car elle contourne les protections et pourrait mener à un dependency hell. Préférez mettre à jour les packages ou utiliser `--force`/`--save-dev` pour de meilleures alternatives. Pour plus de détails, consultez la documentation officielle de npm sur les dépendances peer.