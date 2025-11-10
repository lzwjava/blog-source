---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Métriques d'Exécution de Claude Sonnet Expliquées
translated: true
type: note
---

Ce que vous voyez sont des **métriques d'exécution** de l'inférence du modèle `anthropic/claude-sonnet-4` via Google Vertex AI. Permettez-moi de les détailler :

* **Latence du premier token (2,85 s) :**
  C'est le délai entre l'envoi de votre prompt et la réception du tout premier token de sortie. Cela inclut la latence réseau, la mise en file d'attente de la requête et le calcul initial du modèle. Pour les grands modèles comme Claude Sonnet, quelques secondes sont normales.

* **Débit (32,9 tokens/sec) :**
  Après la génération du premier token, le modèle diffuse les tokens suivants. 32,9 tokens par seconde est un taux correct — pas le plus rapide possible, mais bon pour un grand modèle. Le débit peut varier en fonction de la taille du modèle, de la charge sur la plateforme (Vertex) et de la longueur de votre prompt.

* **Raison de l'arrêt (stop) :**
  Cela indique simplement que le modèle s'est arrêté naturellement lorsqu'il a atteint la fin du texte qu'il générait (par opposition à l'atteinte d'une limite de longueur, une coupure ou une erreur).

Donc, **"pourquoi ?"** → parce que ces chiffres décrivent les caractéristiques d'inférence normales d'un grand LLM exécuté via Vertex :

* Une certaine latence de démarrage est attendue (compilation, optimisation, routage).
* Le débit se stabilise une fois que la génération commence.
* L'arrêt (stop) est la condition d'achèvement prévue.

Souhaitez-vous que je compare également ces chiffres avec les plages de performance typiques d'autres modèles (comme GPT-5, Gemini Pro, DeepSeek, etc.) afin que vous puissiez voir si c'était "rapide" ou "lent" dans ce contexte ?