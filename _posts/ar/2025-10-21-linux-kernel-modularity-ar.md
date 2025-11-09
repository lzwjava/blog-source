---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: شرح نمطية نواة لينكس
translated: true
type: note
---

### فهم الوحدوية في لينكس

تشير الوحدوية في لينكس بشكل أساسي إلى تصميم نواة لينكس، والتي هي في الأساس **نواة أحادية** (حيث تعمل جميع المكونات الأساسية في مساحة عناوين واحدة من أجل الكفاءة) ولكنها تحقق الوحدوية من خلال **وحدات النواة القابلة للتحميل (LKMs)**. هذا يسمح لك بإضافة أو إزالة ميزات النواة ديناميكيًا — مثل برامج تشغيل الأجهزة، وأنظمة الملفات، أو بروتوكولات الشبكة — أثناء وقت التشغيل دون الحاجة إلى إعادة تشغيل النظام أو إعادة تجميع النواة بالكامل. إنها نهج هجين يوازن بين الأداء والمرونة، مما يجعل لينكس شديد التكيف مع الأجهزة وحالات الاستخدام المختلفة.

فكر في الأمر مثل مكعبات LEGO: النواة هي الهيكل الأساسي، ولكن يمكنك تركيب (تحميل) أو إزالة (إلغاء تحميل) القطع حسب الحاجة، مما يحافظ على النظام خفيفًا وقابلًا للتخصيص. يتم تنفيذ معظم برامج تشغيل الأجهزة في لينكس بهذه الطريقة، ولهذا يمكن للينكس دعم مجموعة واسعة من الأجهزة دون تضخيم النواة الأساسية.

#### لماذا تهم الوحدوية
- **المرونة**: قم بتحميل ما تحتاجه فقط (مثل برنامج تشغيل Wi-Fi عند الاتصال بشبكة).
- **الكفاءة**: يقلل البصمة التخزينية في الذاكرة عن طريق تجنب تضمين الكود غير المستخدم بشكل دائم.
- **القابلية للصيانة**: أسهل في تحديث أو تصحيح المكونات الفردية دون المساس بالنظام بأكمله.
- **الاستقرار**: الأعطال في وحدة واحدة معزولة إلى حد ما، وإن لم تكن بشكل صارم كما في النوى المصغرة (مثل تلك الموجودة في MINIX).

لقد ساعد هذا التصميم لينكس على الصمود لعقود، كما ذكرت في محادثتنا السابقة — فمن الأسهل تطوره من النواة الأحادية الصلبة.

#### كيف تعمل وحدات النواة
وحدات النواة هي ملفات كائن مجمعة (بامتداد `.ko`) مكتوبة بلغة C، باستخدام رؤوس النواة ونظام kbuild. يجب أن تتطابق مع إصدار نواتك (تحقق من ذلك باستخدام `uname -r`).

تتضمن الوحدة الأساسية:
- **التهيئة**: دالة معلمة بـ `module_init()` تعمل عند التحميل (مثل تسجيل برنامج تشغيل).
- **التنظيف**: دالة معلمة بـ `module_exit()` تعمل عند إلغاء التحميل (مثل تحرير الموارد).
- **البيانات الوصفية**: ماكروات مثل `MODULE_LICENSE("GPL")` للترخيص والمؤلف.

إليك مثالًا بسيطًا لوحدة (`hello.c`) تطبع رسائل:

```c
#include <linux/kernel.h>
#include <linux/init.h>
#include <linux/module.h>

MODULE_DESCRIPTION("A simple hello module");
MODULE_AUTHOR("You");
MODULE_LICENSE("GPL");

static int __init hello_init(void) {
    printk(KERN_INFO "Hello, Linux modularity!\n");
    return 0;  // Success
}

static void __exit hello_exit(void) {
    printk(KERN_INFO "Goodbye from the module!\n");
}

module_init(hello_init);
module_exit(hello_exit);
```

لتجميعها (يتطلب تثبيت رؤوس النواة، مثلاً عبر `apt install linux-headers-$(uname -r)` في أنظمة دبيان):
- أنشئ ملف `Makefile`:
  ```
  obj-m += hello.o
  KDIR := /lib/modules/$(shell uname -r)/build
  all:
      make -C $(KDIR) M=$(PWD) modules
  clean:
      make -C $(KDIR) M=$(PWD) clean
  ```
