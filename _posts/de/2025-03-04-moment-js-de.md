---
audio: false
generated: true
lang: de
layout: post
title: Verwendung von Moment.js in JavaScript
translated: true
type: note
---

Ich zeige Ihnen, wie Sie die `moment` und `moment-timezone` Bibliotheken in JavaScript verwenden. Dies sind beliebte Bibliotheken für die Arbeit mit Datum und Uhrzeit.

1. Installieren Sie zunächst die Pakete, falls noch nicht geschehen:
```bash
npm install moment moment-timezone
```

2. Grundlegende Verwendungsbeispiele:

```javascript
// Die Bibliotheken importieren
const moment = require('moment');
const momentTimezone = require('moment-timezone');

// Grundlegende Moment.js Verwendung
// Aktuelles Datum und Uhrzeit
const now = moment();
console.log(now.format('YYYY-MM-DD HH:mm:ss')); // z.B. "2025-03-03 14:30:45"

// Ein bestimmtes Datum parsen
const date = moment('2025-12-25');
console.log(date.format('MMMM Do YYYY')); // "December 25th 2025"

// Daten manipulieren
const tomorrow = moment().add(1, 'days');
console.log(tomorrow.format('ddd, MMM D')); // z.B. "Tue, Mar 4"

// Moment-Timezone verwenden
// Uhrzeit in einer bestimmten Zeitzone abrufen
const nyTime = momentTimezone.tz('America/New_York');
console.log(nyTime.format('YYYY-MM-DD HH:mm:ss z')); // Enthält Zeitzonenkürzel

// Zeit zwischen Zeitzonen umrechnen
const localTime = moment();
const tokyoTime = localTime.clone().tz('Asia/Tokyo');
console.log(`Lokal: ${localTime.format('HH:mm')}`);
console.log(`Tokyo: ${tokyoTime.format('HH:mm')}`);

// Alle verfügbaren Zeitzonen auflisten
const timezones = momentTimezone.tz.names();
console.log(timezones); // Array von Zeitzonennamen
```

Häufige Formatierungsoptionen:
- `YYYY`: 4-stellige Jahreszahl (2025)
- `MM`: 2-stelliger Monat (03)
- `DD`: 2-stelliger Tag (03)
- `HH`: 24-Stunden-Format (14)
- `hh`: 12-Stunden-Format (02)
- `mm`: Minuten (30)
- `ss`: Sekunden (45)
- `z`: Zeitzonenkürzel

Nützliche Methoden:
```javascript
// Datumsmanipulation
moment().add(7, 'days');     // Zeit hinzufügen
moment().subtract(2, 'hours'); // Zeit abziehen
moment().startOf('month');   // Anfang des Zeitraums
moment().endOf('month');     // Ende des Zeitraums

// Datumsvergleich
moment().isBefore(date);
moment().isAfter(date);
moment().isSame(date);

// Zeitzonenoperationen
momentTimezone.tz('2025-03-03', 'America/Los_Angeles');
momentTimezone.tz.guess(); // Zeitzone des Benutzers erraten
```

Hinweise:
1. Diese Versionen (^2.14.1 und ^0.5.7) sind recht alt (aus ca. 2016). Ziehen Sie in Betracht, die neuesten Versionen zu verwenden, sofern Sie keine spezifischen Kompatibilitätsanforderungen haben.
2. Moment.js wird mittlerweile als Legacy-Projekt im Wartungsmodus betrachtet. Für neue Projekte sollten Sie Alternativen wie `date-fns` oder `luxon` in Betracht ziehen.