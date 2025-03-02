---
audio: false
generated: true
lang: zh
layout: post
title: 测试 NPM 仓库使用原始 HTTP 请求
translated: true
---

要使用原始 HTTP 请求和工具（如 `curl` 或 Insomnia）测试您的 NPM 仓库，可以通过检查连接性、身份验证和提供包数据的能力来验证其功能，而无需依赖 NPM 客户端。由于您的仓库需要用户名和密码，您需要在请求中手动处理身份验证。以下是使用原始 HTTP 请求测试您的仓库的完整指南，假设它是一个兼容 NPM 的仓库（例如 Verdaccio、Nexus 或自定义实现），并且支持基于令牌或基本身份验证。

---

## 使用原始 HTTP 请求测试仓库的步骤

### 1. 身份验证并获取令牌（如果需要）

大多数 NPM 仓库使用基于令牌的身份验证，要求您登录以获取令牌，然后再进行进一步的请求。某些仓库可能也支持直接的基本身份验证。以下是使用 `curl` 进行身份验证的方法：

#### 使用 `curl` 登录
向仓库的身份验证端点发送 PUT 请求以获取令牌：

```bash
curl -X PUT \
  -H "Content-Type: application/json" \
  -d '{"name": "<username>", "password": "<password>"}' \
  <registry-url>/-/user/org.couchdb.user:<username>
```

- **替换**：
  - `<username>`：您的仓库用户名。
  - `<password>`：您的仓库密码。
  - `<registry-url>`：您的仓库的完整 URL（例如 `https://my-registry.example.com`）。
- **预期响应**：如果成功，您将获得一个包含令牌的 JSON 响应：
  ```json
  {
    "token": "your-auth-token"
  }
  ```
- **保存令牌**：复制 `your-auth-token` 的值，以便在后续请求中使用。

**注意**：如果您的仓库使用不同的身份验证端点或方法（例如基本身份验证或自定义 API），请查看其文档。如果它直接支持基本身份验证，您可以跳过此步骤，并在后续请求中包含 `-u "<username>:<password>"`。

---

### 2. 向仓库发送 Ping

通过向其根 URL 或 ping 端点发送 GET 请求来测试与仓库的基本连接。

#### 使用 `curl` 发送 Ping
```bash
curl -H "Authorization: Bearer your-auth-token" <registry-url>
```

- **替换**：
  - `your-auth-token`：步骤 1 中的令牌。
  - `<registry-url>`：您的仓库 URL。
- **预期响应**：成功的响应（HTTP 200）可能会返回仓库的主页或简单的状态消息（例如，对于基于 CouchDB 的仓库，`{"db_name":"registry"}`）。
- **替代方案**：某些仓库提供 `/-/ping` 端点：
  ```bash
  curl -H "Authorization: Bearer your-auth-token" <registry-url>/-/ping
  ```

**如果使用基本身份验证**：如果您的仓库不使用令牌并且支持基本身份验证：
```bash
curl -u "<username>:<password>" <registry-url>
```

---

### 3. 检索包元数据

通过请求特定包的详细信息来验证仓库是否可以提供包元数据。

#### 使用 `curl` 获取元数据
```bash
curl -H "Authorization: Bearer your-auth-token" <registry-url>/<package-name>
```

- **替换**：
  - `<package-name>`：您知道存在于您的仓库中的包（例如，如果它代理公共仓库，则为 `lodash`，或者私有包 `my-org-utils`）。
- **预期响应**：包含包的元数据的 JSON 对象，包括版本、依赖项和 tarball URL。例如：
  ```json
  {
    "name": "lodash",
    "versions": {
      "4.17.21": {
        "dist": {
          "tarball": "<registry-url>/lodash/-/lodash-4.17.21.tgz"
        }
      }
    }
  }
  ```

**如果使用基本身份验证**：
```bash
curl -u "<username>:<password>" <registry-url>/<package-name>
```

- **成功**：200 OK 响应和元数据确认仓库正确提供包数据。

---

### 4. 下载包 tarball（可选）

为了全面测试仓库，下载包 tarball 以确保它可以提供实际的包文件。

#### 使用 `curl` 下载 tarball
1. 从步骤 3 的元数据中，找到特定版本的 `tarball` URL（例如 `<registry-url>/lodash/-/lodash-4.17.21.tgz`）。
2. 下载它：
```bash
curl -H "Authorization: Bearer your-auth-token" -O <tarball-url>
```

- **替换**：将 `<tarball-url>` 替换为元数据中的 URL。
- **`-O` 标志**：以其原始名称保存文件（例如 `lodash-4.17.21.tgz`）。
- **如果使用基本身份验证**：
  ```bash
  curl -u "<username>:<password>" -O <tarball-url>
  ```
- **成功**：文件成功下载，您可以提取它（例如，使用 `tar -xzf <filename>`）以验证其内容。

---

## 使用 Insomnia 测试

如果您更喜欢使用图形用户界面工具如 Insomnia，请按照以下步骤操作：

### 1. 设置身份验证
- 在 Insomnia 中创建一个新请求。
- 转到 **Auth** 选项卡：
  - **Bearer Token**：如果您在步骤 1 中获得了令牌，选择“Bearer Token”并粘贴 `your-auth-token`。
  - **Basic Auth**：如果仓库使用基本身份验证，选择“Basic Auth”并输入您的 `<username>` 和 `<password>`。

### 2. 向仓库发送 Ping
- **方法**：GET
- **URL**：`<registry-url>` 或 `<registry-url>/-/ping`
- 点击 **Send**。
- **预期响应**：200 OK 状态和简单的响应正文。

### 3. 检索包元数据
- **方法**：GET
- **URL**：`<registry-url>/<package-name>`
- 确保在 Auth 选项卡中设置了身份验证。
- 点击 **Send**。
- **预期响应**：200 OK 状态和 JSON 格式的包元数据。

### 4. 下载 tarball
- **方法**：GET
- **URL**：元数据中的 tarball URL（例如 `<registry-url>/<package-name>/-/<package-name>-<version>.tgz`）。
- 点击 **Send and Download** 以将文件保存到本地。
- **成功**：文件下载，确认仓库提供包。

---

## 故障排除

- **401 未授权**：
  - 检查您的令牌或凭据。
  - 确保 `Authorization` 头或基本身份验证格式正确。
- **404 未找到**：
  - 验证包是否存在于仓库中。
  - 如果测试公共包（例如 `lodash`），确认仓库代理公共 NPM 仓库。
- **连接错误**：
  - 双重检查 `<registry-url>`（例如，如果需要，包含 `https://`）。
  - 对于 HTTPS 仓库，如果使用 `curl` 时出现 SSL 错误，添加 `-k` 以绕过证书检查（仅用于测试）。
- **自定义仓库行为**：
  - 如果这些步骤失败，请参考您的仓库文档，了解特定端点或身份验证方法。

---

## 结论

通过使用 `curl` 或 Insomnia 遵循这些步骤，您可以使用原始 HTTP 请求测试 NPM 仓库的连接性、身份验证和提供包的能力。首先进行身份验证（如果需要），然后向仓库发送 ping，检索已知包的元数据，并可选地下载 tarball。这种方法确保您的仓库在 HTTP 级别上完全可操作。