---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Analyse du Fichier de Configuration Shadowrocket
translated: true
type: note
---

Ceci semble être un fichier de configuration pour Shadowrocket, une application de proxy basée sur des règles pour iOS (similaire à des outils comme Surge ou Quantumult). Il est structuré comme un fichier de configuration textuel qui définit comment l'application route le trafic, gère le DNS, applique des règles et effectue des réécritures ou des interceptions MITM (man-in-the-middle). Le fichier est daté du "2025-10-02 20:25:43", ce qui pourrait être un horodatage ou un espace réservé.

Je vais l'expliquer section par section, en détaillant chaque partie, sa fonction et la raison pour laquelle elle pourrait être configurée de cette manière. Cette configuration semble optimisée pour les utilisateurs dans des régions avec des restrictions internet (par exemple, la Chine), routant certains services globaux/bloqués via un serveur proxy tout en gardant le trafic local/domestique direct pour une meilleure vitesse et pour éviter une redirection inutile. Ce n'est pas une configuration complète—vous devriez toujours configurer un serveur proxy (par exemple, via Shadowsocks, V2Ray, etc.) séparément dans l'application, et cette configuration référence des ensembles de règles externes qui se mettent à jour automatiquement depuis GitHub.

### Hypothèses et Notes Clés
- **Configuration du Proxy** : Cette configuration suppose que vous avez un serveur proxy fonctionnel configuré dans Shadowrocket (par exemple, SOCKS5, HTTP, ou des protocoles chiffrés). Sans cela, les règles "PROXY" ne fonctionneront pas.
- **Objectif** : Elle semble destinée à contourner la censure (par exemple, le Grand Firewall en Chine). Les services d'IA (comme OpenAI/ChatGPT) sont proxifiés, tandis que les domaines/IP chinois passent directement pour éviter la limitation de débit.
- **Mode TUN** : Des références à "tun" (mode tunnel) pour router tout le trafic via l'appareil.
- **Dépendances Externes** : Certaines règles se chargent depuis des URLs GitHub (par exemple, des listes de règles). Assurez-vous de faire confiance à ces sources, car elles peuvent se mettre à jour automatiquement.
- Si quelque chose n'est pas clair ou si vous avez besoin d'aide pour l'appliquer, faites-moi part des détails de votre configuration.

### Découpage par Section

#### **[General]**
Ceci définit les comportements globaux de l'application, la résolution DNS et le routage du réseau. C'est comme les "préférences" ou "paramètres système" pour Shadowrocket.

- `bypass-system = true` : Ignorer les paramètres de proxy système d'iOS. Shadowrocket gère tout le proxying lui-même au lieu de s'appuyer sur les configurations système.
  
- `skip-proxy = 192.168.0.0/16,10.0.0.0/8,172.16.0.0/12,localhost,*.local,captive.apple.com,*.ccb.com,*.abchina.com.cn,*.psbc.com,www.baidu.com` : Une liste séparée par des virgules des domaines/plages d'IP à **toujours router directement** (sans proxy). Cela inclut :
  - Les réseaux privés (par exemple, les IP Wi-Fi domestiques comme 192.168.x.x).
  - Les domaines locaux (*.local) et localhost.
  - La vérification du portail captif d'Apple.
  - Les domaines de banques chinoises (*.ccb.com pour China Construction Bank, *.abchina.com.cn pour Agricultural Bank of China, *.psbc.com pour Postal Savings Bank).
  - Baidu (www.baidu.com), un moteur de recherche chinois majeur.
  - *Pourquoi ?* Les sites chinois domestiques (surtout les banques et la recherche) sont accessibles sans proxy et pourraient être limités ou signalés s'ils sont routés via un proxy.

- `tun-excluded-routes = 10.0.0.0/8, 100.64.0.0/10, 127.0.0.0/8, 169.254.0.0/16, 172.16.0.0/12, 192.0.0.0/24, 192.0.2.0/24, 192.88.99.0/24, 192.168.0.0/16, 198.51.100.0/24, 203.0.113.0/24, 224.0.0.0/4, 255.255.255.255/32, 239.255.255.250/32` : En mode tunnel (TUN), ces plages d'IP sont **exclues** du tunnel proxy. Cela évite les interférences avec le trafic local/de routage comme les IP de bouclage, le multicast et les plages de test.

