---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Guide de Configuration des Tâches Jenkins
translated: true
type: note
---

### Configuration d'un Job dans Jenkins

Jenkins prend en charge différents types de jobs (également appelés projets), les plus courants étant les **projets Freestyle** (pour des builds simples) et les **projets Pipeline** (pour des workflows scriptés plus complexes utilisant un Jenkinsfile). Je vais décrire les étapes pour les deux ci-dessous. Ces étapes supposent que vous avez Jenkins installé et en cours d'exécution (par exemple, via Docker ou sur un serveur). Accédez au tableau de bord Jenkins à l'adresse `http://localhost:8080` (ou l'URL de votre serveur) et connectez-vous.

#### Étapes pour créer et configurer un projet Freestyle
Les projets Freestyle sont simples et utilisent une interface graphique pour configurer les étapes. Ils sont parfaits pour les débutants ou les tâches simples comme la construction et le test de code.

1.  **Créer un Nouveau Job** :
    *   Depuis le tableau de bord Jenkins, cliquez sur **New Item** dans la barre latérale gauche.
    *   Entrez un nom pour votre job (par exemple, "MyFirstBuild").
    *   Sélectionnez **Freestyle project** et cliquez sur **OK**.

2.  **Paramètres Généraux** :
    *   Ajoutez une description pour le job.
    *   Optionnellement, activez des fonctionnalités comme la suppression des anciens builds (par exemple, ne conserver que les 10 derniers builds) ou ajoutez des paramètres (par exemple, des paramètres de type chaîne ou choix pour une saisie utilisateur pendant les builds).

3.  **Gestion du Code Source** :
    *   Choisissez votre outil SCM, tel que Git.
    *   Entrez l'URL du dépôt (par exemple, un repo GitHub).
    *   Ajoutez des identifiants si nécessaire (par exemple, nom d'utilisateur/mot de passe ou clé SSH).
    *   Spécifiez les branches à construire (par exemple, `*/main`).

4.  **Déclencheurs de Build** :
    *   Sélectionnez comment le job démarre, par exemple :
        *   **Build periodically** (par exemple, syntaxe cron comme `H/5 * * * *` pour toutes les 5 minutes).
        *   **Poll SCM** pour vérifier les changements.
        *   **GitHub hook trigger** pour les webhooks de GitHub.
        *   **Build after other projects** pour enchaîner les jobs.

5.  **Environnement de Build** :
    *   Cochez les options comme **Delete workspace before build starts** pour repartir de zéro.
    *   Ajoutez des horodatages à la sortie console ou définissez des variables d'environnement.

6.  **Étapes de Build** :
    *   Cliquez sur **Add build step** et choisissez des actions comme :
        *   **Execute shell** (pour Linux/Mac : par exemple, `echo "Hello World"` ou exécuter des scripts).
        *   **Invoke top-level Maven targets** pour les builds Java.
        *   **Execute Windows batch command** pour Windows.
    *   Vous pouvez ajouter plusieurs étapes qui s'exécutent séquentiellement.

7.  **Actions Post-Build** :
    *   Ajoutez des actions comme :
        *   **Archive the artifacts** (par exemple, sauvegarder les fichiers JAR).
        *   **Publish JUnit test result report**.
        *   **Send email notifications** en cas de succès/échec.
        *   **Trigger another project**.

8.  **Sauvegarder et Exécuter** :
    *   Cliquez sur **Save**.
    *   De retour sur la page du job, cliquez sur **Build Now** pour le tester.
    *   Consultez la sortie console pour les détails.

#### Étapes pour créer et configurer un projet Pipeline
Les Pipelines sont définis comme du code (déclaratif ou scripté) et sont plus flexibles pour les workflows CI/CD.

1.  **Créer un Nouveau Job** :
    *   Depuis le tableau de bord, cliquez sur **New Item**.
    *   Entrez un nom et sélectionnez **Pipeline**, puis **OK**.

2.  **Paramètres Généraux** :
    *   Similaire à Freestyle : ajoutez une description, des paramètres, etc.

3.  **Déclencheurs de Build** :
    *   Les mêmes options que Freestyle (par exemple, webhooks, planifications).

4.  **Définition du Pipeline** :
    *   Choisissez **Pipeline script** pour du code inline ou **Pipeline script from SCM** pour récupérer depuis un dépôt (par exemple, un `Jenkinsfile` dans Git).
    *   Exemple de script de pipeline déclaratif :
        ```
        pipeline {
            agent any
            stages {
                stage('Build') {
                    steps {
                        echo 'Building...'
                        sh 'mvn clean install'  // Exemple de build Maven
                    }
                }
                stage('Test') {
                    steps {
                        echo 'Testing...'
                        sh 'mvn test'
                    }
                }
                stage('Deploy') {
                    steps {
                        echo 'Deploying...'
                    }
                }
            }
            post {
                always {
                    echo 'This runs always'
                }
            }
        }
        ```
    *   Ceci définit des étapes (Build, Test, Deploy) avec des actions.

5.  **Sauvegarder et Exécuter** :
    *   Sauvegardez le job.
    *   Lancez le build et surveillez la vue pipeline pour la progression des étapes.

Jenkins propose de nombreuses options dans chaque section, explorez-les en fonction de vos besoins (par exemple, pour la sécurité, ajoutez des identifiants ; pour le parallélisme, utilisez des agents/nodes). Si vous êtes nouveau, commencez par Freestyle et passez aux Pipelines pour la scalabilité.

### Intégrations logicielles et collaborations avec Jenkins

Jenkins est hautement extensible via des **plugins** (plus de 2000 disponibles), lui permettant de s'intégrer avec pratiquement n'importe quel outil de l'écosystème DevOps. Ces intégrations permettent de déclencher des builds, des déploiements, des tests, des notifications, et bien plus encore. Les plugins peuvent être installés via **Manage Jenkins > Manage Plugins**.

#### Intégrations courantes par catégorie
*   **Contrôle de Version** : Git, GitHub, GitLab, Bitbucket, SVN – Pour récupérer le code et déclencher des builds sur les événements de commit/push via des webhooks.
*   **Conteneurisation et Orchestration** : Docker (construire/pousser des images), Kubernetes (déployer sur des clusters), Helm – Pour les workflows basés sur les conteneurs.
*   **Fournisseurs de Cloud** : AWS (EC2, S3, Lambda via des plugins), Azure, Google Cloud – Pour déployer sur l'infrastructure cloud.
*   **Test et Qualité** : SonarQube (analyses de qualité de code), Selenium (tests UI), JUnit (tests unitaires), Cucumber (BDD) – Intégrez-les dans les étapes de build pour des tests automatisés.
*   **Déploiement et Surveillance** : Ansible, Terraform (infrastructure as code), Prometheus, Grafana – Pour l'orchestration et la surveillance post-build.
*   **Notifications et Collaboration** : Slack, Microsoft Teams, Email, Jira, Trello – Envoyez des alertes ou mettez à jour des tickets sur l'état du build.
*   **Outils de Build** : Maven, Gradle (Java), npm (Node.js), pip (Python) – Exécutez des builds pour divers langages.
*   **Sécurité** : OWASP Dependency-Check, Trivy (scan de vulnérabilités) – Recherchez les problèmes pendant l'intégration continue.
*   **Autres** : Artifactory/Nexus (dépôts d'artefacts), Zapier (intégrations no-code), Octopus Deploy (déploiements avancés).

Par exemple, avec GitHub, installez le plugin GitHub pour activer les déclencheurs par webhook. Avec Docker, utilisez le plugin Docker Pipeline pour construire des images dans les pipelines. Des plugins personnalisés peuvent même être créés pour des outils de niche.

Pour en explorer davantage, consultez l'index officiel des plugins. Mettez toujours à jour les plugins régulièrement pour la sécurité.

#### Références
*   [Working with projects - Jenkins](https://www.jenkins.io/doc/book/using/working-with-projects/)
*   [Jenkins - Setup Build Jobs - Tutorials Point](https://www.tutorialspoint.com/jenkins/jenkins_setup_build_jobs.htm)
*   [How to Create and Configure Build Jobs in Jenkins | BrowserStack](https://www.browserstack.com/guide/build-jobs-in-jenkins)
*   [Jenkins Build: Set Up Freestyle Project in Jenkins {Step-by-Step}](https://phoenixnap.com/kb/jenkins-build-freestyle-project)
*   [Managing Plugins - Jenkins](https://www.jenkins.io/doc/book/managing/plugins/)
*   [How to Integrate Jenkins with Different Tools and Technologies?](https://www.addwebsolution.com/blog/integrating-jenkins-with-other-tools-and-technologies)
*   [Jenkins Plugins](https://plugins.jenkins.io/)
*   [Jenkins](https://www.jenkins.io/)
*   [10 Of Our Favorite Jenkins Plugins | Octopus blog](https://octopus.com/blog/jenkins-ten-plugins)