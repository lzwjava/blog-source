---
audio: false
generated: true
lang: hant
layout: post
title: Checkstyle 設定檔位置
translated: true
type: note
---

要解決執行 `mvn clean checkstyle:check` 時遇到的 `maven-checkstyle-plugin` 問題（包括找不到 `checks.xml` 檔案以及初始化 `SuppressWithNearbyTextFilter` 模組失敗），請按照以下步驟操作。這些問題源於檔案位置設定與不相容的 Checkstyle 版本。以下是完整解決方案：

---

### 步驟 1：修正 `checks.xml` 檔案位置
錯誤訊息顯示外掛程式無法找到 `checks.xml`。由於該檔案位於專案根目錄（而非外掛程式通常尋找的 `src/main/resources` 目錄），您需要明確告知外掛程式其位置。

- **操作**：更新 `pom.xml` 中的 `<configLocation>`，指向專案根目錄。

---

### 步驟 2：解決 `SuppressWithNearbyTextFilter` 錯誤
`SuppressWithNearbyTextFilter` 模組初始化失敗，原因是外掛程式使用的 Checkstyle 版本過舊，不支援此篩選器。您需要升級外掛程式並指定相容的 Checkstyle 版本。

- **操作**：將 `maven-checkstyle-plugin` 升級至版本 `3.3.1`，並新增對 Checkstyle 版本 `10.17.0` 的依賴，該版本支援 `SuppressWithNearbyTextFilter`。

---

### 更新後的 `pom.xml` 配置
按以下方式修改 `pom.xml` 中的 `maven-checkstyle-plugin` 區段：

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-checkstyle-plugin</artifactId>
    <version>3.3.1</version> <!-- 升級至最新版本 -->
    <configuration>
        <configLocation>${project.basedir}/checks.xml</configLocation> <!-- 指向專案根目錄的 checks.xml -->
    </configuration>
    <dependencies>
        <dependency>
            <groupId>com.puppycrawl.tools</groupId>
            <artifactId>checkstyle</artifactId>
            <version>10.17.0</version> <!-- 支援 SuppressWithNearbyTextFilter -->
        </dependency>
    </dependencies>
    <executions>
        <execution>
            <id>checkstyle-check</id>
            <phase>compile</phase>
            <goals>
                <goal>check</goal>
            </goals>
        </execution>
    </executions>
</plugin>
```

#### 說明：
- **`<configLocation>${project.basedir}/checks.xml</configLocation>`**：指定 `checks.xml` 位於專案根目錄（`${project.basedir}` 是 Maven 屬性，代表根目錄）。
- **`version 3.3.1`**：使用較新的外掛程式版本以提升相容性。
- **Checkstyle `10.17.0` 依賴**：確保外掛程式使用包含 `SuppressWithNearbyTextFilter` 的 Checkstyle 版本。

---

### 步驟 3：驗證 `checks.xml` 配置
確保 `checks.xml` 中的 `SuppressWithNearbyTextFilter` 模組正確定義。範例配置可能如下：

```xml
<module name="SuppressWithNearbyTextFilter">
    <property name="nearbyTextPattern" value="@SuppressWarnings"/>
