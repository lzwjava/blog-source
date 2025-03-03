---
audio: false
generated: true
lang: de
layout: post
title: Mit Azure DevOps Pipelines arbeiten
translated: true
---

Lass uns das in zwei Teile aufteilen: **Verwendung von Azure DevOps Pipelines** und **Schreiben von YAML für Pipelines**. Ich werde eine klare, praktische Erklärung für beide bereitstellen.

---

### **Wie man Azure DevOps Pipelines verwendet**
Azure DevOps Pipelines ist ein CI/CD-Tool (Continuous Integration/Continuous Deployment), das das Erstellen, Testen und Bereitstellen von Code automatisiert. Hier ist, wie man beginnt:

#### **1. Ein Projekt einrichten**
- Melden Sie sich bei Azure DevOps (dev.azure.com) mit Ihrer Organisation an.
- Erstellen Sie ein neues Projekt (oder verwenden Sie ein bestehendes), indem Sie auf "Neues Projekt" klicken, ihm einen Namen geben und die Sichtbarkeit (öffentlich/privat) festlegen.

#### **2. Ihren Code verbinden**
- Gehen Sie zu **Repos** in Ihrem Projekt und schieben Sie Ihren Code in ein Repository (GitHub, Azure Repos, Bitbucket, etc.).
- Alternativ können Sie ein externes Repository unter **Pipelines > Neue Pipeline > Verbinden** verknüpfen und Ihre Quelle auswählen.

#### **3. Eine Pipeline erstellen**
- Navigieren Sie zu **Pipelines > Builds > Neue Pipeline**.
- Wählen Sie Ihr Repository und Ihren Branch aus.
- Azure bietet zwei Optionen:
  - **Klassischer Editor**: Ein GUI-basierter Ansatz (kein YAML erforderlich).
  - **YAML**: Eine codebasierte Pipeline (empfohlen für Flexibilität und Versionskontrolle).
- Für YAML wählen Sie "Starter-Pipeline" oder konfigurieren Sie aus einer vorhandenen Datei in Ihrem Repository.

#### **4. Die Pipeline definieren**
- Wenn Sie YAML verwenden, schreiben Sie eine `.yml`-Datei (z. B. `azure-pipelines.yml`) im Stammverzeichnis Ihres Repositories. (Mehr dazu weiter unten.)
- Fügen Sie Auslöser (z. B. bei jedem Push an `main`), Schritte (z. B. Build, Test) und Bereitstellungsziele hinzu.

#### **5. Ausführen und Überwachen**
- Speichern und committen Sie die YAML-Datei (oder speichern Sie im klassischen Editor).
- Klicken Sie auf **Ausführen**, um die Pipeline manuell auszulösen, oder lassen Sie sie basierend auf Auslösern automatisch laufen.
- Überprüfen Sie die Protokolle unter **Pipelines > Builds**, um den Fortschritt zu überwachen oder Fehler zu beheben.

#### **6. Bereitstellen (optional)**
- Fügen Sie eine **Release-Pipeline** (unter **Releases**) hinzu oder erweitern Sie Ihr YAML, um in Umgebungen wie Azure App Service, Kubernetes oder VMs bereitzustellen.

---

### **Wie man YAML für Azure Pipelines schreibt**
YAML (Yet Another Markup Language) ist ein menschenlesbares Format, das zur Definition von Pipeline-Konfigurationen verwendet wird. Hier ist ein Crashkurs:

#### **Grundstruktur**
```yaml
trigger:
  - main  # Pipeline ausführen, wenn der 'main'-Branch aktualisiert wird

pool:
  vmImage: 'ubuntu-latest'  # Geben Sie das Build-Agent (z. B. Ubuntu, Windows, macOS) an

steps:
  - script: echo Hello, world!  # Ein einfacher Befehl zum Ausführen
    displayName: 'Einen einzeiligen Skript ausführen'
```

- **`trigger`**: Definiert, wann die Pipeline läuft (z. B. bei einem Push an `main`).
- **`pool`**: Gibt das virtuelle Maschinenbild für den Build-Agent an.
- **`steps`**: Listet Aufgaben auf, die ausgeführt werden sollen (Skripte, eingebaute Aufgaben usw.).

#### **Häufige Elemente**
1. **Variablen**:
   ```yaml
   variables:
     buildConfiguration: 'Release'
   steps:
     - script: echo $(buildConfiguration)  # Gibt 'Release' aus
   ```

2. **Jobs** (Gruppieren von Schritten):
   ```yaml
   jobs:
   - job: Build
     steps:
       - script: echo Building...
   - job: Test
     steps:
       - script: echo Testing...
   ```

3. **Aufgaben** (vordefinierte Aktionen):
   ```yaml
   steps:
     - task: DotNetCoreCLI@2  # Beispiel: .NET-Projekt erstellen
       inputs:
         command: 'build'
         projects: '**/*.csproj'
   ```

4. **Bedingungen**:
   ```yaml
   steps:
     - script: echo Dies läuft nur auf main
       condition: eq(variables['Build.SourceBranch'], 'refs/heads/main')
   ```

5. **Stages** (für mehrstufige Pipelines):
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

#### **Praxisbeispiel**
Hier ist eine Pipeline für eine Node.js-Anwendung:
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

  - task: CopyFiles@2  # Build-Artifacts kopieren
    inputs:
      contents: 'dist/**'
      targetFolder: '$(Build.ArtifactStagingDirectory)'

  - task: PublishBuildArtifacts@1  # Artifacts veröffentlichen
    inputs:
      pathToPublish: '$(Build.ArtifactStagingDirectory)'
      artifactName: 'dist'
```

#### **Tipps zum Schreiben von YAML**
- Verwenden Sie eine konsistente Einrückung (2 Leerzeichen, keine Tabulatoren).
- Überprüfen Sie die Syntax mit einem Editor (z. B. VS Code mit der "YAML"-Erweiterung).
- Beziehen Sie sich auf das [Azure Pipelines YAML-Schema](https://learn.microsoft.com/en-us/azure/devops/pipelines/yaml-schema) für Optionen.
- Beginnen Sie einfach und fügen Sie Komplexität (z. B. Stages, Variablen) nach Bedarf hinzu.

---

### **Nächste Schritte**
- **Probieren Sie es aus**: Erstellen Sie ein Repository, fügen Sie eine grundlegende `azure-pipelines.yml` wie die oben genannte hinzu und führen Sie sie in Azure DevOps aus.
- **Erfahren Sie mehr**: Überprüfen Sie die offiziellen [Dokumentationen von Microsoft](https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started) oder suchen Sie nach Beispiel-Pipelines auf GitHub.
- **Fragen Sie mich**: Wenn Sie auf ein Problem stoßen oder ein bestimmtes Beispiel benötigen (z. B. Python, Java), lassen Sie es mich wissen!

Worin möchten Sie tiefer eintauchen? Einrichten einer Pipeline, YAML-Syntax oder etwas anderes?