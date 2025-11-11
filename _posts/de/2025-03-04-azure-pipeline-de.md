---
audio: false
generated: true
lang: de
layout: post
title: Verwenden von Azure DevOps Pipelines
translated: true
type: note
---

Unterteilen wir dies in zwei Teile: **Verwendung von Azure DevOps Pipelines** und **Erstellen von YAML für Pipelines**. Ich liefere eine klare, praktische Erklärung für beide.

---

### **Verwendung von Azure DevOps Pipelines**
Azure DevOps Pipelines ist ein CI/CD-Tool (Continuous Integration/Continuous Deployment), das das Erstellen, Testen und Bereitstellen von Code automatisiert. So beginnen Sie:

#### **1. Projekt einrichten**
- Melden Sie sich bei Azure DevOps (dev.azure.com) mit Ihrer Organisation an.
- Erstellen Sie ein neues Projekt (oder verwenden Sie ein bestehendes), indem Sie auf "Neues Projekt" klicken, einen Namen vergeben und die Sichtbarkeit (öffentlich/privat) festlegen.

#### **2. Code verbinden**
- Gehen Sie in Ihrem Projekt zu **Repos** und pushen Sie Ihren Code in ein Repository (GitHub, Azure Repos, Bitbucket usw.).
- Alternativ können Sie ein externes Repo unter **Pipelines > Neue Pipeline > Verbinden** verknüpfen und Ihre Quelle auswählen.

#### **3. Pipeline erstellen**
- Navigieren Sie zu **Pipelines** > **Builds** > **Neue Pipeline**.
- Wählen Sie Ihr Repo und Ihren Branch aus.
- Azure bietet zwei Optionen an:
  - **Klassischer Editor**: Ein GUI-basierter Ansatz (kein YAML erforderlich).
  - **YAML**: Eine code-basierte Pipeline (empfohlen für Flexibilität und Versionskontrolle).
- Wählen Sie für YAML "Starter-Pipeline" oder konfigurieren Sie sie aus einer vorhandenen Datei in Ihrem Repo.

#### **4. Pipeline definieren**
- Wenn Sie YAML verwenden, schreiben Sie eine `.yml`-Datei (z.B. `azure-pipelines.yml`) im Stammverzeichnis Ihres Repos. (Mehr dazu weiter unten.)
- Fügen Sie Trigger hinzu (z.B. Ausführung bei jedem Push zu `main`), Schritte (z.B. Build, Test) und Bereitstellungsziele.

#### **5. Ausführen und überwachen**
- Speichern und committen Sie die YAML-Datei (oder speichern Sie sie im Klassischen Editor).
- Klicken Sie auf **Ausführen**, um die Pipeline manuell zu starten, oder lassen Sie sie automatisch basierend auf Triggern laufen.
- Überprüfen Sie die Protokolle unter **Pipelines > Builds**, um den Fortschritt zu verfolgen oder Fehler zu beheben.

#### **6. Bereitstellen (Optional)**
- Fügen Sie eine **Release-Pipeline** (unter **Releases**) hinzu oder erweitern Sie Ihr YAML, um Bereitstellungen in Umgebungen wie Azure App Service, Kubernetes oder VMs durchzuführen.

---

### **Erstellen von YAML für Azure Pipelines**
YAML (Yet Another Markup Language) ist ein menschenlesbares Format, um Pipeline-Konfigurationen zu definieren. Hier ist ein Schnellkurs:

#### **Grundstruktur**
```yaml
trigger:
  - main  # Pipeline ausführen, wenn der 'main'-Branch aktualisiert wird

pool:
  vmImage: 'ubuntu-latest'  # Build-Agenten angeben (z.B. Ubuntu, Windows, macOS)

steps:
  - script: echo Hello, world!  # Ein einfacher Befehl
    displayName: 'Einzeiliges Skript ausführen'
```

- **`trigger`**: Definiert, wann die Pipeline läuft (z.B. bei Push zu `main`).
- **`pool`**: Gibt das VM-Image für den Build-Agenten an.
- **`steps`**: Listet die auszuführenden Aufgaben auf (Skripte, integrierte Tasks usw.).

#### **Häufige Elemente**
1. **Variablen**:
   ```yaml
   variables:
     buildConfiguration: 'Release'
   steps:
     - script: echo $(buildConfiguration)  # Gibt 'Release' aus
   ```

2. **Jobs** (Schritte gruppieren):
   ```yaml
   jobs:
   - job: Build
     steps:
       - script: echo Building...
   - job: Test
     steps:
       - script: echo Testing...
   ```

3. **Tasks** (vordefinierte Aktionen):
   ```yaml
   steps:
     - task: DotNetCoreCLI@2  # Beispiel: Ein .NET-Projekt erstellen
       inputs:
         command: 'build'
         projects: '**/*.csproj'
   ```

4. **Bedingungen**:
   ```yaml
   steps:
     - script: echo This runs only on main
       condition: eq(variables['Build.SourceBranch'], 'refs/heads/main')
   ```

5. **Stages** (für mehrphasige Pipelines):
   ```yaml
   stages:
   - stage: Build
     jobs:
       - job: BuildJob
         steps:
           - script: echo Building...
   - stage: Deploy
     dependsOn: Build
     jobs:
       - job: DeployJob
         steps:
           - script: echo Deploying...
   ```

#### **Praktisches Beispiel**
Hier ist eine Pipeline für eine Node.js-App:
```yaml
trigger:
  - main

pool:
  vmImage: 'ubuntu-latest'

steps:
  - task: NodeTool@0  # Node.js installieren
    inputs:
      versionSpec: '16.x'
    displayName: 'Node.js installieren'

  - script: |
      npm install
      npm run build
    displayName: 'Installieren und Erstellen'

  - task: CopyFiles@2  # Build-Artefakte kopieren
    inputs:
      contents: 'dist/**'
      targetFolder: '$(Build.ArtifactStagingDirectory)'

  - task: PublishBuildArtifacts@1  # Artefakte veröffentlichen
    inputs:
      pathToPublish: '$(Build.ArtifactStagingDirectory)'
      artifactName: 'dist'
```

#### **Tipps zum Erstellen von YAML**
- Verwenden Sie konsistente Einrückungen (2 Leerzeichen, keine Tabs).
- Validieren Sie die Syntax mit einem Editor (z.B. VS Code mit der "YAML"-Erweiterung).
- Konsultieren Sie das [Azure Pipelines YAML-Schema](https://learn.microsoft.com/en-us/azure/devops/pipelines/yaml-schema) für Optionen.
- Beginnen Sie einfach und fügen Sie Komplexität hinzu (z.B. Stages, Variablen), wenn nötig.

---

### **Nächste Schritte**
- **Probieren Sie es aus**: Erstellen Sie ein Repo, fügen Sie eine einfache `azure-pipelines.yml` wie oben hinzu und führen Sie sie in Azure DevOps aus.
- **Erfahren Sie mehr**: Lesen Sie die [offizielle Dokumentation](https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started) von Microsoft oder suchen Sie nach Beispiel-Pipelines auf GitHub.
- **Fragen Sie mich**: Wenn Sie auf ein Problem stoßen oder ein spezifisches Beispiel möchten (z.B. Python, Java), lassen Sie es mich wissen!

Worauf möchten Sie näher eingehen? Das Einrichten einer Pipeline, die YAML-Syntax oder etwas anderes?