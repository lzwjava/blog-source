---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: بروتون يتيح تشغيل ألعاب ويندوز على لينكس
translated: true
type: note
---

### ما هو Proton؟

Proton هو طبقة توافق طورتها Valve، مدمجة مباشرة في عميل Steam، تتيح للألعاب والتطبيقات المخصصة لنظام Windows فقط أن تعمل بسلاسة على الأنظمة القائمة على Linux (مثل SteamOS على جهاز Steam Deck أو توزيعات Linux القياسية). إنه في الأساس الحل المدمج في Steam لـ "Linux عبر Proton"، مما يسمح للمستخدمين بتشغيل مكتبة ضخمة من ألعاب الكمبيوتر دون الحاجة إلى تثبيت Windows أو إعداد نظام مزدوج التشغيل.

#### كيف يعمل؟
- **التقنية الأساسية**: تم بناء Proton على أساس Wine (طبقة توافق مجانية تترجم استدعاءات Windows API إلى نظيراتها في Linux) ولكنه معزز بتعديلات محددة من Valve، بما في ذلك ترجمة DirectX إلى Vulkan عبر DXVK و VKD3D. هذا يجعله أكثر كفاءة للألعاب.
- **التكامل مع Steam**: في Steam، يمكنك ببساطة النقر بزر الماوس الأيمن على لعبة، والذهاب إلى Properties > Compatibility، وتمكين "Force the use of a specific Steam Play compatibility tool" (اختيار إصدار Proton). يتولى Steam الباقي — تنزيل Proton إذا لزم الأمر وتشغيل اللعبة كما لو كانت أصلية على Linux.
- **الإصدارات**: يأتي Proton بإصدارات تجريبية ومستقرة. اعتبارًا من عام 2025، أحدث إصدار مستقر (مثل Proton 9.x أو أعلى) يدعم آلاف العناوين بتقييمات "Platinum" أو "Gold" على ProtonDB (قاعدة بيانات مجتمعية لتقارير التوافق).

#### فوائده لألعاب Linux
- **سهولة الاستخدام**: لا حاجة للتكوين اليدوي لمعظم الألعاب — فهو "شغّل وابدأ اللعب" داخل Steam.
- **الأداء**: غالبًا ما يطابق أو يتجاوز أداء Windows الأصلي على Linux بسبب التحسينات، خاصة على أجهزة مثل وحدات معالجة الرسومات من AMD. يمكنه حتى تشغيل بعض الألعاب بشكل أفضل على الأجهزة المحمولة التي تعمل بنظام Linux مقارنة بإعدادات Windows المماثلة.
- **تأثير النظام البيئي**: جعل Proton من Linux منصة قابلة للتطبيق للألعاب، حيث يشغل أجهزة مثل Steam Deck ويساهم في اعتماد أوسع للتكنولوجيا مفتوحة المصدر في مجال الألعاب.

إذا كنت تقوم بإعداده، تأكد من أن توزيعة Linux الخاصة بك تحتوي على برامج تشغيل Vulkan المثبتة (على سبيل المثال، عبر Mesa لـ AMD/Intel). لاستكشاف الأخطاء وإصلاحها، تحقق من ProtonDB للحصول على نصائح محددة لكل لعبة.

#### المراجع
- [Valve's Proton GitHub Repository](https://github.com/ValveSoftware/Proton)
- [Steam Community Guide: Proton 101](https://steamcommunity.com/app/221410/discussions/0/1636417404917541481/)
- [Rocky Linux Docs: Gaming on Linux with Proton](https://docs.rockylinux.org/10/desktop/gaming/proton/)