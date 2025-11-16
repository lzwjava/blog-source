---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Jenkins Job Konfigurationsleitfaden
translated: true
type: note
---

### Konfigurieren eines Jobs in Jenkins

Jenkins unterstützt verschiedene Arten von Jobs (auch Projekte genannt), wobei die gebräuchlichsten **Freestyle-Projekte** (für einfache Builds) und **Pipeline-Projekte** (für komplexere, scriptbasierte Workflows mit Jenkinsfile) sind. Ich werde die Schritte für beide unten skizzieren. Diese setzen voraus, dass Jenkins installiert und ausgeführt wird (z. B. via Docker oder auf einem Server). Rufen Sie das Jenkins-Dashboard unter `http://localhost:8080` (oder der URL Ihres Servers) auf und melden Sie sich an.

#### Schritte zum Erstellen und Konfigurieren eines Freestyle-Projekts
Freestyle-Projekte sind unkompliziert und verwenden eine GUI zur Konfiguration der Schritte. Sie sind ideal für Anfänger oder einfache Aufgaben wie das Bauen und Testen von Code.

1.  **Neuen Job erstellen**:
    *   Klicken Sie im Jenkins-Dashboard in der linken Seitenleiste auf **New Item**.
    *   Geben Sie einen Namen für Ihren Job ein (z. B. "MyFirstBuild").
    *   Wählen Sie **Freestyle project** und klicken Sie auf **OK**.

2.  **Allgemeine Einstellungen**:
    *   Fügen Sie eine Beschreibung für den Job hinzu.
    *   Optional können Sie Funktionen aktivieren wie das Verwerfen alter Builds (z. B. nur die letzten 10 Builds behalten) oder Parameter hinzufügen (z. B. String- oder Auswahlparameter für Benutzereingaben während Builds).

3.  **Quellcode-Verwaltung**:
    *   Wählen Sie Ihr SCM-Tool, wie z. B. Git.
    *   Geben Sie die Repository-URL ein (z. B. ein GitHub-Repo).
    *   Fügen Sie bei Bedarf Credentials hinzu (z. B. Benutzername/Passwort oder SSH-Key).
    *   Geben Sie die zu bauenden Branches an (z. B. `*/main`).

4.  **Build-Auslöser**:
    *   Wählen Sie aus, wie der Job starten soll, z. B.:
        *   **Build periodically** (z. B. Cron-Syntax wie `H/5 * * * *` für alle 5 Minuten).
        *   **Poll SCM**, um auf Änderungen zu prüfen.
        *   **GitHub hook trigger** für Webhooks von GitHub.
        *   **Build after other projects**, um Jobs zu verketten.

5.  **Build-Umgebung**:
    *   Aktivieren Sie Optionen wie **Delete workspace before build starts** für einen sauberen Start.
    *   Fügen Sie Zeitstempel zur Konsolenausgabe hinzu oder setzen Sie Umgebungsvariablen.

6.  **Build-Schritte**:
    *   Klicken Sie auf **Add build step** und wählen Sie Aktionen wie:
        *   **Execute shell** (für Linux/Mac: z. B. `echo "Hello World"` oder Skripte ausführen).
        *   **Invoke top-level Maven targets** für Java-Builds.
        *   **Execute Windows batch command** für Windows.
    *   Sie können mehrere Schritte hinzufügen, die sequentiell ausgeführt werden.

7.  **Post-Build-Aktionen**:
    *   Fügen Sie Aktionen hinzu wie:
        *   **Archive the artifacts** (z. B. JAR-Dateien speichern).
        *   **Publish JUnit test result report**.
        *   **Send email notifications** bei Erfolg/Misserfolg.
        *   **Trigger another project**.

8.  **Speichern und Ausführen**:
    *   Klicken Sie auf **Save**.
    *   Klicken Sie auf der Job-Seite auf **Build Now**, um ihn zu testen.
    *   Sehen Sie sich die Konsolenausgabe für Details an.

#### Schritte zum Erstellen und Konfigurieren eines Pipeline-Projekts
Pipelines werden als Code (deklarativ oder scriptbasiert) definiert und sind flexibler für CI/CD-Workflows.

1.  **Neuen Job erstellen**:
    *   Klicken Sie im Dashboard auf **New Item**.
    *   Geben Sie einen Namen ein, wählen Sie **Pipeline** und dann **OK**.

2.  **Allgemeine Einstellungen**:
    *   Ähnlich wie bei Freestyle: Beschreibung, Parameter etc. hinzufügen.

3.  **Build-Auslöser**:
    *   Gleiche Optionen wie bei Freestyle (z. B. Webhooks, Zeitpläne).

