---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Configuration d'OpenWRT en Pont Sans Fil
translated: true
type: note
---

Avec l'aide de Grok, je continue de travailler sur les points suivants.

---

Pour répondre à votre question "est-ce correct ?" concernant les étapes de configuration d'OpenWRT en tant que pont sans fil, et pour fournir les méthodes correctes pour y parvenir, je vais évaluer les étapes que vous avez fournies et les affiner en me basant sur les meilleures pratiques pour OpenWRT. Votre objectif est de configurer votre routeur OpenWRT (par exemple, Xiaomi Mi Router 4C avec OpenWRT 24.10.0) comme un pont sans fil - se connectant sans fil à un réseau Wi-Fi existant en tant que client et partageant cette connexion via son propre point d'accès (AP) Wi-Fi ou ses ports Ethernet, en gardant tous les appareils sur le même sous-réseau que le routeur principal.

Les étapes que vous avez fournies sont globalement exactes mais manquent un ajustement critique pour assurer un pontage correct et éviter les conflits IP. Ci-dessous, je vais d'abord évaluer votre configuration, puis présenter les étapes correctes et complètes pour réaliser un pont sans fil dans OpenWRT en utilisant la méthode du pont simple (client + AP sur le même pont), qui correspond à votre intention. Je mentionnerai également brièvement une alternative utilisant `relayd` pour les cas où la méthode simple échoue, bien que votre configuration supporte probablement l'approche plus simple.

---

### **Évaluation de Vos Étapes Fournies**

Vos étapes visent à :
1. Connecter le routeur OpenWRT en tant que client à un réseau Wi-Fi existant.
2. Configurer un AP pour diffuser un nouveau réseau Wi-Fi.
3. Pontrer les interfaces client et AP pour partager l'internet.

Voici un examen rapide :
- **Étape 1 : Se connecter à LuCI** - Correct, l'accès à l'interface web est le point de départ.
- **Étape 2 : Configurer le client sans fil** - Rejoindre le Wi-Fi cible et l'assigner au réseau `lan` est un bon début, mais la configuration par défaut de `lan` dans OpenWRT (IP statique, typiquement 192.168.1.1) pourrait entrer en conflit avec le routeur principal s'il utilise la même IP. Ceci nécessite un ajustement.
- **Étape 3 : Configurer le point d'accès sans fil** - Configurer un AP et l'assigner à `lan` est correct pour le pontage, mais repose sur le fait que l'interface `lan` est correctement configurée.
- **Étape 4 : Pontrer les réseaux** - Assigner les deux interfaces à `lan` les pontre théoriquement, mais sans désactiver le serveur DHCP ou ajuster les paramètres IP, cela pourrait ne pas fonctionner de manière transparente.
- **Étape 5 : Tester la configuration** - Le test est essentiel, mais le succès dépend du fait que les étapes précédentes soient entièrement correctes.

**Ce qui manque ou est incorrect ?**
- Par défaut, l'interface `lan` d'OpenWRT a une IP statique (par exemple, 192.168.1.1) et exécute un serveur DHCP. Si le routeur principal est aussi 192.168.1.1, cela cause un conflit IP. Vous devez configurer l'interface `lan` en mode client DHCP pour obtenir une IP du routeur principal et désactiver le serveur DHCP local pour laisser le routeur principal assigner les IP à tous les appareils.
- L'assignation de la zone firewall à `lan` est correcte pour la simplicité, mais la configuration IP est critique.

Compte tenu de cela, vos étapes sont "globalement correctes" mais incomplètes sans l'ajustement des paramètres de l'interface `lan`. Ci-dessous se trouvent les étapes corrigées.

---

### **Étapes Correctes pour Configurer OpenWRT en Tant que Pont Sans Fil (Méthode du Pont Simple)**

Cette méthode configure votre routeur OpenWRT pour se connecter à un réseau Wi-Fi existant en tant que client et partager cette connexion via son propre AP ou ses ports Ethernet, le tout sur le même sous-réseau que le routeur principal (par exemple, 192.168.1.x). Voici comment procéder via l'interface web LuCI :

