---
audio: true
lang: hi
layout: post
title: Spring Boot Projects का विश्लेषण
translated: true
---

एक Spring Boot प्रोजेक्ट (जिसमें कई मॉड्यूल हो सकते हैं) का विश्लेषण करने और `@GetMapping` या `@PostMapping` एनोटेशन के साथ परिभाषित सभी एपीआई को निकालने के लिए, हमें प्रोजेक्ट डायरेक्टरी को ट्रैवर्स करना होगा, कंट्रोलर क्लास को पहचानना होगा, एपीआई पथ निकालना होगा और उन्हें एक निर्धारित फॉर्मेट में प्रिंट करना होगा। नीचे एक पूर्ण पाइथन स्क्रिप्ट है जो इस कार्य को पूरा करता है, जो दिए गए कोड के संरचना पर आधारित है लेकिन नए आवश्यकताओं के लिए अनुकूलित है। आउटपुट प्रत्येक कंट्रोलर के साथ उसके संबद्ध GET और POST पथ को "XXController: get path post path" फॉर्मेट में सूचीबद्ध करेगा।

### दृष्टिकोण

1. **डायरेक्टरी ट्रैवर्स करना**: प्रोजेक्ट डायरेक्टरी और उसके सबडायरेक्टरी में सभी `.java` फाइलों को पुनरावर्ती ढंग से खोजें।
2. **कंट्रोलर पहचानना**: प्रत्येक जावा फाइल में `@Controller` या `@RestController` एनोटेशन की जांच करें ताकि यह एक कंट्रोलर क्लास हो।
3. **क्लास-लेवल पथ निकालना**: क्लास लेवल पर `@RequestMapping` एनोटेशन की तलाश करें ताकि बेस पथ निर्धारित करें।
4. **मेथड-लेवल एपीआई निकालना**: `@GetMapping` या `@PostMapping` के साथ एनोटेशन वाले मेथड खोजें, उनके पथ निकालें और यदि मौजूद हों तो उन्हें बेस पथ के साथ मिलाएं।
5. **संगठित और प्रिंट करना**: प्रत्येक कंट्रोलर के लिए GET और POST पथ इकट्ठा करें और उन्हें निर्धारित फॉर्मेट में प्रिंट करें।

### पाइथन स्क्रिप्ट

