---
audio: false
generated: true
lang: fr
layout: post
title: Fichiers de projet dans VSCode
translated: true
type: note
---

Ce problème avec la balise `filterResources` qui est ajoutée de manière répétée à votre fichier `.project` dans les projets Maven Spring Boot est généralement causé par l'intégration Eclipse/M2Eclipse qui s'effectue en arrière-plan.

Lorsque vous travaillez sur un projet Maven dans un IDE (même VSCode), les plugins Maven peuvent générer ou modifier automatiquement les fichiers de projet Eclipse (comme `.project`). La balise `filterResources` est spécifiquement ajoutée lorsque le filtrage des ressources Maven est configuré dans votre projet.

Voici quelques approches pour empêcher cette génération automatique :

1. **Configurer les paramètres de votre plugin m2e** :
   Vous pouvez ajouter une configuration à votre pom.xml qui indique au plugin m2e comment gérer le filtrage des ressources sans modifier le fichier .project :

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

2. **Paramètres spécifiques à VSCode** :
   Dans VSCode, vous utilisez peut-être les extensions Java ou Maven. Vous pouvez vérifier leurs paramètres pour voir si vous pouvez désactiver la génération ou modification automatique des fichiers de projet Eclipse :
   
   - Ouvrez les paramètres (Ctrl+,)
   - Recherchez les paramètres "maven" ou "java" liés à la génération de projet
   - Cherchez des options comme "Update Configuration" ou "Project Generation"

3. **Utiliser .gitattributes au lieu de .gitignore** :
   Si vous souhaitez conserver le fichier, mais empêcher Git de détecter ses modifications :

   ```
   moduleA/.project merge=ours
   ```

   Cela indique à Git de toujours conserver votre version lors des fusions.

4. **Examiner les paramètres de votre espace de travail** :
   Vérifiez si des extensions VSCode exécutent automatiquement des commandes Maven qui pourraient déclencher ce comportement.

La solution exacte peut dépendre des extensions Maven/Java spécifiques que vous utilisez dans VSCode. Si vous partagez quelles extensions spécifiques vous utilisez pour le développement Maven/Java, je pourrais fournir des conseils plus ciblés.