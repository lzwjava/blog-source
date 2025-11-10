---
audio: false
generated: true
lang: fr
layout: post
title: Optimisation des appels d'outils d'IA avec une exécution côté serveur
translated: true
type: note
---

Oui, la nature aller-retour des appels d'outils ou de fonctions traditionnels dans les chatbots (où le modèle d'IA génère un appel, l'envoie au client ou à un autre service, attend l'exécution, puis reçoit les résultats) peut effectivement introduire de la latence, en particulier dans les applications en temps réel. Cela est souvent dû à la surcharge réseau, à la sérialisation/désérialisation et à la nécessité de multiples allers-retours d'API. Votre suggestion d'utiliser des fonctions lambda ou de concevoir une API qui accepte du code Python pour une exécution côté serveur est une manière intelligente d'atténuer ce problème—en déplaçant essentiellement le calcul vers le serveur pour minimiser les interactions client-serveur. Je vais décomposer cela conceptuellement, discuter de la faisabilité, des implémentations potentielles et des compromis.

### Pourquoi les appels d'outils traditionnels peuvent être lents
Dans de nombreux frameworks d'IA (par exemple, LangChain, les appels de fonction d'OpenAI, ou les outils d'Anthropic) :
- Le modèle produit un appel d'outil structuré (par exemple, du JSON avec le nom de la fonction et les arguments).
- Le client (ou l'agent) exécute la fonction localement ou via une autre API.
- Les résultats sont ajoutés à l'historique de la conversation et renvoyés au modèle pour l'étape d'inférence suivante.
Cette boucle peut ajouter des secondes de délai par cycle, ce qui s'accumule dans des tâches complexes comme l'analyse de données ou le raisonnement en plusieurs étapes.

### Utilisation de fonctions Lambda ou de l'exécution de code côté serveur
Votre idée s'aligne sur les modèles d'exécution "serverless" ou "sandboxés", où l'IA génère du code (ou un extrait de type lambda) qui est exécuté directement sur le serveur hébergeant le modèle. Cela maintient le tout dans un seul environnement, réduisant les allers-retours à potentiellement un seul appel d'API de l'utilisateur.

- **Approche par fonctions Lambda** : Des services comme AWS Lambda, Google Cloud Functions ou Azure Functions permettent d'exécuter à la demande de petits extraits de code Python éphémères sans gérer de serveurs. Dans un contexte d'IA :
  - Le backend du chatbot pourrait encapsuler le modèle d'IA (par exemple, via l'API OpenAI) et intégrer Lambda comme un outil.
  - Le modèle génère une expression lambda ou une fonction courte, qui est invoquée côté serveur.
  - Avantages : Évolutif, paiement à l'usage et démarrage rapide (souvent <100 ms de démarrage à froid).
  - Inconvénients : Temps d'exécution limité (par exemple, 15 minutes maximum sur AWS), et vous devriez gérer la gestion de l'état si la tâche s'étend sur plusieurs invocations.
  - Exemple : Un agent d'IA pourrait générer une lambda pour traiter des données (par exemple, `lambda x: sum(x) if isinstance(x, list) else 0`), l'envoyer à un point de terminaison Lambda et obtenir les résultats en ligne.

- **Concevoir une API pour accepter et exécuter du code Python** :
  - Oui, c'est tout à fait possible et existe déjà dans des systèmes en production. La clé est le **sandboxing** pour prévenir les risques de sécurité comme l'exécution de code arbitraire (par exemple, supprimer des fichiers ou effectuer des appels réseau).
  - Fonctionnement : Le point de terminaison de l'API reçoit un extrait de code (sous forme de chaîne), l'exécute dans un environnement isolé, capture la sortie/les erreurs et renvoie les résultats. Le modèle d'IA peut générer et "appeler" ce code de manière itérative sans quitter le serveur.
  - Avantages :
    - Réduit la latence : L'exécution a lieu dans le même centre de données que le modèle, souvent en millisecondes.
    - Permet des tâches complexes : Comme le traitement de données, les simulations mathématiques ou la manipulation de fichiers sans outils externes.
    - Sessions avec état : Certaines implémentations maintiennent un environnement de type REPL entre les appels.
  - Mesures de sécurité :
    - Utiliser des conteneurs (Docker), des micro-VM (Firecracker) ou des interpréteurs Python restreints (par exemple, le sandboxing PyPy ou des globaux restreints).
    - Limiter les ressources : Quotas CPU/temps, pas d'accès réseau, modules autorisés (par exemple, numpy, pandas, mais pas os ou subprocess).
    - Des bibliothèques comme `restrictedpython` ou des outils comme E2B/Firecracker fournissent des sandbox prêts à l'emploi.