- `dns-server = https://doh.pub/dns-query,https://dns.alidns.com/dns-query,223.5.5.5,119.29.29.29` : Liste prioritaire des résolveurs DNS pour le trafic proxy. Ce sont des serveurs DoH (DNS over HTTPS) et du DNS simple (Tencent's 119.29.29.29 et Aliyun's 223.5.5.5). Cela commence par des serveurs chiffrés/publics (doh.pub et alidns.com) pour la confidentialité/la sécurité.

- `fallback-dns-server = system` : Si le DNS principal échoue, revenir au DNS système d'iOS.

- `ipv6 = true` : Activer le support IPv6. `prefer-ipv6 = false` : Préférer IPv4 à IPv6 pour les connexions (par exemple, pour la stabilité ou la compatibilité).

- `dns-direct-system = false` : Ne pas utiliser le DNS système pour les connexions directes—utiliser le DNS configuré à la place.

- `icmp-auto-reply = true` : Répondre automatiquement aux requêtes ICMP (ping). Utile pour les vérifications de connectivité.

- `always-reject-url-rewrite = false` : Permettre le déclenchement des réécritures d'URL (utilisées plus loin dans la configuration).

- `private-ip-answer = true` : Autoriser les réponses DNS avec des IP privées (par exemple, votre routeur).

- `dns-direct-fallback-proxy = true` : Si une requête DNS directe échoue, réessayer via le proxy.

- `tun-included-routes = ` : (Vide) Aucun route personnalisée incluse en mode TUN—utiliser les valeurs par défaut.

- `always-real-ip = ` : (Vide) Aucune exposition forcée de l'IP réelle—comportement standard.

- `hijack-dns = 8.8.8.8:53,8.8.4.4:53` : Intercepter le trafic DNS du DNS public de Google (8.8.8.8/8.8.4.4 sur le port 53) et le router via le proxy. Cela utilise forcément votre DNS configuré au lieu des DNS publics, qui pourraient être bloqués ou surveillés.

- `udp-policy-not-supported-behaviour = REJECT` : Si le trafic UDP n'est pas supporté par une politique, le rejeter au lieu de l'autoriser.

- `include = ` : (Vide) Aucun fichier de configuration supplémentaire inclus.

- `update-url = ` : (Vide) Aucune mise à jour automatique de la configuration depuis une URL.

