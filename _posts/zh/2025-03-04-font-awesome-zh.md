---
audio: false
generated: true
lang: zh
layout: post
title: Font Awesome NPM 包
translated: true
---

### 关键点
- 使用 "font-awesome" npm 包（版本 4）似乎需要首先通过 `npm install font-awesome` 安装它，然后在 HTML 中链接 CSS 文件，并使用类似 `<i class="fa fa-home"></i>` 的图标。
- 研究表明，版本 4 已过时且不再维护；考虑升级到版本 6 以获得更新和安全性，使用类似 `@fortawesome/fontawesome-free` 的包。

---

### 安装和基本使用
要开始使用 "font-awesome" npm 包（版本 4），首先使用命令 `npm install font-awesome` 安装它。安装完成后，通过在 HTML 中添加 `<link rel="stylesheet" href="node_modules/font-awesome/css/font-awesome.min.css">` 来包含 CSS 文件。然后可以通过添加类似 `<i class="fa fa-home"></i>` 的 HTML 来在网页中使用图标，将 `fa-home` 替换为所需的图标名称，可以在 [Font Awesome 版本 4 文档](https://fontawesome.com/v4/cheatsheet) 中找到。

### 替代方法
如果使用构建工具（如 webpack），可以在 JavaScript 文件中直接导入 CSS，使用 `import 'font-awesome/css/font-awesome.min.css';`。对于使用 Less 或 Sass 的项目，可以导入相应的文件，例如在 Less 中使用 `@import "node_modules/font-awesome/less/font-awesome";`，确保路径根据需要进行调整。

### 版本说明
一个意外的细节是，"font-awesome" 包是版本 4，已经超过八年没有更新且不再维护。为了获得最新功能和安全性，考虑升级到版本 6，可以通过 `@fortawesome/fontawesome-free`（免费）或 `@fortawesome/fontawesome-pro`（专业版，需要订阅）获得。使用 `npm install @fortawesome/fontawesome-free` 安装版本 6，并使用 `import '@fortawesome/fontawesome-free/css/all.min.css';` 导入。更多详细信息请参阅 [Font Awesome 文档](https://fontawesome.com/docs/web/use-with/node-js)。

---

### 调查说明：使用 Font Awesome npm 包的全面指南

本节详细探讨了使用 "font-awesome" npm 包，重点介绍版本 4，同时也涉及到过渡到更现代的版本 6。信息来源于官方文档、npm 包详细信息和社区讨论，确保开发人员在各个水平上都能全面理解。

#### 背景和上下文
"font-awesome" npm 包，如 [npm](https://www.npmjs.com/package/font-awesome) 上列出的，对应于 Font Awesome 的 4.7.0 版本，最后发布于八年前，因此是一个较旧的、现已结束生命周期的版本。Font Awesome 是一个流行的可缩放矢量图标工具包，广泛用于网页开发中向网站添加图标。版本 4 主要依赖 CSS 实现图标，使用字体文件，以其简单性著称，但缺乏后续版本中的现代功能和更新。

由于其年龄较大，版本 4 的文档仍然可以在 [Font Awesome 版本 4 文档](https://fontawesome.com/v4/) 中访问，但官方网站现在主要关注版本 6，版本 4 被认为是结束生命周期的，如 [FortAwesome/Font-Awesome](https://github.com/FortAwesome/Font-Awesome) 中的 GitHub 讨论中所指出的。这种转变强调了考虑升级以获得安全性和功能增强的重要性，特别是对于持续项目。

#### 通过 npm 使用 "font-awesome" 包（版本 4）
要使用 "font-awesome" 包，请按照以下步骤操作，这些步骤与标准的 npm 实践和社区使用相一致：

1. **安装：**
   - 在项目目录中运行命令 `npm install font-awesome`。这将安装 4.7.0 版本，并将文件放置在 `node_modules/font-awesome` 目录中。
   - 包括 CSS、Less 和字体文件，如其 npm 描述中所述，提到维护在语义版本控制下，并包括 Less 使用的说明。

2. **在 HTML 中包含：**
   - 对于基本使用，在 HTML 头部链接 CSS 文件：
     ```html
     <link rel="stylesheet" href="node_modules/font-awesome/css/font-awesome.min.css">
     ```
   - 确保路径正确；如果 HTML 不是在根目录中，请相应调整（例如，`../node_modules/font-awesome/css/font-awesome.min.css`）。

3. **使用图标：**
   - 使用类似 `<i class="fa fa-home"></i>` 的 HTML 使用图标，其中 `fa` 是基础类，`fa-home` 指定图标。完整列表可以在 [Font Awesome 版本 4 图标表](https://fontawesome.com/v4/cheatsheet) 中找到。
   - 这种方法利用了包含的字体文件，确保可缩放性和 CSS 定制。

4. **与构建工具的替代集成：**
   - 如果使用构建工具（如 webpack），在 JavaScript 中导入 CSS：
     ```javascript
     import 'font-awesome/css/font-awesome.min.css';
     ```
   - 这种方法在现代网页开发中很常见，确保 CSS 与项目一起打包。

5. **Less 和 Sass 支持：**
   - 对于使用 Less 的项目，可以直接导入文件，如社区讨论中建议的：
     ```less
     @import "node_modules/font-awesome/less/font-awesome";
     ```
   - 类似地，对于 Sass，根据需要调整路径，尽管包主要支持 Less 版本 4，如 Ruby Gem 集成中所见，包括 `font-awesome-less` 和 `font-awesome-sass`。

#### 实际考虑和社区见解
社区讨论，例如 Stack Overflow 上的讨论，揭示了常见的做法，如将文件复制到公共目录以用于生产，使用 gulp 任务，或导入特定的 Less 组件以减少捆绑包大小。例如，一个用户建议导入仅必要的 Less 文件以节省字节，尽管指出节省不多，表明：
   - `@import "@{fa_path}/variables.less";`
   - `@import "@{fa_path}/mixins.less";` 等，将 `@fa_path` 调整为 `"../node_modules/font-awesome/less"`。

然而，对于大多数用户，直接链接 CSS 文件即可，特别是对于小型到中型项目。npm 包的内容还提到 Bundler 和 Less 插件要求，建议高级用户进行额外设置，例如：
   - 使用 `npm install -g less` 全局安装 Less。
   - 使用 `npm install -g less-plugin-clean-css` 使用 Less 插件 Clean CSS。

#### 版本 4 的局限性和升级路径
版本 4 尽管功能齐全，但不再支持，仅为版本 5 提供关键错误修复，版本 3 和 4 标记为结束生命周期，如 [FortAwesome/Font-Awesome GitHub](https://github.com/FortAwesome/Font-Awesome) 中所述。这意味着没有新功能、安全补丁或更新，这对于长期项目是一个重大问题。

要升级，版本 6 引入了显著变化，包括使用 JavaScript 的 SVG、新样式（Solid、Regular、Light、Duotone、Thin）和分离的品牌图标。要过渡，安装 `@fortawesome/fontawesome-free`：
   - 使用 `npm install @fortawesome/fontawesome-free`
   - 使用 `import '@fortawesome/fontawesome-free/css/all.min.css';` 导入，注意 CSS 文件名称从版本 6 更改为 `all.min.css`，反映更广泛的图标支持。

详细升级说明请参阅 [Font Awesome 从版本 4 升级](https://fontawesome.com/docs/web/setup/upgrade/upgrade-from-v4)，其中包括兼容性说明和删除版本 4 文件的步骤，确保平稳过渡。

#### 版本 4 与版本 6 使用的比较表

| 方面                  | 版本 4 (font-awesome)                     | 版本 6 (@fortawesome/fontawesome-free)    |
|-------------------------|---------------------------------------------|---------------------------------------------|
| 安装命令                | `npm install font-awesome`                  | `npm install @fortawesome/fontawesome-free` |
| CSS 文件名称             | `font-awesome.min.css`                      | `all.min.css`                               |
| 图标使用示例              | `<i class="fa fa-home"></i>`                | `<i class="fas fa-home"></i>` (Solid 样式) |
| 维护状态                | 结束生命周期，无更新                     | 活跃维护，最新版本 6.7.2                   |
| 附加功能                | 基本 CSS，Less 支持                     | SVG 与 JS，多种样式，API 支持               |
| 文档 URL                | [版本 4 文档](https://fontawesome.com/v4/) | [版本 6 文档](https://fontawesome.com/docs/web/use-with/node-js) |

此表突出了演变，帮助开发人员在升级决策中做出选择。

#### 结论和建议
对于新项目，强烈建议使用版本 6，以获得其活跃支持和现代功能。对于现有使用版本 4 的项目，评估升级路径，特别是出于安全原因，考虑到八年的差距。提供的步骤确保了版本 4 的功能，但未来的保险方法在于采用版本 6，详细指南请参阅 [Font Awesome 文档](https://fontawesome.com/docs/web/use-with/node-js)。

本全面指南确保用户拥有所有必要信息，从基本安装到高级集成，同时解决了在快速发展的技术环境中更新的关键需求。

---

### 关键引用
- [Font Awesome 版本 4 文档和图标表](https://fontawesome.com/v4/)
- [npm 上的 font-awesome 包，版本 4.7.0 详细信息](https://www.npmjs.com/package/font-awesome)
- [FortAwesome Font-Awesome GitHub 存储库，版本历史](https://github.com/FortAwesome/Font-Awesome)