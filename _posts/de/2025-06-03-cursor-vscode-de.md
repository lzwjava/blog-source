---
audio: false
generated: true
lang: de
layout: post
title: Cursor und VS Code
translated: true
type: note
---

Ja, es ist legal für Cursor, Visual Studio Code (VS Code) zu forken und ein Geschäft darum aufzubauen, vorausgesetzt, sie halten sich an die Bedingungen der MIT-Lizenz, unter der der Quellcode von VS Code veröffentlicht wird. Die MIT-Lizenz ist sehr erlaubnisfreundlich und erlaubt jedem, die Software zu verwenden, zu kopieren, zu modifizieren, zu mergen, zu veröffentlichen, zu verteilen, zu sub-lizenzieren und Kopien der Software zu verkaufen, solange der ursprüngliche Copyright-Hinweis und der Erlaubnishinweis in allen Kopien oder wesentlichen Teilen der Software enthalten sind.

Hier sind die wichtigsten Punkte bezüglich der Legalität von Cursors Fork:

1.  **Einhaltung der MIT-Lizenz**: Der Quellcode von VS Code, verfügbar im `vscode` GitHub-Repository, ist unter der MIT-Lizenz lizenziert. Dies erlaubt es Cursor, das Codebase zu forken, es zu modifizieren und für kommerzielle Zwecke zu nutzen, einschließlich der Erstellung eines Closed-Source-Produkts, solange sie die ursprüngliche MIT-Lizenz und den Copyright-Hinweis in ihrer Distribution beifügen. Die MIT-Lizenz verlangt nicht, dass das geforkte Projekt Open-Source bleibt, daher kann Cursor sein Produkt legal proprietär machen.

2.  **Visual Studio Code vs. Code-OSS**: Es gibt einen Unterschied zwischen dem Open-Source-`vscode`-Repository (oft als Code-OSS bezeichnet) und dem Microsoft-gebrandeten Visual Studio Code-Produkt. Das Microsoft-gebrandete VS Code beinhaltet proprietäre Ergänzungen (z.B. Telemetrie, Marketplace-Integration) und wird unter einer anderen Lizenz vertrieben. Das Forken des Open-Source-`vscode`-Repositorys, das unter der MIT-Lizenz steht, ist jedoch ausdrücklich erlaubt und wurde von Cursor und ähnlichen Projekten wie Windsurf durchgeführt. Sie können ihre eigenen Anpassungen darauf aufbauen.

3.  **Einschränkungen beim Visual Studio Marketplace**: Eine bedeutende Einschränkung für Forks wie Cursor ist, dass sie aufgrund der Nutzungsbedingungen von Microsoft nicht auf den offiziellen Visual Studio Marketplace zugreifen können. Das bedeutet, Cursor kann nicht das gleiche Ökosystem an Erweiterungen wie VS Code anbieten, es sei denn, sie richten ein alternatives Erweiterungs-Registry ein (z.B. OpenVSX) oder entwickeln ihr eigenes. Zusätzlich sind einige proprietäre Erweiterungen, wie GitHub Copilot oder Microsofts C/C++-Erweiterungen, auf die offiziellen VS Code-Builds von Microsoft beschränkt, was die Funktionalität von Forks einschränken kann.

4.  **Ethische und Community-Bedenken**: Während das Forken unter der MIT-Lizenz legal ist, haben einige ethische Bedenken geäußert, dass Unternehmen wie Cursor ein Open-Source-Projekt nehmen, Funktionen hinzufügen und es als proprietäres Produkt verkaufen, ohne zur ursprünglichen VS Code-Community zurückzutragen. Dies ist jedoch eine moralische Debatte, keine rechtliche, und die MIT-Lizenz erlaubt eine solche Nutzung ausdrücklich.

5.  **Microsofts Reaktion**: Microsoft hat Schritte unternommen, um sein Ökosystem zu schützen, wie die Einschränkung des Marketplace-Zugriffs und proprietärer Erweiterungen für Forks, wie man beispielsweise bei der Entfernung der C/C++-Erweiterungsunterstützung für nicht-offizielle Builds gesehen hat. Diese Einschränkungen betreffen jedoch nicht die Legalität des Forkens des `vscode`-Repositorys selbst, solange der Fork die MIT-Lizenz einhält.

Zusammenfassend ist Cursors Fork von VS Code unter der MIT-Lizenz legal, da sie frei sind, das Codebase zu modifizieren und zu kommerzialisieren, vorausgesetzt, sie fügen die erforderlichen Copyright- und Lizenzhinweise bei. Die Hauptherausforderungen, denen sie gegenüberstehen, sind praktischer Natur – wie der mangelnde Zugang zum VS Code Marketplace und zu bestimmten proprietären Erweiterungen – und keine rechtlichen Hindernisse. Wenn Sie Bedenken bezüglich spezifischer Aspekte von Cursors Implementierung oder Compliance haben, ist die Konsultation eines Rechtsanwalts für Ihren Rechtsraum ratsam, da ich kein Anwalt bin.