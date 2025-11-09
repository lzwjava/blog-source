---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast:free
title: Übersicht Pivotal Cloud Foundry
translated: true
type: note
---

### Überblick über Pivotal Cloud Foundry (PCF)
Pivotal Cloud Foundry (PCF), seit der Übernahme von Pivotal durch VMware im Jahr 2019 Teil von VMware Tanzu, ist eine kommerzielle Distribution der Open-Source-Plattform Cloud Foundry. Es handelt sich um eine Platform as a Service (PaaS), die entwickelt wurde, um die Bereitstellung, Skalierung und Verwaltung von Cloud-nativen Anwendungen zu vereinfachen. PCF abstrahiert die Komplexität der zugrunde liegenden Infrastruktur (IaaS) und ermöglicht es Entwicklern, sich auf den Code zu konzentrieren, anstatt auf Server, Netzwerke oder Orchestrierung. Es ist besonders beliebt in regulierten Branchen wie dem Bankwesen aufgrund seines Fokus auf Sicherheit, Compliance und Portabilität.

PCF ist kein eigenständiger Cloud-Anbieter wie AWS, Azure oder GCP – es ist eine Ebene, die *auf* diesen IaaS-Anbietern, in On-Premise-Rechenzentren oder in privaten Clouds laufen kann. Dies macht es zu einem "Cloud-Betriebssystem" für Anwendungen.

### PCF/Cloud Foundry Design und Architektur
Das Design von Cloud Foundry ist modular, opinionated und basiert auf den "12-Factor-App"-Prinzipien für skalierbare, wartbare Software. Hier ist eine grobe Aufschlüsselung:

#### Kernkomponenten und Ablauf
1.  **Diego (Runtime Engine)**: Das Herzstück von PCF. Es ersetzt das ältere Garden-Container-System durch eine moderne Orchestrierungsebene, die Container verwendet (basierend auf Linux-Containern oder später Garden/Linux für Isolation). Diego verwaltet Anwendungsinstanzen über "Cells" (virtuelle Maschinen oder Bare-Metal-Server) hinweg. Es kümmert sich um Staging (das Bauen von Apps aus Quellcode in ausführbare Droplets), das Routen von Traffic und die Skalierung über Auto-Scaling-Gruppen.

2.  **Routing und Lastverteilung**: Der Gorouter (ein hochleistungsfähiger Reverse-Proxy) leitet eingehende Anfragen an die richtigen App-Instanzen basierend auf Routen (z.B. `app.example.com`). Er unterstützt Sticky Sessions und Health Checks.

3.  **Services Marketplace**: PCF bietet ein "Service Broker"-Modell, bei dem verwaltete Dienste (Datenbanken wie MySQL/PostgreSQL, Message Queues wie RabbitMQ oder Drittanbieter-Integrationen) katalogisiert werden. Apps "binden" sich an diese Dienste, um automatisch Anmeldeinformationen und Verbindungsdetails zu erhalten, ohne Hardcoding.

4.  **Sicherheit und Identität**:
    *   UAA (User Account and Authentication): Verarbeitet OAuth2-basierte Authentifizierung, Single Sign-On (SSO) und rollenbasierte Zugriffskontrolle (RBAC).
    *   Es integriert sich mit LDAP, SAML oder Unternehmens-Identity-Providern, was für Banken entscheidend ist.

5.  **Buildpacks und Laufzeitumgebungen**: PCF verwendet "Buildpacks" (vorkonfigurierte Skripte), um Apps in Sprachen wie Java, Node.js, Python, Go oder .NET zu erkennen und zu verpacken. Es unterstützt polyglotte (mehrsprachige) Umgebungen in einer einzigen Plattform.

6.  **BOSH (Deployment Orchestrator)**: Das zugrunde liegende Tool für die Installation und Verwaltung von PCF. Es verwendet YAML-Manifeste, um Komponenten idempotent bereitzustellen und zu aktualisieren (um konsistente Zustände sicherzustellen). BOSH übernimmt die VM-Bereitstellung, Upgrades und Überwachung.

7.  **Monitoring und Protokollierung**: Integrierte Tools wie Loggregator (für strukturierte Logs) und Firehose (für Streaming-Metriken) speisen Tools wie den ELK Stack oder Splunk. Ops Metrics bieten eingebaute Observability.

