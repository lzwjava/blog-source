---
audio: true
generated: false
lang: ja
layout: post
title: 冗長な出力
translated: true
---

- Homebrewで詳細な出力を有効にするには、`export HOMEBREW_CURL_VERBOSE=1`を`brew upgrade --verbose`と一緒に使用します。

- SSHの詳細度を増やすには、`ssh -vvv user@host`を使用します。

- `git`でより詳細な出力を得るには、`git -v`または`git --verbose`を使用します。

- `rsync`からより多くの出力を得るには、`rsync -vv source destination`を使用します。

- SSHの設定ファイルに詳細な設定を書くこともできます。例えば、`.ssh/config`に`LogLevel VERBOSE`を追加します。

- `npm`で詳細な出力を有効にするには、`npm install --verbose`または`npm run <script> --verbose`を使用します。

- Node.jsでの詳細なログを得るには、`NODE_DEBUG`環境変数を使用します: `NODE_DEBUG=http,net node your_script.js`。

- `curl`から詳細な出力を得るには、`curl -v <url>`を使用します。

- `pip`で詳細な出力を有効にするには、`pip install -v <package>`または`pip install --verbose <package>`を使用します。

- `wget`で詳細な出力を得るには、`wget --verbose <url>`を使用します。

- `yum`から詳細な出力を得るには、`yum -v install <package>`を使用します。

- `apt-get`で詳細な出力を有効にするには、`apt-get -o Debug::pkgProblemResolver=yes install <package>`を使用します。

- `adb`での詳細なログを得るには、`adb logcat -v verbose`を使用します。

- Pythonを詳細モードで実行するには、`python -v your_script.py`を使用します。

- Javaコードを詳細な出力でコンパイルするには、`javac -verbose YourClass.java`を使用します。

- VSCodeを詳細モードで起動するには: `code --verbose`。ログを設定するには、`settings.json`に`"trace": true`を設定し、"Developer: Open View..." -> "Log (Window)"または"Log (Extension Host)"でログを表示します。

- IntelliJ IDEAの詳細なログ: "Help" -> "Diagnostic Tools" -> "Debug Log Settings..."または`idea.vmoptions`に`-Didea.logging.level=DEBUG`を追加します。ログはIntelliJ IDEAの設定ディレクトリ内の"log"ディレクトリにあります。

- Eclipseで詳細な出力を有効にするには、`eclipse.ini`を`-debug`または`-consoleLog`で修正します。詳細なログを設定するには、Log4jまたはjava.util.loggingを設定します。ログの場所はログ設定に依存します。

- Mavenから詳細な出力を得るには、`mvn -X <command>`を使用します。例えば、`mvn -X clean install`。

- WebSphere Liberty Serverでの詳細なログを有効にするには、`server.xml`ファイルに`<logging traceSpecification="*=info:com.ibm.ws.*=all:"/>`を含めます。詳細なログには`console.log`と`messages.log`ファイルを使用します。

- AWS CLIでの詳細な出力を得るには、`--debug`フラグを使用します: `aws <command> --debug`。

- `gcloud`から詳細な出力を得るには、`--verbosity`フラグを使用します: `gcloud <command> --verbosity=debug`。

- Gradleで詳細な出力を有効にするには、`-v`または`--verbose`フラグを使用します: `gradle <task> -v`。より詳細なログを得るには、`--debug`を使用します: `gradle <task> --debug`。

- Dockerでの詳細な出力を得るには、`--verbose`フラグ（特定のコマンドで利用可能な場合）を使用するか、Dockerデーモンのログを確認します。Dockerデーモンのログレベルは`daemon.json`ファイルで設定できます。

- Terraformから詳細な出力を得るには、`TF_LOG`環境変数を`DEBUG`または`TRACE`に設定します: `export TF_LOG=DEBUG`または`export TF_LOG=TRACE`。

- Ansibleで詳細な出力を有効にするには、`-v`、`-vv`、`-vvv`、`-vvvv`フラグを使用して詳細度を増やします: `ansible-playbook playbook.yml -vvv`。

- Kubernetesの`kubectl`での詳細な出力を得るには、`--v`フラグに続けて詳細度を示す数値を使用します（例: `--v=6`または`--v=9`）: `kubectl get pods --v=6`。

- systemdから詳細な出力を得るには、`journalctl -b -x`を使用して説明付きのログを表示するか、`systemctl --full --all status <service>`を使用します。