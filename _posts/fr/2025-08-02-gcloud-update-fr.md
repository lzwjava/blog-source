---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Mise à jour de l'interface de ligne de commande Google Cloud
translated: true
type: note
---

% gcloud components update
Début de la mise à jour. Ce processus peut prendre plusieurs minutes.


Votre version actuelle de Google Cloud CLI est : 507.0.0
Vous allez être mis à niveau vers la version : 532.0.0

┌─────────────────────────────────────────────────────────────────────────────┐
│                      Ces composants seront mis à jour.                      │
├─────────────────────────────────────────────────────┬────────────┬──────────┤
│                         Nom                         │  Version   │  Taille  │
├─────────────────────────────────────────────────────┼────────────┼──────────┤
│ BigQuery Command Line Tool                          │     2.1.21 │  1.8 Mio │
│ BigQuery Command Line Tool (Platform Specific)      │     2.1.17 │  < 1 Mio │
│ Cloud Storage Command Line Tool                     │       5.35 │ 12.4 Mio │
│ Cloud Storage Command Line Tool (Platform Specific) │       5.34 │  < 1 Mio │
│ Google Cloud CLI Core Libraries                     │ 2025.07.25 │ 22.1 Mio │
│ Google Cloud CLI Core Libraries (Platform Specific) │ 2025.05.23 │  < 1 Mio │
│ Google Cloud CRC32C Hash Tool (Platform Specific)   │      1.0.0 │  1.4 Mio │
│ gcloud cli dependencies                             │ 2025.04.18 │ 16.1 Mio │
└─────────────────────────────────────────────────────┴────────────┴──────────┘

Beaucoup de choses ont changé depuis votre dernière mise à niveau. Pour les dernières notes de version complètes,
veuillez consulter :
  https://cloud.google.com/sdk/release_notes

Une fois commencée, l'annulation de cette opération peut laisser votre installation SDK dans un état incohérent.

Voulez-vous continuer (O/n) ?  O

Mise à jour en cours...

╔════════════════════════════════════════════════════════════╗
╠═ Téléchargement : BigQuery Command Line Tool              ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Téléchargement : BigQuery Command Line Tool (Platform... ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Téléchargement : Cloud Storage Command Line Tool         ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Téléchargement : Cloud Storage Command Line Tool (Plat...═╣
╠════════════════════════════════════════════════════════════╣
╠═ Téléchargement : Google Cloud CLI Core Libraries         ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Téléchargement : Google Cloud CLI Core Libraries (Plat...═╣
╠════════════════════════════════════════════════════════════╣
╠═ Téléchargement : Google Cloud CRC32C Hash Tool (Platf... ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Téléchargement : gcloud cli dependencies                 ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Désinstallation : BigQuery Command Line Tool             ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Désinstallation : BigQuery Command Line Tool (Platform...═╣
╠════════════════════════════════════════════════════════════╣
╠═ Désinstallation : Cloud Storage Command Line Tool        ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Désinstallation : Cloud Storage Command Line Tool (Pla...═╣
╠════════════════════════════════════════════════════════════╣
╠═ Désinstallation : Google Cloud CLI Core Libraries        ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Désinstallation : Google Cloud CLI Core Libraries (Pla...═╣
╠════════════════════════════════════════════════════════════╣
╠═ Désinstallation : Google Cloud CRC32C Hash Tool (Plat... ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Désinstallation : gcloud cli dependencies                ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Installation : BigQuery Command Line Tool                ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Installation : BigQuery Command Line Tool (Platform Sp...═╣
╠════════════════════════════════════════════════════════════╣
╠═ Installation : Cloud Storage Command Line Tool           ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Installation : Cloud Storage Command Line Tool (Platfo...═╣
╠════════════════════════════════════════════════════════════╣
╠═ Installation : Google Cloud CLI Core Libraries           ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Installation : Google Cloud CLI Core Libraries (Platfo...═╣
╠════════════════════════════════════════════════════════════╣
╠═ Installation : Google Cloud CRC32C Hash Tool (Platform...═╣
╠════════════════════════════════════════════════════════════╣
╠═ Installation : gcloud cli dependencies                   ═╣
╚════════════════════════════════════════════════════════════╝

Exécution des étapes de post-traitement... terminé.

Mise à jour effectuée !

Pour revenir à la version précédemment installée de l'interface de ligne de commande, vous pouvez exécuter :
  $ gcloud components update --version 507.0.0