---
audio: false
generated: true
lang: fr
layout: post
title: Gestion de la Batterie de Souris d'Ubuntu
translated: true
type: note
---

Ubuntu dispose de plusieurs fonctionnalités intégrées qui aident à gérer l'alimentation de la souris et fournissent des notifications de batterie faible :

## Gestion de l'alimentation de la souris dans Ubuntu

**Surveillance de la batterie :**
- Le système de gestion de l'alimentation d'Ubuntu surveille les niveaux de batterie des souris sans fil via les connexions Bluetooth ou les récepteurs USB
- Le système lit les données de batterie depuis le firmware de la souris lorsque cela est disponible
- Les notifications d'alimentation apparaissent dans la zone de notification système lorsque la batterie descend en dessous de certains seuils (généralement autour de 20 % et 10 %)

**Fonctionnement du système de notification :**
- **Démon UPower** - Surveille les états d'alimentation des appareils connectés, y compris les souris sans fil
- **GNOME Power Manager** - Gère les notifications réelles et les paramètres d'alimentation
- **Pile Bluetooth** - Pour les souris Bluetooth, les informations sur la batterie sont transmises via les protocoles Bluetooth standard
- **USB HID** - Pour les souris sans fil avec des dongles USB, les données de batterie proviennent des rapports HID (Human Interface Device)

**Fonctionnalités d'économie d'énergie :**
- Mode veille automatique de la souris en cas d'inactivité
- Taux d'interrogation réduits pendant les périodes de faible activité
- Paramètres de délai de connexion pour préserver la batterie
- Option pour désactiver le réveil de la souris depuis la suspension

**Vérification de la batterie de la souris :**
Vous pouvez vérifier l'état de la batterie de la souris via :
- Paramètres système → Alimentation (affiche les appareils connectés)
- Ligne de commande : `upower -i /org/freedesktop/UPower/devices/mouse_*`
- L'indicateur de batterie dans le panneau supérieur (si la souris le prend en charge)

Le système fonctionne en interrogeant constamment les appareils connectés pour connaître leur état d'alimentation et en utilisant les services de notification du bureau pour alerter les utilisateurs lorsqu'une intervention est nécessaire. Cela permet d'éviter les déconnexions inattendues pendant un travail important.