- شغل `make` لتوليد `hello.ko`.
- قم بالتحميل باستخدام `sudo insmod hello.ko` (أو `sudo modprobe hello` للتعامل مع التبعيات).
- تحقق من السجلات: `dmesg | tail` (سترى رسالة "Hello").
- قم بإلغاء التحميل: `sudo rmmod hello` (سترى "Goodbye" في `dmesg`).

تذهب الرسائل من `printk` إلى buffer النواة الحلقي (`dmesg`) أو `/var/log/kern.log`.

#### إدارة الوحدات في الممارسة العملية
استخدم هذه الأوامر (من حزمة `kmod`؛ قم بتثبيتها إذا لزم الأمر: `sudo yum install kmod` على RHEL أو `sudo apt install kmod` على Ubuntu).

| الإجراء | الأمر | الوصف/مثال |
|--------|---------|---------------------|
| **سرد الوحدات المحملة** | `lsmod` | يظهر الاسم، الحجم، عدد مرات الاستخدام، والتبعيات.<br>مثال: `lsmod \| grep bluetooth` (يصفّي وحدات البلوتوث). |
| **معلومات الوحدة** | `modinfo <name>` | تفاصيل مثل الإصدار، الوصف.<br>مثال: `modinfo e1000e` (لبرنامج تشغيل شبكة إنتل). |
| **تحميل الوحدة** | `sudo modprobe <name>` | يحمل مع التبعيات (مفضل عن `insmod`، الذي يحتاج إلى المسار الكامل).<br>مثال: `sudo modprobe serio_raw` (إدخال تسلسلي خام). |
| **إلغاء تحميل الوحدة** | `sudo modprobe -r <name>` | يلغي التحميل مع التبعيات (ألغِ تحميل التابعيات أولاً إذا لزم الأمر).<br>مثال: `sudo modprobe -r serio_raw`. تحقق من الاستخدام بـ `lsmod`. |
| **توليد التبعيات تلقائيًا** | `sudo depmod -a` | يحدّث `/lib/modules/$(uname -r)/modules.dep` لـ modprobe. |

تعيش الوحدات في `/lib/modules/$(uname -r)/kernel/`. تجنب إلغاء تحميل الوحدات قيد الاستخدام (مثل برامج التشغيل النشطة) لمنع تعطل النظام.

#### جعل الوحدات دائمة
التغييرات ليست دائمة عبر عمليات إعادة التشغيل:
- **التحميل عند الإقلاع**: أضف إلى `/etc/modules-load.d/myfile.conf` (وحدة واحدة في كل سطر).<br>مثال: `echo "hello" \| sudo tee /etc/modules-load.d/hello.conf`.
- **القائمة السوداء (منع التحميل)**: أضف إلى `/etc/modprobe.d/blacklist.conf`.<br>مثال:
  ```
  blacklist bad_module
  install bad_module /bin/false
  ```
  ثم أعيد توليد initramfs: `sudo dracut -f` وأعد التشغيل.

#### المزالق الشائعة والنصائح
- **عدم تطابق الإصدار**: يجب أن تتطابق الوحدات مع نواتك — أعد التجميع بعد التحديثات.
- **التبعيات**: `modprobe` يتعامل معها؛ تحقق منها باستخدام `modinfo --depends <name>`.
- **التصحيح**: استخدم `pr_debug` للسجلات التفصيلية (مكّنها بـ `echo 8 > /proc/sys/kernel/printk`).
- ابدأ بالتجربة في آلة افتراضية لتجنب تعطيل نظامك.

هذا الإعداد هو السبب وراء شعور لينكس بأنه "وحدوي" في الممارسة العملية — إنه ليس نواة مصغرة كاملة، لكن نظام الوحدات يحاكيها من أجل القابلية للتوسع. للتطبيق العملي، حاول تحميل برنامج تشغيل حقيقي مثل `vfat` لأنظمة ملفات FAT.

[KERNEL Modules Lab Documentation](https://linux-kernel-labs.github.io/refs/heads/master/labs/kernel_modules.html)  
[Understanding Kernel Modules on Medium](https://medium.com/@arashjafariwork/understanding-kernel-modules-enhancing-flexibility-in-operating-systems-ed348807ed7b)  
[Red Hat Kernel Administration Guide](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/7/html/kernel_administration_guide/chap-documentation-kernel_administration_guide-working_with_kernel_modules)