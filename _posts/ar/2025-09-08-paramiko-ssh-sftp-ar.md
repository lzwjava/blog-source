---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-code-fast-1
title: دليل باراميكو لبروتوكولات SSH و SFTP
translated: true
type: note
---

### التثبيت
Paramiko هي مكتبة بايثون لبروتوكولات SSH وSFTP. يمكن تثبيتها عبر pip:

```bash
pip install paramiko
```

### الاستخدام الأساسي
تمكنك Paramiko من الاتصال بخوادم SSH، وتنفيذ الأوامر، ونقل الملفات. تعامل دائمًا مع المفاتيح الخاصة بأمان واستخدم كلمات مرور قوية—تدعم Paramiko المصادقة باستخدام المفاتيح وكلمات المرور.

المفاهيم الأساسية:
- **العميل (Client)**: استخدم `paramiko.SSHClient()` لإعداد الاتصال.
- **النقل (Transport)**: للتحكم على مستوى أدنى، استخدم `paramiko.Transport()`.
- قم بالمصادقة عبر `client.connect()` باستخدام اسم المضيف، واسم المستخدم، وإما كلمة المرور أو المفتاح (على سبيل المثال، عبر `paramiko.RSAKey.from_private_key_file()`).

### مثال: الاتصال وتنفيذ أمر
إليك نصًا برمجيًا كاملاً للاتصال بخادم SSH، وتنفيذ أمر، وطباعة الناتج. استبدل العناصر النائبة ببياناتك.

```python
import paramiko

# إنشاء عميل SSH
client = paramiko.SSHClient()

# إضافة مفتاح المضيف تلقائيًا (كن حذرًا في بيئة الإنتاج؛ قم بتحميل known_hosts بدلاً من ذلك)
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # الاتصال (استخدم كلمة المرور أو ملف المفتاح)
    client.connect(
        hostname='your.server.com',
        port=22,  # منفذ SSH الافتراضي
        username='your_username',
        password='your_password',  # أو key_filename='path/to/private_key.pem'
    )

    # تنفيذ أمر
    stdin, stdout, stderr = client.exec_command('echo "Hello from SSH!"')

    # قراءة الناتج
    output = stdout.read().decode('utf-8')
    error = stderr.read().decode('utf-8')

    print("Output:", output)
    print("Error:", error)

except paramiko.SSHException as e:
    print(f"SSH error: {e}")
finally:
    client.close()
```

### مثال متقدم: استخدام المصادقة المعتمدة على المفتاح ونقل الملفات
للمصادقة بالمفتاح، قم بتوليد زوج مفاتيح إذا لزم الأمر (مثل `ssh-keygen`)، أضف المفتاح العام إلى `~/.ssh/authorized_keys` على الخادم، ثم استخدم:

```python
import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # الاتصال باستخدام المفتاح
    client.connect(
        hostname='your.server.com',
        username='your_username',
        key_filename='~/.ssh/id_rsa',  # المسار إلى المفتاح الخاص
    )

    # تنفيذ أمر
    stdin, stdout, stderr = client.exec_command('ls -la')
    print(stdout.read().decode('utf-8'))

    # مثال SFTP: نقل ملف
    sftp = client.open_sftp()
    sftp.put('local_file.txt', 'remote_file.txt')  # رفع
    sftp.get('remote_file.txt', 'local_copy.txt')  # تنزيل
    sftp.close()

except Exception as e:
    print(f"Error: {e}")
finally:
    client.close()
```

### نصائح وأفضل الممارسات
- **الأمان**: فضّل المصادقة باستخدام المفاتيح على كلمات المرور. عطّل `AutoAddPolicy` في بيئة الإنتاج وتحقق من مفاتيح المضيف عبر `client.load_host_keys()`.
- **معالجة الأخطاء**: التقط دائمًا استثناء `paramiko.SSHException` وتحقق من رموز الخروج باستخدام `exit_status = stdout.channel.recv_exit_status()`.
- **الخيوط (Threads)**: مكتبة Paramiko ليست آمنة للاستخدام مع الخيوط بشكل افتراضي؛ استخدم الأقفال إذا لزم الأمر.
- **التوثيق**: للمزيد، راجع [وثائق Paramiko الرسمية](https://docs.paramiko.org/). اختبر باستخدام أدوات مثل `sshd` من OpenSSH أو الأجهزة الافتراضية المحلية.

هذا يجب أن يبدأك؛ قم بالتعديل حسب احتياجاتك!