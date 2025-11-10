---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: Verstehen der npm --legacy-peer-deps-Option
translated: true
type: note
---

### Übersicht
Die Option `--legacy-peer-deps` ist eine Flag, die mit npm (Node Package Manager) verwendet wird, um zu steuern, wie Peer-Abhängigkeiten während der Paketinstallation behandelt werden. Peer-Abhängigkeiten sind Abhängigkeiten, die ein Paket erwartet, dass ein anderes sie bereitstellt, aber sie werden in neueren npm-Versionen nicht automatisch installiert.

### Verhalten
- **Standard npm (v7+)**: Standardmäßig werden die Anforderungen für Peer-Abhängigkeiten strikt durchgesetzt. Wenn ein Paket eine Peer-Abhängigkeit deklariert, die nicht erfüllt ist, warnt npm oder bricht die Installation ab, um Konflikte zu verhindern.
- **Mit --legacy-peer-deps**: Es greift auf das ältere Verhalten (aus npm v3~v6) zurück, bei dem fehlende Peer-Abhängigkeiten automatisch installiert werden, selbst wenn dies zu Duplikaten oder Nichtübereinstimmungen führt. Dies kann einige Probleme mit Legacy-Paketen lösen, aber möglicherweise zu Fehlern führen.

### Beispiel zur Verwendung
In einem Terminal würden Sie Folgendes ausführen:
```
npm install some-package --legacy-peer-deps
```
Dies wird häufig für Projekte verwendet, die auf älteren Bibliotheken aufbauen, die ihre Peer-Abhängigkeitsdeklarationen nicht aktualisiert haben, wie es in vielen React- oder Angular-Setups vor der strikten Peer-Behandlung von npm der Fall war.

### Wann man es verwenden sollte
Verwenden Sie es sparsam, da es Sicherheitsvorkehrungen umgeht und zu einem "Dependency Hell" führen könnte. Bevorzugen Sie das Aktualisieren von Paketen oder die Verwendung von `--force`/`--save-dev` für bessere Alternativen. Weitere Details finden Sie in der offiziellen npm-Dokumentation zu Peer-Abhängigkeiten.