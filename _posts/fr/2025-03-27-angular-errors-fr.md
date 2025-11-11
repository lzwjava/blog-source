---
audio: false
generated: true
lang: fr
layout: post
title: Erreurs Angular
translated: true
type: note
---

Lorsqu'ils travaillent avec Angular, les développeurs rencontrent souvent des exceptions et des erreurs spécifiques. Voici une liste catégorisée des problèmes courants, leurs causes et leurs solutions :

---

### **Erreurs de Template et de Liaison de Données**
1. **`ExpressionChangedAfterItHasBeenCheckedError`**
   - **Cause** : Modification des données du composant après le cycle de détection des changements d'Angular (par exemple, dans `ngAfterViewInit` ou `ngOnChanges`).
   - **Solution** : Utiliser `ChangeDetectorRef.detectChanges()` ou s'assurer que les changements de données se produisent avant la fin de la détection des changements.

2. **`Cannot read property 'X' of undefined`**
   - **Cause** : Accès à des propriétés d'objet non initialisées dans les templates (par exemple, `{{ user.name }}` lorsque `user` est `null`).
   - **Solution** : Utiliser l'opérateur de navigation sécurisée (`{{ user?.name }}`) ou initialiser correctement les objets.

3. **`Can't bind to 'X' since it isn't a known property of 'Y'`**
   - **Cause** : Déclaration manquante du composant/directive ou faute de frappe dans le nom de la propriété.
   - **Solution** : Importer la directive/le composant dans le module ou vérifier les fautes de frappe.

---

### **Erreurs d'Injection de Dépendances (DI)**
4. **`NullInjectorError: No provider for XService`**
   - **Cause** : Service non fourni dans le module/composant ou dépendance circulaire.
   - **Solution** : Ajouter le service au tableau `providers` du module/composant.

5. **`No value accessor for form control`**
   - **Cause** : Contrôle de formulaire personnalisé sans implémentation `ControlValueAccessor` ou liaison `formControlName` incorrecte.
   - **Solution** : Implémenter `ControlValueAccessor` pour les contrôles personnalisés ou vérifier les liaisons de formulaire.

---

### **Erreurs TypeScript et de Build**
6. **`Type 'X' is not assignable to type 'Y'`**
   - **Cause** : Incompatibilités de types (par exemple, un type de données incorrect passé à un composant).
   - **Solution** : S'assurer que les types correspondent ou utiliser des assertions de type (si intentionnel).

7. **`ERROR in Cannot find module 'X'`**
   - **Cause** : Package npm manquant ou chemin d'importation incorrect.
   - **Solution** : Installer le package (`npm install X`) ou corriger le chemin d'importation.

---

### **Erreurs de Composants et de Modules**
8. **`Component is not part of any NgModule`**
   - **Cause** : Composant non déclaré dans un module ou module non importé.
   - **Solution** : Ajouter le composant aux `declarations` de son module ou importer le module.

9. **`ViewDestroyedError: Attempt to use a destroyed view`**
   - **Cause** : Abonnements ou opérations asynchrones s'exécutant après la destruction du composant.
   - **Solution** : Se désabonner dans `ngOnDestroy` ou utiliser le pipe `async`.

---

### **Erreurs HTTP et API**
10. **`HttpClient provider not found`**
    - **Cause** : Import manquant du `HttpClientModule` dans le module.
    - **Solution** : Importer `HttpClientModule` dans `AppModule`.

11. **Problèmes CORS**
    - **Cause** : Le backend n'autorise pas les requêtes provenant de l'origine du frontend.
    - **Solution** : Configurer CORS sur le serveur ou utiliser un proxy dans Angular (`proxy.conf.json`).

---

### **Erreurs de Routage**
12. **`Route not found`**
    - **Cause** : Définition de route incorrecte ou module à chargement différé manquant.
    - **Solution** : Vérifier les chemins des routes et la syntaxe de chargement différé (`loadChildren: () => import(...)`).

---

### **Erreurs de Formulaire**
13. **`FormControl not found`**
    - **Cause** : Utilisation de `formControlName` sans encapsulation dans un `[formGroup]`.
    - **Solution** : S'assurer que le groupe de formulaires parent est initialisé et lié.

---

### **Divers**
14. **`Maximum call stack size exceeded`**
    - **Cause** : Fonctions récursives ou dépendances circulaires.
    - **Solution** : Restructurer le code pour éliminer la récursivité/les références circulaires.

15. **`Zone.js Promise rejection`**
    - **Cause** : Rejets de promesse non gérés.
    - **Solution** : Ajouter `.catch()` ou utiliser `try/catch` avec `async/await`.

16. **Erreurs de Compilation AOT**
    - **Cause** : Syntaxe de template incompatible avec la compilation Ahead-of-Time.
    - **Solution** : Éviter les expressions complexes dans les templates ou utiliser une syntaxe compatible Angular.

---

### **Bonnes Pratiques pour Éviter les Erreurs**
- Utiliser le pipe `async` pour les observables afin de se désabonner automatiquement.
- Activer les vérifications strictes de TypeScript (`strict: true` dans `tsconfig.json`).
- Exécuter `ng lint` pour détecter les problèmes de qualité de code.
- Tester avec le flag `--prod` pour simuler les builds AOT.

En abordant ces problèmes courants de manière méthodique, vous pouvez rationaliser le développement Angular et réduire le temps de débogage.