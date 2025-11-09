---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: هيكل محتوى تطبيقات iOS باستخدام NSArray
translated: true
type: note
---

### تنظيم محتوى الإلكترونيات التناظرية في تطبيق iOS باستخدام NSArray و NSString

في تطبيق iOS لتعليم الإلكترونيات التناظرية وتحليل الدوائر (بناءً على الدليل الذي شاركته)، تعتبر `NSArray` و `NSString` فئتين أساسيتين من إطار عمل Foundation من Apple. إنها مثالية للتعامل مع المحتوى التعليمي المنظم القائم على النص:

- **`NSString`**: استخدم هذه الفئة للسلاسل النصية الثابتة مثل العناوين، والوصوف، والصيغ، والأمثلة. إنها فعالة للنص الثابت وتدعم التنسيق (على سبيل المثال، عبر `NSAttributedString` للنص المنسق في تسميات واجهة المستخدم).
- **`NSArray`**: استخدم هذه الفئة للمجموعات المرتبة من البيانات، مثل قوانين القوانين، أو الخطوات، أو الأمثلة. هي ثابتة بشكل افتراضي، مما يجعلها مثالية للثوابت على مستوى التطبيق. لجعلها قابلة للتعديل، انتقل إلى `NSMutableArray`.

عادةً ما تقوم بتحميل هذه البيانات عند بدء تشغيل التطبيق (على سبيل المثال، في `AppDelegate` أو في كائن إدارة بيانات مفرد) وعرضها في واجهات مثل `UITableView` (للعناوين/القوائم) أو `UILabel` (للتفاصيل). أدناه، سأوضح كيفية نمذجة محتوى الدليل باستخدام هذه الفئات، مع مقاطع كود Objective-C. (المكافئات في Swift تستخدم `Array` و `String`، لكنني سألتزم بالكلاسيكيات بما أنك ذكرت NSArray/NSString.)

#### 1. مثال أساسي: تخزين المفاهيم الأساسية كمصفوفة NSArray من سلاسل NSString
للحصول على قوائم بسيطة مثل الفولتية، والتيارات، أو الصيغ، قم بإنشاء `NSArray` من كائنات `NSString`. يمكن أن يملأ هذا النص الفرعي لخلية عرض الجدول.

```objective-c
// في ملف .h أو في مدير البيانات
@property (nonatomic, strong) NSArray<NSString *> *keyConcepts;

// في ملف .m (على سبيل المثال، viewDidLoad)
self.keyConcepts = @[
    @"الجهد الكهربائي (V): فرق الجهد بين نقطتين، يقاس بالفولت (V). وهو الذي يدفع التيار ليمر عبر الدائرة.",
    @"التيار (I): تدفق الشحنة الكهربائية، يقاس بالأمبير (A). الاتجاه مهم (التيار التقليدي يتدفق من الموجب إلى السالب).",
    @"المقاومة (R): المعارضة لتدفق التيار، تقاس بالأوم (Ω). المقاومات هي مكونات سلبية تبدد الطاقة على شكل حرارة.",
    @"القدرة (P): معدل استهلاك الطاقة، وتعطى بالعلاقة P = VI = I²R = V²/R، بالواط (W)."
];

// الاستخدام: العرض في UITableView
- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath {
    UITableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:@"ConceptCell" forIndexPath:indexPath];
    cell.textLabel.text = self.keyConcepts[indexPath.row];
    return cell;
}
```

هذا ينشئ قائمة قابلة للتمرير للتعريفات. بالنسبة للصيغ، استخدم سلاسل Unicode/LaTeX (اعرضها باستخدام `UILabel` أو مكتبة رياضيات مثل iosMath للحصول على عرض أفضل).

#### 2. نمذجة الأقسام باستخدام مصفوفات متداخلة (مثل القوانين والأمثلة)
يحتوي الدليل على أقسام مثل "مفاهيم الدوائر الأساسية والقوانين". استخدم `NSArray` من كائنات `NSDictionary`، حيث يحتوي كل قاموس على مفاتيح/قيم `NSString` للعنوان، والوصف، والعناصر الفرعية (مصفوفة `NSArray` أخرى من `NSString` للخطوات/الأمثلة).

