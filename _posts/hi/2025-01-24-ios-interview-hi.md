---
audio: false
generated: false
lang: hi
layout: post
title: iOS Engineer Interview का साक्षात्कार
translated: true
---

### SwiftUI

1. SwiftUI क्या है और यह UIKit से कैसे अलग है?
   - SwiftUI Apple की modern framework है जो user interfaces बनाने के लिए declarative syntax provide करता hai, jo UIKit ke imperative approach se alag hai. Yeh UI creation aur updates ko simplify karta hai.

2. SwiftUI mein declarative UI ka concept kya hai?
   - Declarative UI desired outcome ko describe karta hai, nahi ki usse achieve karne ke steps. SwiftUI UI ko build aur update karta hai declared state ke basis par.

3. SwiftUI mein custom view kaise banate hain?
   - Ek naya struct banaye jo `View` protocol ko conform karta hai aur uske content ko `body` property mein define kare.

4. SwiftUI ko UIKit ke upar use karne ke benefits kya hain?
   - Benefits mein declarative syntax, easier state management, aur macOS, iOS, aur doosre Apple platforms ke liye unified interface shamil hain.

5. SwiftUI mein state management kaise handle karta hai?
   - `@State` local state ke liye, `@ObservedObject` observable classes ke liye, aur `@EnvironmentObject` global state ke liye use kare.

6. `@State` aur `@Binding` ke beech ka difference kya hai?
   - `@State` local state management ke liye use hota hai, jabki `@Binding` state ko views ke beech share karne ke liye use hota hai.

7. SwiftUI mein `@EnvironmentObject` kaise use kare?
   - `@EnvironmentObject` use hota hai ek object ko access karne ke liye jo view hierarchy ke through pass kiya gaya hai.

8. `@ObservedObject` aur `@StateObject` ka purpose kya hai?
   - `@ObservedObject` object mein changes ko observe karta hai, jabki `@StateObject` object ke lifecycle ko manage karta hai.

9. SwiftUI mein view animations kaise handle kare?
   - Animation modifiers jaise `.animation()` ya `withAnimation {}` use kare UI changes ko animate karne ke liye.

10. `ViewBuilder` aur `@ViewBuilder` ke beech ka difference kya hai?
    - `ViewBuilder` ek protocol hai views ko build karne ke liye, jabki `@ViewBuilder` ek property wrapper hai jo views return karne wale functions ke liye hai.

### CocoaPods and Dependencies

11. CocoaPods kya hai aur iska iOS development mein kaise use hota hai?
    - CocoaPods ek dependency manager hai Swift aur Objective-C Cocoa projects ke liye, jo library integration ko simplify karta hai.

12. CocoaPods kaise install kare?
    - Ruby gem ke through install kare: `sudo gem install cocoapods`.

13. Podfile kya hai aur iska kaise configure kare?
    - Ek Podfile project dependencies ko list karta hai. Configure kare by specifying pods aur unke versions.

14. CocoaPods ka use karke apne project mein ek dependency kaise add kare?
    - Pod ko Podfile mein add kare aur `pod install` run kare.

15. `pod install` aur `pod update` ke beech ka difference kya hai?
    - `pod install` dependencies ko specified ke hisaab se install karta hai, jabki `pod update` latest versions tak update karta hai.

16. Alag-alag pods ke beech conflicts kaise resolve kare?
    - Compatible pod versions ka use kare ya Podfile mein versions specify kare.

17. Carthage kya hai aur iska CocoaPods se kaise alag hai?
    - Carthage bhi ek dependency manager hai jo libraries ko build aur link karta hai bina project mein deeply integrate hone ke.

18. Alag-alag build configurations ke liye alag-alag pods kaise manage kare?
    - Podfile mein conditional statements ka use kare build configurations ke basis par.

19. Podspec file kya hai aur iska kaise use hota hai?
    - Ek podspec file pod ke version, source, dependencies, aur doosre metadata ko describe karta hai.

20. CocoaPods ke saath issues kaise troubleshoot kare?
    - Pod versions check kare, project ko clean kare, aur CocoaPods issue tracker ko consult kare.

### UI Layout

21. iOS mein responsive layout kaise banate hain?
    - Auto Layout aur constraints ka use kare taaki views alag-alag screen sizes ko adapt kare.

22. `Stack View` aur `Auto Layout` ke beech ka difference kya hai?
    - Stack Views views ko row ya column mein layout karne ko simplify karta hai, jabki Auto Layout precise control provide karta hai positioning ke liye.

23. iOS mein `UIStackView` kaise use kare?
    - Views ko ek Stack View mein add kare aur uske axis, distribution, aur alignment ko configure kare.

24. iOS mein `frame` aur `bounds` ke beech ka difference kya hai?
    - `frame` view ke position aur size ko define karta hai uske superview ke relative, jabki `bounds` view ke own coordinate system ko define karta hai.

25. iOS mein alag-alag screen sizes aur orientations kaise handle kare?
    - Auto Layout aur size classes ka use kare taaki UI alag-alag devices aur orientations ko adapt kare.

26. iOS mein `Auto Layout` constraints kaise use kare?
    - Views ke beech constraints set kare taaki unke relationships aur positions ko define kare.

27. Auto Layout mein `leading` aur `trailing` ke beech ka difference kya hai?
    - Leading aur trailing text direction ko adapt karta hai, jabki left aur right nahi.

