---
audio: false
generated: true
lang: hi
layout: post
title: AES-encrypted Password का उपयोग WebSphere Liberty में
translated: true
---

WebSphere Liberty के `server.xml` से AES-encryption password का उपयोग Squirrel SQL Client में करने के liye, yeh steps follow karein:

---

### **1. WebSphere Liberty ke Tools ka use karke Password Decrypt karein**
Encrypted password (e.g., `password="{aes}ABC123..."`) ko pehle decrypt karna padta hai. Agar aapke paas encryption ke liye use ki gayi keystore ka access hai, to Liberty ke `securityUtility` tool yeh kar sakta hai.

#### **Command to Decrypt:**
```bash
# Liberty ke bin directory mein navigate karein
cd /path/to/wlp/bin

# securityUtility decode command run karein
./securityUtility decode \
  --server=<LibertyServerPath> \
  --key=<KeyAlias> \
  --keyPassword=<KeystorePassword> \
  --source="{aes}ABC123..."
```

Replace karein:
- `<LibertyServerPath>`: Aapke Liberty server ka path (e.g., `usr/servers/defaultServer`).
- `<KeyAlias>`: Keystore mein key ka alias (default: `default`).
- `<KeystorePassword>`: Keystore ka password (default: `KeystorePass` agar change nahi kiya gaya).
- `{aes}ABC123...`: `server.xml` se encrypted password.

---

### **2. Decrypted Password ko Squirrel mein use karein**
1. Squirrel SQL Client ko open karein.
2. Naya connection alias create karein.
3. Connection properties mein:
   - **Driver**: Aapka Oracle JDBC driver choose karein.
   - **URL**: Liberty ke `server.xml` se JDBC URL use karein (e.g., `jdbc:oracle:thin:@//host:port/service`).
   - **Username**: Liberty ke `<dataSource>` se username.
   - **Password**: Step 1 se mila **decrypted password** enter karein.

---

### **Important Notes**
- **Keystore Access**: Aapke paas keystore file (`key.jks` ya `key.p12`) aur uska password hona chahiye. Default, yeh Liberty ke `resources/security` directory mein rehta hai.
- **Security**: Plain text mein decrypted password ko kabhi bhi store na karein. Isse directly Squirrel mein enter karein bina kisi file mein save kiye.
- **Admin Help**: Agar aapke paas keystore credentials nahi hain, to Liberty administrator se secure tarike se password ko decrypt karne ke liye contact karein.

---

### **Alternative Approach (Not Recommended)**
Agar decryption feasible nahi hai, to `server.xml` mein encrypted password ko temporarily plain-text password se replace karein (**testing ke liye matra**). Liberty ko restart karein aur plain-text password ko Squirrel mein use karein. Baad mein encrypted password par wapas aayein.

```xml
<!-- Example: Plain-text password (avoid in production) -->
<dataSource ...>
  <properties password="plaintextPassword" />
</dataSource>
```

---

Yeh steps follow karke, aap securely decrypted password ko Squirrel mein use kar sakte hain, security best practices ke saath compliance maintain karte hue.

---

Squirrel SQL client ko Oracle database ke saath connect karne ke liye, WebSphere Liberty Profile ke `server.xml` file mein specify ki gayi configuration ka use karte hue, particularly jab Oracle JDBC driver properties mein AES-encrypted password include hai, yeh steps follow karein. Yeh process `server.xml` file se connection details ko extract karna, encrypted password ko handle karna, aur Squirrel SQL ko appropriately configure karna include karta hai. Niche complete guide hai:

### Step 1: `server.xml` Configuration ko Samajhne ke liye
WebSphere Liberty Profile mein, database connections `server.xml` file mein `<dataSource>` element ke through define ki gayi hoti hain. Yeh element data source properties ko specify karta hai, including Oracle database ke liye nested `<properties.oracle>` element ke through. Ek example configuration yeh ho sakta hai:

