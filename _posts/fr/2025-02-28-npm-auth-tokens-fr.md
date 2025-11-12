---
audio: false
generated: true
lang: fr
layout: post
title: Utilisation des jetons d'authentification avec les URL du registre npm
translated: true
type: note
---

### Points Clés
- Il semble probable que pour utiliser un jeton d'authentification avec une URL de registre npm, vous le configuriez dans le fichier `.npmrc`, en associant le jeton à l'URL du registre.
- Les recherches suggèrent que la méthode standard consiste à ajouter `//registry.url.com/:_authToken=votre_jeton` dans le fichier `.npmrc`, où `registry.url.com` est l'URL du registre et `votre_jeton` est votre jeton d'authentification.
- Les preuves penchent en faveur de l'utilisation du fichier `.npmrc` pour l'authentification, car inclure le jeton directement dans l'URL (comme dans la requête HTTP) n'est pas standard pour npm et pourrait ne pas fonctionner.

### Réponse Directe

#### Aperçu
Pour utiliser un jeton d'authentification avec une URL de registre npm, vous le configurez généralement dans un fichier spécial appelé `.npmrc`. Ce fichier indique à l'outil en ligne de commande npm comment s'authentifier lors de l'accès à des registres de packages spécifiques, comme le registre public npm ou un registre privé. Voici comment procéder étape par étape, en gardant les choses simples pour les débutants.

#### Étapes de Configuration
1.  **Trouver l'URL du Registre** : Déterminez quel registre vous souhaitez utiliser, comme `registry.npmjs.org` pour le registre public npm ou une URL comme `privateregistry.com` pour un registre privé.
2.  **Obtenir Votre Jeton d'Auth** : Obtenez le jeton d'authentification auprès du fournisseur du registre, qui pourrait être un jeton d'accès personnel ou un autre type fourni par votre organisation.
3.  **Modifier le Fichier `.npmrc`** : Ouvrez ou créez le fichier `.npmrc`. Ce fichier peut se trouver dans votre dossier de projet pour des paramètres spécifiques au projet ou dans votre répertoire personnel (comme `~/.npmrc` sur les systèmes Unix) pour des paramètres globaux à l'utilisateur.
    - Ajoutez une ligne comme celle-ci : `//registry.url.com/:_authToken=votre_jeton`. Remplacez `registry.url.com` par votre URL de registre et `votre_jeton` par votre jeton réel.
    - Par exemple, pour le registre public npm, cela pourrait ressembler à : `//registry.npmjs.org/:_authToken=abc123`.
4.  **Sécuriser le Fichier** : Assurez-vous que le fichier `.npmrc` n'est lisible et modifiable que par vous pour garder votre jeton en sécurité. Sur les systèmes Unix, vous pouvez définir les permissions avec `chmod 600 ~/.npmrc`.
5.  **Vérifier le Fonctionnement** : Essayez d'exécuter une commande npm, comme `npm install`, pour voir si elle peut accéder au registre sans problème.

#### Détail Inattendu
Bien que vous puissiez penser que vous pouvez mettre le jeton d'authentification directement dans l'URL (comme `https://registry.url.com?token=votre_jeton`), ce n'est pas la méthode standard pour npm. Au lieu de cela, npm utilise le fichier `.npmrc` pour gérer l'authentification en arrière-plan, ce qui le rend plus sécurisé et plus facile à gérer.

