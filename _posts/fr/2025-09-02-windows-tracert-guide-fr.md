---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Guide de Diagnostic du Chemin Réseau Windows Tracert
translated: true
type: note
---

Sous Windows, **`tracert`** (abréviation de *trace route*) est un outil de diagnostic en ligne de commande utilisé pour tracer le chemin que prennent les paquets de votre ordinateur vers un hôte de destination (comme un site web ou une adresse IP). Il est principalement utilisé pour identifier où se produisent les délais ou les problèmes de connexion dans un itinéraire réseau.

Voici comment il fonctionne étape par étape :

### 1. Requêtes ICMP Echo avec un TTL Incrémental

* `tracert` envoie des **paquets de requête ICMP Echo** (similaires à `ping`).
* Il manipule le champ **Time-To-Live (TTL)** dans l'en-tête IP.
* Le TTL commence à 1, puis augmente (2, 3, 4, …) avec chaque sonde.

### 2. Expiration du TTL et Réponses « Time Exceeded »

* Lorsqu'un routeur reçoit un paquet, il décrémente le TTL de 1.
* Si le TTL atteint **0**, le routeur supprime le paquet et renvoie un message **ICMP Time Exceeded** à l'expéditeur.
* Cela permet à `tracert` de connaître l'identité (IP/nom d'hôte) de ce routeur.

### 3. Construction de l'Itinéraire

* Pour TTL = 1, vous voyez le premier saut (votre passerelle par défaut).
* Pour TTL = 2, vous voyez le routeur suivant, et ainsi de suite.
* Cela continue jusqu'à ce que :

  * L'hôte de destination réponde par une **réponse ICMP Echo Reply**, ou
  * La limite de sauts maximale (30 par défaut) soit atteinte.

### 4. Mesure de la Latence

* `tracert` envoie **trois sondes** par saut (par défaut).
* Il affiche le **temps aller-retour (RTT)** en millisecondes pour chaque sonde.
* Si un routeur ne répond pas, vous verrez `*` au lieu d'un temps.

### 5. Exemple de Sortie

```text
Tracert vers example.com [93.184.216.34]
sur un maximum de 30 sauts :

  1     1 ms    <1 ms     1 ms  192.168.1.1
  2    10 ms     9 ms    11 ms  isp-gateway.example.net [203.0.113.1]
  3    25 ms    23 ms    24 ms  core-router.example.net [198.51.100.1]
  ...
  8    45 ms    46 ms    47 ms  example.com [93.184.216.34]
```

### 6. Notes sur le Comportement

* Certains routeurs peuvent bloquer ou déprioriser les réponses ICMP, provoquant `* * *`.
* `tracert` sous **Windows** utilise des requêtes ICMP Echo, alors que `traceroute` sous Linux/Unix utilise souvent des **sondes UDP** (bien que cela puisse être modifié).
* Les pare-feux ou le filtrage FAI peuvent parfois masquer des parties de l'itinéraire.

---

👉 Souhaitez-vous que j'explique également **comment interpréter les cas comme `* * *` ou les délais importants** dans un résultat `tracert`, afin que vous puissiez l'utiliser pour un dépannage réel ?