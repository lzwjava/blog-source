---
audio: false
generated: true
lang: zh
layout: post
title: HTTP 文件上传
translated: true
---

### 关键点
- 研究表明，HTTP 文件上传通常使用 POST 方法和 multipart/form-data 格式，适用于网页表单，允许上传多个文件和额外数据。
- PUT 方法也可以上传文件，直接发送原始内容，通常用于 RESTful API 以简化操作。
- 证据表明两种方法都有效，服务器配置和使用场景决定了选择。

### 概述
通过 HTTP 上传文件是在线共享数据的常见任务，例如将照片或文档发送到网站。可以通过两种主要方式实现：使用 POST 方法和一种称为 multipart/form-data 的特殊格式，适用于网页表单，或者使用 PUT 方法，适用于现代 API，更简单。每种方法都有自己的设置，选择哪种方法取决于服务器配置和你要做的事情。

### 如何工作
- **POST 与 Multipart/Form-Data**：这就像将文件和任何额外信息（如描述）打包成单独的部分，用唯一的边界字符串标记。适用于选择文件上传的网页表单。
- **PUT 方法**：直接将文件内容发送到特定的 URL，就像在服务器上更新文件。更简单，但需要服务器支持。

### 意外细节
你可能不会想到 PUT 方法，通常用于更新数据，也可以处理文件上传，特别是在 API 中，使其成为传统表单之外的多功能选项。

---

### 调查说明：HTTP 文件上传的详细解释

通过 HTTP 上传文件是 Web 开发中的基本操作，使用户能够将图像、文档或媒体与服务器共享。可以通过两种主要方法实现：使用 POST 方法和 multipart/form-data 编码，通常用于网页表单，以及 PUT 方法，通常用于 RESTful API 直接传输文件内容。下面，我们深入探讨这些方法，包括其结构、实现和考虑因素，为技术和非技术受众提供全面理解。

#### Multipart/Form-Data：网页表单的标准

multipart/form-data 内容类型是 HTTP 文件上传的默认选择，特别是处理 HTML 表单时。这种方法允许在单个请求中同时传输多个文件和额外的表单数据，如文本字段。该过程涉及构建一个由唯一边界字符串分隔的请求体，以确保服务器能够区分不同的数据部分。

##### 结构和示例
请求开始时设置 `Content-Type` 头为 `multipart/form-data; boundary=boundary_string`，其中 `boundary_string` 是随机选择的字符串，以避免与文件内容冲突。每个请求体部分都包括 `Content-Disposition` 头，指定表单字段名称和文件名，以及 `Content-Type`，指示数据类型（例如，`text/plain` 表示文本文件，`image/jpeg` 表示 JPEG 图像）。部分以边界字符串结束，最后一个部分以边界字符串后跟两个连字符标记。

