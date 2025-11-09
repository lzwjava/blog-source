---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: نظرة عامة على وحدة تحكم نافذة إعدادات RIG
translated: true
type: note
---

### نظرة عامة

ينفّش هذا الكود المكتوب بلغة Objective-C فئة `RIGSettingWindowController`، والتي تدير نافذة إعدادات لتطبيق "Reveal-In-GitHub" (RIG) لنظام macOS (من المحتمل أنه إضافة لـ Xcode تتيح إظهار الكود المحدد بسرعة في مستودعات GitHub). تسمح النافذة للمستخدمين بتكوين عناصر قائمة مخصصة، واختصارات لوحة المفاتيح، وأنماط regex لمستودعات GitHub مختلفة. تستخدم طريقة عرض تشبه الجدول (`RIGConfigCellsView`) لعرض وتعديل ما يصل إلى 10 فتحات إعدادات (مع حشو الفتحات الفارغة لضمان اتساق واجهة المستخدم).

تتوافق الفئة مع بروتوكولي `NSTableViewDataSource` و `NSTableViewDelegate`، مما يشير إلى أنها تتعامل مع البيانات والأحداث لطريقة عرض جدول داخل طريقة عرض الخلايا المخصصة. وهي تتكامل مع الكائنات المفردة على مستوى التطبيق مثل `RIGSetting` للحفظ الدائم و `RIGUtils` للحصول على ملاحظات واجهة المستخدم.

المسؤوليات الرئيسية:
- تحميل وعرض العناصر القابلة للتكوين (مثل عناوين القوائم، ومفاتيح الاختصار، وأنماط regex).
- التحقق من صحة التغييرات وحفظها.
- توفير أزرار للحفظ، ومسح إعدادات المستودع الافتراضي، وإعادة التعيين إلى الإعدادات الافتراضية.

### عمليات الاستيراد والتعريفات

```objectivec
#import "RIGSettingWindowController.h"
#import "RIGConfigCellsView.h"
#import "RIGConfig.h"
#import "RIGPlugin.h"
#import "RIGUtils.h"
#import "RIGSetting.h"

#define kOutterXMargin 0
#define kOutterYMargin 0
```

- تستورد عمليات الاستيراد رأس هذه الفئة، وطريقة عرض مخصصة لعرض صفوف الإعدادات (`RIGConfigCellsView`)، وكائنات النموذج (`RIGConfig` للإعدادات الفردية، `RIGSetting` للتخزين على مستوى التطبيق)، والأدوات المساعدة (`RIGUtils` للتنبيهات، `RIGPlugin` ربما لدورة حياة الإضافة).
- تحدد التعريفات هوامش صفرية لتخطيط عرض الإعدادات بعرض كامل داخل النافذة.

### الواجهة الخاصة

```objectivec
@interface RIGSettingWindowController ()<NSTableViewDataSource, NSTableViewDelegate>

@property (nonatomic, strong) NSArray *configs;
@property (nonatomic, strong) RIGConfigCellsView *configCellsView;
@property (weak) IBOutlet NSView *mainView;
@property (weak) IBOutlet NSView *configsView;

@end
```

- تعلن عن امتداد خاص للخصائص الداخلية والتوافق مع البروتوكول.
- `configs`: مصفوفة من كائنات `RIGConfig` التي تحتفظ بإعدادات المستخدم (مثل عنوان القائمة، آخر مفتاح تم الضغط عليه، نمط regex).
- `configCellsView`: طريقة عرض مخصصة تعرض الإعدادات كصفوف قابلة للتحرير (من المحتمل أن تكون جدولاً قابلاً للتمرير أو مجموعة من الخلايا).
- `mainView` و `configsView`: منافذ IBOutlet لطرق عرض الحاويات في ملف storyboard/nib؛ تستضيف `configsView` الخلايا الديناميكية.

### التنفيذ

#### طرق التهيئة

```objectivec
- (void)awakeFromNib {
    [super awakeFromNib];
}

- (void)windowDidLoad {
    [super windowDidLoad];
    
    self.configs = [self displayConfigs];
    
    self.configCellsView = [[RIGConfigCellsView alloc] initWithFrame:CGRectMake(kOutterXMargin, kOutterYMargin, CGRectGetWidth(self.configsView.frame) - 2 * kOutterXMargin, [RIGConfigCellsView heightForConfigs:self.configs])];
    self.configCellsView.configs = self.configs;
    [self.configsView addSubview:self.configCellsView];
    [self.configCellsView reloadData];
}
```

