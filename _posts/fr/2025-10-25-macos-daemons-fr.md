---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Processus démons par défaut de macOS
translated: true
type: note
---

### Processus démons par défaut dans macOS

Dans macOS, les processus démons sont des services en arrière-plan qui s'exécutent sans interface utilisateur, démarrant généralement au démarrage ou à la demande. Ils sont gérés par **launchd**, le framework d'initialisation et de gestion des services du système (PID 1). Les démons diffèrent des agents : les démons s'exécutent en tant que root/à l'échelle du système (avant la connexion), tandis que les agents s'exécutent par utilisateur (après la connexion).

Les démons système par défaut sont définis dans des fichiers de liste de propriétés (.plist) situés dans `/System/Library/LaunchDaemons/`. Il y en a généralement autour de 300 à 350 sur une installation standard (par exemple, 339 sur macOS 10.14 Mojave), couvrant tout, du réseau et de la sécurité à la gestion du matériel. Les démons installés par l'utilisateur ou tiers vont dans `/Library/LaunchDaemons/`.

#### Comment visualiser les démons par défaut
Pour lister tous les démons (et agents) chargés dans le Terminal :
- `sudo launchctl list` (affiche les démons et agents système).
- `launchctl list` (affiche uniquement les agents spécifiques à l'utilisateur).

Pour un listing complet du répertoire : `ls /System/Library/LaunchDaemons/` (ne nécessite pas de sudo, mais les fichiers sont en lecture seule).

Ces commandes produisent des colonnes comme PID, statut et label (par exemple, `com.apple.timed`).

#### Le démon "timed"
Vous avez spécifiquement mentionné "timed", qui fait référence à **com.apple.timed** (le Time Sync Daemon). Il s'agit d'un démon système central introduit dans macOS High Sierra (10.13) pour remplacer l'ancien processus `ntpd`.

- **Objectif** : Il synchronise automatiquement l'horloge système du Mac avec les serveurs NTP (Network Time Protocol) pour la précision, les interrogeant toutes les 15 minutes. Cela garantit une mesure du temps précise pour les journaux, les certificats et les opérations réseau.
- **Fonctionnement** : Lancé par launchd depuis `/System/Library/LaunchDaemons/com.apple.timed.plist`, il s'exécute en tant qu'utilisateur `_timed` (dans les groupes `_timed` et `_sntpd`). Il utilise l'appel système `settimeofday` pour ajuster l'horloge en fonction des réponses des serveurs. La configuration se trouve dans `/etc/ntpd.conf` (serveurs NTP) et l'état est mis en cache dans `/var/db/timed/com.apple.timed.plist`.
- **Liens** : Est lié aux Réglages Système > Général > Date & Heure > "Régler la date et l'heure automatiquement". Si cette option est désactivée, timed ne se synchronisera pas. Pour les configurations avancées (par exemple, besoins de haute précision), des outils comme Chrony peuvent le remplacer, mais il faut alors désactiver timed.

Si votre horloge dérive, vérifiez les problèmes de réseau ou les blocages de pare-feu sur NTP (port UDP 123).

#### Autres démons par défaut courants ("etc.")
Voici un tableau de quelques démons système par défaut fréquemment en cours d'exécution, regroupés par fonction. Cette liste n'est pas exhaustive (il y en a des centaines), mais couvre les éléments essentiels. Les labels proviennent des noms de fichiers .plist.

| Catégorie       | Label du démon                  | Description |
|----------------|-------------------------------|-------------|
| **Système central** | `com.apple.launchd`          | Le processus launchd lui-même ; démarre tous les autres. |
| **Temps & Synchronisation** | `com.apple.timed`             | Synchronisation de l'heure NTP (comme ci-dessus). |
| **Gestion des utilisateurs** | `com.apple.opendirectoryd`   | Gère les comptes utilisateurs/groupes et les services d'annuaire. |
| **Gestion des utilisateurs** | `com.apple.accounts`         | Gère les comptes utilisateurs et l'authentification. |
| **Réseau** | `com.apple.mDNSResponder`    | Bonjour/mDNS pour la découverte sur le réseau local (par exemple, AirDrop). |
| **Réseau** | `com.apple.nesessionmanager` | Gestion des extensions réseau et des VPN. |
| **Bluetooth/Sans fil** | `com.apple.bluetoothd`      | Gestion des appareils Bluetooth. |
| **iCloud/Synchronisation** | `com.apple.cloudd`            | Synchronisation des données iCloud et services associés. |
| **Sécurité**   | `com.apple.securityd`        | Gestion du trousseau et des informations d'identification (souvent aussi en tant qu'agent). |
| **Mises à jour**    | `com.apple.softwareupdated`  | Gère les mises à jour logicielles et les téléchargements de catalogues. |
| **Matériel**   | `com.apple.kextd`             | Chargement et gestion des extensions du noyau. |
| **Journalisation**    | `com.apple.systemnotificationd` | Notifications système et journalisation. |
| **MDM (si activé)** | `com.apple.mdmclient`     | Client Mobile Device Management pour les environnements d'entreprise. |

Ces processus s'exécutent continuellement ou sur des déclencheurs pour maintenir la stabilité de macOS. Si l'un d'eux dysfonctionne (par exemple, CPU élevé), vous pouvez le décharger temporairement avec `sudo launchctl unload /System/Library/LaunchDaemons/com.apple.example.plist`, mais évitez de modifier les fichiers système.

Pour une liste complète et actuelle sur votre Mac (en octobre 2025, probablement macOS 15 Sequoia ou ultérieur), exécutez les commandes ci-dessus — les versions évoluent légèrement avec les mises à jour.

#### Références
- [The macOS Process Journey — “timed” (Time Sync Daemon)](https://medium.com/@boutnaru/the-macos-process-journey-timed-time-sync-daemon-4898c8185b4b)
- [Daemons and Agents could be slowing down your Mac](https://appleinsider.com/inside/macos/tips/daemons-and-agents-could-be-slowing-down-your-mac)
- [What files are included in the /System/Library/LaunchAgents and /System/Library/LaunchDaemons](https://apple.stackexchange.com/questions/361029/what-files-are-included-in-the-system-library-launchagents-and-system-library)
- [Script management with launchd in Terminal on Mac](https://support.apple.com/guide/terminal/script-management-with-launchd-apdc6c1077b-5d5d-4d35-9c19-60f2397b2369/mac)
- [How to show all running launchctl daemons/agents?](https://apple.stackexchange.com/questions/134817/how-to-show-all-running-launchctl-daemons-agents)