---
audio: false
generated: true
lang: hi
layout: post
title: स्प्रिंग बूट प्रोजेक्ट्स का विश्लेषण करें
translated: true
type: note
---

Spring Boot प्रोजेक्ट (जिसमें कई modules शामिल हो सकते हैं) का विश्लेषण करने और `@GetMapping` या `@PostMapping` annotations के साथ परिभाषित सभी APIs को निकालने के लिए, हमें प्रोजेक्ट directory को traverse करना होगा, controller classes की पहचान करनी होगी, API paths निकालने होंगे और उन्हें एक निर्दिष्ट format में print करना होगा। नीचे एक पूर्ण Python script दी गई है जो इस कार्य को पूरा करती है, जो प्रदान किए गए कोड की संरचना से प्रेरित है लेकिन नई आवश्यकताओं के अनुरूप बनाई गई है। आउटपुट प्रत्येक controller को उससे जुड़े GET और POST paths के साथ "XXController: get path post path" format में सूचीबद्ध करेगा।

### Approach

1.  **Directory Traverse करें**: प्रोजेक्ट directory और उसकी subdirectories में सभी `.java` files को recursively ढूंढें।
2.  **Controllers की पहचान करें**: प्रत्येक Java file में `@Controller` या `@RestController` annotations की जांच करके पुष्टि करें कि यह एक controller class है।
3.  **Class-Level Paths निकालें**: Base paths निर्धारित करने के लिए class level पर `@RequestMapping` annotations देखें।
4.  **Method-Level APIs निकालें**: `@GetMapping` या `@PostMapping` से annotated methods ढूंढें, उनके paths निकालें और यदि मौजूद हों तो उन्हें base paths के साथ combine करें।
5.  **व्यवस्थित करें और Print करें**: प्रति controller GET और POST paths एकत्रित करें और उन्हें निर्दिष्ट format में print करें।

### Python Script

```python
import os
import sys
import re
from collections import defaultdict

def find_java_files(root_dir):
    """
    Recursively find all .java files in the given directory and its subdirectories.
    
    Args:
        root_dir (str): The root directory to start the search from.
    
    Yields:
        str: The full path to each .java file.
    """
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.java'):
                yield os.path.join(dirpath, filename)

def extract_paths(line, annotation_type):
    """
    Extract path values from a Spring annotation (@GetMapping, @PostMapping, or @RequestMapping).
    
    Args:
        line (str): The line containing the annotation.
        annotation_type (str): The type of annotation ('GetMapping', 'PostMapping', or 'RequestMapping').
    
    Returns:
        list: A list of path strings extracted from the annotation.
    """
    if annotation_type in ['GetMapping', 'PostMapping']:
        match = re.search(rf'@{annotation_type}\\((.*)\\)', line)
        if match:
            content = match.group(1)
            # Extract all string literals within quotes
            paths = re.findall(r'"([^"]*)"', content)
            return paths
        return []
    elif annotation_type == 'RequestMapping':
        match = re.search(r'@RequestMapping\\((.*)\\)', line)
        if match:
            content = match.group(1)
            # Look for 'value' or 'path' attribute
            value_match = re.search(r'(value|path)\s*=\s*({[^}]*}|"[^"]*")', content)
            if value_match:
                value = value_match.group(2)
                if value.startswith('{'):
                    paths = re.findall(r'"([^"]*)"', value)
                else:
                    paths = [value.strip('"')]
                return paths
            # If no 'value' or 'path', assume direct path specification
            paths = re.findall(r'"([^"]*)"', content)
            return paths
        return []

if __name__ == '__main__':
    # Parse command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python script.py <root_directory>")
        sys.exit(1)
    
    root_dir = sys.argv[1]
    if not os.path.isdir(root_dir):
        print(f"[ERROR] The specified path is not a directory: {root_dir}")
        sys.exit(1)
    
    print(f"[INFO] Starting analysis of directory: {root_dir}")
    
    # Initialize a dictionary to store controller mappings
    controllers = defaultdict(lambda: {'GET': [], 'POST': []})
    total_files = 0
    error_files = 0
    
    # Process all Java files
    for java_file in find_java_files(root_dir):
        try:
            with open(java_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            # Check if the file is a controller
            if any('@Controller' in line or '@RestController' in line for line in lines):
                controller_name = os.path.basename(java_file).replace('.java', '')
                
                # Find the class declaration line to separate class-level and method-level annotations
                class_line_index = None
                for i, line in enumerate(lines):
                    if re.search(r'public\s+(class|abstract\s+class|interface)\s+\w+', line):
                        class_line_index = i
                        break
                if class_line_index is None:
                    continue
                
                # Extract class-level @RequestMapping as base paths
                base_paths = []
                for line in lines[:class_line_index]:
                    if re.search(r'\s*@RequestMapping', line):
                        base_paths = extract_paths(line, 'RequestMapping')
                        break
                if not base_paths:
                    base_paths = ['']
                
                # Extract method-level @GetMapping and @PostMapping
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
                
                # Store unique paths
                get_paths = sorted(list(set(get_paths)))
                post_paths = sorted(list(set(post_paths)))
                
                if get_paths or post_paths:
                    controllers[controller_name]['GET'] = get_paths
                    controllers[controller_name]['POST'] = post_paths
            
            total_files += 1
        except Exception as e:
            print(f"[ERROR] Could not read file {java_file}: {e}")
            error_files += 1
    
    # Print summary
    print(f"[INFO] Total Java files attempted: {total_files + error_files}")
    print(f"[INFO] Successfully processed: {total_files}")
    print(f"[INFO] Files with errors: {error_files}")
    print(f"[INFO] Total controllers found: {len(controllers)}")
    
    # Print results in the specified format
    for controller, mappings in sorted(controllers.items()):
        print(f"{controller}:")
        for path in mappings['GET']:
            print(f"get {path}")
        for path in mappings['POST']:
            print(f"post {path}")
```

