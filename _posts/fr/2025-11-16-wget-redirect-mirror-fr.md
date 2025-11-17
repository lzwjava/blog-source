---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Redirection normale de wget depuis le miroir d'accum.se
translated: true
type: note
---

Votre commande `wget` accède à `https://mirror.accum.se/mirror/wikimedia.org/dumps/...` et reçoit une **redirection 302** vers `https://laotzu.ftp.acc.umu.se/...`. Ce comportement est tout à fait normal et attendu pour le miroir **accum.se** — voici pourquoi cela se produit et ce que cela signifie :

### Pourquoi la redirection se produit
`mirror.accum.se` est uniquement un **redirectionneur / répartiteur de charge** géré par l'Academic Computer Club à l'Université d'Umeå (ACC) en Suède.  
Il n'héberge **pas** les fichiers lui-même. À la place :

- Il examine la géolocalisation de votre IP (ou parfois la charge)
- Il vous redirige automatiquement vers le serveur de stockage réel le plus rapide/le plus proche dans sa ferme de miroirs
- Dans votre cas, il a choisi `laotzu.ftp.acc.umu.se` (qui est le vrai serveur FTP/HTTP qui contient les données)

C'est le même système qu'ils utilisent depuis de nombreuses années. Les autres noms d'hôte courants vers lesquels vous pourriez être redirigé sont :

- `issac.ftp.acc.umu.se`
- `laotzu.ftp.acc.umu.se` (celui que vous avez obtenu)
- `morpork.ftp.acc.umu.se`
- etc.

Ainsi, même si vous avez écrit `mirror.accum.se` dans votre script, vous finissez presque toujours par télécharger depuis l'un des back-ends `*.ftp.acc.umu.se`.

### Pourquoi vous avez vu "206 Partial Content" sur le premier fichier
Parce que vous (ou quelqu'un/un script) avez déjà commencé à télécharger ce même fichier auparavant, `wget -c` a détecté le fichier local partiel et a envoyé une requête `Range`. Le serveur a correctement repris le téléchargement → 206 Partial Content. C'est une bonne chose !

### Y a-t-il un problème ?
Non. Tout fonctionne comme prévu.

- La redirection est normale et sans conséquence
- Le serveur final (`laotzu.ftp.acc.umu.se`) est toujours le miroir officiel ACC/Wikimedia
- Les sommes de contrôle seront identiques, peu importe le serveur back-end vers lequel vous êtes redirigé

### Si vous voulez éviter la redirection (optionnel)
Vous pouvez contourner complètement le redirectionneur et pointer directement vers l'un des vrais hôtes, par exemple :

```bash
# Ces trois sont répartis de manière cyclique derrière mirror.accum.se de toute façon
wget -c https://laotzu.ftp.acc.umu.se/mirror/wikimedia.org/dumps/enwiki/20251101/...
# ou
wget -c https://issac.ftp.acc.umu.se/mirror/wikimedia.org/dumps/enwiki/20251101/...
```

Mais la plupart des gens continuent d'utiliser `mirror.accum.se` car le redirectionneur choisit automatiquement le meilleur pour vous.

### TL;DR
Votre script est correct. La redirection 302 de `mirror.accum.se` → `laotzu.ftp.acc.umu.se` est le comportement normal et attendu de ce miroir. Il n'y a aucun problème, et vous téléchargez toujours l'archive Wikimedia authentique. Continuez à utiliser `mirror.accum.se` — c'est l'un des miroirs les plus rapides et les plus fiables au monde.