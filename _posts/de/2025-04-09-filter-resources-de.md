---
audio: false
generated: true
lang: de
layout: post
title: Projektdateien in VSCode
translated: true
type: note
---

Dieses Problem mit dem `filterResources`-Tag, das wiederholt zu Ihrer `.project`-Datei in Maven Spring Boot-Projekten hinzugefügt wird, wird typischerweise durch die Eclipse/M2Eclipse-Integration verursacht, die im Hintergrund stattfindet.

Wenn Sie in einer IDE (selbst VSCode) an einem Maven-Projekt arbeiten, können die Maven-Plugins automatisch Eclipse-Projektdateien (wie `.project`) generieren oder modifizieren. Das `filterResources`-Tag wird speziell dann hinzugefügt, wenn Maven Resource Filtering in Ihrem Projekt konfiguriert ist.

Hier sind einige Ansätze, um diese automatische Generierung zu verhindern:

1. **Konfigurieren Sie Ihre m2e Plugin-Einstellungen**:
   Sie können Ihre pom.xml so konfigurieren, dass sie dem m2e Plugin mitteilt, wie es mit Resource Filtering umgehen soll, ohne die .project-Datei zu modifizieren:

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

2. **VSCode-spezifische Einstellungen**:
   In VSCode verwenden Sie möglicherweise die Java- oder Maven-Erweiterungen. Sie können deren Einstellungen überprüfen, um zu sehen, ob Sie die automatische Generierung oder Modifikation von Eclipse-Projektdateien deaktivieren können:
   
   - Öffnen Sie die Einstellungen (Strg+,)
   - Suchen Sie nach "maven" oder "java" Einstellungen bezüglich Projektgenerierung
   - Suchen Sie nach Optionen wie "Update Configuration" oder "Project Generation"

3. **Verwenden Sie .gitattributes anstelle von .gitignore**:
   Wenn Sie die Datei behalten, aber verhindern möchten, dass Git Änderungen daran erkennt:

   ```
   moduleA/.project merge=ours
   ```

   Dies weist Git an, während Merges immer Ihre Version beizubehalten.

4. **Überprüfen Sie Ihre Workspace-Einstellungen**:
   Prüfen Sie, ob irgendwelche VSCode-Erweiterungen automatisch Maven-Befehle ausführen, die dieses Verhalten auslösen könnten.

Die genaue Lösung könnte davon abhängen, welche Maven/Java-Erweiterungen Sie in VSCode verwenden. Wenn Sie mitteilen, welche spezifischen Erweiterungen Sie für die Maven/Java-Entwicklung verwenden, könnte ich gezieltere Ratschläge geben.