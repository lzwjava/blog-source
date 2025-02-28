---
audio: false
lang: zh
layout: post
title: 使用 Auth Tokens 与 npm 仓库 URL
translated: true
---

### 关键要点
- 使用 auth 令牌与 npm 仓库 URL 似乎需要在 `.npmrc` 文件中进行配置，将令牌与仓库 URL 关联。
- 研究表明，标准方法是在 `.npmrc` 文件中添加 `//registry.url.com/:_authToken=your_token`，其中 `registry.url.com` 是仓库 URL，`your_token` 是您的身份验证令牌。
- 证据表明，使用 `.npmrc` 文件进行身份验证，因为在 URL 中直接包含令牌（例如在 HTTP 请求中）不是 npm 的标准做法，可能无法工作。

### 直接回答

#### 概述
要使用身份验证令牌与 npm 仓库 URL，通常在一个名为 `.npmrc` 的特殊文件中进行配置。该文件告诉 npm 命令行工具在访问特定的包仓库（如公共 npm 仓库或私有仓库）时如何进行身份验证。以下是如何逐步操作的方法，保持简单，适合初学者。

#### 配置步骤
1. **找到仓库 URL**：决定要使用的仓库，例如 `registry.npmjs.org` 为公共 npm 仓库，或者像 `privateregistry.com` 这样的 URL 为私有仓库。
2. **获取您的身份验证令牌**：从仓库提供商获取身份验证令牌，这可能是个人访问令牌或您组织提供的其他类型。
3. **编辑 `.npmrc` 文件**：打开或创建 `.npmrc` 文件。该文件可以在项目文件夹中用于项目特定设置，或者在主目录中（如 Unix 系统上的 `~/.npmrc`）用于用户范围的设置。
   - 添加一行，例如：`//registry.url.com/:_authToken=your_token`。将 `registry.url.com` 替换为您的仓库 URL，将 `your_token` 替换为您的实际令牌。
   - 例如，对于公共 npm 仓库，它可能看起来像：`//registry.npmjs.org/:_authToken=abc123`。
4. **保护文件**：确保 `.npmrc` 文件只能由您读取和写入，以保护您的令牌。在 Unix 系统上，可以使用 `chmod 600 ~/.npmrc` 设置权限。
5. **验证是否工作**：尝试运行一个 npm 命令，例如 `npm install`，看看它是否能够访问仓库而没有问题。

#### 意外细节
您可能会认为可以直接在 URL 中放置身份验证令牌（例如 `https://registry.url.com?token=your_token`），但这不是 npm 的标准做法。相反，npm 使用 `.npmrc` 文件在后台处理身份验证，使其更安全且更易于管理。

