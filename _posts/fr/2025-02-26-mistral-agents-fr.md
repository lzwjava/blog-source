---
audio: false
generated: true
lang: fr
layout: post
title: Agents IA Mistral
translated: true
type: note
---

Les agents Mistral AI sont des systèmes autonomes alimentés par de grands modèles de langage (LLM) conçus pour exécuter des tâches complexes à partir d'instructions de haut niveau. Tirant parti du traitement avancé du langage naturel, ces agents peuvent comprendre et réaliser des objectifs spécifiques, ce qui les rend adaptés à un large éventail d'applications telles que le support client, l'analyse de données, l'automatisation des flux de travail et l'assistance au codage. Ils peuvent planifier, utiliser des outils, entreprendre des actions et même collaborer pour atteindre des objectifs spécifiques, offrant ainsi un nouveau niveau d'automatisation et d'intelligence.

---

## Création d'agents

Mistral AI propose deux méthodes principales pour créer des agents : le **La Plateforme Agent Builder** et l'**Agent API**.

### 1. La Plateforme Agent Builder
L'Agent Builder offre une interface conviviale pour créer des agents sans connaissances techniques approfondies. Pour créer un agent :

- Accédez à l'Agent Builder à l'adresse [https://console.mistral.ai/build/agents/new](https://console.mistral.ai/build/agents/new).
- Personnalisez l'agent en sélectionnant un modèle, en réglant la température et en fournissant des instructions facultatives.
- Une fois configuré, l'agent peut être déployé et accessible via l'API ou Le Chat.

### 2. Agent API
Pour les développeurs, l'Agent API permet la création et l'intégration programmatiques d'agents dans les flux de travail existants. Voici des exemples de création et d'utilisation d'un agent via l'API :

#### Exemple Python
```python
import os
from mistralai import Mistral

api_key = os.environ["MISTRAL_API_KEY"]
client = Mistral(api_key=api_key)

chat_response = client.agents.complete(
    agent_id="your-agent-id",
    messages=[{"role": "user", "content": "What is the best French cheese?"}],
)
print(chat_response.choices[0].message.content)
```

#### Exemple JavaScript
```javascript
import { Mistral } from '@mistralai/mistralai';

const apiKey = process.env.MISTRAL_API_KEY;
const client = new Mistral({ apiKey: apiKey });

const chatResponse = await client.agents.complete({
    agentId: "your-agent-id",
    messages: [{ role: 'user', content: 'What is the best French cheese?' }],
});
console.log('Chat:', chatResponse.choices[0].message.content);
```

---

## Personnalisation des agents

Les agents Mistral AI peuvent être personnalisés pour répondre à des besoins spécifiques via plusieurs options :

- **Sélection du modèle** : Choisissez le modèle qui alimente l'agent. Les options incluent :
  - "Mistral Large 2" (par défaut, `mistral-large-2407`)
  - "Mistral Nemo" (`open-mistral-nemo`)
  - "Codestral" (`codestral-2405`)
  - Modèles fine-tunés

- **Température** : Ajustez la température d'échantillonnage (entre 0.0 et 1.0) pour contrôler le caractère aléatoire des réponses de l'agent. Des valeurs plus élevées rendent les sorties plus créatives, tandis que des valeurs plus basses les rendent plus ciblées et déterministes.

- **Instructions** : Fournissez des instructions facultatives pour imposer des comportements spécifiques à toutes les interactions. Par exemple, vous pouvez créer un agent qui parle uniquement français ou qui génère du code Python sans explications.

### Exemple : Création d'un agent francophone
Pour créer un agent qui répond uniquement en français :
- Définissez le modèle sur "Mistral Large 2".
- Utilisez des instructions comme : "Répondez toujours en français, quelle que soit la langue de la saisie."
- Fournissez des exemples few-shot pour renforcer le comportement.

---

## Cas d'utilisation

Les agents Mistral AI peuvent être appliqués dans diverses industries et tâches. Voici quelques cas d'utilisation notables :

- **Support client** : Automatisez les réponses aux demandes courantes, gérez les FAQ et escaladez les problèmes complexes vers des agents humains.
- **Analyse de données** : Créez des agents qui analysent des jeux de données, génèrent des rapports ou effectuent des calculs basés sur les saisies utilisateur.
- **Automatisation des flux de travail** : Intégrez des agents avec des outils comme les e-mails, les systèmes CRM ou le traitement des paiements pour automatiser les tâches répétitives.
- **Assistance au codage** : Concevez des agents pour générer du code, fournir des suggestions de débogage ou créer des tests unitaires.

### Exemples spécifiques
- **Agent francophone** : Un agent configuré pour ne répondre qu'en français, utile pour les entreprises ciblant une clientèle francophone.
- **Générateur de code Python** : Un agent qui produit des extraits de code Python sans explications, idéal pour les développeurs ayant besoin de code rapide et propre.

---

## Déploiement

Une fois créé, un agent peut être déployé et accessible de deux manières :

- **Intégration API** : Utilisez l'API Mistral AI pour intégrer l'agent dans vos applications. Reportez-vous aux exemples de code dans la section "Création d'agents" pour plus de détails.
- **Le Chat** : Activez l'option pour discuter directement avec l'agent sur la plateforme Le Chat de Mistral.

Les agents peuvent être facilement partagés au sein des organisations, et avec les capacités de raisonnement avancé de modèles comme Mistral Large 2, vous pouvez créer des flux de travail complexes impliquant plusieurs agents.

---

Cette documentation fournit un guide complet pour comprendre, créer, personnaliser et déployer des agents Mistral AI, basé sur la documentation officielle à l'adresse [https://docs.mistral.ai/capabilities/agents/](https://docs.mistral.ai/capabilities/agents/). En tirant parti de ces outils, vous pouvez automatiser des tâches, améliorer la productivité et débloquer de nouveaux niveaux d'efficacité dans vos flux de travail. Pour plus de détails, explorez la [documentation Mistral AI](https://docs.mistral.ai/capabilities/agents/).