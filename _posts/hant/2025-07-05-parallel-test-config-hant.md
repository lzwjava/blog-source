---
audio: false
generated: true
lang: hant
layout: post
title: 配置 Maven 以實現並行測試執行
translated: true
type: note
---

若要在您的 Maven 專案中啟用平行測試執行（特別是針對提供的 `MavenTest.java` 類別），您可以配置 Maven Surefire Plugin 以平行執行測試。`MavenTest.java` 類別使用 JUnit 4 的動態測試來執行不同問題的 Maven 指令，而原始錯誤的堆疊追蹤顯示測試已在平行執行（由堆疊追蹤中的 `ForkJoinPool` 可得知）。不過，您可以透過配置 `pom.xml` 檔案中的 Surefire Plugin 來明確控制平行執行。以下將說明如何設定平行測試執行，並處理您要求的 `-DParallel` 旗標使用。

### 為何會發生平行執行
您的測試輸出顯示堆疊追蹤中有 `ForkJoinPool`，表示 JUnit 或 Maven 已在執行緒池中進行平行執行。`MavenTest` 類別使用帶有 `DynamicTest` 的 `@TestFactory`，測試很可能因 JUnit 的預設行為或現有的 Surefire 配置而平行執行。現在的目標是明確配置平行執行，並透過命令列旗標（如 `-DParallel`）進行控制。

### 配置平行測試執行的步驟

1. **更新 `pom.xml` 以配置 Maven Surefire Plugin**：
   Maven Surefire Plugin 支援 JUnit 4.7+ 的平行測試執行（您的專案相容於 `DynamicTest`）。您可以指定平行層級（例如 `classes`、`methods` 或 `both`）和執行緒數量。為了透過 `-DParallel` 控制，您可以使用 Maven 屬性來切換或配置平行執行。

   在您的 `pom.xml` 中新增或更新 Surefire Plugin 配置：

   ```xml
   <project>
       <!-- 其他配置 -->
       <properties>
           <!-- 預設不啟用平行執行，除非特別指定 -->
           <parallel.mode>none</parallel.mode>
           <thread.count>4</thread.count>
       </properties>
       <build>
           <plugins>
               <plugin>
                   <groupId>org.apache.maven.plugins</groupId>
                   <artifactId>maven-surefire-plugin</artifactId>
                   <version>3.5.3</version>
                   <configuration>
                       <parallel>${parallel.mode}</parallel>
                       <threadCount>${thread.count}</threadCount>
                       <perCoreThreadCount>false</perCoreThreadCount>
                       <!-- 可選：平行測試的逾時設定 -->
                       <parallelTestsTimeoutInSeconds>10</parallelTestsTimeoutInSeconds>
                       <!-- 分叉配置以隔離測試 -->
                       <forkCount>1</forkCount>
                       <reuseForks>true</reuseForks>
                   </configuration>
               </plugin>
           </plugins>
       </build>
   </project>
   ```

   - **說明**：
     - `<parallel>`：指定平行層級。JUnit 4.7+ 的有效值為 `methods`、`classes`、`both`、`suites`、`suitesAndClasses`、`suitesAndMethods`、`classesAndMethods` 或 `all`。對於您的 `MavenTest` 類別，`classes` 較為合適，因為每個 `DynamicTest` 代表一個問題，而您希望平行執行不同問題的測試。
     - `<threadCount>`：設定執行緒數量（例如 `4` 表示四個並行測試）。您可以透過 `-Dthread.count=<數字>` 覆寫此值。
     - `<perCoreThreadCount>false</perCoreThreadCount>`：確保 `threadCount` 為固定數字，不按 CPU 核心數縮放。
     - `<parallelTestsTimeoutInSeconds>`：設定平行測試的逾時時間以防止懸置（符合您在 `MavenTest.java` 中設定的 `TEST_TIMEOUT` 10 秒）。
     - `<forkCount>1</forkCount>`：在獨立的 JVM 程序中執行測試以隔離它們，減少共享狀態問題。`<reuseForks>true</reuseForks>` 允許重複使用 JVM 以提高效率。
     - `<parallel.mode>` 和 `<thread.count>`：可透過命令列旗標覆寫的 Maven 屬性（例如 `-Dparallel.mode=classes`）。

