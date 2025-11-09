---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: نظرة عامة على NSArray لتطوير iOS
translated: true
type: note
---

### ما هو NSArray؟

`NSArray` هو فئة في إطار Foundation من Apple، وهو جزء من iOS SDK (وmacOS، إلخ). يمثل مجموعة ثابتة غير قابلة للتغيير ومُرتبة من الكائنات، مشابهة للمصفوفة في اللغات الأخرى. هذا يعني أنه بمجرد إنشاء `NSArray`، لا يمكنك إضافة أو إزالة أو استبدال العناصر—يمكنك فقط القراءة منها. تُستخدم بشكل شائع في Objective-C لتطوير تطبيقات iOS لتخزين وإدارة قوائم البيانات، مثل تفضيلات المستخدم أو نتائج استعلامات قاعدة البيانات أو عناصر واجهة المستخدم.

الميزات الرئيسية:
- **ثابت غير قابل للتغيير**: حجم ومحتويات ثابتة بعد الإنشاء (استخدم `NSMutableArray` للإصدارات القابلة للتغيير).
- **آمن للنوع بالنسبة للكائنات**: يخزن مؤشرات إلى كائنات Objective-C (مثل `NSString`، `NSNumber`، والفئات المخصصة). لا يدعم الأنواع البدائية مباشرة—قم بتغليفها في `NSNumber` أو ما شابه.
- **الوصول المفهرس**: يتم الوصول إلى العناصر بواسطة فهرس عددي (يبدأ من 0).
- **آمن للخيوط**: آمن بشكل عام للقراءات المتزامنة، ولكن ليس للكتابة (لأنه ثابت).
- **التكامل**: يعمل بسلاسة مع فئات Foundation الأخرى مثل `NSDictionary`، `NSString`، ومكونات واجهة مستخدم Cocoa Touch.

في Swift، يتم ربط `NSArray` مع `Array`، ولكن إذا كنت تعمل في Objective-C (شائع في كود iOS القديم)، فستستخدم `NSArray` مباشرة.

### كيفية استخدام NSArray في iOS

لاستخدام `NSArray` في مشروع iOS:
1. قم باستيراد إطار Foundation (عادة ما يكون مضمنًا افتراضيًا في تطبيقات iOS).
   ```objc
   #import <Foundation/Foundation.h>
   ```

2. **إنشاء NSArray**:
   - بناء الجملة الحرفي (iOS 6+): `@[object1, object2, ...]`
   - طريقة التهيئة: `[[NSArray alloc] initWithObjects:object1, object2, nil]`
   - من مصفوفة C: `initWithArray:copyItems:`

   مثال:
   ```objc
   NSArray *fruits = @[@"apple", @"banana", @"cherry"];
   // أو:
   NSArray *numbers = [[NSArray alloc] initWithObjects:@1, @2, @3, nil];
   ```

3. **الوصول إلى العناصر**:
   - `objectAtIndex:` للحصول على عنصر.
   - `count` للحصول على الطول.
   - `firstObject` / `lastObject` للحواف.
   - `containsObject:` للتحقق من الوجود.

   مثال:
   ```objc
   NSString *firstFruit = [fruits objectAtIndex:0]; // "apple"
   NSUInteger count = [fruits count]; // 3
   BOOL hasOrange = [fruits containsObject:@"orange"]; // NO
   ```

4. **التكرار**:
   - التعداد السريع: `for (id obj in array) { ... }`
   - `enumerateObjectsUsingBlock:` للتكرار القائم على البلوكات (iOS 4+).

   مثال:
   ```objc
   for (NSString *fruit in fruits) {
       NSLog(@"Fruit: %@", fruit);
   }
   ```

5. **العمليات الشائعة**:
   - الفرز: `sortedArrayUsingSelector:` أو `sortedArrayUsingComparator:`.
   - التصفية: `filteredArrayUsingPredicate:` (مع NSPredicate).
   - الربط: `componentsJoinedByString:` للنصوص.
   - الكتابة إلى ملف: `writeToFile:atomically:`.

   مثال (تصفية):
   ```objc
   NSPredicate *predicate = [NSPredicate predicateWithFormat:@"length > 5"];
   NSArray *longFruits = [fruits filteredArrayUsingPredicate:predicate];
   // النتائج: @[@"banana", @"cherry"]
   ```

6. **في سياقات iOS**:
   - **عروض الجداول**: مرّر `NSArray` إلى دوال مصدر بيانات `UITableView` مثل `tableView:numberOfRowsInSection:` (عبر `count`) و `tableView:cellForRowAtIndexPath:` (عبر `objectAtIndex:`).
   - **الإعدادات الافتراضية للمستخدم**: تخزين/استرجاع باستخدام `NSUserDefaults`: `[defaults setObject:array forKey:@"savedItems"];`.
   - **معالجة JSON**: التحويل من/إلى `NSData` باستخدام `JSONObjectWithData:options:error:`.

للاحتياجات القابلة للتغيير (مثل إضافة عناصر ديناميكيًا)، انتقل إلى `NSMutableArray`:
```objc
NSMutableArray *mutableFruits = [NSMutableArray arrayWithArray:fruits];
[mutableFruits addObject:@"date"];
```

### نصائح
- تحقق دائمًا من `nil` أو الحدود لتجنب الأعطال: استخدم `objectAtIndex:` مع التحقق من صحة الفهرس.
- الأداء: O(1) للوصول، O(n) للبحث.
- iOS الحديث: فكر في استخدام `Array` من Swift للمشاريع الجديدة—فهو أكثر أمانًا من حيث النوع.

[توثيق NSArray](https://developer.apple.com/documentation/foundation/nsarray)  
[توثيق NSMutableArray](https://developer.apple.com/documentation/foundation/nsmutablearray)