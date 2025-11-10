---
audio: false
generated: true
lang: ar
layout: post
title: مراحل التغيير في خطاف ما قبل الإيداع
translated: true
type: note
---

لدمج التغييرات من سكريبت `update_notes_link.py` في الـ commit الحالي (بدلاً من إنشاء commit منفصل) أثناء تشغيل خطاف pre-commit، ستحتاج إلى تعديل الخطاف لإضافة الملفات المحدثة إلى منطقة التجهيز (staging) دون عمل commit منفصل لها. بهذه الطريقة، سيتم تضمين التغييرات من سكريبت Python في commit المستخدم. أدناه، سأقدم سكريبت خطاف pre-commit معدلاً يحقق هذا.

### التغييرات الرئيسية
- **لا يوجد Commit منفصل**: بدلاً من تشغيل `git commit` في الخطاف، سيقوم السكريبت فقط بإضافة الملفات المحدثة إلى منطقة التجهيز (`git add`) بحيث تُضمن في commit المستخدم.
- **الحفاظ على رسالة Commit المستخدم**: لن ينشئ الخطاف commit جديداً، مما يضمن استخدام رسالة commit الأصلية الخاصة بالمستخدم.
- **معالجة الأخطاء**: إذا فشل سكريبت Python، سينهي الخطاف التنفيذ برمز حالة غير صفري (non-zero status) لمنع إجراء commit.

### سكريبت خطاف Pre-Commit

إليك سكريبت خطاف pre-commit المحدث والذي يجهز التغييرات دون إنشاء commit منفصل:

```x-shellscript
#!/bin/bash

# تشغيل سكريبت update_notes_link.py وحفظ الناتج
OUTPUT=$(python scripts/generate/update_notes_link.py 2>&1)
EXIT_CODE=$?

# التحقق من تنفيذ سكريبت Python بنجاح
if [ $EXIT_CODE -ne 0 ]; then
    echo "خطأ: فشل update_notes_link.py برمز خروج $EXIT_CODE"
    echo "$OUTPUT"
    exit 1
fi

# التحقق مما إذا كان الملف المحدد قد تم تحديثه
if echo "$OUTPUT" | grep -q "Updated original/2025-01-11-notes-en.md"; then
    echo "تم تحديث روابط الملاحظات، تجهيز التغييرات للـ commit الحالي."

    # إضافة الملفات ذات الصلة إلى منطقة التجهيز
    git add original/2025-01-11-notes-en.md
    git add _posts/en/*.md

    # التحقق من أنه تمت إضافة الملفات إلى منطقة التجهيز
    if ! git diff --cached --quiet; then
        echo "تم تجهيز التغييرات بنجاح."
    else
        echo "لا توجد تغييرات لتجهيزها."
    fi
else
    echo "لا توجد تحديثات لـ original/2025-01-11-notes-en.md، لم يتم تجهيز أي ملفات إضافية."
fi

# إنهاء التشغيل بنجاح للسماح لـ commit بالمتابعة
exit 0
```

### شرح السكريبت

-   **Shebang (`#!/bin/bash`)**: يضمن تشغيل السكريبت في بيئة Bash.
-   **تشغيل سكريبت Python**: ينفذ `python scripts/generate/update_notes_link.py` ويحفظ ناتجه ورمز خروجه.
-   **معالجة الأخطاء**: يتحقق من رمز الخروج (`$EXIT_CODE`) لسكريبت Python. إذا كان غير صفري، يفشل الخطاف، يطبع الخطأ، ويمنع commit.
-   **فحص الناتج**: يستخدم `grep` للتحقق مما إذا كان الناتج يشير إلى تحديث `original/2025-01-11-notes-en.md`.
-   **تجهيز الملفات**: يشغل `git add` على الملفات المحددة (`original/2025-01-11-notes-en.md` و `_posts/en/*.md`) لتضمينها في commit المستخدم.
-   **لا يوجد Commit**: يتخطى `git commit`، مما يسمح لأمر `git commit` الخاص بالمستخدم بتضمين التغييرات المجهزة مع رسالة commit الأصلية.
-   **التغذية الراجعة**: يطبع رسائل لإعلام المستخدم بما إذا تم تجهيز التغييرات.
-   **رمز الخروج**: ينهي التشغيل بـ `0` للسماح لـ commit بالمتابعة، ما لم يفشل سكريبت Python.

### إعداد الخطاف

1.  **إنشاء الخطاف**:
    -   ضع السكريبت في `.git/hooks/pre-commit` في مستودعك.
2.  **جعله قابلاً للتنفيذ**:
    ```bash
    chmod +x .git/hooks/pre-commit
    ```
