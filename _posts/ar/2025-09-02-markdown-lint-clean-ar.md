---
audio: false
generated: true
image: false
lang: ar
layout: post
title: تدقيق ماركداون لملفات متسقة ونظيفة
translated: true
type: note
---

إليك مقدمة واضحة وسهلة القراءة لمشروع **markdownlint** بقلم ديفيد أنسون:

---

## ما هو **markdownlint**؟

**markdownlint** هو أداة للتحليل الثابت لملفات Markdown/CommonMark، مبنية على Node.js. هدفه الأساسي هو فرض قواعد الاتساق والأسلوب عبر محتوى Markdown — مما يساعد الكتّاب على الحفاظ على تنسيق نظيف وموحد وتجنب التركيبات التي قد تتلف أو تُعرض بشكل غير متسق عبر المحللات المختلفة ([GitHub][1]).

مستوحى من أداة markdownlint القائمة على Ruby (markdownlint/mdl)، تتبنى هذه الأداة مكتبة غنية من قواعد الفحص. تستفيد من محلل micromark لدعم CommonMark وتوسعه بميزات GitHub Flavored Markdown (GFM) مثل الجداول، والروابط التلقائية، والتوجيهات، والحواشي السفلية، والرياضيات ([GitHub][1]).

## الميزات الرئيسية والتكاملات

*   **تغطية القواعد**: تقدم مجموعة شاملة من القواعد المدمجة — تتراوح من أنماط العناوين ومسافة البادئ في القوائم إلى المسافات الزائدة في نهاية السطر وطول السطر (مثل MD001، MD009، MD013…) ([GitHub][1]).
*   **التوافق مع النظام البيئي**:

    *   **أدوات سطر الأوامر**:

        *   `markdownlint-cli` – واجهة سطر أوامر تقليدية.
        *   `markdownlint-cli2` – واجهة سطر أوامر أسرع قائمة على التكوين مع خيارات تنسيق مرنة ودعم للنماذق (globs)، وتنسيقات الإخراج، والإصلاح التلقائي، والتكامل مع سير عمل التكامل المستمر ([GitHub][2], [GitHub][3]).
    *   **امتداد VS Code**:

        *   `vscode‑markdownlint` يجلب الفحص في الوقت الفعلي إلى محررك. يتم تحديد المخالفات مضمنة (بتسطيرها)، مع تلميحات أدوات قابلة للظهور عند التمرير واقتراحات الإصلاح السريع ([GitHub][4]).
    *   **إجراء GitHub**:

        *   `markdownlint‑cli2‑action` يتيح لك تضمين markdownlint في خط أنابيب التكامل المستمر الخاص بك، مما يتيح إجراء فحوصات تلقائية (وإصلاح تلقائي اختياري) أثناء سير عمل GitHub ([GitHub][5]).

---

## لماذا تستخدمه؟

*   **الاتساق**: يضمن التزام ملفات Markdown بدليل نمط محدد، مما يقلل من انحراف التنسيق عبر المشروع.
*   **المساعدة في المحرر**: الملاحظات المضمنة في VS Code والتكاملات الأخرى تجعل الكتابة أكثر نظافة وسرعة.
*   **الأتمتة**: استخدمه في خطوط أنابيب التكامل المستمر مع أدوات الفحص أو إجراءات GitHub لفرض المعايير قبل عمليات الدمج.
*   **قابل للتخصيص**: يمكنك تخصيص مجموعات القواعد أو حتى تعطيل القواعد عبر ملفات التكوين أو التعليقات المضمنة (مثل تعطيل MD013 للأسطر الطويلة) ([GitHub][5], [Software Recommendations Stack Exchange][6]).

---

هل تريد دليل بدء سريع لإعداده باستخدام npm، أو استخدام امتداد VS Code، أو دمجه في سير عمل التكامل المستمر؟

[1]: https://github.com/DavidAnson/markdownlint?utm_source=chatgpt.com "DavidAnson/markdownlint: A Node.js style checker and lint ..."
[2]: https://github.com/markdownlint/markdownlint?utm_source=chatgpt.com "Markdown lint tool"
[3]: https://github.com/DavidAnson/markdownlint-cli2?utm_source=chatgpt.com "DavidAnson/markdownlint-cli2"
[4]: https://github.com/DavidAnson/vscode-markdownlint?utm_source=chatgpt.com "DavidAnson/vscode-markdownlint: Markdown linting and ..."
[5]: https://github.com/DavidAnson/markdownlint-cli2-action?utm_source=chatgpt.com "DavidAnson/markdownlint-cli2-action"
[6]: https://softwarerecs.stackexchange.com/questions/7138/markdown-lint-tool?utm_source=chatgpt.com "validation - Markdown lint tool"