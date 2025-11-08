---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: PromQL-Abfragesprache Leitfaden
translated: true
type: note
---

PromQL (Prometheus Query Language) ist eine funktionale Abfragesprache, die zur Echtzeitauswahl und Aggregation von Zeitreihendaten aus Prometheus verwendet wird. Sie unterstützt Instant-Abfragen (ausgewertet zu einem einzelnen Zeitpunkt) und Range-Abfragen (ausgewertet in mehreren Schritten über einen Zeitbereich). PromQL-Ausdrücke können einen von vier Datentypen zurückgeben: **Instant Vector**, **Range Vector**, **Scalar** oder **String**.

---

## Einführung

PromQL ermöglicht Benutzern:
- Zeitreihen mithilfe von **Instant Vector Selektoren** auszuwählen.
- Daten über einen Zeitbereich mithilfe von **Range Vector Selektoren** abzurufen.
- **Operatoren** (arithmetisch, Vergleich, logisch, Aggregation) anzuwenden.
- **Funktionen** wie `rate()`, `sum()`, `avg()` für Analysen zu verwenden.
- Daten über die **HTTP API** abzufragen.

Ausdrücke werden in der Prometheus-UI ausgewertet:
- **Table Tab**: Instant-Abfragen.
- **Graph Tab**: Range-Abfragen.

---

## Zeitreihen-Selektoren

Zeitreihen-Selektoren definieren, welche Metriken und Labels abgerufen werden sollen.

### Instant Vector Selektoren

Wählt die neueste Stichprobe für jede passende Zeitreihe aus.

**Syntax**:
```
<metric_name>{<label_matchers>}
```

**Beispiele**:
- Alle Zeitreihen mit der Metrik `http_requests_total`:
  ```
  http_requests_total
  ```
- Spezifischer Job und Gruppe:
  ```
  http_requests_total{job="prometheus", group="canary"}
  ```
- Regex-Match auf Environment und Ausschluss der GET-Methode:
  ```
  http_requests_total{environment=~"staging|testing|development", method!="GET"}
  ```
- Match auf `__name__`:
  ```
  {__name__=~"job:.*"}
  ```

**Label Matcher**:
- `=` : exakte Übereinstimmung
- `!=` : ungleich
- `=~` : Regex-Match (verankert)
- `!~` : kein Regex-Match

> Hinweis: `{job=~".+"}` ist gültig; `{}` allein ist ungültig.

---

### Range Vector Selektoren

Wählt einen Bereich von Stichproben über die Zeit aus.

**Syntax**:
```
<instant_selector>[<duration>]
```

**Beispiel**:
- Letzte 5 Minuten von `http_requests_total` für den Job `prometheus`:
  ```
  http_requests_total{job="prometheus"}[5m]
  ```

> Der Bereich ist **links-offen, rechts-geschlossen**: schließt die Startzeit aus, schließt die Endzeit ein.

---

### Offset Modifier

Verschiebt die Auswertungszeit vorwärts oder rückwärts.

**Syntax**:
```
<selector> offset <duration>
```

**Beispiele**:
- Wert von `http_requests_total` vor 5 Minuten:
  ```
  http_requests_total offset 5m
  ```
- Rate von vor 1 Woche:
  ```
  rate(http_requests_total[5m] offset 1w)
  ```
- Vorausschau (negativer Offset):
  ```
  rate(http_requests_total[5m] offset -1w)
  ```

> Muss unmittelbar auf den Selektor folgen.

---

### `@` Modifier

Wertet zu einem bestimmten Zeitstempel aus.

**Syntax**:
```
<selector> @ <timestamp>
```

**Beispiele**:
- Wert zum Unix-Zeitstempel `1609746000`:
  ```
  http_requests_total @ 1609746000
  ```
- Rate zu einer bestimmten Zeit:
  ```
  rate(http_requests_total[5m] @ 1609746000)
  ```
- Verwende `start()` oder `end()`:
  ```
  http_requests_total @ start()
  rate(http_requests_total[5m] @ end())
  ```

> Kann mit `offset` kombiniert werden.

---

## Rate und Aggregationen

PromQL unterstützt **Rate**- und **Aggregations**-Operatoren, um Metriken über die Zeit oder über Reihen hinweg zu berechnen.

### Rate-Funktion

Berechnet die durchschnittliche pro-Sekunde Rate der Zunahme.

**Beispiel**:
```
rate(http_requests_total[5m])
```

> Wird auf **Range Vectors** angewendet.

---

### Aggregationsoperatoren

Wenden auf Instant Vectors an, um Zeitreihen zu kombinieren.

**Beispiele**:
- Summe aller `http_requests_total`:
  ```
  sum(http_requests_total)
  ```
- Durchschnitt pro Instanz:
  ```
  avg by (instance)(http_requests_total)
  ```
- Anzahl pro Job:
  ```
  count by (job)(http_requests_total)
  ```

