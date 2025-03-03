---
audio: false
lang: zh
layout: post
title: BeanDefinitionStoreException
translated: true
---

根据你提供的错误信息，你的在IBM WebSphere上运行的支持OSGi的Java应用程序在初始化Spring框架应用程序上下文时遇到了`BeanDefinitionStoreException`。这个异常表明“无效的bean定义”，通常是由于Spring设置中的配置错误引起的。以下是一个详细的指南，帮助你排查和解决这个问题。

---

## 理解问题
错误显示：
- **异常**：`org.springframework.beans.factory.BeanDefinitionStoreException: Invalid bean definition`
- **关键组件**：堆栈跟踪中提到`PlaceholderConfigurerSupport`、`PropertySourcesPlaceholderConfigurer`和`AbstractApplicationContext`。
- **上下文**：失败发生在Spring应用程序上下文的`refresh`过程中，由`ContextLoader`在WebSphere的Web应用程序环境中触发。
- **根本原因**：可能与未解析的属性占位符、无效的bean定义或WebSphere/OSGi环境中的部署特定问题有关。

这表明Spring由于配置错误无法正确定义或初始化一个或多个bean。让我们逐步解决这个问题。

---

## 逐步修复

### 1. 验证属性占位符
**为什么**：堆栈跟踪突出显示了`PlaceholderConfigurerSupport`和`PropertySourcesPlaceholderConfigurer`，它们处理属性解析。如果bean定义使用占位符（例如`${admin.email}`）并且未定义，Spring将失败。

**如何修复**：
- **定位属性文件**：确保你的`application.properties`或`application.yml`文件在类路径中（例如`src/main/resources`）。
- **检查属性**：打开文件并确认所有在bean定义中引用的占位符都已定义。例如：
  ```properties
  admin.email=admin@example.com
  ```
- **修正拼写错误**：查找属性名称或文件路径中的拼写错误。
- **配置设置**：
  - **XML**：如果使用XML，验证`<context:property-placeholder>`标签：
    ```xml
    <context:property-placeholder location="classpath:application.properties"/>
    ```
  - **Java配置**：如果使用`@Configuration`，确保`PropertySourcesPlaceholderConfigurer`已配置：
    ```java
    @Bean
    public static PropertySourcesPlaceholderConfigurer propertySourcesPlaceholderConfigurer() {
        return new PropertySourcesPlaceholderConfigurer();
    }
    ```

### 2. 检查Bean定义
**为什么**：“无效的bean定义”消息指向Spring配置中bean定义的问题。

**如何修复**：
- **XML配置**：
  - 打开你的Spring XML文件（例如`applicationContext.xml`）并检查：
    - Bean ID和类名是否正确且存在于类路径中。
    - 属性是否有效且与setter方法或构造函数参数匹配。
    - 正确的bean示例：
      ```xml
      <bean id="myBean" class="com.example.MyClass">
          <property name="email" value="${admin.email}"/>
      </bean>
      ```
  - 使用IDE验证XML语法和模式。
- **Java配置**：
  - 检查`@Configuration`类中的`@Bean`方法：
    ```java
    @Bean
    public MyClass myBean() {
        MyClass bean = new MyClass();
        bean.setEmail(env.getProperty("admin.email"));
        return bean;
    }
    ```
  - 确保返回类型和方法名称有效。
- **组件扫描**：
  - 如果使用`@Component`、`@Service`等，确认基础包已扫描：
    ```java
    @ComponentScan("com.example")
    ```

### 3. 解决循环依赖
**为什么**：如果两个bean相互依赖（例如，Bean A需要Bean B，Bean B需要Bean A），Spring可能无法初始化它们。

**如何修复**：
- **使用`@Lazy`**：
  - 使用`@Lazy`注解一个依赖项以延迟其初始化：
    ```java
    @Autowired
    @Lazy
    private BeanB beanB;
    ```
- **重构**：如果可能，重新设计你的bean以避免循环引用。

### 4. 检查依赖和类路径
**为什么**：缺失或不兼容的库可能导致bean定义中引用的类不可用。

**如何修复**：
- **Maven/Gradle**：
  - 确保所有必要的Spring依赖项在`pom.xml`（Maven）或`build.gradle`（Gradle）中。Maven示例：
    ```xml
    <dependency>
        <groupId>org.springframework</groupId>
        <artifactId>spring-context</artifactId>
        <version>5.3.23</version>
    </dependency>
    ```
  - 运行`mvn dependency:tree`或`gradle dependencies`检查冲突。
- **类路径**：确认所有类（例如`com.example.MyClass`）已编译并在部署的应用程序中可用。

### 5. 启用调试日志
**为什么**：更详细的日志可以定位导致失败的具体bean或属性。

**如何修复**：
- 添加到`application.properties`：
  ```properties
  logging.level.org.springframework=DEBUG
  ```
- 重新启动应用程序并查看日志以获取有关bean创建或属性解析的具体错误。

### 6. 验证WebSphere/OSGi配置
**为什么**：堆栈跟踪显示WebSphere和OSGi组件，可能引入部署特定问题。

**如何修复**：
- **Bundle解析**：确保所有OSGi bundle在WebSphere中正确部署且其依赖项已解析。
- **类路径**：验证WebSphere的类加载器是否包括你的应用程序的JAR和属性文件。
- **服务器日志**：检查WebSphere日志（例如`SystemOut.log`）以获取额外的错误或警告。

### 7. 审查早期日志
**为什么**：日志片段显示在10:15:57成功加载属性，但在16:56:57发生错误。早期问题可能触发了失败。

**如何修复**：
- 在日志文件中向上滚动或检查存档日志，查找`BeanDefinitionStoreException`之前的警告或错误。

---

## 常见场景和解决方案
- **未解析的占位符**：
  - **问题**：bean定义中的`${admin.email}`，但在`application.properties`中未定义。
  - **修复**：将`admin.email=somevalue`添加到文件中。
- **缺失的类**：
  - **问题**：`<bean class="com.example.NonExistentClass">`
  - **修复**：更正类名或添加缺失的依赖项。
- **语法错误**：
  - **问题**：格式不正确的XML或Java配置。
  - **修复**：使用IDE或工具（如`xmllint`）验证XML。

---

## 最终步骤
1. **应用修复**：从属性占位符和bean定义开始，因为根据堆栈跟踪它们是最有可能的问题。
2. **本地测试**：重新部署并在开发环境中测试。
3. **部署到WebSphere**：如果本地工作，重新部署到WebSphere并监控日志。
4. **迭代**：如果错误持续，使用调试日志缩小失败的bean或属性。

通过遵循这些步骤，你应该能够解决`BeanDefinitionStoreException`并成功初始化Spring应用程序上下文。如果问题仍然存在，分享更具体的详细信息（例如配置文件或完整日志）以获取进一步的帮助。