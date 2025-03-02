---
audio: true
generated: true
lang: fr
layout: post
title: Configurer OpenWRT en tant que pont sans fil
translated: true
---

Avec l'aide de Grok, je continue de travailler sur ce qui suit.

---

Pour répondre à votre question, "est-ce correct ?" concernant les étapes pour configurer OpenWRT comme un pont sans fil, et pour fournir les bonnes façons de le faire, j’évaluerai les étapes que vous avez fournies et les affinerai en fonction des meilleures pratiques pour OpenWRT. Votre objectif est de configurer votre routeur OpenWRT (par exemple, Xiaomi Mi Router 4C avec OpenWRT 24.10.0) comme un pont sans fil—se connectant sans fil à un réseau Wi-Fi existant en tant que client et partageant cette connexion via son propre point d'accès Wi-Fi (AP) ou ports Ethernet, en gardant tous les appareils sur le même sous-réseau que le routeur principal.

Vos étapes fournies sont pour la plupart exactes mais manquent d'un ajustement critique pour assurer un pontage correct et éviter les conflits d'IP. Ci-dessous, j’évaluerai d'abord votre configuration, puis je présenterai les étapes correctes et complètes pour obtenir un pont sans fil dans OpenWRT en utilisant la méthode de pont simple (client + AP sur le même pont), qui correspond à votre intention. Je mentionnerai brièvement une alternative utilisant `relayd` pour les cas où la méthode simple échoue, bien que votre configuration supporte probablement l'approche plus simple.

---

### **Évaluation de vos étapes fournies**

Vos étapes visent à :
1. Connecter le routeur OpenWRT en tant que client à un réseau Wi-Fi existant.
2. Configurer un AP pour diffuser un nouveau réseau Wi-Fi.
3. Ponter les interfaces client et AP pour partager l'internet.

Voici un rapide examen :
- **Étape 1 : Connexion à LuCI** - Correct, accéder à l'interface web est le point de départ.
- **Étape 2 : Configurer le client sans fil** - Rejoindre le Wi-Fi cible et l'attribuer au réseau `lan` est un bon début, mais la configuration `lan` par défaut dans OpenWRT (IP statique, généralement 192.168.1.1) pourrait entrer en conflit avec le routeur principal s'il utilise la même IP. Cela nécessite un ajustement.
- **Étape 3 : Configurer le point d'accès sans fil** - Configurer un AP et l'attribuer à `lan` est correct pour le pontage, mais dépend de l'interface `lan` étant correctement configurée.
- **Étape 4 : Ponter les réseaux** - Attribuer les deux interfaces à `lan` théoriquement les ponte, mais sans désactiver le serveur DHCP ou ajuster les paramètres IP, cela pourrait ne pas fonctionner de manière fluide.
- **Étape 5 : Tester la configuration** - Le test est essentiel, mais le succès dépend des étapes précédentes étant entièrement correctes.

**Ce qui manque ou est incorrect ?**
- Par défaut, l'interface `lan` d'OpenWRT a une IP statique (par exemple, 192.168.1.1) et exécute un serveur DHCP. Si le routeur principal est également 192.168.1.1, cela provoque un conflit d'IP. Vous devez définir l'interface `lan` en mode client DHCP pour obtenir une IP du routeur principal et désactiver le serveur DHCP local pour laisser le routeur principal attribuer des IP à tous les appareils.
- L'attribution de la zone de pare-feu à `lan` est correcte pour la simplicité, mais la configuration IP est critique.

Avec cela à l'esprit, vos étapes sont "pour la plupart correctes" mais incomplètes sans ajuster les paramètres de l'interface `lan`. Voici les étapes corrigées.

---

### **Étapes correctes pour configurer OpenWRT comme un pont sans fil (Méthode de pont simple)**

Cette méthode configure votre routeur OpenWRT pour se connecter à un réseau Wi-Fi existant en tant que client et partager cette connexion via son propre AP ou ports Ethernet, tous sur le même sous-réseau que le routeur principal (par exemple, 192.168.1.x). Voici comment le faire via l'interface web LuCI :

