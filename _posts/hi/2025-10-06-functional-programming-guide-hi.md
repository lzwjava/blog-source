---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: जावा फंक्शनल प्रोग्रामिंग गाइड
translated: true
type: note
---

जावा ने जावा 8 के बाद से फंक्शनल प्रोग्रामिंग सिद्धांतों को अपनाया है, जिसमें लैम्बडा, स्ट्रीम्स और अन्य फीचर्स शामिल हैं जो कोड को अधिक संक्षिप्त, पठनीय और डिक्लेरेटिव बनाते हैं। यह गाइड मूल से लेकर उन्नत अवधारणाओं को कवर करती है, और यह मानती है कि आपको कोर जावा की जानकारी है। हम जावा 8+ सिंटैक्स का उपयोग करेंगे, क्योंकि ये फीचर्स तभी शुरू हुए थे। उदाहरणों को आसानी से कॉपी करने के लिए जावा कोड ब्लॉक्स में दिखाया गया है।

## 1. जावा में फंक्शनल प्रोग्रामिंग का परिचय

फंक्शनल प्रोग्रामिंग (FP) इन पर जोर देती है:
- **शुद्ध फंक्शन**: ऐसे फंक्शन जिनका कोई साइड इफेक्ट नहीं होता (जैसे, कोई परिवर्तनशील स्टेट परिवर्तन नहीं)।
- **अपरिवर्तनीयता**: डेटा एक बार बनने के बाद नहीं बदलता।
- **हायर-ऑर्डर फंक्शन**: ऐसे फंक्शन जो अन्य फंक्शन्स को लेते हैं या वापस करते हैं।
- **डिक्लेरेटिव स्टाइल**: *क्या* करना है, इस पर ध्यान दें, *कैसे* करना है पर नहीं (जैसे, लूप्स के बजाय स्ट्रीम्स के माध्यम से)।

जावा हास्केल जैसा विशुद्ध रूप से फंक्शनल नहीं है, लेकिन यह FP को अपनी ऑब्जेक्ट-ओरिएंटेड जड़ों के साथ मिलाता है। प्रमुख सक्षम करने वाले:
- लैम्बडा एक्सप्रेशन (अनाम फंक्शन)।
- फंक्शनल इंटरफेस (एक अमूर्त विधि वाले इंटरफेस)।
- कलेक्शन्स को फंक्शनल तरीके से प्रोसेस करने के लिए स्ट्रीम्स API।

लाभ: बॉयलरप्लेट कोड में कमी, समानांतरता में आसानी, बेहतर कंपोज़ेबिलिटी।

## 2. लैम्बडा एक्सप्रेशन

लैम्बडा छोटे, एक-बार के इम्प्लीमेंटेशन के लिए उपयोग किए जाने वाले अनाम फंक्शन हैं। ये जावा में FP का प्रवेश द्वार हैं।

### बेसिक सिंटैक्स
एक लैम्बडा है: `(पैरामीटर्स) -> { बॉडी }`
- सिंगल पैरामीटर के लिए कोष्ठक वैकल्पिक।
- सिंगल एक्सप्रेशन के लिए ब्रेसिज़ वैकल्पिक (अंतर्निहित रिटर्न)।
- टाइप इनफेरेंस अक्सर काम कर जाता है, लेकिन आप टाइप्स निर्दिष्ट कर सकते हैं।

```java
// पारंपरिक अनाम इनर क्लास
Runnable r = new Runnable() {
    @Override
    public void run() {
        System.out.println("Hello, World!");
    }
};

// लैम्बडा समकक्ष
Runnable lambda = () -> System.out.println("Hello, World!");
lambda.run();
```

### पैरामीटर्स के साथ
```java
// बाइनरी ऑपरेटर उदाहरण
BinaryOperator<Integer> add = (a, b) -> a + b;
System.out.println(add.apply(2, 3)); // 5

// मल्टी-लाइन बॉडी
Comparator<String> comparator = (s1, s2) -> {
    int lenDiff = s1.length() - s2.length();
    return lenDiff != 0 ? lenDiff : s1.compareTo(s2);
};
```