有关更多详细信息，请查看官方 npm 文档中关于配置 `.npmrc` 文件的部分 [这里](https://docs.npmjs.com/configuring-npm/npmrc)。

---

### 调查笔记：使用 npm 仓库 URL 的身份验证令牌的详细探讨

本节提供了如何使用身份验证令牌与 npm 仓库 URL 的全面分析，扩展了直接回答，增加了额外的上下文、技术细节和示例。它旨在涵盖研究中讨论的所有方面，确保用户在不同的专业水平上都能全面理解。

#### npm 和身份验证介绍
Node Package Manager（npm）是 JavaScript 开发人员的重要工具，管理包和依赖项。它与包仓库交互，例如公共仓库 [registry.npmjs.org](https://registry.npmjs.org)，以及组织托管的私有仓库。身份验证通常需要私有仓库或特定操作（如发布包），通常通过存储在配置文件中的身份验证令牌来处理。

`.npmrc` 文件是 npm 配置的核心，允许自定义设置，如仓库 URL、身份验证方法等。它可以存在于多个位置，例如项目级（在项目根目录中）、用户级（在主目录中，例如 Unix 系统上的 `~/.npmrc`）或全局（例如 `/etc/npmrc`）。该文件使用 INI 格式，其中键和值定义了 npm 的行为，包括它如何与仓库进行身份验证。

#### 在 `.npmrc` 中配置身份验证令牌
要使用特定仓库 URL 的身份验证令牌，配置 `.npmrc` 文件将令牌与该仓库关联。标准格式是：

```
registry.url.com/:_authToken=your_token
```

其中，`registry.url.com` 是仓库的基础 URL（例如，`registry.npmjs.org` 为公共仓库或 `privateregistry.com` 为私有仓库），`your_token` 是仓库提供的身份验证令牌。`:_authToken` 键表示这是基于令牌的身份验证，npm 使用它将 `Authorization` 头设置为 `Bearer your_token` 以进行 HTTP 请求。

例如，如果您对公共 npm 仓库有一个令牌 `abc123`，您的 `.npmrc` 条目将是：

```
registry.npmjs.org/:_authToken=abc123
```

此配置确保任何与 `registry.npmjs.org` 交互的 npm 命令都将包含令牌进行身份验证，允许访问私有包或发布功能，具体取决于令牌的范围。

#### 处理作用域包
对于作用域包（以 `@` 开头的包，例如 `@mycompany/mypackage`），可以为该作用域指定不同的仓库。首先，设置作用域的仓库：

```
@mycompany:registry=https://mycompany.artifactory.com/
```

然后，将身份验证令牌与该仓库关联：

```
mycompany.artifactory.com/:_authToken=your_token
```

此设置将所有 `@mycompany` 包的请求路由到指定的私有仓库，并使用提供的令牌进行身份验证。这在企业环境中特别有用，组织托管自己的 npm 仓库以供内部包使用。

#### `.npmrc` 的位置和安全性
`.npmrc` 文件可以位于几个位置，每个位置都有不同的用途：
- **项目级**：位于项目根目录（例如，`package.json` 旁边）。这对于项目特定配置和覆盖全局设置是理想的。
- **用户级**：位于用户的主目录（例如 Unix 系统上的 `~/.npmrc`，Windows 上的 `C:\Users\<Username>\.npmrc`）。这会影响该用户的所有 npm 操作。
- **全局**：位于 `/etc/npmrc` 或由 `globalconfig` 参数指定，通常用于系统范围的设置。

由于 `.npmrc` 可能包含敏感信息，如身份验证令牌，因此安全性至关重要。该文件必须只能由用户读取和写入，以防止未经授权的访问。在 Unix 系统上，可以使用命令 `chmod 600 ~/.npmrc` 确保这一点，将权限设置为仅读写所有者。

#### 其他身份验证方法
虽然基于令牌的身份验证是常见的，但 npm 也支持基本身份验证，可以在 `.npmrc` 文件中包含用户名和密码：

```
registry.url.com/:username=your_username
registry.url.com/:_password=your_password
```

然而，出于安全原因，建议使用基于令牌的身份验证，因为令牌可以撤销并具有范围权限，减少了与存储纯文本密码相比的风险。

#### 直接 URL 包含：是否可能？
问题提到“在 npm 仓库 URL 中使用 auth 或 authtoken”，这可能暗示直接在 URL 中包含令牌，例如 `https://registry.url.com?token=your_token`。然而，研究表明，这不是 npm 的标准做法。npm 仓库 API 文档和相关资源，例如 [NPM 仓库身份验证 | Rush](https://rushjs.io/pages/maintainer/npm_registry_auth/)，强调使用 `.npmrc` 文件进行身份验证，令牌通过 `Authorization` 头作为 `Bearer your_token` 传递。

尝试在 URL 中作为查询参数包含令牌是不受官方 npm 仓库支持的，可能无法工作，因为身份验证是在 HTTP 头级别处理的。某些私有仓库可能支持自定义基于 URL 的身份验证，但这不是官方 npm 仓库的文档。例如，基本身份验证允许 URL 如 `https://username:password@registry.url.com`，但这已被弃用且不安全，与基于令牌的方法相比。

#### 实际示例和用例
为了说明，考虑以下情况：

- **公共仓库与令牌**：如果您需要发布到公共 npm 仓库并有一个令牌，添加：
  ```
  registry.npmjs.org/:_authToken=abc123
  ```
  然后，运行 `npm publish` 上传您的包，npm 将使用令牌进行身份验证。

- **私有仓库用于作用域包**：对于使用私有仓库 `https://company.registry.com` 的公司，用于 `@company` 包，配置：
  ```
  @company:registry=https://company.registry.com/
  company.registry.com/:_authToken=def456
  ```
  现在，安装 `@company/mypackage` 将使用令牌对私有仓库进行身份验证。

- **CI/CD 集成**：在持续集成环境中，将令牌存储为环境变量（例如 `NPM_TOKEN`），并在 `.npmrc` 文件中动态使用它：
  ```
  registry.npmjs.org/:_authToken=${NPM_TOKEN}
  ```
  这种方法，详细说明在 [在 CI/CD 工作流中使用私有包 | npm 文档](https://docs.npmjs.com/using-private-packages-in-a-ci-cd-workflow/)，确保令牌不会硬编码且安全。

#### 故障排除和最佳实践
如果身份验证失败，请验证：
- 仓库 URL 是否正确且可访问。
- 令牌是否有效且具有必要的权限（例如，读取以进行安装，写入以进行发布）。
- `.npmrc` 文件是否在正确位置且具有适当的权限。

最佳实践包括：
- 永远不要将包含令牌的 `.npmrc` 提交到版本控制；将其添加到 `.gitignore`。
- 在 CI/CD 管道中使用环境变量来存储令牌，以增强安全性。
- 定期轮换令牌并撤销未使用的令牌，以最小化风险。

#### 身份验证方法的比较分析
为了提供结构化概述，以下是比较 npm 中基于令牌和基本身份验证的表格：

| **方法**          | **在 `.npmrc` 中的配置**                          | **安全性**                     | **用例**                     |
|---------------------|-------------------------------------------------------|-----------------------------------|-----------------------------------|
| 基于令牌（首选） | `registry.url.com/:_authToken=your_token`            | 高（可撤销，范围）         | 私有仓库，CI/CD        |
| 基本身份验证| `registry.url.com/:username=your_username`<br>`registry.url.com/:_password=your_password` | 低（纯文本密码）         | 遗留系统，公共仓库  |

此表格突出了为什么基于令牌的身份验证是推荐的，特别是对于现代工作流。

#### 结论
使用身份验证令牌与 npm 仓库 URL 主要涉及配置 `.npmrc` 文件将令牌与仓库关联。这种方法是标准的、安全的，并且得到了广泛支持，确保 npm 能够在不在 URL 中暴露令牌的情况下进行身份验证。虽然直接在 URL 中包含令牌不是 npm 的标准做法，可能无法工作，但 `.npmrc` 方法为公共和私有仓库交互提供了强大的解决方案。

有关进一步阅读，请参阅官方 npm 文档中的 [配置 npmrc](https://docs.npmjs.com/configuring-npm/npmrc) 和 [仓库身份验证](https://docs.npmjs.com/using-private-packages-in-a-ci-cd-workflow/)。

### 关键引用
- [NPM 仓库身份验证 Rush 文档](https://rushjs.io/pages/maintainer/npm_registry_auth/)
- [registry-auth-token npm 包详情](https://www.npmjs.com/package/registry-auth-token)
- [在 Stack Overflow 上全局配置 NPM 与令牌](https://stackoverflow.com/questions/38764714/globally-configure-npm-with-a-token-registry-to-a-specific-scope-organisation)
- [配置身份验证 Artifact Registry Google Cloud](https://cloud.google.com/artifact-registry/docs/nodejs/authentication)
- [官方 npm 文档的 npmrc 文件](https://docs.npmjs.com/configuring-npm/npmrc)
- [在 CI/CD 工作流中使用私有包 npm 文档](https://docs.npmjs.com/using-private-packages-in-a-ci-cd-workflow/)