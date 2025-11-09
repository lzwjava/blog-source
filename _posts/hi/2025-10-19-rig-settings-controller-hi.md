---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: आरआईजी सेटिंग्स विंडो नियंत्रक अवलोकन
translated: true
type: note
---

### अवलोकन

यह Objective-C कोड `RIGSettingWindowController` क्लास को लागू करता है, जो "Reveal-In-GitHub" (RIG) macOS ऐप (संभवतः GitHub रिपॉजिटरी में चयनित कोड को जल्दी से दिखाने के लिए एक Xcode प्लगइन) के लिए एक सेटिंग्स विंडो प्रबंधित करता है। यह विंडो उपयोगकर्ताओं को विभिन्न GitHub रिपॉजिटरी के लिए कस्टम मेनू आइटम, कीबोर्ड शॉर्टकट और regex पैटर्न कॉन्फ़िगर करने की अनुमति देती है। यह UI स्थिरता के लिए 10 कॉन्फ़िग स्लॉट (UI स्थिरता के लिए खाली स्थानों से पैड किए गए) प्रदर्शित और संपादित करने के लिए एक टेबल-जैसे दृश्य (`RIGConfigCellsView`) का उपयोग करता है।

क्लास `NSTableViewDataSource` और `NSTableViewDelegate` प्रोटोकॉल का पालन करती है, जो सुझाव देता है कि यह कस्टम सेल्स दृश्य के अंदर एक टेबल व्यू के लिए डेटा और इवेंट्स को संभालती है। यह दृढ़ता (persistence) के लिए `RIGSetting` और UI फीडबैक के लिए `RIGUtils` जैसे ऐप-व्यापी सिंगलटन के साथ एकीकृत होती है।

मुख्य जिम्मेदारियां:
- कॉन्फ़िगरेबल आइटम (जैसे, मेनू शीर्षक, शॉर्टकट कुंजियाँ, regex पैटर्न) लोड और प्रदर्शित करना।
- परिवर्तनों को मान्य करना और सहेजना।
- सहेजने, डिफ़ॉल्ट रिपो सेटिंग्स साफ़ करने और डिफ़ॉल्ट पर रीसेट करने के लिए बटन प्रदान करना।

### इम्पोर्ट्स और डिफाइन

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

- इम्पोर्ट्स इस क्लास के हेडर, कॉन्फ़िग पंक्तियों को रेंडर करने के लिए एक कस्टम व्यू (`RIGConfigCellsView`), मॉडल ऑब्जेक्ट (व्यक्तिगत सेटिंग्स के लिए `RIGConfig`, ऐप-व्यापी स्टोरेज के लिए `RIGSetting`), और यूटिलिटीज (अलर्ट के लिए `RIGUtils`, संभवतः प्लगइन लाइफसाइकिल के लिए `RIGPlugin`) को शामिल करते हैं।
- डिफाइन विंडो के अंदर कॉन्फ़िग व्यू के पूर्ण-चौड़ाई लेआउट के लिए शून्य मार्जिन सेट करते हैं।

### प्राइवेट इंटरफेस

```objectivec
@interface RIGSettingWindowController ()<NSTableViewDataSource, NSTableViewDelegate>

@property (nonatomic, strong) NSArray *configs;
@property (nonatomic, strong) RIGConfigCellsView *configCellsView;
@property (weak) IBOutlet NSView *mainView;
@property (weak) IBOutlet NSView *configsView;

@end
```

- आंतरिक गुणों और प्रोटोकॉल अनुपालन के लिए एक प्राइवेट एक्सटेंशन घोषित करता है।
- `configs`: उपयोगकर्ता की सेटिंग्स (जैसे, मेनू शीर्षक, अंतिम दबाई गई कुंजी, regex पैटर्न) रखने वाली `RIGConfig` ऑब्जेक्ट्स की सरणी।
- `configCellsView`: कॉन्फ़िग्स को संपादन योग्य पंक्तियों के रूप में रेंडर करने वाला कस्टम व्यू (संभवतः एक स्क्रॉल करने योग्य टेबल या कोशिकाओं का ढेर)।
- `mainView` और `configsView`: स्टोरीबोर्ड/निब फ़ाइल में कंटेनर व्यू के लिए IBOutlets; `configsView` डायनामिक सेल्स को होस्ट करता है।

