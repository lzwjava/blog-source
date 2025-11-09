---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Technischer Stack des Yin Wang Blogs
translated: true
type: note
---

Die Website (https://www.yinwang.org/, mit dem Titel "当然我在扯淡") scheint ein individuell erstellter Blog zu sein. Basierend auf dem bereitgestellten HTML-Quellcode:

- **Framework**: Sie ist primär mit **Vue.js** (wahrscheinlich Version 3) gebaut, erkennbar an Vue-spezifischen Attributen wie `data-v-app`, `data-v-[hash]` für gescopten CSS und Komponentenreferenzen (z.B. `HomeView`, `PostView`, `router-link-active` für die Navigation mit Vue Router).
- **Build-Tool**: **Vite** wird für Bundling und Entwicklung verwendet, erkennbar am Favicon (`/vite.svg`), vorab geladenen Modul-Skripten mit gehashten Dateinamen (z.B. `/assets/index-DS_1rR7p.js`) und der allgemeinen Asset-Struktur, die typisch für Vites Output ist.
- **Styling**: **Tailwind CSS** für Utility-First-Klassen (z.B. `bg-gray-50 dark:bg-gray-900`, `flex items-center`, responsive Präfixe wie `sm:px-4`).
- **Weitere Anmerkungen**: Keine Hinweise auf Server-Side Rendering (z.B. keine Nuxt.js-Spuren), daher handelt es sich wahrscheinlich um eine statische Site oder eine Client-seitig gerenderte SPA. Der Inhalt (Beiträge, Tags, Paginierung) deutet auf ein einfaches, individuelles Setup für einen persönlichen Blog hin, möglicherweise mit Markdown für die Beitragsinhalte.

Es ist **nicht alles manuell geschrieben** – das HTML wird während des Build-Prozesses automatisch aus Vue-Komponenten und Templates generiert. Die Kernlogik (Routing, Komponenten) ist in JS/TS codiert, aber die endgültige Ausgabe sind optimierte statische Dateien. Keine Anzeichen für einen vollwertigen Static Site Generator wie Hugo oder Jekyll; es handelt sich eher um ein leichtgewichtiges Vue + Vite Projekt.

[当然我在扯淡](https://www.yinwang.org/)