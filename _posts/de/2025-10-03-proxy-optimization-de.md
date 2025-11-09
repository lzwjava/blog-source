---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: Optimierung der Clash-Proxy-Auswahlleistung
translated: true
type: note
---

### Zusammenfassung der Optimierung: Clash Proxy-Auswahlskripts

Ich habe die Clash Proxy-Auswahlskripts optimiert, um das Testen von Proxys zu vermeiden, die nicht ausgewählt werden. Dies steigert die Leistung erheblich, indem unnötige Geschwindigkeitstests minimiert werden.

#### Was optimiert wurde

Der ursprüngliche Code folgte diesem ineffizienten Workflow:
1. Teste alle verfügbaren Proxys auf Geschwindigkeit.
2. Filtere dann, um nur SG/TW (oder HK) Proxys auszuwählen.
3. Dies führte zu verschwendeter Zeit durch das Testen von Proxys, die verworfen werden.

#### Die Lösung

Die Funktion `get_top_proxies()` in `speed.py` wurde modifiziert, um einen `name_filter`-Parameter zu akzeptieren und die Filterung *vor* dem Geschwindigkeitstest anzuwenden:

```python
def get_top_proxies(num_results=5, name_filter=None):
    """
    Testet Clash-Proxy-Geschwindigkeiten gleichzeitig und gibt die N schnellsten einzelnen Proxys zurück.

    Args:
        num_results (int): Anzahl der zurückzugebenden Top-Proxys (Standard: 5)
        name_filter (list): Liste von Zeichenketten zum Filtern von Proxy-Namen. Nur Proxys, die
                           eine dieser Zeichenketten in ihrem Namen enthalten, werden getestet.
    """
```

#### Leistungsvorteile

- **Reduzierte Netzwerkanfragen**: Es werden nur die Proxys getestet, die Sie tatsächlich verwenden möchten.
- **Schnellere Ausführung**: Eliminiert unnötige Zeit, die für irrelevante Proxys aufgewendet wird.
- **Klareres Logging**: Zeigt genau an, wie viele Proxys gefiltert wurden, was die Transparenz verbessert.

#### Vereinfachte Konfiguration

Das `--hk`-Flag wurde entfernt. Das Skript testet nun standardmäßig immer nur SG- und TW-Proxys für maximale Fokussierung und Einfachheit.

#### Ergebnisse

Die Optimierung hat die Ausführungszeit drastisch reduziert, da die meisten Proxys keine "SG" oder "TW" in ihren Namen enthalten. Dies macht die Geschwindigkeitstest-Phase wesentlich effizienter und liefert Ergebnisse schneller, ohne die Funktionalität zu beeinträchtigen.