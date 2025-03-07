---
title: Specifying the JDK for WebSphere Liberty
lang: en
layout: post
audio: false
translated: false
generated: true
---

To specify the OpenJDK version that WebSphere Liberty should use, you can set the `JAVA_HOME` environment variable to point to the desired OpenJDK installation. Here's how you can do it:

### Steps to Set `JAVA_HOME` for WebSphere Liberty

1. **Locate Your OpenJDK Installation**:
   - Determine the path where your desired version of OpenJDK is installed. For example, it might be something like `/usr/lib/jvm/java-17-openjdk` on Linux or `C:\Program Files\OpenJDK\jdk-17` on Windows.

2. **Set the `JAVA_HOME` Environment Variable**:
   - You need to set the `JAVA_HOME` environment variable to this path. The method to set environment variables differs based on your operating system.

#### On Windows

- **System-Wide**:
  1. Open the Start Search, type in "env", and select "Edit the system environment variables".
  2. In the System Properties window, click on the "Environment Variables" button.
  3. Under "System variables", click "New" and add `JAVA_HOME` as the variable name and the path to your OpenJDK installation as the variable value.
  4. Find the `Path` variable in the "System variables" section, select it, and click "Edit". Add a new entry with the value `%JAVA_HOME%\bin`.

- **Command Prompt (Temporary)**:
  ```cmd
  set JAVA_HOME=C:\path\to\openjdk
  set PATH=%JAVA_HOME%\bin;%PATH%
  ```

#### On macOS and Linux

- **Shell Configuration File**:
  1. Open your shell configuration file (e.g., `~/.bashrc`, `~/.bash_profile`, or `~/.zshrc`) in a text editor.
  2. Add the following lines:
     ```bash
     export JAVA_HOME=/path/to/openjdk
     export PATH=$JAVA_HOME/bin:$PATH
     ```
  3. Save the file and run `source ~/.bashrc` (or the appropriate file) to apply the changes.

- **Temporary Session**:
  ```bash
  export JAVA_HOME=/path/to/openjdk
  export PATH=$JAVA_HOME/bin:$PATH
  ```

3. **Verify the Configuration**:
   - Open a new terminal or command prompt and type `echo $JAVA_HOME` (or `echo %JAVA_HOME%` on Windows) to verify that it points to the correct directory.
   - Type `java -version` to check the Java version being used.

4. **Start WebSphere Liberty**:
   - When you start WebSphere Liberty, it will use the Java runtime specified by the `JAVA_HOME` environment variable.

By setting the `JAVA_HOME` environment variable, you ensure that WebSphere Liberty uses the specified version of OpenJDK. Make sure to replace the example paths with the actual installation path of your OpenJDK version.

---

The error message you're encountering, `Error creating bean UnsatisfiedDependencyException, nested exception is java.lang.NoClassDefFoundError: javax/xml/bind/JAXBException`, indicates that your application is unable to find the `javax.xml.bind.JAXBException` class at runtime. This typically happens when there is a missing dependency or a version mismatch in your project.

Here are some steps you can take to resolve this issue:

1. **Check Java Version**:
   - Ensure that you are using a compatible Java version. The `javax.xml.bind` package was included in Java SE up to version 8 but was removed in Java SE 9 and later. If you are using Java 9 or later, you will need to add the JAXB library explicitly.

2. **Add JAXB Dependency**:
   - If you are using Maven, add the following dependencies to your `pom.xml` file:

     ```xml
     <dependency>
         <groupId>javax.xml.bind</groupId>
         <artifactId>jaxb-api</artifactId>
         <version>2.3.1</version>
     </dependency>
     <dependency>
         <groupId>org.glassfish.jaxb</groupId>
         <artifactId>jaxb-runtime</artifactId>
         <version>2.3.1</version>
     </dependency>
     ```

   - If you are using Gradle, add the following to your `build.gradle` file:

     ```groovy
     implementation 'javax.xml.bind:jaxb-api:2.3.1'
     implementation 'org.glassfish.jaxb:jaxb-runtime:2.3.1'
     ```

3. **Check Classpath**:
   - Ensure that the JAXB library is included in your classpath. If you are running your application from an IDE, make sure the dependencies are correctly configured.

4. **Rebuild the Project**:
   - After adding the dependencies, clean and rebuild your project to ensure that the changes take effect.

5. **Check for Conflicting Dependencies**:
   - Sometimes, other libraries might bring in different versions of JAXB. Use dependency management tools to check for conflicts and exclude any conflicting versions.

6. **Verify Spring Configuration**:
   - If you are using Spring, ensure that your configuration files are correctly set up and that there are no misconfigurations leading to the `UnsatisfiedDependencyException`.

By following these steps, you should be able to resolve the `NoClassDefFoundError` related to `javax.xml.bind.JAXBException`. If the issue persists, please provide more details about your project setup and any additional error messages you might be seeing.