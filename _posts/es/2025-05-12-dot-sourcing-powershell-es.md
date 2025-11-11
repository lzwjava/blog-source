---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast:free
title: Importación de Scripts de PowerShell con Punto
translated: true
type: note
---

### Dot Sourcing de Funciones PowerShell en Archivos .ps1

El dot sourcing (usando el operador `.`) carga un script de PowerShell (.ps1) en la memoria de la sesión actual, haciendo que sus funciones y variables estén disponibles para usar sin ejecutar el código de nivel superior del script. Es útil para importar módulos o código reutilizable.

#### Sintaxis Básica
Ejecuta este comando en tu sesión de PowerShell:
```
. Ruta\A\TuScript.ps1
```
- Reemplaza `Ruta\A\TuScript.ps1` con la ruta real del archivo (usa rutas absolutas para mayor confiabilidad).
- Ejemplo: `. C:\Scripts\MisFunciones.ps1` – Esto carga las funciones de ese archivo en tu sesión.

#### Cómo Funciona
- Las funciones definidas en el script se vuelven invocables en tu sesión actual.
- Las variables también se importan, pero solo si no tienen un ámbito local.
- Evita el dot sourcing en scripts de producción; usa módulos para una mejor organización.
- Consejo: Si la ruta tiene espacios, envuélvela entre comillas: `. "C:\Mis Scripts\Funciones.ps1"`

Problema común: Si el script tiene errores de sintaxis, el dot sourcing fallará con un error. Prueba ejecutando `PowerShell -Command ". .\TuScript.ps1"` desde un símbolo del sistema.

### Usando la Política de Ejecución de PowerShell

Las políticas de ejecución son configuraciones de seguridad que restringen qué scripts puede ejecutar PowerShell, previniendo la ejecución de código malicioso. Son por ámbito (por ejemplo, para toda la máquina, específico del usuario).

#### Verificando la Política Actual
Ejecuta esto en PowerShell:
```
Get-ExecutionPolicy
```
- Ejemplos de salida: `Restricted` (bloquea todos los scripts), `AllSigned` (solo scripts firmados), `RemoteSigned` (scripts remotos firmados, locales permitidos), o `Unrestricted`.

#### Estableciendo o Cambiando la Política
Usa `Set-ExecutionPolicy` (requiere derechos de administrador para cambios a nivel de máquina):
- Ejemplo para permitir scripts escritos localmente: `Set-ExecutionPolicy RemoteSigned`
- Forzar sin preguntas: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force`
- Por ámbito: `Set-ExecutionPolicy -ExecutionPolicy AllSigned -Scope CurrentUser` (afecta solo a tu cuenta de usuario).

#### Políticas Comunes
- `Restricted`: Por defecto; no se ejecutan scripts.
- `AllSigned`: Requiere firmas digitales (seguro pero inconveniente).
- `RemoteSigned`: Equilibra seguridad—permite scripts locales, firma los remotos.
- `Unrestricted`: Ejecuta todos los scripts (riesgoso; usar con precaución).
- `Bypass`: Completamente sin restricciones, para automatización.

Consejo: Las políticas se aplican a sesiones de consola, pero no a ISE o VS Code a menos que se establezcan. Prueba los cambios ejecutando un script de ejemplo como `Write-Host "Hola"`. Para más información, consulta la documentación de Microsoft: `help about_Execution_Policies`. Si estás en un entorno empresarial, la Política de Grupo podría anular la configuración local.