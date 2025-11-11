---
audio: false
generated: true
lang: hant
layout: post
title: 分析 Spring Boot 專案
translated: true
type: note
---

要分析一個 Spring Boot 專案（可能包含多個模組）並提取所有使用 `@GetMapping` 或 `@PostMapping` 註解定義的 API，我們需要遍歷專案目錄、識別控制器類別、提取 API 路徑，並以指定格式列印出來。以下是一個完整的 Python 腳本，靈感來自提供的程式碼結構，但根據新需求進行了調整。輸出將以「XXController: get path post path」的格式列出每個控制器及其關聯的 GET 和 POST 路徑。

### 方法

1. **遍歷目錄**：遞迴尋找專案目錄及其子目錄中的所有 `.java` 檔案。
2. **識別控制器**：檢查每個 Java 檔案是否包含 `@Controller` 或 `@RestController` 註解以確認其為控制器類別。
3. **提取類別層級路徑**：尋找類別層級的 `@RequestMapping` 註解以確定基礎路徑。
4. **提取方法層級 API**：尋找帶有 `@GetMapping` 或 `@PostMapping` 註解的方法，提取其路徑，並與基礎路徑（如果存在）結合。
5. **組織與列印**：收集每個控制器的 GET 和 POST 路徑，並以指定格式列印。

### Python 腳本

```python
import os
import sys
import re
from collections import defaultdict

def find_java_files(root_dir):
    """
    遞迴尋找指定目錄及其子目錄中的所有 .java 檔案。
    
    Args:
        root_dir (str): 開始搜尋的根目錄。
    
    Yields:
        str: 每個 .java 檔案的完整路徑。
    """
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.java'):
                yield os.path.join(dirpath, filename)

def extract_paths(line, annotation_type):
    """
    從 Spring 註解（@GetMapping、@PostMapping 或 @RequestMapping）中提取路徑值。
    
    Args:
        line (str): 包含註解的行。
        annotation_type (str): 註解類型（'GetMapping'、'PostMapping' 或 'RequestMapping'）。
    
    Returns:
        list: 從註解中提取的路徑字串列表。
    """
    if annotation_type in ['GetMapping', 'PostMapping']:
        match = re.search(rf'@{annotation_type}\\((.*)\\)', line)
        if match:
            content = match.group(1)
            # 提取引號內的所有字串字面值
            paths = re.findall(r'"([^"]*)"', content)
            return paths
        return []
    elif annotation_type == 'RequestMapping':
        match = re.search(r'@RequestMapping\\((.*)\\)', line)
        if match:
            content = match.group(1)
            # 尋找 'value' 或 'path' 屬性
            value_match = re.search(r'(value|path)\s*=\s*({[^}]*}|"[^"]*")', content)
            if value_match:
                value = value_match.group(2)
                if value.startswith('{'):
                    paths = re.findall(r'"([^"]*)"', value)
                else:
                    paths = [value.strip('"')]
                return paths
            # 如果沒有 'value' 或 'path'，假設為直接路徑指定
            paths = re.findall(r'"([^"]*)"', content)
            return paths
        return []

if __name__ == '__main__':
    # 解析命令列參數
    if len(sys.argv) != 2:
        print("Usage: python script.py <root_directory>")
        sys.exit(1)
    
    root_dir = sys.argv[1]
    if not os.path.isdir(root_dir):
        print(f"[ERROR] 指定路徑不是目錄: {root_dir}")
        sys.exit(1)
    
    print(f"[INFO] 開始分析目錄: {root_dir}")
    
    # 初始化字典以儲存控制器映射
    controllers = defaultdict(lambda: {'GET': [], 'POST': []})
    total_files = 0
    error_files = 0
    
    # 處理所有 Java 檔案
    for java_file in find_java_files(root_dir):
        try:
            with open(java_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            # 檢查檔案是否為控制器
            if any('@Controller' in line or '@RestController' in line for line in lines):
                controller_name = os.path.basename(java_file).replace('.java', '')
                
                # 尋找類別宣告行以區分類別層級和方法層級註解
                class_line_index = None
                for i, line in enumerate(lines):
                    if re.search(r'public\s+(class|abstract\s+class|interface)\s+\w+', line):
                        class_line_index = i
                        break
                if class_line_index is None:
                    continue
                
                # 提取類別層級的 @RequestMapping 作為基礎路徑
                base_paths = []
                for line in lines[:class_line_index]:
                    if re.search(r'\s*@RequestMapping', line):
                        base_paths = extract_paths(line, 'RequestMapping')
                        break
                if not base_paths:
                    base_paths = ['']
                
                # 提取方法層級的 @GetMapping 和 @PostMapping
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
                
                # 儲存唯一路徑
                get_paths = sorted(list(set(get_paths)))
                post_paths = sorted(list(set(post_paths)))
                
                if get_paths or post_paths:
                    controllers[controller_name]['GET'] = get_paths
                    controllers[controller_name]['POST'] = post_paths
            
            total_files += 1
        except Exception as e:
            print(f"[ERROR] 無法讀取檔案 {java_file}: {e}")
            error_files += 1
    
    # 列印摘要
    print(f"[INFO] 嘗試處理的 Java 檔案總數: {total_files + error_files}")
    print(f"[INFO] 成功處理: {total_files}")
    print(f"[INFO] 發生錯誤的檔案: {error_files}")
    print(f"[INFO] 找到的控制器總數: {len(controllers)}")
    
    # 以指定格式列印結果
    for controller, mappings in sorted(controllers.items()):
        print(f"{controller}:")
        for path in mappings['GET']:
            print(f"get {path}")
        for path in mappings['POST']:
            print(f"post {path}")
```

