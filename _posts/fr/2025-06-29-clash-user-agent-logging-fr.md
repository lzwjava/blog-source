---
audio: false
generated: true
lang: fr
layout: post
title: Journaliser l'User-Agent dans le proxy Clash
translated: true
type: note
---

Il semble que vous fassiez référence à **Clash**, un utilitaire de proxy basé sur des règles, et que vous souhaitiez le configurer pour afficher ou enregistrer dans les logs l'**User-Agent** de ses requêtes HTTP. D'après les informations disponibles, Clash (ou son cœur, souvent appelé `clash-core`) ne dispose pas d'une fonctionnalité intégrée pour afficher directement l'User-Agent des requêtes sortantes de manière simple. Cependant, vous pouvez y parvenir en utilisant les options de configuration de Clash, des outils externes ou des méthodes de débogage. Voici un guide étape par étape pour vous aider à enregistrer ou inspecter l'User-Agent des requêtes passant par Clash.

---

### Comprendre le Contexte
- **Clash** est un utilitaire de proxy qui achemine le trafic en fonction de règles et prend en charge des protocoles comme HTTP, SOCKS5, Shadowsocks, V2Ray, et plus encore. Il opère aux couches réseau et application.
- L'**User-Agent** est un en-tête HTTP généralement défini par l'application cliente (par exemple, un navigateur ou un outil comme `curl`) qui effectue la requête, et non par Clash lui-même. Clash, en tant que proxy, transfère ces requêtes et peut ne pas enregistrer ou modifier l'User-Agent par défaut, sauf s'il est configuré explicitement pour le faire.
- Pour afficher l'User-Agent, vous devez soit :
  1. Configurer Clash pour enregistrer les en-têtes HTTP (y compris l'User-Agent) à des fins de débogage.
  2. Utiliser un outil externe (par exemple, un proxy de débogage ou un analyseur de réseau) pour inspecter les requêtes.
  3. Modifier la configuration de Clash pour ajouter des en-têtes personnalisés ou utiliser un script pour les enregistrer.

Étant donné que Clash lui-même ne dispose pas d'une configuration directe pour enregistrer les en-têtes User-Agent, vous devrez peut-être combiner Clash avec d'autres outils ou utiliser des configurations spécifiques. Voici les méthodes pour y parvenir.

---

### Méthode 1 : Activer la journalisation détaillée dans Clash et inspecter les logs
Clash peut enregistrer les requêtes à différents niveaux, mais il n'enregistre pas nativement les en-têtes HTTP comme l'User-Agent, sauf s'il est configuré explicitement ou utilisé avec un outil capable d'inspecter le trafic. Vous pouvez activer la journalisation détaillée et utiliser un outil pour capturer l'User-Agent.

#### Étapes :
1. **Définir le niveau de log de Clash sur Debug** :
   - Modifiez votre fichier de configuration Clash (`config.yaml`, généralement situé dans `~/.config/clash/config.yaml` ou un répertoire personnalisé spécifié avec l'indicateur `-d`).
   - Définissez `log-level` sur `debug` pour capturer des informations détaillées sur les requêtes :
     ```yaml
     log-level: debug
     ```
   - Enregistrez la configuration et redémarrez Clash :
     ```bash
     clash -d ~/.config/clash
     ```
   - Clash enregistrera maintenant des informations plus détaillées sur `STDOUT` ou dans un fichier de log spécifié. Cependant, cela peut ne pas inclure directement l'en-tête User-Agent, car Clash se concentre sur le routage et les détails de connexion.

2. **Inspecter les logs** :
   - Vérifiez la sortie des logs dans le terminal ou le fichier de log (s'il est configuré). Recherchez les détails des requêtes HTTP, mais notez que la journalisation par défaut de Clash peut ne pas inclure les en-têtes HTTP complets comme l'User-Agent.
   - Si vous ne voyez pas d'informations sur l'User-Agent, passez à l'utilisation d'un proxy de débogage (voir Méthode 2) ou d'un analyseur de réseau (Méthode 3).

3. **Optionnel : Utiliser le Tableau de bord Clash** :
   - Clash fournit un tableau de bord web (par exemple, YACD à `https://yacd.haishan.me/` ou le tableau de bord officiel à `https://clash.razord.top/`) pour surveiller les connexions et les logs.
   - Configurez `external-controller` et `external-ui` dans votre `config.yaml` pour activer le tableau de bord :
     ```yaml
     external-controller: 127.0.0.1:9090
     external-ui: folder
     ```
   - Accédez au tableau de bord via `http://127.0.0.1:9090/ui` et vérifiez l'onglet "Logs" ou "Connections". Cela peut afficher les détails de connexion mais est peu susceptible d'afficher directement l'User-Agent.

#### Limitations :
- Les logs de débogage de Clash se concentrent sur les décisions de routage et de proxy, et non sur les en-têtes HTTP complets. Pour capturer l'User-Agent, vous devez intercepter le trafic HTTP, ce qui nécessite des outils supplémentaires.

---

### Méthode 2 : Utiliser un proxy de débogage pour capturer l'User-Agent
Étant donné que Clash lui-même n'enregistre pas directement les en-têtes HTTP comme l'User-Agent, vous pouvez acheminer le trafic de Clash via un proxy de débogage comme **mitmproxy**, **Charles Proxy** ou **Fiddler**. Ces outils peuvent intercepter et afficher la requête HTTP complète, y compris l'User-Agent.

#### Étapes :
1. **Installer mitmproxy** :
   - Installez `mitmproxy`, un outil open-source populaire pour intercepter le trafic HTTP/HTTPS :
     ```bash
     sudo apt install mitmproxy  # Sur Debian/Ubuntu
     brew install mitmproxy      # Sur macOS
     ```
   - Alternativement, utilisez un autre outil proxy comme Charles ou Fiddler.

2. **Configurer Clash pour acheminer le trafic via mitmproxy** :
   - Par défaut, Clash agit comme un proxy HTTP/SOCKS5. Vous pouvez le chaîner à `mitmproxy` en définissant `mitmproxy` comme proxy en amont.
   - Modifiez votre `config.yaml` de Clash pour inclure un proxy HTTP pointant vers `mitmproxy` :
     ```yaml
     proxies:
       - name: mitmproxy
         type: http
         server: 127.0.0.1
         port: 8080  # Port par défaut de mitmproxy
     proxy-groups:
       - name: Proxy
         type: select
         proxies:
           - mitmproxy
     ```
   - Enregistrez la configuration et redémarrez Clash.

3. **Démarrer mitmproxy** :
   - Exécutez `mitmproxy` pour écouter sur le port 8080 :
     ```bash
     mitmproxy
     ```
   - `mitmproxy` affichera toutes les requêtes HTTP qui passent par lui, y compris l'en-tête User-Agent.

4. **Envoyer une requête de test** :
   - Utilisez un client (par exemple, `curl`, un navigateur ou un autre outil) configuré pour utiliser Clash comme proxy.
   - Exemple avec `curl` :
     ```bash
     curl --proxy http://127.0.0.1:7890 http://example.com
     ```
   - Dans `mitmproxy`, vous verrez la requête HTTP complète, y compris l'User-Agent (par exemple, `curl/8.0.1` ou l'User-Agent du navigateur).

5. **Inspecter l'User-Agent** :
   - Dans l'interface `mitmproxy`, naviguez parmi les requêtes capturées. L'en-tête User-Agent sera visible dans les détails de la requête.
   - Vous pouvez également enregistrer les logs dans un fichier pour une analyse ultérieure :
     ```bash
     mitmproxy -w mitmproxy.log
     ```

#### Notes :
- Si vous utilisez HTTPS, vous devez installer et approuver le certificat CA de `mitmproxy` sur votre appareil client pour déchiffrer le trafic HTTPS. Suivez les instructions sur `http://mitm.clash/cert.crt` ou la documentation de `mitmproxy`.
- Cette méthode nécessite de chaîner les proxys (Client → Clash → mitmproxy → Destination), ce qui peut légèrement augmenter la latence mais permet une inspection complète des en-têtes.

---

### Méthode 3 : Utiliser un analyseur de réseau pour capturer l'User-Agent
Si vous préférez ne pas chaîner les proxys, vous pouvez utiliser un analyseur de réseau comme **Wireshark** pour capturer et inspecter le trafic HTTP passant par Clash.

#### Étapes :
1. **Installer Wireshark** :
   - Téléchargez et installez Wireshark depuis [wireshark.org](https://www.wireshark.org/).
   - Sur Linux :
     ```bash
     sudo apt install wireshark
     ```
   - Sur macOS :
     ```bash
     brew install wireshark
     ```

2. **Démarrer Clash** :
   - Assurez-vous que Clash fonctionne avec votre configuration souhaitée (par exemple, proxy HTTP sur le port 7890) :
     ```bash
     clash -d ~/.config/clash
     ```

3. **Capturer le trafic dans Wireshark** :
   - Ouvrez Wireshark et sélectionnez l'interface réseau que Clash utilise (par exemple, `eth0`, `wlan0` ou `lo` pour le trafic localhost).
   - Appliquez un filtre pour capturer le trafic HTTP :
     ```
     http
     ```
   - Alternativement, filtrez par le port du proxy HTTP de Clash (par exemple, 7890) :
     ```
     tcp.port == 7890
     ```

4. **Envoyer une requête de test** :
   - Utilisez un client configuré pour utiliser Clash comme proxy :
     ```bash
     curl --proxy http://127.0.0.1:7890 http://example.com
     ```

5. **Inspecter l'User-Agent** :
   - Dans Wireshark, recherchez les requêtes HTTP (par exemple, `GET / HTTP/1.1`). Double-cliquez sur un paquet pour voir ses détails.
   - Développez la section "Hypertext Transfer Protocol" pour trouver l'en-tête `User-Agent` (par exemple, `User-Agent: curl/8.0.1`).

#### Notes :
- Pour le trafic HTTPS, Wireshark ne peut pas déchiffrer l'User-Agent à moins que vous n'ayez la clé privée du serveur ou que vous n'utilisiez un outil comme `mitmproxy` pour déchiffrer le trafic.
- Cette méthode est plus complexe et nécessite une familiarité avec l'analyse des paquets réseau.

---

### Méthode 4 : Modifier la configuration de Clash pour injecter ou enregistrer des en-têtes personnalisés
Clash prend en charge les en-têtes HTTP personnalisés dans sa configuration pour certains types de proxy (par exemple, HTTP ou VMess). Vous pouvez configurer Clash pour injecter un User-Agent spécifique ou utiliser un script pour enregistrer les en-têtes. Cependant, cela est moins direct pour enregistrer l'User-Agent de toutes les requêtes.

#### Étapes :
1. **Ajouter un en-tête User-Agent personnalisé** :
   - Si vous souhaitez forcer un User-Agent spécifique pour les tests, modifiez la section `proxies` dans `config.yaml` pour inclure un en-tête personnalisé :
     ```yaml
     proxies:
       - name: my-http-proxy
         type: http
         server: proxy.example.com
         port: 8080
         header:
           User-Agent:
             - "MyCustomUserAgent/1.0"
     ```
   - Cela définit un User-Agent personnalisé pour les requêtes envoyées via ce proxy. Cependant, il remplace l'User-Agent original du client, ce qui n'est peut-être pas ce que vous voulez si vous essayez d'enregistrer l'User-Agent du client.

2. **Utiliser des règles de script pour enregistrer les en-têtes** :
   - Clash prend en charge les règles basées sur des scripts utilisant des moteurs comme `expr` ou `starlark` (). Vous pouvez écrire un script pour enregistrer ou traiter les en-têtes, y compris l'User-Agent.[](https://pkg.go.dev/github.com/yaling888/clash)
   - Exemple de configuration :
     ```yaml
     script:
       engine: starlark
       code: |
         def match(req):
           print("User-Agent:", req.headers["User-Agent"])
           return "Proxy"  # Achemine vers un groupe de proxy
     ```
   - Cela nécessite d'écrire un script personnalisé, ce qui est avancé et peut ne pas être entièrement pris en charge dans toutes les versions de Clash. Vérifiez la documentation de Clash pour le support des scripts.

3. **Vérifier avec mitmproxy ou Wireshark** :
   - Après avoir injecté un User-Agent personnalisé, utilisez la Méthode 2 ou la Méthode 3 pour confirmer que l'User-Agent est envoyé comme prévu.

#### Limitations :
- L'injection d'un User-Agent personnalisé remplace l'User-Agent du client, donc cela n'est utile que pour tester des User-Agents spécifiques.
- L'enregistrement basé sur des scripts est expérimental et peut ne pas être disponible dans toutes les versions de Clash.

---

### Méthode 5 : Utiliser le proxy MITM de Clash pour enregistrer les en-têtes
Clash prend en charge un mode proxy **Man-in-the-Middle (MITM)** qui peut intercepter et enregistrer le trafic HTTPS, y compris les en-têtes comme l'User-Agent.

#### Étapes :
1. **Activer MITM dans Clash** :
   - Modifiez `config.yaml` pour activer le proxy MITM :
     ```yaml
     mitm-port: 7894
     mitm:
       hosts:
         - "*.example.com"
     ```
   - Cela configure Clash pour intercepter le trafic HTTPS pour les domaines spécifiés.

2. **Installer le certificat CA de Clash** :
   - Clash génère un certificat CA pour MITM. Accédez à `http://mitm.clash/cert.crt` dans un navigateur pour le télécharger et l'installer.
   - Approuvez le certificat sur votre appareil client pour permettre à Clash de déchiffrer le trafic HTTPS.

3. **Inspecter les logs** :
   - Avec MITM activé, Clash peut enregistrer des informations de requête plus détaillées, y compris les en-têtes. Vérifiez les logs dans le terminal ou le tableau de bord.
   - Si les en-têtes ne sont pas enregistrés, utilisez `mitmproxy` (Méthode 2) pour capturer le trafic déchiffré.

#### Notes :
- Le mode MITM nécessite d'approuver le certificat CA sur tous les appareils clients, ce qui peut ne pas être pratique dans tous les cas d'utilisation.
- Cette méthode est meilleure pour le trafic HTTPS mais nécessite une configuration supplémentaire.

---

### Recommandations
- **Méthode préférée** : Utilisez la **Méthode 2 (mitmproxy)** pour la façon la plus simple et la plus fiable de capturer et d'enregistrer l'User-Agent des requêtes. C'est open-source, largement supporté et conçu pour le débogage HTTP.
- **Alternative** : Utilisez la **Méthode 3 (Wireshark)** si vous êtes à l'aise avec l'analyse des paquets réseau et ne souhaitez pas chaîner les proxys.
- **Pour les utilisateurs avancés** : Expérimentez avec la **Méthode 4 (En-têtes personnalisés ou Scripts)** si vous avez besoin de manipuler ou d'enregistrer programmatiquement les en-têtes dans Clash.

---

### Notes supplémentaires
- **Documentation de Clash** : Reportez-vous à la documentation officielle de Clash (,) pour les détails de configuration. Le dépôt GitHub (`https://github.com/Dreamacro/clash`) et le wiki (`https://en.clash.wiki`) fournissent des conseils détaillés.[](https://en.clash.wiki/)[](https://en.clash.wiki/configuration/getting-started.html)
- **User-Agent côté client** : L'User-Agent est défini par le client (par exemple, le navigateur, `curl` ou l'application), et non par Clash. Assurez-vous que votre client envoie l'User-Agent attendu. Par exemple :
  - `curl` utilise `curl/<version>` par défaut.
  - Les navigateurs utilisent leurs propres chaînes User-Agent (par exemple, `Mozilla/5.0 ...`).
- **Tests** : Testez toujours avec une requête HTTP simple (par exemple, `curl --proxy http://127.0.0.1:7890 http://example.com`) pour vérifier la configuration.
- **Sécurité** : Lorsque vous utilisez MITM ou des proxys de débogage, assurez-vous d'approuver les certificats CA et les outils pour éviter les risques de sécurité.

Si vous avez besoin de précisions ou d'assistance avec des configurations spécifiques, veuillez fournir plus de détails sur votre configuration (par exemple, version de Clash, système d'exploitation ou type de proxy spécifique), et je pourrai adapter les instructions davantage !