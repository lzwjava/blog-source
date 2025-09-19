---
audio: false
generated: false
image: true
lang: fr
layout: post
title: Comment accéder à Google
translated: true
---

Cet article a été initialement écrit en chinois.

---

Ce cours couvre les points suivants :

1. Comment accéder au site officiel d’un service VPN.
2. Comment utiliser un VPN sous Windows.
3. Introduction au logiciel Clash.
4. Tentative d’ouverture de Google, Twitter, YouTube et TikTok.

Commençons. Voici une description écrite de la façon dont j’ai appris à Xiao Wang à accéder à Google.

Nous allons utiliser une plateforme appelée « Summoner ». Le site web est `https://zhshi.gitlab.io`.

<img src="/assets/images/google/zhs.png" alt="zhs" />

Cependant, il se peut qu’il soit inaccessible car bloqué par le pare-feu chinois.

![zhs_user](/assets/images/google/zhs_user.png)

Voici à quoi cela ressemble lorsque vous vous connectez.

Il existe en fait deux façons de contourner le pare-feu. L’une consiste à acheter notre propre serveur à l’étranger. L’autre consiste à utiliser une plateforme VPN, qui fournit de nombreuses adresses de serveurs à l’étranger.

« Contourner le pare-feu » signifie d’abord accéder à un serveur à l’étranger depuis le pays. Ce serveur à l’étranger peut ensuite accéder aux sites web qui sont bloqués.

Une telle plateforme s’appelle « Summoner ». Mais si le site officiel est inaccessible, comment obtenons-nous les adresses de serveurs à l’étranger qu’il fournit ? Xiao Wang utilise un VPN pour la première fois, et je lui enseigne à distance. Comment dois-je lui apprendre ?

À ce stade, j’ai pensé à activer l’ordinateur Windows de Xiao Wang pour contourner le pare-feu. Je vais fournir à Xiao Wang une adresse. Ensuite, Xiao Wang pourra ouvrir le site web « Summoner », créer un compte et utiliser les adresses de serveurs à l’étranger sous son propre compte.

![clash_win](/assets/images/google/clash_win.png)

![win_version](/assets/images/google/win_version.png)

Ensuite, vérifiez si votre ordinateur est 64 bits ou 32 bits. S’il est 64 bits, téléchargez `Clash.for.Windows.Setup.0.14.8.exe`. S’il est 32 bits, téléchargez `Clash.for.Windows.Setup.0.14.8.ia32.exe`.

L’ordinateur de Xiao Wang est 64 bits. Mais le téléchargement est très lent de son côté. Je l’ai donc téléchargé sur mon ordinateur et je le lui ai envoyé par e-mail QQ.

Il l’a téléchargé depuis l’e-mail QQ, l’a installé et l’a ouvert.

![clash_win_exe](/assets/images/google/clash_win_exe.png)

Je lui ai d’abord donné mon adresse de configuration Summoner. Cette adresse de configuration téléchargera un fichier contenant de nombreuses adresses de serveurs VPN. Sous `Profils`, collez l’adresse et cliquez sur `Télécharger`.

![zhs_url](/assets/images/google/zhs_url.png)

Vous voyez, il est téléchargé. Remarquez la deuxième configuration ci-dessus. Il y a une coche verte devant, indiquant que nous utilisons cette configuration.

![zhs_proxy](/assets/images/google/zhs_proxy.png)

Ensuite, ouvrez l’onglet `Proxys`. Vous verrez certaines choses ici. Ce sont quelques-unes des configurations de `Clash`. En termes simples, cela signifie que les sites web nationaux n’utiliseront pas le VPN, tandis que les sites web étrangers le feront.

Notez que la valeur actuelle de `Proxy` est `DIRECT`, ce qui signifie qu’il s’agit d’une connexion directe. Nous allons la changer pour un nœud.

![zhs_node](/assets/images/google/zhs_node.png)

Nous avons sélectionné le nœud `US Rose`.

![clash_system](/assets/images/google/clash_system.png)

Ensuite, activez le paramètre `Proxy système` pour l’activer. Cela signifie définir le logiciel `Clash` comme couche proxy du système. Ensuite, le trafic du système ira d’abord au logiciel `Clash`, puis accédera au réseau externe.

<img src="/assets/images/google/google.png" alt="google" style="zoom:40%;" />

Xiao Wang a ouvert Google. Ensuite, il a essayé TikTok, YouTube et Twitter.

Bon, donc Xiao Wang a utilisé mon compte Summoner. Comment s’inscrire ? Il doit ouvrir le site web officiel de Summoner.

<img src="/assets/images/google/zhs_register.png" alt="zhs_register" style="zoom:50%;" />

Après son inscription, il a constaté que le rechargement pour acheter des services nécessite quelques étapes. Voici une capture d’écran de mon compte.

![zeng](/assets/images/google/zeng.png)

Il indique qu’il doit être lié à Telegram.

<img src="/assets/images/google/zhs_telegram.png" alt="zhs_telegram" style="zoom:50%;" />

Xiao Wang s’est rendu sur le site web de Telegram et a téléchargé la version de bureau Windows de Telegram.

![telegram](/assets/images/google/telegram.png)

Après l’avoir téléchargé et installé, faites attention au texte ci-dessus.

> Après avoir installé Telegram et vous être inscrit, cliquez pour discuter avec `小兔` ou `城主`, copiez le code QR ci-dessous et envoyez-le leur, ou `cliquez ici pour copier automatiquement le code et l’envoyer au Bot pour le lier`.

Lorsque vous cliquez sur `小兔`, cela sautera automatiquement vers le logiciel `Telegram` et ouvrira une fenêtre de discussion avec `小兔`. Ensuite, envoyez-leur le code.

![telegram_username](/assets/images/google/telegram_username.png)

Cependant, le compte `Telegram` de Xiao Wang est nouvellement créé et n’a pas de `nom d’utilisateur`. C’est comme utiliser WeChat sans définir d’ID WeChat.

Trouvez le menu Telegram et définissez-le. Ensuite, envoyez à nouveau le code pour lier.

<img src="/assets/images/google/zhs_set.png" alt="zhs_set" style="zoom:50%;" />

Ensuite, vous pouvez faire un don pour le soutenir. Vous pouvez commencer par recharger 30 yuans pour deux mois.

Retournez sur la page d’accueil de Summoner. Ici, recherchez le bouton « Cliquez pour copier », obtenez l’adresse, puis téléchargez la configuration dans le logiciel `Clash`.

Ensuite, Xiao Wang peut supprimer l’adresse que je lui ai donnée. Xiao Wang a maintenant son propre compte Summoner.
