---
audio: false
generated: false
lang: fr
layout: post
title: Problèmes de Proxy Shadowsocks
translated: true
---

Zhiwei :

Je suis sorti pour un barbecue avec un ami et j'ai utilisé Shadowsocks avec un serveur basé à Singapour comme proxy pour contourner la Grande Muraille (GFW). En utilisant la 5G à l'extérieur, je n'arrivais pas à me connecter, et le test a expiré en essayant d'accéder à YouTube. Cependant, lorsque je suis chez moi en utilisant la 4G ou mon réseau domestique de China Telecom, Shadowsocks fonctionne parfaitement. Pourquoi cela se produit-il ?

Mistral :

Il semble que vous rencontriez des problèmes de connectivité avec votre proxy Shadowsocks lorsque vous utilisez la 5G à l'extérieur, mais pas lorsque vous utilisez la 4G ou votre réseau domestique. Plusieurs raisons pourraient expliquer cela :

1. Différences de configuration réseau :
   - Réseau 5G : Le réseau 5G pourrait avoir des configurations ou des restrictions différentes par rapport à la 4G. Certains opérateurs pourraient avoir des règles de pare-feu plus strictes ou un routage réseau différent pour la 5G, ce qui pourrait affecter les performances de votre proxy Shadowsocks.
   - Réseau 4G : Le réseau 4G pourrait avoir des paramètres plus souples ou un meilleur routage qui permet à votre proxy Shadowsocks de fonctionner correctement.

2. Restrictions des FAI :
   - Politiques des opérateurs : Différents opérateurs pourraient avoir des politiques différentes concernant l'utilisation des VPN ou des proxies. Votre opérateur 5G pourrait avoir des politiques plus strictes qui bloquent ou limitent le trafic VPN, y compris Shadowsocks.
   - Réseau domestique : Votre réseau domestique, fourni par China Telecom, pourrait avoir moins de restrictions, permettant à Shadowsocks de fonctionner sans problème.

3. Force et stabilité du signal :
   - Signal 5G : La stabilité et la force du signal 5G peuvent varier, surtout en extérieur. Un signal faible ou instable peut causer des problèmes de connectivité, y compris des délais d'attente.
   - Signal 4G : Le signal 4G pourrait être plus stable et constant, offrant une meilleure connexion pour votre proxy Shadowsocks.

4. Localisation du serveur proxy :
   - Serveur de Singapour : L'emplacement de votre serveur Shadowsocks à Singapour pourrait affecter la latence et la connectivité. Le réseau 5G pourrait avoir une latence plus élevée ou un routage moins optimal vers le serveur de Singapour par rapport au réseau 4G ou à votre réseau domestique.

5. Paramètres de l'appareil :
   - Configuration : Assurez-vous que les paramètres de votre appareil sont correctement configurés pour utiliser Shadowsocks. Parfois, le changement de réseau (de la 5G à la 4G ou au Wi-Fi domestique) peut entraîner une réinitialisation ou un changement des paramètres.
   - Permissions de l'application : Assurez-vous que l'application Shadowsocks dispose des permissions nécessaires pour fonctionner sur différents réseaux.

### Étapes de dépannage :

1. Vérifiez les paramètres réseau :
   - Assurez-vous que les paramètres de Shadowsocks sont correctement configurés pour les réseaux 5G et 4G.
   - Vérifiez qu'il n'y a pas de restrictions ou de paramètres spécifiques sur votre réseau 5G qui pourraient bloquer le proxy.

2. Testez différents serveurs :
   - Essayez de vous connecter à différents serveurs Shadowsocks pour voir si le problème est spécifique au serveur de Singapour.
   - Vérifiez la latence et la stabilité de la connexion au serveur.

3. Contactez votre opérateur :
   - Si le problème persiste, contactez votre opérateur 5G pour vous renseigner sur les restrictions ou les paramètres qui pourraient affecter votre connexion Shadowsocks.

4. Mettez à jour les logiciels :
   - Assurez-vous que l'application Shadowsocks et les logiciels de votre appareil sont à jour. Parfois, les mises à jour peuvent résoudre les problèmes de connectivité.

5. Utilisez des proxys alternatifs :
   - Envisagez d'utiliser des services de proxy ou des VPN alternatifs qui pourraient avoir une meilleure compatibilité avec votre réseau 5G.

En vérifiant systématiquement ces facteurs, vous devriez être en mesure d'identifier la cause du problème de connectivité et de trouver une solution appropriée.

--

Mise à jour :

En fait, mon Wi-Fi domestique utilise China Mobile Communications Corporation, et son adresse est du type 120.235.8.xx.

Fait intéressant, j'ai observé des schémas de connectivité incohérents - alors que mon serveur proxy fonctionne normalement sur les données mobiles et les réseaux de China Telecom, il échoue parfois à se connecter lorsque j'utilise mon réseau Wi-Fi domestique.