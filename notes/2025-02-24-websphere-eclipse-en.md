---
audio: false
generated: true
lang: en
layout: post
title: Using WebSphere Liberty with Eclipse
translated: false
---

To use the WebSphere plugin tools in Eclipse and integrate them for working with WebSphere Liberty, you can choose between two main options: **IBM Liberty Developer Tools** and **Liberty Tools**. Both are available through the Eclipse Marketplace and provide features to build, deploy, and manage applications on WebSphere Liberty, a lightweight, production-ready server for Java EE and cloud-native applications. Below is a detailed guide on how to use and integrate these tools.

---

### **Overview of the Tools**
- **IBM Liberty Developer Tools**: A traditional plugin provided by IBM for managing Liberty servers within Eclipse. It allows you to create and manage Liberty servers, deploy applications, and debug directly from the IDE. This tool is ideal for a server-centric workflow or for projects that aren't using Maven or Gradle.
- **Liberty Tools**: A next-generation, open-source alternative focused on Maven and Gradle projects. It offers a more integrated experience with build tools, automatic detection of Liberty projects, and support for Liberty's development mode (dev mode). This tool is better suited for modern, build-tool-centric workflows.

Both tools streamline development for WebSphere Liberty, but they differ in their approach. Choose the one that best fits your project type and development preferences.

---

### **Installation**
1. **Install Eclipse**:
   - Use a compatible version, such as **Eclipse for Enterprise Java and Web Developers**.
   - Ensure your Eclipse version supports the plugin you choose (check compatibility in the marketplace listing).

2. **Install the Plugin**:
   - Open Eclipse and go to **Help > Eclipse Marketplace**.
   - Search for:
     - "IBM Liberty Developer Tools" for the traditional IBM toolset, or
     - "Liberty Tools" for the open-source alternative.
   - Install the desired plugin by following the prompts.

---

### **Setting Up the Liberty Runtime**
- **Download Liberty**:
  - If you haven't already, download the WebSphere Liberty runtime from the [official IBM website](https://www.ibm.com/docs/en/was-liberty).
  - Ensure the Liberty version is compatible with the plugin you installed.

- **Configure the Runtime in Eclipse**:
  - For **IBM Liberty Developer Tools**:
    - Go to **Window > Preferences > Server > Runtime Environments**.
    - Click "Add," select "Liberty Server," and specify the path to your Liberty installation directory.
  - For **Liberty Tools**:
    - No explicit runtime configuration is needed. Liberty Tools detect Liberty projects via Maven or Gradle configurations, so ensure your project is properly set up (see below).

---

### **Integrating with Your Project**
The integration process differs slightly between the two tools. Follow the steps below based on the tool you installed.

#### **For IBM Liberty Developer Tools**
1. **Create a Liberty Server**:
   - Open the **Servers** view (**Window > Show View > Servers**).
   - Right-click in the Servers view and select **New > Server**.
   - Choose "Liberty Server" from the list and follow the wizard to configure the server, including specifying the path to your Liberty installation.

2. **Add Your Project**:
   - Right-click the server in the Servers view and select **Add and Remove...**.
   - Select your project and move it to the "Configured" side.

3. **Start the Server**:
   - Right-click the server and choose **Start** or **Debug** to run your application.
   - Access your application at the specified URL (default: `http://localhost:9080/<context-root>`).

#### **For Liberty Tools (Maven/Gradle Projects)**
1. **Ensure Project Configuration**:
   - Your project must include the necessary Liberty plugin:
     - For Maven: Add the `liberty-maven-plugin` to your `pom.xml`.
     - For Gradle: Add the `liberty-gradle-plugin` to your `build.gradle`.
   - The `server.xml` configuration file should be in the standard location:
     - For Maven: `src/main/liberty/config`.
     - For Gradle: Adjust based on your project structure.

2. **Use the Liberty Dashboard**:
   - Click the Liberty icon in the Eclipse toolbar to open the **Liberty Dashboard**.
   - Liberty Tools automatically detect and list your Liberty projects in the dashboard.
   - Right-click on your project in the dashboard to access commands such as:
     - "Start in dev mode" (automatically redeploys changes without restarting the server).
     - "Run tests."
     - "View test reports."

3. **Access Your Application**:
   - Once the server is running, access your application at the specified URL (default: `http://localhost:9080/<context-root>`).
   - In dev mode, make changes to your code, and Liberty will automatically redeploy them.

---

### **Key Features**
Both tools offer powerful features to enhance productivity:

- **Server Management**:
  - Start, stop, and debug Liberty servers directly from Eclipse.
- **Application Deployment**:
  - Easily deploy and redeploy applications.
- **Configuration Assistance**:
  - Both tools provide code completion, validation, and hover descriptions for Liberty configuration files (e.g., `server.xml`).
- **Development Mode**:
  - Automatically detect and redeploy code changes without restarting the server (especially with Liberty Tools in dev mode).
- **Debugging**:
  - Attach the Eclipse debugger to the Liberty server for troubleshooting.

---

### **Considerations and Potential Issues**
- **Version Compatibility**:
  - Ensure that your versions of Eclipse, the plugin, and the Liberty runtime are compatible. Check the documentation for specific requirements.
- **Project Configuration**:
  - For Liberty Tools, your project must be a properly configured Maven or Gradle project with the Liberty plugin included.
  - Ensure `server.xml` is in the expected location for the tools to recognize your project.
- **Network Settings**:
  - Ensure that the default Liberty ports (e.g., 9080 for HTTP, 9443 for HTTPS) are open and not blocked by firewalls.
- **Java Compatibility**:
  - Liberty is a Java-based server, so ensure you have a compatible Java version installed for your Liberty runtime.

---

### **Quick Start with Liberty Tools (Maven/Gradle)**
If you're using Maven or Gradle, Liberty Tools offer a streamlined experience. Here's a step-by-step guide:

1. Install **Eclipse for Enterprise Java and Web Developers**.
2. Go to **Help > Eclipse Marketplace**, search for "Liberty Tools," and install the plugin.
3. Create or import a Maven/Gradle project configured for Liberty:
   - You can use the [Open Liberty Starter](https://openliberty.io/start/) to generate a sample project.
4. Ensure your project has the `liberty-maven-plugin` (for Maven) or `liberty-gradle-plugin` (for Gradle) configured.
5. Open the **Liberty Dashboard** by clicking the Liberty icon in the toolbar.
6. Your project should appear in the dashboard. Right-click on it and select "Start in dev mode."
7. Access your application at the specified URL (default: `http://localhost:9080/<context-root>`).
8. Make changes to your code; Liberty dev mode will automatically redeploy them.
9. Use the dashboard to run tests or view test reports as needed.

---

### **Choosing Between the Tools**
- **IBM Liberty Developer Tools**:
  - Ideal for a traditional server management approach or for projects that aren't using Maven or Gradle.
  - Offers a Servers view for managing Liberty servers explicitly.
- **Liberty Tools**:
  - Better suited for Maven or Gradle projects, with tighter integration with these build systems.
  - Provides a Liberty Dashboard for project-centric management and dev mode support.
  - Open-source, allowing community contributions and updates.

Both tools are available from the Eclipse Marketplace, so you can try both and choose the one that best fits your workflow.

---

In summary, using the WebSphere plugin tools in Eclipse involves installing the appropriate plugin, setting up the Liberty runtime, and configuring your project to work with Liberty. Whether you choose IBM Liberty Developer Tools or Liberty Tools, both provide robust features to streamline development for WebSphere Liberty within the Eclipse IDE.