3.  **اختبار الخطاف**:
    -   عدل ملفاً أو تأكد من أن سكريبت Python سيحدث `original/2025-01-11-notes-en.md`.
    -   شغل `git commit -m "رسالة الـ commit الخاصة بك"`.
    -   تحقق من تضمين الملفات المحدثة في الـ commit عن طريق فحص `git diff --cached` قبل الـ commit أو `git show` بعده.

### استخدام إطار عمل `pre-commit` (اختياري)

إذا كنت تفضل استخدام إطار عمل `pre-commit`، يمكنك تعريف نفس المنطق في ملف `.pre-commit-config.yaml`. هذه الطريقة أكثر قابلية للنقل وتسمح لك بتحديد أي الملفات تشغل الخطاف.

1.  **تثبيت pre-commit**:
    ```bash
    pip install pre-commit
    ```
2.  **إنشاء `.pre-commit-config.yaml`**:

```yaml
repos:
- repo: local
  hooks:
  - id: update-notes-links
    name: Update Notes Links
    entry: bash -c '
      OUTPUT=$(python scripts/generate/update_notes_link.py 2>&1);
      EXIT_CODE=$?;
      if [ $EXIT_CODE -ne 0 ]; then
        echo "Error: update_notes_link.py failed with exit code $EXIT_CODE";
        echo "$OUTPUT";
        exit 1;
      fi;
      if echo "$OUTPUT" | grep -q "Updated original/2025-01-11-notes-en.md"; then
        echo "Notes links updated, staging changes for the current commit.";
        git add original/2025-01-11-notes-en.md;
        git add _posts/en/*.md;
        if ! git diff --cached --quiet; then
          echo "Changes staged successfully.";
        else
          echo "No changes to stage.";
        fi;
      else
        echo "No updates to original/2025-01-11-notes-en.md, no additional files staged.";
      fi'
    language: script
    files: ^(original/2025-01-11-notes-en\.md|_posts/en/.*\.md)$
    stages: [commit]
```

3.  **تثبيت الخطاف**:
    ```bash
    pre-commit install
    ```
4.  **اختبار الخطاف**:
    -   قم بعمل commit للتغييرات على الملفات التي تطابق regex الخاص بـ `files` (مثل `original/2025-01-11-notes-en.md` أو `_posts/en/*.md`).
    -   تحقق من أن الخطاف يعمل، ويجهز التغييرات إذا كان ذلك مناسباً، ويضمنها في commit الخاص بك.

### الاختلافات الرئيسية عن إجراءات GitHub الأصلية

-   **لا يوجد Commit منفصل**: على عكس سير عمل GitHub Actions، الذي كان ينشئ commit جديداً، هذا الخطاف يجهز التغييرات لـ commit المستخدم الحالي.
-   **لا يوجد Push**: الخطاف لا يدفع (push) التغييرات، لأن خطافات pre-commit تعمل محلياً قبل إنهاء commit. يجب على المستخدم تشغيل `git push` يدوياً.
-   **معالجة الأخطاء**: يتحقق الخطاف من رمز خروج سكريبت Python لضمان عدم فشله بصمت.
-   **لا يوجد تكوين Git للمستخدم**: يحذف السكريبت `git config user.name` و `user.email` لأن تكوين Git الخاص بالمستخدم سيُستخدم في الـ commit.

### ملاحظات

-   **سكريبت Python**: تأكد من وجود `scripts/generate/update_notes_link.py` وأنه قابل للتنفيذ محلياً. إذا كان يعتمد على متغيرات بيئة أو تبعيات، تأكد من توفرها.
-   **مسارات الملفات**: تحقق من تطابق المسارات `original/2025-01-11-notes-en.md` و `_posts/en/*.md` مع هيكل مستودعك.
-   **فشل الخطاف**: إذا فشل سكريبت Python، سيمنع الخطاف الـ commit، مما يضمن عدم تجهيز تحديثات جزئية.
-   **الاختبار**: اختبر باستخدام `git commit` للتأكد من تجهيز التغييرات وتضمينها في الـ commit دون إنشاء commit إضافي. استخدم `git show` لفحص محتويات الـ commit.

### التحقق

للتحقق:
1.  قم بتعديل ملف أو تأكد من أن سكريبت Python يقوم بتحديث `original/2025-01-11-notes-en.md`.
2.  شغل `git commit -m "رسالة اختبار"`.
3.  تحقق من `git show` لتأكيد تضمين الملفات المحدثة في الـ commit مع رسالتك الأصلية.
4.  تأكد من عدم إنشاء أي commits إضافية (مثل commit `chore(notes): Update notes links`).

إذا كنت بحاجة إلى تعديلات إضافية، مثل معالجة حالات أخطاء محددة أو إضافة المزيد من الملفات لتجهيزها، فأعلمني!