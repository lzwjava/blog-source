---
audio: false
generated: true
lang: es
layout: post
title: Usando Moment.js en JavaScript
translated: true
---

Te mostraré cómo usar las bibliotecas `moment` y `moment-timezone` en JavaScript. Estas son bibliotecas populares para manejar fechas y horas.

1. Primero, instala los paquetes si aún no lo has hecho:
```bash
npm install moment moment-timezone
```

2. Ejemplos de uso básico:

```javascript
// Importar las bibliotecas
const moment = require('moment');
const momentTimezone = require('moment-timezone');

// Uso básico de Moment.js
// Fecha y hora actuales
const now = moment();
console.log(now.format('YYYY-MM-DD HH:mm:ss')); // por ejemplo, "2025-03-03 14:30:45"

// Analizar una fecha específica
const date = moment('2025-12-25');
console.log(date.format('MMMM Do YYYY')); // "25 de diciembre de 2025"

// Manipular fechas
const tomorrow = moment().add(1, 'days');
console.log(tomorrow.format('ddd, MMM D')); // por ejemplo, "Mar 4, Mar"

// Usando Moment-Timezone
// Obtener la hora en una zona horaria específica
const nyTime = momentTimezone.tz('America/New_York');
console.log(nyTime.format('YYYY-MM-DD HH:mm:ss z')); // Incluye la abreviatura de la zona horaria

// Convertir hora entre zonas horarias
const localTime = moment();
const tokyoTime = localTime.clone().tz('Asia/Tokyo');
console.log(`Local: ${localTime.format('HH:mm')}`);
console.log(`Tokio: ${tokyoTime.format('HH:mm')}`);

// Listar todas las zonas horarias disponibles
const timezones = momentTimezone.tz.names();
console.log(timezones); // Array de nombres de zonas horarias
```

Opciones de formato comunes:
- `YYYY`: año de 4 dígitos (2025)
- `MM`: mes de 2 dígitos (03)
- `DD`: día de 2 dígitos (03)
- `HH`: hora (24 horas) (14)
- `hh`: hora (12 horas) (02)
- `mm`: minutos (30)
- `ss`: segundos (45)
- `z`: abreviatura de la zona horaria

Métodos útiles:
```javascript
// Manipulación de fechas
moment().add(7, 'days');     // Añadir tiempo
moment().subtract(2, 'hours'); // Restar tiempo
moment().startOf('month');   // Comienzo del período
moment().endOf('month');     // Fin del período

// Comparación de fechas
moment().isBefore(date);
moment().isAfter(date);
moment().isSame(date);

// Operaciones de zona horaria
momentTimezone.tz('2025-03-03', 'America/Los_Angeles');
momentTimezone.tz.guess(); // Adivinar la zona horaria del usuario
```

Notas:
1. Estas versiones (^2.14.1 y ^0.5.7) son bastante antiguas (de alrededor de 2016). Considera usar las versiones más recientes a menos que tengas requisitos específicos de compatibilidad.
2. Moment.js ahora se considera un proyecto legado en modo de mantenimiento. Para nuevos proyectos, podrías querer considerar alternativas como `date-fns` o `luxon`.