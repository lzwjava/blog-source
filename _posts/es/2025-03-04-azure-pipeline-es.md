---
audio: false
generated: true
lang: es
layout: post
title: Usando Azure DevOps Pipelines
translated: true
---

Vamos a desglosar esto en dos partes: **usar Azure DevOps Pipelines** y **escribir YAML para pipelines**. Proporcionaré una explicación clara y práctica para ambas.

---

### **Cómo usar Azure DevOps Pipelines**
Azure DevOps Pipelines es una herramienta de CI/CD (Integración Continua/Despliegue Continuo) que automatiza la construcción, prueba y implementación del código. Aquí tienes cómo empezar:

#### **1. Configurar un Proyecto**
- Inicia sesión en Azure DevOps (dev.azure.com) con tu organización.
- Crea un nuevo proyecto (o usa uno existente) haciendo clic en "Nuevo Proyecto", dándole un nombre y configurando la visibilidad (pública/privada).

#### **2. Conectar tu Código**
- Ve a **Repos** en tu proyecto y envía tu código a un repositorio (GitHub, Azure Repos, Bitbucket, etc.).
- Alternativamente, vincula un repositorio externo bajo **Pipelines > Nuevo Pipeline > Conectar** y selecciona tu fuente.

#### **3. Crear un Pipeline**
- Navega a **Pipelines > Builds > Nuevo Pipeline**.
- Elige tu repositorio y rama.
- Azure ofrece dos opciones:
  - **Editor Clásico**: Un enfoque basado en GUI (no se necesita YAML).
  - **YAML**: Un pipeline basado en código (recomendado por su flexibilidad y control de versiones).
- Para YAML, selecciona "Starter pipeline" o configura desde un archivo existente en tu repositorio.

#### **4. Definir el Pipeline**
- Si usas YAML, escribirás un archivo `.yml` (por ejemplo, `azure-pipelines.yml`) en la raíz de tu repositorio. (Más sobre esto a continuación.)
- Añade disparadores (por ejemplo, ejecutar en cada envío a `main`), pasos (por ejemplo, construir, probar) y objetivos de implementación.

#### **5. Ejecutar y Monitorear**
- Guarda y confirma el archivo YAML (o guarda en el Editor Clásico).
- Haz clic en **Ejecutar** para desencadenar el pipeline manualmente, o déjalo ejecutar automáticamente según los disparadores.
- Revisa los registros bajo **Pipelines > Builds** para monitorear el progreso o solucionar problemas.

#### **6. Implementar (Opcional)**
- Añade un **pipeline de liberación** (bajo **Releases**) o extiende tu YAML para implementar en entornos como Azure App Service, Kubernetes o VMs.

---

### **Cómo escribir YAML para Azure Pipelines**
YAML (Yet Another Markup Language) es un formato legible por humanos utilizado para definir configuraciones de pipeline. Aquí tienes un curso intensivo:

#### **Estructura Básica**
```yaml
trigger:
  - main  # Ejecutar el pipeline cuando se actualice la rama 'main'

pool:
  vmImage: 'ubuntu-latest'  # Especifica la imagen de la máquina virtual para el agente de construcción (por ejemplo, Ubuntu, Windows, macOS)

steps:
  - script: echo Hello, world!  # Un comando simple para ejecutar
    displayName: 'Ejecutar un script de una línea'
```

- **`trigger`**: Define cuándo se ejecuta el pipeline (por ejemplo, en el envío a `main`).
- **`pool`**: Especifica la imagen de la máquina virtual para el agente de construcción.
- **`steps`**: Lista las tareas a ejecutar (scripts, tareas integradas, etc.).

#### **Elementos Comunes**
1. **Variables**:
   ```yaml
   variables:
     buildConfiguration: 'Release'
   steps:
     - script: echo $(buildConfiguration)  # Salida 'Release'
   ```

2. **Trabajos** (agrupar pasos):
   ```yaml
   jobs:
   - job: Build
     steps:
       - script: echo Construyendo...
   - job: Test
     steps:
       - script: echo Probando...
   ```

3. **Tareas** (acciones preconstruidas):
   ```yaml
   steps:
     - task: DotNetCoreCLI@2  # Ejemplo: Construir un proyecto .NET
       inputs:
         command: 'build'
         projects: '**/*.csproj'
   ```

4. **Condiciones**:
   ```yaml
   steps:
     - script: echo Esto solo se ejecuta en main
       condition: eq(variables['Build.SourceBranch'], 'refs/heads/main')
   ```

5. **Etapas** (para pipelines de múltiples fases):
   ```yaml
   stages:
   - stage: Build
     jobs:
       - job: BuildJob
         steps:
           - script: echo Construyendo...
   - stage: Deploy
     dependsOn: Build
     jobs:
       - job: DeployJob
         steps:
           - script: echo Implementando...
   ```

#### **Ejemplo del Mundo Real**
Aquí tienes un pipeline para una aplicación Node.js:
```yaml
trigger:
  - main

pool:
  vmImage: 'ubuntu-latest'

steps:
  - task: NodeTool@0  # Instalar Node.js
    inputs:
      versionSpec: '16.x'
    displayName: 'Instalar Node.js'

  - script: |
      npm install
      npm run build
    displayName: 'Instalar y Construir'

  - task: CopyFiles@2  # Copiar artefactos de construcción
    inputs:
      contents: 'dist/**'
      targetFolder: '$(Build.ArtifactStagingDirectory)'

  - task: PublishBuildArtifacts@1  # Publicar artefactos
    inputs:
      pathToPublish: '$(Build.ArtifactStagingDirectory)'
      artifactName: 'dist'
```

#### **Consejos para Escribir YAML**
- Usa una indentación consistente (2 espacios, sin tabulaciones).
- Valida la sintaxis con un editor (por ejemplo, VS Code con la extensión "YAML").
- Consulta el [esquema YAML de Azure Pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/yaml-schema) para opciones.
- Empieza simple, luego añade complejidad (por ejemplo, etapas, variables) según sea necesario.

---

### **Próximos Pasos**
- **Pruébalo**: Crea un repositorio, añade un `azure-pipelines.yml` básico como el anterior y ejecútalo en Azure DevOps.
- **Aprende más**: Consulta la [documentación oficial de Microsoft](https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started) o busca pipelines de ejemplo en GitHub.
- **Pregúntame**: Si encuentras un problema o quieres un ejemplo específico (por ejemplo, Python, Java), házmelo saber.

¿En qué te gustaría profundizar más? ¿Configurar un pipeline, la sintaxis YAML o algo más?