---
audio: false
generated: true
lang: de
layout: post
title: Günstigste Einfache Google Cloud VM
translated: true
type: note
---

Bei der Suche nach einer kostengünstigen Virtual Machine (VM) auf Google Cloud gibt es einige Optionen und Überlegungen, die Sie beachten sollten, um Ihr Budget von etwa 5 US-Dollar pro Monat einzuhalten. Hier sind einige Schritte und Tipps, um die günstigste VM-Option zu finden:

1.  **Shared-Core VMs**: Google Cloud bietet Shared-Core VMs an, die die preisgünstigsten Optionen sind. Diese VMs teilen sich die CPU-Leistung mit anderen Kunden, was zu einer weniger robusten Leistung führen kann, aber sie sind deutlich günstiger. Dies könnte ein guter Ausgangspunkt für einen einfachen Server mit geringen Ressourcenanforderungen sein.

2.  **Preemptible VMs**: Ziehen Sie die Verwendung von Preemptible VMs in Betracht, die erhebliche Rabatte im Vergleich zu regulären VMs bieten. Diese VMs können von Google Cloud beendet werden, wenn ihre Ressourcen anderweitig benötigt werden, daher eignen sie sich am besten für fehlertolerante Workloads. Preemptible VMs können Rabatte von bis zu 80 % gegenüber den regulären Preisen bieten.

3.  **Tau VMs**: Die Tau VMs von Google Cloud sind für Scale-Out-Workloads konzipiert und bieten bis zu 42 % höhere Preis-Leistung im Vergleich zu General-Purpose VMs. Diese könnten für bestimmte Arten von Workloads kostengünstiger sein.

4.  **Custom Machine Types**: Sie können benutzerdefinierte Maschinentypen erstellen, die auf Ihre spezifischen Bedürfnisse zugeschnitten sind. Dies kann dazu beitragen, die Kosten zu senken, indem Sie nur für die Ressourcen bezahlen, die Sie benötigen. Diese Flexibilität ermöglicht es Ihnen, CPU und Arbeitsspeicher genau auf Ihre Workload-Anforderungen abzustimmen.

5.  **Sustained Use Discounts**: Google Cloud wendet automatisch Rabatte für andauernde Nutzung (Sustained Use Discounts) für VMs an, die einen erheblichen Teil des Abrechnungsmonats laufen. Der Rabatt erhöht sich mit der Nutzungsdauer und kann bis zu 30 % unter dem regulären Preis liegen.

6.  **Free Tier**: Google Cloud bietet einen Free Tier an, der eine kleine Menge an Compute-Ressourcen pro Monat beinhaltet. Dies könnte für sehr einfache Anwendungen ausreichen und die Kosten weiter senken.

7.  **Kostenrechner**: Verwenden Sie den Google Cloud Pricing Calculator, um die Kosten verschiedener Konfigurationen zu schätzen und das kosteneffizienteste Setup für Ihre Bedürfnisse zu finden.

8.  **Spot VMs**: Spot VMs bieten dynamische Preisgestaltung mit Rabatten von 60-91 % auf den On-Demand-Preis für die meisten Maschinentypen. Diese können eine sehr kostengünstige Option sein, wenn Ihre Workload Unterbrechungen tolerieren kann.

Für einen einfachen Server mit geringen Ressourcenanforderungen könnte der Start mit einer Shared-Core oder Preemptible VM der beste Ansatz sein. Sie können dann die Leistung überwachen und die Konfiguration bei Bedarf anpassen, um Kosten und Leistung in Einklang zu bringen.