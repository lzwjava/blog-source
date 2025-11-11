---
audio: false
generated: true
lang: hant
layout: post
title: 香港傳統文化節
translated: true
type: note
---

以下是在各種工具和系統中啟用詳細輸出模式的補充範例，進一步擴展了提供更詳細回饋或記錄的主題：

- **PowerShell**：要啟用詳細輸出，請在支援的 cmdlet 中使用 `-Verbose` 參數。例如：  
  ```powershell
  Get-Process -Verbose
  ```
  或者全域設定 `$VerbosePreference` 變數：  
  ```powershell
  $VerbosePreference = "Continue"
  ```

- **CMake**：在建置過程中取得詳細輸出，請使用 `--verbose` 旗標或設定 `VERBOSE=1`：  
  ```bash
  cmake --build . --verbose
  ```
  或：  
  ```bash
  make VERBOSE=1
  ```

- **Make**：要啟用詳細輸出並查看所有執行的指令，請使用 `-d` 旗標進行除錯，或避免使用 `@` 靜默輸出：  
  ```bash
  make -d
  ```
  或編輯 Makefile 以移除指令前的 `@` 前綴。

- **GCC (GNU 編譯器套件)**：要取得詳細編譯輸出，請使用 `-v` 旗標：  
  ```bash
  gcc -v -o output source.c
  ```

- **GDB (GNU 除錯器)**：要增加詳細程度，請在 GDB 中使用 `set verbose on` 指令：  
  ```gdb
  (gdb) set verbose on
  (gdb) run
  ```

- **Ruby**：使用 `-v` 或 `--verbose` 旗標以詳細模式執行 Ruby 腳本：  
  ```bash
  ruby -v script.rb
  ```
  若要取得額外警告，請使用 `-w`：  
  ```bash
  ruby -w script.rb
  ```

- **Perl**：使用 `-v` 旗標啟用詳細輸出，或使用 `diagnostics` 編譯指示取得詳細錯誤訊息：  
  ```bash
  perl -v script.pl
  ```
  或在腳本中：  
  ```perl
  use diagnostics;
  ```

- **PHP**：透過在 `php.ini` 中設定 `error_reporting` 和 `display_errors`，以詳細錯誤報告模式執行 PHP 腳本：  
  ```ini
  error_reporting = E_ALL
  display_errors = On
  ```
  或從命令列：  
  ```bash
  php -d error_reporting=E_ALL script.php
  ```

- **R**：要在 R 腳本中啟用詳細輸出，請在支援的函數中使用 `verbose=TRUE` 參數（例如 `install.packages`）：  
  ```R
  install.packages("dplyr", verbose=TRUE)
  ```

- **Go (Golang)**：在編譯或測試時取得詳細輸出，請使用 `-v` 旗標：  
  ```bash
  go build -v
  go test -v
  ```

- **Rust (Cargo)**：使用 Cargo 的 `-v` 或 `-vv` 旗標啟用詳細輸出：  
  ```bash
  cargo build -v
  cargo run -vv
  ```

- **Jenkins**：要為流水線啟用詳細記錄，請在腳本中添加 `verbose` 選項或在任務設定中配置主控台輸出。例如在 Jenkinsfile 中：  
  ```groovy
  sh 'some_command --verbose'
  ```
  或者，在啟動 Jenkins 時設定系統屬性 `-Dhudson.model.TaskListener.verbose=true`。

- **Vagrant**：使用 `--debug` 旗標取得詳細輸出：  
  ```bash
  vagrant up --debug
  ```

- **Puppet**：使用 `--verbose` 或 `--debug` 旗標以增加詳細程度執行 Puppet：  
  ```bash
  puppet apply site.pp --verbose
  puppet apply site.pp --debug
  ```

- **Chef**：使用 `-l`（記錄等級）旗標啟用詳細輸出：  
  ```bash
  chef-client -l debug
  ```

- **SaltStack**：使用 `-l` 旗標增加詳細程度（例如 `debug` 或 `trace`）：  
  ```bash
  salt '*' test.ping -l debug
  ```

- **PostgreSQL (psql)**：要從 `psql` 取得詳細輸出，請使用 `-e` 旗標回顯查詢，或使用 `\set VERBOSITY verbose` 取得詳細錯誤訊息：  
  ```bash
  psql -e -f script.sql
  ```
  或在 `psql` 中：  
  ```sql
  \set VERBOSITY verbose
  ```

- **MySQL**：使用 `--verbose` 以詳細輸出模式執行 MySQL 用戶端：  
  ```bash
  mysql --verbose < script.sql
  ```

- **SQLite**：使用 `.explain` 指令取得詳細查詢執行計劃：  
  ```sqlite
  sqlite3 database.db
  sqlite> .explain
  sqlite> SELECT * FROM table;
  ```

- **MongoDB**：透過使用 `-v` 旗標啟動 `mongod` 啟用詳細記錄（最多可使用 `-vvvvv` 取得更多細節）：  
  ```bash
  mongod -v
  ```

- **Elasticsearch**：透過調整 `log4j2.properties` 檔案以詳細記錄模式啟動 Elasticsearch：  
  ```properties
  logger.action.level = debug
  ```
  或在啟動時傳遞 `--verbose`：  
  ```bash
  elasticsearch --verbose
  ```

- **NGINX**：使用 `-T` 測試配置並取得詳細輸出：  
  ```bash
  nginx -T
  ```
  若要取得執行時詳細資訊，請在 `nginx.conf` 中提高 `error_log` 等級：  
  ```nginx
  error_log /var/log/nginx/error.log debug;
  ```

- **Apache HTTP Server**：透過在 `httpd.conf` 或 `apache2.conf` 中設定 `LogLevel` 指令啟用詳細記錄：  
  ```apache
  LogLevel debug
  ```

- **OpenSSL**：使用如 `s_client` 等指令取得詳細輸出：  
  ```bash
  openssl s_client -connect example.com:443 -debug
  ```

- **JUnit (Java 測試)**：透過配置測試執行器（例如 Maven Surefire 插件）以詳細輸出模式執行 JUnit 測試：  
  ```xml
  <configuration>
      <argLine>-verbose</argLine>
  </configuration>
  ```

這些範例涵蓋了程式語言、建置系統、資料庫、伺服器及 DevOps 工具等多種領域的廣泛工具。如果您需要任何特定工具的更多詳細範例或細節，請告訴我！