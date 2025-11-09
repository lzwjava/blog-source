---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Übersicht zu GitHub Actions Nutzungsgrenzen
translated: true
type: note
---

### Nutzungslimits von GitHub Actions

GitHub Actions verfügt über gestaffelte Limits basierend auf Ihrem Plan (persönliche Konten oder Organisationen). Dazu gehören kostenlose monatliche Minuten für GitHub-gehostete Runner in privaten Repositorys und Speicher für Artefakte. Öffentliche Repositorys und selbst-gehostete Runner verbrauchen diese Minuten nicht. Die Limits für Minuten werden monatlich zurückgesetzt (der Speicher ist fortlaufend). Überschreitungen werden automatisch abgerechnet, wenn Sie eine gültige Zahlungsmethode hinterlegt haben; andernfalls werden Jobs nach Erreichen des Limits blockiert.

#### Enthaltene Minuten und Speicher nach Plan

| Plan                          | Speicher | Minuten (pro Monat) |
|-------------------------------|----------|---------------------|
| GitHub Free (persönlich/Org)  | 500 MB   | 2,000               |
| GitHub Pro (persönlich)       | 1 GB     | 3,000               |
| GitHub Team (Org)             | 2 GB     | 3,000               |
| GitHub Enterprise Cloud (Org) | 50 GB    | 50,000              |

- **Minuten**: Zählen die gesamte Laufzeit von Jobs auf GitHub-gehosteten Runnern (Teilzeit für fehlgeschlagene Jobs). Multiplikatoren gelten: Linux (1x), Windows (2x), macOS (10x). Jeder mit Schreibzugriff auf ein Repo nutzt das Kontingent des Repo-Besitzers.
- **Speicher**: Basierend auf GB-Stunden der Artefaktspeicherung (z.B. Uploads/Downloads). Logs und Zusammenfassungen zählen nicht.

#### Abrechnung bei Überschreitung
Wenn Sie Kontingente überschreiten:
- **Minuten**: Berechnung pro zusätzlicher Minute (USD-Preise für Standard-Linux-Runner: $0,008/Min; höher für Windows/macOS aufgrund der Multiplikatoren).
- **Speicher**: Berechnung als GB-Monate (Gesamt-GB-Stunden / 744 Stunden pro Monat, aufgerundet).
- Beispiel: Bei einem Team-Plan kosten 5.000 zusätzliche Minuten (3.000 Linux + 2.000 Windows) ~$56.

Ohne eine Zahlungsmethode stoppt die Nutzung beim Erreichen des Kontingents. Der Fehler, den Sie gesehen haben ("recent account payments have failed or your spending limit needs to be increased") bedeutet, dass entweder Zahlungen fehlgeschlagen sind oder Ihr **Spending Limit (Budget)** die Überschreitungen begrenzt.

#### Spending Limits (Budgets)
- Dies sind optionale Schwellenwerte, um die gesamten monatlichen Ausgaben für Actions (und andere abgerechnete Funktionen) zu kontrollieren.
- Wenn sie zu niedrig gesetzt sind, blockieren sie Jobs, bevor die Kontingente erreicht werden.
- **So prüfen/erhöhen Sie**:
  1. Gehen Sie zu GitHub Einstellungen > Abrechnung & Pläne.
  2. Unter "Budgets and alerts" können Sie Ihr Budget für GitHub Actions einsehen oder bearbeiten.
  3. Erhöhen Sie das Limit, fügen Sie eine Zahlungsmethode hinzu oder entfernen Sie das Budget vollständig (unbegrenzte Überschreitungen, aber überwachen Sie dies über Benachrichtigungen).
- Migrierte Konten können automatisch generierte Budgets von alten Limits haben – passen Sie diese an Ihre Nutzung an.

Weitere Details finden Sie im Echtzeit-Nutzungsbericht Ihres Kontos im Abrechnungs-Dashboard.

[Dokumentation zur GitHub Actions Abrechnung](https://docs.github.com/en/billing/managing-billing-for-github-actions/about-billing-for-github-actions)