---
audio: false
generated: true
lang: en
layout: post
title: Using an AES-encrypted Password in WebSphere Liberty
translated: false
---

To use an AES-encrypted password from WebSphere Liberty's `server.xml` in Squirrel SQL Client, follow these steps:

---

### **1. Decrypt the Password Using WebSphere Liberty's Tools**
The encrypted password (e.g., `password="{aes}ABC123..."`) must be decrypted first. Liberty's `securityUtility` tool can do this if you have access to the keystore used for encryption.

#### **Command to Decrypt:**
```bash
# Navigate to Liberty's bin directory
cd /path/to/wlp/bin

# Run the securityUtility decode command
./securityUtility decode \
  --server=<LibertyServerPath> \
  --key=<KeyAlias> \
  --keyPassword=<KeystorePassword> \
  --source="{aes}ABC123..."
```

Replace:
- `<LibertyServerPath>`: Path to your Liberty server (e.g., `usr/servers/defaultServer`).
- `<KeyAlias>`: Alias of the key in the keystore (default: `default`).
- `<KeystorePassword>`: Password for the keystore (default: `KeystorePass` if unchanged).
- `{aes}ABC123...`: The encrypted password from `server.xml`.

---

### **2. Use the Decrypted Password in Squirrel**
1. Open Squirrel SQL Client.
2. Create a new connection alias.
3. In the connection properties:
   - **Driver**: Choose your Oracle JDBC driver.
   - **URL**: Use the JDBC URL from Liberty's `server.xml` (e.g., `jdbc:oracle:thin:@//host:port/service`).
   - **Username**: The username from Liberty's `<dataSource>`.
   - **Password**: Enter the **decrypted password** obtained from Step 1.

---

### **Important Notes**
- **Keystore Access**: You need the keystore file (`key.jks` or `key.p12`) and its password. By default, it resides in Liberty's `resources/security` directory.
- **Security**: Never store the decrypted password in plain text. Enter it directly in Squirrel without saving it to a file.
- **Admin Help**: If you don’t have the keystore credentials, contact your Liberty administrator to decrypt the password securely.

---

### **Alternative Approach (Not Recommended)**
If decryption isn’t feasible, temporarily replace the encrypted password in `server.xml` with a plain-text password (**for testing only**). Restart Liberty and use the plain-text password in Squirrel. Revert to the encrypted password afterward.

```xml
<!-- Example: Plain-text password (avoid in production) -->
<dataSource ...>
  <properties password="plaintextPassword" />
</dataSource>
```

---

By following these steps, you can securely use the decrypted password in Squirrel while maintaining compliance with security best practices.

---

To connect the Squirrel SQL client to an Oracle database using the configuration specified in a WebSphere Liberty Profile's `server.xml` file, particularly when the Oracle JDBC driver properties include an AES-encrypted password, follow these steps. The process involves extracting the connection details from the `server.xml` file, handling the encrypted password, and configuring Squirrel SQL appropriately. Below is a complete guide:

### Step 1: Understand the `server.xml` Configuration
In WebSphere Liberty Profile, database connections are defined in the `server.xml` file using a `<dataSource>` element. This element specifies the data source properties, including those for an Oracle database via a nested `<properties.oracle>` element. An example configuration might look like this:

```xml
<dataSource jndiName="jdbc/myOracleDS">
    <jdbcDriver libraryRef="OracleLib"/>
    <properties.oracle url="jdbc:oracle:thin:@//localhost:1521/orcl" user="scott" password="{aes}encrypted_password"/>
</dataSource>
<library id="OracleLib">
    <fileset dir="${server.config.dir}/lib" includes="ojdbc6.jar"/>
</library>
```

Here:
- **`url`**: The JDBC URL for connecting to the Oracle database (e.g., `jdbc:oracle:thin:@//localhost:1521/orcl`).
- **`user`**: The database username (e.g., `scott`).
- **`password`**: The password, encrypted with AES, prefixed with `{aes}` (e.g., `{aes}encrypted_password`).
- **`<jdbcDriver>`**: References the Oracle JDBC driver JAR file.

Since Squirrel SQL is a standalone client and cannot directly access the WebSphere-managed data source (e.g., via JNDI lookup), you need to manually configure it using the same connection details.

### Step 2: Extract Connection Details from `server.xml`
Locate the `<dataSource>` element in your `server.xml` file that corresponds to your Oracle database. From the `<properties.oracle>` element, note the following:
- **JDBC URL**: Found in the `url` attribute (e.g., `jdbc:oracle:thin:@//localhost:1521/orcl`).
- **Username**: Found in the `user` attribute (e.g., `scott`).
- **Encrypted Password**: Found in the `password` attribute (e.g., `{aes}encrypted_password`).

The JDBC URL specifies how to connect to the Oracle database, typically in one of these formats:
- `jdbc:oracle:thin:@//hostname:port/service_name` (using a service name)
- `jdbc:oracle:thin:@hostname:port:SID` (using a SID)

