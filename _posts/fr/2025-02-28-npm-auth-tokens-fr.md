---
audio: false
lang: fr
layout: post
title: Utilisation des jetons d'authentification avec les URL du registre npm
translated: true
---

### Points Clés
- Il semble probable que pour utiliser un jeton d'authentification avec une URL de registre npm, vous le configuriez dans le fichier `.npmrc`, en associant le jeton à l'URL du registre.
- La recherche suggère que la méthode standard consiste à ajouter `//registry.url.com/:_authToken=your_token` dans le fichier `.npmrc`, où `registry.url.com` est l'URL du registre et `your_token` est votre jeton d'authentification.
- Les preuves penchent en faveur de l'utilisation du fichier `.npmrc` pour l'authentification, car l'inclusion du jeton directement dans l'URL (comme dans la requête HTTP) n'est pas standard pour npm et pourrait ne pas fonctionner.

### Réponse Directe

#### Aperçu
Pour utiliser un jeton d'authentification avec une URL de registre npm, vous configurez généralement cela dans un fichier spécial appelé `.npmrc`. Ce fichier indique à l'outil en ligne de commande npm comment s'authentifier lorsqu'il accède à des registres de paquets spécifiques, comme le registre npm public ou un registre privé. Voici comment procéder étape par étape, en gardant cela simple pour les débutants.

#### Étapes de Configuration
1. **Trouver l'URL du Registre** : Décidez quel registre vous souhaitez utiliser, comme `registry.npmjs.org` pour le registre npm public ou une URL comme `privateregistry.com` pour un registre privé.
2. **Obtenir Votre Jeton d'Authentification** : Obtenez le jeton d'authentification auprès du fournisseur du registre, qui pourrait être un jeton d'accès personnel ou un autre type fourni par votre organisation.
3. **Éditer le Fichier `.npmrc`** : Ouvrez ou créez le fichier `.npmrc`. Ce fichier peut se trouver dans le dossier de votre projet pour des paramètres spécifiques au projet ou dans votre répertoire personnel (comme `~/.npmrc` sur les systèmes Unix) pour des paramètres utilisateur.
   - Ajoutez une ligne comme celle-ci : `//registry.url.com/:_authToken=your_token`. Remplacez `registry.url.com` par votre URL de registre et `your_token` par votre jeton réel.
   - Par exemple, pour le registre npm public, cela pourrait ressembler à : `//registry.npmjs.org/:_authToken=abc123`.
4. **Sécuriser le Fichier** : Assurez-vous que le fichier `.npmrc` est uniquement lisible et modifiable par vous pour garder votre jeton en sécurité. Sur les systèmes Unix, vous pouvez définir les permissions avec `chmod 600 ~/.npmrc`.
5. **Vérifier que Cela Fonctionne** : Essayez d'exécuter une commande npm, comme `npm install`, pour voir si elle peut accéder au registre sans problème.

#### Détail Inattendu
Bien que vous puissiez penser pouvoir mettre le jeton d'authentification directement dans l'URL (comme `https://registry.url.com?token=your_token`), ce n'est pas la méthode standard pour npm. Au lieu de cela, npm utilise le fichier `.npmrc` pour gérer l'authentification en arrière-plan, ce qui est plus sécurisé et plus facile à gérer.

