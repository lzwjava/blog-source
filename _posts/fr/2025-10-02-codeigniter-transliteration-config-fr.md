---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Guide de Configuration de la Translittération CodeIgniter
translated: true
type: note
---

### Objectif dans CodeIgniter
Il s'agit d'un fichier de configuration (nommé `foreign_characters.php` dans CodeIgniter) provenant de la bibliothèque **Text Helper**. Il est utilisé pour la **transliteration**, un processus qui convertit les caractères non-ASCII (accentués, avec signes diacritiques ou étrangers) en leurs équivalents ASCII les plus proches (par exemple, ä → ae, ñ → n). Cela est utile pour des tâches comme la génération de slugs d'URL, la création de chaînes de caractères sûres pour les bases de données, ou la compatibilité multiplateforme où les caractères spéciaux pourraient poser problème.

- Il fait partie des anciennes versions de CodeIgniter (pré-4.x) ; dans CI4, une fonctionnalité similaire a été déplacée vers des helpers ou des fonctions globales.
- Le tableau utilise des motifs regex (par exemple, `/ä|æ|ǽ/` correspond à ä, æ, ou ǽ) pour remplacer les caractères par des lettres anglaises simples.
- Les fonctions clés qui l'utilisent : `convert_accented_characters()` dans le Text Helper, qui parcourt ce tableau et effectue un `preg_replace`.

Ce n'est pas un code cœur du framework mais un utilitaire d'aide, souvent trouvé à `application/config/foreign_characters.php` dans les installations.

### Langues et Jeux de Caractères Représentés
Le tableau couvre les caractères de plusieurs scripts et langues pour permettre une translittération étendue. Voici une répartition par catégorie, incluant des exemples (provenant du code) et leurs langues/sources :

- **Latin (Europe occidentale)** : Signes diacritiques courants dans les langues romanes et germaniques.
  - Accents (par exemple, ÀÁÂ → A, àáâ → a) pour le français, l'espagnol, le portugais, le catalan.
  - Trémas (par exemple, Ä → Ae, ä → ae, Ü → Ue) pour l'allemand, le suédois.
  - Ligatures (par exemple, æ → ae pour le danois/norvégien, œ → oe pour le français).
  - Caractères spéciaux (par exemple, ñ → n pour l'espagnol, ł → l pour le polonais, þ → th pour l'islandais).

- **Grec (Hellénique)** : Lettres similaires au cyrillique pour l'alphabet grec.
  - Par exemple, Γ → G, Δ → Dj, Η → I, Ν → N, Ο → O, Ρ → R, Σ → S, Τ → T (grec ancien/moderne).

- **Cyrillique (Slave et Europe de l'Est)** : Basé sur le russe, l'ukrainien, le biélorusse, etc.
  - Bases : А → A, Б → B, В → V, Г → G, Д → D, Ж → Zh, З → Z, П → P, Р → R, С → S, Т → T, Ф → F, Х → Kh, Ц → Ts, Ч → Ch, Ш → Sh, Щ → Shch, Ъ/Ь (signes dur/doux) → supprimés (aucun équivalent), Ю → Yu, Я → Ya.
  - Suppléments : Ё/ё → Yo/yo (russe), Є/є → Ye/ye (ukrainien), Ї/ї → Yi/yi (ukrainien), Й → Y (variations en russe/ukrainien).

- **Autres Symboles/Caractères** :
  - ß → ss (S dur allemand "Eszett").
  - ½ → (généralement supprimé ou ignoré, pas dans ce tableau mais similaire).
  - Suppléments mathématiques/grecs : ξ → ks, π → p, β → v, μ → m, ψ → ps (utilisé pour la translittération scientifique).

Cela couvre environ 90 % des caractères non-ASCII courants dans le contenu web international. Si un caractère n'est pas listé, il peut être traité tel quel ou supprimé. L'ordre est important (traité via `preg_replace`), garantissant que les remplacements multi-caractères se produisent en premier. Pour les applications modernes, envisagez de privilégier le support UTF-8 par rapport à la translittération. Si vous avez besoin d'adapter ou d'étendre ceci, le fichier se trouve dans le helper.