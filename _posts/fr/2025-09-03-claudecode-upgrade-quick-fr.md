---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Mettez à Jour le Code de Claude Rapidement Dès Maintenant
translated: true
type: note
---

Si vous cherchez à **mettre à niveau Claude Code**, l'agent de codage en ligne de commande d'Anthropic, voici comment procéder – et ainsi bénéficier des dernières fonctionnalités comme les modes d'apprentissage et les sous-agents personnalisés qui fonctionnent parfaitement.

---

### Comment mettre à niveau Claude Code

1.  **Vérifiez votre version actuelle**
    Exécutez :

    ```
    claude --version
    ```

    Cela vous permet de voir la version que vous utilisez actuellement.

2.  **Mettez à jour via npm**
    La méthode de mise à niveau la plus simple est :

    ```
    npm install -g @anthropic-ai/claude-code@latest
    ```

    Cela télécharge la dernière version depuis npm.
    Des utilisateurs sur Reddit rapportent que cela a corrigé des bugs et amélioré la réactivité. L'un d'eux a écrit :

    > « Après la mise à jour vers la dernière version (1.0.18), c'est le jour et la nuit – il semble bien plus intelligent et réactif. »
    > ([Reddit][1], [Anthropic][2])

3.  **Alternativement, utilisez le programme d'installation natif (Bêta)**
    Si vous préférez un binaire autonome (plutôt que npm), essayez :

    ```
    curl -fsSL https://claude.ai/install.sh | bash -s latest
    ```

    (Sur Windows, utilisez la version PowerShell)
    ([Anthropic][3])

4.  **Vérifiez la mise à jour**
    Après l'installation, redémarrez votre terminal et exécutez à nouveau `claude --version` pour confirmer que la nouvelle version est active.

5.  **Dépannage des problèmes d'installation**
    Si vous rencontrez des problèmes, essayez de désinstaller d'abord :

    ```
    npm uninstall -g @anthropic-ai/claude-code
    npm install -g @anthropic-ai/claude-code
    ```

    Certains utilisateurs ont constaté que cette séquence résolvait les problèmes de mise à jour. ([Anthropic][4], [Reddit][1], [Anthropic][5], [The Verge][6])

---

### Quoi de neuf dans les dernières mises à jour ?

#### Modes d'apprentissage

Anthropic a récemment ajouté deux nouveaux styles d'apprentissage dans Claude Code : **« Explicatif »** et **« Apprentissage »**. Ceux-ci vous aident à comprendre le raisonnement derrière le code généré plutôt que de simplement vous donner des solutions. Pour les activer :

1.  Assurez-vous d'avoir mis à jour Claude Code.
2.  Exécutez `/output-styles` dans votre session Claude Code.
3.  Choisissez entre le style **Par défaut**, **Explicatif** ou **Apprentissage**.
    Cette fonctionnalité a été lancée le **14 août 2025**. ([Tom's Guide][7])

#### Sous-agents personnalisés

Claude Code prend désormais en charge les **sous-agents** – des assistants IA spécialisés conçus pour des tâches spécifiques (par exemple, correction de bugs, refactorisation, documentation). Vous pouvez définir des prompts système, des autorisations d'outils et des fenêtres de contexte différentes pour chacun.
Pour en configurer un :

1.  Exécutez `/agents`
2.  Choisissez « Créer un nouvel agent » (au niveau utilisateur ou projet)
3.  Définissez son comportement, les outils autorisés et enregistrez-le
    Les sous-agents aident à garder votre flux de travail plus propre, plus concentré et conscient du contexte. ([Anthropic][8])

---

### Récapitulatif rapide (Pas de tableaux, juste des étapes claires)

*   **Pour mettre à niveau** :

    ```
    npm install -g @anthropic-ai/claude-code@latest
    ```

    ou utilisez l'installation native avec `curl | bash -s latest`.

*   **Activer les Modes d'Apprentissage** :

    *   Mettez à jour
    *   Dans Claude Code : exécutez `/output-styles` et choisissez votre mode.

*   **Créer des Sous-agents** :

    *   Dans Claude Code : exécutez `/agents`
    *   Personnalisez l'accès aux outils, le prompt système et le comportement.

---

### Dernières réflexions

Mettre à niveau Claude Code est simple – utilisez npm ou le programme d'installation natif, vérifiez que vous êtes sur la dernière version, puis explorez les nouvelles fonctionnalités des **modes d'apprentissage** et des **sous-agents**. Ces ajouts font évoluer Claude Code d'un simple assistant de codage vers quelque chose de plus proche d'un partenaire pédagogique et d'un collaborateur agentique dans votre flux de travail de développement.

Si vous souhaitez de l'aide pour créer votre premier sous-agent ou pour utiliser efficacement le mode d'apprentissage, je serais ravi de vous guider !

[1]: https://www.reddit.com/r/ClaudeAI/comments/1l8gbfo/dont_forget_to_update_your_claude_cli_it_makes_a/?utm_source=chatgpt.com "N'oubliez pas de mettre à jour votre CLI Claude ! Cela fait une énorme ..."
[2]: https://www.anthropic.com/solutions/agents?utm_source=chatgpt.com "Claude Agents | Solutions IA Intelligentes \ Anthropic"
[3]: https://docs.anthropic.com/en/docs/claude-code/quickstart?utm_source=chatgpt.com "Démarrage rapide - Claude Code"
[4]: https://docs.anthropic.com/en/docs/claude-code/settings?utm_source=chatgpt.com "Paramètres de Claude Code"
[5]: https://docs.anthropic.com/en/docs/claude-code/overview?utm_source=chatgpt.com "Vue d'ensemble de Claude Code"
[6]: https://www.theverge.com/2024/11/25/24305774/anthropic-model-context-protocol-data-sources?utm_source=chatgpt.com "Anthropic lance un outil pour connecter les systèmes IA directement aux ensembles de données"
[7]: https://www.tomsguide.com/ai/claudes-new-learning-modes-take-on-chatgpts-study-mode-heres-what-they-do?utm_source=chatgpt.com "Les nouveaux 'modes d'apprentissage' de Claude rivalisent avec le Mode Étude de ChatGPT - voici ce qu'ils font"
[8]: https://docs.anthropic.com/en/docs/claude-code/sub-agents?utm_source=chatgpt.com "Sous-agents"