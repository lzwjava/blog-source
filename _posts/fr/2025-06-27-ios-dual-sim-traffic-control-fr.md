---
audio: false
generated: true
lang: fr
layout: post
title: Gestion du Routage du Trafic Double SIM sur iOS avec Considérations du GFW
translated: true
type: note
---

iOS fournit des API qui vous permettent de gérer et de séparer le trafic réseau pour différents forfaits de données cellulaires lors de l'utilisation de la fonctionnalité Dual SIM, mais il existe des limitations, et le contrôle direct du routage du trafic spécifique vers des SIM spécifiques basé sur les restrictions du Grand Firewall de Chine (GFW) n'est pas nativement pris en charge à un niveau granulaire. Cependant, avec une combinaison d'API iOS, de configuration manuelle et potentiellement d'outils tiers, vous pouvez atteindre un certain niveau de séparation pour traiter le trafic différemment pour une SIM de Macao et une SIM de China Telecom. Ci-dessous, je vais décrire les API pertinentes, les configurations et les considérations, y compris comment aborder les défis liés au GFW.

### API et Fonctionnalités Clés d'iOS pour le Dual SIM et la Gestion du Trafic

1. **Framework CoreTelephony** :
   - **Objectif** : Fournit un accès aux informations et à la configuration liées au cellulaire pour les appareils Dual SIM.
   - **Classes Clés** :
     - `CTCellularPlanProvisioning` : Permet d'ajouter ou de gérer des forfaits cellulaires (par exemple, eSIM ou SIM physique).
     - `CTTelephonyNetworkInfo` : Fournit des informations sur les forfaits cellulaires disponibles et leurs propriétés, telles que le nom de l'opérateur, le code de pays mobile (MCC) et le code de réseau mobile (MNC).
     - `CTCellularData` : Surveille l'utilisation des données cellulaires et l'état du réseau (par exemple, si les données cellulaires sont activées).
   - **Limitations** : CoreTelephony permet d'interroger et de gérer les forfaits cellulaires mais ne fournit pas de contrôle direct sur le routage du trafic spécifique d'une application vers une SIM particulière. Vous pouvez détecter quelle SIM est active pour les données, mais vous ne pouvez pas attribuer programmatiquement un trafic spécifique (par exemple, pour une application ou une destination spécifique) à une SIM au niveau de l'API.