### Explanation

-   **Imports**: हम directory traversal के लिए `os`, command-line arguments के लिए `sys`, regular expressions के लिए `re` और controller data को व्यवस्थित करने के लिए `defaultdict` का उपयोग करते हैं।
-   **`find_java_files`**: यह function `os.walk` के माध्यम से प्रोजेक्ट directory में सभी `.java` files को recursively देता है, जो स्वाभाविक रूप से multiple modules को संभालता है।
-   **`extract_paths`**: यह function path values निकालने के लिए `@GetMapping`, `@PostMapping`, या `@RequestMapping` annotations को parse करता है। यह संभालता है:
    -   Single paths (जैसे, `@GetMapping("/path")`)।
    -   Multiple paths (जैसे, `@GetMapping({"/path1", "/path2"})`)।
    -   Named attributes (जैसे, `@RequestMapping(value = "/path")`)।
-   **Main Logic**:
    -   **Command-Line Handling**: प्रदान किए गए script के समान, इनपुट के रूप में एक root directory लेता है।
    -   **Controller Detection**: file content में `@Controller` या `@RestController` की जांच करता है।
    -   **Base Paths**: class declaration से पहले class-level `@RequestMapping` paths निकालता है।
    -   **API Extraction**: `@GetMapping` और `@PostMapping` के लिए class declaration के बाद की lines को process करता है, paths को base paths के साथ combine करता है।
    -   **Output**: प्रत्येक controller को उसके GET और POST paths के साथ print करता है, प्रत्येक को एक लाइन में, "get" या "post" उपसर्ग के साथ।
-   **Error Handling**: file reading के दौरान exceptions को पकड़ता है और उन्हें रिपोर्ट करता है, जो प्रदान किए गए कोड की robustness को दर्शाता है।

### Sample Output

एक Spring Boot प्रोजेक्ट के लिए जिसमें एक file `UserController.java` है:

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

`python script.py /path/to/project` चलाने पर आउटपुट हो सकता है:

```
[INFO] Starting analysis of directory: /path/to/project
[INFO] Total Java files attempted: 10
[INFO] Successfully processed: 10
[INFO] Files with errors: 0
[INFO] Total controllers found: 1
UserController:
get /users/all
post /users/create
```

### Notes

-   **Simplifications**: Script यह मानती है कि annotations single lines पर हैं और paths complex expressions के बिना string literals हैं। Production use के लिए, एक Java parser अधिक robust हो सकता है।
-   **GET और POST Only**: अनुरोध के अनुसार, यह `@GetMapping` और `@PostMapping` पर केंद्रित है, PUT या DELETE जैसे अन्य methods को नजरअंदाज करता है (हालांकि thinking trace ने methods के साथ `@RequestMapping` पर विचार किया था)।
-   **Path Concatenation**: Class-level और method-level paths को सीधे combine करता है (जैसे, `/users` + `/all` = `/users/all`)। Spring multiple slashes को normalize कर देता है, इसलिए display purposes के लिए यह पर्याप्त है।

यह script query की आवश्यकताओं को पूरा करती है, साथ ही प्रदान किए गए कोड के समान एक संरचना बनाए रखती है, जिससे परिचितता और विश्वसनीयता सुनिश्चित होती है।