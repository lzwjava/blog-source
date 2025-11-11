---
audio: false
generated: true
lang: de
layout: post
title: Werkzeuge zur Git-Branch-Visualisierung
translated: true
type: note
---

Um mehrere Branches in einem Git-Repository unter Windows zu visualisieren, können Sie TortoiseGit oder andere Tools verwenden, um einen Graphen ausgewählter Branches anzuzeigen. Der Revisionsgraph von TortoiseGit ist leistungsstark, kann jedoch überwältigend sein, wenn alle Branches angezeigt werden. Nachfolgend finden Sie Schritte, um einen Graphen mehrerer spezifischer Branches mit TortoiseGit anzuzeigen, sowie alternative Tools für mehr Flexibilität.

### Verwendung von TortoiseGit zum Anzeigen mehrerer Branches
Der Revisionsgraph von TortoiseGit kann mehrere Branches anzeigen, erlaubt jedoch nicht die direkte Auswahl spezifischer Branches in der Oberfläche. Sie können die Ansicht jedoch filtern, um sich auf relevante Branches zu konzentrieren.

1. **Revisionsgraph öffnen**:
   - Navigieren Sie in Windows Explorer zu Ihrem Repository-Ordner.
   - Klicken Sie mit der rechten Maustaste auf den Ordner und wählen Sie **TortoiseGit** > **Revisionsgraph**.
   - Standardmäßig wird ein Graph aller Referenzen (Branches, Tags etc.) angezeigt, was bei vielen Branches unübersichtlich sein kann.[](https://tortoisegit.org/docs/tortoisegit/tgit-dug-revgraph.html)

2. **Spezifische Branches filtern**:
   - Verwenden Sie im Fenster "Revisionsgraph" die **Filteroptionen**, um Unübersichtlichkeit zu reduzieren:
     - Gehen Sie zum Menü **Ansicht** und wählen Sie **Branchings und Mergings anzeigen**, um Branch-Beziehungen hervorzuheben.[](https://stackoverflow.com/questions/67642974/tortoisegit-log-can-i-view-only-branch-and-merge-commits)
     - Um sich auf spezifische Branches zu konzentrieren, klicken Sie mit der rechten Maustaste auf einen Commit und wählen **Log anzeigen**, um den Log-Dialog zu öffnen. Dort können Sie **Ansicht > Labels > Lokale Branches** oder **Remote-Branches** umschalten, um nur relevante Referenzen anzuzeigen.[](https://tortoisegit.org/docs/tortoisegit/tgit-dug-showlog.html)
   - Alternativ können Sie die Option **Walk Behavior > Komprimierter Graph** im Log-Dialog verwenden, um den Graphen zu vereinfachen und nur Merge-Punkte und Commits mit Referenzen (wie Branch-Spitzen) anzuzeigen.[](https://tortoisegit.org/docs/tortoisegit/tgit-dug-showlog.html)[](https://stackoverflow.com/questions/67642974/tortoisegit-log-can-i-view-only-branch-and-merge-commits)

3. **Im Graphen navigieren**:
   - Verwenden Sie das **Übersichtsfenster**, um in großen Graphen zu navigieren, indem Sie den markierten Bereich ziehen.[](https://tortoisegit.org/docs/tortoisegit/tgit-dug-revgraph.html)
   - Fahren Sie mit der Maus über einen Revisionsknoten, um Details wie Datum, Autor und Kommentare zu sehen.[](https://tortoisegit.org/docs/tortoisegit/tgit-dug-revgraph.html)
   - Klicken Sie bei gedrückter Strg-Taste auf zwei Revisionen, um sie über das Kontextmenü zu vergleichen (z.B. **Revisionen vergleichen**).[](https://tortoisegit.org/docs/tortoisegit/tgit-dug-revgraph.html)

4. **Einschränkungen**:
   - Der Revisionsgraph von TortoiseGit zeigt alle Branches an, sofern nicht gefiltert, und es gibt keine direkte Option, im Graph nur spezifische Branches auszuwählen.[](https://stackoverflow.com/questions/60244772/how-to-interpret-tortoise-git-revision-graph)
   - Für eine übersichtlichere Ansicht sollten Sie die unten aufgeführten alternativen Tools in Betracht ziehen.

### Alternative Tools zum Anzeigen mehrerer Branches
Wenn die Oberfläche von TortoiseGit für die Auswahl spezifischer Branches zu eingeschränkt ist, probieren Sie diese Tools aus, die mehr Kontrolle über die Branch-Visualisierung bieten:

#### 1. **Visual Studio Code mit Git Graph Extension**
   - **Installation**: Laden Sie Visual Studio Code herunter und installieren Sie die **Git Graph**-Erweiterung.[](https://x.com/midudev/status/1797990974917927150)
   - **Verwendung**:
     - Öffnen Sie Ihr Repository in VS Code.
     - Greifen Sie auf die Git Graph-Ansicht über die Quellcodeverwaltungs-Seitenleiste oder die Befehlspalette zu (`Strg+Umschalt+P`, "Git Graph" eingeben).
     - Wählen Sie spezifische Branches aus, die im Graphen angezeigt werden sollen, indem Sie auf die Branchnamen in der Oberfläche klicken.
     - Der Graph zeigt Commits, Branches und Merges mit farbcodierten Linien für bessere Übersichtlichkeit.[](https://ardalis.com/git-graph-visualizes-branches-in-vs-code-for-free/)
   - **Vorteile**: Leichtgewicht, kostenlos und erlaubt interaktive Auswahl mehrerer Branches. Unterstützt das Vergleichen von Commits und grundlegende Git-Operationen.[](https://ardalis.com/git-graph-visualizes-branches-in-vs-code-for-free/)

#### 2. **SourceTree**
   - **Installation**: Laden Sie SourceTree (kostenlos) für Windows herunter.[](https://stackoverflow.com/questions/12324050/how-can-i-visualize-github-branch-history-on-windows)[](https://stackoverflow.com/questions/12912985/git-visual-diff-between-branches)
   - **Verwendung**:
     - Öffnen Sie Ihr Repository in SourceTree.
     - Die **History**-Ansicht zeigt eine grafische Darstellung der Branches und Commits.
     - Verwenden Sie die Branch-Liste auf der linken Seite, um die Sichtbarkeit spezifischer Branches umzuschalten und sich nur auf die gewünschten zu konzentrieren.
     - Klicken Sie mit der rechten Maustaste auf Branches oder Commits für Aktionen wie Mergen oder Vergleichen.[](https://www.geeksforgeeks.org/how-to-visualizing-branch-topology-in-git/)
   - **Vorteile**: Klare Branch-Visualisierung mit konsistenter Farbgebung und interaktiven Funktionen wie Drag-and-Drop-Merging.[](https://superuser.com/questions/699094/how-can-i-visualize-git-flow-branches)[](https://www.geeksforgeeks.org/how-to-visualizing-branch-topology-in-git/)

#### 3. **GitKraken**
   - **Installation**: Laden Sie GitKraken herunter (kostenlos für Open-Source-Projekte, kostenpflichtig für private Repos).[](https://www.geeksforgeeks.org/how-to-visualizing-branch-topology-in-git/)[](https://stackoverflow.com/questions/1838873/visualizing-branch-topology-in-git)
   - **Verwendung**:
     - Öffnen Sie Ihr Repository in GitKraken.
     - Der zentrale Graph zeigt alle Branches an, mit Optionen zum Ausblenden/Anzeigen spezifischer Branches über die Branch-Liste.
     - Klicken Sie auf Branch-Labels, um sich auf spezifische Branches zu konzentrieren, oder verwenden Sie die Suche, um Commits zu filtern.[](https://www.geeksforgeeks.org/how-to-visualizing-branch-topology-in-git/)
   - **Vorteile**: Intuitiv und visuell ansprechend, mit konsistenter Branch-Farbgebung und erweiterten Funktionen wie Conflict Resolution.[](https://superuser.com/questions/699094/how-can-i-visualize-git-flow-branches)[](https://www.geeksforgeeks.org/how-to-visualizing-branch-topology-in-git/)

#### 4. **Command Line mit `git log`**
   - Wenn Sie eine terminalbasierte Lösung bevorzugen, verwenden Sie die eingebaute Graph-Ansicht von Git:
     ```bash
     git log --graph --oneline --decorate --branches=<branch1> --branches=<branch2>
     ```
     Ersetzen Sie `<branch1>` und `<branch2>` durch die Namen der Branches, die Sie visualisieren möchten (z.B. `feature1`, `feature2`). Verwenden Sie `--branches=*` für alle Branches oder geben Sie mehrere Branches explizit an.[](https://how-to.dev/how-to-display-git-branches-as-a-tree-in-cli)
   - **Alias für Bequemlichkeit**:
     Erstellen Sie einen Git-Alias für einfacheren Zugriff:
     ```bash
     git config --global alias.tree "log --graph --oneline --decorate --branches="
     ```
     Führen Sie dann `git tree feature1 feature2` aus, um einen Graphen nur dieser Branches zu sehen.[](https://how-to.dev/how-to-display-git-branches-as-a-tree-in-cli)
   - **Vorteile**: Keine zusätzliche Software erforderlich, und Sie können exakte Branches angeben. Die Ausgabe ist textbasiert, aber für kleine Repositories übersichtlich.[](https://x.com/GWierzowiecki/status/1927657575048179899)

### Empfehlungen
- **Für Einfachheit und Integration**: Verwenden Sie **VS Code mit Git Graph** für eine leichtgewichtige, kostenlose Lösung, die Ihnen erlaubt, spezifische Branches auszuwählen.[](https://x.com/midudev/status/1797990974917927150)
- **Für erweiterte Visualisierung**: Verwenden Sie **GitKraken** oder **SourceTree** für eine hochwertigere GUI mit interaktiver Branch-Auswahl und konsistenter Farbgebung.[](https://www.geeksforgeeks.org/how-to-visualizing-branch-topology-in-git/)
- **Für TortoiseGit-Benutzer**: Bleiben Sie beim Revisionsgraph und verwenden Sie Filter wie **Komprimierter Graph** oder **Branchings und Mergings anzeigen**, um sich auf wichtige Branches zu konzentrieren, seien Sie sich jedoch der Einschränkungen bei der Auswahl spezifischer Branches bewusst.[](https://stackoverflow.com/questions/67642974/tortoisegit-log-can-i-view-only-branch-and-merge-commits)
- **Für Terminal-Benutzer**: Verwenden Sie den `git log`-Befehl mit spezifischen Branch-Filtern für schnelle, präzise Visualisierung ohne zusätzliche Tools.[](https://how-to.dev/how-to-display-git-branches-as-a-tree-in-cli)

Wenn Sie eine große Anzahl von Branches haben, sind GitKraken oder SourceTree wahrscheinlich die besten Optionen, um selektiv nur die Branches zu visualisieren, die Sie benötigen, da sie intuitives Umschalten der Branches bieten. Lassen Sie mich wissen, wenn Sie Hilfe bei der Einrichtung eines dieser Tools oder weitere Erklärungen benötigen!