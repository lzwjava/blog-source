---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Styles et Dispositions Web Modernes
translated: true
type: note
---

### Aperçu
Il s'agit de code CSS écrit en syntaxe SCSS (Sass), comportant de l'imbrication, des sélecteurs esperluette (&) pour les pseudo-classes et des directives @extend. Il définit les styles pour une mise en page de page web basique, des formulaires, des boutons et des utilitaires, avec une esthétique moderne et épurée (par exemple, coins arrondis, ombres douces, transitions au survol). Les propriétés sans unité (comme `font-size 16px`) sont des raccourcis SCSS. Je vais le décomposer par section, en expliquant les sélecteurs et leurs effets.

### Styles globaux (html, body)
```css
html, body
  font-family Verdana
  font-size 16px
  height 100%
  background-color #D2D2D2
```
- Applique une pile de polices simple (Verdana en secours si nécessaire) avec une taille de 16px.
- Définit une hauteur pleine (100%) pour une mise en page pleine page, souvent pour centrer ou couvrir la fenêtre d'affichage.
- L'arrière-plan est un gris clair (#D2D2D2) pour une couleur de base neutre.

### Styles de liste et de lien (ul, a)
```css
ul
  list-style-type none
  padding 0
  margin 0

a
  color #000
  cursor pointer
  text-decoration none
```
- Supprime les puces, le remplissage et les marges par défaut des listes non ordonnées pour un style personnalisé plus épuré.
- Les liens sont noirs (#000), ont un curseur de type pointeur au survol et pas de soulignement, leur donnant une apparence de bouton.

### Utilitaire de couleur et de texte (.a-blue)
```css
.a-blue
  color #00BDEF
```
- Une classe pour du texte bleu (#00BDEF, un bleu clair), probablement pour des accents.

### Styles de bouton (.btn, .btn-blue, .btn-gray, .btn-gray-2)
```css
.btn
  border-radius 3px
  padding 10px

.btn-blue
  background #00BDEF
  color #fff
  -webkit-box-shadow 0px 1px 0px rgba(255,255,255,0.15) inset,0px 1px 2px rgba(0,0,0,0.15)
  box-shadow 0px 1px 0px rgba(255,255,255,0.15) inset,0px 1px 2px rgba(0,0,0,0.15)
  &:hover
    background #00ABD8
    transition .5s

.btn-gray
  background #eee
  color #333
  border 1px solid #d5d5d5
  border-radius 3px
  -webkit-box-shadow 0px 1px 0px rgba(255,255,255,0.15) inset,0px 1px 2px rgba(0,0,0,0.15)
  box-shadow 0px 1px 0px rgba(255,255,255,0.15) inset,0px 1px 2px rgba(0,0,0,0.15)
  &:hover
    background #ddd
    transition 0.5s

.btn-gray-2
  background #eee
  color #333
  border 1px solid #d5d5d5
  border-radius 3px
  &:hover
    background #ddd
    transition 0.5s
```
- `.btn` est une classe de base pour des coins arrondis de 3px et un remplissage de 10px.
- `.btn-blue` : Bouton bleu (arrière-plan #00BDEF, texte blanc) avec des reflets en incrustation et des ombres portées pour la profondeur. Le survol assombrit le bleu avec une transition fluide de 0.5s.
- `.btn-gray` et `.btn-gray-2` : Boutons gris (arrière-plan clair #eee, texte foncé #333, bordure subtile #d5d5d5) avec des ombres similaires. `.btn-gray-2` n'a pas d'ombre de boîte explicite mais a le même effet de survol (s'éclaircit vers #ddd). Utile pour les actions secondaires.

### Utilitaires de positionnement (.absolute-center, .full-space)
```css
.absolute-center
    margin auto
    position absolute
    top 0
    left 0
    bottom 0
    right 0

.full-space
    position absolute
    top 0
    left 0
    bottom 0
    right 0
```
- `.absolute-center` : Centre un élément de manière absolue dans son parent (haut/bas/gauche/droite à 0, avec des marges automatiques).
- `.full-space` : Fait en sorte qu'un élément remplisse entièrement l'espace de son parent de manière absolue.

### Styles de formulaire (.base-form, input/textarea/select, button)
```css
.base-form
  @extend .absolute-center
  max-width 350px
  height 400px
  background #fff
  border-radius 20px
  text-align center
  padding 20px 10px

input, textarea, select
  box-sizing border-box
  border none
  outline none
  &:focus
    border none
    outline none
    box-shadow 0px 1px 4px 0px rgba(0,0,0,.06)
    -webkit-box-shadow 0px 1px 4px 0px rgba(0,0,0,.06)

button
  border-style none
  outline none
```
- `.base-form` : Étend `.absolute-center` pour centrer un formulaire de type modale (largeur max 350px, hauteur 400px, arrière-plan blanc, bordure arrondie de 20px, texte centré, remplissage intérieur). Idéal pour les formulaires de connexion/d'inscription.
- Inputs, textareas, selects : Sans bordure avec box-sizing pour inclure le remplissage dans la largeur ; pas de contour de focus, mais ajoute une ombre grise subtile au focus pour l'UX.
- Boutons : Supprime les bordures et contours par défaut, en supposant que les styles `.btn` seront appliqués pour une apparence plus agréable.

Ce code configure une page de formulaire réactive et centrée avec des boutons et des champs stylisés. Si vous utilisez SCSS, compilez-le en CSS standard. Pour la personnalisation, ajustez les couleurs ou les tailles selon les besoins.