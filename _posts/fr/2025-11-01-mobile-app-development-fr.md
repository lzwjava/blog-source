---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Plan de cours pour le développement d'applications mobiles
translated: true
type: note
---

### Plan de cours : 14567 Technologie de développement d'applications mobiles

**Informations sur le cours**
- **Code du cours** : 14567
- **Nom du cours** : Technologie de développement d'applications mobiles (移动应用开发技术)
- **Crédits** : 4
- **Niveau** : Spécialiste (专科)
- **Domaine professionnel** : Technologie d'application informatique (计算机应用技术)
- **Type d'examen** : Écrit (笔试) ; Note : Il existe un examen pratique séparé sous le code 14568 (1 crédit).
- **Autorité d'examen** : Examen d'auto-éducation de l'enseignement supérieur de la province du Guangdong (广东省高等教育自学考试)
- **Manuel** : *Didacticiel de cas de base pour le développement mobile Android (2e édition)* par Heima Programmer (黑马程序员), People's Posts and Telecommunications Press (人民邮电出版社), ISBN : 9787115567680 (2022). Le plan de cours s'aligne étroitement sur la structure de ce manuel, en mettant l'accent sur le développement Android comme exemple central pour la programmation d'applications mobiles.
- **Nature et objectifs du cours** : Il s'agit d'un cours pratique et orienté application pour les spécialités de génie logiciel et de technologie d'application informatique, axé sur les besoins du marché du travail. Il enseigne le développement d'applications mobiles en utilisant Android comme plateforme principale. Les apprenants maîtriseront les fondamentaux d'Android et apprendront à développer des applications mobiles, en combinant théorie et programmation pratique. L'accent est mis sur la construction d'un environnement de développement, la mise en œuvre d'interfaces utilisateur, la gestion des données et les fonctionnalités avancées comme le réseau et le multimédia. Les autodidactes doivent combiner l'étude théorique avec des expérimentations, en utilisant des outils comme Android Studio pour le débogage et les tests.

**Objectifs d'évaluation** :
Les examens testent les connaissances complètes en développement Android, incluant la mise en œuvre de code, la résolution de problèmes et la conception d'applications. L'accent est mis sur la compréhension de la syntaxe, de l'architecture et des scénarios pratiques. Les examens théoriques couvrent un large éventail de sujets de manière systématique ; la pratique met l'accent sur les compétences clés (par exemple, via l'examen séparé 14568). Utilisez des cartes mentales pour l'intégration des connaissances et des exercices pratiques pour la rétention.

**Contenu du cours et exigences d'évaluation**
Le contenu est structuré autour de 12 chapitres, progressant des bases vers des sujets avancés et un projet de synthèse. Chaque chapitre inclut de la théorie, des exemples de code, des exercices pratiques et des évaluations sur les concepts clés (par exemple, identification, application, analyse). Voici le plan hiérarchique :

1.  **Introduction aux bases d'Android**
    - Aperçu d'Android (technologie de communication, historique, architecture, Dalvik VM).
    - Configuration de l'environnement de développement (installation d'Android Studio, émulateur, SDK).
    - Développement et structure du premier programme.
    - Gestion des ressources (images, thèmes/styles, layouts, chaînes de caractères, couleurs, dimensions).
    - Débogage (tests unitaires, Logcat).
    *Exigences* : Comprendre l'écosystème Android ; construire et exécuter des applications simples.

2.  **Dispositions d'interface courantes sous Android**
    - Bases de View et écriture des layouts (XML vs code Java).
    - Attributs communs.
    - LinearLayout (ex. : interface de jeu d'association d'animaux).
    - RelativeLayout (ex. : interface de lecteur de musique).
    - TableLayout (ex. : interface de calculatrice).
    - FrameLayout (ex. : interface de lumière néon).
    *Exigences* : Concevoir des interfaces utilisateur réactives ; appliquer les layouts dans les projets.

