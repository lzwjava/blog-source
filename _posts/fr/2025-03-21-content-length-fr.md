---
audio: false
generated: true
lang: fr
layout: post
title: En-tête HTTP Content-Length
translated: true
type: note
---

L'unité de l'en-tête **Content-Length** dans le protocole HTTP est l'**octet**.

Dans HTTP, l'en-tête **Content-Length** est utilisé pour indiquer la taille du corps de la réponse que le serveur envoie au client. Cette taille est spécifiée sous la forme d'un nombre décimal représentant le nombre d'octets (ou d'octets, où un octet équivaut à 8 bits) dans le corps du message. Selon la spécification HTTP/1.1 (RFC 7230, Section 3.3.2), le champ d'en-tête **Content-Length** indique explicitement la taille du corps du message en octets, ce qui confirme que l'unité est l'octet.

Par exemple, dans le cas fourni où l'en-tête est `'content-length': '130700923'`, cela signifie que le corps de la réponse a une longueur de **130 700 923 octets**. Pour donner une idée de l'échelle, cela représente environ **124,6 mégaoctets (Mo)**, puisque 1 Mo équivaut à environ 1 048 576 octets (2^20 octets). Il s'agit d'une taille plausible pour un fichier volumineux ou un transfert de données dans une réponse HTTP.

Pour clarifier davantage :
- La valeur est un entier, et non un nombre fractionnaire, ce qui exclut des unités comme les kilo-octets ou les mégaoctets directement.
- Dans HTTP, le corps est transmis sous la forme d'une séquence d'octets, et **Content-Length** correspond au nombre exact d'octets que le client doit s'attendre à recevoir.
- Même dans d'autres versions comme HTTP/2, où un cadrage est utilisé à la place d'un seul en-tête **Content-Length**, la taille de la charge utile est toujours mesurée en octets.

Ainsi, l'unité de **Content-Length** dans le protocole HTTP est incontestablement l'**octet**.