#### **Prérequis**
- OpenWRT est installé (par exemple, version 24.10.0 sur Xiaomi Mi Router 4C).
- Vous avez le SSID, le mot de passe et le type de chiffrement (par exemple, WPA2-PSK) du réseau Wi-Fi principal.
- Accès à LuCI à `http://192.168.1.1` (ou l'IP actuelle) et vos identifiants administrateur.

#### **Étape 1 : Se connecter à LuCI**
- Ouvrez un navigateur et allez à `http://192.168.1.1`.
- Connectez-vous avec votre nom d'utilisateur OpenWRT (par défaut : `root`) et votre mot de passe (défini lors de l'installation).

#### **Étape 2 : Configurer le client sans fil**
- **Naviguer vers les paramètres sans fil :**
  - Allez dans **Network > Wireless**.
- **Scanner les réseaux :**
  - Localisez votre radio (par exemple, `radio0` pour 2.4 GHz sur le Mi Router 4C).
  - Cliquez sur **Scan** pour lister les réseaux Wi-Fi disponibles.
- **Rejoindre le réseau Wi-Fi principal :**
  - Trouvez le SSID du Wi-Fi de votre routeur principal.
  - Cliquez sur **Join Network**.
- **Configurer les paramètres client :**
  - **Wi-Fi Key :** Entrez le mot de passe du Wi-Fi principal.
  - **Network :** Sélectionnez ou définissez `lan` (cela ajoute l'interface client au pont `br-lan`).
  - **Firewall Zone :** Assignez à `lan` (cela simplifie les règles de trafic pour le pontage).
  - **Interface Name :** LuCI peut suggérer `wwan` ; vous pouvez la laisser ou la renommer `client` pour plus de clarté, mais assurez-vous qu'elle est liée à `lan`.
- **Sauvegarder et Appliquer :**
  - Cliquez sur **Save & Apply** pour vous connecter au Wi-Fi principal.

#### **Étape 3 : Ajuster l'interface LAN en client DHCP**
- **Aller dans Interfaces :**
  - Naviguez vers **Network > Interfaces**.
- **Modifier l'interface LAN :**
  - Cliquez sur **Edit** à côté de l'interface `lan`.
- **Définir le protocole sur client DHCP :**
  - Dans la liste déroulante **Protocol**, sélectionnez **DHCP client**.
  - Cela permet au pont `br-lan` (qui inclut maintenant le client sans fil) d'obtenir une adresse IP du serveur DHCP du routeur principal (par exemple, 192.168.1.x).
- **Désactiver le serveur DHCP :**
  - Puisque `lan` est maintenant un client DHCP, le serveur DHCP local est automatiquement désactivé. Vérifiez ceci sous **Advanced Settings** ou **DHCP and DNS** - assurez-vous que "Ignore interface" est coché si l'option apparaît.
- **Sauvegarder et Appliquer :**
  - Cliquez sur **Save & Apply**. Le routeur va maintenant demander une IP au routeur principal.

#### **Étape 4 : Configurer le point d'accès sans fil**
- **Ajouter un nouveau réseau sans fil :**
  - Retournez dans **Network > Wireless**.
  - Cliquez sur **Add** sous la même radio (par exemple, `radio0`) pour créer une nouvelle interface sans fil.
- **Configurer l'AP :**
  - **ESSID :** Choisissez un nom pour votre Wi-Fi (par exemple, `OpenWRT_AP`).
  - **Mode :** Définissez sur **Access Point (AP)**.
  - **Network :** Assignez à `lan` (cela le pontre avec l'interface client et les ports Ethernet).
- **Configurer la sécurité :**
  - Allez dans l'onglet **Wireless Security**.
  - **Encryption :** Sélectionnez **WPA2-PSK** (recommandé).
  - **Key :** Définissez un mot de passe fort pour votre AP.
- **Sauvegarder et Appliquer :**
  - Cliquez sur **Save & Apply**. Votre routeur diffusera maintenant son propre Wi-Fi.

#### **Étape 5 : Vérifier le pont**
- **Vérifier les interfaces :**
  - Allez dans **Network > Interfaces**.
  - Assurez-vous que l'interface `lan` liste à la fois le client sans fil (par exemple, `wlan0`) et l'AP (par exemple, `wlan0-1`) sous le pont `br-lan`.
- **Vérifier l'assignation IP :**
  - Allez dans **Status > Overview**.
  - Notez l'adresse IP assignée à l'interface `lan` par le routeur principal (par exemple, `192.168.1.100`).

#### **Étape 6 : Tester la configuration**
- **Tester le Wi-Fi :**
  - Connectez un appareil au Wi-Fi `OpenWRT_AP`.
  - Vérifiez qu'il reçoit une IP du routeur principal (par exemple, `192.168.1.x`) et a accès à internet.
- **Tester Ethernet (si applicable) :**
  - Branchez un appareil sur un des ports LAN du routeur.
  - Confirmez qu'il obtient une IP du routeur principal et se connecte à internet.
- **Accéder à LuCI :**
  - Utilisez la nouvelle adresse IP (par exemple, `http://192.168.1.100`) pour accéder à l'interface OpenWRT.

---

### **Pourquoi Cela Fonctionne**
- Assigner à la fois les interfaces client et AP au réseau `lan` les ajoute au pont `br-lan`, permettant au trafic de couler entre elles et le routeur principal au niveau de la couche 2.
- Configurer `lan` en client DHCP assure que le routeur OpenWRT obtient une IP unique du routeur principal, évitant les conflits (par exemple, avec `192.168.1.1`), et désactive le serveur DHCP local pour que le routeur principal gère toutes les assignations IP.
- Les appareils connectés à l'AP ou aux ports Ethernet apparaissent sur le même sous-réseau que le réseau principal (par exemple, `192.168.1.x`), satisfaisant l'exigence du pont sans fil.

---

### **Méthode Alternative : Utilisation de relayd (Pseudo-Pont)**
Si la méthode du pont simple échoue (par exemple, à cause de limitations des pilotes sans fil), vous pouvez utiliser le paquet `relayd` pour un pseudo-pont. Cela crée une configuration routée où les clients du routeur OpenWRT sont sur un sous-réseau différent, mais c'est plus fiable sur certains matériels. Voici un bref aperçu :

1. **Installer relayd :**
   - Allez dans **System > Software**, cherchez `relayd`, et installez-le.
2. **Configurer le client sans fil :**
   - Rejoignez le Wi-Fi principal, mais assignez-le à une nouvelle interface (par exemple, `wwan`) configurée en client DHCP.
3. **Configurer le LAN :**
   - Définissez `lan` sur une IP statique (par exemple, `192.168.2.1`) avec son propre serveur DHCP.
4. **Configurer relayd :**
   - Configurez `relayd` via SSH ou LuCI (sous **Network > Hostnames**) pour relayer entre `wwan` et `lan`.
5. **Configurer l'AP :**
   - Définissez l'AP sur le réseau `lan`.
6. **Tester :**
   - Les appareils sur `OpenWRT_AP` seront sur `192.168.2.x`, avec internet relayé depuis le routeur principal.

**Note :** Ce n'est pas un vrai pont (sous-réseaux différents), donc utilisez-le seulement si la méthode simple ne fonctionne pas. Pour votre Xiaomi Mi Router 4C avec OpenWRT 24.10.0, le pont simple devrait suffire.

---

### **Conclusion**
Vos étapes originales sont **globalement correctes** mais incomplètes sans configurer l'interface `lan` en mode client DHCP pour éviter les conflits IP et assurer un pontage correct. Les étapes corrigées ci-dessus fournissent un moyen fiable de configurer OpenWRT en tant que pont sans fil. Si vous les suivez, votre routeur se connectera au Wi-Fi principal et partagera cette connexion de manière transparente via son AP ou ses ports Ethernet, le tout sur le même sous-réseau. Testez la configuration, et si des problèmes surviennent (rares avec OpenWRT moderne), considérez l'alternative `relayd`.