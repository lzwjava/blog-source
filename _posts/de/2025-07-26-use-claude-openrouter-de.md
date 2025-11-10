---
audio: false
generated: true
lang: de
layout: post
title: Zugriff auf Claude über OpenRouter
translated: true
type: note
---

### So verwenden Sie Claude-Modelle mit OpenRouter (für chinesische Nutzer ohne Anthropic-API-Zugang)

Als chinesischer Nutzer könnten Sie aufgrund regionaler Beschränkungen Schwierigkeiten haben, direkt auf die Claude-API von Anthropic zuzugreifen. OpenRouter ist jedoch eine zuverlässige Alternative, die als einheitliches API-Gateway für mehrere KI-Anbieter fungiert, einschließlich der Claude-Modelle von Anthropic. OpenRouter ist in China zugänglich (sowohl die Website als auch die API-Endpunkte sind nicht blockiert), sodass Sie Anfragen an Claude routen können, ohne ein direktes Anthropic-Konto oder einen API-Schlüssel zu benötigen. Es ist ein Pay-per-Use-Modell (Sie müssen eine Zahlungsmethode hinterlegen), aber die Registrierung ist kostenlos und es unterstützt ein kostenloses Kontingent für eingeschränkte Nutzung.

Die API von OpenRouter ist mit dem Format von OpenAI kompatibel, sodass Sie vertraute Bibliotheken wie das OpenAI Python SDK verwenden können. Im Folgenden skizziere ich die Schritte für den Einstieg und gebe Code-Beispiele für die Verwendung von Claude in Python.

#### Schritt 1: Registrieren Sie sich bei OpenRouter
1. Besuchen Sie die OpenRouter-Website: https://openrouter.ai.
2. Klicken Sie auf "Sign Up" oder "Get Started" (normalerweise oben rechts).
3. Erstellen Sie ein Konto mit Ihrer E-Mail-Adresse (oder über GitHub/Google-Login, falls verfügbar). Es wird kein VPN benötigt, da die Website in China funktioniert.
4. Verifizieren Sie nach der Registrierung Ihre E-Mail-Adresse, falls erforderlich.
5. Gehen Sie zum Dashboard und fügen Sie eine Zahlungsmethode hinzu (z.B. Kreditkarte), um Ihr Konto aufzuladen. OpenRouter berechnet basierend auf der Token-Nutzung, aber Sie können mit einer kleinen Einzahlung beginnen. Überprüfen Sie die Preise auf der Preis-Seite für Details zu den Claude-Modellen.

#### Schritt 2: Erzeugen Sie einen API-Schlüssel
1. Navigieren Sie in Ihrem OpenRouter-Dashboard zum Abschnitt "API Keys" oder "Keys".
2. Erstellen Sie einen neuen API-Schlüssel (er sieht aus wie eine lange Zeichenkette, z.B. `sk-or-v1-...`).
3. Kopieren und speichern Sie ihn sicher – behandeln Sie ihn wie ein Passwort. Sie werden diesen in Ihrem Code anstelle eines Anthropic-Schlüssels verwenden.

#### Schritt 3: Wählen Sie ein Claude-Modell
OpenRouter listet die Claude-Modelle von Anthropic mit IDs wie:
- `anthropic/claude-3.5-sonnet` (empfohlen für die meisten Aufgaben; ausgewogen und leistungsfähig).
- `anthropic/claude-3-opus` (leistungsstärker, aber teurer).
- Neuere Versionen (z.B. Claude 3.7, falls 2025 verfügbar) werden auf https://openrouter.ai/models?providers=anthropic aufgelistet.

Sie können die Modelle-Seite durchsuchen, um Kosten, Kontextlimits und Verfügbarkeit einzusehen.

#### Schritt 4: Richten Sie Ihre Umgebung ein
- Installieren Sie Python, falls noch nicht geschehen (Version 3.8+ empfohlen).
- Installieren Sie die OpenAI-Bibliothek: Führen Sie `pip install openai` in Ihrem Terminal aus.