### Exemples et implémentations réels
Plusieurs plateformes d'IA prennent déjà en charge cela à divers degrés :
- **Assistants API d'OpenAI avec Code Interpreter** : Permet au modèle d'écrire et d'exécuter du code Python dans un environnement sandboxé sur les serveurs d'OpenAI. Le modèle peut télécharger des fichiers, exécuter du code et itérer sur les résultats—le tout côté serveur. Aucune nécessité d'exécution côté client.
- **Exécution de code de l'API Gemini de Google** : Fournit un sandbox Python intégré où le modèle génère et exécute du code de manière itérative, apprenant des sorties sans appels externes.
- **Solutions personnalisées** :
  - **Sandbox E2B** : Un SDK/API pour créer des sandbox basés sur le cloud avec des noyaux Jupyter. Les agents d'IA peuvent envoyer du code à exécuter de manière sécurisée, idéal pour les outils d'analyse de données.
  - **Sandboxes Modal** : Une plateforme pour exécuter du code généré par l'IA dans des environnements isolés, souvent utilisée pour les agents LLM.
  - **SandboxAI (open-source)** : Un runtime spécifiquement pour exécuter du Python généré par l'IA dans des sandbox.
  - Pour une solution DIY : Construire un serveur FastAPI ou Flask qui accepte le code via POST, utilise `exec()` dans un espace de noms restreint, ou lance un conteneur Docker par requête.

En termes de code, un point de terminaison d'API simple pourrait ressembler à ceci (pseudocode pour illustration) :

```python
from fastapi import FastAPI
import restrictedpython  # Pour une exécution sécurisée

app = FastAPI()

@app.post("/execute")
def execute_code(code: str):
    safe_globals = {"__builtins__": restrictedpython.safe_builtins}  # Environnement restreint
    try:
        result = {}
        exec(code, safe_globals, result)  # Exécuter le code
        return {"output": result.get("output")}
    except Exception as e:
        return {"error": str(e)}
```

Intégrez cela avec votre chatbot : L'IA génère du code basé sur la saisie de l'utilisateur, appelle le point de terminaison en interne et intègre les résultats.

### Inconvénients potentiels et bonnes pratiques
- **Risques de sécurité** : L'exécution de code arbitraire est dangereuse—toujours utiliser un sandbox. À éviter si vous traitez des utilisateurs non fiables.
- **Coût et évolutivité** : L'exécution côté serveur utilise plus de calcul ; surveillez avec des outils comme New Relic pour l'optimisation.
- **Débogage** : Les erreurs dans le code généré peuvent boucler si elles ne sont pas bien gérées.
- **Alternatives pour l'optimisation** :
  - Regrouper les appels d'outils : Grouper plusieurs fonctions en un seul aller-retour serveur.
  - Streaming : Utiliser des API qui diffusent les réponses tout en exécutant les outils en parallèle.
  - Côté client si tolérant à la latence : Pour les tâches non sensibles, exécuter localement.
- Si vous partez de zéro, commencez avec des frameworks comme LangChain ou le SDK AI de Vercel, qui prennent en charge les outils personnalisés et peuvent être configurés pour des exécutions côté serveur.

Cette approche peut rendre les chatbots beaucoup plus rapides et capables, en particulier pour les tâches computationnelles. Si vous implémentez cela, envisagez de commencer par les fonctionnalités intégrées d'OpenAI ou de Gemini pour des résultats rapides.

[Building a Sandboxed Environment for AI generated Code Execution](https://anukriti-ranjan.medium.com/building-a-sandboxed-environment-for-ai-generated-code-execution-e1351301268a)  
[substratusai/sandboxai: Run AI generated code in isolated sandboxes](https://github.com/substratusai/sandboxai)  
[Build AI data analyst with sandboxed code execution using TS ... - E2B](https://e2b.dev/blog/build-ai-data-analyst-with-sandboxed-code-execution-using-typescript-and-gpt-4o)  
[Code execution | Gemini API](https://ai.google.dev/gemini-api/docs/code-execution)  
[Assistants Code Interpreter - OpenAI API](https://platform.openai.com/docs/assistants/tools/code-interpreter)  
[Modal Sandboxes](https://modal.com/use-cases/sandboxes)  
[Optimizing AI chatbot performance with New Relic AI monitoring](https://newrelic.com/blog/how-to-relic/optimizing-ai-chatbot-performance)