### वेरिएबल्स को कैप्चर करना (इफेक्टिवली फाइनल)
लैम्बडा बाहरी वेरिएबल्स तक पहुंच सकते हैं, लेकिन वे **इफेक्टिवली फाइनल** होने चाहिए (दोबारा असाइन नहीं किए गए)।
```java
int threshold = 10;
Predicate<Integer> isHigh = x -> x > threshold; // OK
// threshold = 20; // Error: not effectively final
```

## 3. फंक्शनल इंटरफेस

एक फंक्शनल इंटरफेस में बिल्कुल एक अमूर्त विधि (SAM - Single Abstract Method) होती है। जावा `java.util.function` में बिल्ट-इन प्रदान करता है।

### बिल्ट-इन उदाहरण
- `Predicate<T>`: `boolean test(T t)`
- `Function<T, R>`: `R apply(T t)`
- `Consumer<T>`: `void accept(T t)`
- `Supplier<T>`: `T get()`
- `BiFunction<T, U, R>`, आदि, दो इनपुट के लिए।

कस्टम:
```java
@FunctionalInterface  // वैकल्पिक, लेकिन अच्छा अभ्यास
interface Transformer {
    String transform(String input);
}

Transformer upper = s -> s.toUpperCase();
System.out.println(upper.transform("java")); // JAVA
```

SAM को लागू करने के लिए `@FunctionalInterface` का उपयोग करें।

### डिफॉल्ट और स्टैटिक विधियाँ
फंक्शनल इंटरफेस में डिफॉल्ट (जावा 8+) हो सकते हैं, जैसे `Optional.orElse()`।
```java
default int compare(String a, String b) { ... } // अनुमति है
static void utility() { ... } // अनुमति है
```

## 4. मेथड रेफरेंस

मौजूदा विधियों को इनवोक करने वाले लैम्बडा के लिए शॉर्टहैंड। सिंटैक्स: `Class::method` या `instance::method`।

प्रकार:
- स्टैटिक: `Class::staticMethod`
- विशिष्ट प्रकार का इंस्टेंस: `Class::instanceMethod`
- किसी भी ऑब्जेक्ट का इंस्टेंस: `object::instanceMethod`
- कंस्ट्रक्टर: `Class::new`

उदाहरण:
```java
// Lambda: x -> System.out.println(x)
Consumer<String> printer = System.out::println;

// Static method
Function<String, Integer> length = String::length;

// Instance method
List<String> list = Arrays.asList("a", "b");
list.forEach(System.out::println); // Prints each

// Constructor
Supplier<List<String>> listSupplier = ArrayList::new;
```

## 5. स्ट्रीम्स API

स्ट्रीम्स कलेक्शन्स को डिक्लेरेटिव तरीके से प्रोसेस करती हैं: बनाएं → ट्रांसफॉर्म → कलेक्ट। लेज़ी एवल्यूएशन (इंटरमीडिएट ऑपरेशन तब तक नहीं चलते जब तक टर्मिनल ऑप नहीं चलता)।

### स्ट्रीम्स बनाना
```java
import java.util.*;
import java.util.stream.*;

List<String> names = Arrays.asList("Alice", "Bob", "Charlie");

// कलेक्शन से
Stream<String> stream = names.stream();

// ऐरे से
String[] arr = {"x", "y"};
Stream<String> arrStream = Arrays.stream(arr);

// अनंत
Stream<Integer> infinite = Stream.iterate(0, n -> n + 1);
```

### इंटरमीडिएट ऑपरेशन (लेज़ी)
उन्हें चेन करें; टर्मिनल तक कोई कम्प्यूटेशन नहीं।
- `filter(Predicate)`: मेल खाने वाले एलिमेंट्स रखें।
- `map(Function)`: प्रत्येक को ट्रांसफॉर्म करें।
- `flatMap(Function<? super T, ? extends Stream<? extends R>>)`: नेस्टेड स्ट्रीम्स को फ्लैटन करें।
- `distinct()`, `sorted()`, `limit(n)`, `skip(n)`।

