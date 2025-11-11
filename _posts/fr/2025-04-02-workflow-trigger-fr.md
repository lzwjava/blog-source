---
audio: false
generated: true
lang: fr
layout: post
title: Déclenchez Votre Workflow GitHub
translated: true
type: note
---

Vous avez raison, intégrer directement un jeton GitHub dans votre code frontend présente un risque de sécurité. Toute personne visualisant le code source de votre page pourrait potentiellement accéder à votre jeton et l'utiliser de manière abusive.

Voici un aperçu des approches sécurisées que vous pouvez adopter pour déclencher votre workflow GitHub à partir d'un bouton frontend, accompagnées d'explications et d'exemples de code :

**Idée principale : Introduire un Backend Sécurisé**

La manière la plus sécurisée de gérer cela est d'introduire un composant backend (un point de terminaison d'API) qui va :

1.  **Recevoir la demande de déclenchement de votre frontend.**
2.  **Stocker et utiliser de manière sécurisée votre jeton GitHub.**
3.  **Effectuer l'appel API authentifié vers GitHub pour déclencher votre workflow.**

De cette façon, votre jeton GitHub sensible ne quitte jamais votre environnement côté serveur.

Voici quelques options pour votre backend :

**1. Fonctions Sans Serveur (ex. : AWS Lambda, Google Cloud Functions, Netlify Functions, Vercel Functions)**

C'est souvent une solution légère et économique pour des points de terminaison d'API simples comme celui-ci.

*   **Fonctionnement :** Vous écrivez une petite fonction qui est déployée sur une plateforme sans serveur. Cette fonction contiendra la logique pour appeler l'API GitHub en utilisant votre jeton stocké. Votre bouton frontend effectuera alors une requête HTTP vers l'URL de cette fonction sans serveur.

*   **Exemple (Conceptuel - Vous devrez l'adapter à la plateforme choisie) :**

    **Code de la Fonction Sans Serveur (Python - Exemple pour AWS Lambda/API Gateway) :**

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
            response.raise_for_status()  # Lever une exception pour les codes d'état non valides
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

    *   **Important :** Vous configurerez une variable d'environnement (ex. : `GITHUB_TOKEN`) dans votre plateforme sans serveur pour stocker de manière sécurisée votre jeton d'accès personnel GitHub.

    **Code Frontend (Fichier `nytimes.js` modifié) :**

    ```javascript
    const nytimesDiv = document.querySelector('.nytimes');
    const backendApiUrl = '/.netlify/functions/trigger-nytimes-update'; // Exemple pour Netlify Functions

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
                body: JSON.stringify({}) // Vous n'aurez peut-être pas besoin d'un corps pour un simple déclencheur
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

*   **Déploiement :** Vous devrez déployer cette fonction sans serveur sur la plateforme de votre choix. Le processus de déploiement spécifique varie selon le fournisseur.

**2. Votre Propre Serveur Web (si vous en avez un)**

Si vous avez votre propre serveur web (ex. : utilisant Node.js, Python/Flask, etc.), vous pouvez créer un simple point de terminaison d'API sur ce serveur.

*   **Fonctionnement :** Votre bouton frontend envoie une requête au point de terminaison de votre serveur. Votre code côté serveur, qui a accès à votre jeton GitHub (stocké de manière sécurisée comme variable d'environnement ou dans un fichier de configuration), effectue ensuite l'appel API vers GitHub.

*   **Exemple (Conceptuel - Node.js avec Express) :**

    **Code Côté Serveur (Node.js/Express) :**

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

    *   **Important :** Utilisez un fichier `.env` (et assurez-vous qu'il n'est pas commit dans votre dépôt) pour stocker votre `GITHUB_TOKEN` et y accéder en utilisant une bibliothèque comme `dotenv`.

    **Code Frontend (Fichier `nytimes.js` modifié) :**

    ```javascript
    const nytimesDiv = document.querySelector('.nytimes');
    const backendApiUrl = '/api/trigger-nytimes-update'; // Ajustez selon le point de terminaison de votre serveur

    // ... (le reste du code frontend est similaire à l'exemple de fonction sans serveur)
    ```

*   **Déploiement :** Vous devrez déployer votre application serveur sur votre serveur web.

**3. Déclenchement du Workflow GitHub Actions par un Événement Différent (Moins Direct)**

Bien que ce ne soit pas un déclenchement direct par bouton, vous pourriez configurer un événement différent pour déclencher votre workflow, qui pourrait être initié indirectement par une action de l'utilisateur. Par exemple :

*   **Workflow Planifié :** Exécutez le workflow de mise à jour périodiquement (ex. : quotidiennement).
*   **Déclenchement par Webhook :** Si vous avez un autre système ou service avec lequel les utilisateurs interagissent, ce système pourrait déclencher un webhook qui démarre ensuite votre workflow GitHub Actions.

Cependant, ces options ne fournissent pas la mise à jour immédiate et à la demande que vous souhaitez probablement via un clic de bouton.

**Choisir la Bonne Approche**

*   **Pour les sites statiques simples :** Les fonctions sans serveur sont souvent la solution la plus simple et la plus économique. Des plateformes comme Netlify et Vercel ont un support intégré pour les fonctions sans serveur.
*   **Si vous avez déjà un serveur web :** Créer un point de terminaison d'API sur votre serveur existant est un choix naturel.
*   **La sécurité est primordiale :** Priorisez toujours la sécurisation de votre jeton GitHub sur un serveur backend et ne l'exposez jamais dans votre code frontend.

**Étapes de Mise en Œuvre (en utilisant les Fonctions Sans Serveur comme Exemple) :**

1.  **Créez une Fonction Sans Serveur :** Écrivez le code pour votre fonction sans serveur (ex. : en Python ou Node.js) qui inclut la logique pour appeler l'API GitHub.
2.  **Stocker de Manière Sécurisée Votre Jeton GitHub :** Configurez une variable d'environnement dans les paramètres de votre plateforme sans serveur pour stocker votre jeton d'accès personnel GitHub.
3.  **Déployez Votre Fonction Sans Serveur :** Déployez la fonction sur la plateforme de votre choix (ex. : Netlify, Vercel, AWS Lambda avec API Gateway). Vous obtiendrez une URL pour votre fonction déployée.
4.  **Mettez à Jour Votre Code Frontend :** Modifiez votre fichier `nytimes.js` pour effectuer une requête `POST` vers l'URL de votre fonction sans serveur déployée lorsque le bouton est cliqué.
5.  **Testez :** Déployez votre frontend mis à jour et testez si le clic sur le bouton déclenche bien votre workflow GitHub Actions.

En mettant en œuvre l'une de ces solutions basées sur un backend, vous pouvez fournir un bouton pour déclencher votre workflow GitHub de manière sécurisée sans exposer votre jeton API sensible dans votre code frontend. Choisissez l'approche qui correspond le mieux à votre infrastructure actuelle et à vos compétences techniques.