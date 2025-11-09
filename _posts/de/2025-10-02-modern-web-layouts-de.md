---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: Moderne Webstile und Layouts
translated: true
type: note
---

### Übersicht
Dies scheint CSS-Code in SCSS (Sass)-Syntax zu sein, der Verschachtelung, &-Selektoren für Pseudoklassen und @extend-Direktiven verwendet. Er definiert Stile für ein einfaches Webseiten-Layout, Formulare, Buttons und Utilities mit einem sauberen, modernen Erscheinungsbild (z. B. abgerundete Ecken, weiche Schatten, Hover-Übergänge). Eigenschaften ohne Einheiten (wie `font-size 16px`) sind Kurzschreibweisen für SCSS. Ich werde ihn abschnittsweise aufschlüsseln und die Selektoren sowie ihre Wirkung erklären.

### Globale Stile (html, body)
```css
html, body
  font-family Verdana
  font-size 16px
  height 100%
  background-color #D2D2D2
```
- Wendet einen einfachen Font-Stack (Verdana als Fallback) mit einer Größe von 16px an.
- Setzt die volle Höhe (100%) für ein ganzseitiges Layout, oft für Zentrierung oder Abdeckung des Viewports.
- Der Hintergrund ist ein helles Grau (#D2D2D2) für eine neutrale Grundfarbe.

### Listen- und Link-Stile (ul, a)
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
- Entfernt standardmäßige Aufzählungspunkte, Padding und Ränder von ungeordneten Listen für ein saubereres, benutzerdefiniertes Styling.
- Links sind schwarz (#000), haben einen Pointer-Cursor beim Überfahren und keine Unterstreichung, was sie wie Buttons wirken lässt.

### Farb- und Text-Utility (.a-blue)
```css
.a-blue
  color #00BDEF
```
- Eine Klasse für blauen Text (#00BDEF, ein helles Blau), wahrscheinlich für Akzente.

### Button-Stile (.btn, .btn-blue, .btn-gray, .btn-gray-2)
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
- `.btn` ist eine Basisklasse für 3px abgerundete Ecken und 10px Padding.
- `.btn-blue`: Blauer Button (#00BDEF Hintergrund, weißer Text) mit Inset-Highlights und Schlagschatten für Tiefe. Hover verdunkelt das Blau mit einem sanften 0,5s Übergang.
- `.btn-gray` und `.btn-gray-2`: Graue Buttons (heller Hintergrund #eee, dunkler Text #333, dezente Randlinie #d5d5d5) mit ähnlichen Schatten. `.btn-gray-2` hat keinen expliziten Box-Shadow, aber den gleichen Hover-Effekt (heller zu #ddd). Nützlich für sekundäre Aktionen.

### Positionierungs-Utilities (.absolute-center, .full-space)
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
- `.absolute-center`: Zentriert ein Element absolut in seinem Elternelement (top/bottom/left/right auf 0, mit auto-Rändern).
- `.full-space`: Lässt ein Element den gesamten Raum seines Elternelements absolut ausfüllen.

### Formularstile (.base-form, input/textarea/select, button)
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
- `.base-form`: Erweitert `.absolute-center`, um ein modal-ähnliches Formular zu zentrieren (350px maximale Breite, 400px Höhe, weißer Hintergrund, 20px Randradius, zentrierter Text, inneres Padding). Ideal für Login-/Registrierungsformulare.
- Inputs, Textareas, Selects: Randlos mit Box-Sizing, um Padding in der Breite einzuschließen; kein Fokus-Outline, aber fügt einen dezenten grauen Schatten beim Fokussieren für bessere UX hinzu.
- Buttons: Entfernt standardmäßige Ränder und Outlines, geht davon aus, dass `.btn`-Stile für ein schöneres Erscheinungsbild sorgen.

Dieser Code richtet eine responsive, zentrierte Formularseite mit gestalteten Buttons und Eingabefeldern ein. Bei Verwendung von SCSS muss dieser in Standard-CSS kompiliert werden. Zur Anpassung können Farben oder Größen nach Bedarf geändert werden.