```java
List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);
List<Integer> evensSquared = numbers.stream()
    .filter(n -> n % 2 == 0)
    .map(n -> n * n)
    .collect(Collectors.toList()); // [4, 16]
```

### टर्मिनल ऑपरेशन (ईगर)
कम्प्यूटेशन शुरू करते हैं और एक परिणाम लौटाते हैं।
- `collect(Collector)`: लिस्ट, सेट, मैप में।
- `forEach(Consumer)`: साइड-इफेक्ट (यदि संभव हो तो टालें)।
- `reduce()`: एकत्रित करें (जैसे, योग)।
- `anyMatch()`, `allMatch()`, `findFirst()`।

```java
// Reduce: sum
int sum = numbers.stream().reduce(0, Integer::sum); // 15

// Collect to map
Map<String, Integer> nameLengths = Stream.of("Alice", "Bob")
    .collect(Collectors.toMap(s -> s, String::length)); // {Alice=5, Bob=3}

// Grouping
Map<Integer, List<String>> byLength = names.stream()
    .collect(Collectors.groupingBy(String::length)); // {5=[Alice, Charlie], 3=[Bob]}
```

### पैरेलल स्ट्रीम्स
समानांतरता के लिए: `parallelStream()` या `.parallel()`। सावधानी से उपयोग करें (डीबगिंग कठिन)।
```java
long count = names.parallelStream().count(); // 3
```

## 6. कलेक्टर्स

`java.util.stream.Collectors` से। जटिल रिडक्शन बनाएं।

सामान्य:
- `toList()`, `toSet()`, `toMap()`
- `joining()`: स्ट्रिंग्स को जोड़ें।
- `summingInt()`, `averagingDouble()`
- `groupingBy()`, `partitioningBy()`
- `collectingAndThen()`: पोस्ट-प्रोसेस।

```java
// लंबाई के आधार पर अधिकतम के लिए कस्टम कलेक्टर
String longest = names.stream()
    .collect(Collectors.maxBy(Comparator.comparingInt(String::length)))
    .orElse(""); // "Charlie"

// इवेंस/ऑड्स का पार्टीशन
Map<Boolean, List<Integer>> partitions = numbers.stream()
    .collect(Collectors.partitioningBy(n -> n % 2 == 0));
```

## 7. ऑप्शनल

`NullPointerException` से बचाता है संभावित रूप से नल वैल्यू को रैप करके। स्पष्ट नल हैंडलिंग को प्रोत्साहित करता है।

निर्माण:
- `Optional.of(value)`: नॉन-नल।
- `Optional.ofNullable(value)`: नल → खाली।
- `Optional.empty()`।

ऑपरेशन:
- `isPresent()`, `ifPresent(Consumer)`
- `orElse(default)`, `orElseThrow()`
- `map()`, `flatMap()` चेनिंग के लिए।

```java
Optional<String> opt = Optional.ofNullable(getName()); // मान लें नल लौटा सकता है

String name = opt.orElse("Unknown");
opt.ifPresent(System.out::println);

String upper = opt.map(String::toUpperCase).orElse("DEFAULT");
```

स्ट्रीम्स अक्सर `Optional` लौटाती हैं (जैसे, `findFirst()`)।

## 8. उन्नत विषय

### कंपोज़ेबल फंक्शन
चेनिंग के लिए `Function.andThen()`, `Function.compose()`।
```java
Function<String, Integer> len = String::length;
Function<Integer, String> toStr = i -> "Len: " + i;

Function<String, String> chain = len.andThen(toStr);
System.out.println(chain.apply("Java")); // Len: 4
```

### रिकर्सन और टेल कॉल
जावा में ऑप्टिमाइजेशन की कमी है, लेकिन इटरेटिव रिकर्सन के लिए `Stream.iterate()` का उपयोग करें।

### अपरिवर्तनीयता सहायक
`Collections.unmodifiableList()` या गुआवा/इम्यूटेबल कलेक्शन जैसी लाइब्रेरीज़ का उपयोग करें (हालांकि जावा 10+ के साथ `List.of()` बिल्ट-इन है)।

`List.of("a", "b")` अपरिवर्तनीय लिस्ट बनाता है (जावा 9+)।

