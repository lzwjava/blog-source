---
audio: false
generated: true
image: false
lang: zh
layout: post
model: openai/gpt-5
title: Ubuntu 24.04 浏览器安装指南
translated: true
type: note
---

除了 **Firefox** 和 **Chromium** 之外，你还可以在 **Ubuntu 24.04** 上安装不少优秀的浏览器——具体取决于你的优先级（速度、隐私性、兼容性、资源占用等）。以下是分类列表及说明：

---

### 🧠 主流浏览器

**1. Google Chrome**

* 基于 Chromium，但包含谷歌的同步功能、编解码器和专有特性
* 与各类网页应用（如 Google Docs、Meet 等）具有出色的兼容性
* 可通过谷歌官网的 `.deb` 包安装

**2. Microsoft Edge（Linux 版）**

* 基于 Chromium，界面精美，与微软服务深度集成
* 内存管理通常优于 Chrome
* 可通过微软官网的 `.deb` 包安装

---

### 🔒 隐私保护型浏览器

**3. Brave**

* 基于 Chromium，内置广告拦截器、跟踪器阻止功能和 Tor 窗口模式
* 保持与 Chrome 扩展的兼容性
* 安装方式：

  ```bash
  sudo apt install apt-transport-https curl
  sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg
  echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg] https://brave-browser-apt-release.s3.brave.com/ stable main" | sudo tee /etc/apt/sources.list.d/brave-browser-release.list
  sudo apt update
  sudo apt install brave-browser
  ```

**4. Vivaldi**

* 同样基于 Chromium，但支持高度自定义（标签页平铺、键盘快捷键、侧边栏工具）
* 比 Chrome 或 Edge 功能更丰富
* 从 [vivaldi.com](https://vivaldi.com) 下载 `.deb` 安装包

**5. Tor Browser**

* 专注于匿名访问和突破网络审查
* 基于 Firefox ESR，通过 Tor 网络路由流量
* 安装方式：

  ```bash
  sudo apt install torbrowser-launcher
  ```

---

### 🪶 轻量级浏览器

**6. Falkon（Qt WebEngine）**

* 轻量级，界面简洁，与 KDE/Qt 系统完美集成
* 安装方式：

  ```bash
  sudo apt install falkon
  ```

**7. Midori**

* 经典项目的现代复兴，追求简洁与低资源占用
* 适合简单浏览，不适用于重型网页应用
* 安装方式：

  ```bash
  sudo apt install midori
  ```

**8. Epiphany（GNOME Web）**

* GNOME 默认浏览器，基于 WebKit（非 Chromium）
* 简洁轻量，与 GNOME 环境完美契合
* 安装方式：

  ```bash
  sudo apt install epiphany-browser
  ```

---

### 🧪 开发者/小众浏览器

**9. Ungoogled Chromium**

* 移除了所有谷歌跟踪和 API 依赖的 Chromium
* 需要手动配置，但适合追求严格隐私的用户
* 可通过社区提供的 `.deb` 包或 Flatpak 安装

**10. Floorp**

* 基于 Firefox 的现代分支，增强隐私保护和自定义功能
* 由日本开发者打造，正逐渐流行
* 可通过 Flathub 获取 Flatpak 版本

---

需要我根据你在 Ubuntu 上的工作流程，推荐浏览器组合方案吗？（例如：*一款隐私保护型 + 一款轻量级 + 一款全功能浏览器*）