---
audio: false
generated: true
lang: fr
layout: post
title: Problème d'extension Cline dans Visual Studio Code
translated: true
type: note
---

Il semble que vous rencontriez des problèmes avec l'extension Cline dans Visual Studio Code (VSCode) où elle ne parvient pas à détecter les fichiers nouvellement créés et ne reconnaît pas la fonctionnalité `@mention`. Compte tenu du contexte de Cline en tant qu'assistant de codage alimenté par l'IA, voici comment résoudre et potentiellement corriger ces problèmes :

---

### 1. Cline ne parvient pas à détecter un fichier nouvellement créé
Cline pourrait ne pas détecter un fichier nouvellement créé en raison de délais dans l'indexation de l'espace de travail, de problèmes de permissions ou d'un bogue dans le mécanisme de surveillance de fichiers de l'extension. Voici comment le corriger :

#### Étapes de dépannage :
- **Actualiser l'espace de travail** : Après avoir créé un nouveau fichier, actualisez manuellement l'espace de travail de VSCode pour vous assurer que Cline le récupère.
  - Appuyez sur `Ctrl+Shift+P` (ou `Cmd+Shift+P` sur Mac) pour ouvrir la Palette de commandes.
  - Tapez `Reload Window` et sélectionnez-la. Cela recharge VSCode et force Cline à ré-indexer l'espace de travail.
  
