---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Visibilité et alternatives du menu déroulant
translated: true
type: note
---

Dans l'extrait HTML fourni, vous utilisez des éléments `<select>`, qui s'affichent par défaut comme des menus déroulants. Cela signifie que les utilisateurs ne peuvent voir que l'option actuellement sélectionnée d'un coup d'œil — les autres options sont masquées jusqu'à ce que le menu déroulant soit cliqué ou déployé (via une interaction clavier/souris). C'est le comportement standard pour `<select>` en HTML, car il est conçu pour une sélection compacte dans une liste sans encombrer l'interface utilisateur.

HTML n'a pas d'élément "switch" intégré spécifiquement pour basculer la visibilité des options dans un `<select>`. Cependant, il existe plusieurs façons d'obtenir ce que vous décrivez (rendre toutes les options visibles sans menu déroulant, ou fournir un interrupteur pour les afficher/masquer). Je vais décrire les avantages/inconvénients et des exemples de code ci-dessous. Ces approches utilisent le HTML/CSS natif lorsque c'est possible, avec du JavaScript optionnel pour l'interactivité. Étant donné que votre code semble faire partie d'un site Jekyll (basé sur le templating Liquid), ceux-ci devraient s'intégrer facilement.

### 1. **Utiliser des Boutons Radio au lieu de `<select>` (Options Toujours Visibles)**
   - **Pourquoi ?** Les boutons radio (`<input type="radio">`) affichent toutes les options en ligne ou dans une liste, les rendant entièrement visibles sans aucune interaction. C'est idéal pour les petites listes (comme votre sélection de type avec 2 options) mais peut devenir encombrant pour les listes plus longues (comme votre tri par langue avec 9 options).
   - **Avantages :** Aucun JS nécessaire ; accessible ; les utilisateurs voient tout immédiatement.
   - **Inconvénients :** Prend plus d'espace ; nécessite du JS pour gérer la logique de "sélection" si vous devez déclencher des actions (par exemple, le tri/le filtrage des posts).
   - **Exemple de Code :**
     Remplacez votre `<select>` par un groupe de boutons radio. Enveloppez-les dans un `<fieldset>` pour la sémantique/l'accessibilité.

     ```html
     <div class="sort-container">
       <!-- Sélection du type sous forme de boutons radio -->
       <fieldset>
         <legend>Type</legend>
         <label>
           <input type="radio" name="type" value="posts" checked> Posts
         </label>
         <label>
           <input type="radio" name="type" value="notes"> Notes
         </label>
       </fieldset>

       <!-- Tri par langue sous forme de boutons radio -->
       <fieldset>
         <legend>Trier par Langue</legend>
         <label>
           <input type="radio" name="sort" value="en" checked> English
         </label>
         <label>
           <input type="radio" name="sort" value="zh"> 中文
         </label>
         <label>
           <input type="radio" name="sort" value="ja"> 日本語
         </label>
         <!-- Ajouter plus d'étiquettes pour es, hi, fr, de, ar, hant -->
       </fieldset>

       <div>
         <span id="post-number" class="post-number">
           {{ site[type].size }} {{ type }}
           ({{ site[type].size | divided_by: 7 | times: 6 }} Traduit par <a href="https://openrouter.ai">AI</a>)
         </span>
       </div>
     </div>
     ```

     - Ajoutez du CSS pour le style (par exemple, pour les faire ressembler à des boutons) :
       ```css
       fieldset {
         border: none; /* Supprimer la bordure par défaut */
         display: flex;
         gap: 10px;
       }
       label {
         background: #f0f0f0;
         padding: 5px 10px;
         border-radius: 5px;
         cursor: pointer;
       }
       input[type="radio"] {
         appearance: none; /* Masquer le cercle de radio par défaut */
       }
       input[type="radio"]:checked + span { /* Si vous utilisez <span> à l'intérieur du label pour le texte */
         background: #007bff;
         color: white;
       }
       ```
     - Pour la fonctionnalité : Utilisez du JS pour écouter les changements (par exemple, `addEventListener('change')`) et mettre à jour l'interface utilisateur ou déclencher un tri.

