---
audio: false
generated: true
lang: fr
layout: post
title: L'Impact de Rust sur Cloudflare
translated: true
type: note
---

L'adoption de Rust par Cloudflare a été transformative, motivée par son mélange unique de performance, de sécurité et d'évolutivité. Voici une analyse détaillée des raisons pour lesquelles Cloudflare a choisi Rust et des résultats tangibles qu'il a livrés :

---

### **Pourquoi Cloudflare utilise Rust**
1. **Sécurité mémoire sans compromettre les performances**
   - Le modèle de propriété de Rust élimine des classes entières de vulnérabilités (par exemple, les dépassements de tampon, les erreurs d'utilisation après libération) qui affectent le code C/C++, ce qui était crucial pour l'infrastructure axée sur la sécurité de Cloudflare.
   - Contrairement aux langages avec ramasse-miettes, Rust y parvient sans surcharge d'exécution, ce qui le rend idéal pour les systèmes hautes performances comme les proxys et l'informatique en périphérie.

2. **Concurrence et Évolutivité**
   - Le runtime asynchrone de Rust (Tokio) permet de gérer efficacement des millions de connexions simultanées, surpassant le modèle thread-par-requête de NGINX. Par exemple, Pingora, le proxy de Cloudflare basé sur Rust, traite **plus de 35 millions de requêtes par seconde** avec une utilisation CPU/mémoire réduite.
   - Le support asynchrone dans Workers (via `wasm-bindgen-futures`) permet aux Workers basés sur Rust de gérer les tâches liées aux E/S de manière transparente.

3. **Gains de Performance**
   - La pile QUIC/HTTP/3 propulsée par Rust de Cloudflare est **30% plus rapide** que son prédécesseur en C++, avec **35% d'utilisation mémoire en moins** et **50% de débit supérieur** sur le même matériel.
   - Les micro-optimisations en Rust (par exemple, réduire la latence par requête de quelques microsecondes) permettent d'économiser des milliers de dollars en coûts de calcul à l'échelle de Cloudflare.

4. **Productivité des Développeurs**
   - Le système de types solide de Rust et ses outils modernes (par exemple, Cargo) simplifient la maintenance et réduisent les bogues. Par exemple, Oxy, le framework de proxy de Cloudflare, permet de créer des applications riches en fonctionnalités avec **moins de 200 lignes de code**.
   - Le SDK Rust pour Workers (`workers-rs`) fournit des API ergonomiques pour KV, Durable Objects et l'IA, permettant un développement rapide.

5. **Écosystème et Pérennité**
   - L'adoption croissante de Rust (par exemple, AWS Lambda, Discord) s'aligne avec la vision à long terme de Cloudflare. L'open-sourcing de projets comme Pingora et Oxy favorise la collaboration communautaire.

---

### **Résultats de l'utilisation de Rust**
- **Pingora** : A remplacé NGINX, gérant des billions de requêtes mensuelles avec **une latence réduite** et **une meilleure résilience aux DDoS**.
- **Workers** : Le support de Rust permet des tâches intensives en calcul (par exemple, l'inférence d'IA) avec une vitesse quasi-naturelle, attirant des clients prestigieux comme les fintechs et les plateformes de livraison.
- **Fiabilité** : Les fonctionnalités de sécurité de Rust ont réduit les plantages dans des services critiques comme QUIC et TLS (par exemple, l'intégration de BoringSSL dans Oxy).
- **Économies de Coûts** : Les optimisations dans Pingora ont permis d'économiser **plus de 500 CPU** à l'échelle mondiale, ce qui se traduit par des économies opérationnelles significatives.

---

### **Défis et Atténuations**
- **Courbe d'Apprentissage** : La complexité de Rust a nécessité une formation initiale, mais Cloudflare l'a atténuée avec des bibliothèques internes (par exemple, `workers-rs`) et des modèles.
- **Limitations de Wasm** : Le support initial de Rust pour Workers avait des contraintes de taille, mais des outils comme `wasm-opt` et `worker-build` optimisent maintenant efficacement les binaires.

---

### **Orientations Futures**
Cloudflare continue d'étendre le rôle de Rust, notamment :
- **Conteneurs** : Les Durable Objects basés sur Rust alimentent la nouvelle orchestration de conteneurs (lancement prévu en juin 2025).
- **IA** : Workers AI utilise Rust pour l'inférence de modèles à faible latence.

En résumé, Rust est devenu une pierre angulaire de l'infrastructure de Cloudflare, offrant **sécurité, performance et évolutivité** tout en réduisant les coûts. Son adoption signale un changement plus large de l'industrie vers les langages mémoire-sécurisés pour les systèmes critiques.