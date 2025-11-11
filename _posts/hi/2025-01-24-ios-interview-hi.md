---
audio: false
generated: false
lang: hi
layout: post
title: आईओएस इंजीनियर इंटरव्यू
translated: true
type: note
---

### SwiftUI

1. SwiftUI क्या है और यह UIKit से कैसे अलग है?
   - SwiftUI Apple का आधुनिक फ्रेमवर्क है जो यूजर इंटरफेस बनाने के लिए है, जो UIKit के imperative approach के मुकाबले declarative syntax प्रदान करता है। यह UI creation और updates को सरल बनाता है।

2. SwiftUI में declarative UI की अवधारणा को समझाएं।
   - Declarative UI वांछित परिणाम का वर्णन करती है, न कि उसे प्राप्त करने के चरणों का। SwiftUI घोषित state के आधार पर UI का निर्माण और अद्यतन करता है।

3. SwiftUI में आप एक custom view कैसे बनाते हैं?
   - `View` प्रोटोकॉल का पालन करने वाली एक नई struct बनाएं और उसकी सामग्री को `body` property के भीतर परिभाषित करें।

4. UIKit पर SwiftUI का उपयोग करने के क्या लाभ हैं?
   - लाभों में declarative syntax, आसान state management, और macOS, iOS तथा अन्य Apple प्लेटफॉर्म्स के लिए एकीकृत इंटरफेस शामिल हैं।

5. SwiftUI में आप state management को कैसे संभालते हैं?
   - स्थानीय state के लिए `@State`, observable classes के लिए `@ObservedObject`, और global state के लिए `@EnvironmentObject` का उपयोग करें।

6. `@State` और `@Binding` के बीच अंतर स्पष्ट करें।
   - `@State` का उपयोग स्थानीय state management के लिए किया जाता है, जबकि `@Binding` का उपयोग views के बीच state साझा करने के लिए किया जाता है।

7. SwiftUI में आप `@EnvironmentObject` का उपयोग कैसे करते हैं?
   - `@EnvironmentObject` का उपयोग किसी ऐसे ऑब्जेक्ट तक पहुंचने के लिए किया जाता है जो view hierarchy के माध्यम से नीचे पास किया गया हो।

8. `@ObservedObject` और `@StateObject` का उद्देश्य क्या है?
   - `@ObservedObject` किसी ऑब्जेक्ट में परिवर्तनों का अवलोकन करता है, जबकि `@StateObject` किसी ऑब्जेक्ट के lifecycle का प्रबंधन करता है।

9. SwiftUI में आप view animations को कैसे संभालते हैं?
   - UI परिवर्तनों को एनिमेट करने के लिए `.animation()` या `withAnimation {}` जैसे एनीमेशन मॉडिफायर का उपयोग करें।

10. `ViewBuilder` और `@ViewBuilder` में क्या अंतर है?
    - `ViewBuilder` views बनाने के लिए एक प्रोटोकॉल है, जबकि `@ViewBuilder` views लौटाने वाले फ़ंक्शन के लिए एक property wrapper है।

### CocoaPods और Dependencies

11. CocoaPods क्या है और इसका उपयोग iOS development में कैसे किया जाता है?
    - CocoaPods Swift और Objective-C Cocoa प्रोजेक्ट्स के लिए एक dependency manager है, जो लाइब्रेरी एकीकरण को सरल बनाता है।

12. आप CocoaPods को कैसे इंस्टॉल करते हैं?
    - Ruby gem के माध्यम से इंस्टॉल करें: `sudo gem install cocoapods`।

13. Podfile क्या है और आप इसे कैसे कॉन्फ़िगर करते हैं?
    - एक Podfile प्रोजेक्ट dependencies की सूची बनाती है। pods और उनके versions को निर्दिष्ट करके कॉन्फ़िगर करें।

14. CocoaPods का उपयोग करके आप अपने प्रोजेक्ट में एक dependency कैसे जोड़ते हैं?
    - Podfile में pod जोड़ें और `pod install` चलाएं।

15. `pod install` और `pod update` में क्या अंतर है?
    - `pod install` dependencies को निर्दिष्ट रूप में इंस्टॉल करता है, जबकि `pod update` नवीनतम versions में अपडेट करता है।

16. आप विभिन्न pods के बीच conflicts को कैसे resolve करते हैं?
    - संगत pod versions का उपयोग करें या Podfile में versions निर्दिष्ट करें।

17. Carthage क्या है और यह CocoaPods से कैसे अलग है?
    - Carthage एक अन्य dependency manager है जो प्रोजेक्ट में गहराई से एकीकृत हुए बिना libraries को बनाता और लिंक करता है।

