---
audio: true
lang: zh
layout: post
title: "GitHub Actions 任务的最大执行时间\n\nGitHub Actions 是 GitHub 提供的持续集成和持续交付（CI/CD）平台，允许开发者在代码仓库中自动化构建、测试和部署流程。然而，使用\
  \ GitHub Actions 时，了解任务的最大执行时间限制是非常重要的，以确保工作流能够顺利完成。\n\n### 免费计划的限制\n\n对于使用 GitHub\
  \ Free 计划的公共仓库，每个任务的最大执行时间为 **6 小时**。这意味着如果你的任务在 6 小时内没有完成，它将被自动终止。\n\n### 付费计划的限制\n\
  \n对于使用 GitHub Pro、Team 或 Enterprise 计划的仓库，每个任务的最大执行时间为 **6 小时**。与免费计划相同，付费计划的用户也需要确保任务在\
  \ 6 小时内完成。\n\n### 自托管运行器的限制\n\n如果你使用自托管的运行器（self-hosted runners），则不受 GitHub Actions\
  \ 的时间限制。你可以根据需要配置运行器的最大执行时间，但需要注意自托管运行器的资源管理和维护。\n\n### 如何优化任务执行时间\n\n1. **并行化任务**：将任务分解为多个并行运行的作业，以减少总执行时间。\n\
  2. **缓存依赖**：使用缓存来存储构建依赖项，避免每次运行任务时都重新下载和安装。\n3. **优化脚本**：审查和优化你的构建和测试脚本，删除不必要的步骤和冗余代码。\n\
  4. **使用矩阵构建**：利用 GitHub Actions 的矩阵构建功能，同时运行多个配置的测试，以加快整体执行速度。\n\n### 示例配置\n\n以下是一个简单的\
  \ GitHub Actions 工作流配置示例，展示了如何设置并行任务和缓存依赖：\n\n```yaml\nname: CI\n\non: [push]\n\n\
  jobs:\n  build:\n    runs-on: ubuntu-latest\n    strategy:\n      matrix:\n    \
  \    node-version: [12.x, 14.x, 16.x]\n    steps:\n    - uses: actions/checkout@v2\n\
  \    - name: Use Node.js ${{ matrix.node-version }}\n      uses: actions/setup-node@v2\n\
  \      with:\n        node-version: ${{ matrix.node-version }}\n    - name: Cache\
  \ node modules\n      uses: actions/cache@v2\n      with:\n        path: ~/.npm\n\
  \        key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}\n \
  \       restore-keys: |\n          ${{ runner.os }}-node-\n    - run: npm install\n\
  \    - run: npm test\n```\n\n通过合理配置和优化，你可以确保 GitHub Actions 任务在最大执行时间限制内顺利完成，从而提高开发效率和代码质量。\n\
  \n---\n\n作者：李智维  \n公司：美钛技术服务  \n来源：思芮  \n参考：冲顶大会、趣直播、面包Live、北京大米互娱有限公司、广州玉岩中学"
translated: true
---

我一直使用 GitHub Actions 来自动化翻译我的博客文章。最初，我尝试在一个任务中翻译所有文章，只有在所有翻译完成后才将更改提交回仓库。

我满怀希望地去睡觉，期待这个过程能够完成。然而，8小时后醒来，我发现了以下错误：

> 在 runner GitHub Actions 12 上运行的任务已超过 360 分钟的最大执行时间。

这意味着6个小时的翻译工作白费了，因为提交只在最后进行。

为了解决这个问题，我修改了工作流程，每翻译10篇文章就提交一次更改。

此外，我还实现了多线程编程，将总翻译时间从6小时减少到了大约1小时。