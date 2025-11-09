---
audio: false
generated: true
image: false
lang: ar
layout: post
model: mistralai/mistral-medium-3.1
title: أدوات الرسم البياني خارج نطاق Graphviz وNetworkX
translated: true
type: note
---

بدائل رائعة تتجاوز Graphviz و NetworkX، مصنفة حسب طريقة العمل التي تفضلها.

**النص/لغة المجال الخاصة "مخططات ككود"**
- PlantUML: UML كامل (التسلسل، الفئات، المكونات، النشر)، نموذج C4، الأنشطة؛ نظام بيئي ضخم.
- Mermaid: بناء جملة خفيف يشبه Markdown؛ رائع للمخططات الانسيابية، والتسلسلية، والفئات، والكيان والعلاقة، والحالة؛ يتم عرضه بشكل أصلي على GitHub/GitLab.
- D2 (من Terrastruct): لغة مجال عامة وأنيقة مع تخطيط تلقائي جيد؛ تدعم الطبقات والمخططات الكبيرة.
- Structurizr (C4): النمذجة أولاً (C4) مع لغة مجال؛ يصدر إلى PlantUML/Mermaid؛ جيد لوثائق الهندسة المعمارية.
- C4-PlantUML: قوالب نموذج C4 مبنية على PlantUML.
- nomnoml: بناء جملة بسيط، رسومات سريعة للفئات والعلاقات.
- Kroki: خادم يعرض العديد من لغات المجال (PlantUML, Mermaid, Graphviz) لأنابيب الوثائق.

**الكود أولاً (إنشاء مخططات من الكود/البنية التحتية ككود)**
- diagrams (mingrammer, Python): مخططات هندسة السحابة البرمجية (AWS/Azure/GCP/K8s).
- مساعدو Terraform: Inframap (الرسم من الحالة)، Blast Radius (رسوم بيانية تفاعلية من Terraform).
- AWS CDK: cdk-dia لمخططات الهندسة المعمارية من تطبيقات CDK.
- مكتبات Go/TS: GoDiagrams (Go)، ts-graphviz (TypeScript) للإنشاء القائم على الكود.

**مكتبات التصور على الويب (رسوم بيانية تفاعلية)**
- Cytoscape.js: تصور الرسوم البيانية الكبيرة، خوارزميات التخطيط، أداء جيد.
- D3.js: قوية ولكنها منخفضة المستوى للرسوم البيانية والمخططات البصرية المخصصة.
- vis-network (vis.js): رسوم بيانية للشبكات سهلة مع المحاكاة الفيزيائية.
- Sigma.js: عرض سريع للرسوم البيانية الكبيرة.
- ECharts: مخططات عامة مع وحدة الرسم البياني؛ نتائج سريعة.
- pyvis (بايثون): رسوم بيانية شبكية تفاعلية بسيطة عبر Vis.js.

**أدوات الرسم البياني بواجهة المستخدم الرسومية (السحب والإفلات)**
- diagrams.net (draw.io): مجاني، سهل، استنسل كبير (UML، أيقونات السحابة).
- yEd/yFiles: تخطيط تلقائي رائع؛ yFiles هو إطار تطوير برمجيات تجاري، و yEd مجاني لسطح المكتب.
- Lucidchart/Miro: أدوات ويب تعاونية؛ جيدة للفرق.
- OmniGraffle (macOS), Visual Paradigm, StarUML, Enterprise Architect: أدوات UML/الهندسة المعمارية.

**أدوات خاصة بالهندسة المعمارية والمجال**
- نموذج C4: Structurizr, C4-PlantUML, إضافات Mermaid C4.
- سحابة الهندسة المعمارية كخدمة: Cloudcraft (AWS), Hava, Lucidscale, CloudSkew; الاستيراد من السحابة/البنية التحتية ككود.
- BPMN/العمليات: Camunda Modeler, bpmn.io.
- التسلسل/التوقيت: WebSequenceDiagrams, WaveDrom (مخططات التوقيت).
- مخططات الكيان والعلاقة/قواعد البيانات: dbdiagram.io, SchemaSpy.

**اختيارات سريعة حسب السيناريو**
- الوثائق ككود في Markdown/ملفات README: Mermaid.
- UML كامل + C4 مع القوالب: PlantUML أو Structurizr.
- هندسة السحابة من الكود/البنية التحتية ككود: diagrams (بايثون)، Inframap/Blast Radius (Terraform)، cdk-dia (AWS CDK).
- رسوم بيانية تفاعلية لتطبيقات الويب: Cytoscape.js أو vis-network؛ للتصور المخصص، D3.js.
- الرسم السريع بواجهة المستخدم الرسومية: diagrams.net (draw.io)؛ للتخطيط التلقائي، yEd.

إذا شاركت تفضيلاتك (نص مقابل واجهة مستخدم رسومية، صور ثابتة مقابل تفاعلية، اللغات التي تستخدمها، وأنواع المخططات مثل التسلسل/C4/السحابة/الكيان والعلاقة)، يمكنني أن أوصي بقائمة مختصرة وقوالب بداية.