### 解釋

- **匯入**：使用 `os` 進行目錄遍歷，`sys` 處理命令列參數，`re` 進行正則表達式匹配，`defaultdict` 組織控制器資料。
- **`find_java_files`**：此函數遞迴產生專案目錄中的所有 `.java` 檔案，透過 `os.walk` 自然處理多個模組。
- **`extract_paths`**：此函數解析 `@GetMapping`、`@PostMapping` 或 `@RequestMapping` 註解以提取路徑值。它處理：
  - 單一路徑（例如 `@GetMapping("/path")`）。
  - 多個路徑（例如 `@GetMapping({"/path1", "/path2"})`）。
  - 命名屬性（例如 `@RequestMapping(value = "/path")`）。
- **主要邏輯**：
  - **命令列處理**：接受根目錄作為輸入，類似於提供的腳本。
  - **控制器檢測**：檢查檔案內容中是否存在 `@Controller` 或 `@RestController`。
  - **基礎路徑**：在類別宣告之前提取類別層級的 `@RequestMapping` 路徑。
  - **API 提取**：處理類別宣告後的行，尋找 `@GetMapping` 和 `@PostMapping`，並將路徑與基礎路徑結合。
  - **輸出**：列印每個控制器及其 GET 和 POST 路徑，每行一個，前綴為 "get" 或 "post"。
- **錯誤處理**：在檔案讀取期間捕獲異常並報告，反映了提供程式碼的穩健性。

### 範例輸出

對於包含 `UserController.java` 檔案的 Spring Boot 專案：

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

執行 `python script.py /path/to/project` 可能產生：

```
[INFO] 開始分析目錄: /path/to/project
[INFO] 嘗試處理的 Java 檔案總數: 10
[INFO] 成功處理: 10
[INFO] 發生錯誤的檔案: 0
[INFO] 找到的控制器總數: 1
UserController:
get /users/all
post /users/create
```

### 注意事項

- **簡化**：腳本假設註解位於單行，且路徑為字串字面值，沒有複雜表達式。在生產環境中使用時，Java 解析器可能更為穩健。
- **僅限 GET 和 POST**：根據要求，它專注於 `@GetMapping` 和 `@PostMapping`，忽略其他方法如 PUT 或 DELETE（儘管思考軌跡考慮了帶有方法的 `@RequestMapping`）。
- **路徑串接**：直接結合類別層級和方法層級路徑（例如 `/users` + `/all` = `/users/all`）。Spring 會規範化多個斜線，因此對於顯示目的而言，這已足夠。

此腳本滿足了查詢的要求，同時保持了與提供程式碼相似的結構，確保了熟悉度和可靠性。