```objective-c
// تعريف مصفوفة عالية المستوى للدليل بأكمله
@property (nonatomic, strong) NSArray<NSDictionary *> *guideSections;

// التعبئة في ملف .m
self.guideSections = @[
    @{
        @"title": @"قانون أوم",
        @"description": @"ينص قانون أوم على أن الجهد عبر المقاومة يتناسب طردياً مع التيار المار خلالها: V = IR.",
        @"examples": @[
            @"في دائرة تحتوي على بطارية 12 فولت ومقاومة 4 أوم، التيار هو I = 12/4 = 3A. القدرة المبددة هي P = 12 × 3 = 36W."
        ]
    },
    @{
        @"title": @"قانون كيرشوف للتيار (KCL)",
        @"description": @"مجموع التيارات الداخلة إلى عقدة يساوي مجموع التيارات الخارجة منها (حفظ الشحنة). ∑I_in = ∑I_out.",
        @"examples": @[
            @"عند تقاطع، إذا دخل 2A من فرع و 3A من آخر، يجب أن يخرج 5A عبر الفرع الثالث."
        ]
    },
    @{
        @"title": @"قانون كيرشوف للجهد (KVL)",
        @"description": @"مجموع الجهود حول أي حلقة مغلقة يساوي صفر (حفظ الطاقة). ∑V = 0.",
        @"examples": @[
            @"في حلقة تحتوي على مصدر 10 فولت، انخفاض جهد 2 فولت عبر R1، وانخفاض جهد 3 فولت عبر R2، يجب أن يكون الانخفاض المتبقي 5 فولت لإغلاق الحلقة."
        ]
    }
];

// الاستخدام: التكرار لعرض جدول مقسم
- (NSInteger)numberOfSectionsInTableView:(UITableView *)tableView {
    return self.guideSections.count;
}

- (NSString *)tableView:(UITableView *)tableView titleForHeaderInSection:(NSInteger)section {
    NSDictionary *sectionData = self.guideSections[section];
    return sectionData[@"title"];
}

- (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section {
    NSDictionary *sectionData = self.guideSections[section];
    NSArray<NSString *> *examples = sectionData[@"examples"];
    return 1 + examples.count; // 1 لصف الوصف + صفوف الأمثلة
}

- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath {
    // ... (dequeue cell, set text to description or example based on row)
    NSDictionary *sectionData = self.guideSections[indexPath.section];
    if (indexPath.row == 0) {
        cell.textLabel.text = sectionData[@"description"];
    } else {
        NSArray<NSString *> *examples = sectionData[@"examples"];
        cell.textLabel.text = examples[indexPath.row - 1];
    }
    return cell;
}
```

هذا يدمج البيانات بشكل طبيعي: انقر على عنوان القسم لتوسيع الأمثلة. للمحتوى الديناميكي (مثل ملاحظات المستخدم)، استخدم `NSMutableArray` و `NSMutableDictionary`.

#### 3. متقدم: التحليل العابر مع بيانات منظمة
للأقسام الديناميكية مثل دوائر RC/RL، قم بتضمين الصيغ والبيانات المعتمدة على الزمن. استخدم `NSString` للمعادلات ومصفوفة `NSArray` داخلية لاستجابات الخطوة.

```objective-c
self.transientExamples = @[
    @{
        @"circuitType": @"شحن RC",
        @"formula": @"V_C(t) = V_s (1 - e^{-t/RC})",
        @"timeConstant": @"τ = RC",
        @"steps": @[
            @"ابتدائي: V_C(0) = 0; نهائي: V_C(∞) = V_s.",
            @"مثال: R=1kΩ, C=1μF (τ=1ms), V_s=5V. عند t=1ms, V_C ≈ 3.16V."
        ]
    },
    @{
        @"circuitType": @"اضمحلال RL",
        @"formula": @"I_L(t) = I_0 e^{-Rt/L}",
        @"timeConstant": @"τ = L/R",
        @"steps": @[
            @"التيار لا يمكن أن يتغير فورياً.",
            @"زمن الاستقرار ≈ 5τ."
        ]
    }
];

// في وحدة تحكم عرض التفاصيل، اعرض الصيغة بخط أحادي المسافة
UILabel *formulaLabel = [[UILabel alloc] init];
formulaLabel.font = [UIFont monospacedSystemFontOfSize:14 weight:UIFontWeightMedium];
formulaLabel.text = dict[@"formula"];
```

#### نصائح للتنفيذ
- **مصدر البيانات**: قم بتخزين هذا في ملف plist (حمله باستخدام `NSDictionary *data = [NSDictionary dictionaryWithContentsOfFile:path];`) أو قم بتشفيره كما هو موضح للبساطة.
- **التكامل مع واجهة المستخدم**: اربط بـ `UITableView` أو `UICollectionView` للاختبارات التفاعلية (على سبيل المثال، مثال عشوائي من المصفوفة). استخدم دوال `NSString` مثل `stringByAppendingString:` للنص الديناميكي (على سبيل المثال، إدخال قيم المستخدم للحسابات).
- **الأداء**: المصفوفات خفيفة الوزن؛ للدلائل الكبيرة، فكر في استخدام Core Data إذا كنت تريد إضافة استمرارية.
- **التحسينات**: انتقل إلى Swift للتطبيقات الحديثة، أو أضف `NSAttributedString` للصيغ المكتوبة بخط عريض.

هذا الإعداد يحافظ على تطبيقك معياريًا — يسهل تحديث المحتوى دون تغييرات في واجهة المستخدم. للحصول على الكود الكامل، راجع عينات Apple.

[Apple Foundation Framework Docs](https://developer.apple.com/documentation/foundation)  
[UITableView Tutorial](https://developer.apple.com/tutorials/app-dev-training/creating-a-list-with-a-table-view)