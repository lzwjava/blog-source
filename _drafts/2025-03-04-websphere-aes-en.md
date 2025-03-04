---
audio: false
lang: en
layout: post
title: Using an AES-encrypted Password in WebSphere Liberty
translated: false
generated: true
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