```python
import os
import sys
import re
from collections import defaultdict

def find_java_files(root_dir):
    """
    दिए गए डायरेक्टरी और उसके सबडायरेक्टरी में सभी .java फाइलों को पुनरावर्ती ढंग से खोजें।

    Args:
        root_dir (str): खोज शुरू करने के लिए रूट डायरेक्टरी।

    Yields:
        str: प्रत्येक .java फाइल के पूर्ण पथ।
    """
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.java'):
                yield os.path.join(dirpath, filename)

def extract_paths(line, annotation_type):
    """
    एक स्प्रिंग एनोटेशन (@GetMapping, @PostMapping, या @RequestMapping) से पथ मूल्य निकालें।

    Args:
        line (str): एनोटेशन को रखने वाला लाइन।
        annotation_type (str): एनोटेशन का प्रकार ('GetMapping', 'PostMapping', या 'RequestMapping').

    Returns:
        list: एनोटेशन से निकाले गए पथ स्ट्रिंगों की सूची।
    """
    if annotation_type in ['GetMapping', 'PostMapping']:
        match = re.search(rf'@{annotation_type}\((.*)\)', line)
        if match:
            content = match.group(1)
            # क्वोट में सभी स्ट्रिंग लिटरल निकालें
            paths = re.findall(r'"([^"]*)"', content)
            return paths
        return []
    elif annotation_type == 'RequestMapping':
        match = re.search(r'@RequestMapping\((.*)\)', line)
        if match:
            content = match.group(1)
            # 'value' या 'path' एट्रिब्यूट की तलाश करें
            value_match = re.search(r'(value|path)\s*=\s*({[^}]*}|"[^"]*")', content)
            if value_match:
                value = value_match.group(2)
                if value.startswith('{'):
                    paths = re.findall(r'"([^"]*)"', value)
                else:
                    paths = [value.strip('"')]
                return paths
            # यदि कोई 'value' या 'path' नहीं, तो सीधे पथ निर्दिष्ट करने का मान लिया जाए
            paths = re.findall(r'"([^"]*)"', content)
            return paths
        return []

if __name__ == '__main__':
    # कमांड-लाइन अर्जुमेंट्स को पर्स करें
    if len(sys.argv) != 2:
        print("उपयोग: python script.py <root_directory>")
        sys.exit(1)

    root_dir = sys.argv[1]
    if not os.path.isdir(root_dir):
        print(f"[ERROR] निर्दिष्ट पथ एक डायरेक्टरी नहीं है: {root_dir}")
        sys.exit(1)

    print(f"[INFO] डायरेक्टरी का विश्लेषण शुरू: {root_dir}")

    # कंट्रोलर मैपिंग को स्टोर करने के लिए एक डिक्शनरी को प्रारंभ करें
    controllers = defaultdict(lambda: {'GET': [], 'POST': []})
    total_files = 0
    error_files = 0

    # सभी जावा फाइलों को प्रोसेस करें
    for java_file in find_java_files(root_dir):
        try:
            with open(java_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            # फाइल एक कंट्रोलर है कि नहीं, यह जांचें
            if any('@Controller' in line or '@RestController' in line for line in lines):
                controller_name = os.path.basename(java_file).replace('.java', '')

                # क्लास घोषणा लाइन को अलग करने के लिए क्लास घोषणा लाइन को खोजें
                class_line_index = None
                for i, line in enumerate(lines):
                    if re.search(r'public\s+(class|abstract\s+class|interface)\s+\w+', line):
                        class_line_index = i
                        break
                if class_line_index is None:
                    continue

                # क्लास-लेवल @RequestMapping को बेस पथ के रूप में निकालें
                base_paths = []
                for line in lines[:class_line_index]:
                    if re.search(r'\s*@RequestMapping', line):
                        base_paths = extract_paths(line, 'RequestMapping')
                        break
                if not base_paths:
                    base_paths = ['']

                # मेथड-लेवल @GetMapping और @PostMapping निकालें
                get_paths = []
                post_paths = []
                for line in lines[class_line_index:]:
                    if re.search(r'\s*@GetMapping', line):
                        paths = extract_paths(line, 'GetMapping')
                        for base in base_paths:
                            for path in paths:
                                full_path = base + path
                                get_paths.append(full_path)
                    elif re.search(r'\s*@PostMapping', line):
                        paths = extract_paths(line, 'PostMapping')
                        for base in base_paths:
                            for path in paths:
                                full_path = base + path
                                post_paths.append(full_path)

                # एक्सक्लूसिव पथ स्टोर करें
                get_paths = sorted(list(set(get_paths)))
                post_paths = sorted(list(set(post_paths)))

                if get_paths or post_paths:
                    controllers[controller_name]['GET'] = get_paths
                    controllers[controller_name]['POST'] = post_paths

            total_files += 1
        except Exception as e:
            print(f"[ERROR] फाइल {java_file} को पढ़ा नहीं जा सका: {e}")
            error_files += 1

    # सारांश प्रिंट करें
    print(f"[INFO] कुल जावा फाइलों का प्रयास: {total_files + error_files}")
    print(f"[INFO] सफलतापूर्वक प्रोसेस किया गया: {total_files}")
    print(f"[INFO] गलतियों वाली फाइलों: {error_files}")
    print(f"[INFO] कुल कंट्रोलर पाए गए: {len(controllers)}")

    # निर्धारित फॉर्मेट में परिणाम प्रिंट करें
    for controller, mappings in sorted(controllers.items()):
        print(f"{controller}:")
        for path in mappings['GET']:
            print(f"get {path}")
        for path in mappings['POST']:
            print(f"post {path}")
```

### व्याख्या

