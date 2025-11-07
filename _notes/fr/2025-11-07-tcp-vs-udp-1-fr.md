---
audio: false
generated: true
image: false
lang: fr
layout: post
model: anthropic/claude-4.5-sonnet
title: Différences entre les connexions TCP et UDP
translated: true
---

Vous avez la bonne intuition ! Laissez-moi clarifier les différences clés :

## Connexion TCP

Lorsqu'une connexion TCP est **établie** (via le handshake en trois étapes), les deux parties maintiennent des **informations d'état** l'une sur l'autre :

**Ce que chaque côté stocke :**
- **Adresse IP et port distants** (à qui est-ce que je parle ?)
- **Adresse IP et port locaux** (mon point de terminaison)
- **Numéros de séquence** (pour l'ordonnancement et la fiabilité)
- **Tailles de fenêtre** (pour le contrôle de flux)
- **État de la connexion** (ÉTABLI, FERMETURE, etc.)

Donc oui, "connecté" signifie que le client et le serveur ont alloué de la mémoire et des ressources pour suivre cette conversation spécifique. Ils se connaissent et maintiennent cette relation jusqu'à ce que la connexion soit fermée.

## UDP - Aucune Connexion

UDP est **sans connexion**. Il n'y a pas de handshake, pas d'état stocké :

- Le client envoie simplement un paquet vers une IP:port
- Le serveur le reçoit et le traite
- **Aucune des deux parties ne maintient d'informations sur la relation**
- Chaque paquet est indépendant
- Très léger - pas de surcharge mémoire par "connexion"

## La Différence Clé

**TCP :** "Bonjour, je suis le Client X. Parlons. Voici mes infos, j'ai les vôtres. Nous sommes maintenant connectés." → **Avec état**

**UDP :** "Voici un paquet pour l'adresse Y:port Z" → Envoi et oubli → **Sans état**

Vous avez parfaitement raison que UDP est beaucoup plus léger car il n'y a pas d'état de connexion à maintenir, pas de tampons à gérer et pas d'accusés de réception à suivre. Le compromis est que TCP fournit la fiabilité, l'ordonnancement et le contrôle de flux, tandis qu'UDP offre la vitesse et la simplicité.