---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast:free
title: Aperçu de Pivotal Cloud Foundry
translated: true
type: note
---

### Aperçu de Pivotal Cloud Foundry (PCF)
Pivotal Cloud Foundry (PCF), désormais intégré à VMware Tanzu suite à l'acquisition de Pivotal par VMware en 2019, est une distribution commerciale de la plateforme open source Cloud Foundry. C'est un Platform as a Service (PaaS) conçu pour simplifier le déploiement, la mise à l'échelle et la gestion d'applications cloud-native. PCF masque les complexités de l'infrastructure sous-jacente (IaaS), permettant aux développeurs de se concentrer sur le code plutôt que sur les serveurs, le réseau ou l'orchestration. Il est particulièrement populaire dans les secteurs réglementés comme la banque en raison de son accent sur la sécurité, la conformité et la portabilité.

PCF n'est pas un fournisseur de cloud autonome comme AWS, Azure ou GCP—c'est une couche qui peut s'exécuter *au-dessus* de ces fournisseurs IaaS, ainsi que dans des data centers sur site ou des clouds privés. Cela en fait un "système d'exploitation cloud" pour les applications.

### Conception et Architecture de PCF/Cloud Foundry
La conception de Cloud Foundry est modulaire, opinionated et construite autour des principes de la "12-factor app" pour un logiciel évolutif et maintenable. Voici une répartition de haut niveau :

#### Composants Principaux et Flux
1.  **Diego (Moteur d'exécution)** : Le cœur de PCF. Il remplace l'ancien système de conteneurs Garden par une couche d'orchestration moderne utilisant des conteneurs (basés sur des conteneurs Linux ou plus tard, Garden/Linux pour l'isolation). Diego gère les instances d'applications sur des "cellules" (machines virtuelles ou serveurs bare-metal). Il gère le staging (transformation du code source en applications exécutables, les droplets), le routage du trafic et la mise à l'échelle via des groupes de mise à l'échelle automatique.

2.  **Routage et Répartition de Charge** : Le Gorouter (un proxy inverse haute performance) dirige les requêtes entrantes vers les bonnes instances d'application en fonction des routes (par exemple, `app.example.com`). Il prend en charge les sessions persistantes (sticky sessions) et les contrôles de santé.

