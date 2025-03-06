---
audio: false
generated: false
lang: fr
layout: post
title: Nettoyer l’espace disque
translated: true
---

## Réglages

Utilisez le chemin Réglages -> Général -> Stockage -> Paramètres de stockage pour savoir comment l'espace disque est occupé et supprimer les fichiers inutiles.

## Trouver les Gros Fichiers

Utilisez `du` pour trouver les gros fichiers. Par exemple, utilisez la commande `du -hL -d 1 | sort -h`.

Dans un répertoire, utilisez `find . -type f -print0 | xargs -0 du -h | sort -rh | head -n 20`.

## Supprimer les Applications

Supprimez les applications dans le répertoire des applications.

## Téléchargements

Supprimez les fichiers dmg des packages téléchargés, qui peuvent être facilement téléchargés depuis Internet.

## Disque Portable

Achetez un disque portable et déplacez-y certains fichiers.

## iPhone

Importez les photos sur votre Mac et supprimez-les après l'importation.