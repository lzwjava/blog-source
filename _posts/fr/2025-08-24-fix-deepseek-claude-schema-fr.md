---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Correction de l'Incompatibilité de Schéma de Code DeepSeek Claude
translated: true
type: note
---

Réponse courte : incompatibilité de schéma.

Claude Code « parle Anthropic » (il attend un style d'utilisation d'outils de type Anthropic-Messages comme les blocs `tool_use` / `tool_result`). DeepSeek V3.1 sur OpenRouter « parle OpenAI » (il émet un style d'appel de fonction / `tool_calls` OpenAI). Si votre routeur Claude Code transmet une tâche à DeepSeek V3.1 sans transformer la requête/réponse, les messages d'appel d'outil de l'assistant ne seront pas analysés—et vous verrez des erreurs dès que l'agent tentera de planifier/exécuter des outils ou de diffuser le résultat en streaming. ([Anthropic][1], [OpenRouter][2], [DeepSeek API Docs][3])

Que faire (correctifs rapides) :

1. Utiliser les transformateurs du routeur
   Activez les transformateurs de requête/réponse OpenRouter↔︎Anthropic dans votre routeur Claude Code afin que les `tool_calls` ⇄ `tool_use` soient mappés dans les deux sens. Le routeur communautaire populaire prend cela en charge explicitement ; vérifiez sa section « Transformation des Requêtes/Réponses » et les exemples de configuration. ([GitHub][4], [ClaudeLog][5])

2. Choisir le bon identifiant de modèle
   DeepSeek V3.1 a des identifiants OpenRouter spécifiques (par exemple, les entrées de la famille V3.1/V3). Un identifiant incorrect ou obsolète peut également provoquer des erreurs pendant les phases de streaming ou d'utilisation d'outils. Vérifiez l'id de modèle exact indiqué sur la page DeepSeek d'OpenRouter et utilisez-le dans le mappage de votre routeur. ([OpenRouter][6])

3. Restez en mode « chat » (pas « reasoner ») sauf si vous avez mappé ses champs
   Si vous essayez une variante de raisonnement qui diffuse des champs de raisonnement spéciaux, votre routeur doit les traduire—sinon Claude Code plantera. Préférez le modèle de chat standard ou désactivez la sortie « thinking » supplémentaire jusqu'à ce que votre transformateur la gère. (La documentation de DeepSeek met l'accent sur le style d'appel de fonction OpenAI ; c'est ce que vous devez mapper.) ([DeepSeek API Docs][3])

4. Mettre à jour vers la dernière version du routeur
   Les versions communautaires récentes ont ajouté des ajustements de compatibilité pour les fournisseurs non-Anthropic ; mettez à jour avant de tester. ([GitHub][4])

Pourquoi cela n'arrive qu'avec V3.1
V3.1 a ajouté par défaut des capacités d'agent/appel d'outil plus robustes. Cela augmente la probabilité que votre flux Claude Code rencontre les messages d'outil non traduits, ce qui est exactement là où l'incompatibilité de schéma fait mal. ([DeepSeek API Docs][7])

Si vous partagez le texte d'erreur exact, je peux indiquer l'extrait de transformateur précis à ajouter à votre configuration.

[1]: https://www.anthropic.com/engineering/claude-code-best-practices?utm_source=chatgpt.com "Claude Code: Best practices for agentic coding"
[2]: https://openrouter.ai/docs/features/tool-calling?utm_source=chatgpt.com "Tool & Function Calling"
[3]: https://api-docs.deepseek.com/guides/function_calling?utm_source=chatgpt.com "Function Calling"
[4]: https://github.com/musistudio/claude-code-router?utm_source=chatgpt.com "musistudio/claude-code-router"
[5]: https://claudelog.com/claude-code-mcps/claude-code-router/?utm_source=chatgpt.com "Claude Code Router"
[6]: https://openrouter.ai/models?q=deepseek&utm_source=chatgpt.com "Models: 'deepseek'"
[7]: https://api-docs.deepseek.com/news/news250821?utm_source=chatgpt.com "DeepSeek-V3.1 Release"