- `awakeFromNib`: تجاوز فارغ؛ يتم استدعاؤه عند تحميل النافذة من nib (storyboard). يقتصر على التوصيل بالفئة الأصل.
- `windowDidLoad`: الإعداد الأساسي بعد تحميل النافذة بالكامل.
  - يقوم بتحميل `configs` عبر `displayConfigs` (سيتم شرحه لاحقًا).
  - ينشئ `configCellsView` بإطار يملأ `configsView` أفقيًا (باستخدام الهوامش) وعموديًا بناءً على الارتفاع الإجمالي المطلوب لجميع الإعدادات (يتم حسابه بواسطة طريقة فئة `RIGConfigCellsView`).
  - يعين الإعدادات للعرض، ويضيفها كعرض فرعي، ويطلق إعادة تحميل البيانات (من المحتمل أن يقوم بتحديث خلايا الجدول).

هناك استدعاء معلّق لـ `updateConfigsViewHeight`، مما يشير إلى أنه تم النظر في تغيير الحجم الديناميكي ولكن تم تعطيله - ربما لأن عرض الخلايا يغير حجمه تلقائيًا أو لأن النافذة ثابتة.

```objectivec
- (void)updateConfigsViewHeight {
    CGRect frame = self.configsView.frame;
    frame.size.height = CGRectGetHeight(self.configCellsView.frame);
    self.configsView.frame = frame;
}
```

- أداة مساعدة لتغيير حجم `configsView` ليطابق ارتفاع عرض الخلايا. لا يتم استخدامه حاليًا، ولكن يمكن استخدامه لتكبير النافذة تلقائيًا إذا تمت إضافة المزيد من الإعدادات.

#### إدارة الإعدادات

```objectivec
- (NSMutableArray *)displayConfigs {
    NSMutableArray *configs = [NSMutableArray arrayWithArray:[RIGSetting setting].configs];
    while (configs.count < 10) {
        RIGConfig *config = [[RIGConfig alloc] init];
        config.menuTitle = @"";
        config.lastKey = @"";
        config.pattern = @"";
        [configs addObject:config];
    }
    return configs;
}
```

- يقوم بتحميل الإعدادات الحالية من الكائن المفرد للتطبيق `RIGSetting`.
- يقوم بحشو المصفوفة بما يقارب 10 عنصرًا باستخدام نماذج `RIGConfig` فارغة. يضمن هذا واجهة مستخدم متسقة (على سبيل المثال، 10 صفوف قابلة للتحرير)، حتى إذا كان لدى المستخدم إعدادات محفوظة أقل. يتم تصفية الإعدادات الفارغة عند الحفظ.

```objectivec
- (void)reloadConfigs {
    self.configs = [self displayConfigs];
    self.configCellsView.configs = self.configs;
    [self.configCellsView reloadData];
}
```

- يقوم بتحديث الإعدادات المعروضة من التخزين وتحديث العرض. يتم استخدامه بعد عمليات إعادة التعيين.

```objectivec
- (BOOL)isValidConfigs:(NSArray *)configs {
    for (RIGConfig *config in configs) {
        if (![config isValid]) {
            return NO;
        }
    }
    return YES;
}
```

- يتكرر عبر الإعدادات ويستدعي `isValid` على كل منها (من المحتمل أن يتحقق من أن `menuTitle` و `pattern` غير فارغين). يُرجع `YES` فقط إذا كانت جميعها صالحة أو فارغة (ولكن انظر التصفية أدناه).

```objectivec
- (NSArray *)filteredConfigs {
    NSMutableArray *filtered = [NSMutableArray array];
    NSArray *configs = self.configCellsView.configs;
    for (RIGConfig *config in configs) {
        if (config.menuTitle.length > 0 || config.lastKey.length > 0 || config.pattern.length > 0) {
            [filtered addObject:config];
        }
    }
    return filtered;
}
```

- يقوم بتصفية مصفوفة الفتحات العشر لتشمل فقط الإعدادات غير الفارغة (بناءً على وجود محتوى في أي حقل). هذا يزيل الإعدادات الفارغة قبل التحقق من الصحة/الحفظ، لذا فإن `isValidConfigs` يتحقق فقط من الإدخالات الحقيقية.

