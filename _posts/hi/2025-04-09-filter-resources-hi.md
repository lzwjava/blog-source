---
audio: false
generated: true
lang: hi
layout: post
title: वीएसकोड में प्रोजेक्ट फ़ाइलें
translated: true
type: note
---

Maven Spring Boot प्रोजेक्ट्स में आपकी `.project` फ़ाइल में `filterResources` टैग का बार-बार जुड़ना आमतौर पर Eclipse/M2Eclipse इंटीग्रेशन के कारण होता है जो पृष्ठभूमि में चल रहा होता है।

जब आप किसी IDE (यहां तक कि VSCode) में Maven प्रोजेक्ट पर काम कर रहे होते हैं, तो Maven plugins स्वचालित रूप से Eclipse प्रोजेक्ट फ़ाइलें (जैसे `.project`) generate या modify कर सकते हैं। `filterResources` टैग विशेष रूप से तब जोड़ा जाता है जब आपके प्रोजेक्ट में Maven resource filtering configured होती है।

इस स्वचालित generation को रोकने के लिए यहां कुछ उपाय दिए गए हैं:

1. **अपने m2e plugin settings configure करें**:
   आप अपनी pom.xml में configuration जोड़ सकते हैं जो m2e plugin को बताती है कि .project फ़ाइल को modify किए बिना resource filtering को कैसे handle करें:

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

2. **VSCode specific settings**:
   VSCode में, हो सकता है आप Java या Maven extensions का उपयोग कर रहे हों। आप उनकी settings check कर सकते हैं कि क्या आप स्वचालित Eclipse प्रोजेक्ट फ़ाइल generation या modification को disable कर सकते हैं:
   
   - Settings खोलें (Ctrl+,)
   - "maven" या "java" से संबंधित प्रोजेक्ट generation settings खोजें
   - "Update Configuration" या "Project Generation" जैसे विकल्प देखें

3. **`.gitignore` के बजाय `.gitattributes` का उपयोग करें**:
   यदि आप फ़ाइल को रखना चाहते हैं, लेकिन Git को इसमें changes देखने से रोकना चाहते हैं:

   ```
   moduleA/.project merge=ours
   ```

   यह Git को merges के दौरान हमेशा आपके version को रखने के लिए कहता है।

4. **अपने workspace settings की जांच करें**:
   Check करें कि क्या कोई VSCode extensions स्वचालित रूप से Maven commands चला रही हैं जो इस behavior को trigger कर सकती हैं।

सटीक समाधान इस बात पर निर्भर कर सकता है कि आप VSCode में कौन से specific Maven/Java extensions का उपयोग कर रहे हैं। यदि आप बताएं कि आप Maven/Java development के लिए कौन से specific extensions का उपयोग कर रहे हैं, तो मैं अधिक targeted सलाह दे सकता हूं।