Check your `server.xml` to confirm the exact URL.

### Step 3: Decode the AES-Encrypted Password
The password in the `server.xml` is encrypted with AES, as indicated by the `{aes}` prefix. WebSphere Liberty Profile encrypts passwords for security, but Squirrel SQL requires the plain text password to establish a connection. To decode the encrypted password:

1. **Use WebSphere's `securityUtility` Tool**:
   - This tool is included with your WebSphere Liberty installation, typically located in the `bin` directory (e.g., `<liberty_install_dir>/bin/`).
   - Run the following command in a terminal or command prompt from the `bin` directory:
     ```
     securityUtility decode --encoding=aes <encrypted_password>
     ```
     Replace `<encrypted_password>` with the actual encrypted string from the `password` attribute (everything after `{aes}`). For example:
     ```
     securityUtility decode --encoding=aes encrypted_password
     ```
   - The tool will output the plain text password.

2. **Alternative**:
   - If you don’t have access to the WebSphere Liberty installation or the `securityUtility` tool, you’ll need to obtain the plain text password from your system administrator or the person who configured the data source.

Save the decoded password securely, as you’ll need it for Squirrel SQL.

### Step 4: Configure the Oracle JDBC Driver in Squirrel SQL
Squirrel SQL requires the Oracle JDBC driver to connect to the database. You’ll need the same driver JAR file referenced in the `server.xml` `<library>` element (e.g., `ojdbc6.jar`).

1. **Obtain the Driver JAR**:
   - Locate the Oracle JDBC driver JAR file specified in the `<fileset>` element of the `server.xml` (e.g., `ojdbc6.jar` in `${server.config.dir}/lib`).
   - If you don’t have it, download the appropriate version from Oracle’s website (e.g., `ojdbc6.jar` or `ojdbc8.jar`, matching your database version).

2. **Add the Driver to Squirrel SQL**:
   - Open Squirrel SQL.
   - Go to the **Drivers** tab on the left.
   - Click the **+** button to add a new driver.
   - Configure the driver:
     - **Name**: Enter a name (e.g., “Oracle JDBC Driver”).
     - **Example URL**: Enter a sample URL (e.g., `jdbc:oracle:thin:@//localhost:1521/orcl`).
     - **Class Name**: Enter `oracle.jdbc.OracleDriver`.
     - **Extra Class Path**: Click **Add**, then browse to and select the Oracle JDBC driver JAR file.
   - Click **OK** to save the driver.

### Step 5: Create a Connection (Alias) in Squirrel SQL
Now, create a connection alias using the extracted details:

1. **Add a New Alias**:
   - Go to the **Aliases** tab in Squirrel SQL.
   - Click the **+** button to add a new alias.
   - Configure the alias:
     - **Name**: Enter a name for the connection (e.g., “Oracle DB via WebSphere”).
     - **Driver**: Select the Oracle JDBC driver you just configured.
     - **URL**: Enter the JDBC URL from the `server.xml` `<properties.oracle>` element (e.g., `jdbc:oracle:thin:@//localhost:1521/orcl`).
     - **Username**: Enter the username from the `server.xml` (e.g., `scott`).
     - **Password**: Enter the decoded plain text password from Step 3.

2. **Optional: Additional Properties**:
   - If the `<properties.oracle>` element in `server.xml` includes additional attributes (e.g., `ssl="true"` or `connectionTimeout="30000"`), click the **Properties** tab in the alias configuration and add them as key-value pairs.

3. **Test the Connection**:
   - Click **Test Connection** to verify that Squirrel SQL can connect to the database.
   - If successful, click **OK** to save the alias.

### The JDBC URL
The URL to use in Squirrel SQL is the value specified in the `url` attribute of the `<properties.oracle>` element in the `server.xml` file. For example:
- If `server.xml` has `<properties.oracle url="jdbc:oracle:thin:@//localhost:1521/orcl" .../>`, then use:
  ```
  jdbc:oracle:thin:@//localhost:1521/orcl
  ```

This URL, combined with the username and decoded password, enables Squirrel SQL to connect to the Oracle database.

### Notes
- **Encrypted Password**: You cannot use the encrypted password directly in Squirrel SQL; it must be decoded to plain text.
- **DataSource Scope**: The `<dataSource>` in `server.xml` is designed for applications running in WebSphere Liberty. Squirrel SQL, as an external client, requires a manual configuration mirroring these settings.
- **JAR Compatibility**: Ensure the Oracle JDBC driver JAR version matches your database version for compatibility.

By following these steps, you can successfully configure Squirrel SQL to connect to the Oracle database using the properties defined in the WebSphere Liberty Profile’s `server.xml`.

---

Since the `securityUtility` command in WebSphere Liberty does not provide a decode option for AES-encrypted passwords (e.g., those prefixed with `{aes}` in the `server.xml` file), you need to use a programmatic approach to decrypt them. The recommended method involves leveraging the `com.ibm.websphere.crypto.PasswordUtil` class, which is part of the Liberty runtime and can decode such passwords. Below are two practical solutions to achieve this:

