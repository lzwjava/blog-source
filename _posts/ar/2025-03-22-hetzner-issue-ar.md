---
audio: false
generated: true
lang: ar
layout: post
title: مشكلة واجهة برمجة تطبيقات هيتزنر
translated: true
type: note
---

دعنا نحلل الخطأ الذي تواجهه ونشرح ما يحدث في الكود الخاص بك:

### الخطأ:
```
Error creating snapshot for server sg5: cannot perform operation because server is locked (locked, f21b9dc9d1535310)
```

هذا الخطأ يأتي من واجهة برمجة تطبيقات Hetzner Cloud (عبر `hcloud` Python SDK) ويشير إلى أن عملية إنشاء لقطة للخادم المسمى `sg5` فشلت لأن الخادم **مقفل**. الخادم المقفل يعني أن هناك عملية أخرى (مثل لقطة سابقة، إعادة تشغيل، أو تغيير الحجم) قيد التنفيذ حاليًا، وأن الخادم مؤقتًا محظور عليه قبول عمليات جديدة حتى تكتمل تلك العملية.

### تفصيل الكود:
إليك السكريبت الخاص بك مع الشروحات ومصدر الخطأ:

```python
from hcloud import Client
import os

# الحصول على رمز واجهة برمجة التطبيقات من متغير البيئة
api_token = os.environ.get('HERTZNER_API_KEY')

if not api_token:
    print("Error: HERTZNER_API_KEY environment variable not set.")
    exit(1)

# إنشاء مثيل للعميل
client = Client(token=api_token)

def create_snapshot(server):
    try:
        response = client.servers.create_image(server, description=f"{server.name}-snapshot", type="snapshot")
        print(f"Snapshot created for server {server.name} with ID: {response.image.id}")
    except Exception as e:
        print(f"Error creating snapshot for server {server.name}: {e}")

# سرد جميع الخوادم
servers = client.servers.get_all()

# طباعة تفاصيل الخادم وإنشاء اللقطات
for server in servers:
    print(f"Server ID: {server.id}")
    print(f"Server Name: {server.name}")
    print(f"Server Status: {server.status}")
    print(f"Server IPv4: {server.public_net.ipv4.ip}")
    print(f"Server IPv6: {server.public_net.ipv6.ip}")
    print(f"Server Type: {server.server_type.name}")
    print(f"Server Location: {server.datacenter.location.name}")
    print("----------------------------------")
    create_snapshot(server)
```

1. **إعداد رمز واجهة برمجة التطبيقات**:
   - يسترجع السكريبت مفتاح واجهة برمجة تطبيقات Hetzner من متغير البيئة (`HERTZNER_API_KEY`). إذا لم يكن مضبوطًا، فإنه يخرج بخطأ.

2. **تهيئة العميل**:
   - يتم إنشاء مثيل `Client` باستخدام رمز واجهة برمجة التطبيقات للتفاعل مع واجهة برمجة تطبيقات Hetzner Cloud.

3. **دالة `create_snapshot`**:
   - تحاول هذه الدالة إنشاء لقطة لخادم معين باستخدام `client.servers.create_image()`.
   - المعاملات:
     - `server`: كائن الخادم المراد أخذ لقطة له.
     - `description`: اسم للقطة (مثال: `sg5-snapshot`).
     - `type="snapshot"`: يحدد أن نوع الصورة هو لقطة (على عكس النسخ الاحتياطي أو ISO).
   - إذا نجحت، تطبع معرف اللقطة؛ وإلا تلتقط وتبيع أي استثناءات (مثل الذي تراه).

4. **سرد الخوادم**:
   - `client.servers.get_all()` تسترجع قائمة بجميع الخوادم المرتبطة بحسابك في Hetzner.
   - يقوم السكريبت بالتكرار خلالهم، وطباعة تفاصيلهم (المعرف، الاسم، الحالة، عناوين IP، إلخ)، واستدعاء `create_snapshot()` لكل واحد.

5. **أين يحدث الخطأ**:
   - داخل دالة `create_snapshot()`، فشل استدعاء `client.servers.create_image()` للخادم `sg5` لأنه مقفل. رسالة الاستثناء (`cannot perform operation because server is locked`) يتم إثارتها من قبل مكتبة `hcloud` بناءً على استجابة واجهة برمجة التطبيقات.