3.  **Marketplace de Services** : PCF fournit un modèle de "service broker" où les services managés (bases de données comme MySQL/PostgreSQL, files d'attente de messages comme RabbitMQ, ou intégrations tierces) sont catalogués. Les applications se "lient" à ces services pour obtenir automatiquement les informations d'identification et de connexion, sans codage en dur.

4.  **Sécurité et Identité** :
    - **UAA (User Account and Authentication)** : Gère l'authentification basée sur OAuth2, l'authentification unique (SSO) et le contrôle d'accès basé sur les rôles (RBAC).
    - Il s'intègre avec LDAP, SAML ou des fournisseurs d'identité d'entreprise, ce qui est crucial pour les banques.

5.  **Buildpacks et Runtimes** : PCF utilise des "buildpacks" (scripts préconfigurés) pour détecter et empaqueter des applications dans des langages comme Java, Node.js, Python, Go ou .NET. Il prend en charge les environnements polyglottes (multi-langages) sur une seule plateforme.

6.  **BOSH (Orchestrateur de Déploiement)** : L'outil sous-jacent pour installer et gérer PCF. Il utilise des manifests YAML pour déployer et mettre à jour les composants de manière idempotente (garantissant des états cohérents). BOSH gère l'approvisionnement des machines virtuelles, les mises à niveau et la surveillance.

7.  **Surveillance et Journalisation** : Les outils intégrés comme Loggregator (pour les journaux structurés) et Firehose (pour le streaming de métriques) alimentent des outils comme ELK Stack ou Splunk. Ops Metrics fournit l'observabilité intégrée.

#### Principes de Conception Clés
- **Autoservice et Centré sur le Développeur** : Les développeurs poussent les applications via la CLI `cf push`, et la plateforme gère le reste (mise à l'échelle, contrôles de santé, déploiements sans temps d'arrêt).
- **Multi-location (Multi-Tenancy)** : Plusieurs équipes ou organisations peuvent partager la plateforme de manière sécurisée via des "espaces" (spaces) et des quotas.
- **Mise à l'Échelle Horizontale** : Les applications montent en charge en répliquant les instances sur les cellules, avec une tolérance aux pannes intégrée (par exemple, si une cellule tombe en panne, Diego replanifie les tâches).
- **Piloté par API** : Tout est exposé via une API RESTful (Cloud Controller), permettant l'automatisation avec des outils comme Concourse CI/CD.
- **Extensibilité** : Prend en charge l'intégration de Kubernetes (via PKS, maintenant Tanzu Kubernetes Grid) pour l'orchestration de conteneurs, et des maillages de services comme Istio.

L'architecture est horizontalement évolutive et s'exécute sur des IaaS comme vSphere, AWS, Azure, GCP ou OpenStack. Un déploiement typique peut impliquer 10 à 20 machines virtuelles pour une configuration de production, avec une isolation via des politiques réseau et le chiffrement (TLS partout).

Les défis de conception incluent son héritage Java (pouvant être gourmand en ressources) et la courbe d'apprentissage pour les équipes d'exploitation, mais il est éprouvé depuis 2011.

### Pourquoi Certaines Banques Choisissent-Elles PCF ?
Les banques (par exemple, HSBC, Barclays, Capital One ou BBVA) choisissent souvent PCF pour son adéquation avec les besoins des services financiers. Voici pourquoi :

1.  **Conformité Réglementaire et Sécurité** :
    - PCF prend en charge des normes comme PCI-DSS, FIPS 140-2, GDPR et SOC 2. Il offre des fonctionnalités telles que le stockage etcd chiffré, la journalisation d'audit et des contrôles d'accès granulaires.
    - Les banques traitent des données sensibles ; l'isolation de PCF (par exemple, pas de noyaux partagés dans les configurations multi-locataires) et l'analyse des vulnérabilités réduisent les risques par rapport à une IaaS brute.

2.  **Stratégie Hybride et Multi-Cloud** :
    - De nombreuses banques ont des systèmes legacy sur site (par exemple, des mainframes) et souhaitent se moderniser sans une migration complète vers le cloud. PCF permet un "lift-and-shift" ou un refactoring progressif vers le cloud, en fonctionnant de manière cohérente sur les clouds privés/publics.
    - Il prend en charge les déploiements en air gap (déconnectés) pour les environnements de haute sécurité.

3.  **Productivité des Développeurs et Standardisation** :
    - PCF fournit un "golden path" pour les développeurs : une seule CLI, un seul workflow, quel que soit l'infrastructure backend. Cela accélère l'adoption des microservices, les pipelines CI/CD et les déploiements blue-green—critiques pour les applications de trading à faible latence ou de détection de fraude.
    - Les banques avec des équipes globales bénéficient de sa portabilité ; par exemple, une application développée aux États-Unis peut être déployée dans des data centers de l'UE sans retravail.

4.  **Écosystème de Fournisseurs et Support** :
    - Pivotal/VMware propose un support entreprise, incluant des SLA 24/7 et des certifications. Les banques apprécient les services managés (par exemple, PCF for PCF, maintenant Tanzu Application Service).
    - Ses racines open source signifient l'absence de verrouillage complet du fournisseur, mais avec un soutien commercial pour la stabilité.

Études de cas : Capital One a été un pionnier de PCF pour sa stratégie "cloud-first" en 2015, citant un time-to-market plus rapide (par exemple, déployer des applications en minutes contre des semaines). BBVA l'a utilisé pour conteneuriser des applications bancaires principales, réduisant les coûts de 50 %.

Toutes les banques n'utilisent pas PCF—il est plus courant dans les entreprises avec des charges de travail complexes et réglementées que dans les startups fintech.

### Pourquoi Ne Pas Choisir Directement Azure, AWS ou GCP ?
Les banques *utilisent* largement Azure/AWS/GCP, mais PCF est souvent superposé plutôt que remplacé. Les PaaS natifs des clouds publics (par exemple, AWS Elastic Beanstalk, Azure App Service, Google App Engine) sont excellents pour les applications simples, mais voici pourquoi PCF pourrait être préféré ou utilisé conjointement :

1.  **Éviter le Verrouillage Fournisseur** :
    - Les services natifs vous lient à un seul fournisseur (par exemple, AWS Lambda est exclusif à AWS). PCF s'exécute sur les trois (via des tiles/stems pour chaque cloud), permettant aux banques de changer de fournisseur ou de diversifier leurs paris (par exemple, AWS pour les États-Unis, Azure pour l'Europe en raison de la souveraineté des données).
    - Si une banque dépasse la tarification ou les fonctionnalités d'un cloud, les applications PCF peuvent migrer avec des changements minimes—contrairement aux formats propriétaires.