3.  **Contrôles d'interface courants sous Android**
    - Contrôles simples (TextView, EditText, Button, ImageView, RadioButton, CheckBox, Toast).
    - Contrôles de liste (ListView avec adapters, RecyclerView ; ex. : centre commercial, fil d'actualités).
    - Vues personnalisées.
    *Exigences* : Implémenter des éléments interactifs ; gérer la liaison de données.

4.  **Unité d'activité du programme : Activity**
    - Cycle de vie (états, méthodes).
    - Création, configuration, démarrage/fermeture.
    - Intent et IntentFilter.
    - Sauts entre activités et transmission/retour de données (ex. : jeu du singe cueillant des pêches).
    - Piles de tâches et modes de lancement.
    - Utilisation des Fragments (cycle de vie, création, intégration ; ex. : menu Meituan).
    *Exigences* : Gérer le flux de l'application ; utiliser les fragments pour des interfaces utilisateur modulaires.

5.  **Stockage des données**
    - Aperçu des méthodes de stockage.
    - Stockage de fichiers (écriture/lecture ; ex. : sauvegarde de connexion QQ).
    - SharedPreferences (stocker/lire/supprimer ; ex. : connexion QQ).
    - Base de données SQLite (création, CRUD, transactions ; ex. : contacts de haricots verts).
    *Exigences* : Persister les données de manière sécurisée ; interroger/gérer les bases de données.

6.  **Content Provider**
    - Aperçu.
    - Création.
    - Accéder aux autres applications (interroger les données ; ex. : lire les contacts téléphoniques).
    - Observateurs de contenu (surveiller les changements ; ex. : détection de changement de données).
    *Exigences* : Partager des données entre applications ; implémenter des observateurs.

7.  **Mécanisme de diffusion (Broadcast)**
    - Aperçu.
    - Récepteurs de diffusion (BroadcastReceivers) (création).
    - Diffusions personnalisées (ex. : diffusion de la cafétéria).
    - Types de diffusion (ex. : compter les canards).
    *Exigences* : Gérer les événements système/application via les diffusions.

8.  **Services**
    - Aperçu et création.
    - Cycle de vie.
    - Méthodes de démarrage (startService, bindService).
    - Communication (locale/à distance ; ex. : lecteur de musique NetEase).
    *Exigences* : Exécuter des tâches en arrière-plan ; permettre la communication entre composants.

9.  **Programmation réseau**
    - Accès HTTP (HttpURLConnection).
    - Développement WebView (navigation HTML, support JS).
    - Analyse JSON (ex. : interface de marchandage Pinduoduo).
    - Mécanisme de message Handler.
    *Exigences* : Récupérer/analyser les données web ; gérer les opérations asynchrones.

10. **Traitement des graphiques et des images**
    - Classes de dessin (Bitmap, BitmapFactory, Paint, Canvas ; ex. : dessiner un chiot).
    - Effets d'image.
    - Animations (tween, image par image, propriété ; ex. : papillons/oiseaux volants).
    *Exigences* : Créer des visuels/animations ; optimiser les graphiques.

11. **Développement d'applications multimédias**
    - Lecture audio (MediaPlayer, SoundPool ; ex. : piano).
    - Lecture vidéo (VideoView, SurfaceView+MediaPlayer ; ex. : lecteurs vidéo).
    *Exigences* : Intégrer les médias ; contrôler la lecture.

12. **Projet complet : Imitation de Meituan Takeout**
    - Analyse du projet (aperçu, environnement, modules).
    - Démonstrations de l'interface utilisateur (boutiques, détails, commandes).
    - Préparation des données serveur.
    - Implémenter la liste des boutiques, les détails, le menu/panier, les commandes/paiement.
    *Exigences* : Intégrer tous les concepts dans une application complète.

**Notes supplémentaires et exigences de mise en œuvre**
- **Conseils d'étude** : Construire les environnements de laboratoire tôt ; coder avec les exemples. Se concentrer sur 70% de pratique, 30% de théorie. Utiliser les invites intégrées de l'IDE pendant les examens pratiques.
- **Format de l'examen** : Théorique : Choix multiples, questions à réponse courte, analyse de code (80% de couverture des chapitres 1-11). Pratique (14568) : Programmation pratique pour les fonctionnalités principales (ex. : interface utilisateur, stockage, services).
- **Mises à jour** : Les plans peuvent être ajustés avec les révisions du manuel ; vérifier les dernières informations auprès de l'Autorité d'examen de l'éducation du Guangdong (eea.gd.gov.cn).

Pour le PDF complet du syllabus officiel, visitez les ressources d'auto-examen du Guangdong ou téléchargez-le depuis des sites autorisés comme zikaosw.cn.

**Références**
- [Plan de cours d'auto-examen du Guangdong](https://eea.gd.gov.cn/attachment/0/532/532589/4262692.pdf)
- [Table des matières du manuel](https://resource.ityxb.com/book/android_case2.html)
- [Aperçu du programme d'auto-examen du Guangdong](https://www.zikaosw.cn/news/22151554.html)