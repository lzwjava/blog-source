---
audio: false
generated: true
image: false
lang: ar
layout: post
model: openai/gpt-5
title: إصلاح أخطاء المصادقة في عمليات الدفع على جيت هاب
translated: true
type: note
---

يشير رمز الخطأ 403 إلى أن عملية الدفع تتم المصادقة عليها باسم **`lzwjava` بدون رمز وصول يمتلك صلاحيات الكتابة** (غالبًا لأن المهمة لا تزال تستخدم `GITHUB_TOKEN` الافتراضي، والذي لا يمكنه الدفع إلى مستودع آخر). يمكنك إصلاح ذلك عن طريق **حقن بيانات اعتماد حقيقية لعملية الاستخراج/الدفع إلى الوجهة**.

إليك ثلاث طرق فعّالة — اختر واحدة منها. سأعرض عليك أسرعها أولاً.

---

### الخيار أ — استخدام PAT ودمجه في الـ Remote (الأسرع)

1. أنشئ **PAT كلاسيكي** مع نطاق `repo` (أو PAT محدَد الصلاحيات مع **Contents: Read & Write** للمستودع `lzwjava/lzwjava.github.io`). احفظه في المستودع المصدر كـ `DEPLOY_TOKEN`.

2. حدّث خطوة النشر في سير العمل الخاص بك **لإجبار الـ Remote على استخدام ذلك الرمز**:

```yaml
- name: Check out destination repo
  uses: actions/checkout@v4
  with:
    repository: lzwjava/lzwjava.github.io
    token: ${{ secrets.DEPLOY_TOKEN }}
    path: destination
    fetch-depth: 0

- name: Push built site to destination
  run: |
    rsync -av --delete _site/ destination/
    cd destination
    touch .nojekyll

    git config user.name  "github-actions[bot]"
    git config user.email "github-actions[bot]@users.noreply.github.com"

    # إجبار الـ Remote على استخدام PAT بشكل صريح (يتجنب تعارضات مساعد بيانات الاعتماد)
    git remote set-url origin https://${{ secrets.DEPLOY_TOKEN }}@github.com/lzwjava/lzwjava.github.io.git

    if [ -n "$(git status --porcelain)" ]; then
      git add -A
      git commit -m "deploy: ${GITHUB_SHA}"
      git push origin HEAD:main
    else
      echo "No changes to deploy."
    fi
```

إذا لا يزال يظهر لك خطأ 403، فربما ينقص رمز PAT النطاقات المطلوبة أو (إذا كان المستودع تابعًا لمنظمة) يحتاج إلى تفويض SSO. أنشئه مرة أخرى مع نطاق `repo` وجرّب مرة أخرى.

---

### الخيار ب — تجنب تسرب بيانات الاعتماد: تعطيل بيانات الاعتماد الافتراضية في عملية الاستخراج الأولى

أحيانًا تقوم **عملية الاستخراج الأولى** بكتابة `GITHUB_TOKEN` الافتراضي في مساعد بيانات الاعتماد ويتم إعادة استخدامه لاحقًا. يمكنك تعطيل ذلك:

```yaml
- name: Check out source repo
  uses: actions/checkout@v4
  with:
    fetch-depth: 0
    persist-credentials: false   # <- مهم
```

ثم استمر في عملية استخراج المستودع الوجهة باستخدام PAT الخاص بك كما هو موضح في الخيار أ (يمكنك تخطي سطر `remote set-url` إذا كانت الأمور تعمل بالفعل، ولكن وجوده لا يضر).

---

### الخيار ج — مفتاح نشر SSH (قوي جدًا)

1. على جهازك: `ssh-keygen -t ed25519 -C "deploy@actions" -f deploy_key`
2. أضف **المفتاح العام** (`deploy_key.pub`) كـ **مفتاح نشر** في `lzwjava/lzwjava.github.io` مع **صلاحية الكتابة**.
3. أضف **المفتاح الخاص** (`deploy_key`) كسر `ACTIONS_DEPLOY_KEY` في المستودع **المصدر**.

سير العمل:

```yaml
- name: Check out destination repo via SSH
  uses: actions/checkout@v4
  with:
    repository: lzwjava/lzwjava.github.io
    ssh-key: ${{ secrets.ACTIONS_DEPLOY_KEY }}
    path: destination
    fetch-depth: 0

- name: Push built site (SSH)
  run: |
    rsync -av --delete _site/ destination/
    cd destination
    touch .nojekyll
    git config user.name  "github-actions[bot]"
    git config user.email "github-actions[bot]@users.noreply.github.com"
    if [ -n "$(git status --porcelain)" ]; then
      git add -A
      git commit -m "deploy: ${GITHUB_SHA}"
      git push origin HEAD:main
    else
      echo "No changes to deploy."
    fi
```

---

### تشخيص سريع إذا فشلت مرة أخرى

شغّل هذه الأوامر مباشرة قبل عملية الدفع لترى بيانات المصادقة المكونة فعليًا:

```bash
cd destination
git remote -v
git config --get user.name
git config --get user.email
git config --get url.https://github.com/.insteadof || true
git config --global --list | sed -n 's/^credential\.helper.*/&/p'
```

إذا أظهر `remote -v` عنوان `https://github.com/...` عادي **بدون** حقن PAT الخاص بك (الخيار أ) أو `git@github.com:` (الخيار ج)، فأنت لا تزال تستخدم بيانات الاعتماد الخاطئة.

---

### الأخطاء الشائعة

*   يجب أن يمنح **PAT محدَد الصلاحيات** صلاحية **Contents: Read & Write** **لذلك المستودع المحدد** بشكل صريح.
*   قد تمنع **حماية الفرع** على `main` عمليات الدفع من البوتات (فحوصات مطلوبة/توقيعات). إذا حدث ذلك، انشر إلى فرع غير محمي (مثل `gh-pages`) أو عدّل القواعد.
*   **انتهت صلاحية PAT** → أنشئه مرة أخرى.
*   **SSO الخاص بالمنظمة** (لا ينطبق على حالتك إذا كان المستودع تابعًا لمستخدم) → فوّض PAT للمنظمة.

طبق أحد الخيارات الثلاثة المذكورة أعلاه وسيختفي خطأ 403.