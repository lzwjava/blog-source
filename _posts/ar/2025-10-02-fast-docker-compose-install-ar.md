---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast:free
title: طرق تثبيت Docker Compose السريعة
translated: true
type: note
---

### طرق بديلة سريعة لتنزيل/تثبيت Docker Compose على أوبونتو

بافتراض أنك تقصد الحصول بسرعة على ثنائية Docker Compose الأحدث (الإصدار v2.37.3 اعتبارًا من أكتوبر 2025، وفقًا للوثائق الرسمية) دون عناء زيارة صفحة الإصدار على GitHub بالكامل (مثل التحقق اليدوي باستخدام curl و sha256)، إليك بعض الخيارات الموثوقة والسريعة. تستفيد هذه الطرق من مدير حزم أوبونتو أو مستودعات Docker للحصول على تثبيت شبه فوري. سأركز على السرعة والبساطة — معظمها لا تستغرق أكثر من دقيقة واحدة.

#### 1. **عن طريق APT لأوبونتو (الأسرع لمعظم المستخدمين)**
   إذا كان Docker مثبتًا لديك (ويتضمن `docker-compose-plugin`)، ما عليك سوى استخدام الأمر الفرعي — لا حاجة لتنزيل منفصل. هذه هي الطريقة الحديثة والمدمجة وتجنبك إدارة الملفات الثنائية.

   - **التحقق مما إذا كان متوفرًا بالفعل**:
     ```
     docker compose version
     ```
     إذا أظهر الإصدار v2.x، فقد انتهيت — إنه الأحدث عبر تثبيت Docker الخاص بك.

   - **التثبيت/التحديث إذا لزم الأمر** (يضيف الإضافة إذا كانت مفقودة):
     ```
     sudo apt update
     sudo apt install docker-compose-plugin
     ```
     - **لماذا هي سريعة؟** لا تستخدم حركة مرور GitHub؛ تستخدم المستودعات المحلية. يتم التحديث تلقائيًا مع `apt upgrade`.
     - **طريقة الاستخدام**: شغلها كـ `docker compose up` (لاحظ المسافة، وليس شرطة).
     - **نصيحة للمحترفين**: إذا لم يكن Docker مثبتًا بعد، أضف مستودع Docker أولاً:
       ```
       sudo apt update
       sudo apt install ca-certificates curl
       sudo install -m 0755 -d /etc/apt/keyrings
       sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
       sudo chmod a+r /etc/apt/keyrings/docker.asc
       echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
       sudo apt update
       sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
       ```

#### 2. **أمر Curl من سطر واحد من GitHub (أسرع قليلاً من الإصدار الكامل)**
   تجاوز تصفح صفحة الإصدار — يحصل curl مباشرة على أحدث ثنائية لنظام Linux x86_64 ويثبتها. هذه الطريقة أسرع من الاختيار اليدوي للملفات ولكنها لا تزال تستخدم GitHub.

   ```
   VERSION=$(curl -s https://api.github.com/repos/docker/compose/releases/latest | grep 'tag_name' | cut -d\" -f4) && sudo curl -L "https://github.com/docker/compose/releases/download/${VERSION}/docker-compose-linux-x86_64" -o /usr/local/bin/docker-compose && sudo chmod +x /usr/local/bin/docker-compose && docker-compose --version
   ```
   - **لماذا هي سريعة؟** واجهة برمجة التطبيقات (API) تجلب رقم الإصدار في ثوانٍ؛ أمر واحد يتولى التنزيل والتثبيت.
   - **التحقق**: `--version` في النهاية تؤكد العملية.
   - **ملاحظة**: للإصدار v2.39.4 تحديدًا، استبدل `${VERSION}` بـ `v2.39.4`.

#### 3. **عن طريق Snap (مدير الحزم العالمي لأوبونتو)**
   Snap مثبت مسبقًا على أوبونتو 24.04 ويجلب أحدث إصدار فورًا من متجر Canonical.

   ```
   sudo snap install docker
   ```
   - **لماذا هي سريعة؟** لا حاجة لإعداد مستودع؛ التنزيل يتم بشكل متوازي والتحديث تلقائي. يتضمن إضافة Compose.
   - **طريقة الاستخدام**: نفس طريقة APT (`docker compose`).
   - **التحقق من الإصدار**: `docker compose version`.

#### 4. **عن طريق Pip (بما أن لديك Python 3.13.4)**
   إذا كنت تفضل الطريقة القائمة على Python (نمط الإصدار v1 القديم، ولكن pip يحتوي على أغلفة للإصدار v2)، فهو تثبيت سريع بدون تبعيات نظام.

   ```
   sudo pip3 install docker-compose
   ```
   - **لماذا هي سريعة؟** يقوم Pip بالتخزين المؤقت وحل التبعيات بسرعة؛ لا يتضمن استخدام GitHub.
   - **القيد**: هذه الطريقة أكثر ملاءمة لتوافق الإصدار v1 — استخدم APT للحصول على الإضافة الرسمية للإصدار v2.
   - **التحقق**: `docker-compose --version` (باستخدام شرطة).

هذه الطرق جميعها أسرع من واجهة مستخدم GitHub لأنها تقلل من النقرات أو تستخدم واجهات برمجة التطبيقات/ذاكرة التخزين المؤقت. APT أو Snap هما الخياران الموصى بهما بشدة لأوبونتو — حيث يتم دمجهما بسلاسة ويتوليان أمر التحديثات. إذا كنت تقصد شيئًا آخر بعبارة "docker compose down" (مثل الأمر نفسه)، فوضح ذلك!

[دليل التثبيت الرسمي لـ Docker Compose](https://docs.docker.com/compose/install/linux/)
[إصدارات Docker](https://github.com/docker/compose/releases)