### इम्प्लीमेंटेशन

#### इनिशियलाइज़ेशन मेथड्स

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

- `awakeFromNib`: खाली ओवरराइड; कहलाया जाता है जब विंडो निब (स्टोरीबोर्ड) से लोड होती है। बस सुपरक्लास को चेन करता है।
- `windowDidLoad`: विंडो के पूरी तरह से लोड होने के बाद कोर सेटअप।
  - `displayConfigs` के माध्यम से `configs` लोड करता है (नीचे समझाया गया है)।
  - `configCellsView` को एक फ्रेम के साथ बनाता है जो `configsView` को क्षैतिज रूप से (मार्जिन का उपयोग करके) और लंबवत रूप से सभी कॉन्फ़िग्स के लिए आवश्यक कुल ऊंचाई के आधार पर भरता है (`RIGConfigCellsView` क्लास मेथड द्वारा गणना की गई)।
  - कॉन्फ़िग्स को व्यू को असाइन करता है, इसे एक सबव्यू के रूप में जोड़ता है, और डेटा रीलोड को ट्रिगर करता है (संभवतः टेबल सेल्स को ताज़ा करता है)।

`updateConfigsViewHeight` का एक कमेंट-आउट किया गया कॉल है, जो सुझाव देता है कि डायनामिक रीसाइज़िंग पर विचार किया गया था लेकिन अक्षम कर दिया गया था—संभवतः क्योंकि सेल्स व्यू स्वतः आकार लेता है या विंडो निश्चित है।

```objectivec
- (void)updateConfigsViewHeight {
    CGRect frame = self.configsView.frame;
    frame.size.height = CGRectGetHeight(self.configCellsView.frame);
    self.configsView.frame = frame;
}
```

- `configsView` का आकार सेल्स व्यू की ऊंचाई से मेल खाने के लिए बदलने की उपयोगिता। वर्तमान में उपयोग नहीं किया गया है, लेकिन अधिक कॉन्फ़िग जोड़े जाने पर विंडो को स्वतः बढ़ने के लिए इस्तेमाल किया जा सकता था।

#### कॉन्फ़िग मैनेजमेंट

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

- ऐप के सिंगलटन `RIGSetting` से मौजूदा कॉन्फ़िग्स को लोड करता है।
- सरणी को ठीक 10 आइटमों के साथ खाली `RIGConfig` इंस्टेंस से पैड करता है। यह एक सुसंगत UI सुनिश्चित करता है (जैसे, 10 संपादन योग्य पंक्तियाँ), भले ही उपयोगकर्ता के पास कम सहेजे गए कॉन्फ़िग हों। खाली वाले सेव पर फ़िल्टर कर दिए जाते हैं।

```objectivec
- (void)reloadConfigs {
    self.configs = [self displayConfigs];
    self.configCellsView.configs = self.configs;
    [self.configCellsView reloadData];
}
```

- स्टोरेज से प्रदर्शित कॉन्फ़िग्स को ताज़ा करता है और व्यू को अपडेट करता है। रीसेट के बाद उपयोग किया जाता है।

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

- कॉन्फ़िग्स पर पुनरावृति करता है और प्रत्येक पर `isValid` को कॉल करता है (संभवतः गैर-खाली `menuTitle` और `pattern` की जांच करता है)। केवल तभी `YES` लौटाता है यदि सभी मान्य हैं या खाली हैं (लेकिन नीचे फ़िल्टरिंग देखें)।

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

