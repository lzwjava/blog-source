---
audio: false
date: 2025-09-11
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Travailler avec les modèles de chat Completions d'OpenAI
translated: true
type: note
---

Vous avez partagé l’article Microsoft Learn **« Work with chat completions models »** (publié le **1er septembre 2025**). Voici un résumé clair et concis de ses points principaux :

---

### Points Clés

* **Modèles orientés conversation**
  Les nouveaux modèles de chat diffèrent des anciens modèles GPT-3. Au lieu d’un format « texte-entrée, texte-sortie », ils utilisent un format **conversation-en-entrée, message-en-sortie**. Concrètement, l’entrée est structurée comme une transcription (avec des rôles comme *system*, *user*, *assistant*), et le modèle renvoie un message pour poursuivre la conversation ([Microsoft Learn][1]).

* **Conçus pour le dialogue**
  Cette structure est optimisée pour les conversations interactives à plusieurs tours. Elle fonctionne également bien pour les scénarios à invite unique, mais le format conversationnel permet des interactions plus fluides ([Microsoft Learn][1]).

* **Ne les utilisez pas comme les anciens modèles**
  Ces modèles de chat sont plus verbeux et produisent souvent des réponses moins utiles si vous les abordez comme GPT-3. Il est recommandé d'utiliser la nouvelle interface de type chat pour de meilleurs résultats ([Microsoft Learn][1]).

* **Extrait de code exemple**
  L'article inclut un exemple de code basique utilisant une syntaxe de type Python pour appeler l'API de chat completions d'Azure :

  ```python
  from openai import OpenAI
  import os

  client = OpenAI(
      api_key=os.getenv("AZURE_OPENAI_API_KEY"),
      base_url="https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/"
  )

  response = client.chat.completions.create(
      model="gpt-4o",  # or deployment_name
      messages=[
          {"role": "system", "content": "Assistant is a large language model trained by OpenAI."},
          {"role": "user", "content": "Who were the founders of Microsoft?"}
      ]
  )

  print(response.model_dump_json(indent=2))
  print(response.choices[0].message.content)
  ```

  Cela montre comment envoyer correctement des messages (avec une séparation des rôles) et récupérer la réponse du modèle ([Microsoft Learn][1]).

---

### Pourquoi C'est Important

1. **Contexte conversationnel amélioré** — Les modèles de chat maintiennent mieux le flux et le contexte au cours des interactions à plusieurs tours.
2. **Utilisabilité améliorée** — L'utilisation des rôles (system, user, assistant) permet des instructions plus claires, la définition d'une personnalité ou l'application de contraintes.
3. **Évitez les pièges** — Traiter les modèles de chat comme ceux des générations précédentes peut entraîner une qualité de réponse médiocre ; utilisez l'interface de l'API de chat comme prévu.

---

Faites-moi savoir si vous souhaitez de l'aide pour parcourir l'exemple de code, l'adapter à votre configuration ou explorer d'autres guides — je suis ravi de vous aider !

Et comme vous le préférez, j'ai conservé un format simple et lisible sans tableaux.

[1]: https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/chatgpt?utm_source=chatgpt.com "Work with chat completion models - Azure OpenAI in ..."