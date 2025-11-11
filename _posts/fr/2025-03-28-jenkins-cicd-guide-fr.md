---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Guide Pratique Jenkins CI CD Maintenant
translated: true
type: note
---

Super — construisons ensemble un **guide Jenkins propre et complet** que vous pourrez utiliser au travail immédiatement. Je le rendrai facile à parcourir, sans tableaux trop larges.

# Qu'est-ce que Jenkins (et quand l'utiliser)

Jenkins est un serveur d'automatisation CI/CD auto-hébergé : vous le connectez à votre dépôt de code source, vous définissez des pipelines dans un `Jenkinsfile`, et il exécute les builds, tests et déploiements sur une ou plusieurs machines (« agents »). Les pipelines existent en deux variantes — **Declarative** (préférée) et **Scripted** — toutes deux documentées par le projet. ([Jenkins][1])

---

# Architecture de base (en termes simples)

* **Controller** : L'interface web, la file d'attente et le cerveau d'orchestration.
* **Agents/Nodes** : Machines (VM, conteneurs, bare metal) où les jobs s'exécutent réellement. Vous pouvez ajouter de nombreux agents et les étiqueter par capacité (ex: `java8`, `docker`). ([Jenkins][2])
* **Jobs/Pipelines** : Définitions du travail (idéalement stockées sous forme de code dans votre dépôt).
* **Plugins** : Ajoutent des fonctionnalités (credentials, stratégies d'authentification, agents cloud, JCasC, etc.).

---

# Installation et renforcement initial (liste de contrôle rapide)

1.  **Installez** sur Linux ou une image conteneur.
2.  **Reverse proxy + TLS** (Nginx/Apache, LB d'entreprise).
3.  **Manage Jenkins → Configure Global Security**
    * Définissez un vrai **security realm** (LDAP/OIDC/SAML/etc.).
    * Choisissez un mode d'**authorization** (voir ci-dessous). ([Jenkins][3])
4.  **Créez un utilisateur admin** (non partagé).
5.  **Restreignez les inscriptions**, désactivez l'écriture anonyme.
6.  **Uniquement le plugin Credentials** — ne jamais coder en dur les secrets dans les jobs. ([Jenkins][4])

---

# Contrôle d'accès (RBAC et portée des projets)

Jenkins inclut nativement la sécurité **Matrix-based** pour des permissions granulaires (build, configurer, supprimer, etc.). Utilisez-la pour les petites/moyennes instances ou comme base. ([Jenkins][3], [Jenkins Plugins][5])

Pour les organisations plus importantes et une isolation plus claire des équipes, installez **Role-based Authorization Strategy** (plugin "role-strategy") :

* Définissez des **Global roles** (ex: `admin`, `reader`).
* Définissez des **Project roles** limités par une regex d'item/dossier (ex: `team-alpha.*`).
* Assignez des utilisateurs/groupes aux rôles — ainsi les équipes ne voient et ne construisent que ce qu'elles possèdent. ([Jenkins Plugins][6])

> Astuce : Placez les pipelines de chaque équipe dans un **Folder**, puis appliquez les project roles au niveau du dossier. Combinez avec **Matrix** si vous avez besoin de réglages ultra-granulaires. ([Jenkins Plugins][5])

---

# Credentials & secrets (bonnes pratiques de sécurité)

* Ajoutez les secrets dans **Manage Jenkins → Credentials** (global ou limité à un dossier).
* Dans un Pipeline Declarative, référencez-les avec `credentials()` dans `environment`, ou liez-les à la demande avec `withCredentials { … }`.
* Préférez les tokens de courte durée provenant d'un vault ou d'un plugin fournisseur ; faites-les tourner régulièrement. ([Jenkins][4])

**Exemples (Declarative) :**

```groovy
pipeline {
  agent any
  environment {
    // injecte les variables d'env USER et PASS depuis une credential Username/Password
    CREDS = credentials('dockerhub-creds-id')
  }
  stages {
    stage('Login') {
      steps {
        sh 'echo $CREDS_USR | docker login -u $CREDS_USR --password-stdin'
      }
    }
  }
}
```

```groovy
pipeline {
  agent any
  stages {
    stage('Use Secret Text') {
      steps {
        withCredentials([string(credentialsId: 'slack-token', variable: 'SLACK_TOKEN')]) {
          sh 'curl -H "Authorization: Bearer $SLACK_TOKEN" https://slack.example/api'
        }
      }
    }
  }
}
```

La documentation pour l'utilisation et les liaisons est ici. ([Jenkins][7])

---

# Les agents à grande échelle

* Ajoutez des agents **Permanents** ou **Éphémères** ; étiquetez-les par capacité ; définissez la méthode de lancement (SSH, JNLP, cloud).
* Jenkins surveille le disque, le swap, les temp, le décalage d'horloge et peut mettre hors-ligne automatiquement les nodes non sains. Gardez les labels propres et utilisez `agent { label 'docker' }` dans les stages pour le routage. ([Jenkins][2])

---

# Des pipelines qui ne mordent pas (Jenkinsfile moderne)

**Declarative vs Scripted** : préférez **Declarative** — structure plus claire, garde-fous (`post`, `options`, `when`, `environment`, `input`, `parallel`). ([Jenkins][1])

**Exemple CI minimal :**

```groovy
pipeline {
  agent { label 'docker' }
  options { timestamps(); durabilityHint('PERFORMANCE_OPTIMIZED') }
  triggers { pollSCM('@daily') } // ou utilisez des webhooks dans votre SCM
  stages {
    stage('Checkout') { steps { checkout scm } }
    stage('Build')    { steps { sh './gradlew build -x test' } }
    stage('Test')     { steps { sh './gradlew test' } }
    stage('Package')  { when { branch 'main' } steps { sh './gradlew assemble' } }
  }
  post {
    always { junit 'build/test-results/test/*.xml'; archiveArtifacts 'build/libs/*.jar' }
    failure { mail to: 'team@example.com', subject: "Build failed ${env.JOB_NAME} #${env.BUILD_NUMBER}" }
  }
}
```

**Références clés :** Pipeline book, syntax reference, et step docs. ([Jenkins][1])

---

# Multibranch, GitHub/GitLab, et PRs

Utilisez **Multibranch Pipeline** ou un job GitHub/Bitbucket Organization pour que chaque branche/PR de dépôt avec un `Jenkinsfile` se construise automatiquement (via webhooks). Gardez le comportement des branches dans le code et évitez le "click-ops".

---

# Réutiliser à grande échelle : Shared Libraries

Lorsque vous répétez des étapes dans plusieurs dépôts, créez une **Jenkins Shared Library** (fonctions vars, étapes de pipeline) et importez-la dans le `Jenkinsfile` avec `@Library('your-lib') _`. Cela évite le copier-coller de pipelines et centralise les corrections.

---

# Configuration as Code (JCasC)

Traitez la configuration de votre controller comme du code : versionnez-la dans Git, révisez-la via des PRs, et amorcez de nouveaux controllers de manière reproductible.

* Installez le plugin **Configuration as Code**.
* Écrivez un YAML qui capture la sécurité globale, les lanceurs d'agents, les installateurs d'outils, les dossiers, les liaisons de credentials, etc.
* Chargez-le au démarrage (variable d'env `CASC_JENKINS_CONFIG`) ou depuis l'UI. ([Jenkins Plugins][8], [Jenkins][9])

**Un petit aperçu JCasC :**

```yaml
jenkins:
  systemMessage: "Jenkins managed by JCasC"
  authorizationStrategy:
    roleBased:
      roles:
        global:
          - name: "viewer"
            permissions:
              - "Overall/Read"
            assignments:
              - "devs"
  securityRealm:
    local:
      allowsSignup: false
      users:
        - id: "admin"
          password: "${ADMIN_PW}"
unclassified:
  location:
    url: "https://ci.example.com/"
```

Documentation officielle et page du plugin ci-dessus. ([Jenkins][9], [Jenkins Plugins][8])

---

# Plugins (utilisez-les judicieusement)

* **Indispensables** : Credentials, Matrix/Role-Strategy, Pipeline, Git, SSH, Email, Artifact Manager (ex: S3/GCS), Cloud agents (Kubernetes), JCasC.
* Gardez les plugins **minimaux & à jour**, épinglez les critiques, et testez les mises à jour dans un controller de staging. La documentation pratique des plugins se trouve sur jenkins.io et sur la page de chaque plugin. ([Jenkins][10])

---

# Observabilité et hygiène

* **Logs** : Utilisez le log recorder du controller + envoyez les logs vers ELK/CloudWatch.
* **Artifacts** : archivez seulement ce dont vous avez besoin.
* **JUnit** : publiez toujours les rapports de test ; cassez les builds sur les échecs de test.
* **Santé de la file d'attente** : surveillez la file d'attente des builds et l'utilisation des agents ; scalez les agents en conséquence.
* **Backups** : sauvegardez `$JENKINS_HOME` ou utilisez JCasC + des controllers éphémères.

---

# Gains de sécurité rapides

* Désactivez le CLI là où il n'est pas nécessaire ; préférez les jetons API.
* Séparez les comptes de **service** des humains.
* Secrets limités aux dossiers seulement ; n'echo jamais les secrets.
* Verrouillez les script approvals ; limitez les étapes `script` dans Declarative.
* Auditez les rôles régulièrement. Conseils dans la documentation sécurité de Jenkins. ([Jenkins][3])

---

# Améliorations typiques "Day-2"

* **Parallel** test shards pour réduire le temps de build.
* **Caching** (ex: cache Gradle/Maven sur les agents).
* **Docker-in-Docker** ou **Kubernetes agents** pour des images de build propres et reproductibles.
* **Quality gates** (lint, SAST/DAST) dans les premiers stages.
* Jobs de **Promotion** ou stages de déploiement multi-env avec conditions `when` et `input` manuel.

---

# Aide au dépannage

* Builds bloqués ? Vérifiez les logs des agents, l'espace disque du workspace, et le décalage d'horloge du node. Jenkins mettra hors-ligne automatiquement les nodes dépassant les seuils de santé. ([Jenkins][2])
* Credential introuvable ? Assurez-vous de la portée (dossier vs global) et du bon `credentialsId`. ([Jenkins][4])
* Problème d'authentification ? Re-vérifiez l'appariement realm ↔ authorization strategy (Matrix/Role-strategy). ([Jenkins][3], [Jenkins Plugins][6])
* Erreurs de syntaxe de pipeline ? Validez avec l'étape de validation **Declarative** / l'éditeur en ligne. ([Jenkins][11])

---

# Point de départ "golden" prêt à copier

```groovy
pipeline {
  agent { label 'k8s || docker || linux' }
  options { timestamps(); buildDiscarder(logRotator(numToKeepStr: '50')); ansiColor('xterm') }
  environment { JAVA_TOOL_OPTIONS = '-XX:+UseContainerSupport' }
  stages {
    stage('Checkout') { steps { checkout scm } }
    stage('Setup')    { steps { sh 'python -V || true' } }
    stage('Build')    { steps { sh './gradlew build -x test' } }
    stage('Test')     { steps { junit 'build/test-results/test/*.xml' } }
    stage('Package')  { when { branch 'main' } steps { sh './gradlew assemble' } }
    stage('Deploy')   { when { branch 'main' } steps { input 'Ship to staging?'; sh './scripts/deploy_staging.sh' } }
  }
  post {
    failure { echo "Failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}" }
    always  { archiveArtifacts artifacts: 'build/libs/*.jar', fingerprint: true }
  }
}
```

---

# Où lire plus (documentation pertinente)

* **Pipeline : overview & syntax** (Declarative vs Scripted, toutes les directives & étapes). ([Jenkins][1])
* **Security & authorization** (Matrix), plus **Role-Strategy plugin** pour RBAC. ([Jenkins][3], [Jenkins Plugins][5])
* **Agents & nodes** (ajout, santé, labels). ([Jenkins][2])
* **Credentials usage** (UI & aides/liaisons en Pipeline). ([Jenkins][4])
* **Configuration as Code (JCasC)** (concepts + plugin). ([Jenkins][9], [Jenkins Plugins][8])

---

Si vous le souhaitez, je peux adapter ceci à **votre configuration exacte** (GitHub vs GitLab, on-prem vs agents k8s, et votre modèle RBAC) et rédiger :

* un YAML de départ **JCasC**,
* un mapping **role-strategy** pour vos équipes, et
* un squelette de **Shared Library** pour des stages standardisés.

[1]: https://www.jenkins.io/doc/book/pipeline/?utm_source=chatgpt.com "Pipeline"
[2]: https://www.jenkins.io/doc/book/managing/nodes/?utm_source=chatgpt.com "Managing Nodes"
[3]: https://www.jenkins.io/doc/book/security/managing-security/?utm_source=chatgpt.com "Managing Security"
[4]: https://www.jenkins.io/doc/book/using/using-credentials/?utm_source=chatgpt.com "Using credentials"
[5]: https://plugins.jenkins.io/matrix-auth/?utm_source=chatgpt.com "Matrix Authorization Strategy"
[6]: https://plugins.jenkins.io/role-strategy/?utm_source=chatgpt.com "Role-based Authorization Strategy"
[7]: https://www.jenkins.io/doc/book/pipeline/jenkinsfile/?utm_source=chatgpt.com "Using a Jenkinsfile"
[8]: https://plugins.jenkins.io/configuration-as-code/?utm_source=chatgpt.com "Configuration as Code | Jenkins plugin"
[9]: https://www.jenkins.io/doc/book/managing/casc/?utm_source=chatgpt.com "Configuration as Code"
[10]: https://www.jenkins.io/doc/developer/publishing/documentation/?utm_source=chatgpt.com "Plugin Documentation"
[11]: https://www.jenkins.io/doc/pipeline/steps/pipeline-model-definition/?utm_source=chatgpt.com "Pipeline: Declarative"