---
audio: false
generated: true
lang: fr
layout: post
title: Guide de dépannage des erreurs de l'API Avaloq
translated: true
type: note
---

## Guide Complet des Erreurs d'API Avaloq

### Erreurs Courantes au Niveau Système

**1. Erreurs d'Exécution de l'Agent Avaloq**
Erreur sur le système Avaloq ou sur Oracle lors de l'exécution du code de l'Agent Avaloq. Ces erreurs peuvent survenir si le job exécuté sur le système Avaloq se termine avec des erreurs.

**Dépannage :**
- Vérifier la connectivité à la base de données Oracle
- Vérifier la configuration de l'Agent Avaloq
- Examiner les logs système pour les problèmes liés à la base de données
- S'assurer des permissions appropriées pour l'utilisateur exécutant

**2. Erreurs d'Annulation de Job**
La ligne suivante dans le log signifie que le job a été annulé en raison d'une erreur interne sur le système Avaloq. Le statut final du job est valide pour l'Agent Avaloq : AAAA-MM-JJ hh:mm:ss Job 642 Execute: Job did complete with failures.

**Dépannage :**
- Examiner les logs des jobs pour les raisons spécifiques de l'échec
- Vérifier la disponibilité des ressources système
- Vérifier les paramètres et dépendances du job
- Surveiller les performances du système pendant l'exécution

### Erreurs d'API HTTP Standard dans un Contexte Bancaire

**1. 400 Bad Request**
Causes courantes dans les environnements Avaloq :
- Numéros de compte ou ID client invalides
- Montants de transaction mal formés
- Champs obligatoires manquants dans les ordres de trading
- Formats ou plages de dates invalides

**Dépannage :**
- Examiner l'URL pour s'assurer que les données envoyées sont valides et que les en-têtes corrects sont utilisés
- Valider tous les paramètres d'entrée par rapport aux exigences du schéma Avaloq
- Vérifier les codes et le formatage des devises
- Confirmer le statut et les permissions du compte

**2. 401 Unauthorized**
Causes spécifiques au secteur bancaire :
- Identifiants API invalides
- Jetons d'authentification expirés
- Permissions utilisateur insuffisantes pour des opérations spécifiques
- Restrictions liées à la relation client

**Dépannage :**
- Vérifier la validité de la clé API et du secret
- Vérifier les délais d'expiration des jetons
- Confirmer que l'utilisateur dispose des permissions bancaires appropriées
- Examiner les mappings des relations conseiller-client

**3. 403 Forbidden**
Contexte de gestion de patrimoine :
- Accès refusé à des comptes clients spécifiques
- Restrictions réglementaires sur les opérations
- Violations des règles de conformité
- Limitations basées sur la juridiction

**Dépannage :**
- Examiner les droits et rôles d'accès de l'utilisateur
- Vérifier les règles et restrictions de conformité
- Confirmer les permissions réglementaires
- Vérifier les autorisations de transaction transfrontalières

**4. 404 Not Found**
Scénarios spécifiques au secteur bancaire :
- Numéros de compte inexistants
- ID de portefeuille invalides
- Références de transaction manquantes
- Enregistrements clients supprimés ou archivés

**Dépannage :**
- Vérifier soigneusement votre endpoint et s'assurer qu'il est correctement orthographié
- Vérifier l'existence et le statut du compte
- Vérifier les comptes archivés ou inactifs
- Confirmer la construction correcte de l'URL

**5. 500 Internal Server Error**
Problèmes au niveau système :
- Problèmes de connectivité à la base de données
- Pannes du système bancaire central
- Interruptions des services d'intégration
- Problèmes de mémoire ou de performances

**Dépannage :**
- Vérifier les tableaux de bord d'état du système
- Examiner les pools de connexion à la base de données
- Surveiller l'utilisation des ressources système
- Vérifier la disponibilité des services dépendants

### Catégories d'Erreurs Spécifiques à Avaloq

**1. Erreurs d'Unité Commerciale**
Les jobs RA Avaloq qui font référence à une Unité Commerciale qui n'existe pas sur le système Avaloq peuvent être exécutés

**Problèmes Courants :**
- Références d'unité commerciale invalides
- Unités commerciales inactives ou supprimées
- Mappage incorrect de la hiérarchie organisationnelle

**2. Erreurs d'Intégration**
Basé sur les capacités d'intégration d'Avaloq :
- Incompatibilités de version d'API
- Échecs de validation de schéma
- Incompatibilités de format de message
- Problèmes de timeout avec les systèmes externes

**3. Erreurs de Conformité et Réglementaires**
- Échecs des vérifications pré-trade
- Erreurs de validation AML/KYC
- Problèmes de reporting réglementaire
- Restrictions sur les transactions transfrontalières

### Bonnes Pratiques pour la Gestion des Erreurs

**1. Journalisation et Surveillance**
- Mettre en place une journalisation complète pour tous les appels d'API
- Configurer des alertes pour les modèles d'erreur critiques
- Surveiller les temps de réponse d'API et les taux de réussite
- Suivre les modèles d'erreur spécifiques au métier

**2. Structure de la Réponse d'Erreur**
Les réponses d'erreur typiques d'Avaloq doivent inclure :
- Code et catégorie d'erreur
- Message d'erreur lisible par un humain
- Horodatage et ID de requête
- Étapes de correction suggérées

**3. Logique de Nouvelle Tentative**
- Mettre en œuvre un backoff exponentiel pour les erreurs transitoires
- Éviter de réessayer en cas d'échecs d'authentification
- Définir des limites maximales de tentatives
- Utiliser des modèles de disjoncteur pour les pannes système

**4. Tests et Validation**
Avaloq a posé de bonnes bases pour aider les entreprises à faciliter le parcours de test et d'intégration de nouvelles solutions en gérant les complexités à travers diverses phases en utilisant la solution sandbox d'Avaloq propulsée par AWS.

**Approche de Test Recommandée :**
- Utiliser l'environnement sandbox d'Avaloq pour les tests
- Tester systématiquement les scénarios d'erreur
- Valider la gestion des erreurs pour différents rôles utilisateur
- Tester les points d'intégration avec les systèmes externes

### Stratégies de Prévention des Erreurs

**1. Validation des Entrées**
- Valider tous les paramètres d'entrée avant les appels d'API
- Utiliser les types et formats de données appropriés
- Mettre en œuvre une validation côté client lorsque c'est approprié
- Vérifier les règles métier avant la soumission

**2. Gestion des Connexions**
- Mettre en œuvre un pool de connexions approprié
- Gérer les timeouts avec élégance
- Utiliser des contrôles de santé pour les services dépendants
- Surveiller les limites de débit de l'API

**3. Considérations de Sécurité**
- Mettre en œuvre une gestion d'authentification appropriée
- Utiliser des canaux de communication sécurisés
- Journaliser de manière appropriée les erreurs liées à la sécurité
- Manipuler avec soin les données sensibles dans les messages d'erreur

Pour les codes d'erreur spécifiques et les procédures de dépannage détaillées, consultez la documentation de votre système Avaloq ou contactez directement le support Avaloq, car de nombreux détails d'erreur sont spécifiques à votre implémentation et configuration.