18. आप विभिन्न build configurations के लिए अलग-अलग pods का प्रबंधन कैसे करते हैं?
    - Podfile में build configurations के आधार पर conditional statements का उपयोग करें।

19. एक podspec file क्या है और इसका उपयोग कैसे किया जाता है?
    - एक podspec file किसी pod के version, source, dependencies और अन्य metadata का वर्णन करती है।

20. आप CocoaPods से संबंधित समस्याओं का निवारण कैसे करते हैं?
    - pod versions जांचें, प्रोजेक्ट को clean करें, और CocoaPods issue tracker से सलाह लें।

### UI Layout

21. iOS में आप एक responsive layout कैसे बनाते हैं?
    - विभिन्न स्क्रीन आकारों के अनुकूल views बनाने के लिए Auto Layout और constraints का उपयोग करें।

22. `Stack View` और `Auto Layout` के बीच अंतर स्पष्ट करें।
    - Stack Views पंक्ति या स्तंभ में views को लेआउट करना सरल बनाते हैं, जबकि Auto Layout positioning पर सटीक नियंत्रण प्रदान करता है।

23. iOS में आप `UIStackView` का उपयोग कैसे करते हैं?
    - एक Stack View में views जोड़ें और इसकी axis, distribution, और alignment को कॉन्फ़िगर करें।

24. iOS में `frame` और `bounds` में क्या अंतर है?
    - `frame` view की स्थिति और आकार को उसके superview के सापेक्ष परिभाषित करता है, जबकि `bounds` view की अपनी coordinate system को परिभाषित करता है।

25. iOS में आप विभिन्न स्क्रीन आकारों और orientations को कैसे संभालते हैं?
    - विभिन्न devices और orientations के लिए UI को अनुकूल बनाने के लिए Auto Layout और size classes का उपयोग करें।

26. iOS में `Auto Layout` constraints का उपयोग कैसे करें, यह समझाएं।
    - उनके संबंधों और स्थितियों को परिभाषित करने के लिए views के बीच constraints सेट करें।

27. Auto Layout में `leading` और `trailing` में क्या अंतर है?
    - Leading और trailing text direction के अनुकूल होते हैं, जबकि left और right नहीं होते।

28. iOS में आप एक custom layout कैसे बनाते हैं?
    - `UIView` की subclass बनाएं और subviews को मैन्युअल रूप से position करने के लिए `layoutSubviews()` को override करें।

29. `UIPinchGestureRecognizer` और `UIRotationGestureRecognizer` का उपयोग कैसे करें, यह समझाएं।
    - views से gesture recognizers को जोड़ें और उनकी actions को delegate methods में हैंडल करें।

30. आप विभिन्न device types (iPhone, iPad) के लिए layout परिवर्तनों को कैसे संभालते हैं?
    - विभिन्न devices के लिए UI को समायोजित करने के लिए size classes और adaptive layouts का उपयोग करें।

### Swift

31. Swift और Objective-C के मुख्य अंतर क्या हैं?
    - Swift अधिक सुरक्षित, संक्षिप्त है और closures और generics जैसी आधुनिक भाषा सुविधाओं का समर्थन करती है।

32. Swift में optionals की अवधारणा को समझाएं।
    - Optionals उन मूल्यों का प्रतिनिधित्व करते हैं जो `nil` हो सकते हैं, जो किसी मूल्य की अनुपस्थिति को दर्शाता है।

33. `nil` और `optional` में क्या अंतर है?
    - `nil` किसी मूल्य की अनुपस्थिति है, जबकि एक optional या तो कोई मूल्य रख सकता है या `nil` हो सकता है।

34. Swift में आप errors को कैसे संभालते हैं?
    - `do-catch` ब्लॉक का उपयोग करें या `throw` का उपयोग करके errors को propagate करें।

35. `let` और `var` के बीच अंतर स्पष्ट करें।
    - `let` constants घोषित करता है, जबकि `var` ऐसे variables घोषित करता है जिन्हें संशोधित किया जा सकता है।

36. Swift में class और struct में क्या अंतर है?
    - Classes inheritance का समर्थन करते हैं और reference types हैं, जबकि structs value types हैं।

37. Swift में आप एक enum कैसे बनाते हैं?
    - `enum` कीवर्ड और cases के साथ एक enum को परिभाषित करें, जिनमें associated values हो सकती हैं।

38. Swift में protocol-oriented programming की अवधारणा को समझाएं।
    - Protocols उन methods, properties, और आवश्यकताओं को परिभाषित करते हैं जिन्हें conforming types को implement करना होगा।