</module>
```

- **操作**：檢查 `checks.xml` 是否有拼寫錯誤或不正確的屬性。詳情請參閱 [Checkstyle 文件](https://checkstyle.org/filters/suppresswithnearbytextfilter.html)。
- **疑難排解提示**：若錯誤持續，請暫時從 `checks.xml` 中移除 `SuppressWithNearbyTextFilter` 模組，並執行 `mvn checkstyle:check` 以確認問題是否與此篩選器有關。

---

### 步驟 4：測試修正
- 執行以下指令進行測試：
  ```bash
  mvn clean checkstyle:check
  ```
- 若運作正常，外掛程式應能找到 `checks.xml` 並處理所有模組而無錯誤。
- 若要確保 Checkstyle 在編譯期間執行，請使用：
  ```bash
  mvn compile
  ```

---

### 可選方案：替代檔案位置
若您偏好更標準的 Maven 設定：
- 將 `checks.xml` 移至 `src/main/resources/checks.xml`。
- 將 `<configLocation>` 更新為：
  ```xml
  <configLocation>classpath:checks.xml</configLocation>
  ```
- 這符合 Maven 將資源置於 `src/main/resources` 的慣例。

---

### 補充說明
- **不相關警告**：若您在 `/usr/share/maven/conf/settings.xml` 中看到關於 `<blocked>` 標籤的警告，這與本問題無關，但表示您的 Maven 設定檔案可能存在問題。如有需要，請另行檢查。
- **問題仍未解決？** 請提供以下資訊以獲得進一步協助：
  - `checks.xml` 的內容（或片段）。
  - `mvn clean checkstyle:check -X` 的完整輸出（除錯模式）。

---

透過套用這些變更，`maven-checkstyle-plugin` 應能正確找到 `checks.xml` 並支援 `SuppressWithNearbyTextFilter`，從而解決您的錯誤。

---

您先前遇到的錯誤顯示 `maven-checkstyle-plugin` 無法在 classpath 中找到 `checks.xml`，隨後因 `SuppressWithNearbyTextFilter` 模組問題而失敗。從您更新的專案結構來看，`checks.xml` 位於專案根目錄（`~/Projects/blog-server/checks.xml`），而非先前假設的 `src/main/resources`。這解釋了為何外掛程式在配置為 `<configLocation>classpath:checks.xml</configLocation>` 或 `<configLocation>checks.xml</configLocation>` 時無法找到該檔案，因為這些設定預期檔案位於 classpath 中（通常是 `src/main/resources`）。

為解決此問題，並確保 `maven-checkstyle-plugin` 在執行 `mvn compile` 時使用您位於專案根目錄的自訂 `checks.xml`，您需要更新 `<configLocation>` 以指向檔案的絕對路徑或專案相對路徑。此外，您需要透過確保與 Checkstyle 版本的相容性來處理 `SuppressWithNearbyTextFilter` 問題。以下是逐步解決方案。

### 更新後的 `pom.xml` 配置
修改 `pom.xml` 中的 `maven-checkstyle-plugin`，以引用專案根目錄的 `checks.xml` 並使用相容的 Checkstyle 版本來支援 `SuppressWithNearbyTextFilter`。

```xml
<build>
    <resources>
        <resource>
            <directory>src/main/resources</directory>
            <includes>
                <include>**/*.xml</include>
                <include>**/*.yaml</include>
            </includes>
        </resource>
    </resources>
    <plugins>
        <plugin>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-maven-plugin</artifactId>
            <version>3.4.2</version>
            <executions>
                <execution>
                    <goals>
                        <goal>repackage</goal>
                    </goals>
                </execution>
            </executions>
        </plugin>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-surefire-plugin</artifactId>
            <version>3.0.0-M8</version>
        </plugin>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-checkstyle-plugin</artifactId>
            <version>3.3.1</version> <!-- 最新版本以提升相容性 -->
            <configuration>
                <configLocation>${project.basedir}/checks.xml</configLocation> <!-- 指向專案根目錄的 checks.xml -->
            </configuration>
            <dependencies>
                <dependency>
                    <groupId>com.puppycrawl.tools</groupId>
                    <artifactId>checkstyle</artifactId>
                    <version>10.17.0</version> <!-- 支援 SuppressWithNearbyTextFilter -->
                </dependency>
            </dependencies>
            <executions>
                <execution>
                    <id>checkstyle-check</id>
                    <phase>compile</phase>
                    <goals>
                        <goal>check</goal>
                    </goals>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```

### 變更說明
1. **更新 `<configLocation>`**：
   - 改為 `${project.basedir}/checks.xml` 以指向專案根目錄的 `checks.xml`（`~/Projects/blog-server/checks.xml`）。
   - `${project.basedir}` 會解析為包含 `pom.xml` 的目錄，確保外掛程式無論 classpath 如何都能找到檔案。

2. **升級外掛程式版本**：
   - 將 `maven-checkstyle-plugin` 更新至 `3.3.1`（截至 2025 年 6 月的最新版本）以提升相容性並修復錯誤。

3. **新增 Checkstyle 依賴**：
   - 新增 Checkstyle `10.17.0` 的 `<dependency>`，該版本包含對 `SuppressWithNearbyTextFilter` 的支援。`maven-checkstyle-plugin:3.1.1` 中的預設 Checkstyle 版本（`8.29`）不支援此篩選器，導致先前錯誤。

4. **保留 `<phase>compile</phase>`**：
   - 確保 `checkstyle:check` 在 `mvn compile` 期間執行，如您所要求。

5. **Resources 區段**：
   - 保留 `<resources>` 區段以確保 `src/main/resources` 中的檔案（如 `application.yaml`）被處理，儘管這與 `checks.xml` 無直接關聯，因為它現在位於專案根目錄。

### 驗證 `checks.xml` 內容
關於 `SuppressWithNearbyTextFilter` 的錯誤表明您的 `checks.xml` 引用了此篩選器。請確保其正確配置。有效範例：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE module PUBLIC
    "-//Checkstyle//DTD Checkstyle Configuration 1.3//EN"
    "https://checkstyle.org/dtds/configuration_1_3.dtd">
<module name="Checker">
    <module name="SuppressWithNearbyTextFilter">
        <!-- 範例屬性，請根據需要調整 -->
        <property name="nearbyTextPattern" value="@SuppressWarnings"/>
    </module>
    <module name="TreeWalker">
        <!-- 其他檢查 -->
        <module name="ConstantName"/>
    </module>
</module>
```

