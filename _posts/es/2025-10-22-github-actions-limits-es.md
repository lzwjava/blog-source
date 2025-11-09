---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Descripción General de los Límites de Uso de GitHub Actions
translated: true
type: note
---

### Límites de uso de GitHub Actions

GitHub Actions tiene límites escalonados según tu plan (cuentas personales u organizaciones). Estos incluyen minutos mensuales gratuitos para runners alojados en GitHub en repositorios privados y almacenamiento para artefactos. Los repositorios públicos y los runners auto-hospedados no consumen estos minutos. Los límites se reinician mensualmente para los minutos (el almacenamiento es continuo). Los excesos se facturan automáticamente si tienes un método de pago válido; de lo contrario, los jobs se bloquean después de alcanzar el límite.

#### Minutos y Almacenamiento incluidos por Plan

| Plan                          | Almacenamiento | Minutos (por mes) |
|-------------------------------|---------|---------------------|
| GitHub Free (personal/org)   | 500 MB | 2,000              |
| GitHub Pro (personal)        | 1 GB   | 3,000              |
| GitHub Team (org)            | 2 GB   | 3,000              |
| GitHub Enterprise Cloud (org)| 50 GB  | 50,000             |

- **Minutos**: Cuenta el tiempo total de ejecución del job en runners alojados en GitHub (tiempo parcial para jobs fallidos). Se aplican multiplicadores: Linux (1x), Windows (2x), macOS (10x). Cualquier persona con acceso de escritura a un repo utiliza la asignación del propietario del repo.
- **Almacenamiento**: Se basa en GB-hora de almacenamiento de artefactos (ej., subidas/descargas). Los logs y resúmenes no cuentan.

#### Facturación por Excesos
Si excedes las cuotas:
- **Minutos**: Se cobra por minuto extra (tarifas en USD para runners Linux estándar: $0.008/min; más alto para Windows/macOS debido a los multiplicadores).
- **Almacenamiento**: Se cobra como GB-mes (total de GB-horas / 744 horas por mes, redondeado hacia arriba).
- Ejemplo: En un plan Team, 5,000 minutos extra (3,000 Linux + 2,000 Windows) cuesta ~$56.

Sin un método de pago, el uso se detiene en la cuota. El error que viste ("los pagos recientes de la cuenta han fallado o tu límite de gasto necesita ser aumentado") significa que los pagos fueron rechazados o tu **límite de gasto (presupuesto)** está limitando los excesos.

#### Límites de Gasto (Presupuestos)
- Estos son umbrales opcionales para controlar el gasto mensual total en Actions (y otras funciones medidas).
- Si se establece demasiado bajo, bloquea los jobs antes de alcanzar las cuotas.
- **Cómo verificar/aumentar**:
  1. Ve a Configuración de GitHub > Facturación y planes.
  2. En "Presupuestos y alertas", visualiza o edita tu presupuesto para GitHub Actions.
  3. Aumenta el límite, agrega un método de pago o elimina el presupuesto por completo (excesos ilimitados, pero monitorea mediante alertas).
- Las cuentas migradas pueden tener presupuestos auto-generados a partir de límites antiguos—actualízalos para que se ajusten a tu uso.

Para más detalles, consulta el panel de facturación de tu cuenta para ver el uso en tiempo real.

[Documentación de Facturación de GitHub Actions](https://docs.github.com/en/billing/managing-billing-for-github-actions/about-billing-for-github-actions)