39. protocol और delegate में क्या अंतर है?
    - Protocols methods को परिभाषित करते हैं, जबकि delegates विशिष्ट इंटरैक्शन के लिए protocol methods को implement करते हैं।

40. Swift में आप generics का उपयोग कैसे करते हैं?
    - किसी भी डेटा प्रकार के साथ काम करने वाले लचीले, पुन: प्रयोज्य कोड लिखने के लिए generic types का उपयोग करें।

### Networking

41. iOS में आप network requests को कैसे संभालते हैं?
    - नेटवर्क कार्यों के लिए URLSession का उपयोग करें, या higher-level abstractions के लिए Alamofire जैसी libraries का उपयोग करें।

42. URLSession क्या है?
    - URLSession नेटवर्क requests को संभालता है, जो डेटा कार्य, अपलोड कार्य और डाउनलोड कार्य प्रदान करता है।

43. Swift में आप JSON parsing को कैसे संभालते हैं?
    - JSON डेटा को Swift structs या classes में डीकोड करने के लिए `Codable` प्रोटोकॉल का उपयोग करें।

44. Synchronous और asynchronous requests के बीच अंतर स्पष्ट करें।
    - Synchronous requests calling thread को ब्लॉक करती हैं, जबकि asynchronous requests नहीं करतीं।

45. आप background thread में network requests का प्रबंधन कैसे करते हैं?
    - मुख्य thread से बाहर requests करने के लिए GCD या OperationQueue का उपयोग करें।

46. Alamofire क्या है और यह URLSession से कैसे अलग है?
    - Alamofire एक third-party नेटवर्किंग लाइब्रेरी है जो URLSession की तुलना में HTTP requests को सरल बनाती है।

47. आप network errors और retries को कैसे संभालते हैं?
    - completion handlers में error handling को implement करें और अस्थायी errors के लिए retry mechanisms पर विचार करें।

48. `URLSessionDataDelegate` methods का उपयोग कैसे करें, यह समझाएं।
    - request progress, authentication और अधिक को हैंडल करने के लिए delegate methods को implement करें।

49. GET और POST requests में क्या अंतर है?
    - GET डेटा प्राप्त करती है, जबकि POST संसाधन बनाने या अपडेट करने के लिए सर्वर पर डेटा भेजती है।

50. आप network communications को सुरक्षित कैसे करते हैं?
    - ट्रांजिट में डेटा को एन्क्रिप्ट करने के लिए HTTPS का उपयोग करें और certificates को ठीक से हैंडल करें।

### Best Practices और Problem Solving

51. आप अपने प्रोजेक्ट्स में code quality कैसे सुनिश्चित करते हैं?
    - लिंटिंग टूल्स का उपयोग करें, यूनिट टेस्ट लिखें, और coding standards का पालन करें।

52. समझाएं कि आप एक SwiftUI view को कैसे debug करेंगे।
    - मुद्दों की पहचान करने के लिए Xcode के debugging tools, preview canvas और print statements का उपयोग करें।

53. ऐप performance को optimize करने के लिए आप कौन सी strategies का उपयोग करते हैं?
    - Instruments का उपयोग करके ऐप को profile करें, डेटा फ़ेचिंग को optimize करें, और UI layer counts को कम करें।

54. Swift में आप memory management को कैसे संभालते हैं?
    - ARC (Automatic Reference Counting) का उपयोग करें और retain cycles से बचें।

55. समझाएं कि आप legacy code को refactor करने के लिए कैसे approach करेंगे।
    - code smells की पहचान करें, टेस्ट लिखें, और incremental रूप से refactor करें।

56. CI/CD pipelines के साथ आपका क्या अनुभव है?
    - स्वचालित builds और deployments के लिए Jenkins, GitHub Actions, या Fastlane जैसे टूल्स का उपयोग करके pipelines सेट करें।

57. नवीनतम iOS developments के साथ updated रहने के लिए आप क्या करते हैं?
    - Apple के developer resources को फॉलो करें, conferences में भाग लें, और developer communities में भाग लें।

58. एक ऐसे समय के बारे में समझाएं जब आपने अपने प्रोजेक्ट में एक कठिन bug को solve किया हो।
    - मुद्दे की पहचान करने, उसे अलग करने और ठीक करने की प्रक्रिया का वर्णन करें।

59. Version control के प्रति आपका approach क्या है?
    - प्रभावी ढंग से branching, committing और collaborating के लिए Git का उपयोग करें।

60. प्रोजेक्ट में deadlines और pressure को आप कैसे संभालते हैं?
    - कार्यों को प्राथमिकता दें, प्रभावी ढंग से communicate करें, और समय का कुशलतापूर्वक प्रबंधन करें।