### لماذا الخادم مقفل؟
يصبح الخادم مقفلاً عندما تكون هناك عملية قيد التنفيذ بالفعل. الأسباب الشائعة تشمل:
- يتم إنشاء لقطة أخرى.
- يتم إعادة تشغيل الخادم، أو تغيير حجمه، أو إعادة بنائه.
- عملية سابقة لم تكتمل بعد.

معرف القفل (`f21b9dc9d1535310`) في رسالة الخطأ هو معرف فريد للإجراء الجاري الذي يقفل الخادم.

### كيفية إصلاحه:
إليك الخطوات لحل المشكلة وتحسين السكريبت الخاص بك:

#### 1. **التحقق من حالة القفل قبل المتابعة**
قم بتعديل السكريبت لتخطي إنشاء اللقطة إذا كان الخادم مقفلاً. يمكنك التحقق من الإجراءات الحالية للخادم باستخدام `client.actions.get_all()` أو الانتظار حتى يزول القفل.

دالة `create_snapshot` المحدثة:
```python
def create_snapshot(server):
    try:
        # التحقق مما إذا كان الخادم مقفلاً من خلال النظر إلى إجراءاته
        actions = client.actions.get_all(server=server)
        for action in actions:
            if action.status == "running":
                print(f"Skipping snapshot for {server.name}: Server is locked by action {action.id}")
                return
        # إذا لم تكن هناك إجراءات قيد التشغيل، تابع مع اللقطة
        response = client.servers.create_image(server, description=f"{server.name}-snapshot", type="snapshot")
        print(f"Snapshot created for server {server.name} with ID: {response.image.id}")
    except Exception as e:
        print(f"Error creating snapshot for server {server.name}: {e}")
```

#### 2. **الانتظار حتى يزول القفل**
إذا كنت تريد الانتظار بدلاً من التخطي، يمكنك استقصاء إجراءات الخادم حتى يزول القفل:
```python
import time

def wait_for_unlock(server):
    while True:
        actions = client.actions.get_all(server=server)
        running = any(action.status == "running" for action in actions)
        if not running:
            break
        print(f"Waiting for server {server.name} to unlock...")
        time.sleep(5)  # الانتظار 5 ثوان قبل التحقق مرة أخرى

def create_snapshot(server):
    try:
        wait_for_unlock(server)
        response = client.servers.create_image(server, description=f"{server.name}-snapshot", type="snapshot")
        print(f"Snapshot created for server {server.name} with ID: {response.image.id}")
    except Exception as e:
        print(f"Error creating snapshot for server {server.name}: {e}")
```

#### 3. **التحقق من القفل يدويًا**
- استخدم Hetzner Cloud Console أو واجهة برمجة التطبيقات للتحقق من حالة الإجراء بالمعرف `f21b9dc9d1535310`.
- مثال لاستدعاء واجهة برمجة التطبيقات (عبر Python):
  ```python
  action = client.actions.get_by_id("f21b9dc9d1535310")
  print(f"Action Status: {action.status}, Command: {action.command}")
  ```
- إذا كانت عالقة، قد تحتاج إلى الاتصال بدعم Hetzner.

#### 4. **تشغيل السكريبت مرة أخرى**
بمجرد أن يصبح الخادم غير مقفل (تكتمل الإجراءات أو تقوم بحلها يدويًا)، أعد تشغيل السكريبت.

### ملاحظات إضافية:
- **حدود المعدل**: إنشاء لقطات للعديد من الخوادم في حلقة قد يصطدم بحدود معدل واجهة برمجة تطبيقات Hetzner. أضف تأخيرًا (مثال: `time.sleep(1)`) بين الطلبات إذا لزم الأمر.
- **معالجة الأخطاء**: السكريبت الحالي يتوقف عند أول خطأ. إذا كنت تريد أن يستمر للخوادم الأخرى، تأكد من أن الاستثناء لا يوقف الحلقة (وهو ليس كذلك في حالتك، وهذا جيد).

دعني أعلم إذا كنت بحاجة إلى مساعدة في تنفيذ أي من هذه الإصلاحات أو التصحيح الإضافي!