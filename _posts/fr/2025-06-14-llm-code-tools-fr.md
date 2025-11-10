---
audio: false
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Les LLM, le raisonnement en code et l'utilisation d'outils
translated: true
type: note
---

Excellente question ! Vous demandez essentiellement comment un modèle comme **Claude d'Anthropic (et d'autres LLM similaires)** gère en interne :

1.  **L'exécution de code ou le raisonnement lié au code**
2.  **La validation de schémas JSON / la production de sorties structurées**
3.  **L'utilisation d'outils et l'acheminement entre eux**

Laissez-moi détailler cela.

---

### 1. Raisonnement et exécution de code
Claude (et les autres LLM de pointe) n'exécutent pas réellement de code directement à l'intérieur du modèle — ils **simulent un raisonnement de code** en prédisant des tokens de code ou des étapes logiques.

- En **mode texte normal**, Claude peut "écrire" du code en poursuivant un motif, mais il ne l'exécute pas en interne.
- Lorsqu'il est utilisé avec un **backend (comme Anthropic's Workbench, ou l'Interpréteur de Code d'OpenAI)**, le système peut intercepter ces extraits de code et les *exécuter* réellement dans un environnement sandboxé.
- Les résultats peuvent ensuite être renvoyés au modèle comme contexte, afin qu'il puisse enchaîner son raisonnement comme suit :
  → Générer du code → Exécuter en externe → Recevoir le résultat → Décider de l'étape suivante.

L'intelligence réside donc dans la boucle : le LLM génère → un exécuteur externe exécute → le LLM interprète les résultats.

---

### 2. Validation de schéma JSON
De nombreuses API (Claude, OpenAI, etc.) prennent désormais en charge le **mode de sortie structurée**, où vous pouvez attacher un schéma JSON. Voici comment cela fonctionne en interne :

- Vous transmettez une **définition de schéma JSON** avec votre requête.
- Le LLM est guidé pour produire **uniquement du JSON valide** qui y conforme.
- S'il tente de produire un JSON non valide, le système le détecte (en utilisant un validateur comme [jsonschema](https://pypi.org/project/jsonschema/)) et demande au modèle de "corriger" la sortie.
- En arrière-plan, il s'agit souvent d'un mécanisme de **décodage contraint** ou de **décodage basé sur une grammaire** — cela restreint la génération de tokens pour que seuls les `"tokens valides suivants dans le schéma"` soient autorisés.

Cela garantit que la sortie est un JSON syntaxiquement et sémantiquement correct, ce qui est crucial pour l'automatisation de l'utilisation d'outils.

---

### 3. Utilisation d'outils et acheminement
L'utilisation d'outils est gérée via une **couche de routage** entre le LLM et un environnement d'exécution d'outils :

- **Logique de routage** : Le modèle est incité à *décider quel outil appeler* (ou à répondre directement).
- **Application du schéma** : Chaque outil possède un schéma d'entrée. Le LLM doit produire un JSON valide pour cet outil.
- **Adaptateurs d'exécution** : La couche d'orchestration (en dehors du modèle) prend le JSON du LLM, le valide par rapport au schéma, exécute l'outil, puis renvoie les résultats dans le contexte.
- **Raisonnement enchaîné (style ReAct)** : Le LLM "réfléchit à haute voix" (peut produire des étapes de raisonnement cachées pour l'utilisateur), puis émet des appels d'outils lorsque nécessaire, pour arriver progressivement à une réponse finale.

Par exemple :
```json
{
  "tool": "web_search",
  "query": "dernières recherches sur la correction d'erreurs quantiques"
}
```
→ Le routeur voit `"tool": "web_search"`, valide le schéma, exécute la recherche web, replace les résultats dans le contexte du modèle, et le modèle continue son raisonnement.

Claude d'Anthropic, les GPTs d'OpenAI, LangChain et d'autres prennent tous en charge ce modèle.

---

### 🔑 Résumé
- **Code avec Claude** : N'exécute pas de code en interne ; génère du code → un sandbox exécute → les résultats sont renvoyés → raisonnement itératif.
- **Validation de schéma JSON** : Utilise un décodage contraint / une validation de schéma pour garantir une sortie structurée valide.
- **Routage d'utilisation d'outils** : Le LLM sélectionne des appels d'outils en JSON, le moteur d'orchestration les valide et les exécute, et renvoie les résultats dans la boucle.

---

👉 Souhaitez-vous que je **dessine un diagramme** montrant le flux (LLM ↔ routeur d'outils ↔ validateur de schéma ↔ moteur d'exécution) pour une meilleure clarté visuelle ?