4.  **Pipeline-Definition**:
    *   Wählen Sie **Pipeline script** für Inline-Code oder **Pipeline script from SCM**, um aus einem Repo zu pullen (z. B. eine `Jenkinsfile` in Git).
    *   Beispiel für ein deklaratives Pipeline-Script:
        ```
        pipeline {
            agent any
            stages {
                stage('Build') {
                    steps {
                        echo 'Building...'
                        sh 'mvn clean install'  // Beispiel Maven Build
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
    *   Dies definiert Stages (Build, Test, Deploy) mit Schritten.

5.  **Speichern und Ausführen**:
    *   Speichern Sie den Job.
    *   Bauen Sie ihn und überwachen Sie die Pipeline-Ansicht für den Fortschritt der Stages.

Jenkins bietet viele Optionen in jedem Abschnitt, erkunden Sie diese basierend auf Ihren Anforderungen (z. B. für Sicherheit: Credentials hinzufügen; für Parallelität: Agents/Nodes verwenden). Wenn Sie neu sind, beginnen Sie mit Freestyle und wechseln Sie für Skalierbarkeit zu Pipelines.

### Software-Integrationen und Zusammenarbeit mit Jenkins

Jenkins ist durch **Plugins** (über 2.000 verfügbar) hochgradig erweiterbar und kann mit nahezu jedem Tool im DevOps-Ökosystem integriert werden. Diese Integrationen ermöglichen das Auslösen von Builds, Deployments, Tests, Benachrichtigungen und mehr. Plugins können über **Manage Jenkins > Manage Plugins** installiert werden.

#### Häufige Integrationen nach Kategorie
*   **Versionskontrolle**: Git, GitHub, GitLab, Bitbucket, SVN – Zum Abrufen von Code und Auslösen von Builds bei Commits/Push-Events via Webhooks.
*   **Containerisierung und Orchestrierung**: Docker (Images bauen/pushen), Kubernetes (in Clustern deployen), Helm – Für containerbasierte Workflows.
*   **Cloud-Anbieter**: AWS (EC2, S3, Lambda via Plugins), Azure, Google Cloud – Für das Deployment in Cloud-Infrastrukturen.
*   **Testing und Qualität**: SonarQube (Code-Qualitäts-Scans), Selenium (UI-Testing), JUnit (Unit-Tests), Cucumber (BDD) – In Build-Schritte integrieren für automatisiertes Testen.
*   **Deployment und Monitoring**: Ansible, Terraform (Infrastructure as Code), Prometheus, Grafana – Für Orchestrierung und Monitoring nach dem Build.
*   **Benachrichtigungen und Zusammenarbeit**: Slack, Microsoft Teams, Email, Jira, Trello – Senden von Alerts oder Aktualisieren von Tickets basierend auf dem Build-Status.
*   **Build-Tools**: Maven, Gradle (Java), npm (Node.js), pip (Python) – Ausführen von Builds für verschiedene Sprachen.
*   **Sicherheit**: OWASP Dependency-Check, Trivy (Schwachstellen-Scanning) – Scannen auf Probleme während CI.
*   **Sonstige**: Artifactory/Nexus (Artifact-Repositories), Zapier (No-Code-Integrationen), Octopus Deploy (erweiterte Deployments).

Zum Beispiel: Installieren Sie mit GitHub das GitHub-Plugin, um Webhook-Trigger zu aktivieren. Mit Docker verwenden Sie das Docker Pipeline Plugin, um Images in Pipelines zu bauen. Für Nischen-Tools können sogar benutzerdefinierte Plugins erstellt werden.

Um mehr zu erkunden, sehen Sie sich den offiziellen Plugin-Index an. Aktualisieren Sie Plugins regelmäßig aus Sicherheitsgründen.

#### Referenzen
*   [Working with projects - Jenkins](https://www.jenkins.io/doc/book/using/working-with-projects/)
*   [Jenkins - Setup Build Jobs - Tutorials Point](https://www.tutorialspoint.com/jenkins/jenkins_setup_build_jobs.htm)
*   [How to Create and Configure Build Jobs in Jenkins | BrowserStack](https://www.browserstack.com/guide/build-jobs-in-jenkins)
*   [Jenkins Build: Set Up Freestyle Project in Jenkins {Step-by-Step}](https://phoenixnap.com/kb/jenkins-build-freestyle-project)
*   [Managing Plugins - Jenkins](https://www.jenkins.io/doc/book/managing/plugins/)
*   [How to Integrate Jenkins with Different Tools and Technologies?](https://www.addwebsolution.com/blog/integrating-jenkins-with-other-tools-and-technologies)
*   [Jenkins Plugins](https://plugins.jenkins.io/)
*   [Jenkins](https://www.jenkins.io/)
*   [10 Of Our Favorite Jenkins Plugins | Octopus blog](https://octopus.com/blog/jenkins-ten-plugins)