#### Wichtige Designprinzipien
*   **Self-Service und Entwicklerzentriert**: Entwickler pushen Apps via `cf push` CLI, und die Plattform erledigt den Rest (Skalierung, Health Checks, Zero-Downtime-Deployments).
*   **Multi-Tenancy**: Mehrere Teams oder Organisationen können die Plattform sicher via "Spaces" und Quotas teilen.
*   **Horizontale Skalierung**: Apps skalieren heraus, indem Instanzen über Cells repliziert werden, mit eingebauter Fehlertoleranz (z.B. wenn eine Cell ausfällt, plant Diego Tasks neu).
*   **API-gesteuert**: Alles wird über eine RESTful API (Cloud Controller) verfügbar gemacht, was Automatisierung mit Tools wie Concourse CI/CD ermöglicht.
*   **Erweiterbarkeit**: Unterstützt Kubernetes-Integration (via PKS, jetzt Tanzu Kubernetes Grid) für Container-Orchestrierung und Service Meshes wie Istio.

Die Architektur ist horizontal skalierbar und läuft auf IaaS wie vSphere, AWS, Azure, GCP oder OpenStack. Ein typisches Deployment könnte 10-20 VMs für einen Produktivbetrieb umfassen, mit Isolation via Netzwerkrichtlinien und Verschlüsselung (TLS überall).

Herausforderungen im Design umfassen sein Java-lastiges Erbe (kann ressourcenintensiv sein) und die Lernkurve für Ops-Teams, aber es ist seit 2011 erprobt.

### Warum wählen einige Banken PCF?
Banken (z.B. HSBC, Barclays, Capital One oder BBVA) wählen oft PCF aufgrund seiner Ausrichtung auf die Bedürfnisse von Finanzdienstleistern. Hier ist der Grund:

1.  **Regulatorische Compliance und Sicherheit**:
    *   PCF unterstützt Standards wie PCI-DSS, FIPS 140-2, GDPR und SOC 2. Es bietet Funktionen wie verschlüsselte etcd-Speicherung, Audit-Logging und feingranulare Zugriffskontrollen.
    *   Banken verarbeiten sensible Daten; PCFs Isolation (z.B. keine Shared Kernels in Multi-Tenant-Setups) und Schwachstellenscans reduzieren Risiken im Vergleich zu roher IaaS.

2.  **Hybrid- und Multi-Cloud-Strategie**:
    *   Viele Banken haben Legacy-On-Premise-Systeme (z.B. Mainframes) und wollen modernisieren, ohne vollständig in die Cloud zu migrieren. PCF ermöglicht "Lift-and-Shift" oder schrittweise Refaktorierung in die Cloud, mit konsistentem Betrieb über private/öffentliche Clouds hinweg.
    *   Es unterstützt air-gapped (vom Netzwerk getrennte) Bereitstellungen für Hochsicherheitsumgebungen.

3.  **Entwicklerproduktivität und Standardisierung**:
    *   PCF bietet einen "Golden Path" für Entwickler: eine CLI, ein Workflow, unabhängig von der Backend-Infrastruktur. Dies beschleunigt die Einführung von Microservices, CI/CD-Pipelines und Blue-Green-Deployments – entscheidend für Low-Latency-Trading- oder Betrugserkennungs-Apps.
    *   Banken mit globalen Teams profitieren von seiner Portabilität; z.B. kann eine in den USA entwickelte App ohne Anpassungen in EU-Rechenzentren deployed werden.

4.  **Anbieterecosystem und Support**:
    *   Pivotal/VMware bietet Enterprise-Support, inklusive 24/7-SLAs und Zertifizierungen. Banken schätzen die verwalteten Dienste (z.B. PCF for PCS, jetzt Tanzu Application Service).
    *   Seine Open-Source-Wurzeln bedeuten keine vollständige Vendor-Lock-in, aber mit kommerzieller Unterstützung für Stabilität.

Fallstudien: Capital One setzte PCF 2015 für seine "Cloud-First"-Strategie ein und nannte schnellere Time-to-Market (z.B. Deployment von Apps in Minuten statt Wochen) als Grund. BBVA nutzte es, um Core-Banking-Apps zu containerisieren und senkte die Kosten um 50%.

Nicht alle Banken nutzen PCF – es ist häufiger in Unternehmen mit komplexen, regulierten Workloads als in Fintech-Startups.

### Warum nicht einfach direkt Azure, AWS oder GCP wählen?
Banken *nutzen* Azure/AWS/GCP intensiv, aber PCF wird oft zusätzlich darauf eingesetzt, anstatt es zu ersetzen. Native Public Cloud PaaS (z.B. AWS Elastic Beanstalk, Azure App Service, Google App Engine) sind großartig für einfache Apps, aber hier ist der Grund, warum PCF vorgezogen oder parallel verwendet werden könnte:

