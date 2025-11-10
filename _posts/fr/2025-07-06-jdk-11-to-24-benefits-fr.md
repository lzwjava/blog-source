---
audio: false
generated: true
lang: fr
layout: post
title: Avantages de la mise à niveau vers JDK 24 expliqués
translated: true
type: note
---

La mise à niveau de JDK 11 vers JDK 24 offre des avantages significatifs dans divers aspects, notamment les performances, les nouvelles fonctionnalités et la sécurité. Voici une analyse détaillée :

**1. Améliorations des performances :**

*   **Fils d'exécution virtuels (Project Loom) :** Bien qu'introduits dans JDK 21, JDK 24 affine davantage les fils d'exécution virtuels (JEP 491 : Synchronize Virtual Threads Without Pinning). Il s'agit d'un changement majeur pour les applications à haute concurrence, permettant des millions de fils d'exécution légers sans la surcharge des fils d'exécution de plateforme traditionnels. Cela peut considérablement améliorer l'évolutivité et la réactivité, en particulier pour les applications côté serveur.
*   **Démarrage plus rapide :** JDK 24 inclut le "Chargement et Liaison de Classes Ahead-of-Time" (JEP 483), qui rend les classes d'application instantanément disponibles au démarrage de la JVM, réduisant ainsi les temps de démarrage. Ceci est particulièrement bénéfique pour les microservices et les applications cloud-natives où un démarrage rapide est crucial.
*   **En-têtes d'objets compacts (Expérimental) :** JEP 450 vise à réduire la taille des en-têtes d'objets sur les architectures 64 bits, ce qui peut entraîner des économies de mémoire significatives (10-20 %) et une meilleure localité du cache, en particulier pour les applications avec de nombreux petits objets.
*   **Mode Générationnel ZGC (Par Défaut) :** Le Garbage Collector Z (ZGC) utilise maintenant par défaut un mode générationnel (JEP 490), optimisant le garbage collection pour les objets à courte durée de vie. Cela peut conduire à une réduction des temps de pause et une meilleure efficacité mémoire pour les gros tas.
*   **Stream Gatherers (JEP 485) :** Cette nouvelle API permet des opérations intermédiaires personnalisées dans les pipelines Stream, offrant plus de flexibilité et des transformations de données potentiellement plus efficaces.
*   **Opérations en Masse Optimisées de l'API Foreign Function & Memory :** Les opérations de mémoire en masse utilisent maintenant du code Java au lieu de méthodes natives, conduisant à de meilleures performances sur certaines architectures (par exemple, Linux x64/AArch64), en particulier pour les petites tailles de données.
*   **Amélioration du Démarrage de la Concatenation de Chaînes :** Des optimisations internes de la concaténation de chaînes entraînent un démarrage plus rapide et moins de surcharge de génération de code.

**2. Nouvelles Fonctionnalités du Langage et APIs :**

*   **Améliorations du Pattern Matching (JEP 488) :** Améliorations supplémentaires du pattern matching, permettant l'utilisation de types primitifs dans les motifs et étendant `instanceof` et `switch` pour fonctionner avec tous les types primitifs, rendant le code plus concis et lisible.
*   **Scoped Values (JEP 487) :** Une API en préversion qui offre un moyen plus sûr et plus efficace de partager des données immuables au sein d'un fil d'exécution et avec les fils enfants, particulièrement bénéfique avec les fils d'exécution virtuels.
*   **Concurrence Structurée (JEP 499) :** Une API en préversion qui simplifie la programmation concurrente en traitant les groupes de tâches connexes comme une seule unité, améliorant la gestion des erreurs, l'annulation et l'observabilité.
*   **API Class-File (JEP 484) :** Une API standard pour l'analyse, la génération et la transformation des fichiers de classe Java.
*   **API Vector (JEP 489) :** (Toujours en incubateur) Cette API permet d'exprimer des calculs vectoriels qui se compilent en instructions vectorielles optimales sur les CPU pris en charge, conduisant à des performances supérieures pour certaines opérations numériques.
*   **API Key Derivation Function (JEP 478) :** Une API en préversion pour les algorithmes cryptographiques utilisés pour dériver des clés supplémentaires à partir d'une clé secrète.

**3. Améliorations de la Sécurité :**

*   **Cryptographie Post-Quantique :** JDK 24 introduit des implémentations du Module-Lattice-Based Key-Encapsulation Mechanism (ML-KEM) (JEP 496) et du Module-Lattice-Based Digital Signature Algorithm (ML-DSA) (JEP 497) résistants aux ordinateurs quantiques, préparant Java aux futurs défis cryptographiques.
*   **Améliorations TLS :** Des améliorations comme le nombre configurable de nouveaux tickets de session pour TLSv1.3 et un mécanisme pour désactiver les suites de chiffrement TLS par correspondance de motif. Les suites de chiffrement TLS_RSA sont maintenant désactivées par défaut pour une meilleure confidentialité persistante.
*   **Suppression du Security Manager (JEP 486) :** Le Security Manager, une fonctionnalité héritée, est définitivement désactivé. Cela simplifie le modèle de sécurité de la JVM et encourage l'utilisation de pratiques de sécurité modernes comme le sandboxing basé sur les conteneurs.
*   **Avertissements pour `sun.misc.Unsafe` :** JDK 24 émet des avertissements à l'exécution lorsque les méthodes d'accès mémoire dans `sun.misc.Unsafe` sont utilisées, encourageant la migration vers des alternatives plus sûres comme l'API VarHandle et l'API Foreign Function & Memory.

**4. Dépréciations et Suppressions :**

*   Bien que celles-ci puissent nécessiter des modifications de code, elles contribuent à une plateforme plus propre, plus sécurisée et plus maintenable. La désactivation permanente du Security Manager et les avertissements pour `sun.misc.Unsafe` en sont des exemples.

**5. Considérations sur le Support à Long Terme (LTS) :**

*   JDK 11 est une version LTS, avec un support étendu d'Oracle disponible jusqu'en janvier 2032.
*   JDK 24 n'est *pas* une version LTS. La prochaine version LTS après JDK 21 est prévue pour être JDK 25 en septembre 2025.
*   Cela signifie que si vous effectuez une mise à niveau vers JDK 24, vous devrez planifier une autre mise à niveau vers JDK 25 (ou une LTS ultérieure) relativement rapidement pour garantir un support à long terme continu et des mises à jour de sécurité.

**En résumé :**

La mise à niveau vers JDK 24 à partir de JDK 11 offre une multitude de nouvelles fonctionnalités, des gains de performance significatifs (en particulier avec les fils d'exécution virtuels et le démarrage plus rapide) et des améliorations de sécurité cruciales. Cependant, il est important de prendre en compte le cycle de vie du support, car JDK 24 est une version non-LTS, ce qui signifie qu'une mise à niveau ultérieure vers JDK 25 (la prochaine LTS) sera nécessaire pour la stabilité et le support à long terme.