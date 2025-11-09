---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Guía de Inicio Rápido de la CLI de Azure
translated: true
type: note
---

Azure CLI (Command-Line Interface) es un conjunto de herramientas multiplataforma para administrar recursos de Azure desde la línea de comandos. Es ideal para automatizar tareas, crear scripts de implementación e interactuar con los servicios de Azure sin necesidad del portal web. Es compatible con Bash, PowerShell y Command Prompt en Windows, macOS y Linux.

## Instalación

1. **Requisitos previos**: Asegúrate de tener Python 3.8 o posterior instalado (verifica con `python --version`).

2. **Instalar mediante el Administrador de Paquetes** (Recomendado):
   - **Windows**: Usa Winget (`winget install Microsoft.AzureCLI`) o Chocolatey (`choco install azure-cli`).
   - **macOS**: Usa Homebrew (`brew install azure-cli`).
   - **Linux (Ubuntu/Debian)**: Ejecuta `curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash`.
   - **Otros Linux**: Usa RPM o descarga manualmente desde el sitio oficial.

3. **Verificar la instalación**: Abre una terminal y ejecuta `az --version`. Deberías ver la versión de la CLI (por ejemplo, 2.64.0 a finales de 2025).

Para pasos detallados específicos de la plataforma, consulta la documentación oficial de instalación.

## Autenticación

Antes de usar Azure CLI, inicia sesión en tu cuenta de Azure:

1. **Inicio de sesión interactivo**: Ejecuta `az login`. Esto abre un navegador para la autenticación de Microsoft Entra ID. Sigue las indicaciones para iniciar sesión.

2. **Entidad de servicio (para automatización)**: Crea una entidad de servicio con `az ad sp create-for-rbac --name "MyApp" --role contributor --scopes /subscriptions/{subscription-id}`. Luego usa `az login --service-principal -u <app-id> -p <password> --tenant <tenant-id>`.

3. **Verificar inicio de sesión**: Usa `az account show` para verificar tu suscripción activa.

4. **Cerrar sesión**: `az logout`.

La autenticación multifactor (MFA) es compatible, y puedes administrar múltiples suscripciones con `az account set --subscription <id>`.

## Comandos Básicos

Azure CLI usa el comando `az` seguido de un grupo (por ejemplo, `vm`, `storage`) y subcomandos. Usa `az --help` para obtener una visión general, o `az <group> --help` para detalles específicos.

### Opciones Globales Comunes
- `--help` o `-h`: Mostrar ayuda.
- `--output table/json/yaml`: Formatear la salida (por defecto: tabla).
- `--query`: Consulta JMESPath para filtrar la salida JSON (por ejemplo, `--query "[].name"`).

### Ejemplos Clave
- **Listar Suscripciones**: `az account list --output table`
- **Obtener Grupos de Recursos**: `az group list --output table`
- **Crear un Grupo de Recursos**: `az group create --name "MyResourceGroup" --location "eastus"`

## Administración de Máquinas Virtuales (VM)
Azure CLI es excelente para la gestión del ciclo de vida de las VM.

1. **Crear una VM**:
   ```
   az vm create \
     --resource-group "MyResourceGroup" \
     --name "MyVM" \
     --image Ubuntu2204 \
     --admin-username azureuser \
     --admin-password MyP@ssw0rd123! \
     --location "eastus"
   ```

2. **Listar VM**: `az vm list --output table`

3. **Iniciar/Detener VM**: `az vm start --name "MyVM" --resource-group "MyResourceGroup"` o `az vm stop --name "MyVM" --resource-group "MyResourceGroup"`

4. **SSH a la VM**: `az vm ssh "MyVM" --resource-group "MyResourceGroup"`

5. **Eliminar VM**: `az vm delete --name "MyVM" --resource-group "MyResourceGroup" --yes`

## Administración de Cuentas de Almacenamiento
1. **Crear Cuenta de Almacenamiento**:
   ```
   az storage account create \
     --name mystorageaccount \
     --resource-group "MyResourceGroup" \
     --location "eastus" \
     --sku Standard_LRS
   ```

2. **Cargar Blob**: Primero, obtén la clave con `az storage account keys list --account-name mystorageaccount --resource-group "MyResourceGroup" --query "[0].value -o tsv"`. Luego: `az storage blob upload --account-name mystorageaccount --container-name mycontainer --name myfile.txt --file ./myfile.txt --auth-mode key`

## Otros Escenarios Comunes
- **Implementar Plantillas ARM**: `az deployment group create --resource-group "MyResourceGroup" --template-file template.json`
- **Consultar Recursos**: `az resource list --resource-group "MyResourceGroup" --output table`
- **Actualizar CLI**: `az upgrade`
- **Extensiones**: Instala extensiones como `az extension add --name azure-devops` para comandos adicionales.

Para scripting, combínalo con bucles de Bash/PowerShell o usa Azure CLI en pipelines de CI/CD como GitHub Actions.

## Consejos y Mejores Prácticas
- Usa `--dry-run` para vistas previas (donde sea compatible).
- Habilita el autocompletado: En Bash, ejecuta `az completion`.
- Maneja errores: Verifica los códigos de salida (0 para éxito) y usa `--debug` para solucionar problemas.
- Seguridad: Evita codificar credenciales; usa variables de entorno o Azure Key Vault.

## Referencias
[Instalar Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)  
[Referencia de Azure CLI](https://learn.microsoft.com/en-us/cli/azure/)  
[Inicio Rápido de Azure CLI](https://learn.microsoft.com/en-us/cli/azure/get-started-with-azure-cli)