#### Schritt 5: Verwenden Sie Claude im Code
Verwenden Sie das OpenAI SDK mit der Basis-URL von OpenRouter (`https://openrouter.ai/api/v1`). Geben Sie die Claude-Modell-ID in Ihren Anfragen an.

Hier ein einfaches Python-Beispiel für einen Chat mit Claude 3.5 Sonnet:

```python
from openai import OpenAI

# Initialisieren Sie den Client mit dem OpenRouter-Endpunkt und Ihrem API-Schlüssel
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="YOUR_OPENROUTER_API_KEY_HERE",  # Ersetzen Sie dies mit Ihrem echten Schlüssel
)

# Senden Sie eine Anfrage an Claude
completion = client.chat.completions.create(
    model="anthropic/claude-3.5-sonnet",  # Verwenden Sie die Claude-Modell-ID
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello, what is the capital of China?"}
    ],
    temperature=0.7,  # Optional: Anpassen für Kreativität (0-1)
    max_tokens=150    # Optional: Antwortlänge begrenzen
)

# Drucken Sie die Antwort
print(completion.choices[0].message.content)
```

- **Erklärung**: Dies sendet einen System-Prompt und eine Benutzernachricht an Claude, erhält eine Antwort und gibt sie aus. Ersetzen Sie den API-Schlüssel und passen Sie die Parameter nach Bedarf an.
- **Wenn Sie rohe HTTP-Anfragen bevorzugen** (ohne die OpenAI-Bibliothek):

```python
import requests
import json

response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": "Bearer YOUR_OPENROUTER_API_KEY_HERE",
        "Content-Type": "application/json"
    },
    data=json.dumps({
        "model": "anthropic/claude-3.5-sonnet",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello, what is the capital of China?"}
        ]
    })
)

# Antwort parsen und ausgeben
data = response.json()
print(data['choices'][0]['message']['content'])
```

- **Tipps**:
  - Fügen Sie optionale Header wie `"HTTP-Referer": "your-site-url"` und `"X-Title": "Your App Name"` hinzu, um die Nutzung zuzuordnen (hilft bei Bestenlisten und potenziellen kostenlosen Guthaben).
  - Überwachen Sie die Nutzung in Ihrem OpenRouter-Dashboard, um unerwartete Kosten zu vermeiden.
  - Für Streaming-Antworten oder erweiterte Funktionen (z.B. Tools) lesen Sie die vollständige Dokumentation von OpenRouter.
  - Wenn Sie auf Ratenbegrenzungen oder Fehler stoßen, überprüfen Sie Ihr Guthaben oder versuchen Sie ein anderes Modell.

#### Problembehebung
- **API-Fehler**: Stellen Sie sicher, dass Ihr Schlüssel korrekt ist und Guthaben vorhanden ist. Testen Sie zuerst mit einem günstigen Modell.
- **Regionale Probleme**: Falls Blockaden auftreten (unwahrscheinlich), verwenden Sie ein VPN, aber OpenRouter ist dafür ausgelegt, solche Beschränkungen für unterstützte Modelle zu umgehen.
- **Kostenlose Alternativen**: Für eingeschränkten kostenlosen Zugang erkunden Sie Proxies wie Puter.js (diese können jedoch Einschränkungen haben).

Dieses Setup ermöglicht Ihnen die programmatische Nutzung von Claude ohne direkten Anthropic-Zugang. Wenn Sie Integrationen mit spezifischen Tools (z.B. Cursor IDE oder Make.com) benötigen, suchen Sie nach Tutorials dafür.

Referenzen:  
[OpenRouter Dokumentation](https://openrouter.ai/docs)  
[Anthropic Claude auf OpenRouter](https://openrouter.ai/anthropic/claude-3.5-sonnet)  
[Verwendung von OpenRouter in China](https://medium.com/ai-simplified-in-plain-english/not-re-inventing-the-wheel-in-ai-2ec3e76ae2bd)  
[So verwenden Sie Claude in China](https://www.comparitech.com/blog/vpn-privacy/how-to-use-claude-in-china/)