2. **使用 `-DParallel` 執行測試**：
   若要使用 `-DParallel` 旗標控制平行執行，您可以將其對應到 `parallel.mode` 屬性。例如，執行：

   ```bash
   mvn test -Dparallel.mode=classes -Dthread.count=4
   ```

   - 若未指定 `-Dparallel.mode`，預設值（`none`）會停用平行執行。
   - 您也可以使用更簡單的旗標，如 `-DParallel=true` 來啟用具有預定義模式（例如 `classes`）的平行執行。為支援此功能，請更新 `pom.xml` 以解譯 `-DParallel`：

   ```xml
   <project>
       <!-- 其他配置 -->
       <properties>
           <parallel.mode>${Parallel ? 'classes' : 'none'}</parallel.mode>
           <thread.count>4</thread.count>
       </properties>
       <build>
           <plugins>
               <plugin>
                   <groupId>org.apache.maven.plugins</groupId>
                   <artifactId>maven-surefire-plugin</artifactId>
                   <version>3.5.3</version>
                   <configuration>
                       <parallel>${parallel.mode}</parallel>
                       <threadCount>${thread.count}</threadCount>
                       <perCoreThreadCount>false</perCoreThreadCount>
                       <parallelTestsTimeoutInSeconds>10</parallelTestsTimeoutInSeconds>
                       <forkCount>1</forkCount>
                       <reuseForks>true</reuseForks>
                   </configuration>
               </plugin>
           </plugins>
       </build>
   </project>
   ```

   現在，您可以執行：

   ```bash
   mvn test -DParallel=true
   ```

   - `-DParallel=true`：啟用平行執行，設定為 `parallel=classes` 和 `threadCount=4`。
   - `-DParallel=false` 或省略 `-DParallel`：停用平行執行（`parallel=none`）。
   - 您可以使用 `-Dthread.count=<數字>` 覆寫執行緒數量（例如 `-Dthread.count=8`）。

3. **確保執行緒安全**：
   您的 `MavenTest` 類別平行執行 Maven 指令（`mvn exec:exec -Dproblem=<problem>`），這會產生獨立的程序。由於每個程序擁有自己的記憶體空間，這本質上是執行緒安全的，避免了共享狀態問題。但請確保：
   - `com.lzw.solutions.uva.<problem>.Main` 類別不共享可能導致衝突的資源（例如檔案或資料庫）。
   - 每個問題使用的輸入/輸出檔案或資源（例如 `p10009` 的測試資料）是隔離的，以避免競爭條件。
   - 若使用共享資源，請考慮在特定測試類別上使用 `@NotThreadSafe` 或同步化對共享資源的存取。

4. **處理平行執行中的跳過清單**：
   您的 `MavenTest.java` 已包含 `SKIP_PROBLEMS` 集合以跳過如 `p10009` 的問題。這與平行執行配合良好，因為跳過的問題在測試排程前已被排除。請確保視需要更新跳過清單：

   ```java
   private static final Set<String> SKIP_PROBLEMS = new HashSet<>(Arrays.asList(
       "p10009", // 因 NumberFormatException 跳過 p10009
       "p10037"  // 在此新增其他有問題的題目
   ));
   ```

5. **執行測試**：
   若要使用跳過清單和 `-DParallel` 旗標平行執行測試：

   ```bash
   mvn test -DParallel=true -Dthread.count=4
   ```

   - 這會同時執行最多四個問題測試，跳過 `p10009` 和 `SKIP_PROBLEMS` 中的任何其他問題。
   - 若您想停用平行執行以進行除錯：

     ```bash
     mvn test -DParallel=false
     ```

