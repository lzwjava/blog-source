---
audio: false
generated: true
lang: zh
layout: post
title: npm 包的安装源
translated: true
---

要将 `@ngx-formly/bootstrap` 包的安装源从本地 `.tgz` 文件更改为 npm 仓库，请按照以下步骤操作：

### 1. 卸载本地安装的包
由于你之前从本地 `.tgz` 文件安装了 `@ngx-formly/bootstrap`，它目前在项目的 `node_modules` 目录中。要删除它，在终端中运行以下命令：

```bash
npm uninstall @ngx-formly/bootstrap
```

此命令将包从 `node_modules` 中删除。如果包被手动添加到 `package.json` 文件的 `dependencies` 或 `devDependencies` 下，这也会将其从中删除。如果它没有列在 `package.json` 中（通常在从 `.tgz` 文件安装但未保存时），它仍将从项目中删除。

### 2. 从 npm 仓库安装包
现在，通过运行以下命令从 npm 仓库安装包：

```bash
npm install @ngx-formly/bootstrap
```

此命令从 npm 仓库（通常是 `https://registry.npmjs.org/`，除非你配置了不同的仓库）获取 `@ngx-formly/bootstrap` 的最新版本，并将其安装到 `node_modules` 目录中。它还会将包默认添加到 `package.json` 文件的 `dependencies` 下（在较新的 npm 版本中），确保它作为项目的一部分被跟踪。

### 可选：验证仓库（如果需要）
如果你之前更改了 npm 仓库，并且想确保它设置为默认 npm 仓库，可以使用以下命令检查：

```bash
npm config get registry
```

如果输出是 `https://registry.npmjs.org/`，你正在使用默认仓库，`npm install` 命令将按预期工作。如果它设置为不同的仓库，并且你想恢复为默认仓库，运行：

```bash
npm config set registry https://registry.npmjs.org/
```

然而，由于你提到已经配置了你的仓库，这个步骤可能不必要。

### 注意事项
- **版本控制**：如果你需要与 `.tgz` 文件中相同的版本，在卸载之前检查 `node_modules/@ngx-formly/bootstrap/package.json` 中的版本号。然后，安装该特定版本：
  ```bash
  npm install @ngx-formly/bootstrap@<version>
  ```
  如果不指定版本，将安装仓库中的最新版本。
- **依赖类型**：如果你想将包作为开发依赖而不是普通依赖，使用：
  ```bash
  npm install @ngx-formly/bootstrap --save-dev
  ```

按照这些步骤，你将成功将 `@ngx-formly/bootstrap` 从通过本地 `.tgz` 文件安装更改为从 npm 仓库安装。