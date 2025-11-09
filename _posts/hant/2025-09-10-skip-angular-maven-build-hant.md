---
audio: false
date: 2025-09-10
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: 跳過 Maven 中的 Angular 構建
translated: true
type: note
---

簡短回答：可以——你可以跳過 Angular/npm 構建，但無法使用內建標記如 `--skip-web`。請使用以下其中一種方法。

### 1) 在多模組構建中排除網頁模組

如果你的 Angular 應用程式是獨立的 Maven 模組（例如 `web`），只需在反應器中排除它：

```
mvn -pl '!web' -am clean package
```

或僅構建後端模組：

```
mvn -pl :backend -am clean package
```

（`-am` 會構建任何需要的依賴項；`!web` 語法會排除該模組。）

### 2) 新增「跳過前端」屬性（適用於 frontend-maven-plugin 或 exec）

使用屬性保護 npm 目標，並從命令列切換它。

**POM（網頁模組或父級）：**

```xml
<properties>
  <skip.frontend>false</skip.frontend>
</properties>

<build>
  <plugins>
    <!-- 範例：com.github.eirslett:frontend-maven-plugin -->
    <plugin>
      <groupId>com.github.eirslett</groupId>
      <artifactId>frontend-maven-plugin</artifactId>
      <version>...你的版本...</version>
      <configuration>
        <skip>${skip.frontend}</skip>
      </configuration>
      <executions>
        <execution>
          <id>npm-build</id>
          <phase>prepare-package</phase>
          <goals>
            <goal>npm</goal>
          </goals>
          <configuration>
            <arguments>run build</arguments>
          </configuration>
        </execution>
      </executions>
    </plugin>

    <!-- 如果你使用 exec-maven-plugin 呼叫 npm -->
    <plugin>
      <groupId>org.codehaus.mojo</groupId>
      <artifactId>exec-maven-plugin</artifactId>
      <version>...你的版本...</version>
      <executions>
        <execution>
          <id>npm-build</id>
          <phase>prepare-package</phase>
          <goals><goal>exec</goal></goals>
          <configuration>
            <skip>${skip.frontend}</skip>
            <executable>npm</executable>
            <arguments>
              <argument>run</argument>
              <argument>build</argument>
            </arguments>
          </configuration>
        </execution>
      </executions>
    </plugin>
  </plugins>
</build>
```

**命令列：**

```
mvn -Dskip.frontend=true clean package
```

### 3) 使用 Maven 設定檔

僅在「with-frontend」設定檔中綁定前端構建，並在開發中將「skip-frontend」設定檔設為預設。

**POM：**

```xml
<profiles>
  <profile>
    <id>with-frontend</id>
    <activation>
      <property>
        <name>!skip.frontend</name>
      </property>
    </activation>
    <build>
      <plugins>
        <!-- 同上方的插件配置，但不含 skip -->
      </plugins>
    </build>
  </profile>
</profiles>
```

**命令列：**

* 正常（跳過）：`mvn -Dskip.frontend clean package`
* 發佈（構建 UI）：`mvn -Pwith-frontend clean package`

---

## 如果你*確實*需要構建 UI 的加速技巧

* 確保 Angular 的持久快取已開啟（Angular CLI 預設快取；在 CI 中保留 `node_modules` 和 `.angular/cache` 的快取）。
* 僅在發佈時執行 `ng build`；在開發中，單獨提供 UI 服務（`npm start`），並讓 Spring 提供預先構建的靜態資源（例如，將 `dist/` 放在 `src/main/resources/static` 下以用於打包構建）。
* 考慮拆分儲存庫，使 Angular 應用程式完全不是 Maven 模組；僅在前端檔案變更時構建它。
* 如果你使用較新的 Angular，請使用預設的 esbuild/Vite 構建器，並在 CI 發佈構建中停用源映射。

---

### 總結

使用 `-pl '!web'` 排除網頁模組，**或**新增 `skip.frontend` 屬性並配置你的插件執行以遵循它。雖然沒有標準的 `mvn package --skip-web`，但以上兩種模式既可靠又常見。