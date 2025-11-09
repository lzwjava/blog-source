---
audio: false
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: Git Rebase Drop entfernt Commits
translated: true
type: note
---

Ja — genau.

Wenn du **`drop`** während eines interaktiven `git rebase -i` verwendest, bedeutet das **„diesen Commit vollständig aus dem Verlauf entfernen.“**

Hier ist, was passiert:

* Git wird diesen Commit **überspringen und nicht anwenden**, während es die anderen erneut anwendet.
* Der resultierende Branch sieht so aus, als ob dieser Commit **nie existiert hätte** — seine Änderungen und seine Commit-Nachricht sind beide verschwunden.
* Die folgenden Commits werden weiterhin angewendet (sofern sie nicht von den entfernten Änderungen abhängen).

Beispiel:

```bash
git rebase -i HEAD~4
```

Du könntest so etwas sehen:

```
pick a1b2c3d Tippfehler korrigieren
pick b2c3d4e README hinzufügen
pick c3d4e5f Login implementieren
pick d4e5f6g Debug-Log hinzufügen
```

Wenn du die letzte Zeile änderst in:

```
drop d4e5f6g Debug-Log hinzufügen
```

dann wird Git, nachdem du den Editor speicherst und schließt, den Branch rebasen und **diesen Commit ausschließen**.

Also ja — „drop“ = **lösche den Commit aus der Branch-Historie.**

Möchtest du, dass ich erkläre, wie sich das von `revert` unterscheidet (was einen Commit *rückgängig macht*, aber einen Vermerk darüber beibehält)?