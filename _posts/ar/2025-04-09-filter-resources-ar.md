---
audio: false
generated: true
lang: ar
layout: post
title: ملفات المشروع في في إس كود
translated: true
type: note
---

هذه المشكلة المتعلقة بإضافة وسم `filterResources` بشكل متكرر إلى ملف `.project` الخاص بك في مشاريع Maven Spring Boot تنتج عادةً عن تكامل Eclipse/M2Eclipse الذي يحدث في الخلفية.

عندما تعمل على مشروع Maven في بيئة التطوير المتكاملة (حتى VSCode)، يمكن لإضافات Maven أن تولد أو تعدل تلقائيًا ملفات مشروع Eclipse (مثل `.project`). يتم إضافة وسم `filterResources` تحديدًا عندما يكون تصفية موارد Maven مضبوطة في مشروعك.

إليك بعض الطرق لمنع هذا التوليد التلقائي:

1. **ضبط إعدادات إضافة m2e**:
   يمكنك إضافة إعدادات إلى ملف pom.xml الخاص بك تخبر إضافة m2e بكيفية التعامل مع تصفية الموارد دون تعديل ملف .project:

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

2. **إعدادات محددة لـ VSCode**:
   في VSCode، قد تستخدم إضافات Java أو Maven. يمكنك التحقق من إعداداتها لمعرفة ما إذا كان يمكنك تعطيل توليد أو تعديل ملف مشروع Eclipse تلقائيًا:
   
   - افتح الإعدادات (Ctrl+,)
   - ابحث عن إعدادات "maven" أو "java" المتعلقة بتوليد المشروع
   - ابحث عن خيارات مثل "Update Configuration" أو "Project Generation"

3. **استخدم .gitattributes بدلاً من .gitignore**:
   إذا كنت تريد الاحتفاظ بالملف، ولكن منع Git من رؤية التغييرات عليه:

   ```
   moduleA/.project merge=ours
   ```

   هذا يخبر Git دائمًا بالاحتفاظ بإصدارك أثناء عمليات الدمج.

4. **افحص إعدادات مساحة العمل الخاصة بك**:
   تحقق مما إذا كانت أي إضافات VSCode تقوم بتشغيل أوامر Maven تلقائيًا مما قد يؤدي إلى هذا السلوك.

قد يعتمد الحل الدقيق على إضافات Maven/Java المحددة التي تستخدمها في VSCode. إذا شاركتنا الإضافات المحددة التي تستخدمها لتطوير Maven/Java، يمكنني تقديم نصائح أكثر استهدافًا.