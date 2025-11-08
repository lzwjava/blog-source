---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Cultiver un langage par Guy Steele
translated: true
type: note
---

### Aperçu
La conférence « Growing a Language » a été prononcée par Guy L. Steele Jr. à OOPSLA '98 (conférence sur la programmation orientée objet, les systèmes, les langages et les applications) à Vancouver, Canada, le 19 octobre 1998. C'est une présentation séminale de 45 minutes sur la conception et l'évolution des langages, utilisant Scheme (un dialecte de Lisp) comme démonstration de codage en direct. Steele, co-concepteur de Java et Scheme, illustre comment construire un langage de programmation de manière incrémentale à partir de zéro, en mettant l'accent sur la simplicité, l'expressivité et l'extensibilité. L'idée centrale est que les langages « poussent » organiquement en commençant par des primitives minimales et en ajoutant des fonctionnalités par couches, plutôt que de tout concevoir en une seule fois.

La vidéo est disponible sur YouTube (archivée par ACM SIGPLAN) et a influencé les discussions modernes sur la conception des langages, y compris dans les langages fonctionnels et les langages dédiés embarqués (DSL).

### Thèmes clés et structure
Steele structure la conférence comme un tutoriel pratique, codant en direct en Scheme pour « faire pousser » un évaluateur d'expressions simple en un langage complet. Il utilise des métaphores comme le « jardinage » (favoriser les fonctionnalités) contre l'« architecture » (plans rigides) pour défendre la conception évolutive. Voici une répartition des sections principales :

1.  **Introduction : Pourquoi faire pousser un langage ? (0:00–5:00)**
    Steele motive la conférence en critiquant la conception de langage en « big bang » (par exemple, tout spécifier à l'avance, conduisant à l'embonpoint). Il propose plutôt de « faire pousser » : commencer petit, tester souvent et étendre en fonction des besoins réels. Il s'inspire de l'histoire de Lisp, où le langage a grandi à partir du code de l'évaluateur. Objectif : Construire un petit langage pour les expressions arithmétiques qui peut évoluer vers quelque chose de Turing-complet.

2.  **Graine : Évaluateur de base (5:00–10:00)**
    Commence par le noyau le plus simple : une fonction qui évalue les nombres atomiques (par exemple, `3` → 3).
    - Extrait de code (en Scheme) :
      ```scheme
      (define (eval exp) exp)  ; Identité pour les atomes
      ```
    Il l'exécute en direct, montrant que `(eval 3)` renvoie 3. C'est la « graine » — pure, sans sucre syntaxique.

3.  **Germination : Ajout d'opérations (10:00–20:00)**
    Introduit des opérateurs binaires comme `+` et `*` en faisant correspondre des motifs sur des listes (par exemple, `(+ 2 3)`).
    - Fait grandir l'évaluateur :
      ```scheme
      (define (eval exp)
        (if (pair? exp)
            (let ((op (car exp))
                  (args (cdr exp)))
              (apply op (map eval args)))
            exp))
      ```
    Montre l'évaluation : `(+ (* 2 3) 4)` → 10. Souligne l'hygiène — garder la simplicité, éviter l'optimisation prématurée.

4.  **Ramification : Conditionnelles et variables (20:00–30:00)**
    Ajoute `if` pour les conditionnelles et `let` pour lier les variables, montrant comment la portée émerge naturellement.
    - Exemple de croissance :
      ```scheme
      (define (eval exp env)
        (if (pair? exp)
            (case (car exp)
              ((quote) (cadr exp))
              ((if) (if (eval (cadr exp) env)
                        (eval (caddr exp) env)
                        (eval (cadddr exp) env)))
              ((let) (eval (cadddr exp) (extend-env env (caadr exp) (eval (cadadr exp) env))))
              (else ...))  ; Retour à l'application de fonction
            (lookup exp env)))  ; Recherche de variable
      ```
    Démo en direct : Calcule des factorielles via des liaisons `let` récursives, soulignant comment la récursion « pousse » à partir de l'itération.

5.  **Floraison : Macros et abstraction (30:00–40:00)**
    Introduit des macros hygiéniques pour ajouter une syntaxe spécifique à un domaine (par exemple, une boucle `while`). Montre comment les macros permettent aux utilisateurs de « faire pousser » le langage eux-mêmes.
    - Idée clé : Les langages devraient être « ouverts » à l'extension, comme le système de macros de Lisp, permettant des DSL sans bifurquer le noyau.

6.  **Conclusion : Leçons pour les concepteurs (40:00–45:00)**
    Steele conclut avec des principes :
    - **Incrémentalisme** : Ajouter une fonctionnalité à la fois ; tester immédiatement.
    - **Uniformité** : Réutiliser les primitives (par exemple, tout est une expression).
    - **Autonomisation de l'utilisateur** : Permettre aux utilisateurs d'étendre via des macros ou similaire.
    Il le lie à des langages du monde réel (Java, Scheme) et met en garde contre le « feature creep ». La Q&R aborde les performances et les défis de mise en œuvre.

### Impact et points à retenir
Cette conférence a popularisé les idées de « language workbench », influençant des outils comme Racket (qui étend Scheme) et des concepts dans les macros de Rust ou les extensions de Swift. C'est une masterclass pour penser les langages comme des systèmes vivants — pratique, philosophique et divertissante (l'humour pince-sans-rire de Steele y brille).

Pour l'expérience complète, regardez la vidéo : [Growing a Language - OOPSLA '98](https://www.youtube.com/watch?v=_ahvzDzKdB0). Les transcriptions/résumés sont rares, mais le code est reconstructible à partir des diapositives (disponibles via ACM Digital Library). Si vous êtes passionné par la conception de langages, associez-la avec la conférence ultérieure de Steele « Growing a Pattern Language » (OOPSLA '05).