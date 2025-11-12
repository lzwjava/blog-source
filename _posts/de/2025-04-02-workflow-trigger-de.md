---
audio: false
generated: true
lang: de
layout: post
title: GitHub-Workflow Auslösen
translated: true
type: note
---

Du hast recht, das direkte Einbetten eines GitHub-Tokens in deinen Frontend-Code ist ein Sicherheitsrisiko. Jeder, der den Quellcode deiner Seite einsehen kann, könnte potenziell auf deinen Token zugreifen und ihn missbrauchen.

Hier ist eine Übersicht sicherer Ansätze, mit denen du deinen GitHub-Workflow über einen Frontend-Button auslösen kannst, zusammen mit Erklärungen und Codebeispielen:

**Kernidee: Einführung eines sicheren Backends**

Der sicherste Weg, dies zu handhaben, ist die Einführung einer Backend-Komponente (ein API-Endpoint), die:

1.  **Die Auslöseanfrage von deinem Frontend empfängt.**
2.  **Deinen GitHub-Token sicher speichert und verwendet.**
3.  **Den authentifizierten API-Aufruf an GitHub durchführt, um deinen Workflow zu dispatchen.**

Auf diese Weise verlässt dein sensibler GitHub-Token niemals deine Server-Umgebung.

Hier sind einige Optionen für dein Backend:

**1. Serverless Functions (z.B. AWS Lambda, Google Cloud Functions, Netlify Functions, Vercel Functions)**

Dies ist oft eine leichtgewichtige und kostengünstige Lösung für einfache API-Endpoints wie diesen.

*   **Funktionsweise:** Du schreibst eine kleine Funktion, die auf einer Serverless-Plattform deployed wird. Diese Funktion enthält die Logik, um die GitHub-API unter Verwendung deines gespeicherten Tokens aufzurufen. Dein Frontend-Button sendet dann eine HTTP-Anfrage an die URL dieser Serverless Function.

*   **Beispiel (Konzeptionell - Du musst dies an deine gewählte Plattform anpassen):**

    **Serverless Function Code (Python - Beispiel für AWS Lambda/API Gateway):**

    ```python
    import os
    import requests
    import json

    def handler(event, context):
        github_token = os.environ.get("GITHUB_TOKEN")
        if not github_token:
            return {
                'statusCode': 500,
                'body': json.dumps({'error': 'GitHub token not configured'})
            }

        owner = "lzwjava"
        repo = "lzwjava.github.io"
        workflow_id = "nytimes.yml"
        ref = "main"
        api_url = f"https://api.github.com/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches"

        headers = {
            'Accept': 'application/vnd.github+json',
            'Authorization': f'Bearer {github_token}',
            'X-GitHub-Api-Version': '2022-11-28',
            'Content-Type': 'application/json'
        }
        payload = {'ref': ref}

        try:
            response = requests.post(api_url, headers=headers, json=payload)
            response.raise_for_status()  # Raise an exception for bad status codes
            return {
                'statusCode': 204,
                'body': ''
            }
        except requests.exceptions.RequestException as e:
            return {
                'statusCode': 500,
                'body': json.dumps({'error': f'Failed to trigger workflow: {e}'})
            }
    ```

    *   **Wichtig:** Du würdest eine Umgebungsvariable (z.B. `GITHUB_TOKEN`) auf deiner Serverless-Plattform konfigurieren, um deinen GitHub Personal Access Token sicher zu speichern.

    **Frontend Code (Modifiziertes `nytimes.js`):**

    ```javascript
    const nytimesDiv = document.querySelector('.nytimes');
    const backendApiUrl = '/.netlify/functions/trigger-nytimes-update'; // Beispiel für Netlify Functions

    if (nytimesDiv) {
        const updateButton = document.createElement('button');
        updateButton.textContent = 'Update NYTimes Articles';
        nytimesDiv.appendChild(updateButton);

        updateButton.addEventListener('click', () => {
            fetch(backendApiUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({}) // Für einen einfachen Trigger benötigst du möglicherweise keinen Body
            })
            .then(response => {
                if (response.status === 204) {
                    alert('Update triggered successfully! Please wait a few minutes to see the result.');
                } else {
                    return response.json().then(data => {
                        alert(`Update failed. Status code: ${response.status}: ${data.error || 'Unknown error'}`);
                        console.error('Update failed:', response, data);
                    });
                }
            })
            .catch(error => {
                alert('Update failed. Check the console for errors.');
                console.error('Error triggering update:', error);
            });
        });
    } else {
        console.error("nytimes div not found!");
    }
    ```

*   **Deployment:** Du musst diese Serverless Function auf deiner gewählten Plattform deployen. Der spezifische Deployments-Prozess variiert je nach Anbieter.

**2. Dein eigener Web-Server (falls vorhanden)**

Wenn du einen eigenen Web-Server hast (z.B. mit Node.js, Python/Flask, etc.), kannst du einen einfachen API-Endpoint auf diesem Server erstellen.

*   **Funktionsweise:** Dein Frontend-Button sendet eine Anfrage an den Endpoint deines Servers. Dein serverseitiger Code, der Zugriff auf deinen GitHub-Token hat (sicher gespeichert als Umgebungsvariable oder in einer Konfigurationsdatei), führt dann den API-Aufruf an GitHub durch.

