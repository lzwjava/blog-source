---
audio: false
generated: true
lang: de
layout: post
title: 'Meta Spatial SDK: Android zu XR'
translated: true
type: note
---

Das **Meta Spatial SDK** ist ein Wendepunkt für Entwickler, die immersive Anwendungen für Metas VR/MR-Headsets erstellen möchten, insbesondere für solche, die mit **Meta Horizon OS** laufen (wie die Meta Quest Serie). Sein Hauptzweck ist es, die Lücke zwischen traditioneller Android-Mobile-App-Entwicklung und den einzigartigen Fähigkeiten des Spatial Computing zu schließen.

Hier ist eine kurze Einführung in das Meta Spatial SDK:

**Was ist es?**

Das Meta Spatial SDK ist ein neues Framework, das Android-Entwicklern ermöglicht, ihre vorhandenen Fähigkeiten, Tools und Bibliotheken (wie Android Studio und Kotlin) zu nutzen, um umfassende, immersive Mixed-Reality-Erlebnisse auf Meta Quest Geräten zu erstellen. Vor diesem SDK erforderte die Entwicklung für Quest oft die Verwendung einer vollwertigen Game Engine wie Unity oder Unreal, was eine erhebliche Hürde für mobile-first-Entwickler darstellen konnte.

**Wichtige Ziele und Vorteile:**

*   **Demokratisierung der XR-Entwicklung:** Es senkt die Einstiegshürde für Mobile-Entwickler und ermöglicht so einer breiteren Palette von Entwicklern, für Spatial Computing zu entwickeln.
*   **Nutzung vorhandener Fähigkeiten:** Entwickler können ihre vertraute Android-Entwicklungsumgebung nutzen, was die Lernkurve verringert und die Entwicklung beschleunigt.
*   **Erweiterung von 2D-Apps in 3D:** Es ermöglicht Entwicklern, bestehende 2D-Android-Anwendungen auf Meta Horizon OS zu portieren und sie mit 3D-Elementen, Mixed-Reality-Funktionen und räumlichen Interaktionen zu erweitern.
*   **Schnelle Iteration:** Das SDK bietet einen schnellen Workflow, der ein rasches Prototyping, Erstellen und Testen von räumlichen Ideen ermöglicht.
*   **Verbesserte Benutzererfahrung:** Es erleichtert die Erstellung von Apps, die über traditionelle flache Bildschirme hinausgehen, und bietet Funktionen wie 3D-Rendering, Video-Passthrough, Hand-Tracking, Spatial Audio und Physik für fesselndere Interaktionen.

**Kernfähigkeiten und Funktionen:**

*   **Native Android-Entwicklung:** Basiert auf Kotlin und integriert sich nahtlos in das Android-Ökosystem.
*   **Mixed-Reality-Funktionen:** Zugriff auf die Passthrough-Kamera (Camera2 API) ermöglicht das Verschmelzen von virtuellen Inhalten mit der realen Welt.
*   **3D-Rendering:** Unterstützt moderne Grafik-Pipelines, einschließlich GLTF-Modelle, Physically-Based Rendering (PBR), Animationen und Rigid-Body-Physik.
*   **Interaktive Panels:** Ermöglicht die Erstellung von 2D-UI-Panels innerhalb der 3D-Umgebung, erstellt mit vertrauten Android-UI-Frameworks wie Jetpack Compose.
*   **Eingabe und Interaktionen:** Bietet APIs für Hand-Tracking, Controller-Eingabe und andere natürliche Benutzerinteraktionen.
*   **Szenerfassung:** Ermöglicht Entwicklern den Zugriff auf Daten über die physische Umgebung des Benutzers.
*   **Spatial Audio:** Tools zur Einbindung von räumlichem Sound zur Steigerung der Immersion.
*   **Meta Spatial Editor:** Ein Begleittool, das es Entwicklern ermöglicht, 2D- und 3D-Elemente innerhalb ihrer räumlichen Anwendungen visuell anzuordnen und zu komponieren, ohne einen vollwertigen Game-Engine-Editor zu benötigen.
*   **Entity-Component-System (ECS):** Ein Architekturmuster, das innerhalb des SDK verwendet wird, um modulare und leistungsstarke räumliche Anwendungen zu erstellen.

Im Wesentlichen befähigt das Meta Spatial SDK Android-Entwickler, einfach in die Welt der virtuellen und gemischten Realität einzusteigen und traditionelle Mobile Apps in überzeugende räumliche Erlebnisse auf Meta Quest Geräten zu verwandeln.