---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast:free
title: Dotation des scripts PowerShell
translated: true
type: note
---

### Utilisation du Dot Sourcing pour les Fonctions PowerShell dans les Fichiers .ps1

Le dot sourcing (en utilisant l'opérateur `.`) charge un script PowerShell (.ps1) dans la mémoire de la session actuelle, rendant ses fonctions et variables disponibles sans exécuter le code de niveau supérieur du script. C'est utile pour importer des modules ou du code réutilisable.

#### Syntaxe de Base
Exécutez cette commande dans votre session PowerShell :
```
. Chemin\Vers\VotreScript.ps1
```
- Remplacez `Chemin\Vers\VotreScript.ps1` par le chemin réel du fichier (utilisez des chemins absolus pour plus de fiabilité).
- Exemple : `. C:\Scripts\MesFonctions.ps1` – Cela charge les fonctions de ce fichier dans votre session.

#### Fonctionnement
- Les fonctions définies dans le script deviennent appelables dans votre session actuelle.
- Les variables sont également importées, mais seulement si elles ne sont pas définies avec une portée locale.
- Évitez le dot sourcing dans les scripts de production ; utilisez des modules pour une meilleure organisation.
- Astuce : Si le chemin contient des espaces, entourez-le de guillemets : `. "C:\Mes Scripts\Fonctions.ps1"`

Problème courant : Si le script contient des erreurs de syntaxe, le dot sourcing échouera avec une erreur. Testez en exécutant `PowerShell -Command ". .\VotreScript.ps1"` depuis une invite de commandes.

### Utilisation de la Stratégie d'Exécution PowerShell

Les stratégies d'exécution sont des paramètres de sécurité qui restreignent les scripts que PowerShell peut exécuter, empêchant l'exécution de code malveillant. Elles sont définies par portée (par exemple, pour toute la machine, ou spécifique à l'utilisateur).

#### Vérifier la Stratégie Actuelle
Exécutez cette commande dans PowerShell :
```
Get-ExecutionPolicy
```
- Exemples de sortie : `Restricted` (bloque tous les scripts), `AllSigned` (uniquement les scripts signés), `RemoteSigned` (scripts distants signés, scripts locaux autorisés), ou `Unrestricted`.

#### Définir ou Modifier la Stratégie
Utilisez `Set-ExecutionPolicy` (nécessite des droits d'administrateur pour les changements au niveau de la machine) :
- Exemple pour autoriser les scripts écrits localement : `Set-ExecutionPolicy RemoteSigned`
- Forcer sans invites : `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force`
- Par portée : `Set-ExecutionPolicy -ExecutionPolicy AllSigned -Scope CurrentUser` (n'affecte que votre compte utilisateur).

#### Stratégies Courantes
- `Restricted` : Par défaut ; aucun script ne s'exécute.
- `AllSigned` : Nécessite des signatures numériques (sécurisé mais peu pratique).
- `RemoteSigned` : Équilibre sécurité et commodité — autorise les scripts locaux, signe les scripts distants.
- `Unrestricted` : Exécute tous les scripts (risqué ; à utiliser avec prudence).
- `Bypass` : Entièrement sans restriction, pour l'automatisation.

Astuce : Les stratégies s'appliquent aux sessions console, mais pas à l'ISE ou à VS Code sauf si elles sont définies. Testez les changements en exécutant un script exemple comme `Write-Host "Hello"`. Pour plus d'informations, consultez la documentation Microsoft : `help about_Execution_Policies`. Si vous êtes dans un environnement d'entreprise, une stratégie de groupe peut remplacer les paramètres locaux.