#### **Prérequis**
- OpenWRT est installé (par exemple, version 24.10.0 sur Xiaomi Mi Router 4C).
- Vous avez le SSID, le mot de passe et le type de chiffrement (par exemple, WPA2-PSK) du réseau Wi-Fi principal.
- Accès à LuCI à `http://192.168.1.1` (ou l'IP actuelle) et vos identifiants d'administrateur.

#### **Étape 1 : Connexion à LuCI**
- Ouvrez un navigateur et accédez à `http://192.168.1.1`.
- Connectez-vous avec votre nom d'utilisateur OpenWRT (par défaut : `root`) et votre mot de passe (défini pendant l'installation).

#### **Étape 2 : Configurer le client sans fil**
- **Naviguer vers les paramètres sans fil :**
  - Allez à **Réseau > Sans fil**.
- **Scanner les réseaux :**
  - Localisez votre radio (par exemple, `radio0` pour 2,4 GHz sur le Mi Router 4C).
  - Cliquez sur **Scanner** pour lister les réseaux Wi-Fi disponibles.
- **Rejoindre le réseau Wi-Fi principal :**
  - Trouvez le SSID du Wi-Fi de votre routeur principal.
  - Cliquez sur **Rejoindre le réseau**.
- **Configurer les paramètres du client :**
  - **Clé Wi-Fi :** Entrez le mot de passe pour le Wi-Fi principal.
  - **Réseau :** Sélectionnez ou définissez sur `lan` (ceci ajoute l'interface client au pont `br-lan`).
  - **Zone de pare-feu :** Attribuez à `lan` (ceci simplifie les règles de trafic pour le pontage).
  - **Nom de l'interface :** LuCI peut suggérer `wwan` ; vous pouvez le laisser ou le renommer en `client` pour plus de clarté, mais assurez-vous qu'il est lié à `lan`.
- **Enregistrer et appliquer :**
  - Cliquez sur **Enregistrer et appliquer** pour vous connecter au Wi-Fi principal.

#### **Étape 3 : Ajuster l'interface LAN en client DHCP**
- **Aller aux interfaces :**
  - Naviguez vers **Réseau > Interfaces**.
- **Éditer l'interface LAN :**
  - Cliquez sur **Éditer** à côté de l'interface `lan`.
- **Définir le protocole sur client DHCP :**
  - Dans le menu déroulant **Protocole**, sélectionnez **Client DHCP**.
  - Cela permet au pont `br-lan` (qui inclut maintenant le client sans fil) d'obtenir une adresse IP du serveur DHCP du routeur principal (par exemple, 192.168.1.x).
- **Désactiver le serveur DHCP :**
  - Puisque `lan` est maintenant un client DHCP, le serveur DHCP local est automatiquement désactivé. Vérifiez ceci sous **Paramètres avancés** ou **DHCP et DNS**—assurez-vous que "Ignorer l'interface" est coché si l'option apparaît.
- **Enregistrer et appliquer :**
  - Cliquez sur **Enregistrer et appliquer**. Le routeur demandera maintenant une IP au routeur principal.

#### **Étape 4 : Configurer le point d'accès sans fil**
- **Ajouter un nouveau réseau sans fil :**
  - Revenez à **Réseau > Sans fil**.
  - Cliquez sur **Ajouter** sous la même radio (par exemple, `radio0`) pour créer une nouvelle interface sans fil.
- **Configurer l'AP :**
  - **ESSID :** Choisissez un nom pour votre Wi-Fi (par exemple, `OpenWRT_AP`).
  - **Mode :** Définir sur **Point d'accès (AP)**.
  - **Réseau :** Attribuer à `lan` (ceci le ponte avec l'interface client et les ports Ethernet).
- **Configurer la sécurité :**
  - Allez à l'onglet **Sécurité sans fil**.
  - **Chiffrement :** Sélectionnez **WPA2-PSK** (recommandé).
  - **Clé :** Définissez un mot de passe fort pour votre AP.
- **Enregistrer et appliquer :**
  - Cliquez sur **Enregistrer et appliquer**. Votre routeur diffusera maintenant son propre Wi-Fi.

#### **Étape 5 : Vérifier le pont**
- **Vérifier les interfaces :**
  - Allez à **Réseau > Interfaces**.
  - Assurez-vous que l'interface `lan` liste à la fois le client sans fil (par exemple, `wlan0`) et l'AP (par exemple, `wlan0-1`) sous le pont `br-lan`.
- **Vérifier l'attribution IP :**
  - Allez à **Statut > Aperçu**.
  - Notez l'adresse IP attribuée à l'interface `lan` par le routeur principal (par exemple, `192.168.1.100`).

#### **Étape 6 : Tester la configuration**
- **Tester le Wi-Fi :**
  - Connectez un appareil au Wi-Fi `OpenWRT_AP`.
  - Vérifiez qu'il reçoit une IP du routeur principal (par exemple, `192.168.1.x`) et a accès à internet.
- **Tester l'Ethernet (si applicable) :**
  - Branchez un appareil sur l'un des ports LAN du routeur.
  - Confirmez qu'il obtient une IP du routeur principal et se connecte à internet.
- **Accéder à LuCI :**
  - Utilisez la nouvelle adresse IP (par exemple, `http://192.168.1.100`) pour accéder à l'interface OpenWRT.

---

### **Pourquoi cela fonctionne**
- Attribuer les interfaces client et AP au réseau `lan` les ajoute au pont `br-lan`, permettant au trafic de couche 2 de circuler entre eux et le routeur principal.
- Définir `lan` en mode client DHCP assure que le routeur OpenWRT obtient une IP unique du routeur principal, évitant les conflits (par exemple, avec `192.168.1.1`), et désactive le serveur DHCP local pour que le routeur principal gère toutes les attributions d'IP.
- Les appareils connectés à l'AP ou aux ports Ethernet apparaissent sur le même sous-réseau que le réseau principal (par exemple, `192.168.1.x`), répondant à l'exigence de pont sans fil.

---

### **Méthode alternative : Utilisation de relayd (Pseudo-pont)**
Si la méthode de pont simple échoue (par exemple, en raison de limitations du pilote sans fil), vous pouvez utiliser le package `relayd` pour un pseudo-pont. Cela crée une configuration routée où les clients du routeur OpenWRT sont sur un sous-réseau différent, mais c'est plus fiable sur certains matériels. Voici un bref aperçu :

1. **Installer relayd :**
   - Allez à **Système > Logiciels**, recherchez `relayd`, et installez-le.
2. **Configurer le client sans fil :**
   - Rejoignez le Wi-Fi principal, mais attribuez-le à une nouvelle interface (par exemple, `wwan`) définie en client DHCP.
3. **Configurer LAN :**
   - Définissez `lan` sur une IP statique (par exemple, `192.168.2.1`) avec son propre serveur DHCP.
4. **Configurer relayd :**
   - Configurez `relayd` via SSH ou LuCI (sous **Réseau > Noms d'hôte**) pour relayer entre `wwan` et `lan`.
5. **Configurer AP :**
   - Définissez l'AP sur le réseau `lan`.
6. **Tester :**
   - Les appareils sur `OpenWRT_AP` seront sur `192.168.2.x`, avec internet relayé depuis le routeur principal.

**Note :** Ce n'est pas un vrai pont (sous-réseaux différents), utilisez-le uniquement si la méthode simple ne fonctionne pas. Pour votre Xiaomi Mi Router 4C avec OpenWRT 24.10.0, le pont simple devrait suffire.

---

### **Conclusion**
Vos étapes originales sont **pour la plupart correctes** mais incomplètes sans définir l'interface `lan` en mode client DHCP pour éviter les conflits d'IP et assurer un pontage correct. Les étapes corrigées ci-dessus fournissent une méthode fiable pour configurer OpenWRT comme un pont sans fil. Si vous les suivez, votre routeur se connectera au Wi-Fi principal et partagera cette connexion de manière fluide via son AP ou ses ports Ethernet, tous sur le même sous-réseau. Testez la configuration, et si des problèmes surviennent (rare avec OpenWRT moderne), envisagez l'alternative `relayd`.