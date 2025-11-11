---
audio: false
generated: true
lang: hi
layout: post
title: अपने गिटहब वर्कफ़्लो को ट्रिगर करें
translated: true
type: note
---

आप सही हैं, अपने frontend कोड में सीधे GitHub token embed करना एक सुरक्षा जोखिम है। आपके पेज के सोर्स कोड को देखने वाला कोई भी व्यक्ति संभावित रूप से आपके token तक पहुंच सकता है और उसका दुरुपयोग कर सकता है।

यहां कुछ सुरक्षित तरीके दिए गए हैं जिन्हें आप अपने GitHub workflow को frontend बटन से ट्रिगर करने के लिए अपना सकते हैं, साथ ही स्पष्टीकरण और कोड उदाहरण भी दिए गए हैं:

**मुख्य विचार: एक सुरक्षित Backend शामिल करें**

इसे संभालने का सबसे सुरक्षित तरीका एक backend component (एक API endpoint) शामिल करना है जो:

1.  **आपके frontend से ट्रिगर अनुरोध प्राप्त करेगा।**
2.  **आपके GitHub token को सुरक्षित रूप से संग्रहीत करेगा और उपयोग करेगा।**
3.  **आपके workflow को dispatch करने के लिए GitHub को प्रमाणित API कॉल करेगा।**

इस तरह, आपका संवेदनशील GitHub token आपके server-side environment को कभी नहीं छोड़ता।

यहां आपके backend के लिए कुछ विकल्प दिए गए हैं:

**1. Serverless Functions (जैसे, AWS Lambda, Google Cloud Functions, Netlify Functions, Vercel Functions)**

यह अक्सर इस तरह के सरल API endpoints के लिए एक हल्का और लागत-प्रभावी समाधान होता है।

*   **यह कैसे काम करता है:** आप एक छोटा सा function लिखते हैं जो एक serverless प्लेटफॉर्म पर deploy हो जाता है। इस function में आपके stored token का उपयोग करके GitHub API को कॉल करने का logic शामिल होगा। आपका frontend बटन तब इस serverless function के URL पर एक HTTP अनुरोध करेगा।