- 10-स्लॉट सरणी को केवल गैर-खाली कॉन्फ़िग्स (किसी भी फ़ील्ड में सामग्री होने के आधार पर) शामिल करने के लिए फ़िल्टर करता है। यह मान्यता/सहेजने से पहले रिक्त स्थान को हटा देता है, इसलिए `isValidConfigs` केवल वास्तविक प्रविष्टियों की जांच करता है।

#### एक्शन हैंडलर्स (IBActions)

ये UI में बटनों से इंटरफेस बिल्डर के माध्यम से जुड़े होते हैं।

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

- **सेव बटन**: कॉन्फ़िग्स को फ़िल्टर करता है, उन्हें मान्य करता है (अमान्य होने पर त्रुटि अलर्ट), फिर पूर्ण (पैड की गई) सरणी को `RIGSetting` में वापस सेव करता है। ध्यान दें: यह पूर्ण 10 स्लॉट सेव करता है, लेकिन लोड/फ़िल्टर पर रिक्त स्थान को नजरअंदाज कर दिया जाता है। सफलता संदेश दिखाता है जो Xcode रीस्टार्ट (प्लगइन रीलोड) की आवश्यकता बताता है।

मेथड नाम में टाइपो: "Clcked" का "Clicked" होना चाहिए।

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

- **क्लियर बटन**: `settingForGitPath` के माध्यम से एक प्रोजेक्ट-विशिष्ट सेटिंग को लक्षित करता है (मानता है कि `self.gitRepo` उपलब्ध है, संभवतः कहीं और सेट किया गया है)। `defaultRepo` (जैसे, एक फॉलबैक GitHub URL) साफ़ करता है। अलर्ट करता है यदि कोई सेट नहीं है, या विवरण के साथ सफलता की पुष्टि करता है।

नोट: `self.gitRepo` यहाँ घोषित नहीं है—संभवतः एक सुपरक्लास या श्रेणी से एक गुण।

```objectivec
- (IBAction)resetMenusButtonClicked:(id)sender {
    [[RIGSetting setting] setConfigs:[RIGSetting defaultConfigs]];
    [self reloadConfigs];
}
```

- **रीसेट बटन**: कॉन्फ़िग्स को ऐप डिफ़ॉल्ट (`RIGSetting` से) के साथ ओवरराइट करता है, फिर UI को रीलोड करता है। कोई पुष्टि संवाद नहीं—सीधी कार्रवाई।

### संभावित सुधार/नोट्स

- **UI फ्लो**: विंडो गैर-मोडल है (यहाँ कोई स्पष्ट शो कॉल नहीं), इसलिए यह संभवतः `[controller showWindow:sender]` के माध्यम से प्रस्तुत की जाती है। प्लगइन की प्रकृति के कारण परिवर्तनों के लिए Xcode रीस्टार्ट की आवश्यकता होती है।
- **मान्यता**: `RIGConfig.isValid` पर निर्भर करता है, जो दिखाया नहीं गया है—संभवतः आवश्यक फ़ील्ड जैसे शीर्षक और पैटर्न को गैर-खाली सुनिश्चित करता है।
- **एज केस**: 10 तक पैडिंग एक निश्चित UI मानती है; डायनामिक साइज़िंग कमेंट किए गए `updateConfigsViewHeight` का उपयोग कर सकती थी। रीसेट/क्लियर के लिए कोई पूर्ववत/पुष्टि नहीं।
- **निर्भरताएँ**: ऐप मॉडल (`RIGConfig`, `RIGSetting`) से भारी रूप से जुड़ा हुआ है—पूर्ण समझ के लिए उन हेडरों की आवश्यकता है।

यह कोड 2015 का है, इसलिए यह पुराने Cocoa पैटर्न (जैसे, ऑटो लेआउट पर मैनुअल फ्रेम सेटअप) का उपयोग करता है। आधुनिक SwiftUI के लिए, यह कॉन्फ़िग्स के लिए `@State` के साथ एक `View` होगा।