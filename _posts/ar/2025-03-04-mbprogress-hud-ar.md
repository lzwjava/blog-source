---
audio: false
generated: true
lang: ar
layout: post
title: استخدام MBProgressHUD في iOS
translated: true
type: note
---

يبدو أنك تسأل عن كيفية استخدام مكتبة `MBProgressHUD` في مشروع iOS، الإصدار `0.9.1` تحديدًا، عبر ملف Podfile في CocoaPods. دعني أرشدك خلال العملية خطوة بخطوة.

### ما هي MBProgressHUD؟
`MBProgressHUD` هي مكتبة طرف ثالث شائعة لنظام iOS توفر طريقة سهلة لعرض HUD (شاشة عرض أمامية) مع مؤشرات نشاط، أشرطة تقدم، أو عناصر واجهة مخصصة، تُستخدم عادةً لإظهار حالات التحميل أو رسائل موجزة.

### خطوات استخدام `pod 'MBProgressHUD', '0.9.1'`

#### 1. **تثبيت CocoaPods (إذا لم يكن مثبتًا مسبقًا)**
CocoaPods هو مدير تبعيات لمشاريع iOS. إذا لم يكن لديك مثبتًا، شغّل هذا الأمر في الطرفية:
```bash
sudo gem install cocoapods
```

#### 2. **إعداد ملف Podfile**
- انتقل إلى دليل مشروع Xcode الخاص بك في الطرفية:
  ```bash
  cd /path/to/your/project
  ```
- إذا لم يكن لديك ملف Podfile مسبقًا، أنشئه بتشغيل:
  ```bash
  pod init
  ```
- افتح ملف `Podfile` في محرر نصوص (مثل `nano Podfile` أو `open Podfile`).

#### 3. **إضافة MBProgressHUD إلى ملف Podfile الخاص بك**
في ملف `Podfile` الخاص بك، أضف سطر `MBProgressHUD` الإصدار `0.9.1` داخل كتلة الهدف (target) لتطبيقك. يجب أن يبدو كالتالي تقريبًا:
```ruby
platform :ios, '9.0'  # حدد هدف النشر الخاص بك

target 'YourAppName' do
  use_frameworks!
  pod 'MBProgressHUD', '0.9.1'
end
```
- استبدل `'YourAppName'` بالاسم الفعلي للهدف (target) في Xcode الخاص بك.
- يحدد سطر `platform :ios, '9.0'` الحد الأدنى لإصدار iOS؛ اضبطه بناءً على احتياجات مشروعك.

#### 4. **تثبيت الـ Pod**
- احفظ ملف `Podfile` وشغّل هذا الأمر في الطرفية:
  ```bash
  pod install
  ```
- يقوم هذا بتنزيل ودمج `MBProgressHUD` الإصدار `0.9.1` في مشروعك. إذا نجحت العملية، سترى ناتجًا يؤكد التثبيت.

#### 5. **فتح مساحة العمل (Workspace)**
- بعد التثبيت، أغلق مشروع Xcode الخاص بك (إذا كان مفتوحًا) وافتح ملف `.xcworkspace` newly created (مثل `YourAppName.xcworkspace`) بدلاً من ملف `.xcodeproj`. يقوم CocoaPods بإنشاء مساحة العمل هذه لإدارة التبعيات.

#### 6. **استخدام MBProgressHUD في الكود الخاص بك**
- **Swift**: استورد الوحدة النمطية واستخدمها في الكود الخاص بك:
  ```swift
  import MBProgressHUD

  class ViewController: UIViewController {
      override func viewDidLoad() {
          super.viewDidLoad()
          
          // عرض HUD بسيط مع مؤشر تحميل
          let hud = MBProgressHUD.showAdded(to: self.view, animated: true)
          hud.label.text = "جاري التحميل..."
          
          // إخفاؤه بعد فترة زمنية (مثلاً، ثانيتين)
          DispatchQueue.main.asyncAfter(deadline: .now() + 2) {
              hud.hide(animated: true)
          }
      }
  }
  ```

- **Objective-C**: استورد العنوان واستخدمه:
  ```objc
  #import <MBProgressHUD/MBProgressHUD.h>

  @interface ViewController ()
  @end

  @implementation ViewController
  - (void)viewDidLoad {
      [super viewDidLoad];
      
      // عرض HUD بسيط مع مؤشر تحميل
      MBProgressHUD *hud = [MBProgressHUD showHUDAddedTo:self.view animated:YES];
      hud.label.text = @"جاري التحميل...";
      
      // إخفاؤه بعد فترة زمنية (مثلاً، ثانيتين)
      dispatch_after(dispatch_time(DISPATCH_TIME_NOW, 2 * NSEC_PER_SEC), dispatch_get_main_queue(), ^{
          [hud hideAnimated:YES];
      });
  }
  @end
  ```

#### 7. **ميزات MBProgressHUD الشائعة**
- **HUD أساسي**: كما هو موضح أعلاه، عرض مؤشر دوار مع نص اختياري.
- **نص مخصص فقط**:
  ```swift
  let hud = MBProgressHUD.showAdded(to: view, animated: true)
  hud.mode = .text
  hud.label.text = "تم!"
  hud.hide(animated: true, afterDelay: 1.5)
  ```
- **شريط التقدم**:
  ```swift
  let hud = MBProgressHUD.showAdded(to: view, animated: true)
  hud.mode = .determinate
  hud.progress = 0.5 // تقدم 50%
  ```

#### ملاحظات
- **الإصدار 0.9.1**: هذا إصدار قديم (تم إصداره حوالي عام 2015). أحدث إصدار اعتبارًا من مارس 2025 هو أحدث بكثير (مثل 1.2.0 أو أعلى). لاستخدام الأحدث، اكتب ببساطة `pod 'MBProgressHUD'` بدون رقم إصدار. فكّر في التحديث إلا إذا كنت تحتاج تحديدًا إلى الإصدار 0.9.1 لأسباب توافقية.
- **التوثيق**: راجع [صفحة MBProgressHUD على GitHub](https://github.com/jdg/MBProgressHUD) للحصول على المزيد من الخيارات والأمثلة. قد يكون للإصدار 0.9.1 ميزات أقل من الإصدارات الحديثة.

دعني أعلم إذا كنت بحاجة إلى مساعدة في استكشاف الأخطاء وإصلاحها أو إلى أمثلة أكثر تحديدًا!