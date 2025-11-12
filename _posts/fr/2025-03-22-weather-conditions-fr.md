---
audio: false
generated: true
lang: fr
layout: post
title: Conditions météorologiques complètes dans Raccourcis iOS
translated: true
type: note
---

Voici une analyse détaillée de toutes les plages de valeurs des conditions météorologiques disponibles dans les Raccourcis iOS :

## Indice UV
- **Plage** : 0-11+
- **Échelle** :
  - 0-2 : Faible
  - 3-5 : Modéré
  - 6-7 : Élevé
  - 8-10 : Très élevé
  - 11+ : Extrême

## Température
- **Plage** : Variable selon la localisation
- **Unités** : Celsius (°C) ou Fahrenheit (°F)
- **Plage typique** : -50°C à 50°C (-58°F à 122°F)

## Température Ressentie
- **Plage** : Similaire à la température réelle
- **Unités** : Celsius (°C) ou Fahrenheit (°F)
- **Facteurs** : Combine la température, l'humidité, le refroidissement éolien

## Humidité
- **Plage** : 0-100%

## Visibilité
- **Plage** : 0-10+ miles ou 0-16+ kilomètres

## Vitesse du Vent
- **Plage** : 0-100+ mph ou 0-160+ km/h
- **Unités** : mph, km/h, m/s ou nœuds

## Direction du Vent
- **Plage** : 0-359 degrés
- **Directions cardinales** : N (0°), E (90°), S (180°), O (270°)

## Indice de Qualité de l'Air (AQI)
- **Plage** : 0-500+
- **Échelle** : Bonne (0-50) à Dangereuse (301+)

## Probabilité de Précipitations
- **Plage** : 0-100%
- **Interprétation** : Probabilité de précipitations sur la période de prévision

## Quantité de Précipitations
- **Plage** : 0 à 100+ mm ou pouces
- **Unités** : mm ou pouces
- **Période** : Généralement mesurée par heure ou par jour

## Intensité des Précipitations
- **Plage** :
  - Aucune : 0 mm/h
  - Légère : 0.1-2.5 mm/h
  - Modérée : 2.5-10 mm/h
  - Forte : 10-50 mm/h
  - Violente : 50+ mm/h

## Pression Atmosphérique
- **Plage** : Typiquement 950-1050 hPa/mb
- **Unités** : hPa, mb ou inHg
- **Pression standard** : 1013.25 hPa au niveau de la mer

## Point de Rosée
- **Plage** : Similaire à la plage de température
- **Unités** : Celsius (°C) ou Fahrenheit (°F)
- **Niveaux de confort** :
  - <55°F (<13°C) : Sec et confortable
  - 55-65°F (13-18°C) : Confortable
  - >65°F (>18°C) : De plus en plus humide et inconfortable

## Couverture Nuageuse
- **Plage** : 0-100%

## Condition Météorologique
- **Valeurs** : Descriptions textuelles (Dégagé, Partiellement Nuageux, Pluie, Neige, etc.)

## Heures de Lever/Coucher du Soleil
- **Plage** : Valeurs horaires dans le fuseau horaire local

## Phase de la Lune
- **Plage** : 0-1 (0 = Nouvelle Lune, 0.5 = Pleine Lune, 1 = Nouvelle Lune)
- **Valeurs textuelles** : Nouvelle Lune, Premier Croissant, Premier Quartier, etc.

## Compte Pollinique
- **Plage** : Généralement 0-12
- **Échelle** : Faible, Modéré, Élevé, Très Élevé

## Indice de Chaleur
- **Plage** : Plage de température, mais uniquement calculé lorsque la température est supérieure à 80°F (27°C)
- **Unités** : Identiques à la température

## Quantité de Neige
- **Plage** : 0 à 100+ cm ou pouces
- **Unités** : cm ou pouces
- **Période** : Généralement par heure ou par jour

Ces valeurs de conditions météorologiques peuvent être utilisées dans des instructions conditionnelles au sein des Raccourcis pour créer des automatisations sophistiquées basées sur la météo, adaptées à des conditions spécifiques.