- **檢查**：開啟 `~/Projects/blog-server/checks.xml` 並驗證 `SuppressWithNearbyTextFilter` 拼寫正確且包含任何必要屬性（參閱 [Checkstyle 文件](https://checkstyle.org/filters/suppresswithnearbytextfilter.html)）。
- **操作**：若不確定，請暫時移除 `<module name="SuppressWithNearbyTextFilter"/>` 區段並測試以隔離問題。

### 測試配置
1. **清理專案**：
   ```bash
   mvn clean
   ```
   這會移除 `target` 目錄，包括 `checkstyle-checker.xml` 和 `checkstyle-result.xml`，確保沒有過時的產物干擾。

2. **執行 Checkstyle**：
   ```bash
   mvn checkstyle:check
   ```
   這會獨立測試 Checkstyle 配置。

3. **執行編譯**：
   ```bash
   mvn compile
   ```
   這應執行 Checkstyle（由於綁定至 `compile` 階段），然後在無違規導致建置失敗時進行編譯。

### 若問題持續存在則進行除錯
若遇到錯誤：
1. **檢查檔案路徑**：
   - 確認 `checks.xml` 存在於 `~/Projects/blog-server/checks.xml`。
   - 驗證檔案名稱確為 `checks.xml`（區分大小寫，無隱藏副檔名）。

2. **使用除錯記錄執行**：
   ```bash
   mvn clean checkstyle:check -X
   ```
   尋找關於 `checks.xml` 載入或 `SuppressWithNearbyTextFilter` 初始化的訊息。若錯誤持續，請分享相關輸出。

3. **使用精簡版 `checks.xml` 測試**：
   暫時將 `checks.xml` 替換為精簡配置以排除檔案內容問題：
   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE module PUBLIC
       "-//Checkstyle//DTD Checkstyle Configuration 1.3//EN"
       "https://checkstyle.org/dtds/configuration_1_3.dtd">
   <module name="Checker">
       <module name="TreeWalker">
           <module name="ConstantName"/>
       </module>
   </module>
   ```
   然後執行 `mvn checkstyle:check`。若此方法有效，則問題在於原始 `checks.xml` 中的 `SuppressWithNearbyTextFilter` 或其他模組。

### 補充說明
- **Settings.xml 警告**：您的輸出顯示關於 `/usr/share/maven/conf/settings.xml` 中無法識別的 `<blocked>` 標籤的警告。這與 Checkstyle 問題無關，但表示您的 Maven 配置可能存在問題。請檢查 `/usr/share/maven/conf/settings.xml` 的第 164 行，並移除或修正 `<blocked>` 標籤，因為它不是標準的 Maven 設定元素。
- **替代檔案位置**：若您偏好，可將 `checks.xml` 移至 `src/main/resources/checks.xml` 並將 `<configLocation>` 還原為 `classpath:checks.xml`。這對 Maven 專案而言更為慣例，因為資源會自動包含在 classpath 中。
- **違規時失敗**：若 Checkstyle 違規導致建置失敗，而您希望允許編譯繼續進行，請在外掛程式的 `<configuration>` 中新增 `<failOnViolation>false</failOnViolation>`：
  ```xml
  <configuration>
      <configLocation>${project.basedir}/checks.xml</configLocation>
      <failOnViolation>false</failOnViolation>
  </configuration>
  ```

### 驗證
套用變更後：
1. 執行 `mvn clean compile` 並確認：
   - Checkstyle 使用專案根目錄的 `checks.xml` 執行。
   - 未發生與 `checks.xml` 或 `SuppressWithNearbyTextFilter` 相關的錯誤。
   - 若 Checkstyle 通過或配置為不使建置失敗，則編譯繼續進行。
2. 檢查 `target/checkstyle-result.xml` 以查看 Checkstyle 結果。

若錯誤持續，請分享：
- `checks.xml` 的內容（或相關片段）。
- `mvn clean checkstyle:check -X` 的除錯輸出。
- 您嘗試透過 `SuppressWithNearbyTextFilter` 強制執行的任何特定 Checkstyle 規則。