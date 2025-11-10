---
audio: false
generated: true
lang: fr
layout: post
title: Utiliser l'IA pour améliorer les produits dans les projets financiers
translated: true
type: note
---

Sur la base de votre expérience sur la plateforme Finance Transformation, où vous gérez des systèmes backend pour le traitement des données financières, les workflows et les intégrations avec des outils comme Java, Spring Boot et Db2, l'IA peut en effet jouer un rôle transformateur. Votre idée d'utiliser l'IA pour "rechercher des en-têtes financiers" s'aligne bien avec les applications de traitement du langage naturel (NLP), comme la conversion de requêtes utilisateur en SQL pour une récupération efficace des données. Cela peut démocratiser l'accès à des ensembles de données financières complexes, permettant aux parties prenantes non techniques (par exemple, les équipes financières) d'interroger des éléments tels que les écritures de grand livre, les en-têtes de transaction ou les statuts d'approbation sans écrire de code. Votre exemple de génération de SQL à partir du langage naturel est un point de départ parfait—analysons-le et élargissons-le à des applications plus vastes.

#### Analyse de votre exemple de génération SQL
Votre requête en langage naturel ("obtenir quelques utilisateurs dont le prénom est andy, créés autour du jour du mois dernier, qui ont 20 ans en 2025, et dont la dernière connexion remonte à la semaine dernière") est une démonstration solide de la façon dont l'IA peut faire le lien entre le langage courant et les opérations de base de données. La requête SQL générée que vous avez fournie est globalement efficace et utilise bien les fonctionnalités de PostgreSQL :

```sql
SELECT *
FROM users
WHERE first_name ILIKE 'andy'
  AND CAST(created_at AS DATE) BETWEEN 
      (CURRENT_DATE - INTERVAL '1 MONTH' - INTERVAL '1 DAY') 
      AND 
      (CURRENT_DATE - INTERVAL '1 MONTH' + INTERVAL '1 DAY')
  AND EXTRACT(YEAR FROM AGE(date_of_birth)) = 20
  AND last_login >= CURRENT_TIMESTAMP - INTERVAL '7 DAYS';
```

- **Points forts** :
  - `ILIKE 'andy'` gère l'insensibilité à la casse, ce qui est convivial pour l'utilisateur.
  - La clause `created_at` interprète "autour du jour du mois dernier" comme une fenêtre de ±1 jour autour de la date équivalente le mois dernier (par exemple, si nous sommes le 14 juillet 2025, elle interroge du 13 au 15 juin). C'est une approximation raisonnable pour "autour", bien que l'expression soit quelque peu ambiguë—les outils d'IA ont souvent besoin d'invites claires pour éviter les mauvaises interprétations.
  - `last_login >= CURRENT_TIMESTAMP - INTERVAL '7 DAYS'` capture avec précision "la semaine dernière".

- **Améliorations potentielles** :
  - La condition d'âge (`EXTRACT(YEAR FROM AGE(date_of_birth)) = 20`) calcule l'âge actuel au 14 juillet 2025, ce qui sélectionnerait les utilisateurs ayant exactement 20 ans aujourd'hui (en tenant compte du fait que leur anniversaire est passé ou non). Cependant, "20 ans en 2025" pourrait mieux signifier les utilisateurs qui auront 20 ans au cours de l'année 2025 (c'est-à-dire nés en 2005). Une alternative plus simple et plus précise pourrait être :
    ```sql
    AND date_of_birth BETWEEN '2005-01-01' AND '2005-12-31'
    ```
    Ou de manière équivalente :
    ```sql
    AND EXTRACT(YEAR FROM date_of_birth) = 2005
    ```
    Cela évite les calculs d'âge en temps d'exécution et se concentre sur l'année de naissance, ce qui est souvent plus stable pour les requêtes "en [année]" dans des contextes financiers ou de conformité (par exemple, l'éligibilité basée sur l'âge pour les comptes).
  - Pour la rendre plus robuste, ajoutez des limites (par exemple, `LIMIT 10`) si vous voulez "quelques utilisateurs", et envisagez les fuseaux horaires pour les horodatages si le système est global.
  - Dans un projet financier, adaptez cela à votre base de données Db2—la syntaxe PostgreSQL comme `AGE()` et `ILIKE` pourrait nécessiter des ajustements (par exemple, utilisez `CURRENT DATE - date_of_birth` pour l'âge et `LOWER(first_name) LIKE 'andy'`).

Les outils d'IA comme Copilot (que vous avez mentionné utiliser abondamment) ou les modèles avancés (par exemple, via des API d'OpenAI ou Google Cloud) excellent dans cette traduction NL-vers-SQL. Dans votre configuration, intégrez-la dans les workflows en créant une interface de chatbot qui analyse les requêtes sur les en-têtes financiers (par exemple, "Afficher les en-têtes non approuvés du dernier trimestre avec des soldes supérieurs à 10 000 $") et génère/exécute le SQL en toute sécurité, avec des garde-fous pour la sécurité.

#### Manières plus larges d'utiliser l'IA dans les systèmes backend financiers
Dans des projets comme le vôtre—axés sur l'importation/validation/exportation de données, les workflows et les systèmes bancaires—l'IA peut stimuler l'efficacité, réduire les erreurs et permettre l'innovation. En s'inspirant des tendances du secteur, voici des applications pratiques adaptées à l'ingénierie backend :

- **Automatisation du traitement et de la validation des données** :
  - Utilisez des modèles de machine learning (ML) pour détecter les anomalies dans les imports de données financières (par exemple, des écritures de grand livre inhabituelles ou des incohérences dans les en-têtes). Par exemple, entraînez des modèles sur des données historiques pour signaler les fraudes ou les erreurs lors de la validation, réduisant potentiellement les revues manuelles de 30 à 50 %. Des outils comme scikit-learn ou TensorFlow de Python (disponibles dans votre environnement) peuvent permettre de prototyper cela.
  - OCR et NLP pilotés par l'IA pour le traitement de documents : Extrayez automatiquement les données de PDF ou de relevés financiers scannés, en classant les en-têtes et en les intégrant à Db2.

- **Optimisation des workflows et des approbations** :
  - Mettez en œuvre une IA prédictive pour prévoir les goulots d'étranglement dans les workflows (par exemple, les retards d'approbation pour les nouveaux en-têtes) sur la base de modèles historiques. Cela pourrait utiliser l'analyse de séries chronologiques pour prioriser les tâches dans les plannings Control-M.
  - IA générative pour le routage dynamique : Dans les flux de soumission/approbation, l'IA peut suggérer les prochaines étapes ou approuver automatiquement les éléments à faible risque, accélérant ainsi les mises en production de l'UAT vers la production.

