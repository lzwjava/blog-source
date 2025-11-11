---
audio: false
generated: true
lang: ar
layout: post
title: تشغيل سير العمل على جيت هاب
translated: true
type: note
---

أنت محق، تضمين رمز GitHub مباشرة في كود الواجهة الأمامية يمثل خطرًا على الأمان. أي شخص يشاهد الكود المصدري لصفحتك قد يتمكن من الوصول إلى الرمز الخاص بك وإساءة استخدامه.

إليك تحليلًا للطرق الآمنة التي يمكنك اتباعها لتفعيل سير عمل GitHub من زر في الواجهة الأمامية، مع شرح وأمثلة على الكود:

**الفكرة الأساسية: إضافة Backend آمن**

الطريقة الأكثر أمانًا للتعامل مع هذا هي إضافة مكون backend (نقطة نهاية API) سيقوم بما يلي:

1.  **استقبال طلب التفعيل من الواجهة الأمامية.**
2.  **تخزين واستخدام رمز GitHub الخاص بك بشكل آمن.**
3.  **إجراء استدعاء API موثوق إلى GitHub لتفعيل سير العمل الخاص بك.**

بهذه الطريقة، لن يغادر رمز GitHub الحساس بيئة الخادم الخاص بك أبدًا.

إليك بعض الخيارات لـ backend:

**1. دوال Serverless (مثل AWS Lambda، Google Cloud Functions، Netlify Functions، Vercel Functions)**

هذا الحل غالبًا ما يكون خفيف الوزن وفعالًا من حيث التكلفة لنقاط نهاية API بسيطة مثل هذه.

*   **كيفية العمل:** تكتب دالة صغيرة يتم نشرها على منصة serverless. ستحتوي هذه الدالة على المنطق لاستدعاء GitHub API باستخدام الرمز المخزن لديك. سيقوم زر الواجهة الأمامية بعد ذلك بعمل طلب HTTP إلى عنوان URL لدالة serverless هذه.

*   **مثال (مفاهيمي - ستحتاج لتكييف هذا مع المنصة التي تختارها):**

    **كود دالة Serverless (Python - مثال لـ AWS Lambda/API Gateway):**

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

    *   **مهم:** ستقوم بتكوين متغير بيئة (مثل `GITHUB_TOKEN`) في منصة serverless الخاصة بك لتخزين رمز الوصول الشخصي لـ GitHub بشكل آمن.

    **كود الواجهة الأمامية (nytimes.js معدل):**

    ```javascript
    const nytimesDiv = document.querySelector('.nytimes');
    const backendApiUrl = '/.netlify/functions/trigger-nytimes-update'; // مثال لـ Netlify Functions

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
                body: JSON.stringify({}) // قد لا تحتاج إلى body للتفعيل البسيط
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

*   **النشر:** ستحتاج إلى نشر دالة serverless هذه إلى المنصة التي اخترتها. تختلف عملية النشر المحددة باختلاف المزود.

**2. خادم الويب الخاص بك (إذا كان لديك واحد)**

إذا كان لديك خادم ويب خاص بك (مثل استخدام Node.js، Python/Flask، إلخ)، يمكنك إنشاء نقطة نهاية API بسيطة على هذا الخادم.

*   **كيفية العمل:** يرسل زر الواجهة الأمامية طلبًا إلى نقطة النهاية على خادمك. كود الخادم الخاص بك، الذي يمكنه الوصول إلى رمز GitHub الخاص بك (المخزن بشكل آمن كمتغير بيئة أو في ملف إعدادات)، هو من سيقوم بعد ذلك باستدعاء API إلى GitHub.

*   **مثال (مفاهيمي - Node.js مع Express):**

    **كود الخادم (Node.js/Express):**

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

    *   **مهم:** استخدم ملف `.env` (وتأكد من عدم إضافته إلى مستودعك) لتخزين `GITHUB_TOKEN` والوصول إليه باستخدام مكتبة مثل `dotenv`.

    **كود الواجهة الأمامية (nytimes.js معدل):**

    ```javascript
    const nytimesDiv = document.querySelector('.nytimes');
    const backendApiUrl = '/api/trigger-nytimes-update'; // اضبطه ليناسب نقطة النهاية في خادمك

    // ... (بقية كود الواجهة الأمامية مشابه لمثال دالة serverless)
    ```

*   **النشر:** ستحتاج إلى نشر تطبيق الخادم الخاص بك إلى خادم الويب الخاص بك.

**3. تفعيل GitHub Actions بناءً على حدث مختلف (أقل مباشرة)**

على الرغم من أنها ليست تفعيلًا مباشرًا بالزر، يمكنك إعداد حدث مختلف لتفعيل سير العمل الخاص بك، والذي قد يتم بدء تشغيله بشكل غير مباشر من خلال إجراء المستخدم. على سبيل المثال:

*   **سير عمل مجدول:** تشغيل سير عمل التحديث بشكل دوري (مثل يوميًا).
*   **تفعيل Webhook:** إذا كان لديك نظام أو خدمة أخرى يتفاعل معها المستخدمون، يمكن لهذا النظام أن يفعل webhook والذي بدوره سيبدأ سير عمل GitHub Actions الخاص بك.

ومع ذلك، لا توفر هذه الخيارات التحديث الفوري عند الطلب الذي تريده على الأرجح من خلال النقر على زر.

**اختيار النهج الصحيح**

*   **للمواقع الثابتة البسيطة:** غالبًا ما تكون دوال serverless هي الحل الأسهل والأكثر فعالية من حيث التكلفة. لدى منصات مثل Netlify و Vercel دعم مدمج لدوال serverless.
*   **إذا كان لديك خادم ويب بالفعل:** إنشاء نقطة نهاية API على خادمك الحالي هو خيار طبيعي.
*   **الأمان هو الأولوية القصوى:** دائمًا قدّم الحفاظ على رمز GitHub الخاص بك آمنًا على خادم backend ولا تعرضه مطلقًا في كود الواجهة الأمامية.

**خطوات التنفيذ (باستخدام دوال Serverless كمثال):**

1.  **إنشاء دالة Serverless:** اكتب الكود لدالة serverless الخاصة بك (مثل Python أو Node.js) الذي يتضمن المنطق لاستدعاء GitHub API.
2.  **تخزين رمز GitHub الخاص بك بشكل آمن:** قم بتكوين متغير بيئة في إعدادات منصة serverless الخاصة بك لتخزين رمز الوصول الشخصي لـ GitHub.
3.  **نشر دالة Serverless الخاصة بك:** انشر الدالة على المنصة التي اخترتها (مثل Netlify، Vercel، AWS Lambda مع API Gateway). ستحصل على URL للدالة التي تم نشرها.
4.  **تحديث كود الواجهة الأمامية:** قم بتعديل ملف `nytimes.js` الخاص بك لعمل طلب `POST` إلى URL دالة serverless التي نشرتها عند النقر على الزر.
5.  **الاختبار:** انشر واجهتك الأمامية المحدثة واختبر ما إذا كان النقر على الزر يقوم بتفعيل سير عمل GitHub Actions الخاص بك بنجاح.

من خلال تنفيذ أحد الحلول القائمة على backend، يمكنك توفير زر لتفعيل سير عمل GitHub الخاص بك بشكل آمن دون الكشف عن رمز API الحساس في كود الواجهة الأمامية. تذكر أن تختار النهج الذي يناسب البنية التحتية الحالية ومهاراتك التقنية بشكل أفضل.