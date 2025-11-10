---
audio: false
generated: true
image: false
lang: de
layout: post
title: Modellbeziehungen, nicht Daten
translated: true
type: note
---

Du hast absolut recht – „one-to-one, one-to-many, many-to-many“ sind überall: Familien, Teams, Zahlungen; Kurse, Repos, Pull-Requests. Hier ist ein kompaktes Playbook, um **Beziehungen zu klären**, damit Designs einfach bleiben und der Nutzung entsprechen.

# Ein praktisches Modellierungs-Playbook

## 1) Beginne beim Verhalten, nicht bei den Daten

* Notiere die **5 wichtigsten Benutzeraufgaben** („Bestellung aufgeben“, „Kosten genehmigen“, „Reviewer zuweisen“).
* Liste unter jeder Aufgabe **Nomen** (Entitäten) und **Verben** (Beziehungen/Aktionen) auf.
* Behalte nur Beziehungen, die **Ergebnisse in diesen Aufgaben verändern**; alles andere ist Metadaten.

## 2) Entscheide zuerst über Besitz und Grenzen

* Frage: *Wer kontrolliert den Lebenszyklus von wem?*
  * Wenn A ohne B nicht existieren kann → A ist **Teil von** B (Komposition).
  * Wenn A und B unabhängig voneinander existieren → **Referenz**-Beziehung.
* Verwende **Bounded Contexts**: Derselbe „Kunde“ kann im Bereich Abrechnung vs. Marketing unterschiedlich sein. Erzwinge kein einziges Riesen-Modell.

## 3) Wähle die **einfachste Kardinalität**, die funktioniert

* Bevorzuge **1→1** nur, wenn zwei Datensätze operativ untrennbar sind, aber unterschiedliche Sicherheit oder Volatilität benötigen (z.B. User ↔ Credentials).
* Bevorzuge **1→N**, wenn es eine klare Besitzverhältnis gibt und häufiger Zugriff von Eltern-→Kind-Elementen erfolgt (Order → LineItems).
* Verwende **M↔N** nur, wenn beide Seiten gleichberechtigt sind und die Verknüpfung ein eigenes Geschäftskonzept darstellt (Student ↔ Course über „Enrollment“, das Note, Status, Daten hat).

## 4) Mache Beziehungen mit Invarianten explizit

Schreibe für jede Beziehung Invarianten in Klartext:

* **Kardinalität**: „Ein Benutzer hat höchstens eine primäre E-Mail.“
* **Optionalität**: „Eine Rechnung muss ≥1 Position haben.“
* **Zeitlichkeit**: „Die Mitgliedschaft ist gültig im Zeitraum [Start, Ende).“
* **Eindeutigkeit**: „Ein Produktcode ist eindeutig pro Mandant.“
  Diese lassen sich direkt in Constraints, Indizes und Checks umwandeln.

## 5) Modellierungsmuster nach Kardinalität (ohne Tabellen 😉)

### One-to-one

* Verwende sie, um volatile/sichere Felder aufzuteilen oder wenn eine Entität modular wächst.
* Erzwinge sie mit einem Unique Key auf dem Fremdschlüssel.
* Erwäge **Embedding** (Dokumente), wenn die Daten immer zusammen gelesen werden.

### One-to-many

* Wenn Kinder nie den Eltern-Element wechseln → behalte **Eltern-Schlüssel** beim Kind; cascade deletes als Richtlinie.
* Wenn Neuzuordnung vorkommt → erlaube nullable FK + Geschäftsregel für Übergänge.
* Wenn Lesezugriffe elternzentriert sind → denormalisiere Zusammenfassungsfelder beim Eltern-Element (Anzahlen, last_updated).

### Many-to-many

* Befördere die Verknüpfung zu einer **First-Class-Entity** (Enrollment, Membership, Assignment).
* Platziere die **Geschäftsdaten** in der Verknüpfung (Rolle, Priorität, Gewichtung, Zeitstempel).
* Wenn die Verknüpfung keine Attribute hat und sehr groß ist, wähle Speicher & Indizes für die Abfragen der schwereren Seite.

## 6) Wähle den Speicher nach Zugriffsmustern

