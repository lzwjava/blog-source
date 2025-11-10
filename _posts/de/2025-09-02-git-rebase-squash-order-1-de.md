---
audio: false
generated: true
image: false
lang: de
layout: post
title: Git Rebase Squash-Reihenfolge erklärt
translated: true
type: note
---

Wenn Sie `git rebase -i` (interaktiver Rebase) ausführen, um Commits zusammenzuführen, folgt Git einer sehr spezifischen Reihenfolge und Logik:

---

### 1. Standardreihenfolge

Wenn Sie einen interaktiven Rebase starten (z.B. `git rebase -i HEAD~5`), öffnet Git Ihren Editor mit den **Commits, die von alt nach neu aufgelistet sind** (oben = ältester, unten = neuester).
Die Reihenfolge ist wichtig: Dies ist die Sequenz, die Git versuchen wird, auf die neue Basis anzuwenden.

---

### 2. Pick vs. Squash

* **pick** → behält den Commit unverändert.
* **squash (oder s)** → kombiniert diesen Commit mit dem **vorherigen Commit, der als `pick` markiert ist**.
* **fixup (oder f)** → wie squash, verwirft aber die Commit-Nachricht (behält nur die Nachricht des ersten Commits).

Wenn Sie also schreiben:

```
pick  a1b2c3  Initial feature
squash d4e5f6  Minor fix
squash g7h8i9  Small cleanup
pick  j1k2l3  Another feature
```

Dann wird Git `d4e5f6` und `g7h8i9` in `a1b2c3` zusammenführen und einen einzelnen Commit erzeugen.

---

### 3. Commits neu anordnen

Sie können **Commits direkt im Rebase-Editor neu anordnen**, indem Sie Zeilen nach oben oder unten verschieben.
Zum Beispiel:

```
pick  a1b2c3  Initial feature
pick  j1k2l3  Another feature
squash d4e5f6  Minor fix
squash g7h8i9  Small cleanup
```

Hier wird Git zuerst `a1b2c3` anwenden, dann `j1k2l3`.
Die `squash`-Commits (`d4e5f6` und `g7h8i9`) werden nun in **`j1k2l3`** zusammengeführt, da `squash` immer in den unmittelbar vorhergehenden `pick`-Commit merged.

---

### 4. Nachrichten bearbeiten

Nach dem Zusammenführen hält Git an und ermöglicht Ihnen, die **Commit-Nachricht** für den zusammengeführten Commit zu **bearbeiten**. Sie können:

* Alle Nachrichten beibehalten.
* Sie manuell kombinieren.
* Nur die erste beibehalten.

---

### 5. Häufige Fallstricke

* Wenn Sie `squash` als allerersten Commit setzen (kein `pick` davor), wird Git einen Fehler werfen – es benötigt einen Basis-Commit, in den zusammengeführt werden kann.
* Wenn Commits nach einer Neuanordnung in Konflikt geraten, müssen Sie die Konflikte während des Rebases manuell auflösen.
* Neuanordnung kann die Historie erheblich verändern; tun Sie dies nur auf Branches, die Sie noch nicht gepusht/geteilt haben, es sei denn, Sie sind sicher, dass Sie die Historie umschreiben möchten.

---

✅ Kurz gesagt:

* Commits sind **von alt nach neu** aufgelistet.
* `pick` behält, `squash` merged in den **nächstgelegenen früheren `pick`**.
* Sie können Commits manuell im Editor neu anordnen; `squash` hängt nachfolgende Commits immer an den vorherigen ausgewählten Commit an.

---

Möchten Sie, dass ich dies an einem **Vorher/Nachher-Commit-Historie-Beispiel** veranschauliche (das `git log --oneline` vor und nach dem Zusammenführen zeigt)? Das macht die Reihenfolge normalerweise klarer.