例如，将名为 `example.txt` 的文件内容为 "Hello, world!" 上传到 [此端点](https://example.com/upload)，表单字段名称为 "file"。HTTP 请求如下所示：

```
POST /upload HTTP/1.1
Host: example.com
Content-Type: multipart/form-data; boundary=abc123
Content-Length: 101

--abc123
Content-Disposition: form-data; name="file"; filename="example.txt"
Content-Type: text/plain

Hello, world!
--abc123--
```

这里，`Content-Length` 计算为 101 字节，包括边界、头和文件内容，通常使用 CRLF（\r\n）进行正确的 HTTP 格式化。

##### 处理多个文件和表单字段
这种方法在需要额外元数据的场景中表现出色。例如，如果上传一个带有描述的文件，请求体可以包括多个部分：

```
--abc123
Content-Disposition: form-data; name="description"

This is my file
--abc123
Content-Disposition: form-data; name="file"; filename="example.txt"
Content-Type: text/plain

Hello, world!
--abc123--
```

每个部分的内容都被保留，包括任何换行符，边界确保分隔。这种灵活性使其非常适合包含 `<input type="file">` 元素的网页表单。

#### PUT 方法：RESTful API 的直接文件上传

PUT 方法为 RESTful API 上下文提供了更简单的替代方案，目的是使用文件内容更新或创建资源。与 multipart/form-data 不同，PUT 直接在请求体中发送原始文件数据，减少了开销并简化了服务器端处理。

##### 结构和示例
例如，将 `example.txt` 上传到 [此 URL](https://example.com/files/123)，请求如下所示：

```
PUT /files/123 HTTP/1.1
Host: example.com
Content-Type: text/plain
Content-Length: 13

Hello, world!
```

这里，`Content-Type` 指定文件的 MIME 类型（例如，`text/plain`），`Content-Length` 是文件的字节大小。这种方法对于大文件非常高效，因为它避免了 multipart/form-data 的编码开销，但需要服务器配置为处理文件上传的 PUT 请求。

##### 使用场景和考虑因素
PUT 方法通常用于更新用户头像或将文件上传到 API 中的特定资源。然而，并非所有服务器都默认支持 PUT 文件上传，特别是在共享托管环境中，POST 与 multipart/form-data 更为普遍接受。可能需要配置服务器，例如在 Apache 中启用 PUT 动词，如 [PHP 手册中 PUT 方法支持](https://www.php.net/manual/en/features.file-upload.put-method.php) 中所述。

#### 比较分析

为了说明两种方法的区别，请考虑以下表格：

| 方面                  | POST 与 Multipart/Form-Data          | PUT 与原始内容                  |
|-------------------------|----------------------------------------|---------------------------------------|
| **使用场景**            | 网页表单、多个文件、元数据    | RESTful API、单个文件更新     |
| **复杂性**          | 较高（边界处理、多个部分） | 较低（直接内容）               |
| **效率**          | 中等（编码开销）           | 较高（无编码）                 |
| **服务器支持**      | 广泛支持                      | 可能需要配置            |
| **示例头**     | `Content-Type: multipart/form-data; boundary=abc123` | `Content-Type: text/plain`           |
| **请求体**        | 由边界分隔的部分          | 原始文件内容                     |

该表格突出了 multipart/form-data 适用于 Web 交互的多功能性，而 PUT 适用于 API 驱动的上传，具体取决于服务器功能。

#### 实现细节和陷阱

##### 边界选择和文件内容
在 multipart/form-data 中，选择边界字符串至关重要，以避免与文件内容冲突。如果边界出现在文件中，可能会导致解析错误。现代库通过生成随机边界来处理这一点，但手动实现需要小心。对于二进制文件，内容按原样传输，保留所有字节，这对于保持文件完整性至关重要。

##### 文件大小和性能
两种方法都必须考虑服务器施加的文件大小限制。multipart/form-data 请求可能会变得很大，包含多个文件，可能会超过服务器限制或导致内存问题。PUT 方法虽然简单，但也需要流处理大文件，以避免将整个内容加载到内存中，如 [HTTPie 文件上传文档](https://httpie.io/docs/cli/file-upload-forms) 中所述。

##### 错误处理和安全性
发送请求后，客户端应检查 HTTP 状态代码。成功通常由 200（OK）或 201（Created）表示，而错误如 400（Bad Request）或 403（Forbidden）表示问题。安全性至关重要，因为文件上传可以被利用进行攻击，如上传恶意可执行文件。服务器应验证文件类型、扫描恶意软件并限制上传目录，如 [Stack Overflow 关于 HTTP 文件上传安全性的讨论](https://stackoverflow.com/questions/8659808/how-does-http-file-upload-work) 中所述。

#### 各种语言的实际示例

各种编程语言提供库来简化 HTTP 文件上传。例如，Python 的 `requests` 库处理 multipart/form-data 如下：

```python
import requests
files = {'file': open('example.txt', 'rb')}
response = requests.post('https://example.com/upload', files=files)
```

对于 PUT，可以使用 curl，如 [Stack Overflow 关于测试 PUT 上传](https://stackoverflow.com/questions/5143915/test-file-upload-using-http-put-method) 中所示：

```bash
curl -X PUT "https://example.com/files/123" --upload-file example.txt
```

这些示例展示了抽象，但理解底层 HTTP 结构对于排除故障和自定义实现至关重要。

#### 结论

总之，HTTP 文件上传可以通过 POST 与 multipart/form-data 实现，适用于多功能的网页表单交互，或者 PUT 适用于高效的 API 更新，每种方法都有其独特的优势和要求。服务器配置、文件大小和安全性考虑是关键，确保实现的健壮性。有关进一步阅读，请参阅 [Medium 关于 POST 文件上传的指南](https://medium.com/@API4AI/post-a-file-via-http-request-the-ultimate-guide-b23fb70a3f73) 以获取各种语言的实际示例。

### 关键引用
- [如何将文件上传到 Web 服务器 Learn web development MDN](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Tools_and_setup/Upload_files_to_a_web_server)
- [如何进行 HTTP 文件上传 Stack Overflow](https://stackoverflow.com/questions/8659808/how-does-http-file-upload-work)
- [通过 HTTP 请求发布文件 The Ultimate Guide by API4AI Medium](https://medium.com/@API4AI/post-a-file-via-http-request-the-ultimate-guide-b23fb70a3f73)
- [HTTP REST API 文件上传 Phil Sturgeon](https://philsturgeon.com/http-rest-api-file-uploads/)
- [PHP PUT 方法支持手册](https://www.php.net/manual/en/features.file-upload.put-method.php)
- [curl 测试使用 HTTP PUT 方法的文件上传 Stack Overflow](https://stackoverflow.com/questions/5143915/test-file-upload-using-http-put-method)
- [文件上传表单 HTTPie 3.2.4 文档](https://httpie.io/docs/cli/file-upload-forms)