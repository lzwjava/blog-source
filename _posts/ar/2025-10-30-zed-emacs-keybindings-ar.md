---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: تهيئة زيد بروابط مفاتيح إيمكس
translated: true
type: note
---

### تكوين محرر Zed باستخدام اختصارات Emacs

يبدو أنك تقصد **Zed** (محرر الأكواد عالي الأداء)، حيث أن "محرر Zig" لا يشير إلى أداة قياسية — Zig هي لغة برمجة بدون محرر مدمج. إذا لم يكن هذا هو ما تقصده، فلا تتردد في التوضيح! بافتراض أنك تقصد Zed، فإنه يدعم مدمجًا اختصارات Emacs (المُصنفة باسم "Emacs (Beta)"). هذا يغطي العديد من الأساسيات مباشرة، مثل الحركة (`Ctrl-b/f/n/p`) والتحرير (`Ctrl-d` لحذف حرف، `Ctrl-k` لقص حتى نهاية السطر). يمكنك تمكينه بسهولة، ثم تخصيصه أكثر إذا لزم الأمر.

#### الخطوة 1: تمكين خريطة مفاتيح Emacs المدمجة
وضع Emacs في Zed مُعرف مسبقًا ولا يتطلب إعداد ربط يدوي للأساسيات. إليك كيفية التبديل إليه:

1. افتح إعدادات Zed:
   - نظام macOS: `Cmd-,`
   - نظام Windows/Linux: `Ctrl-,`

2. في واجهة مستخدم الإعدادات، ابحث عن "base keymap" وعينه إلى **Emacs**.

   *أو، قم بالتعديل مباشرة في ملف `settings.json`* (افتحه عبر `Cmd-Alt-,` على نظام macOS أو `Ctrl-Alt-,` على نظام Windows/Linux):
   ```json
   {
     "base_keymap": "Emacs"
   }
   ```

   احفظ وأعد تحميل Zed (`Cmd-R` أو `Ctrl-R`). هذا كل شيء — يتم تفعيل خريطة مفاتيح Emacs التجريبية على الفور.

   بدلاً من ذلك، استخدم لوحة الأوامر (`Cmd-Shift-P` أو `Ctrl-Shift-P`)، واكتب "toggle base keymap"، واختر Emacs.

هذا يمنحك ذاكرة العضلات الأساسية لـ Emacs بدون عمل إضافي. للحصول على قائمة كاملة بالاختصارات المدمجة، تحقق من ملفات خريطة المفاتيح الافتراضية لـ Zed في المصدر (على سبيل المثال، عبر GitHub)، ولكن الأساسيات تشمل:
- **الحركة**: `Ctrl-b` (حرف لليسار)، `Ctrl-f` (حرف لليمين)، `Ctrl-p` (سطر لأعلى)، `Ctrl-n` (سطر لأسفل)، `Alt-b/f` (كلمة سابقة/تالية).
- **التحرير**: `Ctrl-d` (حذف حرف)، `Ctrl-k` (قص حتى نهاية السطر)، `Ctrl-y` (نسخ/لصق)، `Ctrl-@` (تعيين علامة للمنطقة)، `Ctrl-w` (قص المنطقة).
- **أخرى**: `Ctrl-x Ctrl-s` (حفظ)، `Ctrl-g` (إلغاء)، `Ctrl-/` (تراجع).

#### الخطوة 2: إضافة أو تخصيص الاختصارات الأساسية (إذا لزم الأمر)
للتعديلات أو سلوك أكثر شبهاً بـ Emacs (على سبيل المثال، تحسين التنقل إلى Home/End أو التنقل بين الفقرات)، قم بتعديل `keymap.json`:
- افتحه عبر لوحة الأوامر: اكتب "open keymap file."
- المسار: `~/.config/zed/keymap.json` (macOS/Linux) أو `~\AppData\Roaming\Zed\keymap.json` (Windows).

أضف الاختصارات كمصفوفة JSON في سياقات مثل "Editor". إليك **مثال بسيط** للحركة والتحرير الأساسيين (الصقه في المصفوفة؛ وهو مبني على إعدادات المجتمع للتطابق):

```json
[
  {
    "context": "Editor",
    "bindings": {
      // الحركة الأساسية
      "ctrl-a": "editor::MoveToBeginningOfLine",
      "ctrl-e": "editor::MoveToEndOfLine",
      "ctrl-b": "editor::MoveLeft",
      "ctrl-f": "editor::MoveRight",
      "ctrl-p": "editor::MoveLineUp",
      "ctrl-n": "editor::MoveLineDown",
      "alt-b": "editor::MoveToPreviousWordStart",
      "alt-f": "editor::MoveToNextWordEnd",

      // التحرير الأساسي
      "ctrl-d": "editor::DeleteRight",
      "ctrl-k": "editor::CutToEndOfLine",
      "ctrl-y": "editor::Paste",
      "ctrl-w": "editor::Cut",
      "ctrl-@": ["editor::SetSelectionAnchor", { "selection_id": 0 }],  // تعيين العلامة
      "ctrl-x ctrl-x": "editor::FlipSelectionAnchor",  // تبادل النقطة/العلامة

      // إضافات التنقل
      "ctrl-home": "editor::MoveToBeginning",
      "ctrl-end": "editor::MoveToEnd",
      "ctrl-g": "editor::Cancel"
    }
  }
]
```

- احفظ وأعد تحميل Zed. هذه تتجاوز أو تُضاف إلى خريطة Emacs الأساسية.
- اختبر في مخزن مؤقت للمحرر. للتحديدات، استخدم `Ctrl-Space` (أو `Ctrl-@`) لتعيين العلامة، ثم تحرك لتحديد منطقة.
- نصيحة احترافية: اجمعها مع `vim_mode: false` في settings.json لتجنب التعارضات.

#### نصائح
- **حالة التجريب**: وضع Emacs في تحسن (تتبع التقدم [هنا](https://github.com/zed-industries/zed/issues/4856)). أبلغ عن المشكلات على GitHub الخاص بـ Zed.
- **الإعدادات المخصصة الكاملة**: للمستوى المتقدم (على سبيل المثال، تبديل الألواح بـ `Ctrl-x o`)، راجع أمثلة المجتمع في المناقشة أدناه.
- إذا كنت تريد أوضاع Vim/Helix أيضًا، عيّن `vim_mode: true` أو `helix_mode: true` في الإعدادات — فهي تعمل فوقها.

هذا يجب أن يمنحك 80% من الإحساس الأساسي بـ Emacs. ابدأ بالمدمج، ثم تقدم تدريجيًا!

[وثائق اختصارات المفاتيح](https://zed.dev/docs/key-bindings)  
[تكوين Zed](https://zed.dev/docs/configuring-zed)  
[مناقشة خريطة مفاتيح Emacs](https://github.com/zed-industries/zed/discussions/6572)  
[مشكلة توافق Emacs](https://github.com/zed-industries/zed/issues/4856)