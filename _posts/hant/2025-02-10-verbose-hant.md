---
audio: true
generated: false
image: false
lang: hant
layout: post
title: 冗長輸出
translated: true
type: post
---

- 要在 Homebrew 中啟用詳細輸出，請使用 `export HOMEBREW_CURL_VERBOSE=1` 結合 `brew upgrade --verbose`。

- 要增加 SSH 的詳細程度，請使用 `ssh -vvv user@host`。

- 要獲得 `git` 的更多詳細輸出，請使用 `git -v` 或 `git --verbose`。

- 要從 `rsync` 获取更多輸出，請使用 `rsync -vv source destination`。

- 在 ssh 配置中寫入詳細配置，例如在 .ssh/config 中有 LogLevel VERBOSE。

- 要在 `npm` 中啟用詳細輸出，請使用 `npm install --verbose` 或 `npm run <script> --verbose`。

- 要在 Node.js 中進行詳細記錄，請使用 `NODE_DEBUG` 環境變量：`NODE_DEBUG=http,net node your_script.js`。

- 要從 `curl` 获取詳細輸出，請使用 `curl -v <url>`。

- 要在 `pip` 中啟用詳細輸出，請使用 `pip install -v <package>` 或 `pip install --verbose <package>`。

- 要在 `wget` 中獲得詳細輸出，請使用 `wget --verbose <url>`。

- 要從 `yum` 获取詳細輸出，請使用 `yum -v install <package>`。

- 要在 `apt-get` 中啟用詳細輸出，請使用 `apt-get -o Debug::pkgProblemResolver=yes install <package>`。

- 要在 `adb` 中進行詳細記錄，請使用 `adb logcat -v verbose`。

- 要以詳細模式運行 Python，請使用 `python -v your_script.py`。

- 要以詳細輸出編譯 Java 代碼，請使用 `javac -verbose YourClass.java`。

- 要以詳細模式啟動 VSCode：`code --verbose`。 要進行記錄，請在 `settings.json` 中設置 `"trace": true`，並通過 "Developer: Open View..." -> "Log (Window)" 或 "Log (Extension Host)" 查看日誌。

- 要在 IntelliJ IDEA 中進行詳細記錄："Help" -> "Diagnostic Tools" -> "Debug Log Settings..." 或在 `idea.vmoptions` 中添加 `-Didea.logging.level=DEBUG`。 日誌位於 IntelliJ IDEA 配置目錄下的 "log" 目錄中。

- 要在 Eclipse 中啟用詳細輸出，請修改 `eclipse.ini` 以包含 `-debug` 或 `-consoleLog`。 要進行詳細記錄，請配置 Log4j 或 java.util.logging。 日誌位置取決於記錄配置。

- 要從 Maven 获取詳細輸出，請使用 `mvn -X <command>`。 例如，`mvn -X clean install`。

- 要在 WebSphere Liberty Server 中啟用詳細記錄，請配置 `server.xml` 文件以包含 `<logging traceSpecification="*=info:com.ibm.ws.*=all:"/>`。 您還可以使用 `console.log` 和 `messages.log` 文件進行詳細日誌。

- 要在 AWS CLI 中獲得詳細輸出，請使用 `--debug` 旗標：`aws <command> --debug`。

- 要從 `gcloud` 获取詳細輸出，請使用 `--verbosity` 旗標：`gcloud <command> --verbosity=debug`。

- 要在 Gradle 中啟用詳細輸出，請使用 `-v` 或 `--verbose` 旗標：`gradle <task> -v`。 要進行更詳細的記錄，請使用 `--debug`：`gradle <task> --debug`。

- 要在 Docker 中獲得詳細輸出，請使用 `--verbose` 旗標（如果特定命令可用）或檢查 Docker 守護進程日誌。 您可以在 `daemon.json` 文件中配置 Docker 守護進程記錄級別。

- 要從 Terraform 获取詳細輸出，請將 `TF_LOG` 環境變量設置為 `DEBUG` 或 `TRACE`：`export TF_LOG=DEBUG` 或 `export TF_LOG=TRACE`。

- 要在 Ansible 中啟用詳細輸出，請使用 `-v`、`-vv`、`-vvv` 或 `-vvvv` 旗標以增加詳細程度：`ansible-playbook playbook.yml -vvv`。

- 要在 Kubernetes `kubectl` 中獲得詳細輸出，請使用 `--v` 旗標後跟一個表示詳細程度的數字（例如，`--v=6` 或 `--v=9`）：`kubectl get pods --v=6`。

- 要從 systemd 获取詳細輸出，請使用 `journalctl -b -x` 查看帶有說明的日誌，或 `systemctl --full --all status <service>`。

- 要在 `bundle install` 中啟用詳細輸出，請使用 `bundle install --verbose`。