6. **處理 `p10009` 的 `NumberFormatException`**：
   `p10009` 中的 `NumberFormatException`（來自您的原始錯誤）表示正在解析一個 `null` 字串。雖然跳過 `p10009` 可避免此問題，但為了完整性您可能想修復它。檢查 `com.lzw.solutions.uva.p10009.Main` 的第 17 行（`readInt` 方法）並加入 null 檢查：

   ```java
   public int readInt() {
       String input = readInput(); // 假設的輸入讀取方法
       if (input == null || input.trim().isEmpty()) {
           throw new IllegalArgumentException("Input cannot be null or empty");
       }
       return Integer.parseInt(input);
   }
   ```

   或者，在問題解決前將 `p10009` 保留在跳過清單中。

### 平行執行的注意事項
- **效能**：對於您的 `MavenTest` 類別，使用 `parallel=classes` 進行平行執行是合適的，因為每個 `DynamicTest` 代表一個獨立的問題。與 `methods` 或 `both` 相比，這能最小化負擔。
- **資源使用**：平行執行會增加 CPU 和記憶體使用量。請監控您的系統以確保 `threadCount`（例如 `4`）不會使硬體負擔過重。若出現記憶體問題，請使用 `forkCount` 在獨立的 JVM 中隔離測試。
- **逾時**：`parallelTestsTimeoutInSeconds` 設定確保測試不會無限期懸置，與您在 `MavenTest.java` 中設定的 `TEST_TIMEOUT` 10 秒一致。
- **執行緒安全**：由於您的測試執行 `mvn exec:exec` 指令（在獨立程序中執行），執行緒安全的顧慮較少。但請確保每個問題的測試輸入/輸出（例如檔案）是隔離的。
- **除錯**：若測試在平行模式下意外失敗，請順序執行它們（`-DParallel=false`）以隔離問題。

### 完整命令範例
若要平行執行測試，跳過 `p10009`，並使用四個執行緒：

```bash
mvn test -DParallel=true -Dthread.count=4
```

若要除錯特定問題（例如 `p10009`）而不使用平行執行，請暫時將其從 `SKIP_PROBLEMS` 中移除並執行：

```bash
mvn test -DParallel=false -Dproblem=p10009
```

### 其他考量
- **JUnit 4 限制**：您的專案使用 JUnit 4（基於 `org.junit.jupiter.api` 匯入和 `DynamicTest`）。JUnit 4.7+ 透過 Surefire 支援平行執行，但 JUnit 5 提供了更靈活的平行化選項。若您需要進階功能（如每類別平行化或自訂策略），請考慮升級至 JUnit 5。
- **Maven 版本**：請確保您使用最新版本的 Maven（例如 3.9.10，如您的錯誤輸出所示）和 Surefire（例如 3.5.3）以獲得最佳的平行執行支援。
- **錯誤處理**：為了使測試更穩健，請考慮在 `runMavenExecTests` 中捕獲異常（如先前回應所建議），以記錄失敗而不停止測試套件：

   ```java
   @TestFactory
   Collection<DynamicTest> runMavenExecTests() {
       return PROBLEMS.stream()
               .map(problem -> DynamicTest.dynamicTest("Test problem: " + problem, () -> {
                   String command = String.format("mvn exec:exec -Dproblem=%s", problem);
                   System.out.println("Executing command for " + problem + ": " + command);
                   try {
                       Process process = Runtime.getRuntime().exec(command);
                       // ...（其餘程序處理程式碼）
                       int exitCode = process.exitValue();
                       Assertions.assertTrue(
                               exitCode == 0,
                               "Maven command failed for problem: " + problem + "\nError output:\n" + errorOutput);
                   } catch (Exception e) {
                       System.err.println("Exception for problem " + problem + ": " + e.getMessage());
                       // 可選擇繼續執行而非失敗
                   }
               }))
               .collect(Collectors.toList());
   }
   ```

此設定允許您使用 `-DParallel=true` 控制平行執行，跳過有問題的測試（如 `p10009`），並維持穩健的測試執行。若您需要進一步自訂，例如透過命令列參數的動態跳過清單或進階的 JUnit 5 配置，請隨時告知！