```xml
<dataSource jndiName="jdbc/myOracleDS">
    <jdbcDriver libraryRef="OracleLib"/>
    <properties.oracle url="jdbc:oracle:thin:@//localhost:1521/orcl" user="scott" password="{aes}encrypted_password"/>
</dataSource>
<library id="OracleLib">
    <fileset dir="${server.config.dir}/lib" includes="ojdbc6.jar"/>
</library>
```

Yahan:
- **`url`**: Oracle database ke liye JDBC URL (e.g., `jdbc:oracle:thin:@//localhost:1521/orcl`).
- **`user`**: Database username (e.g., `scott`).
- **`password`**: AES ke through encrypted password, `{aes}` ke saath prefix (e.g., `{aes}encrypted_password`).
- **`<jdbcDriver>`**: Oracle JDBC driver JAR file ko reference karta hai.

Squirrel SQL ek standalone client hai aur directly WebSphere-managed data source ko access nahi kar sakta (e.g., JNDI lookup ke through), isliye aapko manually configure karna padta hai, same connection details ka use karte hue.

### Step 2: `server.xml` se Connection Details ko Extract karein
Aapke Oracle database ke corresponding `<dataSource>` element ko `server.xml` file mein locate karein. `<properties.oracle>` element se note karein:
- **JDBC URL**: `url` attribute mein milta hai (e.g., `jdbc:oracle:thin:@//localhost:1521/orcl`).
- **Username**: `user` attribute mein milta hai (e.g., `scott`).
- **Encrypted Password**: `password` attribute mein milta hai (e.g., `{aes}encrypted_password`).

JDBC URL specify karta hai ki Oracle database ke saath kaise connect karein, typically ek ya do formats mein:
- `jdbc:oracle:thin:@//hostname:port/service_name` (service name ka use karte hue)
- `jdbc:oracle:thin:@hostname:port:SID` (SID ka use karte hue)

Aapke `server.xml` ko check karein exact URL ko confirm karne ke liye.

### Step 3: AES-Encrypted Password ko Decode karein
`server.xml` mein password AES ke through encrypted hai, `{aes}` prefix ke saath indicate kiya gaya hai. WebSphere Liberty Profile passwords ko security ke liye encrypt karta hai, lekin Squirrel SQL plain text password ko establish karne ke liye require karta hai. Decode encrypted password ke liye:

1. **WebSphere ke `securityUtility` Tool ka use karein**:
   - Yeh tool aapke WebSphere Liberty installation ke saath aata hai, typically `bin` directory mein (e.g., `<liberty_install_dir>/bin/`).
   - Terminal ya command prompt mein `bin` directory se yeh command run karein:
     ```
     securityUtility decode --encoding=aes <encrypted_password>
     ```
     `<encrypted_password>` ko actual encrypted string se replace karein `password` attribute se (sab kuch `{aes}` ke baad). For example:
     ```
     securityUtility decode --encoding=aes encrypted_password
     ```
   - Tool plain text password ko output karega.

2. **Alternative**:
   - Agar aapke paas WebSphere Liberty installation ya `securityUtility` tool ka access nahi hai, to aapko plain text password ko aapke system administrator ya us person se obtain karna padta hai jo data source ko configure kiya hai.

Save karo decoded password securely, kyunki aapko iske liye Squirrel SQL mein use karna padta hai.

### Step 4: Oracle JDBC Driver ko Squirrel SQL mein Configure karein
Squirrel SQL ko Oracle JDBC driver ke saath connect karne ke liye require hai. Aapko same driver JAR file chahiye jo `server.xml` ke `<library>` element mein reference kiya gaya hai (e.g., `ojdbc6.jar`).

1. **Driver JAR ko Obtain karein**:
   - `server.xml` ke `<fileset>` element mein specify ki gayi Oracle JDBC driver JAR file ko locate karein (e.g., `ojdbc6.jar` in `${server.config.dir}/lib`).
   - Agar aapke paas nahi hai, to Oracle ke website se appropriate version download karein (e.g., `ojdbc6.jar` ya `ojdbc8.jar`, matching aapke database version).

