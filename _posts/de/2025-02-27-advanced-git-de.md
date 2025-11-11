---
audio: false
generated: true
lang: de
layout: post
title: Erweiterte Git-Befehle
translated: true
type: note
---

Git ist wie ein Schweizer Taschenmesser für Entwickler – vielseitig, leistungsstark und gelegentlich verwirrend, wenn man nicht weiß, welches Werkzeug man herausziehen soll. Heute tauchen wir in einige der praktischsten Git-Features und Workflows ein: das gezielte Übernehmen von Änderungen (Cherry-Picking), das Mergen mit Stil, das Rebasing für eine sauberere History, das Löschen dieser lästigen großen Dateien, die man versehentlich committed hat, und das Rückgängigmachen eines Commits, wenn man merkt, dass man sich verlaufen hat. Fassen wir es zusammen.

#### Cherry-Picking: Nur das nehmen, was man braucht
Stellen Sie sich vor, Sie haben einen Feature-Branch mit einem Dutzend Commits, aber da ist ein glänzender Commit dabei, den Sie herausziehen und auf Ihren Main-Branch anwenden möchten – ohne den Rest mitzunehmen. Hier kommt `git cherry-pick` ins Spiel.

Es ist ganz einfach: Finden Sie den Commit-Hash (Sie können ihn aus `git log` holen), wechseln Sie zu dem Branch, auf dem Sie ihn haben wollen, und führen Sie aus:
```
git cherry-pick <Commit-Hash>
```
Schwupps, dieser Commit ist jetzt Teil Ihres aktuellen Branches. Wenn es einen Konflikt gibt, hält Git an und lässt Sie ihn lösen, genau wie bei einem Merge. Wenn Sie zufrieden sind, committen Sie die Änderungen, und Sie sind fertig.

Ich benutze dies ständig, wenn sich eine Bugfix in einen unordentlichen Feature-Branch geschlichen hat und ich sie so schnell wie möglich auf `main` brauche. Seien Sie nur vorsichtig – Cherry-Picking dupliziert den Commit, also erhält er einen neuen Hash. Erwarten Sie nicht, dass er sich gut verhält, wenn Sie den ursprünglichen Branch später ohne eine gewisse Bereinigung mergen.

#### Merge-Optionen: Mehr als nur "Merge"
Mergen ist Git's täglich Brot, aber wussten Sie, dass es verschiedene Varianten gibt? Das Standard-`git merge` macht, wenn möglich, einen "Fast-Forward" (die History wird begradigt) oder erstellt einen Merge-Commit, wenn die Branches auseinandergegangen sind. Aber Sie haben Optionen:

- **`--no-ff` (No Fast-Forward)**: Erzwingt einen Merge-Commit, selbst wenn ein Fast-Forward möglich wäre. Ich liebe dies, um einen klaren Nachweis darüber zu haben, wann ein Feature-Branch in `main` eingeflossen ist. Führen Sie es so aus:
  ```
  git merge --no-ff feature-branch
  ```
- **`--squash`**: Holt alle Änderungen aus dem Branch in einen einzigen Commit in Ihrem aktuellen Branch. Kein Merge-Commit, nur ein einziges, ordentliches Paket. Perfekt, um einen unordentlichen Branch in etwas Präsentables zu verwandeln:
  ```
  git merge --squash feature-branch
  ```
  Danach müssen Sie manuell committen, um den Deal zu besiegeln.

Jede Option hat ihren Platz. Ich neige zu `--no-ff` für langlebige Branches und zu `--squash`, wenn ich einen Branch voller "WIP"-Commits habe, die ich lieber vergessen würde.

#### Rebasing: Geschichte umschreiben wie ein Profi
Wenn Merges Ihnen zu unübersichtlich erscheinen, könnte `git rebase` Ihr Ding sein. Es nimmt Ihre Commits und spielt sie auf einem anderen Branch neu ab, was Ihnen eine lineare History gibt, die aussieht, als hätten Sie von Anfang an alles perfekt geplant.

