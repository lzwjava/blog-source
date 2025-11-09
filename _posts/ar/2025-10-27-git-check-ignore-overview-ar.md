---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: نظرة عامة على أمر Git Check-Ignore
translated: true
type: note
---

### ما هو `git check-ignore`؟

أمر `git check-ignore` هو أداة في Git تُستخدم لتحديد ما إذا كان ملف أو مسار معين يتم تجاهله بواسطة آليات التجاهل في Git، مثل ملفات `.gitignore`، أو `.git/info/exclude`، أو ملفات التجاهل العامة (عبر `core.excludesFile`). إنه مفيد بشكل خاص لتصحيح الأخطاء (debugging) عندما لا يتم تتبع ملف أو إضافته إلى المستودع.

إذا كان المسار مُتجاهلاً، فإن الأمر يخرج المسار (واختياريًا، النمط المطابق). إذا لم يكن مُتجاهلاً، فلا يوجد ناتج (كود خروج 0). هذا يجعلها صديقة للاستخدام في النصوص البرمجية (scripts) للأتمتة.

### الاستخدام الأساسي

شغله مع مسار واحد أو أكثر للتحقق:

```
git check-ignore <اسم_المسار>...
```

- **مثال**: تحقق مما إذا كان ملف معين مُتجاهلاً:
  ```
  git check-ignore path/to/myfile.txt
  ```
  - الناتج: إذا كان مُتجاهلاً، يطبع `path/to/myfile.txt`. إذا لم يكن، لا يطبع شيئاً.

- **مثال**: تحقق من عدة ملفات:
  ```
  git check-ignore file1.txt file2.txt dir/file3.txt
  ```
  - يُخرج فقط المسارات المُتجاهلة، واحد لكل سطر.

### الخيارات الرئيسية

| الخيار | الوصف | مثال |
|--------|-------------|---------|
| `-v`, `--verbose` | إظهار نمط التجاهل الذي تمت مطابقته (مثل السطر من `.gitignore`). | `git check-ignore -v path/to/myfile.txt`<br>الناتج: `path/to/myfile.txt: .gitignore:1:*.txt` (مسار + ملف:سطر:نمط) |
| `-q`, `--quiet` | كتم الناتج، ولكن لا يزال يستخدم كود الخروج (0 إذا لم يتم التجاهل، 1 إذا تم التجاهل). مفيد في النصوص البرمجية. | `git check-ignore -q path/to/myfile.txt`<br>(لا يوجد ناتج؛ تحقق من `$?` لمعرفة كود الخروج) |
| `--stdin` | قراءة المسارات من الإدخال القياسي (standard input) بدلاً من سطر الأوامر. | `echo "file1.txt\nfile2.txt" \| git check-ignore --stdin` |
| `--non-matching` | عكس الناتج: إظهار المسارات التي *ليست* مُتجاهلة. | `git check-ignore --non-matching -v file1.txt file2.txt` |

### حالات الاستخدام الشائعة

1. **تصحيح قواعد `.gitignore`**:
   - إذا كان `git status` لا يُظهر ملفاً تتوقعه، شغل `git check-ignore -v <الملف>` لترى بالضبط أي قاعدة تتجاهله.
   - مثال على الناتج: `src/logs/app.log: .gitignore:5:logs/*` (مشيراً إلى أن السطر 5 في `.gitignore` يطابقه).

2. **في النصوص البرمجية (Scripts)**:
   - تحقق مما إذا كان يجب إضافة ملف:
     ```
     if git check-ignore -q myfile.txt; then
         echo "الملف مُتجاهل، يتم التخطي..."
     else
         git add myfile.txt
     fi
     ```

3. **التحقق الدفعي (Batch Checking)**:
   - اذكر جميع الملفات المُتجاهلة في دليل:
     ```
     find . -type f -print0 | xargs -0 git check-ignore
     ```

### نصائح
- يحترم ترتيب أولويات التجاهل في Git: `.gitignore` المحلي، استثناءات عامة، إلخ.
- يعمل على الملفات غير المُتتبعة أو تلك الموجودة بالفعل في المستودع (ولكنه يتحقق مقابل قواعد التجاهل).
- للمزيد من التفاصيل، راجع الوثائق الرسمية.

[Git check-ignore Documentation](https://git-scm.com/docs/git-check-ignore)  
[Stack Overflow: Git command to show which specific files are ignored](https://stackoverflow.com/questions/466764/git-command-to-show-which-specific-files-are-ignored-by-gitignore)  
[Using git check-ignore to debug your .gitignore](https://alexwlchan.net/til/2020/using-git-check-ignore-to-debug-your-gitignore/)