2. **Driver ko Squirrel SQL mein Add karein**:
   - Squirrel SQL ko open karein.
   - Left mein **Drivers** tab par click karein.
   - **+** button par click karein naya driver add karne ke liye.
   - Driver ko configure karein:
     - **Name**: Ek name enter karein (e.g., “Oracle JDBC Driver”).
     - **Example URL**: Ek sample URL enter karein (e.g., `jdbc:oracle:thin:@//localhost:1521/orcl`).
     - **Class Name**: `oracle.jdbc.OracleDriver` enter karein.
     - **Extra Class Path**: **Add** par click karein, phir Oracle JDBC driver JAR file ko browse aur select karein.
   - **OK** par click karein driver ko save karne ke liye.

### Step 5: Squirrel SQL mein Connection (Alias) Create karein
Ab, extracted details ka use karke naya connection alias create karein:

1. **Naya Alias Add karein**:
   - Squirrel SQL mein **Aliases** tab par jaayein.
   - **+** button par click karein naya alias add karne ke liye.
   - Alias ko configure karein:
     - **Name**: Connection ke liye ek name enter karein (e.g., “Oracle DB via WebSphere”).
     - **Driver**: Aapne configure ki Oracle JDBC driver select karein.
     - **URL**: `server.xml` ke `<properties.oracle>` element se JDBC URL enter karein (e.g., `jdbc:oracle:thin:@//localhost:1521/orcl`).
     - **Username**: `server.xml` se username enter karein (e.g., `scott`).
     - **Password**: Step 3 se mila decoded plain text password enter karein.

2. **Optional: Additional Properties**:
   - Agar `<properties.oracle>` element mein `server.xml` mein additional attributes hain (e.g., `ssl="true"` ya `connectionTimeout="30000"`), alias configuration mein **Properties** tab par click karein aur unhe key-value pairs ke roop mein add karein.

3. **Connection ko Test karein**:
   - **Test Connection** par click karein verify karne ke liye ki Squirrel SQL database se connect kar sakta hai.
   - Agar successful, **OK** par click karein alias ko save karne ke liye.

### JDBC URL
Squirrel SQL mein use karne ke liye URL `server.xml` file mein `<properties.oracle>` element ke `url` attribute mein specify kiya gaya hai. For example:
- Agar `server.xml` mein `<properties.oracle url="jdbc:oracle:thin:@//localhost:1521/orcl" .../>` hai, to use karein:
  ```
  jdbc:oracle:thin:@//localhost:1521/orcl
  ```

Yeh URL, username aur decoded password ke saath, Squirrel SQL ko Oracle database se connect karne deta hai.

### Notes
- **Encrypted Password**: Aap Squirrel SQL mein encrypted password ko directly use nahi kar sakte; isse plain text mein decode karna padta hai.
- **DataSource Scope**: `server.xml` mein `<dataSource>` WebSphere Liberty mein run karne ke liye applications ke liye design kiya gaya hai. Squirrel SQL, ek external client hai, isliye manual configuration chahiye jo in settings ko mirror karta hai.
- **JAR Compatibility**: Ensure ki Oracle JDBC driver JAR version aapke database version ke saath match karta hai compatibility ke liye.

Yeh steps follow karke, aap successfully Squirrel SQL ko Oracle database se connect kar sakte hain, jo properties define ki gayi hai WebSphere Liberty Profile ke `server.xml` mein.

---

Since `securityUtility` command in WebSphere Liberty AES-encrypted passwords (e.g., those prefixed with `{aes}` in the `server.xml` file) ke liye decode option nahi provide karta, aapko programmatic approach ka use karna padta hai unhe decrypt karne ke liye. Recommended method `com.ibm.websphere.crypto.PasswordUtil` class ka use karna hai, jo Liberty runtime ka part hai aur un passwords ko decode kar sakta hai. Niche do practical solutions hain yeh achieve karne ke liye:

### Option 1: Use a Temporary Web Application (Recommended)
Liberty server par ek simple web application deploy karke, aap decoding logic ko server environment mein run kar sakte hain, isse ensure karte hue ki correct encryption key (default ya custom, jo `server.xml` mein define kiya gaya hai) ka access hai.