#### **[Rule]**
Ceci définit les règles de routage du trafic, traitées dans l'ordre. C'est comme une ACL (liste de contrôle d'accès) indiquant à Shadowrocket quoi proxyfier, quoi envoyer directement, en fonction des domaines, mots-clés, GEOIP, etc. Si aucune règle ne correspond, cela passe à `FINAL,DIRECT`.

- `DOMAIN-SUFFIX,anthropic.com,PROXY` : Router tous les sous-domaines de anthropic.com via le proxy (par exemple, api.anthropic.com). Anthropic est une entreprise d'IA—probablement pour contourner les blocs.

- `DOMAIN-SUFFIX,chatgpt.com,PROXY` : Router les domaines ChatGPT via le proxy. ChatGPT est souvent restreint dans certaines régions.

- `DOMAIN-SUFFIX,openai.com,PROXY` : Router les domaines OpenAI via le proxy (raison similaire).

- `DOMAIN-SUFFIX,googleapis.com,PROXY` : Router les services API de Google via le proxy (peut être pour accéder indirectement aux services Google).

- `DOMAIN-SUFFIX,zhs.futbol,DIRECT` : Router ce domaine spécifique (probablement un site sportif en espagnol/chinois) directement.

- `RULE-SET,https://github.com/lzwjava/lzwjava.github.io/raw/refs/heads/main/scripts/auto-ss-config/AI.list,PROXY` : Charger un ensemble de règles externe depuis GitHub (une liste de domaines liés à l'IA) et les proxyfier. Cela met à jour et étend automatiquement les règles de proxy pour l'IA.

- `RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Lan/Lan.list,DIRECT` : Charger un ensemble de règles pour le réseau local (LAN) et les router directement. Évite de proxyfier le trafic domestique/interne.

- `DOMAIN-KEYWORD,cn,DIRECT` : Tout domaine contenant le mot-clé "cn" (par exemple, n'importe quoi.cn) passe directement. Utile pour les sites chinois.

- `GEOIP,CN,DIRECT` : Toute IP géolocalisée en Chine (CN) passe directement. Empêche de proxyfier le trafic domestique, qui est rapide et sans restriction.

- `FINAL,DIRECT` : Action par défaut—si aucune règle ne correspond, router directement. Garde la plupart du trafic non proxyfié pour l'efficacité.

*Effet Global* : Il s'agit d'une configuration "proxy pour les globaux bloqués". Le trafic IA/ChatGPT/OpenAI est forcé via le VPN/proxy pour contourner les restrictions régionales, tandis que les éléments chinois/locaux restent directs.

#### **[Host]**
Mappages manuels des hôtes (comme un fichier hosts local).

- `localhost = 127.0.0.1` : Mapper "localhost" vers l'IP de bouclage. Standard—assure que l'application peut se connecter aux services locaux.

#### **[URL Rewrite]**
Réécrit les URLs entrantes avant que les requêtes ne soient faites. Utilise la correspondance par regex.

- `^https?://(www.)?g.cn https://www.google.com 302` : Réécrire toute URL HTTP/HTTPS pour g.cn (ou www.g.cn) pour rediriger vers google.com avec un statut 302 (redirection temporaire). g.cn est le domaine chinois de Google—cela le contourne.

- `^https?://(www.)?google.cn https://www.google.com 302` : Idem pour google.cn vers google.com. La Chine bloque ou redirige souvent google.com, donc cela force une redirection propre.

*Pourquoi ?* Dans les régions censurées, google.cn peut servir des résultats altérés/interdits. Cela garantit d'atteindre directement le site Google global.

#### **[MITM]**
Paramètres Man-in-the-middle pour intercepter et modifier le trafic HTTPS (nécessite un certificat d'autorité de certification racine dans Shadowrocket).

- `hostname = *.google.cn` : Intercepter le trafic pour tout sous-domaine de google.cn. Combiné avec la réécriture d'URL, cela peut déchiffrer/rediriger le trafic pour les domaines Google CN.

*Pourquoi ?* Cela pourrait être pour appliquer les réécritures ou gérer les problèmes d'épinglage de certificat en Chine, où google.cn utilise des certificats différents.

### Comment Utiliser Cette Configuration
1. **Importer** : Dans Shadowrocket, importer ceci en tant que fichier de configuration.
2. **Serveur Proxy** : Ajouter votre proxy réel (par exemple, serveur Shadowsocks) dans la section "Servers"—les règles comme "PROXY" en dépendent.
3. **Activer** : Basculer vers cette configuration et activer le mode tunnel (VPN) si nécessaire.
4. **Certificat CA** : Pour MITM, installer et approuver le CA de Shadowrocket si ce n'est pas déjà fait.
5. **Tester** : Vérifier des sites comme whatismyipaddress.com pour voir si les IP/le routage fonctionnent comme prévu. Surveiller les sites chinois lents.
6. **Dépannage** : Si les ensembles de règles échouent à charger, ils pourraient être limités en taux ou modifiés. Les préférences IPv6 pourraient nécessiter d'être basculées pour la connectivité.

### Problèmes Potentiels / Notes de Sécurité
- **Confidentialité** : Les ensembles de règles exposés (liens GitHub) pourraient révéler ce que vous routez. MITM peut intercepter le trafic sensible—n'utiliser que des CA de confiance.
- **Mises à jour** : Les ensembles de règles se chargent automatiquement ; si GitHub est bloqué, utiliser un proxy pour eux.
- **Date Future** : La configuration est datée d'octobre 2025—cela pourrait être une faute de frappe ou une préparation pour l'avenir, mais aucune fonctionnalité n'en dépend.
- **Légalité** : Le proxying pour contourner la censure est acceptable dans certains endroits mais restreint dans d'autres—utiliser à vos risques et périls.
- Si vous partagez les journaux d'erreurs ou ce que vous essayez d'accomplir, je peux affiner les conseils !