---
audio: false
generated: true
lang: es
layout: post
title: Programación Cron de GitHub Actions
translated: true
type: note
---

Sí, se puede configurar un flujo de trabajo de GitHub para que se ejecute una vez al día utilizando un cron schedule en GitHub Actions.

### Explicación
GitHub Actions te permite automatizar tareas dentro de tu repositorio mediante flujos de trabajo, los cuales se definen en archivos YAML ubicados en el directorio `.github/workflows`. Una forma de activar un flujo de trabajo es usando el evento `schedule`, que emplea una sintaxis similar a cron para especificar cuándo debe ejecutarse el flujo de trabajo. La sintaxis cron en GitHub Actions sigue el formato POSIX estándar, que consta de cinco campos: minuto, hora, día del mes, mes y día de la semana.

Para ejecutar un flujo de trabajo una vez al día, puedes usar una expresión cron como `0 0 * * *`, que se traduce en "cada día a las 00:00 UTC". Así se desglosa:
- **Minuto (0)**: En el minuto 0 de la hora
- **Hora (0)**: 00:00 (medianoche) UTC
- **Día del mes (*)**: Cada día del mes
- **Mes (*)**: Cada mes
- **Día de la semana (*)**: Cada día de la semana

### Configuración de Ejemplo
A continuación se muestra una configuración de ejemplo de un flujo de trabajo de GitHub Actions que se ejecuta una vez al día:

```yaml
name: Daily Workflow
on:
  schedule:
    - cron: '0 0 * * *'
jobs:
  example-job:
    runs-on: ubuntu-latest
    steps:
      - name: Print message
        run: echo "This runs once a day!"
```

Este flujo de trabajo se ejecutará a la medianoche UTC todos los días.

### Consideraciones Clave
- **Zona Horaria**: El programa opera en UTC, así que ajusta la expresión cron si necesitas que se ejecute a una hora específica en tu zona horaria local.
- **Rama Predeterminada**: Por defecto, los flujos de trabajo programados se ejecutan en la rama predeterminada del repositorio (por ejemplo, `main` o `master`) a menos que se especifique lo contrario.
- **Fiabilidad**: Aunque GitHub Actions intenta ejecutar los flujos de trabajo a la hora especificada, pueden ocurrir ligeros retrasos debido a la carga de la infraestructura, aunque esto es poco común.
- **Límites de Uso**: Para las cuentas gratuitas de GitHub, existen límites en el uso de Actions (por ejemplo, minutos por mes), pero una única ejecución diaria normalmente está bien dentro de estos límites.

### Conclusión
Con una expresión cron correctamente configurada en el archivo del flujo de trabajo, GitHub Actions puede ejecutar un flujo de trabajo una vez al día. Por lo tanto, la respuesta a tu pregunta es **sí**.