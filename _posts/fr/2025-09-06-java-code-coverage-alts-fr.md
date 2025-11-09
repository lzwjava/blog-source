---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Alternatives aux outils de couverture de code Java
translated: true
type: note
---

En plus de **JaCoCo**, il existe plusieurs autres outils et plugins de couverture de code à considérer dans l'écosystème Java, en fonction de votre système de build et de vos besoins d'intégration :

### 1. **Cobertura**

* L'un des plus anciens frameworks de couverture de code pour Java.
* Fonctionne en instrumentant le bytecode.
* S'intègre avec Maven, Ant et Gradle.
* N'est pas aussi activement maintenu que JaCoCo, mais est encore utilisé dans certains systèmes hérités.

### 2. **Clover (par Atlassian)**

* Outil commercial (bien que les anciennes versions soient open source).
* Fournit des rapports de couverture détaillés, incluant la couverture des branches, l'optimisation des tests (exécution uniquement des tests pertinents) et les données historiques.
* Fonctionne bien avec les grands projets d'entreprise.

### 3. **OpenClover** (fork communautaire de Clover)

* Continuation open source de Clover après qu'Atlassian a arrêté le développement actif.
* Ensemble de fonctionnalités similaire à Clover, incluant la couverture par test et les rapports avancés.

### 4. **Pitest (Mutation Testing avec Couverture)**

* Principalement un outil de **test de mutation**, mais il génère également des rapports de couverture dans le cadre de l'analyse de mutation.
* Offre des garanties plus solides sur la qualité des tests qu'une simple couverture de lignes/branches.
* S'intègre facilement avec Maven/Gradle.

### 5. **EMMA**

* Outil de couverture léger pour Java.
* Est maintenant principalement considéré comme un outil hérité, mais était largement utilisé avant que JaCoCo ne gagne en popularité.
* Certains projets le conservent encore pour des raisons de compatibilité.

### 6. **TestNG / JUnit + Intégrations avec les outils de build**

* Bien que ce ne soient pas des outils de couverture autonomes, de nombreuses configurations de build modernes utilisent **Maven Surefire**, **Failsafe** ou les **plugins de test Gradle** conjointement avec JaCoCo, Cobertura ou Pitest pour intégrer la couverture directement dans les pipelines de test.

---

👉 En pratique, la plupart des équipes modernes utilisent **JaCoCo** (le mieux maintenu, largement supporté), mais si vous voulez des alternatives, **OpenClover** et **Pitest** méritent une considération sérieuse, surtout si vous souhaitez des informations *au-delà de la couverture* sur l'efficacité des tests.

Voulez-vous que j'explique également lesquels de ces outils s'intègrent le mieux avec les **pipelines Jenkins / SonarQube** (courants dans l'entreprise Java) ?