---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Développement WebSphere avec Eclipse
translated: true
type: note
---

### Développer avec IBM WebSphere Application Server (WAS) dans Eclipse

IBM WebSphere Application Server (WAS) est un serveur d'applications Java EE, et Eclipse constitue un excellent IDE pour développer, assembler et déployer des applications sur celui-ci. L'outil principal pour cette intégration est **IBM WebSphere Application Server Developer Tools for Eclipse** (souvent abrégé en WDT). Ce plugin fournit des capacités de gestion de serveur, de création de projet, de déploiement et de débogage directement dans Eclipse. Il prend en charge à la fois le WAS traditionnel (par exemple, v8.5 et v9.x) et le profil Liberty plus léger.

#### Plugin Requis
- **IBM WebSphere Application Server Developer Tools for Eclipse** : C'est le plugin essentiel. Choisissez la version correspondant à votre runtime WAS (par exemple, les outils V8.5x ou V9.x). Il est disponible gratuitement sur l'Eclipse Marketplace et prend en charge les versions récentes d'Eclipse comme 2024-06 ou 2025-03.

Aucun autre plugin n'est strictement requis, mais pour un développement Java EE complet, assurez-vous que votre installation Eclipse inclut le Web Tools Platform (WTP), qui est standard dans le package Eclipse IDE for Java EE Developers.

#### Prérequis
- Eclipse IDE for Java EE Developers (version 2023-09 ou ultérieure recommandée pour la compatibilité).
- Runtime IBM WAS installé localement (traditionnel ou Liberty) pour les tests et le déploiement.
- Accès à Internet pour l'installation via le Marketplace (ou téléchargez les fichiers hors ligne).

#### Étapes d'Installation
Vous pouvez installer WDT via l'Eclipse Marketplace (méthode la plus simple), un site de mise à jour, ou des fichiers téléchargés. Redémarrez Eclipse après l'installation.

1. **Via l'Eclipse Marketplace** (Recommandé) :
   - Ouvrez Eclipse et allez dans **Help > Eclipse Marketplace**.
   - Recherchez "IBM WebSphere Application Server Developer Tools".
   - Sélectionnez la version appropriée (par exemple, pour V9.x ou V8.5x).
   - Cliquez sur **Install** et suivez les instructions. Acceptez les licences et redémarrez Eclipse une fois terminé.

2. **Via un Site de Mise à Jour** :
   - Allez dans **Help > Install New Software**.
   - Cliquez sur **Add** et entrez l'URL du site de mise à jour (par exemple, `https://public.dhe.ibm.com/ibmdl/export/pub/software/websphere/wasdev/updates/wdt/2025-03_comp/` pour les versions récentes — vérifiez la documentation IBM pour la dernière).
   - Sélectionnez les fonctionnalités WDT (par exemple, WebSphere Application Server V9.x Developer Tools) et installez.

3. **À partir de Fichiers Téléchargés** (Option Hors Ligne) :
   - Téléchargez l'archive ZIP depuis le [site IBM Developer](https://www.ibm.com/docs/en/wasdtfe?topic=installing-websphere-developer-tools) (par exemple, `wdt-update-site_<version>.zip`).
   - Extrayez-la dans un dossier local.
   - Dans Eclipse, allez dans **Help > Install New Software > Add > Archive** et sélectionnez le `site.xml` du site extrait.
   - Sélectionnez et installez les fonctionnalités souhaitées, puis redémarrez.

Après l'installation, vérifiez en allant dans **Window > Show View > Servers** — WAS devrait apparaître comme un type de serveur disponible.

#### Étapes de Base pour Développer et Déployer des Applications WAS
Une fois installé, vous pouvez créer, construire et exécuter des applications Java EE ciblant WAS.

1. **Créer un Nouveau Projet** :
   - Allez dans **File > New > Project**.
   - Sélectionnez **Web > Dynamic Web Project** (pour les applications web) ou **Java EE > Enterprise Application Project** (pour les EAR complets).
   - Dans l'assistant de projet, définissez le runtime cible sur votre installation WAS locale (s'il n'est pas listé, ajoutez-le via **Window > Preferences > Server > Runtime Environments > Add > WebSphere**).
   - Configurez les facettes pour la version Java EE (par exemple, 7 ou 8) correspondant à votre WAS.

2. **Configurer le Serveur** :
   - Ouvrez la vue **Servers** (**Window > Show View > Servers**).
   - Faites un clic droit dans la vue et sélectionnez **New > Server**.
   - Choisissez **WebSphere Application Server** (traditionnel ou Liberty) et pointez vers votre répertoire d'installation WAS local.
   - Terminez et démarrez le serveur (clic droit > Start).

3. **Développer Votre Application** :
   - Ajoutez des classes Java, des JSP, des servlets, des EJBs, etc., dans votre projet.
   - Utilisez les éditeurs d'Eclipse pour les configurations XML (par exemple, web.xml, ibm-web-bnd.xml pour les liaisons spécifiques à WAS).
   - Construisez le projet (**Project > Build Project**).

4. **Déployer et Exécuter** :
   - Clic droit sur votre projet > **Run As > Run on Server** (sélectionnez votre serveur WAS).
   - Eclipse publie l'application (publication automatique en mode développement) et démarre le serveur.
   - Déboguez en définissant des points d'arrêt et en exécutant en mode Debug.
   - Pour le déploiement à chaud (mises à jour rapides sans redémarrage), activez "Publish server changes immediately" dans la configuration du serveur.

5. **Conseils Avancés** :
   - Utilisez le profil Liberty pour des tests locaux plus rapides — il est inclus dans WDT et imite le comportement du WAS traditionnel.
   - Pour OSGi ou les microservices, créez des OSGi Bundle Projects via le plugin.
   - Surveillez les journaux dans la vue **Console** pendant l'exécution.

Si vous rencontrez des problèmes (par exemple, des erreurs de compatibilité), consultez la page des problèmes connus d'IBM ou assurez-vous que vos versions d'Eclipse et de WAS sont alignées.

#### Références
- [Aperçu des IBM WebSphere Application Server Developer Tools](https://www.ibm.com/docs/en/wasdtfe?topic=websphere-developer-tools-overview)
- [Eclipse Marketplace : Outils V9.x](https://marketplace.eclipse.org/content/ibm-websphere-application-server-v9x-developer-tools)
- [Eclipse Marketplace : Outils V8.5x](https://marketplace.eclipse.org/content/ibm-websphere-application-server-v85x-developer-tools)
- [Guide d'installation depuis IBM Docs](https://www.ibm.com/docs/en/wasdtfe?topic=installing-websphere-developer-tools)