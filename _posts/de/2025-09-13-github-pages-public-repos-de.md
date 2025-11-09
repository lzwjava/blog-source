---
audio: false
date: 2025-09-13
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: GitHub Pages erfordert öffentliche Repositorys
translated: true
type: note
---

Richtig — wenn du dein GitHub Pages-Repository auf privat stellst, verlierst du das kostenlose GitHub Pages-Hosting.

GitHub Pages funktioniert nur automatisch, wenn das Repo **öffentlich** ist. Wenn das Repo privat ist, wird die `github.io`-Seite nicht veröffentlicht, es sei denn, du bist auf einem **GitHub Enterprise-Plan mit aktivierten Pages für private Repos** (das ist eine kostenpflichtige Funktion, die nicht in kostenlosen oder standardmäßigen persönlichen Konten enthalten ist).

Also für dein persönliches Blog unter `username.github.io`:

* **Öffentliches Repo** → GitHub Pages baut es auf und stellt es unter `https://username.github.io/` bereit.
* **Privates Repo (kostenloses Konto)** → GitHub Pages ist deaktiviert.
* **Privates Repo (Enterprise)** → Funktioniert weiterhin, aber nur, wenn deine Organisation Pages für private Repos aktiviert hat.

Möchtest du, dass ich auch einen Workaround erkläre (wie z.B. dein Haupt-Repo privat zu halten, aber nur die `_site`-Ausgabe in ein separates öffentliches Repo zur Veröffentlichung zu synchronisieren)?