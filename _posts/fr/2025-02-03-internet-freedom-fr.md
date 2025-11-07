---
audio: false
generated: false
image: true
lang: fr
layout: post
title: Le Voyage pour Poursuivre la Liberté d'Internet
translated: true
type: post
---

### Table des matières

1. [Solutions de proxy en Chine](#proxy-solutions-in-china)
   - Utiliser une carte SIM Macao pour un accès direct
   - Recommander des fournisseurs de serveurs proxy abordables
   - Configurer les applications avec des règles de routage global
   - Éviter les configurations de serveur proxy auto-hébergées
   - Changer la région de l'App Store avec un proxy

2. [Le cheminement pour la liberté d'Internet](#the-journey-to-pursue-internet-freedom)
   - Chronologie de l'évolution des méthodes de proxy
   - Comparer la lutte contre le GFW à l'inversion de la myopie
   - La configuration actuelle utilise plusieurs serveurs proxy
   - Sélection automatique du proxy basée sur la vitesse
   - Regret de ne pas avoir appris les techniques des fournisseurs plus tôt

3. [Cartes SIM Macao](#macau-sim-cards)
   - Détails de la carte SIM China Telecom Easy+
   - Carte SIM Macao bleue prépayée
   - Différents forfaits journaliers et de données
   - Nécessite un appareil compatible 4G
   - Pas de contrat ni de frais de résiliation

4. [Problèmes de proxy Shadowsocks](#shadowsocks-proxy-issues)
   - Des problèmes de connectivité spécifiques au réseau surviennent
   - Différences de performance entre la 5G et la 4G
   - Les politiques des opérateurs peuvent bloquer le trafic proxy
   - L'emplacement du serveur affecte la latence
   - Dépannage avec différents serveurs

5. [S'inscrire sur n'importe quelle plateforme, quelle que soit l'identité](#registering-on-any-platform-regardless-of-identity)
   - Utiliser plusieurs comptes de messagerie pour l'inscription
   - Louer des numéros de téléphone via des services en ligne
   - Changer la région de l'Apple Store avec un proxy
   - Restrictions de paiement avec les cartes Visa chinoises
   - Les documents d'identité chinois aident parfois


## Solutions de proxy en Chine

*2024.12.29*

* La meilleure façon est d'obtenir une carte SIM Hong Kong/Macao pour utiliser directement les données cellulaires lorsque nécessaire. Visitez [https://www.1888.com.mo](https://www.1888.com.mo). Cela coûte environ 80 CNY pour 10 Go de données cellulaires, offrant une expérience rapide et simple.

* Les cartes SIM China Telecom Macao sont disponibles en deux types : rouges et bleues. Les cartes rouges proposent des forfaits journaliers, coûtant généralement 2, 3 ou 5 dollars de Macao par jour. Les cartes bleues offrent des forfaits de données, tels que 10 Go pour 98 dollars de Macao ou 20 Go pour 198 dollars de Macao, sans frais mensuels.

* Si vous avez besoin de plus de données réseau ou utilisez fréquemment un ordinateur portable, envisagez d'utiliser [zhs.cloud](https://zhs.cloud). Il offre l'accès à environ 15 serveurs proxy mondiaux pour seulement 30 CNY par mois.

* Sur iOS, utilisez Shadowrocket avec les règles Shadowsocks : [https://github.com/Johnshall/Shadowrocket-ADBlock-Rules-Forever](https://github.com/Johnshall/Shadowrocket-ADBlock-Rules-Forever). Configurez le routage global pour séparer le trafic chinois du trafic étranger.

* Sur Android, utilisez V2Ray. Sur Fire TV, utilisez l'application V2Ray. Sur Apple TV, utilisez l'application Shadowrocket. Sur Mac, utilisez l'application ShadowsocksX-NG ou ClashX.

* Il n'est pas recommandé de configurer un serveur proxy par vous-même. Les protocoles comme Shadowsocks, VMess ou Trojan sont facilement bloqués, quel que soit le serveur utilisé.

* Pour passer l'App Store à la région USA, activez un proxy global (USA), et l'option de paiement "Aucun" s'affichera, vous permettant de changer librement.

* Utilisez une carte Visa pour acheter des cartes cadeaux sur Amazon ou utilisez le portail de cartes cadeaux Apple pour recharger votre compte App Store.

---

## Le cheminement pour la liberté d'Internet

*2025.02.03, Ce billet a été mis à jour pour la dernière fois en août 2025.*

#### Le cheminement

De 2010 à 2013, j'ai utilisé Goagent et l'outil de proxy SwitchyOmega pour contourner le GFW.

Entre 2014 et 2015, j'ai utilisé Qujing (曲径) pour le proxy et suivi son auteur sur Twitter, qui vit maintenant au Japon.

De juin 2016 à juillet 2018, j'ai utilisé Digital Ocean pour héberger mon serveur proxy Shadowsocks.

À partir de 2019, j'ai commencé à utiliser https://zhs.cloud.

En mars 2023, j'ai commencé à utiliser une carte SIM Macao sur mon téléphone portable pour l'accès à internet sans proxy ni VPN. Cela coûtait environ 150 CNY par mois pour 20 Go de données cellulaires, et j'ai utilisé cette méthode pendant environ un an.

En 2024, j'ai recommencé à utiliser Outline Manager avec mon serveur proxy Shadowsocks, en expérimentant avec divers fournisseurs de cloud.

En février 2025, ma configuration préférée est Outline Manager avec un serveur Aliyun Hong Kong pour une utilisation quotidienne et un serveur non-Hong Kong (comme Singapour ou le Japon) pour les outils d'IA. Je maintiens la même configuration de règles de proxy que celle utilisée dans Shadowrocket ou Clash.

À partir de juin 2025, j'ai commencé à utiliser un script Python sur mon ordinateur portable pour sélectionner automatiquement un serveur proxy toutes les 10 minutes en fonction des résultats des tests de vitesse. Le script priorise les serveurs de Singapour par rapport aux serveurs de Hong Kong pour l'utilisation des outils d'IA. Pour plus de détails, veuillez consulter [Automatiser la gestion des proxy Clash](/clash-en). Pour le fournisseur de cloud VPN, j'utilisais toujours https://zhs.cloud.

De plus, sur iOS, je suis revenu à l'utilisation d'une carte SIM Macao, coûtant 150 CNY par mois pour 20 Go de données. J'ai également acheté trois fois 5 Go de données supplémentaires pour 20 MOP chacune, totalisant environ 200 CNY pour 35 Go de données sur mon téléphone portable.

À partir de mi-octobre 2025, j'ai arrêté d'utiliser mon forfait de carte SIM Macao car j'utilisais environ 35 Go par mois ces derniers mois. Cela coûterait des données cellulaires pour utiliser les applications chinoises, qui représentent environ un tiers de mon utilisation de données - principalement dans WeChat.

J'ai recommencé à utiliser l'application iOS Shadowsocks avec les serveurs proxy de https://zhs.cloud. Et j'ai commencé à acquérir des connaissances sur les câbles CN2.

#### La différence par rapport à l'inversion de ma myopie

Un défi est de combattre le GFW, qui est fait par l'homme. L'autre est de s'attaquer aux principes du fonctionnement des muscles oculaires.

Il est facile de mesurer l'efficacité d'une solution de proxy. Cependant, inverser la myopie demande du temps pour déterminer si le globe oculaire change.

#### Similarités avec l'inversion de ma myopie

Une similitude est que tant une solution de proxy que des lunettes avec une réduction de 200 degrés fonctionnent souvent bien. L'une implique l'accès à Internet, et l'autre l'amélioration de la vue. Les deux abordent des problèmes très importants.

Le principe sous-jacent est que si nous comprenons comment fonctionne le GFW et trouvons un moyen de le contourner, la solution devrait être simple.

#### Raisonnement et nuances

Je ne comprends toujours pas entièrement comment fonctionne le GFW. Lorsque l'adresse IP de mon serveur proxy est bloquée, j'ai maintenant plus de moyens d'enquêter sur la cause.

Je peux vérifier si le blocage se produit sur le réseau cellulaire ou le haut débit domestique. Si c'est le réseau cellulaire, je peux vérifier si c'est en 4G ou 5G.

De même, si ma myopie ne s'améliore pas après six mois ou un an, je dois vérifier s'il y a des différences entre mes yeux. Je dois aussi considérer si j'ai vu des choses juste à peine clairement sans forcer mes yeux pendant la majeure partie de l'année.

#### État actuel

Mon serveur proxy fonctionne actuellement très bien. Les vitesses de téléchargement sur mon téléphone atteignent 80 Mbps et les vitesses de téléversement atteignent 50 Mbps lorsque je me connecte au serveur proxy de Hong Kong. Il en va de même sur mon ordinateur portable.

J'utilise les mêmes configurations de proxy sur mon ordinateur portable et mes téléphones, et elles fonctionnent parfaitement. Normalement, j'utilise un serveur proxy pour visiter des sites en dehors de la Chine, et j'utilise un serveur non-HK pour les outils d'IA.

#### Récupération

Si les choses ne fonctionnent plus, ma méthode de récupération est simple. Il me suffit de changer l'adresse IP élastique de mon serveur proxy Aliyun Hong Kong et de télécharger la nouvelle URL du proxy sur le stockage cloud. Cela signifie que je dois exécuter deux scripts, ce qui prend environ 1 minute, et mon ordinateur portable et mes téléphones peuvent mettre à jour l'adresse du serveur proxy.

#### Regret

J'ai combattu le GFW trop souvent et pendant trop longtemps. J'ai essayé de nombreux protocoles proxy, sachant qu'ils seraient détectés par le GFW et bannis. Sans un serveur proxy fiable, il est difficile de configurer un proxy sur un routeur OpenWrt.

Une chose que je regrette est de ne pas avoir appris les techniques des fournisseurs de proxy plus tôt, comme [zhs.cloud](https://zhs.cloud). Je connais maintenant la plupart de leurs secrets.

L'autre chose est que chaque fois que mon serveur proxy était banni, je ne réfléchissais pas trop profondément. Il semblait qu'il suffisait de configurer un nouveau serveur proxy pour obtenir une nouvelle adresse IP qui n'avait pas été bannie. Mais c'était une réflexion superficielle.

#### Métriques

Je regrette de ne pas avoir utilisé Speedtest plus tôt. Je connaissais le nom de l'outil il y a longtemps, mais je n'ai pas appris à l'utiliser attentivement.

Il est bon d'utiliser Speedtest souvent lorsque vous vous connectez à des stations de signal mobile 5G ou 4G ou à un réseau haut débit domestique.

Pour inverser la myopie, c'est la même chose. J'ai acheté une échelle optométrique en forme de C et une échelle optométrique standard.

Pas de mesure, pas d'amélioration. Mesurer les choses aide à apprendre. Utiliser Speedtest souvent m'aide à constater que sur un réseau 5G, il est facile de dépasser les 100 Mbps, tandis que sur un réseau haut débit domestique, il est difficile de dépasser les 100 Mbps.

#### Il est encore tôt

Le mur du GFW tombera-t-il dans les prochaines années ? C'est difficile à dire.

Quand, après avoir inversé la myopie pendant deux ans, j'ai dit à mon ami que ma méthode d'inversion devait être améliorée et que je devais porter des lunettes avec 200 degrés de moins que ma prescription réelle au lieu de 150 degrés de moins.

Il a dit que ce n'était pas un problème, que c'était bien, pas une perte de temps, et que c'était encore tôt. Oui. Ces choses sont fondamentales. Comme la myopie, les gens devraient la découvrir plus tôt. Todd Becker a partagé cette découverte sur YouTube en 2014, et les vidéos ont cumulé plus de 1 million de vues. Et maintenant nous sommes en 2025, combien de personnes la connaissent vraiment dans le monde ? Je suppose que ce sera moins de 10 000.

---

## Cartes SIM Macao

*2023.04.20*

#### Mon expérience avec les cartes SIM Macao

Lors de ma visite de week-end à Macao en 2023, j'ai acheté une carte SIM China Telecom Easy+ Macau. Après être arrivé à Guangzhou, j'ai constaté qu'elle fonctionnait toujours parfaitement, m'aidant à apprendre l'anglais et à télécharger de nombreuses applications étrangères. J'avais l'impression d'être toujours à Macao. Je la recommande vivement. Plus tard, j'ai essayé la carte SIM Blue Macau, qui était également bonne. Voici un aperçu rapide des deux :

#### Carte SIM China Telecom Easy+

Facile à utiliser à tout moment !

### Points clés
- Pas de dépôt; activation automatique pour la Chine continentale, Macao et Hong Kong.
- Pas de contrat ni de frais de résiliation; prête à l'emploi dès l'achat.
- Numéro de Macao inclus; numéro de Chine continentale facultatif pour une utilisation à double numéro.
- Recharge en ligne ou avec des cartes de valeur.

### Options de frais journaliers
- 2 $/jour: 4GB haute vitesse, puis illimité à vitesse réduite; 5 000 minutes d'appels locaux.
- 3 $/jour: 10GB haute vitesse, puis illimité à vitesse réduite; 5 000 minutes d'appels locaux.
- 5 $/jour: 20GB haute vitesse, puis illimité à vitesse réduite; 5 000 minutes d'appels locaux.

### Suppléments
- Utilisation des données à Hong Kong: 0,1 $/MB.
- Changer de forfait à tout moment en envoyant un message texte.

#### Carte SIM Blue Macau

### Points clés
- Pas de loyer mensuel; payez à l'usage.
- Appels locaux: 0,39 MOP/minute; Internet: 0,1 MOP/MB; SMS: 1 MOP/message.
- Forfaits de données sans expiration facultatifs: 10GB pour 98 MOP, 20GB pour 188 MOP, 40GB pour 288 MOP.
- Recharge tous les 180 jours pour rester actif.

#### Appareils compatibles

- Nécessite un téléphone 4G tout réseau ou compatible China Telecom.

Pour plus d'informations, visitez [China Telecom Macau](https://www.1888.com.mo/).

---

Vous pouvez également les trouver sur Taobao:

<div align="center"><img src="/assets/images/macao/easy.jpg" width="300px" /><img/></div>

---

## Problèmes de proxy Shadowsocks

*2025.01.03*

Zhiwei :

Je suis sorti faire un barbecue avec un ami et j'ai utilisé Shadowsocks avec un serveur basé à Singapour comme proxy pour contourner le Grand Firewall (GFW). En utilisant la 5G à l'extérieur, je n'arrivais pas à me connecter, et le test expirait lorsque j'essayais d'accéder à YouTube. Cependant, lorsque je suis à la maison en utilisant la 4G ou mon réseau domestique China Telecom, Shadowsocks fonctionne bien. Pourquoi cela se produit-il ?

Mistral :

Il semble que vous rencontriez des problèmes de connectivité avec votre proxy Shadowsocks lorsque vous utilisez la 5G à l'extérieur, mais pas lorsque vous utilisez la 4G ou votre réseau domestique. Il pourrait y avoir plusieurs raisons à cela :

1. Différences de configuration réseau :
   - Réseau 5G : Le réseau 5G pourrait avoir des configurations ou des restrictions différentes par rapport à la 4G. Certains opérateurs pourraient avoir des règles de pare-feu plus strictes ou un routage réseau différent pour la 5G, ce qui pourrait affecter les performances de votre proxy Shadowsocks.
   - Réseau 4G : Le réseau 4G pourrait avoir des paramètres plus souples ou un meilleur routage qui permet à votre proxy Shadowsocks de fonctionner correctement.

2. Restrictions du FAI :
   - Politiques des opérateurs : Différents opérateurs pourraient avoir des politiques différentes concernant l'utilisation des VPN ou des proxys. Votre opérateur 5G pourrait avoir des politiques plus strictes qui bloquent ou limitent le trafic VPN, y compris Shadowsocks.
   - Réseau domestique : Votre réseau domestique, fourni par China Telecom, pourrait avoir moins de restrictions, permettant à Shadowsocks de fonctionner sans problème.

3. Force et stabilité du signal :
   - Signal 5G : La stabilité et la force du signal 5G peuvent varier, surtout dans les environnements extérieurs. Des signaux faibles ou instables peuvent provoquer des problèmes de connectivité, y compris des délais d'attente.
   - Signal 4G : Le signal 4G pourrait être plus stable et cohérent, offrant une meilleure connexion pour votre proxy Shadowsocks.

4. Emplacement du serveur proxy :
   - Serveur de Singapour : L'emplacement de votre serveur Shadowsocks à Singapour pourrait affecter la latence et la connectivité. Le réseau 5G pourrait avoir une latence plus élevée ou un routage moins optimal vers le serveur de Singapour par rapport au réseau 4G ou à votre réseau domestique.

5. Paramètres de l'appareil :
   - Configuration : Assurez-vous que les paramètres de votre appareil sont correctement configurés pour l'utilisation de Shadowsocks. Parfois, le changement de réseau (de 5G à 4G ou Wi-Fi domestique) peut entraîner la réinitialisation ou la modification des paramètres.
   - Autorisations de l'application : Assurez-vous que l'application Shadowsocks dispose des autorisations nécessaires pour fonctionner sur différents réseaux.

### Étapes de dépannage :

1. Vérifier les paramètres réseau :
   - Assurez-vous que vos paramètres Shadowsocks sont correctement configurés pour les réseaux 5G et 4G.
   - Vérifiez qu'il n'y a pas de restrictions ou de paramètres spécifiques sur votre réseau 5G qui pourraient bloquer le proxy.

2. Tester différents serveurs :
   - Essayez de vous connecter à différents serveurs Shadowsocks pour voir si le problème est spécifique au serveur de Singapour.
   - Vérifiez la latence et la stabilité de la connexion au serveur.

3. Contacter votre opérateur :
   - Si le problème persiste, contactez votre opérateur 5G pour vous renseigner sur d'éventuelles restrictions ou paramètres qui pourraient affecter votre connexion Shadowsocks.

4. Mettre à jour le logiciel :
   - Assurez-vous que votre application Shadowsocks et le logiciel de votre appareil sont à jour. Parfois, les mises à jour peuvent résoudre les problèmes de connectivité.

5. Utiliser des proxys alternatifs :
   - Envisagez d'utiliser des services proxy ou des VPN alternatifs qui pourraient avoir une meilleure compatibilité avec votre réseau 5G.

En vérifiant systématiquement ces facteurs, vous devriez pouvoir identifier la cause du problème de connectivité et trouver une solution appropriée.

--

Mise à jour :

En fait, mon Wi-Fi domestique utilise China Mobile Communications Corporation, et son adresse est du type 120.235.8.xx.

Curieusement, j'ai observé des schémas de connectivité incohérents - alors que mon serveur proxy fonctionne normalement sur les données cellulaires et les réseaux China Telecom, il ne parvient parfois pas à se connecter lorsque j'utilise mon réseau Wi-Fi domestique.

---

## S'inscrire sur n'importe quelle plateforme, quelle que soit l'identité

Je suis un citoyen chinois et un ingénieur logiciel axé sur les dernières technologies. Il est frustrant de voir de nombreux produits interdire l'accès depuis la Chine. Bien que je sois toujours en train de faire mon diplôme d'associé et que j'espère travailler en dehors de la Chine un jour, je resterai en Chine pendant encore quelques années. En attendant, j'aimerais partager quelques informations sur la façon de surmonter les barrières d'Internet basées sur la nationalité.

#### E-mail

Avoir plusieurs comptes de messagerie est préférable. Claude a bloqué mon Gmail en raison de l'accès VPN, j'ai donc enregistré un nouveau compte Outlook et cela a fonctionné correctement.

#### Numéro de téléphone

Via [http://sms-activate.org](http://sms-activate.org), il est possible de louer un numéro de téléphone pour l'inscription. Cependant, le problème est que les comptes enregistrés avec de tels numéros de téléphone peuvent présenter certains risques.

En Chine, je recommande personnellement [https://www.1888.com.mo](https://www.1888.com.mo) pour une carte China Telecom Macau. J'ai également essayé la carte SIM Giffgaff UK et j'ai récemment commandé une carte SIM PayGo T-Mobile USA.

#### Région de l'Apple Store

Pour passer l'App Store en région États-Unis, activez un proxy global (États-Unis), et l'option de paiement "Aucun" s'affichera, vous permettant de changer librement.

Vous pouvez utiliser une carte Visa pour acheter des cartes cadeaux sur Amazon ou utiliser le portail de cartes cadeaux Apple pour alimenter votre compte App Store.

La même méthode s'applique à Singapour ou à d'autres régions.

#### Paiement

Avoir une carte Visa est pratique. Cependant, les cartes Visa émises par la Chine ont encore certaines restrictions. Par exemple, Anthropic ou OpenAI n'acceptent pas les cartes Visa émises en Chine.

#### VPN

Vous voudrez peut-être consulter [Solutions de proxy en Chine](./proxy-en) et [Configurer votre serveur proxy](./diy-proxy-en).

#### Identité

J'ai une carte d'identité civique et un passeport chinois, ce qui peut être utile dans certaines situations.