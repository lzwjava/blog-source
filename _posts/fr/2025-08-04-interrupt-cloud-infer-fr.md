---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Les interruptions n'annulent pas l'inférence en nuage
translated: true
type: note
---

Lorsque vous interrompez (par exemple avec Ctrl-C) votre script Python pendant qu'il est en attente sur l'appel `generate_images(), voici grosso modo ce qui se passe :

1. **Comportement côté client**
   – Dès que vous terminez le processus Python, la connexion HTTP/gRPC sous-jacente est interrompue.
   – La bibliothèque cliente GenAI détectera généralement la rupture de connexion ou la réinitialisation et lèvera une exception (que vous verrez dans votre script).

2. **Ce qui se passe côté Google**
   – Au moment où vous annulez, votre requête a déjà atteint le service d'inférence de Google et a été mise en file d'attente (ou a déjà commencé à s'exécuter).
   – La plupart des points de terminaison d'inférence dans le cloud **n'annulent pas** automatiquement le travail simplement parce que le client a disparu. Ils continueront à exécuter votre tâche de génération d'image jusqu'à son terme (consommant des GPU/TPU et générant des coûts), même s'il n'y a plus de connexion active pour renvoyer le résultat.
   – Une fois le travail terminé, l'image générée est ignorée—il n'y a pas de rappel à moins que vous n'ayez configuré une opération de longue durée ou un webhook.

3. **Le rôle de Nginx (ou d'un autre proxy)**
   – S'il y a un proxy inverse Nginx devant le service d'inférence, son comportement par défaut est de surveiller la connexion client. Dès que le client abandonne, Nginx ferme sa connexion en amont vers le processus d'inférence (en envoyant un FIN/RST).
   – Le processus en amont voit alors un socket rompu lorsqu'il tente éventuellement d'écrire la réponse. À ce stade, il peut enregistrer une erreur d'E/S, mais—et c'est crucial—il ne **revient pas en arrière** et n'arrête pas le calcul que vous avez demandé ; il ne peut simplement pas délivrer les octets.
   – Vous pouvez ajuster la directive `proxy_ignore_client_abort` de Nginx—si vous la définissez sur `on`, Nginx maintiendra la connexion en amont même après la déconnexion du client (ce qui peut vous permettre de finaliser complètement l'écriture des journaux ou d'autres opérations de nettoyage).

4. **Points clés pour votre script**

   * **Les interruptions n'annulent pas** ou ne "déploient pas" le modèle sur les serveurs de Google—vous serez toujours facturé pour l'inférence complète.
   * Si vous avez besoin d'une inférence annulable, vous devriez utiliser un modèle différent : par exemple,

     1. Soumettre un traitement par lots non bloquant ou une opération de longue durée,
     2. Surveiller son statut ou l'annuler explicitement via un appel API séparé.

En résumé : arrêter votre script à 5 s interrompt votre attente locale et ferme le socket, mais l'inférence de Google continue de s'exécuter jusqu'à son terme sur son matériel (et Nginx ou un équivalent se contentera de rejeter la réponse dans le vide une fois qu'elle est prête).