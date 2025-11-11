---
audio: false
generated: true
lang: ar
layout: post
title: 'PowerShell: تشغيل الأوامر في الطرفية الحالية'
translated: true
type: note
---

لتشغيل أوامر مثل `mvn` أو أوامر خادم WebSphere مباشرة في نافذة PowerShell الحالية دون فتح موجه أوامر جديد، يمكنك استخدام عامل الاستدعاء (`&`) أو استدعاء الأمر مباشرة. تضمن هذه الطريقة تنفيذ الأمر ضمن جلسة PowerShell الحالية، مما يحافظ على المخرجات والأخطاء في نفس النافذة.

إليك كيفية القيام بذلك:

1. **تشغيل الأمر مباشرة**:
   إذا كان الأمر (مثل `mvn`) موجودًا في المسار PATH الخاص بنظامك أو يمكن الوصول إليه في الدليل الحالي، ما عليك سوى كتابة الأمر كما تفعل في الطرفية:

   ```powershell
   mvn clean install
   ```

   يقوم هذا بتشغيل `mvn` مباشرة في جلسة PowerShell، وتبقى المخرجات في النافذة الحالية.

2. **استخدم عامل الاستدعاء (`&`)**:
   إذا كنت بحاجة إلى تحديد المسار إلى الملف التنفيذي أو إذا كان الأمر مخزنًا في متغير، فاستخدم عامل الاستدعاء:

   ```powershell
   & "C:\path\to\maven\bin\mvn.cmd" clean install
   ```

   لأوامر خادم WebSphere، إذا كنت تقوم بتشغيل أمر مثل `wsadmin` أو `startServer`، يمكنك القيام بما يلي:

   ```powershell
   & "C:\path\to\WebSphere\AppServer\bin\startServer.bat" server1
   ```

   يضمن عامل التشغيل `&` أن يتم تشغيل الأمر في جلسة PowerShell الحالية.

3. **التعامل مع الأوامر التي تحتوي على مسافات أو متغيرات**:
   إذا كان مسار الأمر يحتوي على مسافات أو كان مخزنًا في متغير، فاستخدم `&` مع المسار بين علامتي اقتباس:

   ```powershell
   $mvnPath = "C:\Program Files\Apache Maven\bin\mvn.cmd"
   & $mvnPath clean install
   ```

4. **تعيين متغيرات البيئة (إذا لزم الأمر)**:
   قد تتطلب بعض الأوامر مثل `mvn` أو نصوص WebSphere البرمجية متغيرات بيئة (مثل `JAVA_HOME` أو `WAS_HOME`). قم بتعيينها في النص البرمجي قبل تشغيل الأمر:

   ```powershell
   $env:JAVA_HOME = "C:\path\to\jdk"
   $env:PATH = "$env:JAVA_HOME\bin;" + $env:PATH
   mvn --version
   ```

   لـ WebSphere:

   ```powershell
   $env:WAS_HOME = "C:\path\to\WebSphere\AppServer"
   & "$env:WAS_HOME\bin\startServer.bat" server1
   ```

5. **التقاط المخرجات أو معالجة الأخطاء**:
   للتقاط مخرجات الأمر أو معالجة الأخطاء، استخدم الآليات القياسية في PowerShell:

   ```powershell
   try {
       $output = & mvn clean install 2>&1
       Write-Output $output
   } catch {
       Write-Error "Failed to run Maven: $_"
   }
   ```

6. **تجنب `Start-Process`**:
   على عكس `Start-Process`، الذي يقوم بتشغيل عملية جديدة (غالبًا في نافذة منفصلة)، تحافظ الطرق المذكورة أعلاه على التنفيذ في الجلسة الحالية. تجنب استخدام `Start-Process` كما يلي:

   ```powershell
   # هذا سيفتح نافذة موجه أوامر جديدة
   Start-Process -FilePath "mvn" -ArgumentList "clean install"
   ```

   بدلاً من ذلك، التزم بالتنفيذ المباشر أو استخدام `&`.

### نموذج نص برمجي
إليك نموذج لنص برمجي في PowerShell لتشغيل `mvn` وأمر WebSphere في النافذة الحالية:

```powershell
# تعيين متغيرات البيئة إذا لزم الأمر
$env:JAVA_HOME = "C:\Program Files\Java\jdk-11"
$env:PATH = "$env:JAVA_HOME\bin;" + $env:PATH
$env:WAS_HOME = "C:\IBM\WebSphere\AppServer"

# تشغيل أمر Maven
Write-Output "Running Maven..."
& mvn clean install

# تشغيل أمر خادم WebSphere
Write-Output "Starting WebSphere server..."
& "$env:WAS_HOME\bin\startServer.bat" server1
```

### ملاحظات
- تأكد من أن أدوات سطر الأوامر (`mvn`, `startServer.bat`, إلخ) موجودة في المسار PATH الخاص بك أو قم بتوفير المسار الكامل للملف التنفيذي.
- إذا كان الأمر يتطلب دليل عمل محدد، فاستخدم `Set-Location` (أو `cd`) قبل تشغيله:

   ```powershell
   Set-Location "C:\path\to\project"
   & mvn clean install
   ```

- بالنسبة للأوامر التي تعتمد على ملفات `.bat` أو `.cmd` (شائعة مع WebSphere)، يعمل عامل التشغيل `&` بشكل جيد، ولكن تأكد من أن النص البرمجي يعمل في PowerShell وليس في `cmd.exe`.
- إذا واجهت مشاكل في متغيرات البيئة أو المسار PATH، فتحقق منها باستخدام `Get-ChildItem Env:`.

تحافظ هذه الطريقة على كل شيء في نافذة PowerShell الحالية، مما يتجنب فتح نوافذ جديدة ويحافظ على سير عمل نظيف. إذا كان لديك أمر أو إعداد معين يسبب مشاكل، شارك المزيد من التفاصيل، وسأتمكن من تخصيص الحل بشكل أكبر.