#### معالجات الإجراءات (IBActions)

يتم توصيل هذه بالزر في واجهة المستخدم عبر Interface Builder.

```objectivec
- (IBAction)saveButtonClcked:(id)sender {
    NSArray *configs = [self filteredConfigs];
    if (![self isValidConfigs:configs]) {
        [RIGUtils showMessage:@"Please complete the config, should at least have menuTitle and pattern."];
        return;
    }
    [RIGSetting setting].configs = self.configCellsView.configs;
    [RIGUtils showMessage:@"Save succeed. Will Take effect when reopen Xcode."];
}
```

- **زر الحفظ**: يقوم بتصفية الإعدادات، والتحقق من صحتها (تنبيه خطأ إذا كانت غير صالحة)، ثم يحفظ المصفوفة الكاملة (المحشوة) مرة أخرى في `RIGSetting`. ملاحظة: يحفظ الفتحات العشر كاملة، ولكن يتم تجاهل الفتحات الفارغة عند التحميل/التصفية. يظهر رسالة نجاح تشير إلى الحاجة إلى إعادة تشغيل Xcode (إعادة تحميل الإضافة).

خطأ إملائي في اسم الطريقة: "Clcked" يجب أن يكون "Clicked".

```objectivec
- (IBAction)clearButtonClicked:(id)sender {
    RIGSetting *setting = [RIGSetting settingForGitPath:self.gitRepo.localPath];
    NSString *defaultRepo = setting.defaultRepo;
    if (defaultRepo == nil) {
        [RIGUtils showMessage:@"There's no default repo setting."];
    } else {
        setting.defaultRepo = nil;
        [RIGUtils showMessage:[NSString stringWithFormat:@"Succeed to clear current default repo(%@) setting. In the next time to open github, will ask you to select new default repo.", defaultRepo]];
    }
}
```

- **زر المسح**: يستهدف إعدادًا محددًا للمشروع عبر `settingForGitPath` (يفترض أن `self.gitRepo` متاح، ربما تم تعيينه في مكان آخر). يمسح `defaultRepo` (على سبيل المثال، عنوان GitHub الاحتياطي). ينبه إذا لم يتم تعيين أي مستودع، أو يؤكد المسح مع التفاصيل.

ملاحظة: `self.gitRepo` غير مُعلن عنه هنا - من المحتمل أنه خاصية من فئة أصلية أو فئة فرعية.

```objectivec
- (IBAction)resetMenusButtonClicked:(id)sender {
    [[RIGSetting setting] setConfigs:[RIGSetting defaultConfigs]];
    [self reloadConfigs];
}
```

- **زر إعادة التعيين**: يستبدل الإعدادات بالإعدادات الافتراضية للتطبيق (من `RIGSetting`)، ثم يعيد تحميل واجهة المستخدم. لا يوجد مربع حوار تأكيد - إجراء مباشر.

### تحسينات/ملاحظات محتملة

- **سير عمل واجهة المستخدم**: النافذة غير نمطية (لا توجد استدعاءات صريحة لعرضها هنا)، لذلك يتم عرضها على الأرجح عبر `[controller showWindow:sender]`. التغييرات تتطلب إعادة تشغيل Xcode بسبب طبيعة الإضافة.
- **التحقق من الصحة**: يعتمد على `RIGConfig.isValid`، والذي لم يتم عرضه - من المحتمل أنه يضمن أن الحقول المطلوبة مثل العنوان والنمط غير فارغة.
- **الحالات الطارئة**: الحشو إلى 10 يفترض واجهة مستخدم ثابتة؛ يمكن أن يستخدم تغيير الحجم الديناميكي الدالة المعلقة `updateConfigsViewHeight`. لا يوجد تراجع/تأكيد لإعادة التعيين/المسح.
- **التبعيات**: مرتبطة بشدة بنماذج التطبيق (`RIGConfig`, `RIGSetting`) - الفهم الكامل يتطلب رؤوس تلك الفئات.

هذا الكود من عام 2015، لذلك يستخدم أنماط Cocoa القديمة (على سبيل المثال، إعداد الإطار يدويًا بدلاً من Auto Layout). بالنسبة لـ SwiftUI الحديثة، سيكون `View` مع `@State` للإعدادات.