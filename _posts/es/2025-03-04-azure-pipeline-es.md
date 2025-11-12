---
audio: false
generated: true
lang: es
layout: post
title: Usar Canalizaciones De Azure DevOps
translated: true
type: note
---

Vamos a desglosar esto en dos partes: **usar Azure DevOps Pipelines** y **escribir YAML para pipelines**. Proporcionaré una explicación clara y práctica para ambos.

---

### **Cómo usar Azure DevOps Pipelines**
Azure DevOps Pipelines es una herramienta de CI/CD (Integración Continua/Despliegue Continuo) que automatiza la compilación, prueba y despliegue de código. Así es como puedes empezar:

#### **1. Configurar un Proyecto**
- Inicia sesión en Azure DevOps (dev.azure.com) con tu organización.
- Crea un nuevo proyecto (o usa uno existente) haciendo clic en "New Project", asignándole un nombre y configurando la visibilidad (público/privado).

#### **2. Conectar tu Código**
- Ve a **Repos** en tu proyecto y sube tu código a un repositorio (GitHub, Azure Repos, Bitbucket, etc.).
- Alternativamente, vincula un repositorio externo en **Pipelines > New Pipeline > Connect** y selecciona tu fuente.

#### **3. Crear un Pipeline**
- Navega a **Pipelines** > **Builds** > **New Pipeline**.
- Elige tu repositorio y rama.
- Azure ofrece dos opciones:
  - **Classic Editor**: Un enfoque basado en interfaz gráfica (no requiere YAML).
  - **YAML**: Un pipeline basado en código (recomendado por su flexibilidad y control de versiones).
- Para YAML, selecciona "Starter pipeline" o configura desde un archivo existente en tu repositorio.

#### **4. Definir el Pipeline**
- Si usas YAML, escribirás un archivo `.yml` (ej. `azure-pipelines.yml`) en la raíz de tu repositorio. (Más sobre esto abajo).
- Añade triggers (ej. ejecutar en cada push a `main`), pasos (ej. compilar, probar) y objetivos de despliegue.

#### **5. Ejecutar y Monitorear**
- Guarda y confirma el archivo YAML (o guárdalo en el Classic Editor).
- Haz clic en **Run** para activar el pipeline manualmente, o déjalo ejecutarse automáticamente basado en los triggers.
- Revisa los registros en **Pipelines > Builds** para monitorear el progreso o solucionar fallos.

#### **6. Desplegar (Opcional)**
- Añade un **Release Pipeline** (en **Releases**) o extiende tu YAML para desplegar en entornos como Azure App Service, Kubernetes o VMs.

---

### **Cómo escribir YAML para Azure Pipelines**
YAML (Yet Another Markup Language) es un formato legible por humanos usado para definir configuraciones de pipeline. Aquí tienes un curso rápido:

#### **Estructura Básica**
```yaml
trigger:
  - main  # Ejecutar el pipeline cuando se actualice la rama 'main'

pool:
  vmImage: 'ubuntu-latest'  # Especifica el agente de compilación (ej. Ubuntu, Windows, macOS)

steps:
  - script: echo Hello, world!  # Un comando simple a ejecutar
    displayName: 'Ejecutar un script de una línea'
```

- **`trigger`**: Define cuándo se ejecuta el pipeline (ej. al hacer push a `main`).
- **`pool`**: Especifica la imagen de máquina virtual para el agente de compilación.
- **`steps`**: Enumera las tareas a ejecutar (scripts, tareas integradas, etc.).

#### **Elementos Comunes**
1. **Variables**:
   ```yaml
   variables:
     buildConfiguration: 'Release'
   steps:
     - script: echo $(buildConfiguration)  # Imprime 'Release'
   ```

2. **Jobs** (agrupar pasos):
   ```yaml
   jobs:
   - job: Build
     steps:
       - script: echo Building...
   - job: Test
     steps:
       - script: echo Testing...
   ```

3. **Tasks** (acciones preconstruidas):
   ```yaml
   steps:
     - task: DotNetCoreCLI@2  # Ejemplo: Compilar un proyecto .NET
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

5. **Stages** (para pipelines multifase):
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

#### **Ejemplo del Mundo Real**
Aquí hay un pipeline para una aplicación Node.js:
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
    displayName: 'Instalar y Compilar'

  - task: CopyFiles@2  # Copiar artefactos de compilación
    inputs:
      contents: 'dist/**'
      targetFolder: '$(Build.ArtifactStagingDirectory)'

  - task: PublishBuildArtifacts@1  # Publicar artefactos
    inputs:
      pathToPublish: '$(Build.ArtifactStagingDirectory)'
      artifactName: 'dist'
```

#### **Consejos para Escribir YAML**
- Usa indentación consistente (2 espacios, sin tabulaciones).
- Valida la sintaxis con un editor (ej. VS Code con la extensión "YAML").
- Consulta el [esquema YAML de Azure Pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/yaml-schema) para ver opciones.
- Empieza de forma simple, luego añade complejidad (ej. stages, variables) según sea necesario.

---

### **Próximos Pasos**
- **Pruébalo**: Crea un repositorio, añade un `azure-pipelines.yml` básico como el de arriba y ejecútalo en Azure DevOps.
- **Aprende más**: Revisa la [documentación oficial](https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started) de Microsoft o busca pipelines de ejemplo en GitHub.
- **Pregúntame**: Si encuentras un problema o quieres un ejemplo específico (ej. Python, Java), ¡avísame!

¿Sobre qué quieres profundizar? ¿Configurar un pipeline, la sintaxis de YAML, o algo más?