2.  **Cohérence entre les Environnements** :
    - Les clouds publics ont des services fragmentés (par exemple, AWS ECS vs. Azure AKS pour les conteneurs). PCF standardise la couche PaaS, offrant une expérience de développement uniforme. Ceci est vital pour les banques avec des équipes distribuées ou des acquisitions.
    - Configurations hybrides : 70 % des banques utilisent le cloud hybride (selon Gartner) ; PCF fait le pont entre VMware/vSphere sur site et les clouds publics de manière transparente.

3.  **Fonctionnalités Entreprises Avancées** :
    - Les PaaS natifs peuvent nécessiter l'assemblage de plusieurs services (par exemple, AWS API Gateway + ECS + RDS), entraînant une surcharge opérationnelle. PCF les regroupe (par exemple, via le Marketplace pour les brokers vers des équivalents RDS).
    - Mieux adapté à la migration des legacy : Les banques ont des monolithes COBOL/Java ; les buildpacks de PCF les prennent en charge sans réécriture complète.
    - Coût : Bien que les clouds publics soient moins chers pour les charges de travail irrégulières, PCF optimise l'utilisation des ressources (par exemple, via l'application de quotas), et les banques négocient des contrats entreprise.

4.  **Quand les Solutions Natives Gagnent** :
    - Du serverless pur ? Optez pour une solution native (par exemple, GCP Cloud Run pour les applications événementielles).
    - Si une banque est entièrement engagée sur un cloud (par exemple, AWS pour le ML via SageMaker), elle pourrait ignorer PCF pour tirer parti des intégrations profondes.
    - Inconvénients de PCF : Coût initial plus élevé (~ 100 000 $+ pour les licences), configuration plus complexe, et il est moins "managé" qu'un PaaS entièrement hébergé comme Heroku (maintenant Salesforce).

En pratique, de nombreuses banques utilisent un mix : PCF sur AWS pour les applications principales, les services natifs pour l'analytique (par exemple, Azure Synapse).

### Pourquoi Avoir PCF "Au Milieu" ?
PCF agit comme une couche d'abstraction (PaaS) entre vos applications (en haut) et l'IaaS (en bas). Pensez à la pile cloud :

- **IaaS (Fondation)** : AWS EC2, Azure VMs, GCP Compute Engine—fournit le calcul/stockage/réseau bruts.
- **PaaS (Milieu)** : PCF se situe ici, gérant le cycle de vie des applications sur l'IaaS. Il gère l'orchestration, la découverte de services et la mise à l'échelle afin que vous n'ayez pas à gérer directement les machines virtuelles.
- **Applications (Haut)** : Vos microservices, APIs, interfaces utilisateur.

**Avantages de l'Intermediaire** :
- **Simplification** : Les développeurs n'apprennent pas les APIs spécifiques au cloud ; poussez le code une fois, exécutez-le n'importe où.
- **Portabilité** : Passez d'AWS à GCP sans modifier l'application—clé pour les banques craignant le verrouillage ou ayant besoin de la redondance géographique.
- **Efficacité Opérationnelle** : Centralise la gouvernance (par exemple, politiques de sécurité, contrôles des coûts) sur tous les clouds.
- **Évolution** : A commencé comme un PaaS sur site ; s'intègre maintenant avec Kubernetes pour les charges de travail modernes.

En bref, PCF ne concurrence pas AWS/Azure/GCP—il les améliore pour la fiabilité entreprise. Si vous évaluez pour une banque, envisagez une pre-of-concept ; VMware propose des essais via Tanzu.

Pour des analyses plus approfondies, consultez la documentation de VMware ou le dépôt open source de Cloud Foundry. Si vous avez des spécificités (par exemple, un cas d'utilisation), je peux affiner cela !