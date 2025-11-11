---
audio: false
generated: true
lang: fr
layout: post
title: Utiliser Moment.js en JavaScript
translated: true
type: note
---

Je vais vous montrer comment utiliser les bibliothèques `moment` et `moment-timezone` en JavaScript. Ce sont des bibliothèques populaires pour manipuler les dates et heures.

1. D'abord, installez les packages si vous ne l'avez pas déjà fait :
```bash
npm install moment moment-timezone
```

2. Exemples d'utilisation de base :

```javascript
// Importer les bibliothèques
const moment = require('moment');
const momentTimezone = require('moment-timezone');

// Utilisation de base de Moment.js
// Date et heure actuelles
const now = moment();
console.log(now.format('YYYY-MM-DD HH:mm:ss')); // ex. "2025-03-03 14:30:45"

// Analyser une date spécifique
const date = moment('2025-12-25');
console.log(date.format('MMMM Do YYYY')); // "December 25th 2025"

// Manipuler les dates
const tomorrow = moment().add(1, 'days');
console.log(tomorrow.format('ddd, MMM D')); // ex. "Tue, Mar 4"

// Utilisation de Moment-Timezone
// Obtenir l'heure dans un fuseau horaire spécifique
const nyTime = momentTimezone.tz('America/New_York');
console.log(nyTime.format('YYYY-MM-DD HH:mm:ss z')); // Inclut l'abréviation du fuseau horaire

// Convertir l'heure entre les fuseaux horaires
const localTime = moment();
const tokyoTime = localTime.clone().tz('Asia/Tokyo');
console.log(`Local: ${localTime.format('HH:mm')}`);
console.log(`Tokyo: ${tokyoTime.format('HH:mm')}`);

// Lister tous les fuseaux horaires disponibles
const timezones = momentTimezone.tz.names();
console.log(timezones); // Tableau des noms de fuseaux horaires
```

Options de formatage courantes :
- `YYYY` : année à 4 chiffres (2025)
- `MM` : mois à 2 chiffres (03)
- `DD` : jour à 2 chiffres (03)
- `HH` : heure au format 24h (14)
- `hh` : heure au format 12h (02)
- `mm` : minutes (30)
- `ss` : secondes (45)
- `z` : abréviation du fuseau horaire

Méthodes utiles :
```javascript
// Manipulation de date
moment().add(7, 'days');     // Ajouter du temps
moment().subtract(2, 'hours'); // Soustraire du temps
moment().startOf('month');   // Début de la période
moment().endOf('month');     // Fin de la période

// Comparaison de dates
moment().isBefore(date);
moment().isAfter(date);
moment().isSame(date);

// Opérations sur les fuseaux horaires
momentTimezone.tz('2025-03-03', 'America/Los_Angeles');
momentTimezone.tz.guess(); // Deviner le fuseau horaire de l'utilisateur
```

Notes :
1. Ces versions (^2.14.1 et ^0.5.7) sont assez anciennes (datant d'environ 2016). Envisagez d'utiliser les dernières versions, sauf si vous avez des exigences de compatibilité spécifiques.
2. Moment.js est désormais considéré comme un projet legacy en mode maintenance. Pour les nouveaux projets, vous pourriez envisager des alternatives comme `date-fns` ou `luxon`.