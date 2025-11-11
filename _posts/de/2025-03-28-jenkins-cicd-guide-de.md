---
audio: false
generated: true
image: false
lang: de
layout: post
title: Praktischer Jenkins CI/CD-Leitfaden Jetzt
translated: true
type: note
---

Fantastisch – erstellen wir dir eine **saubere, End-to-End Jenkins-Anleitung**, die du sofort im Job verwenden kannst. Ich halte sie übersichtlich, ohne breite Tabellen.

# Was Jenkins ist (und wann man es verwendet)

Jenkins ist ein selbst gehosteter CI/CD-Automatisierungsserver: Du verbindest ihn mit deinem Source-Repo, definierst Pipelines in einer `Jenkinsfile`, und er führt Builds, Tests und Deployments auf einem oder mehreren Rechnern ("Agenten") aus. Pipelines gibt es in zwei Varianten – **Deklarativ** (bevorzugt) und **Skriptbasiert** – beide sind vom Projekt dokumentiert. ([Jenkins][1])

---

# Kernarchitektur (einfach erklärt)

* **Controller**: Die Web-UI, die Warteschlange und das Orchestrierungs-Hirn.
* **Agenten/Nodes**: Maschinen (VMs, Container, Bare Metal), auf denen Jobs tatsächlich laufen. Du kannst viele Agenten hinzufügen und sie nach Fähigkeiten labeln (z.B. `java8`, `docker`). ([Jenkins][2])
* **Jobs/Pipelines**: Definitionen von Arbeit (idealerweise als Code in deinem Repo gespeichert).
* **Plugins**: Fügen Funktionen hinzu (Credentials, Auth-Strategien, Cloud-Agenten, JCasC, etc.).

---

# Installation & Erstinbetriebnahme-Härtung (Schnell-Checkliste)

1.  **Installiere** auf Linux oder einem Container-Image.
2.  **Reverse Proxy + TLS** (Nginx/Apache, Corporate Load Balancer).
3.  **Manage Jenkins → Configure Global Security**
    *   Richte ein echtes **Security Realm** ein (LDAP/OIDC/SAML/etc.).
    *   Wähle einen **Authorization**-Modus (siehe unten). ([Jenkins][3])
4.  **Erstelle einen Admin**-Benutzer (nicht geteilt).
5.  **Beschränke Registrierungen**, deaktiviere anonymes Schreiben.
6.  **Nur Credentials-Plugin** – niemals Secrets hardcoded in Jobs. ([Jenkins][4])

---

# Zugriffskontrolle (RBAC und Projekt-Scoping)

Jenkins liefert **Matrix-basierte Sicherheit** für feingranulare Berechtigungen (bauen, konfigurieren, löschen, etc.). Verwende sie für kleine/mittlere Instanzen oder als Basis. ([Jenkins][3], [Jenkins Plugins][5])

Für größere Organisationen und sauberere Team-Isolierung, installiere **Role-based Authorization Strategy** ("role-strategy" Plugin):

*   Definiere **Globale Rollen** (z.B. `admin`, `reader`).
*   Definiere **Projektrollen**, begrenzt durch Item/Ordner-Regex (z.B. `team-alpha.*`).
*   Weise Benutzern/Gruppen Rollen zu – jetzt sehen/bauen Teams nur, was ihnen gehört. ([Jenkins Plugins][6])

> Tipp: Lege die Pipelines jedes Teams in einen **Ordner**, wende dann Projektrollen auf Ordnerebene an. Kombiniere mit **Matrix**, wenn du ultra-granulare Anpassungen brauchst. ([Jenkins Plugins][5])

---

# Credentials & Secrets (sichere Muster)

*   Füge Secrets unter **Manage Jenkins → Credentials** hinzu (global oder ordnerbeschränkt).
*   In der Deklarativen Pipeline, referenziere sie mit `credentials()` in `environment`, oder binde sie bei Bedarf mit `withCredentials { … }`.
*   Bevorzuge kurzlebige Tokens von einem Vault oder Provider-Plugin; rotiere sie regelmäßig. ([Jenkins][4])

**Beispiele (Deklarativ):**

