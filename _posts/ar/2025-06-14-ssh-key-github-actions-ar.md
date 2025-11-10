---
audio: false
generated: true
lang: ar
layout: post
title: إعداد مفتاح SSH لنشر جرة جيت هاب أكشنز
translated: true
type: note
---

لإنشاء مفتاح SSH لاستخدامه في GitHub Actions لنشر ملف JAR، اتبع الخطوات التالية:

1.  **إنشاء زوج مفاتيح SSH**:
    - على جهازك المحلي أو في بيئة آمنة، نفّذ الأمر:
      ```bash
      ssh-keygen -t ed25519 -C "your_email@example.com" -f github-actions-deploy
      ```
    - إذا كان نظامك لا يدعم Ed25519، استخدم:
      ```bash
      ssh-keygen -t rsa -b 4096 -C "your_email@example.com" -f github-actions-deploy
      ```
    - اضغط على Enter لقبول الموقع الافتراضي للملف وقم بتعيين كلمة مرور اختيارية (موصى بها للأمان). سينشئ هذا ملفين:
      - `github-actions-deploy` (المفتاح الخاص)
      - `github-actions-deploy.pub` (المفتاح العام)

2.  **إضافة المفتاح العام إلى الخادم المستهدف**:
    - انسخ المفتاح العام:
      ```bash
      cat github-actions-deploy.pub
      ```
    - سجّل الدخول إلى الخادم حيث تريد نشر ملف JAR.
    - ألحق المفتاح العام إلى الملف `~/.ssh/authorized_keys` على الخادم:
      ```bash
      echo "your-public-key-content" >> ~/.ssh/authorized_keys
      ```
    - تأكد من أن ملف `authorized_keys` لديه الصلاحيات الصحيحة:
      ```bash
      chmod 600 ~/.ssh/authorized_keys
      ```

3.  **تخزين المفتاح الخاص في GitHub Secrets**:
    - اذهب إلى مستودع GitHub الخاص بك: `Settings > Secrets and variables > Actions > Secrets`.
    - انقر على **New repository secret**.
    - سمّى الـ Secret (على سبيل المثال، `SSH_PRIVATE_KEY`).
    - الصق محتويات المفتاح الخاص (`github-actions-deploy`):
      ```bash
      cat github-actions-deploy
      ```
    - احفظ الـ Secret.

4.  **تكوين سير العمل (Workflow) في GitHub Actions**:
    - أنشئ أو حرر ملف سير العمل (مثل `.github/workflows/deploy.yml`).
    - أضف خطوة لاستخدام مفتاح SSH لنشر ملف JAR. فيما يلي مثال على سير العمل:

      ```yaml
      name: Deploy JAR

      on:
        push:
          branches:
            - main

      jobs:
        deploy:
          runs-on: ubuntu-latest

          steps:
          - name: Checkout code
            uses: actions/checkout@v4

          - name: Set up Java
            uses: actions/setup-java@v4
            with:
              java-version: '17' # اضبطه ليطابق إصدار Java الخاص بك
              distribution: 'temurin'

          - name: Build JAR
            run: mvn clean package # اضبطه لأداة البناء الخاصة بك (مثل Gradle)

          - name: Install SSH Key
            uses: shimataro/ssh-key-action@v2
            with:
              key: ${{ secrets.SSH_PRIVATE_KEY }}
              known_hosts: 'optional-known-hosts' # انظر الملاحظة أدناه

          - name: Add Known Hosts
            run: |
              ssh-keyscan -H <server-ip-or-hostname> >> ~/.ssh/known_hosts
            # استبدل <server-ip-or-hostname> مع IP الخادم أو اسم المضيف الخاص به

          - name: Deploy JAR to Server
            run: |
              scp target/your-app.jar user@<server-ip-or-hostname>:/path/to/deploy/
              ssh user@<server-ip-or-hostname> "sudo systemctl restart your-service" # اضبطه ليطابق عملية النشر الخاصة بك
      ```

    - **ملاحظات**:
      - استبدل `target/your-app.jar` بالمسار إلى ملف JAR الخاص بك.
      - استبدل `user@<server-ip-or-hostname>` بمستخدم SSH وعنوان الخادم الخاص بك.
      - اضبط أمر النشر (مثل `sudo systemctl restart your-service`) ليطابق كيفية تشغيل أو نشر ملف JAR على خادمك.
      - خطوة `known_hosts` حرجة لتجنب مشاكل التحقق من هوية مضيف SSH. إذا كنت تعرف مفتاح مضيف الخادم، يمكنك إضافته مسبقًا في خطوة `shimataro/ssh-key-action`، أو استخدام `ssh-keyscan` كما هو موضح.

5.  **تأمين سير العمل**:
    - تأكد من أن المفتاح الخاص لا يتم عرضه مطلقًا في السجلات أو المخرجات.
    - قيّد صلاحيات المستودع لمنع الوصول غير المصرح به إلى الأسرار (Secrets).
    - إذا كنت تستخدم كلمة مرور للمفتاح SSH، أضفها كـ Secret آخر وضمّنها في خطوة `shimataro/ssh-key-action`:
      ```yaml
      with:
        key: ${{ secrets.SSH_PRIVATE_KEY }}
        passphrase: ${{ secrets.SSH_KEY_PASSPHRASE }}
        known_hosts: 'optional-known-hosts'
      ```

6.  **اختبار سير العمل**:
    - ادفع تغييرًا إلى فرع `main` (أو الفرع المحدد في سير العمل).
    - راقب سير العمل في علامة التبويب **Actions** في مستودع GitHub الخاص بك للتأكد من أن ملف JAR يتم بناؤه ونشره بشكل صحيح.

7.  **استكشاف الأخطاء وإصلاحها**:
    - **Permission denied**: تحقق من إضافة مفتاح SSH بشكل صحيح إلى `authorized_keys` على الخادم وأن للمستخدم صلاحية الوصول إلى المجلد المستهدف.
    - **Host verification failed**: تأكد من تكوين خطوة `known_hosts` بشكل صحيح مع IP الخادم أو اسم المضيف.
    - **Build issues**: تأكد من أن إصدار Java وأوامر البناء تطابق إعداد مشروعك.

هذا الإعداد يدمج النشر باستخدام SSH بأمان في سير عمل GitHub Actions لنشر ملف JAR. إذا كنت بحاجة إلى تعديلات محددة (مثل إعداد خادم معين أو أداة بناء)، دعني أعلم!