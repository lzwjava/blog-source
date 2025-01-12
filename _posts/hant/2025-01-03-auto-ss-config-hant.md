---
audio: true
lang: hant
layout: post
title: 开源工具：自动SS配置
---

我很高兴地宣布，我已经开源了一个名为**Auto SS Config**的工具。这款工具能够自动从Shadowsocks链接生成并上传Shadowsocks或Clash的订阅链接，从而简化了代理服务器配置的管理与更新过程。

这款工具对我来说简直是改变游戏规则的存在，尤其是在我的Shadowsocks服务器遭遇封锁时。我利用Outline Manager创建新服务器，获取全新地址，并通过Mac应用直接导入该URL，以此绕过GFW的限制。运行本项目中的`python upload_configs.py`命令，即可更新我的订阅链接，确保我所有的电子设备都能保持畅通的网络连接。

## 功能特点

- **将Shadowsocks链接转换为Clash配置**：轻松在不同代理配置间切换。
- **支持多Shadowsocks服务器**：便捷管理多个服务器。
- **自动上传配置至Google云存储**：确保配置安全且可访问。
- **使配置公开可访问**：与他人共享你的配置。
- **利用缓存控制实现即时更新**：保证配置始终最新。

## 文件

- `app_config_tmp.yaml`: 应用程序配置（存储桶名称，SS URLs）。
- `clash_config_tmp.yaml`: 临时的Clash配置文件。
- `upload_configs.py`: 生成Clash配置并上传配置到Google云存储的脚本。
- `requirements.txt`: Python依赖项。

## 设置

1. **安裝依賴**：
    ```bash
    pip install -r requirements.txt
    ```

2. **设置Google Cloud凭据**：
    - 安装Google Cloud SDK。
    - 运行`gcloud auth application-default login`命令。
    - 或者设置`GOOGLE_APPLICATION_CREDENTIALS`环境变量。

3. **將 `app_config_tmp.yaml` 複製為 `app_config.yaml` 並進行配置**：
    ```yaml
    bucket_name: 你的存儲桶名稱
    ss_urls:
        - ss://方法:密碼@服務器:端口
    ```

## 使用方法

1. **將您的 Shadowsocks 網址添加到 `app_config.yaml` 中的 `ss_urls` 列表**：
    ```yaml
    ss_urls:
        - ss://方法:密碼@伺服器:端口
    ```

2. **上傳配置**：
    ```bash
    python upload_configs.py
    ```

脚本将输出两种配置的公共URL。

## 发展历程

- **Python 3.6+**
- 使用 `ruamel.yaml` 进行 YAML 处理。
- 使用 `google-cloud-storage` 进行 GCS 操作。

## 许可证

麻省理工学院

---

欢迎随时查看[仓库](https://github.com/lzwjava/auto-ss-config)以获取更多详情并参与贡献！