#### Steps:
1. **Create a JSP File**
   Ek file banayein jo `decode.jsp` kehte hain, is content ke saath:
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
   - `decode.jsp` ko ek web application directory mein place karein, jaise `wlp/usr/servers/yourServer/apps/myApp.war/WEB-INF/`.
   - Agar zaroorat hai, ek basic WAR file banayein is JSP ke saath aur Liberty admin console ya `dropins` directory mein drop karke deploy karein.

3. **Access the JSP**
   - Liberty server ko start karein (`server start yourServer`).
   - Browser open karein aur navigate karein:
     `http://localhost:9080/myApp/decode.jsp?encoded={aes}your_encrypted_password`
     `{aes}your_encrypted_password` ko `server.xml` se actual encrypted password se replace karein.

4. **Retrieve the Decoded Password**
   Page decoded password ko display karega, jo aap use kar sakte hain (e.g., Squirrel SQL mein database se connect karne ke liye).

5. **Secure the Application**
   Password milne ke baad, JSP ko remove ya access ko restrict karein unauthorized use ko roke.

#### Why This Works:
Server mein run karna ensure karta hai ki `PasswordUtil.decode()` same encryption key (default ya custom, jo `wlp.password.encryption.key` ke through `server.xml` mein specify kiya gaya hai) ka use karta hai jo password ko encode karne ke liye use kiya gaya tha.

---

### Option 2: Use a Standalone Java Program
Agar web application deploy karna feasible nahi hai, to aap ek standalone Java program likh sakte hain aur Liberty runtime libraries ke saath classpath mein run karein. Yeh approach tricky hai kyunki isme manual handling encryption key ki zaroorat hoti hai, especially agar custom key use kiya gaya tha.

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
   - Code ko `PasswordDecoder.java` ke roop mein save karein.
   - Liberty ke jars ke saath compile karein:
     ```bash
     javac -cp /path/to/wlp/lib/* PasswordDecoder.java
     ```
     `/path/to/wlp` ko aapke Liberty installation directory se replace karein (e.g., `/opt/ibm/wlp`).

2. **Run the Program**
   - Agar password default key ke through encrypted hai:
     ```bash
     java -cp /path/to/wlp/lib/*:. PasswordDecoder "{aes}your_encrypted_password"
     ```
   - Agar custom key use kiya gaya hai (e.g., `server.xml` mein define kiya gaya hai as `<variable name="wlp.password.encryption.key" value="yourKey"/>`):
     ```bash
     java -cp /path/to/wlp/lib/*:. PasswordDecoder "{aes}your_encrypted_password" "yourKey"
     ```

3. **Handle the Output**
   Program plain text password ya error print karega agar key incorrect hai.

#### Notes:
- Liberty jars (e.g., in `wlp/lib`) mein `com.ibm.websphere.crypto.PasswordUtil` aur uske dependencies hain.
- Agar custom key use kiya gaya hai aur aap usse provide nahi karte, to decoding fail hoga. `server.xml` ya include ki gayi configuration files mein key ko check karein.

---

### Key Considerations
- **Default vs. Custom Key**:
  - Agar `server.xml` mein `wlp.password.encryption.key` specify nahi kiya gaya, to default key use hota hai aur `PasswordUtil.decode(encoded)` server ke bahar (Option 2) bina additional parameters ke kaam karega.
  - Agar custom key define kiya gaya hai, to aapko explicitly decode karte waqt usse provide karna padta hai (Option 2) ya server context par rely karna padta hai (Option 1).

- **Security**:
  Decoded password ko carefully handle karein, kyunki yeh plain text mein hoga. Logging ya unnecessarily expose karne se bachayein.

- **Preference**:
  Option 1 (web application) generally zyada reliable hai kyunki yeh Liberty environment mein run hota hai, automatically key aur dependencies ko handle karte hue.

Yeh steps follow karke, aap successfully `server.xml` se AES-encrypted password ko decode kar sakte hain, despite `securityUtility` mein decode option ke absence ke.