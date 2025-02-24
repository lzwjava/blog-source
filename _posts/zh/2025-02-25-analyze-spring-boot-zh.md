---
audio: false
lang: zh
layout: post
title: 分析 Spring Boot 项目
translated: true
---

要分析一个Spring Boot项目（可能包含多个模块）并提取所有使用 `@GetMapping` 或 `@PostMapping` 注解定义的API，我们需要遍历项目目录，识别控制器类，提取API路径，并以指定格式打印它们。下面是一个完成此任务的完整Python脚本，灵感来自提供的代码结构，但根据新需求进行了调整。输出将以格式 "XXController: get path post path" 列出每个控制器及其关联的GET和POST路径。

### 方法

1. **遍历目录**：递归查找项目目录及其子目录中的所有 `.java` 文件。
2. **识别控制器**：检查每个Java文件是否包含 `@Controller` 或 `@RestController` 注解，以确认它是一个控制器类。
3. **提取类级路径**：查找类级别的 `@RequestMapping` 注解，以确定基础路径。
4. **提取方法级API**：查找使用 `@GetMapping` 或 `@PostMapping` 注解的方法，提取它们的路径，并与基础路径（如果有）结合。
5. **组织和打印**：按控制器收集GET和POST路径，并以指定格式打印它们。

### Python 脚本

```python
import os
import sys
import re
from collections import defaultdict

def find_java_files(root_dir):
    """
    递归查找给定目录及其子目录中的所有 .java 文件。

    参数:
        root_dir (str): 从中开始搜索的根目录。

    生成:
        str: 每个 .java 文件的完整路径。
    """
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.java'):
                yield os.path.join(dirpath, filename)

def extract_paths(line, annotation_type):
    """
    从Spring注解（@GetMapping、@PostMapping 或 @RequestMapping）中提取路径值。

    参数:
        line (str): 包含注解的行。
        annotation_type (str): 注解类型 ('GetMapping'、'PostMapping' 或 'RequestMapping')。

    返回:
        list: 从注解中提取的路径字符串列表。
    """
    if annotation_type in ['GetMapping', 'PostMapping']:
        match = re.search(rf'@{annotation_type}\((.*)\)', line)
        if match:
            content = match.group(1)
            # 提取引号内的所有字符串字面量
            paths = re.findall(r'"([^"]*)"', content)
            return paths
        return []
    elif annotation_type == 'RequestMapping':
        match = re.search(r'@RequestMapping\((.*)\)', line)
        if match:
            content = match.group(1)
            # 查找 'value' 或 'path' 属性
            value_match = re.search(r'(value|path)\s*=\s*({[^}]*}|"[^"]*")', content)
            if value_match:
                value = value_match.group(2)
                if value.startswith('{'):
                    paths = re.findall(r'"([^"]*)"', value)
                else:
                    paths = [value.strip('"')]
                return paths
            # 如果没有 'value' 或 'path'，则假定直接路径规范
            paths = re.findall(r'"([^"]*)"', content)
            return paths
        return []

if __name__ == '__main__':
    # 解析命令行参数
    if len(sys.argv) != 2:
        print("用法: python script.py <root_directory>")
        sys.exit(1)

    root_dir = sys.argv[1]
    if not os.path.isdir(root_dir):
        print(f"[ERROR] 指定的路径不是目录: {root_dir}")
        sys.exit(1)

    print(f"[INFO] 开始分析目录: {root_dir}")

    # 初始化一个字典来存储控制器映射
    controllers = defaultdict(lambda: {'GET': [], 'POST': []})
    total_files = 0
    error_files = 0

    # 处理所有Java文件
    for java_file in find_java_files(root_dir):
        try:
            with open(java_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            # 检查文件是否是控制器
            if any('@Controller' in line or '@RestController' in line for line in lines):
                controller_name = os.path.basename(java_file).replace('.java', '')

                # 查找类声明行以分隔类级别和方法级别的注解
                class_line_index = None
                for i, line in enumerate(lines):
                    if re.search(r'public\s+(class|abstract\s+class|interface)\s+\w+', line):
                        class_line_index = i
                        break
                if class_line_index is None:
                    continue

                # 提取类级别的 @RequestMapping 作为基础路径
                base_paths = []
                for line in lines[:class_line_index]:
                    if re.search(r'\s*@RequestMapping', line):
                        base_paths = extract_paths(line, 'RequestMapping')
                        break
                if not base_paths:
                    base_paths = ['']

                # 提取方法级别的 @GetMapping 和 @PostMapping
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

                # 存储唯一路径
                get_paths = sorted(list(set(get_paths)))
                post_paths = sorted(list(set(post_paths)))

                if get_paths or post_paths:
                    controllers[controller_name]['GET'] = get_paths
                    controllers[controller_name]['POST'] = post_paths

            total_files += 1
        except Exception as e:
            print(f"[ERROR] 无法读取文件 {java_file}: {e}")
            error_files += 1

    # 打印摘要
    print(f"[INFO] 尝试的Java文件总数: {total_files + error_files}")
    print(f"[INFO] 成功处理: {total_files}")
    print(f"[INFO] 文件错误: {error_files}")
    print(f"[INFO] 找到的控制器总数: {len(controllers)}")

    # 以指定格式打印结果
    for controller, mappings in sorted(controllers.items()):
        print(f"{controller}:")
        for path in mappings['GET']:
            print(f"get {path}")
        for path in mappings['POST']:
            print(f"post {path}")
```

