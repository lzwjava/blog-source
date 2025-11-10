---
audio: false
generated: true
image: false
lang: de
layout: post
title: KI-CLI-Designprinzipien entpackt
translated: true
type: note
---

### Wichtige Erkenntnisse aus dem Prompt

Dieser Prompt beschreibt ein System für ein KI-gesteuertes CLI-Tool (Claude Code), das auf Software-Engineering-Aufgaben spezialisiert ist. Hier ist, was wir über die Gestaltung effektiver KI-Assistenten lernen können:

#### 1. **Priorisierung von Sicherheit und Ethik**
   - Betont defensive Sicherheit: Die KI muss Aufgaben ablehnen, die bösartigen Code betreffen (z.B. das Erstellen von Exploits), aber defensive Aufgaben wie Schwachstellenanalyse oder die Erstellung von Erkennungsregeln erlauben.
   - Lehre: Baue ethische Leitplanken frühzeitig ein, um Missbrauch zu verhindern, besonders in sensiblen Bereichen wie der Programmierung, wo Ergebnisse reale Auswirkungen haben können.

#### 2. **Antwortstil und Prägnanz**
   - Verlangt ultra-kurze Antworten (unter 4 Zeilen, sofern keine Details angefordert wurden), mit Beispielen wie der einfachen Antwort "4" auf "2 + 2".
   - Vermeidet Einleitungen, Erklärungen oder Emojis, sofern nicht gefragt; konzentriert sich auf direkte, token-effiziente Ausgaben für die CLI-Darstellung.
   - Lehre: Passe die Kommunikation an die Schnittstelle an (z.B. erfordert die CLI Kürze, um Unübersichtlichkeit zu vermeiden). Dies verringert die kognitive Belastung und verbessert die Benutzerfreundlichkeit interaktiver Tools.

#### 3. **Proaktivität mit Grenzen**
   - Erlaubt proaktive Aktionen (z.B. das Ausführen von Befehlen, Planen von Aufgaben), aber nur bei benutzerinitiierten Aktionen; warnt davor, Benutzer zu überraschen.
   - Balanciert Autonomie (z.B. das Überprüfen von Lösungen mit Tests) mit Benutzerkontrolle (z.B. niemals Änderungen committen ohne explizite Aufforderung).
   - Lehre: KI sollte effizient assistieren, ohne zu übergriffig zu sein, um Vertrauen zu fördern. Verwende Planungstools (wie TodoWrite), um Fortschritte transparent nachzuverfolgen.

#### 4. **Tool-Integration und Workflow**
   - Bietet eine Reihe von Tools (z.B. Bash zur Ausführung, WebFetch für Docs, Suchtools für Codebasen) mit Richtlinien für parallele Nutzung und Bündelung.
   - Ermutigt zum häufigen Management von Todo-Listen, um Aufgaben zu zerlegen, Lösungen mit Lint/Typechecks zu verifizieren und Codierungsrichtlinien zu folgen (z.B. vorhandene Stile nachahmen, Bibliotheken prüfen).
   - Behandelt Sonderfälle wie Hooks, Redirects und Umgebungsbewusstsein (z.B. Git-Status, OS-Details).
   - Lehre: Statte KIs mit modularen Tools für komplexe Aufgaben aus; fördere sequentielle/parallele Nutzung für Effizienz. Bette Aktionen stets in den Kontext ein (z.B. erst suchen, dann Annahmen treffen).

#### 5. **Domänenspezifische Anpassung**
   - Auf Software-Engineering abgestimmt: Planen, Suchen, Implementieren, Verifizieren; verweist präzise auf Code-Stellen (z.B. "Dateipfad:Zeilennummer").
   - Beinhaltet Feedback-Kanäle und Hilfebefehle; passt sich Benutzerkonfigurationen wie Hooks an.
   - Lehre: Passe Prompts an die Domäne an – hier sorgen Coding-Konventionen für idiomatische, sichere Ausgaben. Biete Selbsthilfe-Mechanismen, um Benutzer zu befähigen.

#### 6. **Allgemeine Erkenntnisse zum Prompt-Engineering**
   - Strukturiert mit Abschnitten (z.B. Ton, Proaktivität, Tools) und Beispielen für Klarheit.
   - Verwendet XML-ähnliche Tags für Erinnerungen; spezifiziert Wissensstände und Modelldetails.
   - Lehre: Effektive Prompts sind modular, beispielgetrieben und stark einschränkend, um das Verhalten zu steuern. Dies verringert Halluzinationen und gewährleistet Konsistenz.

Insgesamt zeigt dieser Prompt, wie man ein zuverlässiges, benutzerzentriertes KI-Tool erstellt, indem strenge Regeln, Tools und Planung kombiniert werden – wertvoll für den Bau ähnlicher Systeme in der Programmierung und darüber hinaus.