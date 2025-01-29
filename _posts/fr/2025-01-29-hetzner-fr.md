---
audio: true
lang: fr
layout: post
title: Hetzner Cloud
translated: true
---

Je suis très excité d'essayer cette plateforme cloud récemment.

{: .centered }
![](assets/images/hertzner/h.jpg){: .responsive }
*Source: Hetzner*{: .caption }

Un serveur à Helsinki avec une configuration de 2 AMD VCPUs, 2GB RAM, 40GB SSD, et 20TB de trafic coûte 4,49 USD par mois.

Une adresse IPv4 coûte 0,60 USD supplémentaire par mois, portant le total à 5,09 USD par mois.

Ils offrent des services dans six lieux :

- Nuremberg, Allemagne
- Falkenstein, Allemagne
- Helsinki, Finlande
- Singapour, Singapour
- Hillsboro, OR, USA
- Ashburn, VA, USA

Il est intéressant de noter qu'ils ne suivent pas les tendances pour sélectionner des lieux populaires. Leurs emplacements sont différents de ceux de Vultr ou Digital Ocean.

Les paramètres de pare-feu sont faciles à utiliser. Bien que ce soit la première fois que j'utilise cela, j'ai rapidement configuré les paramètres corrects pour mon serveur proxy.

> sudo bash -c "$(wget -qO- https://raw.githubusercontent.com/Jigsaw-Code/outline-server/master/src/server_manager/install_scripts/install_server.sh)"

La vitesse du serveur Hetzner à Helsinki est très rapide. En utilisant l'application Speedtest iOS, la vitesse de téléchargement est de 423 Mbps et la vitesse de téléchargement est de 56,1 Mbps.

Le ping dans Shadowrocket est de 1175 ms, mais ce n'est pas un problème significatif.