> Aggregation erfordert passende Reihen; verwende `by` oder `without` Klauseln.

---

## Operatoren

PromQL unterstützt mehrere Operatortypen.

### Arithmetische Operatoren

| Operator | Beschreibung       | Beispiel                         |
|----------|--------------------|-----------------------------------|
| `+`      | Addition           | `rate(a[5m]) + rate(b[5m])`       |
| `-`      | Subtraktion        | `rate(a[5m]) - rate(b[5m])`       |
| `*`      | Multiplikation     | `http_requests_total * 60`        |
| `/`      | Division           | `rate(a[5m]) / rate(b[5m])`       |
| `%`      | Modulo             | `http_requests_total % 100`       |

> Operanden müssen kompatibel sein (gleicher Typ und Form).

---

### Vergleichsoperatoren

Vergleichen zwei Instant Vectors.

| Operator | Beschreibung       | Beispiel                             |
|----------|--------------------|---------------------------------------|
| `==`     | Gleich             | `rate(a[5m]) == rate(b[5m])`         |
| `!=`     | Ungleich           | `rate(a[5m]) != 0`                   |
| `>`      | Größer als         | `http_requests_total > 100`          |
| `<`      | Kleiner als        | `http_requests_total < 10`           |
| `>=`     | Größer oder gleich | `rate(a[5m]) >= 2`                   |
| `<=`     | Kleiner oder gleich| `http_requests_total <= 5`           |

> Gibt einen booleschen Instant Vector zurück.

---

### Logische Operatoren

Kombinieren boolesche Ausdrücke.

| Operator | Beschreibung       | Beispiel                                |
|----------|--------------------|------------------------------------------|
| `and`    | Logisches UND      | `rate(a[5m]) > 1 and rate(b[5m]) > 1`   |
| `or`     | Logisches ODER     | `rate(a[5m]) > 1 or rate(b[5m]) > 1`    |
| `unless` | Außer              | `rate(a[5m]) unless rate(b[5m]) > 0`    |

> Operanden müssen boolesche Vektoren gleicher Kardinalität sein.

---

## Funktionen

PromQL enthält eingebaute Funktionen für Transformation und Analyse.

**Häufige Funktionen**:
- `rate(v range-vector)` – pro-Sekunde Rate.
- `irate(v range-vector)` – momentane Rate (letzte zwei Punkte).
- `avg(v)` – Durchschnittswert.
- `sum(v)` – Summe der Werte.
- `count(v)` – Anzahl der Elemente.
- `min(v)`, `max(v)` – Minimum/Maximum.
- `quantile(v instant-vector, q)` – Perzentil.

**Beispiel**:
```
quantile by (job)(0.95, http_request_duration_seconds_bucket[5m])
```

> Siehe [Prometheus Functions Dokumentation](https://prometheus.io/docs/prometheus/latest/querying/functions/) für die vollständige Liste.

---

## HTTP API für Abfragen

PromQL-Abfragen können über die HTTP API gesendet werden.

### Instant-Abfragen

**Endpoint**: `/api/v1/query`

**Methode**: `GET`

**Parameter**:
- `query`: PromQL-Ausdruck
- `time`: Auswertungszeitstempel (Unix-Sekunden, optional)
- `timeout`: Abfragetimeout (z.B. `30s`)

**Beispiel**:
```
GET /api/v1/query?query=http_requests_total{job="prometheus"}&time=1609746000
```

**Antwort**: JSON mit `status`, `data.result` (Instant Vector oder Scalar).

---

### Range-Abfragen

**Endpoint**: `/api/v1/query_range`

**Parameter**:
- `query`: PromQL-Ausdruck
- `start`: Startzeit (Unix-Sekunden)
- `end`: Endzeit (Unix-Sekunden)
- `step`: Auflösungsschritt (z.B. `15s`)

**Beispiel**:
```
GET /api/v1/query_range?query=rate(http_requests_total[5m])&start=1609746000&end=1609746600&step=10s
```

**Antwort**: JSON mit Zeitreihendaten bei jedem Schritt.

---

## Zusätzliche Hinweise

- **Literale**:
  - Strings: `"hello"`, `'world'`, `` `raw` ``
  - Floats: `3.14`, `-2.5e-3`, `1_000`, `0xFF`
  - Dauer: `5m`, `1h30m`, `500ms`

- **Kommentare**: Beginnen mit `#`

- **Veraltet**: Reihen werden nach 5 Minuten (Standard) ohne Updates veraltet.

- **Subquery**: Führt eine Instant-Abfrage über einen Bereich aus:
  ```
  rate(http_requests_total[10m:5m])[5m]
  ```

---

Dieser Leitfaden behandelt den Kern von PromQL für Anfänger bis fortgeschrittene Benutzer. Für fortgeschrittene Verwendung siehe [Prometheus Querying Basics](https://prometheus.io/docs/prometheus/latest/querying/basics/) und verlinkte Seiten.