---
audio: false
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Suppression des Fourches GitHub Indésirables
translated: true
type: note
---

Compris. Version courte : vous ne pouvez pas supprimer directement le fork de quelqu'un d'autre. Mais vous pouvez (a) le lui demander, (b) purger les éléments sensibles et verrouiller les futures fuites, et (c) utiliser les voies officielles de GitHub (DMCA ou Support) si justifié. Voici un plan clair, sans tableaux, qui fonctionne bien pour les blogs personnels.

### 1) D'abord, contactez la personne ayant fait le fork (méthode la plus rapide)

Ouvrez une issue sur son fork ou envoyez-lui un email. Voici un modèle concis que vous pouvez copier-coller :

> Bonjour @tornadobaflocer — ce fork contient mes notes personnelles et mon historique d'activité. J'ai publié le repo uniquement pour utiliser le domaine `lzwjava.github.io`, et non pour une redistribution. Veuillez supprimer ce fork. Je rends la source privée et ne garderai publics que les assets compilés du site.
> Merci pour votre compréhension.

S'il le supprime, c'est terminé. Sinon, continuez.

### 2) Comprenez ce que GitHub fera ou ne fera pas

* Supprimer ou rendre privé votre repo **public** ne **supprime pas** les forks publics existants. Les forks publics restent publics et deviennent leur propre "réseau". ([Stack Overflow][1])
* Vous ne pouvez supprimer un fork que si vous en êtes un **administrateur** (ce qui n'est pas le cas ici). ([Stack Overflow][2])

### 3) Si le fork copie votre contenu protégé par le droit d'auteur sans autorisation

Vous pouvez déposer une demande de retrait DMCA auprès de GitHub. C'est la procédure officielle pour supprimer un contenu contrefait présent dans des forks. Lisez la politique et le guide "how to submit" ; ils expliquent les informations que vous devez inclure. ([GitHub Docs][3])

Conseil : Si votre repo n'avait **aucune licence**, le droit d'auteur par défaut s'applique, ce qui renforce une demande de retrait (les gens n'avaient aucun droit de réutilisation). Le DMCA reste valable même si vous aviez une licence permissive, mais c'est plus nuancé.

### 4) Empêchez les futurs forks d'exposer votre code source

Gardez le **domaine** public, mais gardez la **source** privée en séparant les repos :

* **Repo source privé** (ex. `blog-source`) : votre contenu Jekyll/Hugo, brouillons, notes, configurations.
* **Repo de déploiement public** nommé **`lzwjava.github.io`** : contient **uniquement le site compilé** (HTML/CSS/JS). Pas de brouillons, pas d'historique.

Les sites GitHub Pages sont publics même lorsque le repo est privé (sauf dans Enterprise Cloud avec les Pages privées). Donc pour un blog personnel, la configuration à deux repos "déploiement uniquement" est le modèle sûr. ([GitHub Docs][4])

Options de déploiement que vous pouvez utiliser aujourd'hui :

* Poussez la sortie `public/` ou `docs/` du générateur vers `lzwjava.github.io`. ([Quarto][5])
* Ou utilisez un workflow GitHub Actions dans `blog-source` qui construit et force-push la sortie vers la branche par défaut du repo `lzwjava.github.io`. (Docs : choisissez le flux "Publish from a branch" ou "Publish with Actions".) ([GitHub Docs][6])

### 5) Purgez tout élément sensible de l'historique (le vôtre et toute copie restante)

* Remplacez tous les tokens/clés exposés (considérez-les comme compromis).
* Réécrivez l'historique pour supprimer les fichiers/chemins sensibles avec `git filter-repo` (GitHub le recommande maintenant) ou BFG (plus rapide pour les cas courants). Puis faites un force-push. ([GitHub Docs][7])

Cela ne corrigera pas à lui seul les forks d'autres personnes, mais il nettoie votre repo canonique et étaye toute demande de retrait en montrant que le contenu est supprimé.

### 6) Renforcement optionnel

* Ajoutez une LICENSE claire (si vous souhaitez explicitement restreindre la réutilisation).
* Ajoutez un avertissement dans le README : "Ce repo existe uniquement pour la sortie compilée du site. **Ne forkez pas** la source ; elle est privée."
* Si vous hébergez un jour dans une **organisation**, vous pouvez désactiver le forking des repos privés au niveau de l'organisation et par repo (cela n'arrête pas le clonage du code public, mais aide pour les repos privés). ([GitHub Docs][8])

---

## Prochaines étapes concrètes (ordre qui fonctionne)

1. Demandez à @tornadobaflocer de supprimer le fork (utilisez le message ci-dessus).
2. Déplacez immédiatement votre source dans un nouveau repo **privé** (`blog-source`).
3. Faites de `lzwjava.github.io` un repo **public, déploiement uniquement** avec uniquement les fichiers compilés. Configurez Pages pour publier à partir de sa branche/dossier. ([GitHub Docs][6])
4. Réécrivez l'historique de votre ancien repo public pour supprimer les éléments sensibles, puis archivez-le ou supprimez-le. ([GitHub Docs][7])
5. S'il refuse et que vous voulez le faire supprimer, soumettez une **demande de retrait DMCA** à GitHub. ([GitHub Docs][9])

Si vous le souhaitez, je peux rédiger l'avis DMCA dans le format exact demandé par GitHub, et un workflow GitHub Actions minimal qui construit votre site à partir de `blog-source` et pousse uniquement les fichiers compilés vers `lzwjava.github.io`.

[1]: https://stackoverflow.com/questions/53052745/what-happens-to-the-forks-when-deleting-the-original-repository?utm_source=chatgpt.com "What happens to the forks when deleting the original repository?"
[2]: https://stackoverflow.com/questions/50280412/github-delete-a-fork-that-was-created-from-my-repo?utm_source=chatgpt.com "Github - Delete a fork that was created from my repo"
[3]: https://docs.github.com/articles/dmca-takedown-policy?utm_source=chatgpt.com "DMCA Takedown Policy"
[4]: https://docs.github.com/articles/creating-project-pages-manually?utm_source=chatgpt.com "Creating a GitHub Pages site"
[5]: https://quarto.org/docs/publishing/github-pages.html?utm_source=chatgpt.com "GitHub Pages"
[6]: https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site?utm_source=chatgpt.com "Configuring a publishing source for your GitHub Pages site"
[7]: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository?utm_source=chatgpt.com "Removing sensitive data from a repository"
[8]: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/managing-the-forking-policy-for-your-repository?utm_source=chatgpt.com "Managing the forking policy for your repository"
[9]: https://docs.github.com/en/site-policy/content-removal-policies/guide-to-submitting-a-dmca-takedown-notice?utm_source=chatgpt.com "Guide to Submitting a DMCA Takedown Notice"