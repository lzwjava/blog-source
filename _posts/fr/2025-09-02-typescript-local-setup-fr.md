---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Guide de Configuration Locale TypeScript
translated: true
type: note
---

Pour exécuter TypeScript localement, vous utiliserez généralement **npm** et le compilateur TypeScript (`tsc`). Voici un guide étape par étape :

---

### 1. Initialiser votre projet

Si vous n'avez pas encore de fichier `package.json` :

```bash
npm init -y
```

Cela crée un `package.json` pour que vous puissiez gérer les dépendances.

---

### 2. Installer TypeScript

Installez-le en tant que dépendance de développement :

```bash
npm install typescript --save-dev
```

Si vous voulez aussi que le compilateur TypeScript (`tsc`) soit disponible globalement :

```bash
npm install -g typescript
```

---

### 3. Créer un fichier tsconfig.json

Générez un fichier de configuration par défaut :

```bash
npx tsc --init
```

Cela crée `tsconfig.json` qui contrôle la façon dont TypeScript compile vos fichiers (cible, système de modules, mode strict, etc.).

---

### 4. Écrire un fichier TypeScript

Exemple `index.ts` :

```ts
function greet(name: string): string {
  return `Hello, ${name}!`;
}

console.log(greet("World"));
```

---

### 5. Compiler TypeScript

Exécutez :

```bash
npx tsc
```

Cela compile tous les fichiers `.ts` selon les règles de `tsconfig.json`.

Ou, pour compiler un seul fichier :

```bash
npx tsc index.ts
```

Cela génère un fichier `.js` (par exemple, `index.js`).

---

### 6. Exécuter le JavaScript compilé

Utilisez Node.js :

```bash
node index.js
```

---

### 7. Optionnel : Compilation automatique à la sauvegarde

Exécutez avec `--watch` pour qu'il recompile à chaque modification :

```bash
npx tsc --watch
```

---

👉 C'est le flux de travail standard :
`npm install` → `tsc` (compiler) → `node` (exécuter le code compilé).

---

Souhaitez-vous que je vous montre aussi comment **éviter la compilation manuelle** en exécutant TypeScript directement avec `ts-node` ?