---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Guide de la commande Taskkill de Windows
translated: true
type: note
---

Sous Windows, `taskkill` est un outil en ligne de commande intégré que vous pouvez utiliser pour arrêter (tuer) des processus par leur **ID de processus (PID)** ou par leur **nom d'image (nom de l'exécutable)**.

### Syntaxe de base

```bat
taskkill /PID <process_id> [/F]
taskkill /IM <image_name> [/F]
```

* `/PID <process_id>` → Tuer par ID de processus.
* `/IM <image_name>` → Tuer par nom de processus (ex. : `notepad.exe`).
* `/F` → Terminer le processus de force.
* `/T` → Tuer le processus spécifié et tous les processus enfants.

---

### Exemples

1. **Tuer un processus par PID :**

```bat
taskkill /PID 1234
```

Cela va tenter d'arrêter le processus avec le PID 1234.

2. **Tuer de force un processus par PID :**

```bat
taskkill /PID 1234 /F
```

3. **Tuer un processus par nom :**

```bat
taskkill /IM notepad.exe
```

4. **Tuer de force par nom :**

```bat
taskkill /IM notepad.exe /F
```

5. **Tuer un processus et ses enfants :**

```bat
taskkill /IM cmd.exe /T /F
```

---

### Trouver le PID

Si vous ne connaissez pas le PID :

```bat
tasklist
```

Cela liste tous les processus en cours d'exécution avec leurs PID. Vous pouvez ensuite utiliser `taskkill /PID` sur le bon.

---

⚠️ **Notes**

* Certains processus système ne peuvent pas être tués.
* Vous devrez peut-être exécuter l'Invite de commandes en tant qu'**Administrateur** pour terminer les processus protégés.

---

Souhaitez-vous que je vous montre également comment combiner `tasklist` et `taskkill` en une seule commande (par exemple, tuer automatiquement tous les processus correspondant à un nom) ?