Pour plus de détails, consultez la documentation officielle de npm sur la configuration du fichier `.npmrc` [ici](https://docs.npmjs.com/configuring-npm/npmrc).

---

### Note d'Enquête : Exploration Détaillée de l'Utilisation des Jetons d'Auth avec les URLs de Registre npm

Cette section fournit une analyse complète de la façon d'utiliser les jetons d'authentification avec les URLs de registre npm, développant la réponse directe avec un contexte supplémentaire, des détails techniques et des exemples. Elle vise à couvrir tous les aspects discutés dans la recherche, assurant une compréhension approfondie pour les utilisateurs de tous niveaux d'expertise.

#### Introduction à npm et à l'Authentification
Le Node Package Manager (npm) est un outil crucial pour les développeurs JavaScript, gérant les packages et les dépendances. Il interagit avec des registres de packages, tels que le registre public à [registry.npmjs.org](https://registry.npmjs.org), et des registres privés hébergés par des organisations. L'authentification est souvent requise pour les registres privés ou des actions spécifiques comme la publication de packages, et elle est généralement gérée via des jetons d'authentification stockés dans des fichiers de configuration.

Le fichier `.npmrc` est central pour la configuration de npm, permettant de personnaliser les paramètres comme les URLs de registre, les méthodes d'authentification, et plus encore. Il peut exister à plusieurs emplacements, comme par projet (dans la racine du projet), par utilisateur (dans le répertoire personnel, par exemple `~/.npmrc`), ou globalement (par exemple, `/etc/npmrc`). Ce fichier utilise un format INI, où les clés et les valeurs définissent le comportement de npm, y compris comment il s'authentifie auprès des registres.

#### Configuration des Jetons d'Auth dans `.npmrc`
Pour utiliser un jeton d'authentification avec une URL de registre spécifique, vous configurez le fichier `.npmrc` pour associer le jeton à ce registre. Le format standard est :

```
registry.url.com/:_authToken=votre_jeton
```

Ici, `registry.url.com` est l'URL de base du registre (par exemple, `registry.npmjs.org` pour le registre public ou `privateregistry.com` pour un registre privé), et `votre_jeton` est le jeton d'authentification fourni par le registre. La clé `:_authToken` indique qu'il s'agit d'une authentification basée sur un jeton, que npm utilise pour définir l'en-tête `Authorization` comme `Bearer votre_jeton` lors des requêtes HTTP vers le registre.

Par exemple, si vous avez un jeton `abc123` pour le registre public npm, votre entrée dans `.npmrc` serait :

```
registry.npmjs.org/:_authToken=abc123
```

Cette configuration garantit que toute commande npm interagissant avec `registry.npmjs.org` inclura le jeton pour l'authentification, permettant l'accès aux packages privés ou les capacités de publication, selon la portée du jeton.

#### Gestion des Packages à Périmètre (Scoped)
Pour les packages à périmètre (packages commençant par `@`, comme `@mycompany/mypackage`), vous pouvez spécifier un registre différent pour ce périmètre. Tout d'abord, définissez le registre pour le périmètre :

```
@mycompany:registry=https://mycompany.artifactory.com/
```

Ensuite, associez le jeton d'authentification à ce registre :

```
mycompany.artifactory.com/:_authToken=votre_jeton
```

Cette configuration achemine toutes les requêtes pour les packages `@mycompany` vers le registre privé spécifié et utilise le jeton fourni pour l'authentification. Ceci est particulièrement utile dans les environnements d'entreprise où les organisations hébergent leurs propres registres npm pour les packages internes.

#### Emplacement et Sécurité du Fichier `.npmrc`
Le fichier `.npmrc` peut se trouver à plusieurs endroits, chacun servant à des fins différentes :
- **Par projet** : Situé dans la racine du projet (par exemple, à côté du `package.json`). C'est idéal pour les configurations spécifiques au projet et remplace les paramètres globaux.
- **Par utilisateur** : Situé dans le répertoire personnel de l'utilisateur (par exemple, `~/.npmrc` sur Unix, `C:\Users\<NomUtilisateur>\.npmrc` sur Windows). Cela affecte toutes les opérations npm pour cet utilisateur.
- **Global** : Situé à `/etc/npmrc` ou spécifié par le paramètre `globalconfig`, généralement utilisé pour les paramètres système.

Étant donné que `.npmrc` peut contenir des informations sensibles comme des jetons d'authentification, la sécurité est cruciale. Le fichier doit être lisible et modifiable uniquement par l'utilisateur pour empêcher tout accès non autorisé. Sur les systèmes Unix, vous pouvez vous en assurer avec la commande `chmod 600 ~/.npmrc`, définissant les permissions en lecture/écriture uniquement pour le propriétaire.

#### Méthodes d'Authentification Alternatives
Bien que l'authentification par jeton soit courante, npm prend également en charge l'authentification basique, où vous pouvez inclure le nom d'utilisateur et le mot de passe dans le fichier `.npmrc` :

```
registry.url.com/:username=votre_nom_utilisateur
registry.url.com/:_password=votre_mot_de_passe
```

Cependant, pour des raisons de sécurité, l'authentification par jeton est préférée, car les jetons peuvent être révoqués et avoir des permissions limitées, réduisant les risques par rapport au stockage des mots de passe en clair.

#### Inclusion Directe dans l'URL : Est-ce Possible ?
La question mentionne "utiliser auth ou authtoken dans l'url du registre npm", ce qui pourrait suggérer d'inclure le jeton directement dans l'URL, comme `https://registry.url.com?token=votre_jeton`. Cependant, les recherches indiquent que ce n'est pas la pratique standard pour npm. La documentation de l'API du registre npm et les ressources associées, telles que [NPM registry authentication | Rush](https://rushjs.io/pages/maintainer/npm_registry_auth/), mettent l'accent sur l'utilisation du fichier `.npmrc` pour l'authentification, avec le jeton passé dans l'en-tête `Authorization` comme `Bearer votre_jeton`.

Tenter d'inclure le jeton dans l'URL en tant que paramètre de requête n'est pas pris en charge par le registre npm standard et pourrait ne pas fonctionner, car l'authentification est gérée au niveau de l'en-tête HTTP. Certains registres privés pourraient prendre en charge l'authentification personnalisée basée sur l'URL, mais cela n'est pas documenté pour le registre npm officiel. Par exemple, l'authentification basique permet des URLs comme `https://nom_utilisateur:mot_de_passe@registry.url.com`, mais celle-ci est dépréciée et moins sécurisée que les méthodes basées sur les jetons.

#### Exemples Pratiques et Cas d'Utilisation
Pour illustrer, considérez ces scénarios :

-   **Registre Public avec Jeton** : Si vous devez publier sur le registre public npm et avez un jeton, ajoutez :
    ```
    registry.npmjs.org/:_authToken=abc123
    ```
    Ensuite, exécutez `npm publish` pour télécharger votre package, et npm utilisera le jeton pour l'authentification.

-   **Registre Privé pour les Packages à Périmètre** : Pour une entreprise utilisant un registre privé à `https://company.registry.com` pour les packages `@company`, configurez :
    ```
    @company:registry=https://company.registry.com/
    company.registry.com/:_authToken=def456
    ```
    Maintenant, l'installation de `@company/mypackage` s'authentifiera auprès du registre privé en utilisant le jeton.

-   **Intégration CI/CD** : Dans les environnements d'intégration continue, stockez le jeton en tant que variable d'environnement (par exemple, `NPM_TOKEN`) et utilisez-le dans le fichier `.npmrc` dynamiquement :
    ```
    registry.npmjs.org/:_authToken=${NPM_TOKEN}
    ```
    Cette approche, détaillée dans [Using private packages in a CI/CD workflow | npm Docs](https://docs.npmjs.com/using-private-packages-in-a-ci-cd-workflow/), garantit que les jetons ne sont pas codés en dur et sont sécurisés.

#### Dépannage et Bonnes Pratiques
Si l'authentification échoue, vérifiez :
- L'URL du registre est correcte et accessible.
- Le jeton est valide et dispose des permissions nécessaires (par exemple, lecture pour l'installation, écriture pour la publication).
- Le fichier `.npmrc` se trouve au bon emplacement et dispose des permissions appropriées.

Les bonnes pratiques incluent :
- Ne jamais commettre `.npmrc` avec des jetons dans le contrôle de version ; l'ajouter à `.gitignore`.
- Utiliser des variables d'environnement pour les jetons dans les pipelines CI/CD pour améliorer la sécurité.
- Faire tourner régulièrement les jetons et révoquer ceux inutilisés pour minimiser les risques.

#### Analyse Comparative des Méthodes d'Authentification
Pour fournir un aperçu structuré, voici un tableau comparant l'authentification par jeton et l'authentification basique dans npm :

| **Méthode**               | **Configuration dans `.npmrc`**                                                          | **Sécurité**                          | **Cas d'Utilisation**               |
|---------------------------|------------------------------------------------------------------------------------------|---------------------------------------|-------------------------------------|
| Par jeton (Préférée)      | `registry.url.com/:_authToken=votre_jeton`                                               | Élevée (révocable, à portée limitée)  | Registres privés, CI/CD             |
| Authentification Basique   | `registry.url.com/:username=votre_nom_utilisateur`<br>`registry.url.com/:_password=votre_mot_de_passe` | Faible (mot de passe en clair)        | Systèmes hérités, registre public   |

Ce tableau met en évidence pourquoi l'authentification par jeton est recommandée, en particulier pour les workflows modernes.

#### Conclusion
Utiliser un jeton d'authentification avec une URL de registre npm implique principalement de configurer le fichier `.npmrc` pour associer le jeton au registre. Cette approche est standard, sécurisée et largement prise en charge, garantissant que npm peut authentifier les requêtes sans exposer les jetons dans les URLs. Bien que l'inclusion de jetons directement dans les URLs ne soit pas standard pour npm et puisse ne pas fonctionner, la méthode `.npmrc` fournit une solution robuste pour les interactions avec les registres publics et privés.

Pour aller plus loin, consultez la documentation officielle de npm sur [configuring npmrc](https://docs.npmjs.com/configuring-npm/npmrc) et [registry authentication](https://docs.npmjs.com/using-private-packages-in-a-ci-cd-workflow/).

### Citations Clés
- [NPM registry authentication Rush documentation](https://rushjs.io/pages/maintainer/npm_registry_auth/)
- [registry-auth-token npm package details](https://www.npmjs.com/package/registry-auth-token)
- [Globally configure NPM with token Stack Overflow question](https://stackoverflow.com/questions/38764714/globally-configure-npm-with-a-token-registry-to-a-specific-scope-organisation)
- [Configure authentication Artifact Registry Google Cloud](https://cloud.google.com/artifact-registry/docs/nodejs/authentication)
- [Official npm documentation for npmrc file](https://docs.npmjs.com/configuring-npm/npmrc)
- [Using private packages in CI/CD workflow npm Docs](https://docs.npmjs.com/using-private-packages-in-a-ci-cd-workflow/)