*   **Beispiel (Konzeptionell - Node.js mit Express):**

    **Serverseitiger Code (Node.js/Express):**

    ```javascript
    const express = require('express');
    const fetch = require('node-fetch');
    require('dotenv').config();

    const app = express();
    const port = 3000;

    app.post('/api/trigger-nytimes-update', async (req, res) => {
        const githubToken = process.env.GITHUB_TOKEN;
        if (!githubToken) {
            return res.status(500).json({ error: 'GitHub token not configured' });
        }

        const owner = "lzwjava";
        const repo = "lzwjava.github.io";
        const workflow_id = "nytimes.yml";
        const ref = "main";
        const apiUrl = `https://api.github.com/repos/${owner}/${repo}/actions/workflows/${workflow_id}/dispatches`;

        const headers = {
            'Accept': 'application/vnd.github+json',
            'Authorization': `Bearer ${githubToken}`,
            'X-GitHub-Api-Version': '2022-11-28',
            'Content-Type': 'application/json'
        };
        const payload = { ref: ref };

        try {
            const response = await fetch(apiUrl, {
                method: 'POST',
                headers: headers,
                body: JSON.stringify(payload)
            });
            if (response.status === 204) {
                res.sendStatus(204);
            } else {
                const data = await response.json();
                res.status(response.status).json({ error: `Failed to trigger workflow: ${JSON.stringify(data)}` });
            }
        } catch (error) {
            console.error('Error triggering workflow:', error);
            res.status(500).json({ error: `Failed to trigger workflow: ${error.message}` });
        }
    });

    app.listen(port, () => {
        console.log(`Server listening at http://localhost:${port}`);
    });
    ```

    *   **Wichtig:** Verwende eine `.env`-Datei (und stelle sicher, dass sie nicht in dein Repository committet wird), um deinen `GITHUB_TOKEN` zu speichern, und greife mit einer Bibliothek wie `dotenv` darauf zu.

    **Frontend Code (Modifiziertes `nytimes.js`):**

    ```javascript
    const nytimesDiv = document.querySelector('.nytimes');
    const backendApiUrl = '/api/trigger-nytimes-update'; // Passe dies an den Endpoint deines Servers an

    // ... (der Rest des Frontend-Codes ist ähnlich dem Serverless Function Beispiel)
    ```

*   **Deployment:** Du musst deine Server-Anwendung auf deinem Web-Server deployen.

**3. GitHub Actions Workflow, ausgelöst durch ein anderes Event (Weniger direkt)**

Dies ist kein direkter Button-Trigger, aber du könntest ein anderes Event einrichten, um deinen Workflow auszulösen, das indirekt durch eine Benutzeraktion initiiert werden könnte. Zum Beispiel:

*   **Geplanter Workflow:** Führe den Update-Workflow regelmäßig aus (z.B. täglich).
*   **Webhook-Trigger:** Wenn du ein anderes System oder einen anderen Dienst hast, mit dem Benutzer interagieren, könnte dieses System einen Webhook auslösen, der dann deinen GitHub Actions Workflow startet.

Diese Optionen bieten jedoch nicht das sofortige, bedarfsgesteuerte Update, das du dir wahrscheinlich von einem Button-Klick wünschst.

**Auswahl des richtigen Ansatzes**

*   **Für einfache statische Seiten:** Serverless Functions sind oft die einfachste und kostengünstigste Lösung. Plattformen wie Netlify und Vercel haben eingebaute Unterstützung für Serverless Functions.
*   **Wenn du bereits einen Web-Server hast:** Die Erstellung eines API-Endpoints auf deinem bestehenden Server ist eine naheliegende Wahl.
*   **Sicherheit hat oberste Priorität:** Priorisiere immer, deinen GitHub-Token sicher auf einem Backend-Server zu halten und expose ihn niemals in deinem Frontend-Code.

**Schritte zur Implementierung (am Beispiel von Serverless Functions):**

1.  **Erstelle eine Serverless Function:** Schreibe den Code für deine Serverless Function (z.B. in Python oder Node.js), der die Logik zum Aufruf der GitHub-API enthält.
2.  **Speichere deinen GitHub-Token sicher:** Konfiguriere eine Umgebungsvariable in den Einstellungen deiner Serverless-Plattform, um deinen GitHub Personal Access Token zu speichern.
3.  **Deploye deine Serverless Function:** Deploye die Funktion auf deiner gewählten Plattform (z.B. Netlify, Vercel, AWS Lambda mit API Gateway). Du erhältst eine URL für deine deployed Function.
4.  **Aktualisiere deinen Frontend-Code:** Passe deine `nytimes.js` Datei an, um eine `POST`-Anfrage an die URL deiner deployed Serverless Function zu senden, wenn der Button geklickt wird.
5.  **Teste:** Deploye dein aktualisiertes Frontend und teste, ob ein Klick auf den Button deinen GitHub Actions Workflow erfolgreich auslöst.

Durch die Implementierung einer dieser backend-basierten Lösungen kannst du einen Button bereitstellen, um deinen GitHub-Workflow sicher auszulösen, ohne deinen sensiblen API-Token in deinem Frontend-Code zu exponieren. Denke daran, den Ansatz zu wählen, der am besten zu deiner aktuellen Infrastruktur und deinen technischen Fähigkeiten passt.