```groovy
pipeline {
  agent any
  environment {
    // injects USER and PASS env vars from a Username/Password credential
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

Docs für Nutzung und Bindungen sind hier. ([Jenkins][7])

---

# Agenten im großen Maßstab

*   Füge **Permanente** oder **Kurzlebige** Agenten hinzu; label sie nach Fähigkeiten; setze die Startmethode (SSH, JNLP, Cloud).
*   Jenkins überwacht Disk, Swap, Temp, Clock Drift und kann ungesunde Nodes automatisch offline schalten. Halte Labels sauber und verwende `agent { label 'docker' }` in Stages für das Routing. ([Jenkins][2])

---

# Pipelines, die nicht beißen (moderne Jenkinsfile)

**Deklarativ vs. Skriptbasiert**: Bevorzuge **Deklarativ** – klarere Struktur, Schutzränder (`post`, `options`, `when`, `environment`, `input`, `parallel`). ([Jenkins][1])

**Minimales CI-Beispiel:**

```groovy
pipeline {
  agent { label 'docker' }
  options { timestamps(); durabilityHint('PERFORMANCE_OPTIMIZED') }
  triggers { pollSCM('@daily') } // or use webhooks in your SCM
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

**Wichtige Referenzen:** Pipeline-Buch, Syntax-Referenz und Step-Docs. ([Jenkins][1])

---

# Multibranch, GitHub/GitLab und PRs

Verwende **Multibranch Pipeline** oder einen GitHub/Bitbucket Organization-Job, damit jeder Repo-Branch/PR mit einer `Jenkinsfile` automatisch gebaut wird (via Webhooks). Halte Branch-Verhalten in Code und vermeide Click-Ops.

---

# Wiederverwendung im großen Maßstab: Shared Libraries

Wenn du Steps über Repos hinweg wiederholst, erstelle eine **Jenkins Shared Library** (Vars-Funktionen, Pipeline-Steps) und importiere sie in der `Jenkinsfile` mit `@Library('your-lib') _`. Dies verhindert Copy-Paste-Pipelines und zentralisiert Fixes.

---

# Configuration as Code (JCasC)

Behandle die Konfiguration deines Controllers wie Code: checke sie in Git ein, review sie via PRs und bootstrappe neue Controller reproduzierbar.

*   Installiere das **Configuration as Code** Plugin.
*   Schreibe YAML, das globale Sicherheit, Agent-Launcher, Tool-Installer, Ordner, Credential-Bindings, etc. erfasst.
*   Lade sie beim Start (Env-Var `CASC_JENKINS_CONFIG`) oder von der UI. ([Jenkins Plugins][8], [Jenkins][9])

**Kleiner JCasC-Vorgeschmack:**

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

Offizielle Docs & Plugin-Seite oben. ([Jenkins][9], [Jenkins Plugins][8])

---

# Plugins (verwende sie weise)

*   **Must-knows**: Credentials, Matrix/Role-Strategy, Pipeline, Git, SSH, Email, Artifact Manager (z.B. S3/GCS), Cloud-Agenten (Kubernetes), JCasC.
*   Halte Plugins **minimal & aktuell**, pinne kritische, und teste Updates in einem Staging-Controller. Praktische Plugin-Docs leben auf jenkins.io und der Seite jedes Plugins. ([Jenkins][10])

---

# Observability & Hygiene

*   **Logs**: Verwende Controller-Log-Recorder + sende Logs an ELK/CloudWatch.
*   **Artifacts**: archive nur, was du brauchst.
*   **JUnit**: publiziere immer Test-Reports; brich Builds bei Testfehlern.
*   **Queue Health**: beobachte die Build-Warteschlange und Agent-Auslastung; skaliere Agenten entsprechend.
*   **Backups**: backup `$JENKINS_HOME` oder verwende JCasC + kurzlebige Controller.

---

# Security Quick Wins

*   Deaktiviere die CLI, wo nicht benötigt; bevorzuge API-Tokens.
*   Trenne **Service**-Accounts von Menschen.
*   Nur ordner-beschränkte Secrets; gebe Secrets nie per echo aus.
*   Schränke Script-Approvals ein; beschränke `script`-Steps in Deklarativ.
*   Auditiere Rollen regelmäßig. Anleitung in Jenkins' Security-Docs. ([Jenkins][3])

---

# Typische "Day-2"-Verbesserungen

*   **Parallele** Test-Shards, um Build-Zeit zu kürzen.
*   **Caching** (z.B. Gradle/Maven Cache auf Agenten).
*   **Docker-in-Docker** oder **Kubernetes-Agenten** für saubere, reproduzierbare Build-Images.
*   **Quality Gates** (Lint, SAST/DAST) in frühen Stages.
*   **Promotion**-Jobs oder Multi-Env-Deploy-Stages mit `when`-Bedingungen und manuellem `input`.

---

# Troubleshooting Cheats

*   Hängende Builds? Prüfe Agent-Logs, Workspace-Disk und Node-Clock-Skew. Jenkins wird Nodes außerhalb der Health-Thresholds automatisch offline schalten. ([Jenkins][2])
*   Credential nicht gefunden? Stelle sicher, dass der Scope (Ordner vs. global) und die korrekte `credentialsId` stimmen. ([Jenkins][4])
*   Auth-Komisch? Verifiziere erneut die Paarung Realm ↔ Authorization Strategy (Matrix/Role-Strategy). ([Jenkins][3], [Jenkins Plugins][6])
*   Pipeline-Syntaxfehler? Validiere mit dem **Deklarativ**-Validator-Step / Online-Editor. ([Jenkins][11])

---

# Kopierfertiger "Goldener" Startpunkt

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

# Wo man mehr liest (High-Signal-Docs)

*   **Pipeline: Überblick & Syntax** (Deklarativ vs. Skriptbasiert, alle Direktiven & Steps). ([Jenkins][1])
*   **Sicherheit & Authorisierung** (Matrix), plus **Role-Strategy Plugin** für RBAC. ([Jenkins][3], [Jenkins Plugins][5])
*   **Agenten & Nodes** (Hinzufügen, Health, Labels). ([Jenkins][2])
*   **Credentials-Nutzung** (UI & Pipeline-Helper/Bindings). ([Jenkins][4])
*   **Configuration as Code (JCasC)** (Konzepte + Plugin). ([Jenkins][9], [Jenkins Plugins][8])

---

Falls du möchtest, kann ich das auf **dein exaktes Setup** zuschneiden (GitHub vs. GitLab, On-Prem vs. k8s-Agenten, und dein RBAC-Modell) und entwerfen:

*   eine **JCasC** YAML-Seed,
*   ein **Role-Strategy**-Mapping für deine Teams, und
*   ein **Shared Library**-Skelett für standardisierte Stages.

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