### 2. **Utiliser des Boutons ou des Divs pour des Options Clicables (Groupe de Boutons Personnalisé)**
   - **Pourquoi ?** Si vous voulez une interface plus semblable à des boutons, utilisez des éléments `<button>` ou `<div>` stylisés comme des boutons. Cela montre toutes les options visiblement et permet un basculement personnalisé.
   - **Avantages :** Style flexible ; peut imiter des onglets ou des pastilles ; facile à rendre responsive.
   - **Inconvénients :** Nécessite du JS pour gérer les états actifs et les actions ; pas aussi sémantiquement correct que les éléments de formulaire (utilisez les attributs ARIA pour l'accessibilité).
   - **Exemple de Code :**
     ```html
     <div class="sort-container">
       <!-- Type comme groupe de boutons -->
       <div class="button-group" role="group" aria-label="Sélection du type">
         <button data-type="posts" class="active">Posts</button>
         <button data-type="notes">Notes</button>
       </div>

       <!-- Langue comme groupe de boutons -->
       <div class="button-group" role="group" aria-label="Sélection de la langue">
         <button data-sort="en" class="active">English</button>
         <button data-sort="zh">中文</button>
         <button data-sort="ja">日本語</button>
         <!-- Ajouter plus de boutons pour les autres langues -->
       </div>

       <div>
         <span id="post-number" class="post-number">
           {{ site[type].size }} {{ type }}
           ({{ site[type].size | divided_by: 7 | times: 6 }} Traduit par <a href="https://openrouter.ai">AI</a>)
         </span>
       </div>
     </div>
     ```

     - CSS pour le style des boutons :
       ```css
       .button-group {
         display: flex;
         gap: 5px;
         flex-wrap: wrap; /* Pour les longues listes */
       }
       button {
         padding: 5px 10px;
         border: 1px solid #ccc;
         border-radius: 5px;
         cursor: pointer;
       }
       button.active {
         background: #007bff;
         color: white;
       }
       ```
     - JS pour gérer les clics (ajoutez ceci dans une balise `<script>` ou un fichier externe) :
       ```javascript
       document.querySelectorAll('.button-group button').forEach(button => {
         button.addEventListener('click', function() {
           // Retirer active des frères et sœurs
           this.parentNode.querySelectorAll('button').forEach(btn => btn.classList.remove('active'));
           this.classList.add('active');
           // Déclencher votre logique de tri ici, par exemple, mettre à jour post-number ou filtrer le contenu
           console.log('Sélectionné :', this.dataset.type || this.dataset.sort);
         });
       });
       ```

### 3. **Ajouter un Interrupteur pour Développer les Options (Approche Hybride)**
   - **Pourquoi ?** Si vous voulez conserver le `<select>` compact mais permettre aux utilisateurs de "basculer" vers une vue montrant toutes les options, utilisez une case à cocher stylisée comme un interrupteur pour afficher/masquer une liste développée.
   - **Avantages :** Garde la compacité par défaut ; HTML natif pour l'interrupteur.
   - **Inconvénients :** Nécessite du CSS/JS ; ajoute de la complexité.
   - **Exemple :** Utilisez `<input type="checkbox">` pour l'interrupteur, et basculez la visibilité d'une div listant toutes les options.
     ```html
     <div class="sort-container">
       <!-- Vos selects originaux ici -->

       <!-- Interrupteur -->
       <label class="switch">
         <input type="checkbox" id="show-all-toggle">
         <span>Afficher Toutes les Options</span>
       </label>

       <!-- Vue développée masquée -->
       <div id="expanded-options" style="display: none;">
         <!-- Lister toutes les options de type et de tri sous forme de texte brut ou de boutons -->
         <ul>
           <li>Posts</li>
           <li>Notes</li>
           <li>English</li>
           <li>中文</li>
           <!-- etc. -->
         </ul>
       </div>

       <!-- Votre span post-number -->
     </div>
     ```

     - CSS pour l'interrupteur :
       ```css
       .switch input {
         opacity: 0;
         width: 0;
         height: 0;
       }
       .switch span {
         /* Styliser comme un curseur d'interrupteur */
         position: relative;
         display: inline-block;
         width: 40px;
         height: 20px;
         background: #ccc;
         border-radius: 20px;
         transition: background 0.3s;
       }
       .switch input:checked + span {
         background: #007bff;
       }
       /* Ajouter un bouton de curseur avec ::before ou ::after */
       ```
     - JS pour basculer :
       ```javascript
       document.getElementById('show-all-toggle').addEventListener('change', function() {
         document.getElementById('expanded-options').style.display = this.checked ? 'block' : 'none';
       });
       ```

### Recommandations
- Pour votre **type-select** (seulement 2 options), les boutons radio ou les boutons fonctionnent bien et gardent les choses simples.
- Pour **sort-select** (9 langues), les boutons dans un groupe conviennent si l'espace le permet ; sinon, restez avec `<select>` et ajoutez une info-bulle ou une étiquette l'expliquant.
- Testez l'accessibilité (par exemple, en utilisant des lecteurs d'écran) et la réactivité mobile.
- Si c'est pour un site dynamique, intégrez avec votre JS existant pour mettre à jour le `post-number` en fonction des sélections.

Si cela ne correspond pas à ce que vous entendez par "switch", ou si vous partagez plus de contexte (par exemple, ce que font les selects), je peux affiner cela !