- **इम्पोर्ट**: हम `os` को डायरेक्टरी ट्रैवर्सल के लिए, `sys` को कमांड-लाइन अर्जुमेंट्स के लिए, `re` को रेगुलर एक्सप्रेशन के लिए, और `defaultdict` को कंट्रोलर डेटा को संगठित करने के लिए उपयोग करते हैं।
- **`find_java_files`**: यह फंक्शन प्रोजेक्ट डायरेक्टरी में सभी `.java` फाइलों को पुनरावर्ती ढंग से यील्ड करता है, `os.walk` के माध्यम से कई मॉड्यूल को स्वाभाविक रूप से संभालता है।
- **`extract_paths`**: यह फंक्शन `@GetMapping`, `@PostMapping`, या `@RequestMapping` एनोटेशन को पर्स करता है ताकि पथ मूल्य निकालें। यह संभालता है:
  - एकल पथ (जैसे, `@GetMapping("/path")`).
  - कई पथ (जैसे, `@GetMapping({"/path1", "/path2"})`).
  - नामित एट्रिब्यूट (जैसे, `@RequestMapping(value = "/path")`).
- **मुख्य तर्क**:
  - **कमांड-लाइन हैंडलिंग**: एक रूट डायरेक्टरी को इनपुट के रूप में लेता है, जैसा कि दिए गए स्क्रिप्ट में है।
  - **कंट्रोलर डिटेक्शन**: फाइल कंटेंट में `@Controller` या `@RestController` की जांच करता है।
  - **बेस पथ**: क्लास घोषणा से पहले क्लास-लेवल `@RequestMapping` पथ निकालता है।
  - **एपीआई निकालना**: क्लास घोषणा के बाद लाइनों को `@GetMapping` और `@PostMapping` के लिए प्रोसेस करता है, पथ को बेस पथ के साथ मिलाता है।
  - **आउटपुट**: प्रत्येक कंट्रोलर के साथ GET और POST पथ को एक लाइन पर प्रिंट करता है, "get" या "post" के साथ प्रीफिक्स किया गया है।
- **गलतियों का हैंडल करना**: फाइल पढ़ने के दौरान अपवादों को कैच करता है और उन्हें रिपोर्ट करता है, दिए गए कोड के रॉबस्टनेस को दर्शाता है।

### नमूना आउटपुट

एक स्प्रिंग बूट प्रोजेक्ट के साथ एक फाइल `UserController.java`:

```java
@RestController
@RequestMapping("/users")
public class UserController {
    @GetMapping("/all")
    public ResponseEntity<?> getAllUsers() { ... }

    @PostMapping("/create")
    public ResponseEntity<?> createUser() { ... }
}
```

`python script.py /path/to/project` चलाने पर:

```
[INFO] डायरेक्टरी का विश्लेषण शुरू: /path/to/project
[INFO] कुल जावा फाइलों का प्रयास: 10
[INFO] सफलतापूर्वक प्रोसेस किया गया: 10
[INFO] गलतियों वाली फाइलों: 0
[INFO] कुल कंट्रोलर पाए गए: 1
UserController:
get /users/all
post /users/create
```

### नोट्स

- **सादगीकरण**: स्क्रिप्ट एनोटेशन को एकल लाइन पर मानता है और पथ को स्ट्रिंग लिटरल के बिना जटिल अभिव्यक्तियों के रूप में नहीं मानता है। उत्पादन उपयोग के लिए एक जावा पार्सर अधिक रॉबस्ट हो सकता है।
- **केवल GET और POST**: जैसा कि अनुरोध किया गया है, यह केवल `@GetMapping` और `@PostMapping` पर ध्यान केंद्रित करता है, PUT या DELETE जैसे अन्य मेथड को नजरअंदाज करता है (हालांकि सोचने का ट्रेस `@RequestMapping` के साथ मेथडों को शामिल करता है).
- **पथ संयोजन**: क्लास-लेवल और मेथड-लेवल पथ को सीधे संयोजित करता है (जैसे, `/users` + `/all` = `/users/all`). स्प्रिंग कई स्लैश को नॉर्मलाइज़ करता है, इसलिए यह प्रदर्शन के लिए पर्याप्त है।

इस स्क्रिप्ट ने अनुरोध के आवश्यकताओं को पूरा किया है जबकि दिए गए कोड के संरचना के समान संरचना बनाए रखी है, जिससे परिचितता और विश्वसनीयता सुनिश्चित होती है।