28. iOS mein custom layout kaise banate hain?
    - `UIView` ko subclass kare aur `layoutSubviews()` ko override kare taaki subviews ko manually position kare.

29. `UIPinchGestureRecognizer` aur `UIRotationGestureRecognizer` kaise use kare?
    - Gesture recognizers ko views ke saath attach kare aur unke actions ko delegate methods mein handle kare.

30. Alag-alag device types (iPhone, iPad) ke liye layout changes kaise handle kare?
    - Size classes aur adaptive layouts ka use kare taaki UI alag-alag devices ke liye adjust ho sake.

### Swift

31. Swift aur Objective-C ke beech key differences kya hain?
    - Swift safer, concise, aur modern language features jaise closures aur generics ko support karta hai.

32. Swift mein optionals ka concept kya hai?
    - Optionals values ko represent karte hain jo `nil` ho sakte hain, jo ki value ke absence ko indicate karta hai.

33. `nil` aur `optional` ke beech ka difference kya hai?
    - `nil` value ke absence ko indicate karta hai, jabki ek optional ya to value hold karta hai ya `nil`.

34. Swift mein errors kaise handle kare?
    - `do-catch` blocks ka use kare ya errors ko propagate kare `throw` ke through.

35. `let` aur `var` ke beech ka difference kya hai?
    - `let` constants ko declare karta hai, jabki `var` variables ko declare karta hai jo modify kiya ja sake.

36. Swift mein class aur struct ke beech ka difference kya hai?
    - Classes inheritance ko support karte hain aur reference types hain, jabki structs value types hain.

37. Swift mein enum kaise banate hain?
    - `enum` keyword ke saath enum define kare aur cases define kare jo associated values rakh sakte hain.

38. Swift mein protocol-oriented programming ka concept kya hai?
    - Protocols methods, properties, aur requirements define karte hain jo conforming types implement karne hain.

39. Protocol aur delegate ke beech ka difference kya hai?
    - Protocols methods define karte hain, jabki delegates specific interactions ke liye protocol methods implement karte hain.

40. Swift mein generics kaise use kare?
    - Generic types ka use kare flexible, reusable code likhne ke liye jo any data type ke saath kaam kare.

### Networking

41. iOS mein network requests kaise handle kare?
    - URLSession ke liye network tasks ke liye ya libraries jaise Alamofire ke liye higher-level abstractions ke liye use kare.

42. URLSession kya hai?
    - URLSession network requests handle karta hai, providing data tasks, upload tasks, aur download tasks.

43. Swift mein JSON parsing kaise handle kare?
    - `Codable` protocol ka use kare JSON data ko Swift structs ya classes mein decode karne ke liye.

44. Synchronous aur asynchronous requests ke beech ka difference kya hai?
    - Synchronous requests calling thread ko block karta hai, jabki asynchronous requests nahi.

45. Background thread par network requests kaise manage kare?
    - GCD ya OperationQueue ka use kare requests ko main thread se baahar perform karne ke liye.

46. Alamofire kya hai aur iska URLSession se kaise alag hai?
    - Alamofire ek third-party networking library hai jo HTTP requests ko simplify karta hai URLSession se.

47. Network errors aur retries kaise handle kare?
    - Error handling ko completion handlers mein implement kare aur transient errors ke liye retry mechanisms ko consider kare.

48. `URLSessionDataDelegate` methods kaise use kare?
    - Delegate methods ko implement kare taaki request progress, authentication, aur aur handle kare.

49. GET aur POST requests ke beech ka difference kya hai?
    - GET data ko retrieve karta hai, jabki POST data ko server par send karta hai taaki resources create ya update kare.

50. Network communications ko secure kaise kare?
    - HTTPS ka use kare data ko transit mein encrypt karne ke liye aur certificates ko properly handle kare.

### Best Practices and Problem Solving

51. Apne projects mein code quality kaise ensure kare?
    - Linting tools ka use kare, unit tests likhe, aur coding standards follow kare.

52. SwiftUI view kaise debug kare?
    - Xcode ke debugging tools, preview canvas, aur print statements ka use kare issues ko identify karne ke liye.

53. App performance ko optimize karne ke liye kaise strategies use kare?
    - App ko profile kare Instruments ke through, data fetching optimize kare, aur UI layer counts ko reduce kare.

54. Swift mein memory management kaise handle kare?
    - ARC (Automatic Reference Counting) ka use kare aur retain cycles se bach kare.

55. Legacy code ko refactor karne ka approach kya hai?
    - Code smells ko identify kare, tests likhe, aur incrementally refactor kare.

56. CI/CD pipelines ke saath ka experience kya hai?
    - Pipelines ko set up kare tools jaise Jenkins, GitHub Actions, ya Fastlane ke through automated builds aur deployments ke liye.

57. Latest iOS developments ke saath updated kaise rahe?
    - Apple ke developer resources ko follow kare, conferences attend kare, aur developer communities mein participate kare.

58. Ek difficult bug ko solve karne ka ek example describe kare.
    - Identifying, isolating, aur fixing issue ke process ko describe kare.

59. Version control ka approach kya hai?
    - Git ka use kare branching, committing, aur collaborating ke liye effectively.

60. Deadlines aur pressure ko handle karne ka approach kya hai?
    - Tasks ko prioritize kare, effectively communicate kare, aur time ko efficiently manage kare.