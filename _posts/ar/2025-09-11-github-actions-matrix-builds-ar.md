---
audio: false
generated: true
image: false
lang: ar
layout: post
model: openai/gpt-5
title: دليل المصفوفات للبناء في GitHub Actions
translated: true
type: note
---

يبدو أنك تسأل عن استخدام **GitHub Actions** matrix builds لتشغيل الاختبارات بالتوازي، وكيفية استخدام خيار `fail-fast` في استراتيجية المصفوفة. دعني أوضح ذلك لك.

---

### المصفوفات في GitHub Actions
تتيح لك **استراتيجية المصفوفة** تشغيل نفس المهمة بالتوازي مع معلمات مختلفة—على سبيل المثال، الاختبار عبر إصدارات متعددة من Python أو Node، أو على أنظمة تشغيل مختلفة.

مثال بسيط:

```yaml
name: CI

on:
  push:
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.8, 3.9, 3.10]
        os: [ubuntu-latest, windows-latest]
      fail-fast: false
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: pytest
```

---

### النقاط الرئيسية

- **`matrix`:** تُعرّف المتغيرات لإنشاء مجموعات المهام.  
  المثال أعلاه يشغل الاختبارات لجميع مجموعات (`python-version`, `os`).

- **التنفيذ المتوازي:** كل مهمة تم إنشاؤها بواسطة المصفوفة تعمل **بالتوازي** بشكل افتراضي.

- **`fail-fast`:**
  - القيمة الافتراضية هي `true`. هذا يعني أنه إذا فشلت مهمة واحدة، يتم إلغاء بقية مهام المصفوفة.
  - عيّن `fail-fast: false` إذا كنت تريد أن تستمر جميع مهام المصفوفة في العمل، حتى إذا فشلت واحدة.

  مثال:
  ```yaml
  strategy:
    matrix:
      node: [14, 16, 18]
    fail-fast: false
  ```

- **تقييد إجمالي المهام:** يمكنك استبعاد بعض المجموعات:
  ```yaml
  strategy:
    matrix:
      python-version: [3.8, 3.9, 3.10]
      os: [ubuntu-latest, windows-latest]
    exclude:
      - python-version: 3.8
        os: windows-latest
  ```

---

### تشغيل الاختبارات بالتوازي
- كل **مهمة في المصفوفة تعمل بالتوازي** على مُشغّل خاص بها، لذا لا تحتاج إلى فعل أي شيء خاص.
- داخل كل مهمة، إذا كنت تريد **تنفيذ اختبارات متوازي** (مثل `-n auto` في pytest)، يمكنك إضافة ذلك على مستوى أمر الاختبار.

مثال:
```yaml
- name: Run pytest in parallel
  run: pytest -n auto
```

---

✅ **الخلاصة:**
- استخدم `strategy.matrix` لتعريف مجموعات المعلمات المختلفة.
- عيّن `fail-fast: false` إذا كنت تريد أن تعمل جميع مهام المصفوفة حتى إذا فشلت واحدة.
- مهام المصفوفة تعمل بالتوازي تلقائيًا.
- لوقت تشغيل أسرع داخل كل مهمة، استخدم توازي أطر الاختبار (مثل pytest-xdist).

---

هل تريد مني أن أريك مثالًا حقيقيًا **لتشغيل اختبارات Node/JavaScript** باستخدام المصفوفة (إصدارات متعددة من Node، `fail-fast: false`، اختبارات موازية باستخدام `npm test`)؟