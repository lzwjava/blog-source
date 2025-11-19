---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: جدولة GitHub Actions تستخدم توقيت UTC
translated: true
type: note
---

**تفسر مهام GitHub Actions المجدولة (باستخدام مشغل `on: schedule:` مع بناء cron) أوقات cron دائمًا بالتوقيت العالمي المنسق (UTC).**

لا يوجد دعم مدمج لتحديد منطقة زمنية مختلفة مباشرة في YAML لسير العمل. إذا كنت تريد تشغيل مهمة في وقت محلي معين (على سبيل المثال، الساعة 9:00 صباحًا بتوقيت المحيط الهادئ PST)، فيجب عليك تحويل ذلك إلى الوقت المكافئ في UTC وكتابة تعبير cron وفقًا لذلك.

### النقاط الرئيسية من الوثائق الرسمية:
- تستخدم مهام العمل المجدولة بناء cron الخاص بـ POSIX وتعمل في **أوقات UTC** المحددة.
- مثال: `cron: '0 5 * * *'` يعمل يوميًا في الساعة 5:00 صباحًا UTC (وليس بتوقيتك المحلي).

كان هذا الأمر ثابتًا لسنوات ولا يزال الحال كذلك حتى أواخر عام 2025 — لا توجد معلمة منطقة زمنية أصلية لحدث `schedule` (على عكس بعض ميزات GitHub الأخرى مثل Dependabot).

[الأحداث التي تُطلق مهام العمل - وثائق GitHub](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#schedule)  
[بناء جملة سير العمل لـ GitHub Actions - وثائق GitHub](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#on-schedule)