---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Désactivation de la Notification Sonore de Ghostty
translated: true
type: note
---

### Qu'est-ce que l'« onglet de notification » de Ghostty ?

Dans Ghostty (un émulateur de terminal accéléré par GPU), l'« onglet de notification » fait probablement référence à la fonctionnalité de notification visuelle par cloche. Lorsqu'un caractère de cloche (`\a`) est envoyé par une commande ou une application en cours d'exécution dans le terminal (par exemple, par un processus de longue durée ou une erreur), Ghostty peut ajouter un emoji de cloche (🔔) au titre de l'onglet ou de la fenêtre concerné. Cela sert d'alerte subtile pour ramener votre attention sur cet onglet, surtout si le terminal n'est pas actif ou si vous travaillez dans un autre onglet. Cela fait partie du système de gestion de la cloche de Ghostty, qui vise à fournir des notifications non intrusives sans dépendre uniquement de l'audio ou des fenêtres contextuelles du système.

Ce comportement est activé par défaut dans la configuration `bell-features`, spécifiquement l'option `title`. Il est conçu pour être utile dans des flux de travail comme l'achèvement de tâches en arrière-plan, mais il peut être perçu comme une « notification » indésirable dans la barre d'onglets.

### Comment le désactiver

Pour annuler ou désactiver cette notification de titre par cloche (et potentiellement d'autres comportements de cloche), modifiez votre fichier de configuration Ghostty. L'emplacement par défaut est `~/.config/ghostty/config` sur Linux ou `~/Library/Application Support/com.mitchellh.Ghostty/config` sur macOS.

1.  Ouvrez le fichier de configuration dans votre éditeur préféré.
2.  Ajoutez ou modifiez la ligne suivante pour désactiver spécifiquement l'emoji dans le titre (tout en conservant d'autres fonctionnalités de cloche comme les demandes d'attention) :
    ```
    bell-features = no-title
    ```
    - Cela supprime le 🔔 du titre de l'onglet mais permet d'autres effets de cloche (par exemple, l'audio système ou la mise en surbrillance de la fenêtre).

3.  Pour une désactivation plus complète (pas d'emoji dans le titre, pas de demandes d'attention, etc.), utilisez :
    ```
    bell-features = false
    ```
    - Cela désactive toutes les fonctionnalités de cloche.

4.  Enregistrez le fichier et rechargez votre configuration dans Ghostty :
    - Appuyez sur `Cmd/Ctrl + Maj + ,` (ou exécutez `ghostty --reload-config` depuis un autre terminal).
    - Les nouvelles fenêtres/onglets utiliseront les paramètres mis à jour ; les existants peuvent nécessiter un redémarrage.

Si ce n'est pas la notification exacte que vous visez (par exemple, s'il s'agit d'une notification toast intégrée à l'application comme "Copié dans le presse-papiers" ou des notifications de bureau provenant d'applications), vous pouvez également les désactiver :
- Pour les notifications toast intégrées à l'application (Linux GTK uniquement) : `app-notifications = false`
- Pour les notifications de bureau des applications terminal : `desktop-notifications = false`

Testez en exécutant une commande qui déclenche une cloche, comme `echo -e '\a'`.

[Référence de configuration de Ghostty](https://ghostty.org/docs/config/reference)  
[Discussion sur les fonctionnalités de cloche de Ghostty](https://github.com/ghostty-org/ghostty/discussions/3242)