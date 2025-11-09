---
audio: false
date: 2025-09-09
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: Verhindern von Repository-Forks auf GitHub
translated: true
type: note
---

Auf GitHub **können Sie nicht verhindern, dass Personen ein öffentliches Repository forken**. Forking ist eine Kernfunktion von GitHub für offene Zusammenarbeit. Wenn Ihr Repository öffentlich ist, kann jeder einen Fork erstellen.

Hier sind Ihre Optionen, abhängig von Ihrem Ziel:

### 1. Wenn Sie das Forken komplett verhindern möchten

* Der einzige Weg ist, Ihr Repository **privat** zu stellen.
* Private Repositories können nicht auf externe Accounts geforkt werden.
* Innerhalb einer Organisation können Admins kontrollieren, ob private Repositories auf andere Mitglieder forkbar sind.

### 2. Wenn Sie die Sichtbarkeit reduzieren, aber öffentlich bleiben möchten

* Sie können **Lizenzbeschränkungen hinzufügen**: Fügen Sie eine Lizenz hinzu, die keine Weiterverbreitung erlaubt (z.B. "Alle Rechte vorbehalten"). Dies wird Forking technisch nicht stoppen, bietet Ihnen aber rechtlichen Schutz.
* Sie können **GitHub Pages und andere Sichtbarkeitsfunktionen deaktivieren**, um die Sichtbarkeit zu reduzieren.

### 3. Wenn Ihr Repository bereits geforkt wurde

* Sie können den Fork eines anderen Benutzers nicht "entfernen".
* Sie können nur den Besitzer des Forks bitten, ihn zu löschen, oder eine **DMCA-Takedown-Anfrage** bei GitHub stellen, wenn dieser Ihre Lizenz oder Rechte verletzt.

---

👉 Kurz gesagt:

* Öffentliches Repository → kann immer geforkt werden.
* Privates Repository → Fork-Schutz, es sei denn, es wird innerhalb Ihrer Organisation explizit erlaubt.

Möchten Sie, dass ich Ihnen erkläre, **wie Sie ein Repository auf privat stellen und internes Forken deaktivieren**?