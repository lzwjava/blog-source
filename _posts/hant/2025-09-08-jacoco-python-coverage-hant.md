---
audio: false
date: 2025-09-08
generated: true
image: false
lang: hant
layout: post
title: Python 測試的 JaCoCo 覆蓋率策略
translated: true
type: note
---

# 使用 Python 整合測試的 JaCoCo 覆蓋率分析與策略

## 現狀分析

您已建立一個多模組 Maven 專案，包含：
- 父 POM（`PlaygroundLib`）
- `PlaygroundUtils` 模組（包含工具類別的 JAR）
- `PlaygroundWeb` 模組（包含 Spring MVC 控制器的 WAR）

您的目標是使用 Python 的 `unittest` 來測試 API 端點，並為 Java 程式碼生成覆蓋率報告。挑戰在於 Python 測試位於 Java 專案外部，且需要在測試期間運行 Jetty 來提供應用程式服務。

## 當前方法的問題

1. **多次運行問題**：您需要多次運行 `PlaygroundWeb` 來為不同模組生成獨立的覆蓋率報告，效率低下。

2. **擴展性顧慮**：此方法在模組數量增加時無法良好擴展。對於擁有 10 個模組的專案，您需要進行 10 次獨立運行。

3. **覆蓋率碎片化**：按模組生成的報告使得難以獲得整個應用程式的整體覆蓋率視圖。

## 推薦策略

### 1. 統一覆蓋率收集方法

我建議不要多次運行應用程式，而是：

1. **一次性運行附帶 JaCoCo 代理的 Web 應用程式**
2. **對此單一實例執行所有 Python 整合測試**
3. **生成包含所有模組的統一覆蓋率報告**

這種方法更有效率，並能提供整個應用程式的統一覆蓋率視圖。

### 2. 實施步驟

#### 父 POM（`PlaygroundLib`）修改

為整合測試添加 JaCoCo 配置檔：

```xml
<profiles>
    <profile>
        <id>integration-test</id>
        <build>
            <plugins>
                <plugin>
                    <groupId>org.jacoco</groupId>
                    <artifactId>jacoco-maven-plugin</artifactId>
                    <executions>
                        <execution>
                            <id>merge</id>
                            <phase>post-integration-test</phase>
                            <goals>
                                <goal>merge</goal>
                            </goals>
                            <configuration>
                                <fileSets>
                                    <fileSet>
                                        <directory>${project.basedir}</directory>
                                        <includes>
                                            <include>*/target/jacoco-it.exec</include>
                                        </includes>
                                    </fileSet>
                                </fileSets>
                                <destFile>${project.build.directory}/jacoco-merged.exec</destFile>
                            </configuration>
                        </execution>
                        <execution>
                            <id>report-merged</id>
                            <phase>verify</phase>
                            <goals>
                                <goal>report</goal>
                            </goals>
                            <configuration>
                                <dataFile>${project.build.directory}/jacoco-merged.exec</dataFile>
                                <outputDirectory>${project.reporting.outputDirectory}/jacoco-merged</outputDirectory>
                            </configuration>
                        </execution>
                    </executions>
                </plugin>
            </plugins>
        </build>
    </profile>
</profiles>
```

#### PlaygroundWeb POM 修改

修改 JaCoCo 代理配置以包含所有模組：

```xml
<plugin>
    <groupId>org.eclipse.jetty</groupId>
    <artifactId>jetty-maven-plugin</artifactId>
    <executions>
        <execution>
            <id>start-jetty</id>
            <phase>pre-integration-test</phase>
            <goals>
                <goal>start</goal>
            </goals>
            <configuration>
                <daemon>true</daemon>
                <jvmArgs>
                    -javaagent:${settings.localRepository}/org/jacoco/org.jacoco.agent/${jacoco.version}/org.jacoco.agent-${jacoco.version}-runtime.jar=destfile=${project.build.directory}/jacoco-it.exec,includes=org.lzw.*
                </jvmArgs>
                <!-- 其餘配置保持不變 -->
            </configuration>
        </execution>
        <!-- 其餘執行配置保持不變 -->
    </executions>
</plugin>
```

請注意 JaCoCo 代理配置中添加了 `includes=org.lzw.*`。這確保了 `org.lzw` 套件中的所有類別（跨所有模組）都會包含在覆蓋率報告中。

### 3. 執行流程

推薦的執行流程如下：

```bash
# 建置所有模組
mvn clean install

# 執行含覆蓋率的整合測試
mvn verify -Pintegration-test
```

這將：
1. 編譯所有模組
2. 啟動附帶 JaCoCo 代理的 Jetty
3. 運行 Python 整合測試
4. 停止 Jetty
5. 為所有模組生成合併的覆蓋率報告

### 4. 擴展至大型專案

對於擁有十個模組的大型專案：

1. **Web 模組**（如 `PlaygroundWeb`）將配置為運行附帶 JaCoCo 代理的應用程式。
2. **工具模組**（如 `PlaygroundUtils`）不需要特殊配置。
3. 父 POM 將處理來自所有模組的覆蓋率資料合併。

如果您有多個需要獨立測試的 Web 模組，可以為每個 Web 模組創建獨立的 Maven 配置檔，分別運行每個模組的整合測試，然後在父級別合併所有覆蓋率資料。

### 5. 應對 JaCoCo 複雜性

為管理 JaCoCo 的複雜性：

1. **將配置封裝**在 Maven 配置檔中，以保持主 POM 的整潔
2. **清晰記錄流程**，讓團隊成員了解如何運行測試和生成報告
3. **考慮 CI/CD 自動化**以減少開發人員的手動操作複雜性

## 總結

推薦的方法通過一次性運行附帶 JaCoCo 代理的 Web 應用程式，對此實例執行所有 Python 整合測試，並生成統一覆蓋率報告，來整合覆蓋率收集。這種方法更有效率、可擴展性更好，並能提供整個應用程式的統一覆蓋率視圖。

此策略應能解決您當前的挑戰，並在專案成長時良好擴展，同時簡化 JaCoCo 複雜性的管理。