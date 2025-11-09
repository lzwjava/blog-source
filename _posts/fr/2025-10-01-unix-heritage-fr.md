---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Héritage Unix de macOS et Linux
translated: true
type: note
---

### Origines communes de macOS et Linux

macOS (anciennement OS X) et Linux partagent des racines conceptuelles communes avec Unix, un système d'exploitation multitâche pionnier développé aux Bell Labs dans les années 1970. Linux, créé par Linus Torvalds en 1991, est un noyau open-source inspiré d'Unix mais développé indépendamment — il n'est pas dérivé du code source d'Unix. macOS, quant à lui, est construit sur Darwin (un système d'exploitation de type Unix d'Apple, basé sur FreeBSD), qui inclut des composants Unix et est certifié conforme à Unix par The Open Group. Cette héritage commun explique de nombreuses similitudes dans les outils et les commandes, car les deux systèmes visent à fournir une fonctionnalité de type Unix.

Preuve à l'appui : Les normes d'Unix (par exemple, POSIX) ont influencé les deux systèmes pour assurer la compatibilité. Les distributions Linux comme Ubuntu sont explicitement de type Unix, et macOS hérite des outils Unix via BSD (Berkeley Software Distribution), une autre branche historique d'Unix.

### Pourquoi ils ont tous les deux la commande 'ps'

La commande 'ps' (process status) affiche des informations sur les processus en cours d'exécution et provient directement d'Unix, où elle a été implémentée pour la première fois dans les années 1970. macOS et Linux incluent tous deux 'ps' parce que :
- Cela fait partie de leur héritage Unix : macOS via Darwin/FreeBSD, et Linux via le système de fichiers PROC et les utilitaires standard des spécifications GNU ou POSIX.
- Elle est essentielle pour le diagnostic système, les scripts et l'administration, elle est donc inclue par défaut dans leurs ensembles d'outils de base (par exemple, dans le Terminal de macOS ou le shell de Linux).

La syntaxe de la commande, comme `ps -p pid -o pid,ppid,lstart,etime,command`, est prise en charge sur les deux systèmes en raison des normes POSIX partagées, bien que les options puissent varier légèrement (par exemple, macOS utilise des drapeaux de style BSD, tandis que Linux utilise souvent des variantes GNU). Ce n'est pas une coïncidence — c'est une filiation directe avec Unix.

### Peut-on dire que macOS et Linux sont tous les deux Unix ?

Pas exactement : « Unix » est une famille de systèmes d'exploitation et une marque déposée. macOS est qualifié d'Unix car Darwin est certifié (par The Open Group) et conforme à la Single Unix Specification (SUS). Linux, cependant, est un noyau qui forme la base de systèmes d'exploitation complets (distributions comme Debian), mais le noyau lui-même et ses distributions ne sont pas officiellement des « Unix » — ils sont de type Unix ou compatibles Unix en raison de leur adhésion à POSIX sans certification complète ou base de code partagée.

On pourrait dire qu'ils sont « de type Unix » ou « porteurs des traditions Unix », mais les qualifier tous de « Unix » serait inexact pour Linux. En pratique, cela n'a pas beaucoup d'importance pour la plupart des utilisateurs, car ils se comportent de manière similaire pour des commandes comme 'ps'. Si la rigueur est essentielle, vérifiez les certifications ou référez-vous aux définitions officielles.