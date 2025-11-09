---
audio: false
generated: true
image: false
lang: zh
layout: post
model: x-ai/grok-4-fast
title: 在Ubuntu 24.04上安装Chromium浏览器
translated: true
type: note
---

要在 **Ubuntu 24.04** 上安装 **Chromium**，你有几种不错的选择——取决于你想要**官方的 Snap 版本**、**APT（Debian 包）版本**，还是**手动下载**。以下是每种方法的简明指南：

---

### 🧩 选项 1：通过 Snap 安装（官方 Ubuntu 方式）

这是**默认**且最稳定的方法。

```bash
sudo snap install chromium
```

然后通过以下命令运行：

```bash
chromium
```

✅ *优点：*

* 由 Canonical 官方维护。
* 自动更新。

⚠️ *缺点：*

* 启动可能较慢。
* Snap 沙盒可能导致系统代理或文件访问问题。

---

### ⚙️ 选项 2：通过 APT 安装（Debian 包，非 Snap）

如果你**不喜欢 Snap**，可以从**第三方仓库**安装 Chromium，例如由 **ungoogled-chromium** 或 **OBS** 提供的官方 Debian 构建。

1. 添加 OBS 仓库：

   ```bash
   sudo apt install wget gnupg
   wget -qO - https://download.opensuse.org/repositories/home:/ungoogled_chromium/Ubuntu_24.04/Release.key | sudo gpg --dearmor -o /usr/share/keyrings/ungoogled-chromium.gpg
   ```

2. 添加软件源：

   ```bash
   echo "deb [signed-by=/usr/share/keyrings/ungoogled-chromium.gpg] https://download.opensuse.org/repositories/home:/ungoogled_chromium/Ubuntu_24.04/ /" | sudo tee /etc/apt/sources.list.d/ungoogled-chromium.list
   ```

3. 安装 Chromium：

   ```bash
   sudo apt update
   sudo apt install ungoogled-chromium
   ```

然后通过以下命令运行：

```bash
ungoogled-chromium
```

✅ *优点：*

* 无 Snap 依赖。
* 提供隐私强化版本。

⚠️ *缺点：*

* 更新比 Snap 慢。
* 某些功能（如 Google 同步）被禁用。

---

### 🧰 选项 3：从 Chromium 官方构建安装（手动）

如果你想要**最新的开发者版本**：

```bash
sudo apt install chromium-browser
```

如果它重定向到 Snap 而你想避免这种情况：

```bash
sudo apt purge chromium-browser
sudo apt install chromium
```

或者，手动下载 `.deb` 文件：

```bash
wget https://commondatastorage.googleapis.com/chromium-browser-snapshots/Linux_x64/LAST_CHANGE -O /tmp/LAST_CHANGE
LATEST=$(cat /tmp/LAST_CHANGE)
wget "https://commondatastorage.googleapis.com/chromium-browser-snapshots/Linux_x64/${LATEST}/chrome-linux.zip"
unzip chrome-linux.zip
./chrome-linux/chrome
```

---

### 🌍 关于代理设置的说明

由于你的系统使用：

```
HTTP_PROXY=http://127.0.0.1:7890
HTTPS_PROXY=http://127.0.0.1:7890
```

请确保 Snap 和 APT 尊重你的代理，通过在 `/etc/environment` 或你的 shell 配置文件中导出这些变量：

```bash
export http_proxy=http://127.0.0.1:7890
export https_proxy=http://127.0.0.1:7890
```

---

需要我展示如何让 Chromium 自动使用该代理（使其始终通过代理连接）吗？