1.  **Vermeidung von Vendor Lock-In**:
    *   Native Dienste binden Sie an einen Anbieter (z.B. AWS Lambda ist nur für AWS). PCF läuft auf allen dreien (via Tiles/Stems für jede Cloud), was es Banken ermöglicht, Anbieter zu wechseln oder zu hedgen (z.B. AWS für die USA, Azure für Europa aufgrund von Data Sovereignty).
    *   Wenn eine Bank die Preise oder Features einer Cloud überwächst, können PCF-Apps mit minimalen Änderungen migriert werden – anders als bei proprietären Formaten.

2.  **Konsistenz über Umgebungen hinweg**:
    *   Public Clouds haben fragmentierte Dienste (z.B. AWS ECS vs. Azure AKS für Container). PCF standardisiert die PaaS-Ebene und bietet eine einheitliche Developer Experience. Dies ist entscheidend für Banken mit verteilten Teams oder Akquisitionen.
    *   Hybride Setups: 70 % der Banken betreiben Hybrid Cloud (laut Gartner); PCF überbrückt On-Premise VMware/vSphere nahtlos mit Public Clouds.

3.  **Erweiterte Enterprise-Features**:
    *   Native PaaS könnte das Zusammenstricken mehrerer Dienste erfordern (z.B. AWS API Gateway + ECS + RDS), was zu Ops-Overhead führt. PCF bündelt diese (z.B. via Marketplace für Broker zu RDS-Äquivalenten).
    *   Besser für Legacy-Migration: Banken haben COBOL/Java-Monolithen; PCFs Buildpacks unterstützen diese ohne komplette Neuentwicklung.
    *   Kosten: Während Public Clouds für bursty Workloads günstiger sind, optimiert PCF die Ressourcennutzung (z.B. via Quota-Erzwingung), und Banken verhandeln Enterprise-Deals.

4.  **Wann Natives gewinnt**:
    *   Pure Serverless? Gehen Sie nativen Weg (z.B. GCP Cloud Run für Event-driven Apps).
    *   Wenn eine Bank vollständig auf eine Cloud setzt (z.B. AWS für ML via SageMaker), könnte sie PCF überspringen, um tiefe Integrationen zu nutzen.
    *   Nachteile von PCF: Höhere Anfangskosten (~100.000 $+ für Lizenzen), steilerer Setup, und es ist weniger "managed" als vollständig gehostete PaaS wie Heroku (jetzt Salesforce).

In der Praxis nutzen viele Banken einen Mix: PCF auf AWS für Core-Apps, native Dienste für Analytics (z.B. Azure Synapse).

### Warum PCF "in der Mitte" haben?
PCF fungiert als Abstraktionsebene (PaaS) zwischen Ihren Anwendungen (oben) und IaaS (unten). Denken Sie an den Cloud-Stack:

*   **IaaS (Fundament)**: AWS EC2, Azure VMs, GCP Compute Engine – stellt rohe Rechen-/Speicher-/Netzwerkleistung bereit.
*   **PaaS (Mitte)**: PCF sitzt hier und verwaltet den Application Lifecycle auf IaaS. Es übernimmt Orchestrierung, Service Discovery und Skalierung, sodass Sie keine VMs direkt verwalten müssen.
*   **Apps (Oben)**: Ihre Microservices, APIs, UIs.

**Vorteile des Mittelsmanns**:
*   **Vereinfachung**: Entwickler müssen keine cloud-spezifischen APIs lernen; Code einmal pushen, überall ausführen.
*   **Portabilität**: Wechseln Sie von AWS zu GCP ohne App-Änderungen – entscheidend für Banken, die Lock-In fürchten oder Geo-Redundanz benötigen.
*   **Ops-Effizienz**: Zentralisiert Governance (z.B. Sicherheitsrichtlinien, Kostenkontrollen) über Clouds hinweg.
*   **Evolution**: Begann als On-Premise-PaaS; integriert sich jetzt mit Kubernetes für moderne Workloads.

Kurz gesagt, PCF konkurriert nicht mit AWS/Azure/GCP – es verbessert sie für Enterprise-Zuverlässigkeit. Wenn Sie für eine Bank evaluieren, ziehen Sie einen Proof-of-Concept in Betracht; VMware bietet Trials via Tanzu an.

Für tiefergehende Einblicke, sehen Sie sich die VMware-Dokumentation oder das Open-Source-Repo von Cloud Foundry an. Wenn Sie Spezifisches haben (z.B. einen Use Case), kann ich das gerne verfeinern!