*   **उदाहरण (संकल्पनात्मक - आपको इसे अपने चुने हुए प्लेटफॉर्म के अनुकूल बनाना होगा):**

    **Serverless Function कोड (Python - AWS Lambda/API Gateway के लिए उदाहरण):**

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

    *   **महत्वपूर्ण:** आप अपने serverless प्लेटफॉर्म में एक environment variable (जैसे, `GITHUB_TOKEN`) configure करेंगे ताकि आपका GitHub Personal Access Token सुरक्षित रूप से store हो सके।

    **Frontend कोड (संशोधित `nytimes.js`):**

    ```javascript
    const nytimesDiv = document.querySelector('.nytimes');
    const backendApiUrl = '/.netlify/functions/trigger-nytimes-update'; // Netlify Functions के लिए उदाहरण

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
                body: JSON.stringify({}) // एक साधारण ट्रिगर के लिए आपको body की आवश्यकता नहीं हो सकती है
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

*   **Deployment:** आपको इस serverless function को अपने चुने हुए प्लेटफॉर्म पर deploy करना होगा। विशिष्ट deployment प्रक्रिया provider के आधार पर अलग-अलग होती है।

**2. आपका अपना Web Server (यदि आपके पास है)**

यदि आपके पास अपना खुद का web server है (जैसे, Node.js, Python/Flask, आदि का उपयोग करके), तो आप उस server पर एक सरल API endpoint बना सकते हैं।

*   **यह कैसे काम करता है:** आपका frontend बटन आपके server के endpoint पर एक अनुरोध भेजता है। आपका server-side कोड, जिसकी पहुंच आपके GitHub token तक है (जो एक environment variable के रूप में या configuration फ़ाइल में सुरक्षित रूप से stored है), तब GitHub को API कॉल करता है।

*   **उदाहरण (संकल्पनात्मक - Node.js with Express):**

    **Server-side कोड (Node.js/Express):**

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

    *   **महत्वपूर्ण:** अपना `GITHUB_TOKEN` store करने के लिए एक `.env` फ़ाइल का उपयोग करें (और सुनिश्चित करें कि यह आपके repository में commit न हो) और इसे `dotenv` जैसी लाइब्रेरी का उपयोग करके एक्सेस करें।

    **Frontend कोड (संशोधित `nytimes.js`):**

    ```javascript
    const nytimesDiv = document.querySelector('.nytimes');
    const backendApiUrl = '/api/trigger-nytimes-update'; // अपने server के endpoint के अनुसार समायोजित करें

    // ... (frontend कोड का बाकी हिस्सा serverless function उदाहरण के समान है)
    ```

*   **Deployment:** आपको अपने server application को अपने web server पर deploy करना होगा।

**3. एक अलग Event द्वारा ट्रिगर किया गया GitHub Actions Workflow (कम प्रत्यक्ष)**

हालांकि यह एक सीधा बटन ट्रिगर नहीं है, आप अपने workflow को ट्रिगर करने के लिए एक अलग event सेट कर सकते हैं, जो एक user action द्वारा अप्रत्यक्ष रूप से शुरू किया जा सकता है। उदाहरण के लिए:

*   **Scheduled Workflow:** समय-समय पर update workflow चलाएं (जैसे, दैनिक)।
*   **Webhook Trigger:** यदि आपके पास कोई अन्य सिस्टम या सेवा है जिसके साथ users interact करते हैं, तो वह सिस्टम एक webhook ट्रिगर कर सकता है जो तब आपके GitHub Actions workflow को शुरू करता है।

हालांकि, ये विकल्प बटन क्लिक से तुरंत, on-demand update प्रदान नहीं करते हैं जिसकी आपको संभवतः आवश्यकता है।

**सही दृष्टिकोण चुनना**

*   **सरल static sites के लिए:** Serverless functions अक्सर सबसे आसान और लागत-प्रभावी समाधान होते हैं। Netlify और Vercel जैसे प्लेटफॉर्म में serverless functions के लिए अंतर्निहित समर्थन है।
*   **यदि आपके पास पहले से ही एक web server है:** अपने मौजूदा server पर एक API endpoint बनाना एक स्वाभाविक विकल्प है।
*   **सुरक्षा सर्वोच्च है:** हमेशा अपने GitHub token को backend server पर सुरक्षित रखने को प्राथमिकता दें और इसे कभी भी अपने frontend कोड में एक्सपोज़ न करें।

**कार्यान्वयन के चरण (Serverless Functions का उदाहरण का उपयोग करके):**

1.  **एक Serverless Function बनाएँ:** अपने serverless function के लिए कोड लिखें (जैसे, Python या Node.js में) जिसमें GitHub API को कॉल करने का logic शामिल हो।
2.  **अपने GitHub Token को सुरक्षित रूप से Store करें:** अपने GitHub Personal Access Token को store करने के लिए अपने serverless प्लेटफॉर्म की सेटिंग्स में एक environment variable configure करें।
3.  **अपने Serverless Function को Deploy करें:** Function को अपने चुने हुए प्लेटफॉर्म (जैसे, Netlify, Vercel, AWS Lambda with API Gateway) पर deploy करें। आपको अपने deployed function के लिए एक URL प्राप्त होगा।
4.  **अपने Frontend कोड को अपडेट करें:** अपनी `nytimes.js` फ़ाइल को संशोधित करें ताकि बटन क्लिक होने पर आपके deployed serverless function के URL पर एक `POST` अनुरोध किया जा सके।
5.  **परीक्षण करें:** अपने अपडेट किए गए frontend को deploy करें और परीक्षण करें कि क्या बटन क्लिक करने से आपका GitHub Actions workflow सफलतापूर्वक ट्रिगर होता है।

इन backend-आधारित समाधानों में से किसी एक को लागू करके, आप अपने संवेदनशील API token को अपने frontend कोड में एक्सपोज़ किए बिना, अपने GitHub workflow को सुरक्षित रूप से ट्रिगर करने के लिए एक बटन प्रदान कर सकते हैं। उस दृष्टिकोण को चुनना याद रखें जो आपके मौजूदा infrastructure और तकनीकी कौशल के अनुकूल हो।