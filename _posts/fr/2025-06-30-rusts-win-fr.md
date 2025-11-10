---
audio: false
generated: true
lang: fr
layout: post
title: Amélioration des performances de Discord avec Rust
translated: true
type: note
---

L'adoption de Rust par Discord a été motivée par des goulots d'étranglement de performance dans leur service « Read States » basé sur Go, qui suit les lectures des messages par les utilisateurs à travers les canaux. Le passage à Rust a permis des améliorations significatives de la latence, a éliminé les pics de ramasse-miettes et a mis en avant les points forts de Rust en matière de gestion de la mémoire et de concurrence. Voici une analyse détaillée :

---

### **Pourquoi Discord est passé à Rust**
1.  **Problèmes de Ramasse-Miettes (GC) en Go**
    - Le service Go de Discord subissait des pics de latence toutes les ~2 minutes en raison du GC conservateur et non générationnel de Go, qui *devait parcourir l'intégralité du cache LRU* (contenant des millions d'objets) même avec une production minimale de déchets .
    - Le réglage du GC de Go (par exemple, l'ajustement de la taille du cache) n'a pas permis de résoudre les pics ou a empiré la latence au 99e centile .

2.  **Gestion de la Mémoire de Rust**
    - Le modèle de propriété de Rust *libère immédiatement la mémoire* lors de l'éviction du cache LRU, évitant les pauses induites par le GC. Cette approche déterministe a éliminé les pics de latence .
    - L'absence de surcharge d'exécution due au GC a permis des performances constantes sous charge élevée (des centaines de milliers de mises à jour par seconde) .

3.  **Optimisation des Performances**
    - Même une implémentation naïve en Rust égalait les performances de Go. Des optimisations supplémentaires (par exemple, l'utilisation de `BTreeMap` au lieu de `HashMap`, la réduction des copies mémoire) *ont réduit l'utilisation du CPU de 70 %* et ont ramené les temps de réponse moyens à quelques microsecondes .

4.  **Écosystème et Support Async**
    - Discord a adopté tôt les fonctionnalités async nightly de Rust (stabilisées par la suite), permettant des services en réseau efficaces sans les compromis du GC .

---

### **Résultats du Changement**
- **Latence** : Élimination des pics de GC de 2 minutes, permettant d'atteindre des temps de réponse inférieurs à la milliseconde .
- **Efficacité des Ressources** : Réduction de l'utilisation du CPU et de la mémoire, permettant au cache de monter en capacité jusqu'à 8 millions d'états de lecture sans dégradation des performances .
- **Fiabilité** : Moins de bugs à l'exécution grâce aux vérifications de sécurité à la compilation de Rust .

---

### **Avantages de Rust pour Discord**
1.  **Performances**
    - Latence faible et prévisible, idéale pour les services en temps réel .
    - Le contrôle fin de la mémoire surpasse les langages dépendants d'un GC .

2.  **Sécurité**
    - Le modèle de propriété empêche les fuites de mémoire, les pointeurs nuls et les accès concurrents aux données .
    - Sécurité de la concurrence sans synchronisation manuelle .

3.  **Outillage Moderne**
    - Cargo (gestionnaire de paquets) et les génériques avancés ont réduit le code répétitif par rapport à Go .

4.  **Croissance de l'Écosystème**
    - Les mises à niveau (par exemple, le runtime async Tokio) ont offert des gains de performance sans effort supplémentaire .

---

### **Inconvénients & Défis**
1.  **Courbe d'Apprentissage**
    - La propriété et les durées de vie de Rust nécessitent un investissement initial .

2.  **Limitations Initiales d'Async**
    - La dépendance initiale aux fonctionnalités nightly instables présentait des risques de maintenance .

3.  **Écosystème Plus Restreint**
    - Moins de bibliothèques que Go ou C++, bien qu'en croissance rapide .

---

### **Points Clés à Retenir**
Le succès de Discord avec Rust souligne son adéquation pour les *services sensibles à la latence et à grande échelle* où les pauses du GC sont inacceptables. Bien que la transition ait nécessité de surmonter la courbe d'apprentissage abrupte de Rust, le bénéfice a inclus **des performances plus rapides, une utilisation réduite des ressources et moins d'erreurs d'exécution**. Pour les équipes qui privilégient la maintenabilité à long terme et les performances, Rust offre des avantages convaincants par rapport aux langages dépendants d'un GC comme Go.

Pour des informations techniques plus approfondies, reportez-vous au [billet de blog original de Discord](https://discord.com/blog/why-discord-is-switching-from-go-to-rust).