Pour plus de détails, consultez la documentation officielle npm sur la configuration du fichier `.npmrc` [ici](https://docs.npmjs.com/configuring-npm/npmrc).

---

### Note de Sondage : Exploration Détaillée de l'Utilisation de Jetons d'Authentification avec des URL de Registres npm

Cette section fournit une analyse complète de l'utilisation de jetons d'authentification avec des URL de registres npm, en approfondissant la réponse directe avec des contextes supplémentaires, des détails techniques et des exemples. Elle vise à couvrir tous les aspects discutés dans la recherche, assurant une compréhension approfondie pour les utilisateurs de tous niveaux d'expertise.

#### Introduction à npm et à l'Authentification
Le Node Package Manager (npm) est un outil crucial pour les développeurs JavaScript, gérant les paquets et les dépendances. Il interagit avec des registres de paquets, tels que le registre public à [registry.npmjs.org](https://registry.npmjs.org), et des registres privés hébergés par des organisations. L'authentification est souvent requise pour les registres privés ou des actions spécifiques comme la publication de paquets, et cela est généralement géré par des jetons d'authentification stockés dans des fichiers de configuration.

Le fichier `.npmrc` est central à la configuration de npm, permettant la personnalisation des paramètres comme les URL de registres, les méthodes d'authentification, et plus encore. Il peut exister à plusieurs endroits, tels que par projet (dans la racine du projet), par utilisateur (dans le répertoire personnel, par exemple `~/.npmrc`), ou globalement (par exemple, `/etc/npmrc`). Ce fichier utilise un format INI, où les clés et les valeurs définissent comment npm se comporte, y compris comment il s'authentifie avec les registres.

#### Configuration des Jetons d'Authentification dans `.npmrc`
Pour utiliser un jeton d'authentification avec une URL de registre spécifique, vous configurez le fichier `.npmrc` pour associer le jeton à ce registre. Le format standard est :

```
registry.url.com/:_authToken=your_token
```

Ici, `registry.url.com` est l'URL de base du registre (par exemple, `registry.npmjs.org` pour le registre public ou `privateregistry.com` pour un registre privé), et `your_token` est le jeton d'authentification fourni par le registre. La clé `:_authToken` indique qu'il s'agit d'une authentification basée sur un jeton, que npm utilise pour définir l'en-tête `Authorization` comme `Bearer your_token` lors de la réalisation de requêtes HTTP vers le registre.

Par exemple, si vous avez un jeton `abc123` pour le registre npm public, votre entrée `.npmrc` serait :

```
registry.npmjs.org/:_authToken=abc123
```

Cette configuration garantit que toute commande npm interagissant avec `registry.npmjs.org` inclura le jeton pour l'authentification, permettant l'accès aux paquets privés ou les capacités de publication, en fonction de la portée du jeton.

#### Gestion des Paquets à Portée
Pour les paquets à portée (paquets commençant par `@`, comme `@mycompany/mypackage`), vous pouvez spécifier un registre différent pour cette portée. Tout d'abord, définissez le registre pour la portée :

```
@mycompany:registry=https://mycompany.artifactory.com/
```

Ensuite, associez le jeton d'authentification à ce registre :

```
mycompany.artifactory.com/:_authToken=your_token
```

Cette configuration route toutes les requêtes pour les paquets `@mycompany` vers le registre privé spécifié et utilise le jeton fourni pour l'authentification. Cela est particulièrement utile dans les environnements d'entreprise où les organisations hébergent leurs propres registres npm pour les paquets internes.

#### Emplacement et Sécurité de `.npmrc`
Le fichier `.npmrc` peut être situé à plusieurs endroits, chacun servant des objectifs différents :
- **Par projet** : Situé dans la racine du projet (par exemple, à côté de `package.json`). Cela est idéal pour les configurations spécifiques au projet et remplace les paramètres globaux.
- **Par utilisateur** : Situé dans le répertoire personnel de l'utilisateur (par exemple, `~/.npmrc` sur Unix, `C:\Users\<Username>\.npmrc` sur Windows). Cela affecte toutes les opérations npm pour cet utilisateur.
- **Global** : Situé à `/etc/npmrc` ou spécifié par le paramètre `globalconfig`, généralement utilisé pour les paramètres système.

Étant donné que `.npmrc` peut contenir des informations sensibles comme des jetons d'authentification, la sécurité est cruciale. Le fichier doit être lisible et modifiable uniquement par l'utilisateur pour éviter un accès non autorisé. Sur les systèmes Unix, vous pouvez garantir cela avec la commande `chmod 600 ~/.npmrc`, définissant les permissions en lecture/écriture pour le propriétaire uniquement.

#### Méthodes d'Authentification Alternatives
Bien que l'authentification basée sur des jetons soit courante, npm prend également en charge l'authentification de base, où vous pouvez inclure le nom d'utilisateur et le mot de passe dans le fichier `.npmrc` :

```
registry.url.com/:username=your_username
registry.url.com/:_password=your_password
```

Cependant, pour des raisons de sécurité, l'authentification basée sur des jetons est préférée, car les jetons peuvent être révoqués et ont des permissions spécifiques, réduisant le risque par rapport au stockage de mots de passe en texte brut.

#### Inclusion Directe dans l'URL : Est-ce Possible ?
La question mentionne "utiliser auth ou authtoken dans l'URL du registre npm", ce qui pourrait suggérer d'inclure le jeton directement dans l'URL, comme `https://registry.url.com?token=your_token`. Cependant, la recherche indique que ce n'est pas la pratique standard pour npm. La documentation de l'API du registre npm et les ressources connexes, telles que [NPM registry authentication | Rush](https://rushjs.io/pages/maintainer/npm_registry_auth/), mettent l'accent sur l'utilisation du fichier `.npmrc` pour l'authentification, avec le jeton passé dans l'en-tête `Authorization` comme `Bearer your_token`.

Essayer d'inclure le jeton dans l'URL en tant que paramètre de requête n'est pas pris en charge par le registre npm standard et pourrait ne pas fonctionner, car l'authentification est gérée au niveau de l'en-tête HTTP. Certains registres privés pourraient prendre en charge une authentification basée sur l'URL personnalisée, mais cela n'est pas documenté pour le registre npm officiel. Par exemple, l'authentification de base permet des URL comme `https://username:password@registry.url.com`, mais cela est déprécié et moins sécurisé par rapport aux méthodes basées sur des jetons.

#### Exemples Pratiques et Cas d'Utilisation
Pour illustrer, considérons ces scénarios :

- **Registre Public avec Jeton** : Si vous devez publier sur le registre npm public et avez un jeton, ajoutez :
  ```
  registry.npmjs.org/:_authToken=abc123
  ```
  Ensuite, exécutez `npm publish` pour télécharger votre paquet, et npm utilisera le jeton pour l'authentification.

- **Registre Privé pour les Paquets à Portée** : Pour une entreprise utilisant un registre privé à `https://company.registry.com` pour les paquets `@company`, configurez :
  ```
  @company:registry=https://company.registry.com/
  company.registry.com/:_authToken=def456
  ```
  Maintenant, l'installation de `@company/mypackage` s'authentifiera avec le registre privé en utilisant le jeton.

- **Intégration CI/CD** : Dans les environnements d'intégration continue, stockez le jeton en tant que variable d'environnement (par exemple, `NPM_TOKEN`) et utilisez-le dans le fichier `.npmrc` de manière dynamique :
  ```
  registry.npmjs.org/:_authToken=${NPM_TOKEN}
  ```
  Cette approche, détaillée dans [Using private packages in a CI/CD workflow | npm Docs](https://docs.npmjs.com/using-private-packages-in-a-ci-cd-workflow/), garantit que les jetons ne sont pas codés en dur et sont sécurisés.

#### Dépannage et Meilleures Pratiques
Si l'authentification échoue, vérifiez :
- L'URL du registre est correcte et accessible.
- Le jeton est valide et dispose des permissions nécessaires (par exemple, lecture pour l'installation, écriture pour la publication).
- Le fichier `.npmrc` est à l'emplacement correct et dispose des permissions appropriées.

Les meilleures pratiques incluent :
- Ne jamais commettre `.npmrc` avec des jetons dans le contrôle de version ; ajoutez-le à `.gitignore`.
- Utiliser des variables d'environnement pour les jetons dans les pipelines CI/CD pour améliorer la sécurité.
- Faire tourner régulièrement les jetons et révoquer les jetons inutilisés pour minimiser les risques.

#### Analyse Comparative des Méthodes d'Authentification
Pour fournir un aperçu structuré, voici un tableau comparant l'authentification basée sur des jetons et l'authentification de base dans npm :

| **Méthode**          | **Configuration dans `.npmrc`**                          | **Sécurité**                     | **Cas d'Utilisation**                     |
|---------------------|-------------------------------------------------------|-----------------------------------|-----------------------------------|
| Basée sur des Jetons (Préférée) | `registry.url.com/:_authToken=your_token`            | Élevée (révocable, spécifique)         | Registres privés, CI/CD        |
| Authentification de Base| `registry.url.com/:username=your_username`<br>`registry.url.com/:_password=your_password` | Faible (mot de passe en texte brut)         | Systèmes hérités, registre public  |

Ce tableau met en évidence pourquoi l'authentification basée sur des jetons est recommandée, surtout pour les flux de travail modernes.

#### Conclusion
L'utilisation d'un jeton d'authentification avec une URL de registre npm implique principalement la configuration du fichier `.npmrc` pour associer le jeton au registre. Cette approche est standard, sécurisée et largement prise en charge, garantissant que npm peut authentifier les requêtes sans exposer les jetons dans les URL. Bien que l'inclusion de jetons directement dans les URL ne soit pas standard pour npm et pourrait ne pas fonctionner, la méthode `.npmrc` fournit une solution robuste pour les interactions avec les registres publics et privés.

Pour plus de lecture, consultez la documentation officielle npm sur [configurer npmrc](https://docs.npmjs.com/configuring-npm/npmrc) et [authentification du registre](https://docs.npmjs.com/using-private-packages-in-a-ci-cd-workflow/).

### Citations Clés
- [NPM registry authentication Rush documentation](https://rushjs.io/pages/maintainer/npm_registry_auth/)
- [registry-auth-token npm package details](https://www.npmjs.com/package/registry-auth-token)
- [Globally configure NPM with token Stack Overflow question](https://stackoverflow.com/questions/38764714/globally-configure-npm-with-a-token-registry-to-a-specific-scope-organisation)
- [Configure authentication Artifact Registry Google Cloud](https://cloud.google.com/artifact-registry/docs/nodejs/authentication)
- [Official npm documentation for npmrc file](https://docs.npmjs.com/configuring-npm/npmrc)
- [Using private packages in CI/CD workflow npm Docs](https://docs.npmjs.com/using-private-packages-in-a-ci-cd-workflow/)