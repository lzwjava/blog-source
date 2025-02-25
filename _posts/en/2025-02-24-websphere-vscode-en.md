---
audio: false
lang: en
layout: post
title: Using the WebSphere Liberty server in VSCode
translated: false
---

To use the WebSphere Liberty server in Visual Studio Code (VSCode), you can leverage the **Liberty Tools** extension, which supports both Open Liberty and WebSphere Liberty. This extension allows you to manage your Liberty server, deploy applications, and debug directly from within VSCode, streamlining your development workflow.

### Steps to Use WebSphere Liberty in VSCode

#### 1. **Install the Liberty Tools Extension**
   - Open VSCode and navigate to the Extensions view by clicking the Extensions icon in the Activity Bar or pressing `Ctrl+Shift+X`.
   - Search for "Liberty Tools" in the Extensions Marketplace.
   - Click "Install" to add the extension to VSCode.
   - Reload VSCode if prompted to enable the extension.

#### 2. **Set Up Prerequisites**
   - **Java**: Ensure you have a compatible version of Java installed (Java 8 or later is recommended). Liberty is a Java-based server, so Java is essential for running it.
   - **WebSphere Liberty**: Download and install the WebSphere Liberty runtime if you haven't already. You can obtain it from the [official IBM website](https://www.ibm.com/docs/en/was-liberty). Note the installation directory, as you'll need it to configure the extension.

#### 3. **Configure the Liberty Tools Extension**
   - After installing the extension, configure it to point to your Liberty installation.
   - Open the Command Palette in VSCode by pressing `Ctrl+Shift+P`.
   - Type "Liberty: Add Liberty Runtime" and select the command.
   - Provide the path to your Liberty installation directory (e.g., `/opt/ibm/wlp`).
   - The extension will detect the Liberty runtime and make it available for use within VSCode.

#### 4. **Manage Your Liberty Server**
   - Once configured, you can manage your Liberty server directly from VSCode.
   - **Liberty Dashboard**: Access the Liberty Dashboard view in the Explorer pane or via the Command Palette. This dashboard lists your Liberty projects and servers.
   - **Start/Stop Server**: Right-click on your server in the dashboard to start, stop, or restart it.
   - **Deploy Applications**: For Liberty projects (e.g., Maven or Gradle projects with Liberty plugins), right-click on the project and select "Deploy to Liberty" to deploy applications.
   - **Development Mode (Dev Mode)**: For Maven or Gradle projects, start the server in dev mode, which automatically detects code changes, recompiles, and redeploys the application without restarting the server. This is ideal for iterative development.

#### 5. **Debugging and Testing**
   - **Debugging**: Attach a debugger to your running Liberty server directly from VSCode. Use the "Debug" option in the Liberty Dashboard or set up a debug configuration in VSCode's Run and Debug view.
   - **Run Tests**: If your project includes tests, run them from the dashboard and view the results within VSCode.

#### 6. **Additional Features**
   - **Configuration Assistance**: The extension provides code completion, validation, and hover descriptions for Liberty configuration files (e.g., `server.xml`), simplifying server configuration.
   - **Language Support**: It supports Java, MicroProfile, and Jakarta EE APIs, enhancing your development experience.

### Key Benefits
- **Seamless Integration**: Manage your Liberty server without leaving VSCode, improving efficiency.
- **Automatic Deployment**: In dev mode, code changes are automatically detected and deployed, saving time during development.
- **Debugging Support**: Easily attach a debugger to your server for troubleshooting.
- **Lightweight and Efficient**: Liberty Tools is designed to be lightweight, aligning with Liberty's focus on speed and efficiency.

### Additional Resources
- For detailed guidance, refer to the [Open Liberty Documentation](https://openliberty.io/docs/) and the [Liberty Tools VSCode Documentation](https://openliberty.io/docs/latest/develop/liberty-tools.html).
- If you encounter issues, check the extension's troubleshooting section or seek help from the community on platforms like Stack Overflow.

By following these steps, you can effectively use WebSphere Liberty within VSCode, leveraging its features to enhance your development process.