### पैटर्न मैचिंग (जावा 21+ प्रीव्यू/स्टेबल)
स्विच में डीस्ट्रक्चरिंग के साथ FP को बढ़ाता है।
```java
// Preview feature; enable with --enable-preview
String desc = switch (obj) {
    case Integer i -> "int: " + i;
    case String s -> "str: " + s.length();
    default -> "unknown";
};
```

### वर्चुअल थ्रेड्स (जावा 21+)
कंकरंट स्ट्रीम्स के लिए लाइटवेट थ्रेड्स के साथ FP चमकता है।

## 9. सर्वोत्तम अभ्यास

- **अपरिवर्तनीयता को प्राथमिकता दें**: फाइनल फील्ड्स का उपयोग करें, कलेक्शन्स को बदलने से बचें।
- **साइड इफेक्ट्स से बचें**: लैम्बडा को शुद्ध रखें; साइड इफेक्ट्स केवल `forEach` या स्पष्ट कंज्यूमर्स में हों।
- **स्ट्रीम्स बनाम लूप्स**: पठनीयता के लिए स्ट्रीम्स का उपयोग करें; परफॉर्मेंस-क्रिटिकल कोड के लिए लूप्स का।
- **नल**: नल चेक्स पर `Optional` को प्राथमिकता दें।
- **टेस्टिंग**: लैम्बडा के साथ फंक्शनल इंटरफेस को आसानी से मॉक करें।
- **परफॉर्मेंस**: स्ट्रीम्स में ओवरहेड होता है; पैरेलल का उपयोग करने से पहले प्रोफाइल करें।
- **पठनीयता**: छोटे लैम्बडा ठीक हैं; जटिल लॉजिक के लिए मेथड्स निकालें।

सामान्य गलतियाँ:
- लैम्बडा में बाहरी स्टेट को मॉडिफाई करना।
- टर्मिनल ऑपरेशन भूल जाना (स्ट्रीम्स कुछ नहीं करती!)।
- पैरेलल स्ट्रीम्स का अत्यधिक उपयोग (हमेशा तेज़ नहीं)।

## 10. उदाहरण: फंक्शनल पाइपलाइन

कर्मचारियों की एक सूची को फंक्शनल तरीके से प्रोसेस करें।

```java
import java.util.*;
import java.util.stream.Collectors;

class Employee {
    String name;
    int salary;
    Department dept;

    Employee(String name, int salary, Department dept) {
        this.name = name;
        this.salary = salary;
        this.dept = dept;
    }
}

enum Department { ENG, HR }

public class FunctionalExample {
    public static void main(String[] args) {
        List<Employee> employees = Arrays.asList(
            new Employee("Alice", 50000, Department.ENG),
            new Employee("Bob", 60000, Department.HR),
            new Employee("Charlie", 55000, Department.ENG)
        );

        // High-paid engineers' names, sorted
        List<String> result = employees.stream()
            .filter(e -> e.dept == Department.ENG)
            .filter(e -> e.salary > 52000)
            .map(Employee::getName)  // Assume getter
            .sorted()
            .collect(Collectors.toList());

        System.out.println(result); // [Charlie]
    }
}
```

## निष्कर्ष

लैम्बडा और FP जावा को इम्पेरेटिव से एक्सप्रेसिव में बदल देते हैं। सरल प्रतिस्थापन (जैसे, लूप्स पर `forEach`) से शुरुआत करें, फिर पाइपलाइन बनाएं। महारत के लिए वास्तविक प्रोजेक्ट्स पर अभ्यास करें। गहराई से जानने के लिए, एक IDE में प्रयोग करें।

### संदर्भ
- [Oracle Java Tutorials: Lambda Expressions](https://docs.oracle.com/javase/tutorial/java/javaOO/lambdaexpressions.html)
- [Baeldung: Java 8 Functional Interfaces](https://www.baeldung.com/java-functional-interfaces)
- [Java Streams Guide](https://www.baeldung.com/java-8-streams)
- [Effective Java (3rd Ed.) - Item 42-45 on Lambdas](https://www.oreilly.com/library/view/effective-java-3rd/9780134686097/)