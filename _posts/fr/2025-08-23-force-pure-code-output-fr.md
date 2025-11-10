---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Méthodes de production de code pure
translated: true
type: note
---

Compris — vous voulez que Claude Code (et vos workflows « router » qui l'appellent) produise **uniquement du code**, **sans commentaires en ligne/docstrings/explications**. Voici trois méthodes fiables pour appliquer cela, de la plus souple à la plus stricte. Pas de tableaux — juste des étapes directes.

---

# 1) Mettre la règle dans `CLAUDE.md` (global ou par projet)

Claude Code charge automatiquement les fichiers « mémoire » et les suit entre les sessions. Ajoutez une règle courte et explicite :

**Global (tous les projets) :** `~/.claude/CLAUDE.md`
**Par projet (versionnés) :** `./CLAUDE.md`

```md
# Règles de sortie
- Lors de la génération de code, produire uniquement du code.
- Ne pas inclure de commentaires en ligne, de commentaires en bloc, de docstrings ou de prose explicative, sauf demande explicite de ma part.
- Garder les messages concis ; si une explication est nécessaire, la placer après le bloc de code et seulement si je le demande.
```

Astuce : vous pouvez gérer ces mémoires avec `/memory` et en ajouter rapidement en commençant un message par `#` dans Claude Code. ([Anthropic][1])

---

# 2) Créer un **Style de Sortie personnalisé** qui interdit les commentaires (plus fort)

Les Styles de Sortie modifient le **prompt système** de Claude Code. Créez-en un et basculez dessus :

**Créer :**

```
/output-style:new Je veux un style de sortie qui produit toujours du code sans aucun commentaire ni docstring, ni explications.
```

Cela crée un fichier sous `~/.claude/output-styles/…`. Vous pouvez l'éditer pour garantir que la règle est sans ambiguïté :

```md
---
name: Code Uniquement (Sans Commentaires)
description: Émet toujours du code sans commentaires/docstrings ; pas d'explications sauf demande.
---
# Instructions
- Vous codez en mode « code uniquement ».
- N'incluez jamais de commentaires en ligne, de commentaires en bloc ou de docstrings.
- N'ajoutez pas de prose avant ou après le code, sauf demande explicite.

## Comportements Spécifiques
- Si une tâche implique des tests, produisez le(s) fichier(s) de test uniquement sous forme de code.
- Si une clarification est nécessaire, demandez brièvement, sans explications.
```

**Activer :**

```
/output-style "Code Uniquement (Sans Commentaires)"
```

(Les styles de sortie modifient directement le prompt système ; vous pouvez basculer avec `/output-style` à tout moment.) ([Anthropic][2])

---

# 3) Ajouter un prompt système supplémentaire à l'exécution (le plus fort / par session)

Si vous lancez Claude Code depuis la CLI ou un script, ajoutez :

```bash
claude --append-system-prompt "Toujours produire uniquement du code. Pas de commentaires en ligne, pas de commentaires en bloc, pas de docstrings, pas d'explications sauf demande explicite."
```

Vous pouvez aussi définir ceci via `/config` si vous préférez des paramètres de projet persistants. (Anthropic note que vous pouvez utiliser `--append-system-prompt` pour modifier le comportement de Claude Code.) ([Anthropic][3])

---

## Où mettre les règles à l'échelle du « router »

* Si votre « router Claude Code » correspond simplement à vos sessions Claude Code habituelles à travers les dépôts, préférez la **mémoire globale** (`~/.claude/CLAUDE.md`) ou un **Style de Sortie personnalisé** pour que la règle s'applique partout. ([Anthropic][1])
* Si vous lancez via un script, intégrez le flag `--append-system-prompt` pour que chaque exécution hérite de la règle. ([Anthropic][3])

---

## Garde-fous supplémentaires (optionnels mais utiles)

* Dans la mémoire du projet, ajoutez une ligne **« Violations »** pour que le modèle s'auto-contrôle : « Si vous êtes sur le point de produire des commentaires/docstrings, arrêtez-vous et supprimez-les. »
* Si vous voulez parfois des commentaires, ajoutez une annulation ponctuelle dans votre prompt : « Cette fois-ci uniquement, incluez des commentaires brefs. »

C'est tout. Si vous me dites comment vous lancez Claude Code (desktop, VS Code, JetBrains, ou terminal), je peux vous donner un snippet prêt à l'emploi pour cette configuration.

[1]: https://docs.anthropic.com/en/docs/claude-code/memory "Manage Claude's memory - Anthropic"
[2]: https://docs.anthropic.com/en/docs/claude-code/output-styles "Output styles - Anthropic"
[3]: https://docs.anthropic.com/en/docs/claude-code/settings "Claude Code settings - Anthropic"