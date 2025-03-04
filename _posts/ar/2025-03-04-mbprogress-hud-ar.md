---
audio: false
generated: true
lang: ar
layout: post
title: استخدام MBProgressHUD في iOS
translated: true
---

يبدو أنك تسأل عن كيفية استخدام مكتبة `MBProgressHUD` في مشروع iOS، بشكل خاص الإصدار `0.9.1` عبر ملف Podfile في CocoaPods. دعني أريك كيفية القيام بذلك خطوة بخطوة.

### ما هو MBProgressHUD؟
`MBProgressHUD` هي مكتبة ثالثة شعبية لiOS توفر طريقة سهلة لعرض HUD (Heads-Up Display) مع مؤشرات النشاط، شريط التقدم، أو مشاهد مخصصة، يتم استخدامها عادةً لعرض حالات التحميل أو رسائل قصيرة.

### خطوات لاستخدام `pod 'MBProgressHUD', '0.9.1'`

#### 1. **تثبيت CocoaPods (إذا لم يكن مثبتًا بالفعل)**
CocoaPods هو مدير الاعتماديات لمشاريع iOS. إذا لم يكن لديك مثبتًا، قم بتشغيل هذا الأمر في terminal:
```bash
sudo gem install cocoapods
```

#### 2. **إعداد ملف Podfile**
- انتقل إلى مجلد مشروعك في Xcode في terminal:
  ```bash
  cd /path/to/your/project
  ```
- إذا لم يكن لديك ملف Podfile، قم بإنشائه بتشغيل:
  ```bash
  pod init
  ```
- افتح ملف `Podfile` في محرر النصوص (مثل `nano Podfile` أو `open Podfile`).

#### 3. **إضافة MBProgressHUD إلى ملف Podfile**
في ملف `Podfile`، أضف السطر لـ `MBProgressHUD` الإصدار `0.9.1` داخل كتلة الهدف لمشروعك. يجب أن يبدو شيئًا مثل هذا:
```ruby
platform :ios, '9.0'  # تحديد هدف التوزيع الخاص بك

target 'YourAppName' do
  use_frameworks!
  pod 'MBProgressHUD', '0.9.1'
end
```
- استبدل `'YourAppName'` باسم الهدف الفعلي لمشروعك في Xcode.
- السطر `platform :ios, '9.0'` يحدد الإصدار الأدنى من iOS؛ قم بتعديله بناءً على احتياجات مشروعك.

#### 4. **تثبيت Pod**
- احفظ ملف `Podfile` و قم بتشغيل هذا الأمر في terminal:
  ```bash
  pod install
  ```
- هذا ينزيل ويدمج `MBProgressHUD` الإصدار `0.9.1` في مشروعك. إذا كان النجاح، ستشاهد إخراج يؤكد التثبيت.

#### 5. **فتح ملف العمل**
- بعد التثبيت، أغلق مشروع Xcode (إذا كان مفتوحًا) و افتح الملف `.xcworkspace` الجديد (مثل `YourAppName.xcworkspace`) بدلاً من الملف `.xcodeproj`. CocoaPods يخلق هذا الملف للعمل لإدارة الاعتماديات.

#### 6. **استخدام MBProgressHUD في كودك**
- **Swift**: استورد الوحدة واستخدمها في كودك:
  ```swift
  import MBProgressHUD

  class ViewController: UIViewController {
      override func viewDidLoad() {
          super.viewDidLoad()

          // عرض HUD بسيط مع مؤشر التحميل
          let hud = MBProgressHUD.showAdded(to: self.view, animated: true)
          hud.label.text = "Loading..."

          // اخفيه بعد فترة (مثل 2 ثانية)
          DispatchQueue.main.asyncAfter(deadline: .now() + 2) {
              hud.hide(animated: true)
          }
      }
  }
  ```

- **Objective-C**: استورد الملف الرؤوس واستخدمه:
  ```objc
  #import <MBProgressHUD/MBProgressHUD.h>

  @interface ViewController ()
  @end

  @implementation ViewController
  - (void)viewDidLoad {
      [super viewDidLoad];

      // عرض HUD بسيط مع مؤشر التحميل
      MBProgressHUD *hud = [MBProgressHUD showHUDAddedTo:self.view animated:YES];
      hud.label.text = @"Loading...";

      // اخفيه بعد فترة (مثل 2 ثانية)
      dispatch_after(dispatch_time(DISPATCH_TIME_NOW, 2 * NSEC_PER_SEC), dispatch_get_main_queue(), ^{
          [hud hideAnimated:YES];
      });
  }
  @end
  ```

#### 7. **ميزات MBProgressHUD الشائعة**
- **HUD أساسي**: كما هو موضح أعلاه، عرض مؤشر دوران مع نص اختياري.
- **نص مخصص فقط**:
  ```swift
  let hud = MBProgressHUD.showAdded(to: view, animated: true)
  hud.mode = .text
  hud.label.text = "Done!"
  hud.hide(animated: true, afterDelay: 1.5)
  ```
- **شريط التقدم**:
  ```swift
  let hud = MBProgressHUD.showAdded(to: view, animated: true)
  hud.mode = .determinate
  hud.progress = 0.5 // 50% تقدم
  ```

#### ملاحظات
- **الإصدار 0.9.1**: هذا الإصدار قديم (نشر حوالي 2015). الإصدار الأحدث حتى مارس 2025 هو أحدث بكثير (مثل 1.2.0 أو أعلى). لاستخدام أحدث إصدار، أكتب فقط `pod 'MBProgressHUD'` بدون رقم الإصدار. اعتبر التحديث إلا إذا كنت تحتاج إلى 0.9.1 لمتطلبات التوافق.
- **التوثيق**: تحقق من [صفحة MBProgressHUD على GitHub](https://github.com/jdg/MBProgressHUD) للحصول على مزيد من الخيارات والمثالات. قد يكون الإصدار 0.9.1 يحتوي على أقل من الميزات من الإصدارات الحديثة.

أعلمني إذا كنت تحتاج إلى مساعدة في حل المشاكل أو أمثلة أكثر تحديدًا!