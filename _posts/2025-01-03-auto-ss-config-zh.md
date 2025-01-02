---
audio: true
lang: zh
layout: post
title: "开源工具：Auto SS Config"
---

我很高兴地宣布，我开源了一个名为 **Auto SS Config** 的工具。这个工具可以自动生成和上传 Shadowsocks 或 Clash 订阅 URL，从 Shadowsocks URL 中生成，使管理和更新代理服务器配置变得更加容易。

这个工具对我来说是一个游戏规则的改变者，特别是当我的 Shadowsocks 服务器被封锁时。我使用 Outline Manager 创建一个新的服务器，获取一个新的地址，并使用 Mac 应用程序直接导入此 URL 以绕过 GFW 限制。从这个项目运行 `python upload_configs.py` 更新我的订阅 URL，确保所有我的数字设备保持功能网络连接。

## 功能

- **将 Shadowsocks URL 转换为 Clash 配置**：轻松在不同的代理配置之间切换。
- **支持多个 Shadowsocks 服务器**：方便管理多个服务器。
- **自动上传配置到 Google Cloud Storage**：保持配置的安全和可访问性。
- **使配置公开可访问**：与他人分享您的配置。
- **使用缓存控制进行即时更新**：确保您的配置始终是最新的。

## 文件

- `ss_urls.txt`：包含 Shadowsocks 服务器 URL（每行一个）。
- `ss_urls_tmp.txt`：临时文件，包含 Shadowsocks 服务器 URL（每行一个）。
- `clash_config_tmp.yaml`：临时 Clash 配置文件。
- `app_config.json`：应用配置（存储桶名称，文件路径）。
- `generate_clash_config.py`：从 SS URL 生成 Clash 配置的脚本。
- `upload_configs.py`：上传配置到 Google Cloud Storage 的脚本。
- `requirements.txt`：Python 依赖项。

## 设置

1. **安装依赖项**：
    ```bash
    pip install -r requirements.txt
    ```

2. **设置 Google Cloud 凭证**：
    - 安装 Google Cloud SDK。
    - 运行 `gcloud auth application-default login`。
    - 或设置 `GOOGLE_APPLICATION_CREDENTIALS` 环境变量。

3. **配置 `app_config.json`**：
    ```json
    {
        "bucket_name": "your-bucket-name",
        "ss_config_file": "ss_urls.txt"
    }
    ```

## 使用

1. **将 `ss_urls_tmp.txt` 复制到 `ss_urls.txt` 以使用**。

2. **将您的 Shadowsocks URL 添加到 `ss_urls.txt`，每行一个**：
    ```
    ss://method:password@server:port
    ```

3. **上传配置**：
    ```bash
    python upload_configs.py
    ```

    脚本将输出两个配置的公共 URL。

## 开发

- **Python 3.6+**
- 使用 `ruamel.yaml` 处理 YAML。
- 使用 `google-cloud-storage` 进行 GCS 操作。

## 许可证

MIT

---

欢迎查看 [仓库](https://github.com/lzwjava/auto-ss-config) 了解更多详细信息并贡献！