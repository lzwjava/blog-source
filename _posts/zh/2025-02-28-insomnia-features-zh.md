---
audio: false
generated: false
lang: zh
layout: post
title: 使用 Kong Insomnia GUI 中的功能
translated: true
---

Kong Insomnia 提供了一个强大的图形用户界面（GUI），以简化 API 开发。下面是如何在 Insomnia GUI 中使用 **params**、**body**、**auth**、**cookies**、**certificates**、**settings** 和 **proxy** 的详细指南。

---

#### 1. **Params (查询参数)**
查询参数用于将数据附加到 URL，通常用于 GET 请求。

- **如何使用**：
  - 打开 **Debug** 选项卡并选择或创建一个请求（例如，GET）。
  - 在 URL 字段旁边，点击 **Query** 选项卡。
  - 添加键值对以用于查询参数。例如，输入 `key` 为 "id" 和 `value` 为 "123" 将在 URL 中追加 `?id=123`。
  - 要使用环境变量，在值字段中输入 `{{variableName}}`（例如，`{{userId}}`）。
  - 通过切换每对旁边的复选框来启用或禁用特定参数。

- **示例**：
  对于类似 `https://api.example.com/users?id=123` 的 URL，添加：
  - 键：`id`
  - 值：`123`
  Insomnia 将自动将查询字符串格式化到 URL 中。

---

#### 2. **Body**
Body 用于与 POST 或 PUT 请求一起发送数据。

- **如何使用**：
  - 在 **Debug** 选项卡中，选择一个请求（例如，POST 或 PUT）。
  - 切换到 URL 字段下方的 **Body** 选项卡。
  - 从下拉菜单中选择一个 body 类型：
    - **JSON**：输入 JSON 数据（例如，`{"name": "John", "age": 30}`）。
    - **Form URL-Encoded**：添加键值对，类似于查询参数。
    - **Multipart Form**：添加字段或上传文件以用于带有文件附件的表单。
    - **Raw**：输入纯文本或其他格式（例如，XML）。
  - 通过在 body 内容中输入 `{{variableName}}` 来使用环境变量。

- **示例**：
  对于发送 JSON 的 POST 请求：
  - 从下拉菜单中选择 **JSON**。
  - 输入：`{"name": "John", "age": "{{userAge}}"}`。
  Insomnia 将自动将 `Content-Type` 头设置为 `application/json`。

---

#### 3. **Auth (认证)**
认证设置允许您在请求中包含凭据或令牌。

- **如何使用**：
  - 在 **Debug** 选项卡中，选择您的请求。
  - 转到 **Auth** 选项卡。
  - 从下拉菜单中选择一个认证类型：
    - **Basic Auth**：输入用户名和密码。
    - **Bearer Token**：粘贴令牌（例如，JWT）。
    - **OAuth 2.0**：配置客户端 ID、密钥和其他 OAuth 流细节。
    - **API Key**：添加键值对（例如，Key: `Authorization`，Value: `your-api-key`）。
  - Insomnia 会自动将认证详细信息添加到请求头中。

- **示例**：
  对于 Bearer Token：
  - 选择 **Bearer Token**。
  - 粘贴您的令牌（例如，`abc123xyz`）。
  请求头将包括：`Authorization: Bearer abc123xyz`。

---

#### 4. **Cookies**
Cookies 会自动管理，但可以手动查看或编辑。

- **如何使用**：
  - Insomnia 会根据工作区存储从服务器响应接收到的 cookies。
  - 要管理 cookies：
    - 转到 **Preferences** (Ctrl + , 或 macOS 上的 Cmd + ,)。
    - 导航到 **Data** > **Cookie Jar**。
    - 根据需要查看、编辑或删除 cookies。
  - Cookies 在同一工作区的请求之间持久化，并会自动与后续请求一起发送。

- **提示**：
  如果需要使用特定的 cookies 进行测试，请在 **Cookie Jar** 中为相关域手动添加它们。

---

#### 5. **Certificates**
客户端证书用于需要相互 TLS 认证的 HTTPS 请求。

- **如何使用**：
  - 转到 **Preferences** (Ctrl + , 或 Cmd + ,)。
  - 选择 **Certificates** 部分。
  - 点击 **Add Certificate**：
    - 提供证书文件（例如，`.pem`，`.crt`）。
    - 添加私钥文件和可选的密码（如果需要）。
    - 将证书与特定主机（例如，`api.example.com`）关联。
  - Insomnia 将使用证书进行对指定主机的请求。

- **示例**：
  对于需要证书的 `api.example.com`：
  - 上传 `client.crt` 和 `client.key`。
  - 将主机设置为 `api.example.com`。
  对该域的请求将包括证书。

---

#### 6. **Settings**
设置允许您自定义 Insomnia 的行为。

- **如何使用**：
  - 通过 **Preferences** (Ctrl + , 或 Cmd + ,) 访问。
  - 关键选项包括：
    - **Theme**：在浅色、深色或系统默认之间切换。
    - **Proxy**：配置代理设置（见下文）。
    - **Plugins**：安装额外功能（例如，自定义响应格式化程序）。
    - **Data**：管理 Local Vault 以安全存储敏感数据（例如，API 密钥）。

- **提示**：
  使用 **Local Vault** 安全存储敏感值（例如，令牌），而不是硬编码它们。

---

#### 7. **Proxy**
代理将您的请求路由到指定的服务器，适用于调试或企业网络。

- **如何使用**：
  - 转到 **Preferences** > **Proxy**。
  - 启用代理并输入代理服务器详细信息（例如，`http://proxy.example.com:8080`）。
  - 要全局使用，请在此处保存。
  - 对于每个请求的代理：
    - 点击 **Debug** 选项卡中请求名称旁边的齿轮图标。
    - 在请求特定配置中覆盖代理设置。

- **示例**：
  要通过企业代理路由请求：
  - 在 **Preferences** 中启用代理。
  - 将代理 URL 设置为 `http://proxy.example.com:8080`。
  所有请求现在都将使用此代理，除非被覆盖。

---

### 总结
这是如何在 Insomnia GUI 中使用这些功能的快速回顾：
- **Params**：在 **Query** 选项卡中为 GET 请求添加查询参数。
- **Body**：通过 **Body** 选项卡选择格式，将数据与 POST/PUT 请求一起发送。
- **Auth**：在 **Auth** 选项卡中设置认证以进行安全请求。
- **Cookies**：在 **Preferences** > **Cookie Jar** 中管理 cookies。
- **Certificates**：在 **Preferences** > **Certificates** 中为 HTTPS 添加客户端证书。
- **Settings**：在 **Preferences** 中自定义 Insomnia（主题、插件等）。
- **Proxy**：在 **Preferences** 或每个请求中配置代理。

通过利用这些功能，您可以高效地测试和调试 Kong Insomnia 中的 API。实验每个部分以定制您的工作流程！