- **Amélioration du développement et de la maintenance du code** :
  - Comme vous l'avez fait avec Copilot pour l'analyse des causes racines, les scripts Python et la documentation, étendez cela aux revues de code assistées par l'IA ou à la correction de bugs. Pour les problèmes de multithreading dans Java/Spring Boot, l'IA peut générer des extraits de code optimisés ou profiler les performances (en complément de YourKit).
  - Votre idée d'agent IA basé sur AspectJ est innovante—collecter les logs et convertir les états de débogage en texte pour l'analyse par l'IA. Cela pourrait évoluer vers un "IDE spécifique au secteur bancaire" comme Cursor, où l'IA interroge les logs en langage naturel (par exemple, "Pourquoi cette transaction a-t-elle échoué ?") et suggère des correctifs. Pour implémenter : Utilisez AspectJ pour l'instrumentation, dirigez les logs vers un LLM (via l'API xAI ou similaire), et créez une boucle de rétroaction pour l'amélioration continue.

- **Analyses avancées et insights** :
  - Extensions NL-vers-SQL : Au-delà des requêtes, utilisez l'IA pour générer des rapports sur les tendances financières (par exemple, "Résumer les soumissions d'en-têtes par département le mois dernier").
  - Risque et conformité : Modèles d'IA pour l'évaluation du risque de crédit en temps réel ou les vérifications réglementaires, analysant les données du grand livre pour prédire les problèmes avant l'exportation.

- **Évolutivité et intégration** :
  - Exploitez l'IA pour l'optimisation du système, comme la mise à l'échelle automatique des ressources dans WebSphere basée sur les prévisions de charge.
  - Dans les configurations externalisées, l'IA peut standardiser la documentation (vous avez mentionné 50 guides), en les rendant consultables via la recherche sémantique.

Ces approches peuvent conduire à des économies (par exemple, des gains de productivité de 20 à 30 % dans l'ingénierie logicielle) et à de meilleurs produits, mais commencez modestement : Testez NL-vers-SQL dans un bac à sable, assurez la confidentialité des données (cruciale dans le secteur bancaire) et mesurez le ROI via des métriques comme le temps de déploiement réduit.

Si vous construisez cet agent IA, envisagez des frameworks open-source comme LangChain pour enchaîner l'analyse des logs avec la génération SQL. Pour les tarifs des API ou des abonnements, vérifiez les sites officiels car les détails varient.

**Références**  
- [AI and bank software development | Deloitte Insights](https://www.deloitte.com/us/en/insights/industry/financial-services/financial-services-industry-predictions/2025/ai-and-bank-software-development.html)  
- [AI in Banking: Applications, Benefits and Examples | Google Cloud](https://cloud.google.com/discover/ai-in-banking)  
- [Extracting value from AI in banking: Rewiring the enterprise | McKinsey](https://www.mckinsey.com/industries/financial-services/our-insights/extracting-value-from-ai-in-banking-rewiring-the-enterprise)  
- [AI in Finance: Applications, Examples & Benefits | Google Cloud](https://cloud.google.com/discover/finance-ai)  
- [Top AI Applications in Finance for 2025: [Benefits & Success Stories] | Acropolium](https://acropolium.com/blog/artificial-intelligence-applications-in-finance-real-world-success-cases/)  
- [QueryGPT - Natural Language to SQL using Generative AI | Uber Blog](https://www.uber.com/blog/query-gpt/)  
- [NL2SQL with BigQuery and Gemini | Google Cloud Blog](https://cloud.google.com/blog/products/data-analytics/nl2sql-with-bigquery-and-gemini)