---
audio: false
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Arrêt des processus Cisco AnyConnect
translated: true
type: note
---

Compris 👍 — vous demandez comment arrêter/tuer **les processus Cisco AnyConnect** comme *NAM* (Network Access Manager) ou le service en arrière-plan *vpnagent.exe* qui s'exécute lorsque AnyConnect est installé.

Voici une explication :

---

## 1. Comprendre les processus
- **vpnagent.exe** → Le service en arrière-plan "Cisco AnyConnect Secure Mobility Agent". Il s'exécute au démarrage et gère les connexions VPN et les modules associés (y compris NAM si installé).
- **Service NAM** → Installé en tant que **Cisco Network Access Manager** ; il remplace le gestionnaire de réseau intégré de Windows et s'exécute automatiquement au démarrage du système s'il est activé.

---

## 2. Arrêter / tuer les processus AnyConnect (Windows)
### Option A : Arrêter le service correctement
1. Appuyez sur **Win+R**, tapez `services.msc`, appuyez sur Entrée.
2. Recherchez :
   - *Cisco AnyConnect Secure Mobility Agent*
   - *Cisco Network Access Manager* (s'il est installé)
3. Clic droit → **Arrêter**.
4. Pour empêcher le démarrage automatique : clic droit → Propriétés → Définir le **Type de démarrage** sur *Désactivé* (ou *Manuel*).

### Option B : Tuer via le Gestionnaire des tâches
1. Appuyez sur **Ctrl+Maj+Échap** pour ouvrir le Gestionnaire des tâches.
2. Trouvez `vpnagent.exe` ou tout processus Cisco AnyConnect.
3. Clic droit → **Terminer la tâche**.  
   *(Cela ne dure que jusqu'au redémarrage ou si le service redémarre automatiquement.)*

---

## 3. Désinstaller les modules que vous ne voulez pas
Si vous ne voulez que le VPN et pas NAM :
1. Allez dans **Panneau de configuration → Programmes et fonctionnalités**.
2. Trouvez **Cisco AnyConnect Secure Mobility Client**.
3. Cliquez sur **Modifier** → Modifier l'installation.
4. Décochez **Network Access Manager** (gardez VPN activé si vous en avez encore besoin).
5. Terminez — cela supprime NAM de manière chirurgicale mais laisse le VPN fonctionnel.

---

## ⚠️ Notes / Mises en garde
- Tuer `vpnagent.exe` directement supprimera également la fonctionnalité VPN AnyConnect jusqu'à ce que vous le redémarriez.
- Si NAM gère le Wi-Fi/éthernet, le tuer sans revenir au gestionnaire de réseau Windows peut interrompre votre connexion réseau.
- La meilleure pratique est de désactiver/désinstaller NAM si vous n'en avez pas besoin, plutôt que de simplement le forcer à s'arrêter.

---

👉 Souhaitez-vous que je vous montre également la **méthode en ligne de commande / PowerShell** pour arrêter et désactiver les services `vpnagent` et NAM (afin que vous n'ayez pas à aller dans services.msc à chaque fois) ?