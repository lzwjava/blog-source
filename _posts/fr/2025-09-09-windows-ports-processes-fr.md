---
audio: false
date: 2025-09-09
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Gestion des Ports et Processus Windows
translated: true
type: note
---

Sous Windows, vous pouvez vérifier quels ports sont en écoute — et par quel processus (PID) — en utilisant `netstat`, puis gérer ou arrêter ces processus avec `taskkill`. Cela est souvent nécessaire lors du débogage de projets backend comme les applications Java Spring Boot, Redis ou MySQL. Voici comment procéder :

---

### 1. Vérifier les ports en écoute

Exécutez **Invite de commandes (cmd)** ou **PowerShell** en tant qu'Administrateur :

```bash
netstat -ano | findstr LISTENING
```

* `-a` → affiche toutes les connexions et les ports en écoute
* `-n` → affiche les adresses et les ports sous forme numérique
* `-o` → inclut le PID (Identifiant de Processus)

Exemple de sortie :

```
TCP    0.0.0.0:8080     0.0.0.0:0     LISTENING     12345
TCP    0.0.0.0:3306     0.0.0.0:0     LISTENING     6789
```

Ici :

* Le port `8080` est utilisé par le PID `12345` (probablement votre application Spring Boot).
* Le port `3306` est utilisé par le PID `6789` (MySQL).

---

### 2. Trouver à quel processus correspond ce PID

Vous pouvez faire correspondre le PID à un nom de processus :

```bash
tasklist | findstr 12345
```

La sortie pourrait afficher :

```
java.exe                  12345 Console                    1     512,000 K
```

Cela signifie que votre application Spring Boot s'exécute sur le port 8080.

---

### 3. Arrêter le processus si nécessaire

Si vous souhaitez arrêter ce processus :

```bash
taskkill /PID 12345 /F
```

* `/PID` → spécifie l'identifiant de processus
* `/F` → arrêt forcé

---

### 4. Ports typiques pour les services backend courants

* **Spring Boot (application Java) :** 8080, 8081, etc.
* **MySQL :** 3306
* **Redis :** 6379
* **PostgreSQL :** 5432

Ainsi, si vous voyez ces ports dans la sortie de `netstat`, vous saurez quel service est en cours d'exécution.

---

👉 Conseil pro : Vous pouvez combiner ces commandes en une seule pour trouver directement quel processus utilise un port donné (par exemple, 8080) :

```bash
netstat -ano | findstr :8080
```

Puis prenez le PID et vérifiez-le avec `tasklist`.

---

Souhaitez-vous que je vous montre également une **commande PowerShell en une ligne** qui mappe directement les ports aux noms de processus sans avoir besoin de vérifier séparément avec `tasklist` ?