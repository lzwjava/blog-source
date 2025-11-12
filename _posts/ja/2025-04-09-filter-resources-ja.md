---
audio: false
generated: true
lang: ja
layout: post
title: VSCodeのプロジェクトファイル
translated: true
type: note
---

Maven Spring Bootプロジェクトで`.project`ファイルに`filterResources`タグが繰り返し追加されるこの問題は、通常、バックグラウンドで動作するEclipse/M2Eclipse連携によって引き起こされます。

IDE（VSCodeでも）でMavenプロジェクトを操作している場合、Mavenプラグインが自動的にEclipseプロジェクトファイル（`.project`など）を生成または変更することがあります。`filterResources`タグは特に、プロジェクトでMavenリソースフィルタリングが設定されている場合に追加されます。

この自動生成を防ぐためのいくつかの方法を以下に示します：

1. **m2eプラグイン設定の構成**：
   pom.xmlに設定を追加して、m2eプラグインが.projectファイルを変更せずにリソースフィルタリングを処理する方法を指定できます：

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

2. **VSCode固有の設定**：
   VSCodeでは、JavaまたはMaven拡張機能を使用している可能性があります。設定で自動的なEclipseプロジェクトファイルの生成や変更を無効にできるか確認できます：
   
   - 設定を開く（Ctrl+,）
   - プロジェクト生成に関連する「maven」または「java」設定を検索
   - 「Update Configuration」や「Project Generation」などのオプションを探す

3. **`.gitignore`の代わりに`.gitattributes`を使用**：
   ファイルを保持したいが、Gitがその変更を検知しないようにする場合：

   ```
   moduleA/.project merge=ours
   ```

   これは、マージ中に常にあなたのバージョンを保持するようにGitに指示します。

4. **ワークスペース設定の確認**：
   この動作を引き起こす可能性のあるMavenコマンドを自動実行しているVSCode拡張機能がないか確認してください。

正確な解決策は、VSCodeで使用している特定のMaven/Java拡張機能によって異なる場合があります。Maven/Java開発に使用している具体的な拡張機能を共有していただければ、より対象を絞ったアドバイスを提供できます。