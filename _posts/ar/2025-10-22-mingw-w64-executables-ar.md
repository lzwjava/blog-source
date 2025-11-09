---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: التنفيذيات المضمنة في MinGW-w64
translated: true
type: note
---

### الملفات التنفيذية المضمنة في MinGW-w64

MinGW-w64 هو في الأساس سلسلة أدوات دنيا للترجمة المتقاطعة لتطبيقات Windows الأصلية باستخدام GCC والأدوات ذات الصلة. فهو يركز على أدوات التطوير بدلاً من مجموعة كاملة من أوامر شبيهة بـ Unix (على سبيل المثال، لا يشمل `gpg` أو GnuPG افتراضيًا — فهذه متاحة كحزم منفصلة في بيئات مثل MSYS2). يحتوي دليل `bin` في التثبيت الأساسي عادةً على الملفات التنفيذية التالية (استنادًا إلى تنزيل قائم بذاته قياسي، مثل الإصدارات الرسمية من SourceForge). يمكن أن يختلف هذا القليل قليلاً حسب الإصدار والبناء، ولكن هذه هي الملفات الشائعة:

| الملف التنفيذي | الوصف |
|------------|-------------|
| `gcc.exe` | مترجم لغة C من GNU |
| `g++.exe` | مترجم لغة ++C من GNU |
| `cpp.exe` | المعالج المسبق لـ C |
| `gfortran.exe` | مترجم Fortran من GNU (إذا كان مضمنًا في البناء) |
| `ld.exe` | رابط GNU |
| `as.exe` | مجمع GNU |
| `ar.exe` | الأداة المؤرشفة لإنشاء المكتبات |
| `ranlib.exe` | ينشئ فهرسًا للمكتبات المؤرشفة |
| `nm.exe` | يعرض الرموز من ملفات الكائن |
| `objdump.exe` | يعرض المعلومات من ملفات الكائن |
| `objcopy.exe` | ينسخ ويترجم ملفات الكائن |
| `strip.exe` | يزيل الرموز من الملفات التنفيذية |
| `size.exe` | يعرض أحجام الأقسام لملفات الكائن |
| `strings.exe` | يطبع السلاسل النصية القابلة للطباعة في الملفات |
| `readelf.exe` | يعرض معلومات ملف ELF (لأدوات الترجمة المتقاطعة) |
| `dlltool.exe` | ينشئ ملفات استيراد/تصدير DLL |
| `windres.exe` | يترجم ملفات موارد Windows |
| `gendef.exe` | ينشئ ملفات .def من ملفات DLL |
| `genidl.exe` | ينشئ ملفات .idl من ملفات DLL |
| `widl.exe` | يترجم ملفات IDL لـ Wine/Winelib |
| `gcc-ar.exe` | غلاف GCC لـ ar |
| `gcc-nm.exe` | غلاف GCC لـ nm |
| `gcc-ranlib.exe` | غلاف GCC لـ ranlib |

هذه في الغالب أدوات مترجم ورابط ومعالجة للملفات الثنائية من GCC و Binutils. للحصول على بيئة كاملة شبيهة بـ Unix تتضمن أدوات مثل `gpg` و `make` و `bash`، إلخ، فكر في تثبيت MSYS2 (والذي يتضمن MinGW-w64 كأحد مكوناته) وإضافة الحزم عبر `pacman`.

[الموقع الرسمي لـ MinGW-w64](https://www.mingw-w64.org/)  
[حزم MSYS2 (لإضافات مثل GnuPG)](https://packages.msys2.org/package/mingw-w64-x86_64-gnupg)  
[تنزيلات MinGW-w64 من SourceForge](https://sourceforge.net/projects/mingw-w64/files/)