### 解释

- **导入**：我们使用 `os` 进行目录遍历，`sys` 进行命令行参数处理，`re` 进行正则表达式匹配，`defaultdict` 组织控制器数据。
- **`find_java_files`**：该函数递归生成项目目录及其子目录中的所有 `.java` 文件，通过 `os.walk` 自然处理多个模块。
- **`extract_paths`**：该函数解析 `@GetMapping`、`@PostMapping` 或 `@RequestMapping` 注解以提取路径值。它处理：
  - 单个路径（例如，`@GetMapping("/path")`）。
  - 多个路径（例如，`@GetMapping({"/path1", "/path2"})`）。
  - 命名属性（例如，`@RequestMapping(value = "/path")`）。
- **主逻辑**：
  - **命令行处理**：以根目录作为输入，类似于提供的脚本。
  - **控制器检测**：检查文件内容是否包含 `@Controller` 或 `@RestController`。
  - **基础路径**：在类声明之前提取类级别的 `@RequestMapping` 路径。
  - **API提取**：处理类声明后的行以查找 `@GetMapping` 和 `@PostMapping`，并将路径与基础路径结合。
  - **输出**：按控制器打印其GET和POST路径，每行前缀为 "get" 或 "post"。
- **错误处理**：在文件读取过程中捕获异常并报告它们，模仿提供代码的健壮性。

### 示例输出

对于一个包含 `UserController.java` 文件的Spring Boot项目：

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

运行 `python script.py /path/to/project` 可能会产生：

```
[INFO] 开始分析目录: /path/to/project
[INFO] 尝试的Java文件总数: 10
[INFO] 成功处理: 10
[INFO] 文件错误: 0
[INFO] 找到的控制器总数: 1
UserController:
get /users/all
post /users/create
```

### 注意事项

- **简化**：脚本假设注解在单行上，路径是字符串字面量，没有复杂表达式。对于生产使用，Java解析器可能更加健壮。
- **仅GET和POST**：如要求，它专注于 `@GetMapping` 和 `@PostMapping`，忽略其他方法如PUT或DELETE（虽然思考路径考虑了 `@RequestMapping` 与方法）。
- **路径拼接**：直接将类级别和方法级别路径结合（例如，`/users` + `/all` = `/users/all`）。Spring会规范化多个斜杠，因此对于显示目的来说这是足够的。