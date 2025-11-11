---
audio: false
generated: true
lang: fr
layout: post
title: Utilisation de Get-NetTCPConnection dans PowerShell
translated: true
type: note
---

La cmdlet `Get-NetTCPConnection` dans PowerShell récupère des informations sur les connexions TCP sur un système Windows. Elle fait partie du module `NetTCPIP`, disponible sur Windows 8/Windows Server 2012 et versions ultérieures. Voici un guide concis sur son utilisation :

### Utilisation de base
Exécutez `Get-NetTCPConnection` pour lister toutes les connexions TCP actives :

```powershell
Get-NetTCPConnection
```

Cela retourne des détails comme LocalAddress, LocalPort, RemoteAddress, RemotePort, State et OwningProcess.

### Paramètres courants
- **-State** : Filtrer par état de connexion (par exemple, Established, Listening, TimeWait).
  ```powershell
  Get-NetTCPConnection -State Established
  ```
- **-LocalPort** : Filtrer par numéro de port local.
  ```powershell
  Get-NetTCPConnection -LocalPort 80
  ```
- **-RemoteAddress** : Filtrer par adresse IP distante.
  ```powershell
  Get-NetTCPConnection -RemoteAddress 192.168.1.1
  ```
- **-RemotePort** : Filtrer par port distant.
  ```powershell
  Get-NetTCPConnection -RemotePort 443
  ```
- **-OwningProcess** : Filtrer par l'ID de processus (PID) propriétaire de la connexion.
  ```powershell
  Get-NetTCPConnection -OwningProcess 1234
  ```

### Combinaison de filtres
Vous pouvez combiner les paramètres pour des résultats plus spécifiques :
```powershell
Get-NetTCPConnection -State Established -LocalPort 80
```

### Afficher des propriétés spécifiques
Utilisez `Select-Object` pour afficher uniquement les propriétés souhaitées :
```powershell
Get-NetTCPConnection | Select-Object LocalAddress, LocalPort, RemoteAddress, RemotePort, State
```

### Trouver les détails d'un processus
Pour identifier le processus derrière une connexion, combinez avec `Get-Process` :
```powershell
Get-NetTCPConnection -LocalPort 80 | ForEach-Object { Get-Process -Id $_.OwningProcess }
```

### Trier et formater la sortie
Triez les résultats (par exemple, par LocalPort) et formatez-les en tableau :
```powershell
Get-NetTCPConnection | Sort-Object LocalPort | Format-Table LocalAddress, LocalPort, RemoteAddress, RemotePort, State
```

### Exemples pratiques
1. **Lister toutes les connexions en écoute :**
   ```powershell
   Get-NetTCPConnection -State Listening
   ```
2. **Trouver les connexions vers un serveur distant spécifique :**
   ```powershell
   Get-NetTCPConnection -RemoteAddress "8.8.8.8"
   ```
3. **Vérifier quel processus utilise un port spécifique :**
   ```powershell
   $connection = Get-NetTCPConnection -LocalPort 8080
   Get-Process -Id $connection.OwningProcess
   ```

### Notes
- **Privilèges d'administrateur** : Certains détails (par exemple, OwningProcess pour les processus système) peuvent nécessiter l'exécution de PowerShell en tant qu'Administrateur.
- **IPv4/IPv6** : La cmdlet gère à la fois les connexions IPv4 et IPv6.
- **Exporter les résultats** : Sauvegardez la sortie dans un fichier avec `Export-Csv` :
  ```powershell
  Get-NetTCPConnection | Export-Csv -Path "tcp_connections.csv" -NoTypeInformation
  ```

Pour plus de détails, exécutez :
```powershell
Get-Help Get-NetTCPConnection -Full
```

Si vous avez besoin d'exemples spécifiques ou d'un cas d'utilisation particulier, faites-le moi savoir !