2. **Framework NetworkExtension** :
   - **Objectif** : Permet une configuration réseau avancée, telle que la création de VPN personnalisés ou la gestion de règles de trafic réseau.
   - **Fonctionnalités Clés** :
     - **NEVPNManager** : Permet de configurer et de gérer les connexions VPN, qui peuvent être utilisées pour router le trafic via un serveur spécifique pour contourner les restrictions du GFW.
     - **NEPacketTunnelProvider** : Pour créer des tunnels VPN personnalisés, qui peuvent être configurés pour router un trafic spécifique via une SIM de Macao pour éviter les restrictions du GFW.
   - **Cas d'Usage pour le GFW** : En configurant un VPN sur la SIM de Macao (qui n'est pas soumise à la censure du GFW, car les réseaux de Macao sont indépendants), vous pouvez router le trafic via un serveur situé en dehors de la Chine continentale pour accéder à des services bloqués comme Google, WhatsApp ou YouTube.[](https://prepaid-data-sim-card.fandom.com/wiki/Macau)
   - **Limitations** : Les configurations VPN sont généralement appliquées au niveau du système, et non par SIM. Vous devriez basculer manuellement la SIM de données active ou utiliser une solution VPN personnalisée pour router le trafic de manière sélective.

3. **Configuration Dual SIM (Basée sur les Réglages)** :
   - iOS prend en charge le Dual SIM Dual Standby (DSDS) sur les iPhones compatibles (par exemple, iPhone XS, XR ou ultérieur achetés dans des régions comme Macao ou Hong Kong, qui prennent en charge le Dual SIM avec deux nano-SIM ou eSIM). Cela vous permet de :[](https://support.apple.com/en-us/109317)[](https://support.apple.com/en-us/108898)
     - Attribuer une SIM par défaut pour les données cellulaires (Réglages > Cellulaire > Données cellulaires).
     - Activer « Autoriser la commutation des données cellulaires » pour basculer automatiquement entre les SIM en fonction de la couverture ou de la disponibilité (Réglages > Cellulaire > Données cellulaires > Autoriser la commutation des données cellulaires).[](https://support.apple.com/en-us/108898)
     - Étiqueter les SIM (par exemple, « SIM Macao » pour un accès sans restriction, « China Telecom » pour les services locaux) et sélectionner manuellement quelle SIM gère les données pour des tâches spécifiques.
   - **Séparation Manuelle du Trafic** : Vous pouvez basculer manuellement la SIM de données active dans les Réglages pour diriger tout le trafic cellulaire via la SIM de Macao (pour contourner le GFW) ou la SIM de China Telecom (pour les services locaux soumis au GFW). Cependant, iOS ne fournit pas d'API pour router dynamiquement le trafic vers une SIM spécifique en fonction de l'application ou de la destination sans intervention de l'utilisateur.

4. **VPN par Application (NetworkExtension)** :
   - iOS prend en charge les configurations VPN par application via les classes `NEAppProxyProvider` ou `NEAppRule` dans le framework NetworkExtension, généralement utilisées dans des contextes d'entreprise (par exemple, Configurations d'Application Gérées).
   - **Cas d'Usage** : Vous pourriez configurer un VPN par application pour router le trafic d'applications spécifiques (par exemple, YouTube, Google) via un tunnel VPN utilisant la connexion de données de la SIM de Macao pour contourner les restrictions du GFW, tandis que d'autres applications utilisent la SIM de China Telecom pour les services locaux.
   - **Exigences** : Cela nécessite une application VPN personnalisée ou une solution d'entreprise de gestion des appareils mobiles (MDM), qui est complexe à mettre en œuvre pour les développeurs individuels. De plus, vous devriez vous assurer que la SIM de Macao est définie comme la SIM de données active lorsque le VPN est utilisé.

5. **URLSession et Réseau Personnalisé** :
   - L'API `URLSession` permet de configurer les requêtes réseau avec des interfaces cellulaires spécifiques en utilisant `allowsCellularAccess` ou en se liant à une interface réseau spécifique.
   - **Cas d'Usage** : Vous pouvez désactiver programmatiquement l'accès cellulaire pour certaines requêtes (forçant le Wi-Fi ou une autre interface) ou utiliser un VPN pour router le trafic. Cependant, lier des requêtes spécifiques à l'interface cellulaire d'une SIM particulière n'est pas directement pris en charge ; vous devriez compter sur le réglage de la SIM de données active du système.
   - **Solution de Contournement** : Combinez `URLSession` avec un VPN configuré pour utiliser les données de la SIM de Macao pour router le trafic vers des serveurs en dehors de la Chine.

### Gestion des Restrictions du GFW avec le Dual SIM

Le Grand Firewall de Chine (GFW) bloque l'accès à de nombreux sites Web et services étrangers (par exemple, Google, YouTube, WhatsApp) lors de l'utilisation d'opérateurs chinois continentaux comme China Telecom, car leur trafic est routé via l'infrastructure censurée de la Chine. En revanche, une SIM de Macao (par exemple, de CTM ou Three Macao) route le trafic via les réseaux indépendants de Macao, qui ne sont pas soumis à la censure du GFW (sauf pour China Telecom Macao, qui applique les restrictions du GFW). Voici comment vous pouvez tirer parti de cela avec une SIM de Macao et une SIM de China Telecom :[](https://www.getnomad.app/blog/do-esims-work-in-china)[](https://prepaid-data-sim-card.fandom.com/wiki/China)[](https://prepaid-data-sim-card.fandom.com/wiki/Macau)

1. **SIM de Macao pour un Accès Sans Restriction** :
   - Utilisez la SIM de Macao comme forfait de données cellulaires par défaut pour les applications ou services bloqués par le GFW (par exemple, Google, YouTube).
   - **Configuration** :
     - Allez dans Réglages > Cellulaire > Données cellulaires et sélectionnez la SIM de Macao.
     - Assurez-vous que l'itinérance des données est activée pour la SIM de Macao lorsque vous êtes en Chine continentale, car elle routera le trafic via le réseau de Macao, contournant ainsi le GFW.[](https://www.flyertalk.com/forum/china/2113715-sim-card-bypass-great-firewall.html)[](https://www.reddit.com/r/shanghai/comments/10c9fqc/can_phone_data_roaming_from_overseas_bypass_the/)
     - Optionnellement, configurez un VPN (par exemple, en utilisant `NEVPNManager`) pour sécuriser davantage le trafic, bien qu'une SIM de Macao ne nécessite généralement pas de VPN pour accéder aux services bloqués.
   - **Prise en charge de l'API** : Utilisez `CTTelephonyNetworkInfo` pour confirmer que la SIM de Macao est active pour les données (propriété `dataServiceIdentifier`) et surveiller son état.

2. **SIM de China Telecom pour les Services Locaux** :
   - Utilisez la SIM de China Telecom pour les applications et services locaux (par exemple, WeChat, Alipay) qui nécessitent un numéro de téléphone chinois ou sont optimisés pour les réseaux continentaux.
   - **Configuration** :
     - Basculez manuellement vers la SIM de China Telecom dans Réglages > Cellulaire > Données cellulaires lors de l'accès aux services locaux.
     - Soyez conscient que le trafic sur cette SIM sera soumis aux restrictions du GFW, bloquant l'accès à de nombreux sites étrangers à moins qu'un VPN ne soit utilisé.
   - **Prise en charge de l'API** : Utilisez `CTCellularData` pour surveiller l'utilisation des données cellulaires et vous assurer que la SIM correcte est active. Vous pouvez également utiliser `NEVPNManager` pour configurer un VPN pour des applications spécifiques afin de contourner le GFW sur la SIM de China Telecom, bien que la fiabilité des VPN en Chine soit inconstante en raison du blocage actif.[](https://www.flyertalk.com/forum/china/2113715-sim-card-bypass-great-firewall.html)

3. **Flux de Travail Pratique pour la Séparation du Trafic** :
   - **Basculement Manuel** : Pour plus de simplicité, basculez la SIM de données active dans les Réglages en fonction de la tâche (par exemple, SIM de Macao pour les applications internationales, SIM de China Telecom pour les applications locales). C'est l'approche la plus simple mais elle nécessite une intervention de l'utilisateur.
   - **VPN pour la SIM de China Telecom** : Si vous avez besoin d'accéder à des services bloqués tout en utilisant la SIM de China Telecom, configurez un VPN en utilisant `NEVPNManager`. Notez que de nombreux VPN (par exemple, ExpressVPN, NordVPN) peuvent être peu fiables en Chine en raison du blocage du GFW, donc testez des fournisseurs comme Astrill ou des solutions personnalisées au préalable. Certains fournisseurs d'eSIM (par exemple, Holafly, ByteSIM) proposent des VPN intégrés qui peuvent être activés pour contourner les restrictions.[](https://www.flyertalk.com/forum/china/2113715-sim-card-bypass-great-firewall.html)[](https://www.reddit.com/r/chinalife/comments/1ebjcxi/can_you_use_esims_to_get_around_the_firewall/)[](https://esim.holafly.com/internet/mobile-internet-china/)
   - **VPN par Application** : Pour une utilisation avancée, développez une application personnalisée utilisant `NEAppProxyProvider` pour router le trafic d'applications spécifiques via un VPN lorsque la SIM de China Telecom est active, tout en permettant à d'autres applications d'utiliser directement la SIM de Macao.
   - **Limitations de l'Automatisation** : iOS ne fournit pas d'API pour basculer programmatiquement la SIM de données active en fonction de l'application ou de l'URL de destination. Vous devriez compter sur un basculement de SIM initié par l'utilisateur ou sur un VPN pour gérer le routage du trafic.

### Étapes pour Mettre en Œuvre la Séparation du Trafic

1. **Configurer le Dual SIM** :
   - Assurez-vous que votre iPhone prend en charge le Dual SIM (par exemple, iPhone XS ou ultérieur avec iOS 12.1 ou ultérieur).[](https://support.apple.com/en-us/109317)
   - Insérez la SIM de Macao et la SIM de China Telecom (ou configurez un eSIM pour l'une d'elles).
   - Allez dans Réglages > Cellulaire, étiquetez les forfaits (par exemple, « Macao » et « China Telecom ») et définissez la SIM de données par défaut (par exemple, Macao pour un accès sans restriction).[](https://support.apple.com/en-us/108898)

2. **Configurer les Réglages des Données Cellulaires** :
   - Désactivez « Autoriser la commutation des données cellulaires » pour empêcher la commutation automatique des SIM, vous donnant un contrôle manuel sur la SIM utilisée pour les données (Réglages > Cellulaire > Données cellulaires > Autoriser la commutation des données cellulaires).[](https://support.apple.com/en-us/108898)
   - Utilisez `CTTelephonyNetworkInfo` pour vérifier programmatiquement quelle SIM est active pour les données dans votre application.

3. **Mettre en Œuvre un VPN pour Contourner le GFW** :
   - Pour la SIM de China Telecom, configurez un VPN en utilisant `NEVPNManager` ou une application VPN tierce (par exemple, Astrill, le VPN intégré de Holafly) pour contourner les restrictions du GFW.
   - Pour la SIM de Macao, un VPN peut ne pas être nécessaire, car son trafic est routé en dehors de l'infrastructure censurée de la Chine.[](https://prepaid-data-sim-card.fandom.com/wiki/Macau)[](https://www.reddit.com/r/shanghai/comments/10c9fqc/can_phone_data_roaming_from_overseas_bypass_the/)

4. **Surveiller et Gérer le Trafic** :
   - Utilisez `CTCellularData` pour surveiller l'utilisation des données cellulaires et vous assurer que la SIM correcte est utilisée.
   - Pour un routage avancé, explorez `NEPacketTunnelProvider` pour créer un VPN personnalisé qui route sélectivement le trafic en fonction de l'application ou de la destination, bien que cela nécessite un effort de développement important.

5. **Tester et Optimiser** :
   - Testez la connectivité en Chine continentale avec les deux SIM pour vous assurer que la SIM de Macao contourne le GFW comme prévu et que la SIM de China Telecom fonctionne pour les services locaux.
   - Vérifiez les performances du VPN sur la SIM de China Telecom, car le GFW bloque activement de nombreux protocoles VPN.[](https://www.flyerttalk.com/forum/china/2113715-sim-card-bypass-great-firewall.html)

### Limitations et Défis

- **Aucune API Native pour le Routage Dynamique des SIM** : iOS ne fournit pas d'API pour router dynamiquement le trafic vers une SIM spécifique en fonction de l'application, de l'URL ou de la destination. Vous devez basculer manuellement la SIM de données active ou utiliser un VPN pour gérer le trafic.
- **Blocage des VPN par le GFW** : Le GFW bloque activement de nombreux protocoles VPN (par exemple, IPsec, PPTP), et même les VPN basés sur SSL peuvent être limités en débit s'ils sont détectés. Une SIM de Macao est souvent plus fiable pour contourner le GFW sans VPN.[](https://www.flyertalk.com/forum/china/2113715-sim-card-bypass-great-firewall.html)
- **Restrictions de la SIM de China Telecom** : Le réseau basé sur CDMA de China Telecom peut avoir des problèmes de compatibilité avec certains téléphones étrangers, bien que son réseau LTE/5G soit plus largement compatible. De plus, son trafic est soumis à la censure du GFW, nécessitant un VPN pour les services bloqués.[](https://esim.holafly.com/sim-card/china-sim-card/)[](https://yesim.app/blog/mobile-internet-and-sim-card-in-china/)
- **Enregistrement en Nom Réel** : Les SIM de Macao et de China Telecom peuvent toutes deux nécessiter un enregistrement en nom réel (par exemple, détails du passeport), ce qui peut compliquer la configuration.[](https://prepaid-data-sim-card.fandom.com/wiki/Macau)[](https://prepaid-data-sim-card.fandom.com/wiki/China)
- **Performances** : L'itinérance sur une SIM de Macao en Chine continentale peut entraîner des vitesses plus lentes par rapport à une SIM locale de China Telecom, en particulier dans les zones rurales.[](https://www.flyertalk.com/forum/china/2113715-sim-card-bypass-great-firewall.html)

### Recommandations

- **Stratégie Principale** : Utilisez la SIM de Macao comme forfait de données cellulaires par défaut pour accéder aux services bloqués, car elle contourne naturellement le GFW en routant le trafic via les réseaux non censurés de Macao. Basculez vers la SIM de China Telecom pour les applications locales comme WeChat ou Alipay qui nécessitent un numéro chinois ou sont optimisées pour les réseaux continentaux.[](https://prepaid-data-sim-card.fandom.com/wiki/Macau)[](https://www.reddit.com/r/shanghai/comments/10c9fqc/can_phone_data_roaming_from_overseas_bypass_the/)
- **VPN comme Sauvegarde** : Pour la SIM de China Telecom, utilisez un fournisseur VPN fiable (par exemple, Astrill, ou des eSIM avec VPN intégré comme Holafly ou ByteSIM) pour accéder aux services bloqués. Pré-installez et testez le VPN avant d'entrer en Chine, car le téléchargement d'applications VPN en Chine peut être restreint.[](https://esim.holafly.com/internet/mobile-internet-china/)[](https://bytesim.com/blogs/esim/mobile-internet-china)[](https://prepaid-data-sim-card.fandom.com/wiki/China)
- **Effort de Développement** : Si vous créez une application, utilisez `NetworkExtension` pour mettre en œuvre un VPN personnalisé pour le routage sélectif du trafic, mais notez que c'est complexe et peut nécessiter des autorisations de niveau entreprise. Pour la plupart des utilisateurs, le basculement manuel des SIM combiné à un VPN est suffisant.
- **Configuration Pré-Voyage** : Achetez et activez les deux SIM (ou eSIM) avant d'arriver en Chine, car les politiques locales peuvent restreindre l'achat d'eSIM en Chine continentale. Par exemple, des fournisseurs comme Nomad ou Holafly permettent l'achat et l'activation préalables d'eSIM avec contournement intégré du GFW.[](https://www.getnomad.app/blog/do-esims-work-in-china)[](https://www.getnomad.app/blog/do-esims-work-in-china)[](https://esim.holafly.com/internet/mobile-internet-china/)

### Exemple de Code

Voici un exemple basique d'utilisation de `CTTelephonyNetworkInfo` pour vérifier le forfait cellulaire actif et de `NEVPNManager` pour configurer un VPN pour la SIM de China Telecom :

```swift
import CoreTelephony
import NetworkExtension

// Vérifier le forfait cellulaire actif
func checkActiveCellularPlan() {
    let networkInfo = CTTelephonyNetworkInfo()
    if let dataService = networkInfo.serviceCurrentRadioAccessTechnology {
        for (serviceIdentifier, rat) in dataService {
            print("Service: \(serviceIdentifier), Radio Access Technology: \(rat)")
            // Identifier quelle SIM est active (par exemple, Macao ou China Telecom)
        }
    }
}

// Configurer un VPN pour la SIM de China Telecom
func setupVPN() {
    let vpnManager = NEVPNManager.shared()
    vpnManager.loadFromPreferences { error in
        if let error = error {
            print("Failed to load VPN preferences: \(error)")
            return
        }
        
        let vpnProtocol = NEVPNProtocolIKEv2()
        vpnProtocol.serverAddress = "vpn.example.com" // Remplacez par votre serveur VPN
        vpnProtocol.remoteIdentifier = "vpn.example.com"
        vpnProtocol.authenticationMethod = .certificate // Configurez selon les besoins
        
        vpnManager.protocolConfiguration = vpnProtocol
        vpnManager.isEnabled = true
        
        vpnManager.saveToPreferences { error in
            if let error = error {
                print("Failed to save VPN preferences: \(error)")
            } else {
                print("VPN configured successfully")
            }
        }
    }
}
```

### Conclusion

Bien qu'iOS n'offre pas d'API native pour router dynamiquement le trafic vers des SIM spécifiques en fonction de l'application ou de la destination, vous pouvez réaliser une séparation du trafic en :
1. Utilisant la SIM de Macao pour un accès sans restriction afin de contourner le GFW sans VPN.
2. Utilisant la SIM de China Telecom pour les services locaux, associée à un VPN (configuré via `NEVPNManager` ou une application tierce) pour accéder aux services bloqués.
3. Basculez manuellement la SIM de données active dans les Réglages pour différentes tâches.
4. Optionnellement, développez une solution VPN personnalisée avec `NetworkExtension` pour le routage du trafic par application, bien que ce soit complexe.

Pour l'approche la plus simple, comptez sur la SIM de Macao pour les services bloqués par le GFW et basculez vers la SIM de China Telecom pour les besoins locaux, en pré-installant un VPN fiable pour cette dernière. Testez toujours les configurations avant de voyager en Chine, car les politiques du GFW et la fiabilité des VPN peuvent changer rapidement.[](https://www.flyertalk.com/forum/china/2113715-sim-card-bypass-great-firewall.html)[](https://prepaid-data-sim-card.fandom.com/wiki/China)

Si vous avez besoin de plus de précisions ou d'assistance avec des implémentations d'API spécifiques, faites-le moi savoir !