* **Relational**: Stärkste Integrität, komplexe Joins, Reporting.
* **Dokument**: Aggregate-first, leselastige, elternzentrierte Abläufe, lokalisierte Updates.
* **Graph**: Pfadabfragen, Empfehlungen, Berechtigungsvererbung, Traversierung mit variabler Tiefe.
  Wähle einen **pro Bounded Context**; synchronisiere über Events, nicht über gemeinsame Tabellen.

## 7) API-Oberfläche spiegelt Beziehungen – intentional

* **Aggregate** werden primäre API-Ressourcen.
* **Kind-Sammlungen** als verschachtelte Routen (z.B. `/orders/{id}/items`).
* **Verknüpfungsentitäten** erhalten ihre eigene Ressource, wenn sie wichtig sind (`/enrollments`).
* Für Client-Flexibilität, biete **GraphQL** nur an, wenn die Domäne graphenähnlich ist oder Clients stark variieren; ansonsten halte REST einfach.

## 8) Halte es entwickelbar (temporal + soft change)

* Verfolge **Valid-Time** bei wichtigen Verknüpfungen (`valid_from`, `valid_to`), nicht nur `updated_at`.
* Bevorzuge **Soft Deletes** bei Beziehungszeilen, um den Verlauf rekonstruieren zu können.
* Verwende **Surrogate-IDs** für alle Entitäten und Verknüpfungszeilen; baue niemals Bedeutung in IDs ein.

## 9 Vereinfache aggressiv

* Führe Entitäten zusammen, wenn Benutzer den Unterschied nie wahrnehmen.
* Kollabiere 1→1-Aufteilungen, wenn Sicherheits-/Leistungsgründe entfallen.
* Ersetze weitläufige M↔N-Netze durch eine **Hierarchie**, wenn Geschäftsregeln tatsächlich baumförmig sind.
* Führe **Rollen** ein, anstatt mehrere Verknüpfungstypen zu haben (z.B. eine Membership mit role=owner/viewer anstatt separate Links).

## 10) Reverse-Research (reverse-engineer) eines bestehenden Wirrwarrs

* Mappe **tatsächliche Abfragen** (Slow Logs, Dashboards). Behalte nur Beziehungen, die von ≥1 kritischer Abfrage genutzt werden.
* Zeichne **Context Maps**: Welches Team/System besitzt welche Entitäten und wer konsumiert welche Events.
* Identifiziere **Hot Joins** → denormalisiere sie, cache sie oder wandle sie in Aggregate um.
* Erhebe häufige M↔N-Links zu **First-Class-Concepts** mit klaren Invarianten.
* Füge **Contracts** hinzu: Constraints, Tests und Linter für Schema & API, um Drift zu verhindern.

# Häufige Fallstricke, die du vermeiden solltest

* M↔N als „nur eine Join-Tabelle“ zu behandeln, wenn es eigentlich das geschäftliche Herzstück ist (z.B. Berechtigungen, Zuteilungen).
* Über-Normalisierung von Lese-Pfaden, die niedrige Latenz benötigen; behebe dies mit **Read Models** (CQRS) oder materialisierten Sichten.
* Unter-Spezifizierung der Optionalität – `NULL` explodiert die Komplexität. Bevorzuge explizite „Unknown/NotApplicable“-Zustände, wenn sinnvoll.
* **Multi-Tenancy** ignorieren: Scope Eindeutigkeit und Abfragen frühzeitig pro Mandant.
* **Richtung** vergessen: „folgt“ vs. „befreundet“ ist nicht dasselbe.

# Eine leichtgewichtige Checkliste, die du wiederverwenden kannst

* Was sind die wichtigsten Aufgaben und ihre Erfolgsmetriken?
* Was sind die Aggregate (Ownership/Lebenszyklus)?
* Was sind die Invarianten (Kardinalität, Optionalität, Zeitlichkeit, Eindeutigkeit)?
* Welche Beziehungen tragen Geschäftsattribute (befördere sie zu Entitäten)?
* Welche Zugriffsmuster dominieren (wähle entsprechend Speicher/Indizes)?
* Welche Vereinfachungen sind heute sicher (Zusammenführen/Aufteilen/Denormalisieren)?
* Welche Contracts erzwingen dies (Constraints, API-Tests, Event-Schemas)?

Wenn du möchtest, gib mir einen kleinen Ausschnitt deiner Domäne (drei Entitäten + die Hauptbenutzeraufgabe), und ich skizziere die Beziehungen, Invarianten und eine Speicher-/API-Form, die du direkt implementieren kannst.