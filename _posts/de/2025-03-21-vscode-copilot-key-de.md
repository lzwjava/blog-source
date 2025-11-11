---
audio: false
generated: true
lang: de
layout: post
title: Visual Studio Code Copilot-Erweiterung
translated: true
type: note
---

Nein, das Visual Studio Code (VSCode) Copilot-Plugin kann keinen benutzerdefinierten API-Schlüssel, wie Ihren Gemini-Schlüssel, verwenden. GitHub Copilot, entwickelt von GitHub (im Besitz von Microsoft), ist ein KI-gestütztes Code-Vervollständigungstool, das eng mit der GitHub-Infrastruktur und bestimmten KI-Modellen verzahnt ist, ursprünglich basierend auf OpenAIs Codex. Es setzt auf eine Authentifizierung über ein GitHub-Konto und ein Copilot-Abonnement und bietet keine integrierte Option, es mit benutzerdefinierten API-Schlüsseln anderer Anbieter, wie etwa von Google Gemini, zu konfigurieren.

Wenn Sie jedoch einen Gemini-Schlüssel besitzen, gibt es alternative Möglichkeiten, diesen in VSCode zu nutzen:

- **Gemini Code Assist**: Google bietet einen KI-gestützten Coding-Assistenten namens Gemini Code Assist an, für den es eine offizielle Erweiterung für VSCode gibt. Diese Erweiterung ist für die Zusammenarbeit mit Googles Gemini-Modellen konzipiert und ermöglicht Ihnen voraussichtlich, Ihren Gemini-API-Schlüssel zur Authentifizierung einzugeben. Sie können diese Erweiterung aus dem VSCode Marketplace installieren und mit Ihrem Schlüssel konfigurieren, um von Gemini gestützte Code-Vervollständigung zu erhalten.

- **Drittanbieter-Plugins**: Möglicherweise sind auch andere VSCode-Erweiterungen von Drittanbietern im Marketplace verfügbar, die mehrere KI-Anbieter unterstützen und die Verwendung benutzerdefinierter API-Schlüssel, auch für Gemini, erlauben. Diese Plugins würden es Ihnen ermöglichen, sich mit der Gemini-API für Code-Vorschläge zu verbinden, erfordern jedoch möglicherweise eine zusätzliche Einrichtung.

### Warum Copilot keine benutzerdefinierten Schlüssel unterstützt
GitHub Copilot ist ein proprietäres Tool, das für sein eigenes Ökosystem optimiert ist. Obwohl es in jüngster Zeit Entwicklungen gab, bei denen GitHub eine Partnerschaft mit Google einging, um Gemini-Modelle in Copilot zu integrieren, wird diese Integration von GitHub verwaltet und erlaubt es Benutzern nicht, direkt ihre eigenen Gemini-API-Schlüssel einzugeben. Stattdessen wird der Zugriff auf alle unterstützten Modelle (einschließlich Gemini, falls verfügbar) über den Copilot-Dienst selbst bereitgestellt, unter der Kontrolle von GitHub.

### Praktische Empfehlung
Wenn Ihr Ziel darin besteht, Ihren Gemini-Schlüssel in VSCode zu verwenden, ist die Installation der **Gemini Code Assist Erweiterung** die unkomplizierteste und offiziell unterstützte Option. So können Sie vorgehen:

1.  Öffnen Sie VSCode.
2.  Gehen Sie zur Erweiterungs-Ansicht (`Strg+Umschalt+X` oder `Cmd+Umschalt+X` auf macOS).
3.  Suchen Sie nach "Gemini Code Assist" (oder überprüfen Sie die offizielle Dokumentation von Google auf den genauen Namen).
4.  Installieren Sie die Erweiterung und befolgen Sie die Einrichtungsanleitung, um Ihren Gemini-API-Schlüssel einzugeben.

Dieser Ansatz stellt sicher, dass Sie das Tool wie beabsichtigt verwenden und vermeidet potenzielle Probleme wie die Verletzung von Nutzungsbedingungen oder den Umgang mit nicht unterstützten Modifikationen an Copilot.

Zusammenfassend lässt sich sagen: Während das VSCode Copilot-Plugin selbst Ihren Gemini-Schlüssel nicht verwenden kann, können Sie Ihr Ziel, Gemini in VSCode zu nutzen, dennoch erreichen, indem Sie sich für die Gemini Code Assist Erweiterung oder ein kompatibles Drittanbieter-Plugin entscheiden.