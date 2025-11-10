---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Localiser et tuer le processus du port JMX
translated: true
type: note
---

Compris — vous voulez vérifier quel programme Java sur Windows a ouvert un **agent JMX distant** sur le port `9091`, puis le tuer si nécessaire. Voici comment procéder étape par étape :

---

### 1. Trouver le Processus Utilisant le Port 9091

Ouvrez **l'Invite de commandes** (en tant qu'Administrateur si possible), et exécutez :

```cmd
netstat -ano | findstr :9091
```

Cela affichera quelque chose comme :

```
  TCP    0.0.0.0:9091    0.0.0.0:0    LISTENING    12345
```

* La dernière colonne (`12345` ici) est le **PID (Identifiant de Processus)**.

---

### 2. Identifier à Quel Programme Ce PID Correspond

Maintenant, associez le PID au programme réel :

```cmd
tasklist /FI "PID eq 12345"
```

Cela affichera quelque chose comme :

```
Nom de l’Image                 PID   Nom de Session    Utilisation Mémoire
========================= ======== ================ ============
java.exe                    12345 Console           200,000 K
```

S'il s'agit d'un processus Java, vous pouvez obtenir encore plus de détails :

```cmd
wmic process where processid=12345 get CommandLine
```

Cette commande affiche la **ligne de commande** utilisée pour lancer la JVM — vous verrez les flags JMX (`-Dcom.sun.management.jmxremote.port=9091`), ce qui confirme qu'il s'agit bien de l'agent JMX distant.

---

### 3. Tuer le Processus

Si vous avez confirmé qu'il est sûr de l'arrêter, vous pouvez le tuer :

```cmd
taskkill /PID 12345 /F
```

* `/PID` spécifie l'identifiant du processus.
* `/F` force la termination.

---

### 4. Alternative avec PowerShell

Si vous préférez PowerShell, vous pouvez exécuter :

```powershell
Get-Process -Id (Get-NetTCPConnection -LocalPort 9091).OwningProcess
```

Pour tuer directement :

```powershell
Stop-Process -Id (Get-NetTCPConnection -LocalPort 9091).OwningProcess -Force
```

---

🔎 Résumé :

1. `netstat -ano | findstr :9091` → obtenir le PID
2. `tasklist /FI "PID eq <PID>"` → voir quel programme
3. `wmic process where processid=<PID> get CommandLine` → voir les flags JVM
4. `taskkill /PID <PID> /F` → tuer

---

Voulez-vous que je vous montre aussi comment **vérifier plusieurs JVM simultanément** pour les ports des agents JMX (afin de voir si d'autres sont en cours d'exécution sur des ports comme 9090, 9999, etc.) ?