- **Vérifier la méthode de création du fichier** : Si vous créez des fichiers en dehors de VSCode (par exemple, via le terminal ou un autre éditeur), le surveillant de fichiers de VSCode pourrait ne pas les détecter immédiatement.
  - Essayez de créer le fichier directement dans VSCode (clic droit dans l'Explorateur > Nouveau fichier) et voyez si Cline le reconnaît.
  - Si vous utilisez un outil externe, assurez-vous que le fichier est enregistré dans le répertoire de l'espace de travail que Cline surveille.

- **Vérifier les permissions** : Cline nécessite des permissions de lecture/écriture pour interagir avec les fichiers.
  - Ouvrez les paramètres de Cline dans VSCode (via le volet Extensions ou la Palette de commandes : `Cline: Open Settings`).
  - Assurez-vous de lui avoir accordé l'autorisation de lire et de modifier les fichiers. Si une action vous est demandée lors d'une tâche, approuvez-la.

- **Vérifier l'instantané de l'espace de travail** : Cline prend des instantanés de votre espace de travail pour suivre les changements. S'il ne se met pas à jour :
  - Démarrez une nouvelle tâche dans Cline (cliquez sur le bouton "+" dans l'onglet Cline) et voyez s'il détecte le fichier après avoir ré-analysé l'espace de travail.
  - Alternativement, utilisez les boutons `Restore` ou `Compare` dans Cline pour forcer un rafraîchissement de l'espace de travail.

- **Mettre à jour Cline et VSCode** : Assurez-vous d'utiliser les dernières versions, car les bogues liés à la détection de fichiers ont pu être corrigés.
  - Mettez à jour VSCode : `Help > Check for Updates`.
  - Mettez à jour Cline : Allez dans Extensions dans VSCode, trouvez Cline, et cliquez sur le bouton de mise à jour si disponible.

- **Déboguer via les journaux** : Vérifiez les journaux de Cline pour des erreurs.
  - Ouvrez le panneau Output dans VSCode (`Ctrl+Shift+U` ou `Cmd+Shift+U`).
  - Sélectionnez "Cline" dans la liste déroulante pour voir ses journaux. Recherchez les messages concernant les échecs de détection de fichiers et traitez les problèmes spécifiques mentionnés (par exemple, erreurs de chemin).

#### Cause possible :
Cline s'appuie sur les APIs du système de fichiers de VSCode pour détecter les changements. Si le fichier n'est pas indexé ou si le surveillant est retardé, Cline ne le verra pas jusqu'à ce que l'espace de travail soit mis à jour.

---

### 2. Cline ne parvient pas à utiliser @mention
La syntaxe `@mention` dans Cline est généralement utilisée pour invoquer des outils ou des fonctionnalités spécifiques (par exemple, `@url` pour récupérer une page web ou `@problems` pour traiter les erreurs de l'espace de travail). Si cela ne fonctionne pas, cela pourrait être dû à une mauvaise configuration, un modèle non pris en charge ou une méprise sur la syntaxe.

#### Étapes de dépannage :
- **Vérifier la syntaxe** : Assurez-vous d'utiliser la syntaxe `@mention` correcte.
  - Exemples de la documentation de Cline :
    - `@url` : Récupère une URL et la convertit en markdown.
    - `@problems` : Inclut les erreurs/avertissements de l'espace de travail pour que Cline les corrige.
  - Tapez la `@mention` dans le champ de saisie de la tâche exactement comme documenté (sensible à la casse). Par exemple, `@Url` ou `@URL` pourrait ne pas fonctionner si `@url` est attendu.

- **Vérifier la prise en charge du modèle** : Tous les modèles d'IA que Cline prend en charge ne peuvent pas gérer la fonctionnalité `@mention`. Claude 3.5 Sonnet (recommandé par Cline) prend en charge les fonctionnalités agentiques, mais d'autres non.
  - Ouvrez les paramètres de Cline et confirmez votre fournisseur d'API et le modèle.
  - Si vous utilisez OpenRouter ou un autre fournisseur, passez à Claude 3.5 Sonnet et testez à nouveau.

- **Tester avec une tâche simple** : Démarrez une nouvelle tâche et essayez une `@mention` basique :
  - Exemple : "Corrige les problèmes listés dans @problems."
  - S'il ne répond pas, la fonctionnalité est peut-être désactivée ou mal configurée.

- **Activer les extensions d'outils** : Certaines `@mentions` (par exemple, des outils personnalisés comme `@jira` ou `@aws`) nécessitent un serveur Model Context Protocol (MCP).
  - Vérifiez si la `@mention` que vous utilisez correspond à un outil personnalisé. Si c'est le cas :
    - Demandez à Cline d'"ajouter un outil" (par exemple, "ajoute un outil qui récupère les tickets Jira") et suivez ses invites pour le configurer.
    - Redémarrez VSCode après avoir ajouté l'outil pour vous assurer qu'il est enregistré.

- **Inspecter la clé API** : Si `@mention` implique des requêtes externes (par exemple, `@url`), votre clé API pourrait ne pas avoir les permissions ou les crédits suffisants.
  - Vérifiez votre clé API dans les paramètres de Cline (par exemple, clé Anthropic ou OpenRouter).
  - Assurez-vous que votre compte dispose de fonds ou d'un accès à la fonctionnalité demandée.

- **Signaler un bogue** : Si les étapes ci-dessus échouent, il peut s'agir d'un bogue.
  - Visitez le GitHub de Cline (github.com/cline/cline) et vérifiez les problèmes ouverts.
  - Si aucun problème similaire n'existe, ouvrez-en un nouveau avec les détails : votre version de Cline, votre version de VSCode, le modèle utilisé et la `@mention` exacte tentée.

#### Cause possible :
La fonctionnalité `@mention` pourrait ne pas être entièrement implémentée pour votre configuration, ou il y a un décalage entre les capacités du modèle et le comportement attendu.

---

### Conseils généraux
- **Redémarrer VSCode** : Un redémarrage complet peut résoudre les problèmes temporaires avec les extensions.
- **Réinstaller Cline** : Si les problèmes persistent, désinstallez et réinstallez l'extension depuis le VSCode Marketplace.
- **Rejoindre la communauté de Cline** : Pour une aide en temps réel, rejoignez leur Discord (lien sur leur GitHub) et demandez dans le canal #support ou #contributors.

---

### Exemple de workflow pour tester les correctifs
1. Créez un nouveau fichier dans VSCode (par exemple, `test.txt`).
2. Rechargez la fenêtre (`Ctrl+Shift+P > Reload Window`).
3. Ouvrez Cline, démarrez une nouvelle tâche, et tapez : "Lis le contenu de test.txt et utilise @problems pour lister tous les problèmes."
4. Approuvez toutes les permissions et vérifiez si Cline détecte le fichier et traite la `@mention`.

Si ces étapes ne résolvent pas le problème, faites-moi savoir votre configuration spécifique (version de Cline, modèle, et quelle `@mention` vous essayez), et je creuserai plus profondément !