---
audio: false
generated: false
image: false
lang: fr
layout: post
title: Le Voyage vers la Quête de la Liberté sur Internet
translated: true
---

### Table des matières

1. [Solutions de proxy en Chine](#solutions-de-proxy-en-chine)
   - Cartes SIM de Macao (Meilleure option)
   - Recommandations de serveurs proxy
   - Configuration et installation des applications
   - Paiements et paramètres régionaux

2. [Le parcours vers la liberté sur Internet](#le-parcours-vers-la-liberté-sur-internet)
   - Chronologie des méthodes de proxy (2010-2025)
   - Comparaison entre liberté sur Internet et solutions contre la myopie
   - Configuration actuelle et performances
   - Méthodes de récupération et leçons apprises

3. [Cartes SIM de Macao](#cartes-sim-de-macao)
   - Détails de la carte SIM China Telecom Easy+
   - Options de cartes SIM Blue Macau
   - Tarifs et forfaits de données
   - Compatibilité des appareils

4. [Problèmes de proxy Shadowsocks](#problèmes-de-proxy-shadowsocks)
   - Problèmes de connectivité spécifiques au réseau
   - Différences de performance entre 5G et 4G
   - Étapes de dépannage et solutions
   - Impact des politiques des FAI et opérateurs

---

## Solutions de proxy en Chine

*29.12.2024*

* La meilleure solution consiste à obtenir une carte SIM de Macao (Chine) pour utiliser directement les données mobiles lorsque nécessaire. Visitez [https://www.1888.com.mo](https://www.1888.com.mo). Cela coûte environ 80 CNY pour 10 Go de données mobiles, offrant une expérience rapide et sans tracas.

* Les cartes SIM China Telecom Macao sont disponibles en deux types : rouges et bleues. Les cartes rouges offrent des forfaits journaliers, coûtant généralement 2, 3 ou 5 patacas de Macao par jour. Les cartes bleues proposent des forfaits de données, comme 10 Go pour 98 patacas de Macao ou 20 Go pour 198 patacas de Macao, sans frais mensuels.

* Si vous avez besoin de plus de données ou utilisez fréquemment un ordinateur portable, envisagez d'utiliser [zhs.cloud](https://zhs.cloud). Il donne accès à environ 15 serveurs proxy mondiaux pour seulement 30 CNY par mois.

* Sur iOS, utilisez Shadowrocket avec les règles Shadowsocks : [https://github.com/Johnshall/Shadowrocket-ADBlock-Rules-Forever](https://github.com/Johnshall/Shadowrocket-ADBlock-Rules-Forever). Configurez le routage global pour séparer le trafic chinois du trafic international.

* Sur Android, utilisez V2Ray. Sur Fire TV, utilisez l'application V2Ray. Sur Apple TV, utilisez l'application Shadowrocket. Sur Mac, utilisez l'application ShadowsocksX-NG ou ClashX.

* Il n'est pas recommandé de configurer soi-même un serveur proxy. Les protocoles comme Shadowsocks, VMess ou Trojan sont facilement bloqués, quel que soit le serveur utilisé.

* Pour changer la région de l'App Store en USA, activez un proxy global (USA), et l'option de paiement "Aucun" apparaîtra, vous permettant de changer ouvertement de région.

* Utilisez une carte Visa pour acheter des cartes cadeaux sur Amazon ou utilisez le portail de cartes cadeaux Apple pour créditer votre compte App Store.

---

## Le parcours vers la liberté sur Internet

*03.02.2025, Cet article a été mis à jour pour la dernière fois en août 2025.*

#### Le parcours

De 2010 à 2013, j'ai utilisé Goagent et l'outil proxy SwitchyOmega pour contourner le GFW.

Entre 2014 et 2015, j'ai utilisé Qujing (曲径) pour le proxy et j'ai suivi son auteur sur Twitter, qui vit maintenant au Japon.

De juin 2016 à juillet 2018, j'ai utilisé Digital Ocean pour héberger mon serveur proxy Shadowsocks.

À partir de 2019, j'ai commencé à utiliser [zhs.cloud](https://zhs.cloud).

En mars 2023, j'ai commencé à utiliser une carte SIM de Macao dans mon téléphone portable pour accéder à Internet sans proxy ni VPN. Cela coûtait environ 150 CNY par mois pour 20 Go de données mobiles, et j'ai utilisé cette méthode pendant environ un an.

En 2024, j'ai recommencé à utiliser Outline Manager avec mon serveur proxy Shadowsocks, en expérimentant divers fournisseurs de cloud.

En février 2025, ma configuration préférée est Outline Manager avec un serveur Aliyun Hong Kong pour un usage quotidien et un serveur non hongkongais (comme Singapour ou le Japon) pour les outils d'IA. Je maintiens la même configuration de règles de proxy utilisée dans Shadowrocket ou Clash.

À partir de juin 2025, j'ai commencé à utiliser un script Python sur mon ordinateur portable pour sélectionner automatiquement un serveur proxy toutes les 10 minutes en fonction des résultats des tests de vitesse. Le script privilégie les serveurs de Singapour plutôt que ceux de Hong Kong pour l'utilisation des outils d'IA. Pour plus de détails, veuillez consulter [Automatisation de la gestion des proxys Clash](/clash-en). Pour le fournisseur de cloud VPN, j'ai toujours utilisé [zhs.cloud](https://zhs.cloud).

De plus, sur iOS, je suis revenu à l'utilisation d'une carte SIM de Macao, coûtant 150 CNY par mois pour 20 Go de données. J'ai également acheté 5 Go de données supplémentaires à trois reprises pour 20 MOP chacun, soit un total d'environ 200 CNY pour 35 Go de données sur mon téléphone portable.

Cela fonctionne très bien depuis les 2 derniers mois. J'espère pouvoir continuer à utiliser cette méthode pour surfer sur Internet jusqu'à ce que je quitte la Chine pour travailler à l'étranger.

#### La différence par rapport à la correction de la myopie

Un défi consiste à lutter contre le GFW, qui est d'origine humaine. L'autre consiste à aborder les principes du fonctionnement des muscles oculaires.

Il est facile de mesurer l'efficacité d'une solution proxy. Cependant, la correction de la myopie nécessite du temps pour déterminer si le globe oculaire change.

#### Similitudes avec la correction de la myopie

Une similitude est qu'une solution proxy et des lunettes avec une réduction de 200 degrés fonctionnent souvent bien. L'une concerne l'accès à Internet, l'autre l'amélioration de la vue. Les deux abordent des problèmes très importants.

Le principe sous-jacent est que si nous comprenons comment fonctionne le GFW et trouvons un moyen de le contourner, la solution devrait être simple.

#### Raisonnement et nuances

Je ne comprends toujours pas entièrement le fonctionnement du GFW. Lorsque l'IP de mon serveur proxy est bloquée, j'ai désormais plus de moyens d'enquêter sur la cause.

Je peux vérifier si le blocage se produit sur le réseau mobile ou la connexion haut débit domestique. Si c'est le réseau mobile, je peux vérifier si c'est sur le 4G ou le 5G.

De même, si ma myopie ne s'améliore pas après six mois ou un an, je dois enquêter pour voir s'il y a des différences entre mes yeux. Je dois également considérer si j'ai vu les choses à peine clairement sans forcer mes yeux pendant la majeure partie de l'année.

#### État actuel

Mon serveur proxy fonctionne actuellement très bien. Les vitesses de téléchargement sur mon téléphone atteignent 80 Mbps et les vitesses de téléversement atteignent 50 Mbps lors de la connexion au serveur proxy de Hong Kong. C'est également le cas sur mon ordinateur portable.

J'utilise les mêmes configurations de proxy sur mon ordinateur portable et mes téléphones, et elles fonctionnent parfaitement. Normalement, j'utilise un serveur proxy pour visiter des sites en dehors de la Chine, et un serveur non hongkongais pour les outils d'IA.

#### Récupération

Si quelque chose ne fonctionne pas, ma méthode de récupération est simple. Je dois simplement changer l'IP élastique de mon serveur proxy Aliyun Hong Kong et téléverser la nouvelle URL du proxy sur le stockage cloud. Cela signifie que je dois exécuter deux scripts, ce qui prend environ 1 minute, et mon ordinateur portable et mes téléphones peuvent mettre à jour l'adresse du serveur proxy.

#### Regret

J'ai lutté contre le GFW trop souvent et pendant trop de temps. J'ai essayé de nombreux protocoles de proxy, sachant qu'ils seraient détectés par le GFW et bloqués. Sans un serveur proxy fiable, il est difficile de configurer un proxy sur un routeur OpenWrt.

Une chose que je regrette est de ne pas avoir appris plus tôt les techniques des fournisseurs de proxy, comme [zhs.cloud](https://zhs.cloud). Je connais maintenant la plupart de leurs secrets.

L'autre chose est que chaque fois que mon serveur proxy était bloqué, je n'ai pas réfléchi assez profondément. Il semblait qu'il suffisait de configurer un nouveau serveur proxy pour obtenir une nouvelle adresse IP non bloquée. Mais c'était une réflexion superficielle.

#### Métriques

Je regrette de ne pas avoir utilisé Speedtest plus tôt. Je connaissais le nom de l'outil depuis longtemps, mais je n'ai pas appris à l'utiliser correctement.

Il est bon d'utiliser Speedtest souvent lorsque vous êtes connecté à des stations de signal mobile 5G ou 4G ou à un réseau haut débit domestique.

Pour la correction de la myopie, c'est la même chose. J'ai acheté un tableau oculaire en forme de C et un tableau oculaire standard.

Pas de mesure, pas d'amélioration. Mesurer les choses vous aide à apprendre. Utiliser souvent Speedtest m'aide à constater qu'il est facile de dépasser 100 Mbps sur un réseau 5G, tandis que sur un réseau haut débit domestique, il est difficile de dépasser 100 Mbps.

#### Il est encore tôt

Le GFW tombera-t-il dans les prochaines années ? Il est difficile de le dire.

Quand, après avoir corrigé ma myopie pendant deux ans, j'ai dit à mon ami que ma méthode de correction devait être améliorée et que je devais porter des lunettes avec 200 degrés de moins que ma prescription réelle au lieu de 150 degrés de moins.

Il a dit que ce n'était pas un problème, que c'était bien, que ce n'était pas une perte de temps, et qu'il était encore tôt. Oui. Ces choses sont fondamentales. Comme pour la myopie, les gens devraient la découvrir plus tôt. Todd Becker a partagé cette découverte sur YouTube en 2014, et les vidéos ont obtenu plus d'un million de vues. Et maintenant nous sommes en 2025, combien de personnes dans le monde la connaissent vraiment ? Je suppose que ce sera moins de 10 000.

---

## Cartes SIM de Macao

*20.04.2023*

#### Mon expérience avec les cartes SIM de Macao

Lors de ma visite de week-end à Macao en 2023, j'ai acheté une carte SIM China Telecom Easy+ Macao. Après mon arrivée à Guangzhou, j'ai constaté qu'elle fonctionnait toujours parfaitement, m'aidant à apprendre l'anglais et à télécharger de nombreuses applications étrangères. On aurait dit que j'étais encore à Macao. Je la recommande vivement. Plus tard, j'ai essayé la carte SIM Blue Macau, qui était également bonne. Voici un aperçu rapide des deux :

#### Carte SIM China Telecom Easy+

Facile à utiliser à tout moment !

### Points clés
- Pas de dépôt ; activation automatique pour la Chine continentale, Macao et Hong Kong.
- Pas de contrat ni de frais de résiliation ; prête à l'emploi dès l'achat.
- Numéro de Macao inclus ; numéro de Chine continentale optionnel pour une utilisation à double numéro.
- Recharge en ligne ou avec des cartes de valeur.

### Options de frais journaliers
- 2 $/jour : 4 Go à haute vitesse, puis illimité à vitesse réduite ; 5 000 minutes d'appels locaux.
- 3 $/jour : 10 Go à haute vitesse, puis illimité à vitesse réduite ; 5 000 minutes d'appels locaux.
- 5 $/jour : 20 Go à haute vitesse, puis illimité à vitesse réduite ; 5 000 minutes d'appels locaux.

### Extras
- Utilisation de données à Hong Kong : 0,1 $/Mo.
- Changez de forfait à tout moment en envoyant un SMS.

#### Carte SIM Blue Macau

### Points clés
- Pas de loyer mensuel ; payez à l'usage.
- Appels locaux : 0,39 MOP/minute ; Internet : 0,1 MOP/Mo ; SMS : 1 MOP/message.
- Forfaits de données sans expiration optionnels : 10 Go pour 98 MOP, 20 Go pour 188 MOP, 40 Go pour 288 MOP.
- Rechargez tous les 180 jours pour rester actif.

#### Appareils compatibles

- Nécessite un téléphone compatible 4G complet ou China Telecom.

Pour plus d'informations, visitez [China Telecom Macau](https://www.1888.com.mo/).

---

Vous pouvez également les trouver sur Taobao :

<div align="center"><img src="/assets/images/macao/easy.jpg" width="300px" /><img/></div>

---

## Problèmes de proxy Shadowsocks

*03.01.2025*

Zhiwei :

Je suis sorti pour un barbecue avec un ami et j'ai utilisé Shadowsocks avec un serveur basé à Singapour comme proxy pour contourner le Grand Pare-feu (GFW). Alors que j'utilisais le 5G à l'extérieur, je n'arrivais pas à me connecter, et le test a expiré lorsque j'ai essayé d'accéder à YouTube. Cependant, lorsque je suis chez moi en utilisant le 4G ou mon réseau domestique China Telecom, Shadowsocks fonctionne bien. Pourquoi cela se produit-il ?

Mistral :

Il semble que vous rencontriez des problèmes de connectivité avec votre proxy Shadowsocks lorsque vous utilisez le 5G à l'extérieur, mais pas lorsque vous utilisez le 4G ou votre réseau domestique. Plusieurs raisons peuvent expliquer cela :

1. Différences de configuration réseau :
   - Réseau 5G : Le réseau 5G peut avoir des configurations ou restrictions différentes par rapport au 4G. Certains opérateurs peuvent avoir des règles de pare-feu plus strictes ou un routage réseau différent pour le 5G, ce qui peut affecter les performances de votre proxy Shadowsocks.
   - Réseau 4G : Le réseau 4G peut avoir des paramètres plus souples ou un meilleur routage qui permet à votre proxy Shadowsocks de fonctionner correctement.

2. Restrictions des FAI :
   - Politiques des opérateurs : Différents opérateurs peuvent avoir des politiques différentes concernant l'utilisation des VPN ou proxys. Votre opérateur 5G peut avoir des politiques plus strictes qui bloquent ou limitent le trafic VPN, y compris Shadowsocks.
   - Réseau domestique : Votre réseau domestique, fourni par China Telecom, peut avoir moins de restrictions, permettant à Shadowsocks de fonctionner sans problème.

3. Force et stabilité du signal :
   - Signal 5G : La stabilité et la force du signal 5G peuvent varier, en particulier dans les environnements extérieurs. Un signal faible ou instable peut provoquer des problèmes de connectivité, y compris des délais d'attente.
   - Signal 4G : Le signal 4G peut être plus stable et cohérent, offrant une meilleure connexion pour votre proxy Shadowsocks.

4. Emplacement du serveur proxy :
   - Serveur de Singapour : L'emplacement de votre serveur Shadowsocks à Singapour peut affecter la latence et la connectivité. Le réseau 5G peut avoir une latence plus élevée ou un routage moins optimal vers le serveur de Singapour par rapport au réseau 4G ou à votre réseau domestique.

5. Paramètres de l'appareil :
   - Configuration : Assurez-vous que les paramètres de votre appareil sont correctement configurés pour utiliser Shadowsocks. Parfois, le changement de réseau (du 5G au 4G ou au Wi-Fi domestique) peut entraîner une réinitialisation ou un changement des paramètres.
   - Autorisations de l'application : Assurez-vous que l'application Shadowsocks dispose des autorisations nécessaires pour fonctionner sur différents réseaux.

### Étapes de dépannage :

1. Vérifiez les paramètres réseau :
   - Assurez-vous que les paramètres de Shadowsocks sont correctement configurés pour les réseaux 5G et 4G.
   - Vérifiez qu'il n'y a pas de restrictions ou de paramètres spécifiques sur votre réseau 5G qui pourraient bloquer le proxy.

2. Testez différents serveurs :
   - Essayez de vous connecter à différents serveurs Shadowsocks pour voir si le problème est spécifique au serveur de Singapour.
   - Vérifiez la latence et la stabilité de la connexion au serveur.

3. Contactez votre opérateur :
   - Si le problème persiste, contactez votre opérateur 5G pour vous renseigner sur les restrictions ou paramètres pouvant affecter votre connexion Shadowsocks.

4. Mettez à jour les logiciels :
   - Assurez-vous que votre application Shadowsocks et les logiciels de votre appareil sont à jour. Parfois, les mises à jour peuvent résoudre les problèmes de connectivité.

5. Utilisez des proxys alternatifs :
   - Envisagez d'utiliser des services de proxy ou VPN alternatifs qui pourraient avoir une meilleure compatibilité avec votre réseau 5G.

En vérifiant systématiquement ces facteurs, vous devriez pouvoir identifier la cause du problème de connectivité et trouver une solution adaptée.

--

Mise à jour :

En fait, mon Wi-Fi domestique utilise China Mobile Communications Corporation, et son adresse est du type 120.235.8.xx.

Intéressamment, j'ai observé des schémas de connectivité incohérents : alors que mon serveur proxy fonctionne normalement sur les données mobiles et les réseaux China Telecom, il échoue parfois à se connecter lorsque j'utilise mon réseau Wi-Fi domestique.