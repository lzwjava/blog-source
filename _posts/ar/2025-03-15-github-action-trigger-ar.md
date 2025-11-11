---
audio: false
generated: true
lang: ar
layout: post
title: تشغيل إجراءات جيت هاب
translated: true
type: note
---

نعم، يمكن لـ GitHub Action تشغيل GitHub Action آخر، وإن لم يكن بشكل مباشر. عادةً ما يتم تشغيل سير عمل GitHub Actions بواسطة أحداث محددة مثل عمليات الدفع (push) أو طلبات السحب (pull requests) أو الجداول الزمنية، ولكن هناك عدة طرق غير مباشرة لجعل سير عمل واحد يؤدي إلى تشغيل آخر. فيما يلي الطرق الرئيسية لتحقيق ذلك:

---

### 1. استخدام حدث `workflow_dispatch`
يمكنك تشغيل سير عمل برمجيًا باستخدام حدث `workflow_dispatch` عبر GitHub API. هذا يسمح لسير العمل الأول ببدء تشغيل سير عمل آخر تم تكوينه للاستماع إلى هذا الحدث.

- **الكيفية**: يقوم سير العمل الأول بإجراء استدعاء API لتشغيل سير العمل الثاني.
- **مثال**:
  ```yaml
  name: Trigger Another Workflow
  on: [push]
  jobs:
    trigger:
      runs-on: ubuntu-latest
      steps:
        - name: Trigger Workflow
          run: |
            curl -X POST \
              -H "Authorization: token ${{ secrets.GITHUB_TOKEN }}" \
              -H "Accept: application/vnd.github.v3+json" \
              https://api.github.com/repos/<owner>/<repo>/actions/workflows/<workflow_id>/dispatches \
              -d '{"ref": "main"}'
  ```
  استبدل `<owner>`, `<repo>`, و `<workflow_id>` بتفاصيل مستودعك ومعرف سير العمل المستهدف. يجب أن يتضمن سير العمل الثاني `on: [workflow_dispatch]` في تكوينه.

---

### 2. استخدام أحداث Repository Dispatch
يمكن لسير العمل إرسال حدث مخصص باستخدام repository dispatch، يمكن لسير عمل آخر الاستماع إليه والتشغيل بناءً عليه.

- **الكيفية**: يرسل سير العمل الأول حدث repository dispatch عبر GitHub API، ويستجيب سير العمل الثاني لذلك الحدث.
- **مثال**:
  - سير العمل الأول (يرسل الحدث):
    ```yaml
    name: Send Dispatch Event
    on: [push]
    jobs:
      send-dispatch:
        runs-on: ubuntu-latest
        steps:
          - name: Send Dispatch
            run: |
              curl -X POST \
                -H "Authorization: token ${{ secrets.GITHUB_TOKEN }}" \
                -H "Accept: application/vnd.github.v3+json" \
                https://api.github.com/repos/<owner>/<repo>/dispatches \
                -d '{"event_type": "custom_event"}'
    ```
  - سير العمل الثاني (يتم تشغيله بواسطة الحدث):
    ```yaml
    name: Triggered by Dispatch
    on:
      repository_dispatch:
        types: [custom_event]
    jobs:
      respond:
        runs-on: ubuntu-latest
        steps:
          - name: Respond to Event
            run: echo "Triggered by custom_event"
    ```

---

### 3. التشغيل عبر أحداث Git
يمكن لسير عمل واحد أن يشغل آخر من خلال توليد حدث Git، مثل إنشاء commit أو فتح طلب سحب (pull request)، والذي يتم تكوين سير العمل الثاني للاستجابة له.

- **الكيفية**: يقوم سير العمل الأول بتعديل المستودع (على سبيل المثال، عن طريق دفع commit)، مما يؤدي إلى تشغيل سير عمل آخر تم تكوينه لهذا الحدث (مثل `on: [push]`).
- **مثال**:
  ```yaml
  name: Create Commit
  on: [push]
  jobs:
    create-commit:
      runs-on: ubuntu-latest
      steps:
        - name: Checkout
          uses: actions/checkout@v2
        - name: Create File
          run: echo "New file" > newfile.txt
        - name: Commit and Push
          run: |
            git config user.name "GitHub Action"
            git config user.email "action@github.com"
            git add newfile.txt
            git commit -m "Add new file"
            git push
  ```
  يمكن أن يؤدي هذا إلى تشغيل سير عمل آخر مضبوط للتشغيل على أحداث `push`.

---

### اعتبارات رئيسية
- **الأذونات**: يجب أن يكون رمز GitHub المستخدم في استدعاءات API لديه أذونات كافية لتشغيل سير العمل أو إرسال أحداث dispatch.
- **حدود المعدل**: كن على علم بحدود معدل GitHub's API، خاصة لسير العمل الذي يعمل بشكل متكرر.
- **تجنب الحلقات**: امنع الحلقات اللانهائية عن طريق إضافة شروط لإيقاف سير العمل عن تشغيل بعضها البعض بشكل لا نهائي.
- **التكوين**: تأكد من إعداد سير العمل المستهدف بشكل صحيح للاستماع للحدث المقصود.

---

### خاتمة
بينما لا تقدم GitHub Action آلية مباشرة لاستدعاء سير عمل لآخر، يمكنك تحقيق هذا بشكل غير مباشر باستخدام `workflow_dispatch`، أو أحداث repository dispatch، أو أحداث Git مثل commits أو pull requests. تسمح لك هذه الطرق بربط أو تشغيل سير العمل بشكل فعال بناءً على احتياجاتك.