---
audio: false
lang: en
layout: post
title: SQuirreL SQL Client and DB2 Database
translated: false
generated: true
---

To use your IBM DB2 JCC JAR (`db2jcc.jar`) in SQuirreL SQL Client and connect to a DB2 database, follow these detailed steps. This process involves configuring the DB2 driver in SQuirreL and setting up a connection alias.

---

### Step 1: Verify the JAR File
- Ensure you have the correct DB2 JDBC driver JAR file. The file you mentioned, `db2jcc.jar`, is typically the right one for IBM DB2, though some setups might use `db2jcc4.jar` depending on the version.
- Check if your DB2 installation requires an additional license file (e.g., `db2jcc_license_cisuz.jar`). If so, locate this file as well, as it may be needed to avoid license-related errors when connecting.

---

### Step 2: Configure the DB2 Driver in SQuirreL SQL Client
1. **Open SQuirreL SQL Client**:
   - Launch the application on your system.

2. **Access the Drivers Tab**:
   - In the left panel, click the **Drivers** tab to view the list of available database drivers.

3. **Locate or Add the DB2 Driver**:
   - Look for an existing DB2 driver in the list (e.g., "IBM DB2 App Driver"). It might be marked with a red X if it’s not configured properly.
   - If it’s present, you can modify it. If not, you’ll need to create a new driver:
     - **Modify Existing Driver**: Double-click the DB2 driver entry.
     - **Add New Driver**: Click the **+** icon in the Drivers tab to open the "Add Driver" wizard.

4. **Configure the Driver Settings**:
   - **Name**: Enter a descriptive name, such as "IBM DB2 JCC Driver."
   - **Example URL**: Set this to `jdbc:db2://<host>:<port>/<database>` (you’ll customize this later for your specific database).
   - **Class Name**: Enter `com.ibm.db2.jcc.DB2Driver` (this is the standard driver class for DB2 JDBC).

5. **Add the JAR File**:
   - Go to the **Extra Class Path** tab in the driver configuration window.
   - Click **Add**, then browse to and select the location of your `db2jcc.jar` file.
   - If you have a license JAR (e.g., `db2jcc_license_cisuz.jar`), click **Add** again and include it as well.

6. **Save the Configuration**:
   - Click **OK** to save the driver settings. The DB2 driver should now appear in the Drivers tab with a checkmark, indicating it’s properly configured.

---

### Step 3: Create a Database Alias
1. **Switch to the Aliases Tab**:
   - In the left panel, click the **Aliases** tab, which manages your database connections.

2. **Add a New Alias**:
   - Click the **+** icon to open the "Add Alias" wizard.

3. **Configure the Alias**:
   - **Name**: Give your connection a name (e.g., "My DB2 Database").
   - **Driver**: From the dropdown, select the DB2 driver you configured in Step 2 (e.g., "IBM DB2 JCC Driver").
   - **URL**: Enter the connection URL for your database in the format:
     ```
     jdbc:db2://<host>:<port>/<database>
     ```
     Replace `<host>` (e.g., `localhost` or your server’s IP), `<port>` (e.g., `50000`, the default DB2 port), and `<database>` (your database name) with your actual details. For example:
     ```
     jdbc:db2://localhost:50000/mydb
     ```
   - **User Name** and **Password**: Provide your DB2 database credentials.

4. **Save and Connect**:
   - Click **OK** to save the alias.
   - In the Aliases tab, double-click your new alias to connect. Enter your password if prompted.

---

### Potential Issues and Solutions
- **License Errors**:
  - If you see an error like "The IBM Data Server for JDBC and SQLJ license was invalid," ensure the license JAR (e.g., `db2jcc_license_cisuz.jar`) is added to the driver’s Extra Class Path.
- **Class Not Found Errors**:
  - If SQuirreL reports "Could not find class com.ibm.db2.jcc.DB2Driver," verify that:
    - The `db2jcc.jar` file is correctly added to the Extra Class Path.
    - The class name is set to `com.ibm.db2.jcc.DB2Driver` with no typos.
- **Multiple JAR Conflicts**:
  - Avoid including multiple versions of the DB2 JDBC driver (e.g., both `db2jcc.jar` and `db2jcc4.jar`) in the Extra Class Path, as this can cause conflicts. Use only the JARs required for your DB2 version.
- **Incorrect URL Format**:
  - Double-check your connection URL syntax. A malformed URL (e.g., missing port or incorrect database name) will prevent connection.

---

By following these steps, you should be able to configure SQuirreL SQL Client to use your `db2jcc.jar` file and successfully connect to your DB2 database. If you encounter any issues, review the troubleshooting tips above or ensure your database server is accessible from your network.