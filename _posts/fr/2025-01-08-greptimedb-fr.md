---
audio: false
generated: false
lang: fr
layout: post
title: Les entreprises devraient fournir un contexte ou des agents IA pour faciliter
  l'intégration
translated: true
---

J'ai un ami qui travaille chez Greptime DB, et j'ai réfléchi à la manière d'intégrer rapidement leur produit dans des systèmes existants.

## Contexte

Une approche potentielle consiste à fournir plus de contexte pour l'IA. Greptime DB pourrait organiser sa documentation de manière à être compatible avec des outils d'IA comme ChatGPT, simplifiant ainsi le processus d'intégration.

Greptime DB propose une documentation sur [https://greptime.com](https://greptime.com), mais je me demande si des outils comme ChatGPT ou DeepSeek peuvent traiter efficacement toutes les pages de leur documentation. De plus, une grande quantité d'informations est dispersée dans les dépôts GitHub, les issues, les documents internes, les documents publics, et d'autres fragments de connaissances cachées qui ne sont pas explicitement documentés.

Pour résoudre ce problème, Greptime DB pourrait avoir besoin de créer plusieurs GPT spécialisés. Par exemple, ils pourraient créer des invites comme celles-ci :

```

### Documentation de Greptime :  
La documentation officielle est disponible à l'adresse suivante : [https://docs.greptime.com](https://docs.greptime.com)

* [Guide de démarrage rapide](https://docs.greptime.com/getting-started/quick-start)  
* [Guide de l'utilisateur](https://docs.greptime.com/user-guide/overview)  
* [Démonstrations](https://github.com/GreptimeTeam/demo-scene)  
* [FAQ](https://docs.greptime.com/faq-and-others/faq)

### URLs des dépôts :
Voici les répertoires et fichiers clés à partir de la racine du dépôt GreptimeDB :

1. [benches](https://github.com/GreptimeTeam/greptimedb/tree/main/benches)  
2. [docs](https://github.com/GreptimeTeam/greptimedb/tree/main/docs)  
3. [src](https://github.com/GreptimeTeam/greptimedb/tree/main/src)  
4. [test](https://github.com/GreptimeTeam/greptimedb/tree/main/test)  
5. [third_party](https://github.com/GreptimeTeam/greptimedb/tree/main/third_party)  
6. [tools](https://github.com/GreptimeTeam/greptimedb/tree/main/tools)

Fichiers clés supplémentaires :

7. [Cargo.lock](https://github.com/GreptimeTeam/greptimedb/tree/main/Cargo.lock)  
8. [Cargo.toml](https://github.com/GreptimeTeam/greptimedb/tree/main/Cargo.toml)  
9. [LICENSE](https://github.com/GreptimeTeam/greptimedb/tree/main/LICENSE)  
10. [Makefile](https://github.com/GreptimeTeam/greptimedb/tree/main/Makefile)  
11. [README.md](https://github.com/GreptimeTeam/greptimedb/tree/main/README.md)  
12. [NOTICE](https://github.com/GreptimeTeam/greptimedb/tree/main/NOTICE)

Veuillez consulter ces ressources avant de répondre à toute requête utilisateur.

```

Cela permettrait aux utilisateurs d'interagir avec un chatbot basé sur GPT qui répond aux questions en se basant sur la documentation, garantissant ainsi des réponses plus précises.

Créons ce GPT : [https://chatgpt.com/g/g-677e87121d448191b0813ca28425ce38-greptimedb-integration](https://chatgpt.com/g/g-677e87121d448191b0813ca28425ce38-greptimedb-integration)

Je n'ai pas pu répondre à cette question,

```
De quoi parle `greptimedb/src/query/src/query_engine/context.rs` ?
```



## Agent

J'imagine un outil appelé `greptimedb-agent` pour simplifier le processus d'intégration.

Imaginez exécuter une simple commande comme :

```bash
pip install greptimedb-agent
greptimedb-agent
```

`greptimedb-agent` recueillera intelligemment des informations sur le système actuel, telles que les détails de la machine et le code existant, afin de comprendre le contexte et de décider de la meilleure façon d'intégrer Greptime DB.

Cette commande mettrait automatiquement à jour votre code pour intégrer Greptime DB, remplaçant de manière transparente votre base de données actuelle par Greptime DB en quelques étapes seulement.