Wechseln Sie zu Ihrem Feature-Branch und führen Sie aus:
```
git rebase main
```
Git wird Ihre Commits anheben, den Branch an `main` anpassen und Ihre Änderungen wieder oben draufsetzen. Wenn Konflikte auftauchen, lösen Sie sie, dann `git rebase --continue`, bis es fertig ist.

Der Vorteil? Eine makellose Timeline. Der Nachteil? Wenn Sie diesen Branch bereits gepusht haben und andere daran arbeiten, schreibt das Rebasing die History um – was verärgerte E-Mails von Teammitgliedern zur Folge haben kann. Ich bleibe beim Rebasing für lokale Branches oder Solo-Projekte. Für gemeinsame Projekte ist Mergen sicherer.

#### Große Dateien aus der History löschen: Hoppla, diese 2GB-Video
Das ist uns allen schon passiert: Man committed versehentlich eine riesige Datei, pusht sie, und jetzt ist das Repo aufgebläht. Git vergisst nicht leicht, aber Sie können diese Datei mit etwas Aufwand aus der History schrubben.

Das bevorzugte Werkzeug hier ist `git filter-branch` oder das neuere `git filter-repo` (ich empfehle Letzteres – es ist schneller und weniger fehleranfällig). Sagen wir, Sie haben `bigfile.zip` committed und müssen sie loswerden:
1. Installieren Sie `git-filter-repo` (sehen Sie in der Dokumentation für die Einrichtung nach).
2. Führen Sie aus:
   ```
   git filter-repo --path bigfile.zip --invert-paths
   ```
   Dies entfernt `bigfile.zip` aus jedem Commit in der History.
3. Pushen Sie die umgeschriebene History mit Force:
   ```
   git push --force
   ```

Achtung: Dies schreibt die History um, also koordinieren Sie sich mit Ihrem Team. Und wenn es sich in einem Pull Request irgendwo befindet, müssen Sie möglicherweise auch Refs bereinigen. Sobald es weg ist, schrumpft Ihr Repo nach einer Garbage Collection (`git gc`).

#### Uncommitting: Die Uhr zurückdrehen
Einen Commit gemacht und ihn sofort bereut? Git hat Sie im Blick. Es gibt einige Möglichkeiten, ihn rückgängig zu machen, je nachdem, wie weit Sie gegangen sind:

- **Wenn Sie noch nicht gepusht haben**: Verwenden Sie `git reset`. Um den letzten Commit rückgängig zu machen, aber die Änderungen in Ihrem Arbeitsverzeichnis zu behalten:
  ```
  git reset HEAD^ --soft
  ```
  Möchten Sie die Änderungen komplett verwerfen?
  ```
  git reset HEAD^ --hard
  ```
- **Wenn Sie bereits gepusht haben**: Müssen Sie die History umschreiben. Setzen Sie lokal mit `git reset HEAD^` zurück und pushen Sie dann mit Force:
  ```
  git push --force
  ```
  Auch hier gilt: Dies bringt die gemeinsame History durcheinander, also gehen Sie vorsichtig vor.

Ich habe mich mit `git reset --soft` öfter gerettet, als ich zählen kann – perfekt, wenn ich zu früh committe und noch etwas anpassen muss.

#### Zusammenfassung

Git's Flexibilität ist es, was es so mächtig macht, aber es ist leicht, sich zu verstricken, wenn man seine Optionen nicht kennt. Verwenden Sie Cherry-Pick für chirurgische Präzision, passen Sie Merges an Ihren Workflow an, rebasen Sie für eine polierte History, und geraten Sie nicht in Panik, wenn Sie einen Fehler löschen müssen – sei es eine riesige Datei oder ein übereilter Commit. Üben Sie diese Befehle in einem Test-Repo, wenn Sie nervös sind, und bald werden sie Ihnen in Fleisch und Blut übergehen.

Was ist Ihr liebster Git-Trick? Lassen Sie es mich wissen – ich bin immer offen, etwas Neues zu lernen!