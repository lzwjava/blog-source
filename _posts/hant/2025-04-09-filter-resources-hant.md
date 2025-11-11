---
audio: false
generated: true
lang: hant
layout: post
title: VSCode 中的項目檔案
translated: true
type: note
---

在 Maven Spring Boot 專案中，`.project` 檔案重複出現 `filterResources` 標籤的問題，通常是由於 Eclipse/M2Eclipse 整合在背景運作所導致。

當您在 IDE（即使是 VSCode）中處理 Maven 專案時，Maven 插件會自動生成或修改 Eclipse 專案檔案（例如 `.project`）。特別是當您的專案配置了 Maven 資源過濾功能時，就會自動添加 `filterResources` 標籤。

以下提供幾種防止自動生成的方法：

1. **配置 m2e 插件設定**：
   您可以在 pom.xml 中添加配置，指示 m2e 插件如何處理資源過濾而不修改 .project 檔案：

   ```xml
   <build>
     <pluginManagement>
       <plugins>
         <plugin>
           <groupId>org.eclipse.m2e</groupId>
           <artifactId>lifecycle-mapping</artifactId>
           <version>1.0.0</version>
           <configuration>
             <lifecycleMappingMetadata>
               <pluginExecutions>
                 <pluginExecution>
                   <pluginExecutionFilter>
                     <groupId>org.apache.maven.plugins</groupId>
                     <artifactId>maven-resources-plugin</artifactId>
                     <versionRange>[2.0,)</versionRange>
                     <goals>
                       <goal>resources</goal>
                       <goal>testResources</goal>
                     </goals>
                   </pluginExecutionFilter>
                   <action>
                     <ignore />
                   </action>
                 </pluginExecution>
               </pluginExecutions>
             </lifecycleMappingMetadata>
           </configuration>
         </plugin>
       </plugins>
     </pluginManagement>
   </build>
   ```

2. **VSCode 特定設定**：
   在 VSCode 中，您可能正在使用 Java 或 Maven 擴充功能。您可以檢查其設定以查看是否能停用自動生成或修改 Eclipse 專案檔案的功能：
   
   - 開啟設定（Ctrl+,）
   - 搜尋與專案生成相關的「maven」或「java」設定
   - 尋找如「更新配置」或「專案生成」等選項

3. **使用 .gitattributes 替代 .gitignore**：
   若想保留檔案但防止 Git 偵測其變更：

   ```
   moduleA/.project merge=ours
   ```

   這會指示 Git 在合併時始終保留您的版本

4. **檢查工作區設定**：
   確認是否有任何 VSCode 擴充功能正在自動執行可能觸發此行為的 Maven 指令

具體解決方案可能取決於您在 VSCode 中使用的 Maven/Java 擴充功能。如果您能分享正在使用的具體 Maven/Java 開發擴充功能，我可以提供更具針對性的建議。