### Option 1: Use a Temporary Web Application (Recommended)
Deploying a simple web application to your Liberty server allows you to run the decoding logic within the server environment, ensuring access to the correct encryption key (default or custom, as defined in `server.xml`).

#### Steps:
1. **Create a JSP File**  
   Create a file named `decode.jsp` with the following content:
   ```jsp
   <%@ page import="com.ibm.websphere.crypto.PasswordUtil" %>
   <%
       String encoded = request.getParameter("encoded");
       if (encoded != null) {
           try {
               String decoded = PasswordUtil.decode(encoded);
               out.println("Decoded password: " + decoded);
           } catch (Exception e) {
               out.println("Error decoding password: " + e.getMessage());
           }
       }
   %>
   ```

2. **Deploy the JSP**  
   - Place `decode.jsp` in a web application directory, such as `wlp/usr/servers/yourServer/apps/myApp.war/WEB-INF/`.
   - If needed, create a basic WAR file with this JSP and deploy it using the Liberty admin console or by dropping it into the `dropins` directory.

3. **Access the JSP**  
   - Start your Liberty server (`server start yourServer`).
   - Open a browser and navigate to:  
     `http://localhost:9080/myApp/decode.jsp?encoded={aes}your_encrypted_password`  
     Replace `{aes}your_encrypted_password` with the actual encrypted password from `server.xml`.

4. **Retrieve the Decoded Password**  
   The page will display the decrypted password, which you can then use (e.g., in Squirrel SQL to connect to a database).

5. **Secure the Application**  
   After obtaining the password, remove or restrict access to the JSP to prevent unauthorized use.

#### Why This Works:
Running within the Liberty server ensures that `PasswordUtil.decode()` uses the same encryption key (default or custom, specified via `wlp.password.encryption.key` in `server.xml`) that was used to encode the password.

---

### Option 2: Use a Standalone Java Program
If deploying a web application isn’t feasible, you can write a standalone Java program and run it with the Liberty runtime libraries in the classpath. This approach is trickier because it requires manual handling of the encryption key, especially if a custom key was used.

#### Sample Code:
```java
import com.ibm.websphere.crypto.PasswordUtil;

public class PasswordDecoder {
    public static void main(String[] args) {
        if (args.length < 1 || args.length > 2) {
            System.out.println("Usage: java PasswordDecoder <encoded_password> [crypto_key]");
            return;
        }
        String encoded = args[0];
        String cryptoKey = args.length == 2 ? args[1] : null;
        try {
            String decoded;
            if (cryptoKey != null) {
                decoded = PasswordUtil.decode(encoded, cryptoKey);
            } else {
                decoded = PasswordUtil.decode(encoded);
            }
            System.out.println("Decoded password: " + decoded);
        } catch (Exception e) {
            System.err.println("Error decoding password: " + e.getMessage());
        }
    }
}
```

#### Steps:
1. **Compile the Program**  
   - Save the code as `PasswordDecoder.java`.
   - Compile it using Liberty’s jars:  
     ```bash
     javac -cp /path/to/wlp/lib/* PasswordDecoder.java
     ```
     Replace `/path/to/wlp` with your Liberty installation directory (e.g., `/opt/ibm/wlp`).

2. **Run the Program**  
   - If the password was encrypted with the default key:  
     ```bash
     java -cp /path/to/wlp/lib/*:. PasswordDecoder "{aes}your_encrypted_password"
     ```
   - If a custom key was used (e.g., defined in `server.xml` as `<variable name="wlp.password.encryption.key" value="yourKey"/>`):  
     ```bash
     java -cp /path/to/wlp/lib/*:. PasswordDecoder "{aes}your_encrypted_password" "yourKey"
     ```

3. **Handle the Output**  
   The program will print the decoded password or an error if the key is incorrect.

#### Notes:
- The Liberty jars (e.g., in `wlp/lib`) contain `com.ibm.websphere.crypto.PasswordUtil` and its dependencies.
- If a custom key was used and you don’t provide it, decoding will fail. Check `server.xml` or included configuration files for the key.

---

### Key Considerations
- **Default vs. Custom Key**:  
  - If no `wlp.password.encryption.key` is specified in `server.xml`, the default key is used, and `PasswordUtil.decode(encoded)` should work without additional parameters.
  - If a custom key is defined, you must supply it explicitly when decoding outside the server (Option 2) or rely on the server context (Option 1).

- **Security**:  
  Handle the decoded password carefully, as it will be in plain text. Avoid logging it or exposing it unnecessarily.

- **Preference**:  
  Option 1 (web application) is generally more reliable because it runs within the Liberty environment, automatically handling the key and dependencies.

By following either approach, you can successfully decode the AES-encrypted password from `server.xml` despite the lack of a decode option in `securityUtility`.