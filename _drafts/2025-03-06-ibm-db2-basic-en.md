---
audio: false
lang: en
layout: post
title: Basic SQL Operations in IBM DB2 Database
translated: false
generated: true
---

Here’s a step-by-step guide on how to use an IBM DB2 database to perform basic SQL operations (CRUD: Create, Read, Update, Delete) and how to execute these operations using Squirrel SQL Client after connecting to the database.

---

### **Step 1: Connecting to IBM DB2 with Squirrel SQL Client**
Before performing any SQL operations, you need to connect to the IBM DB2 database using Squirrel SQL Client. Here’s how:

1. **Prerequisites**:
   - Ensure you have the connection details: hostname, port, database name, username, and password.
   - Confirm you have the DB2 JDBC driver (e.g., `db2jcc.jar`). If not, download it from IBM’s official site and add it to Squirrel SQL Client.

2. **Open Squirrel SQL Client**:
   - Launch the application on your computer.

3. **Create a New Alias**:
   - Go to the **Aliases** tab on the left-hand side.
   - Click the **+** icon to create a new alias.
   - Give it a name (e.g., "DB2 Connection").

4. **Configure the DB2 Driver**:
   - In the alias setup window, select the **Driver** dropdown.
   - Choose the IBM DB2 driver (e.g., "IBM DB2 JDBC Driver"). If it’s not listed:
     - Click **Extra Class Path**, then **Add**, and locate the DB2 JDBC driver file (e.g., `db2jcc.jar`).
     - Ensure the driver is loaded successfully.

5. **Enter Connection Details**:
   - Specify the connection URL in the format:  
     ```
     jdbc:db2://<hostname>:<port>/<database_name>
     ```
     Example: `jdbc:db2://localhost:50000/mydb`
   - Enter your **username** and **password**.

6. **Test and Connect**:
   - Click **Test Connection** to verify the details.
   - If successful, click **OK** to save the alias.
   - Double-click the alias and click **Connect** to establish the connection.

Once connected, you’ll see the database objects (e.g., tables) in the **Objects** tab on the left.

---

### **Step 2: Performing Basic SQL Operations (CRUD)**
With the connection established, you can use SQL to perform CRUD operations. These operations are executed in Squirrel SQL Client’s **SQL Editor**. Here’s how to do each one:

#### **1. Create (INSERT)**
To add new data to a table:
- **Syntax**:  
  ```
  INSERT INTO table_name (column1, column2, column3) VALUES (value1, value2, value3);
  ```
- **Example**:  
  Suppose you have an `employees` table with columns `id` (INTEGER), `name` (VARCHAR), `position` (VARCHAR), and `department` (VARCHAR). To add a new employee:  
  ```
  INSERT INTO employees (id, name, position, department) VALUES (1, 'John Doe', 'Manager', 'Sales');
  ```
- **Notes**:
  - Ensure values match the column data types (e.g., strings in single quotes).
  - If a column is a primary key (e.g., `id`), the value must be unique.

#### **2. Read (SELECT)**
To retrieve data from a table:
- **Syntax**:  
  ```
  SELECT column1, column2 FROM table_name WHERE condition;
  ```
- **Examples**:  
  - Get all columns from the `employees` table:  
    ```
    SELECT * FROM employees;
    ```
  - Get specific columns:  
    ```
    SELECT id, name, position FROM employees;
    ```
  - Filter with a condition:  
    ```
    SELECT * FROM employees WHERE department = 'Sales';
    ```
- **Notes**:
  - Use `*` to select all columns, or list specific ones.
  - The `WHERE` clause is optional but useful for filtering.

#### **3. Update (UPDATE)**
To modify existing data:
- **Syntax**:  
  ```
  UPDATE table_name SET column1 = value1, column2 = value2 WHERE condition;
  ```
- **Example**:  
  Change the position of the employee with `id = 1`:  
  ```
  UPDATE employees SET position = 'Senior Manager' WHERE id = 1;
  ```
  Update multiple columns:  
  ```
  UPDATE employees SET position = 'Senior Manager', department = 'Marketing' WHERE id = 1;
  ```
- **Notes**:
  - The `WHERE` clause specifies which rows to update. Without it, all rows are updated—be cautious!

#### **4. Delete (DELETE)**
To remove data from a table:
- **Syntax**:  
  ```
  DELETE FROM table_name WHERE condition;
  ```
- **Example**:  
  Remove the employee with `id = 1`:  
  ```
  DELETE FROM employees WHERE id = 1;
  ```
  Delete all rows (use with caution):  
  ```
  DELETE FROM employees;
  ```
- **Notes**:
  - Always include a `WHERE` clause unless you intend to delete all data.

---

### **Step 3: Using Squirrel SQL Client to Execute CRUD Operations**
Here’s how to perform these operations within Squirrel SQL Client:

1. **Open the SQL Editor**:
   - After connecting, go to the **Session** window.
   - Locate the **SQL** tab (or a text area labeled "SQL Editor").

2. **Write Your SQL Statement**:
   - Type your `SELECT`, `INSERT`, `UPDATE`, or `DELETE` statement in the editor.  
     Example:  
     ```
     SELECT * FROM employees;
     ```

3. **Execute the Query**:
   - Click the **Run** button (a green triangle) or press **Ctrl+Enter**.
   - For **SELECT**: Results appear in a table below the editor.
   - For **INSERT**, **UPDATE**, **DELETE**: A message shows the number of rows affected (e.g., "1 row inserted").

4. **Run Multiple Statements**:
   - You can write multiple statements separated by semicolons:  
     ```
     INSERT INTO employees (id, name, position) VALUES (2, 'Jane Smith', 'Analyst');
     SELECT * FROM employees;
     ```
   - Execute them together, but confirm Squirrel supports this (some versions may require separate executions).

5. **View Results**:
   - For `SELECT`, check the results pane.
   - For other operations, verify the affected rows message.

---

### **Additional Tips**
- **Transactions**:
  - In DB2, changes from `INSERT`, `UPDATE`, or `DELETE` may require a `COMMIT` to save them permanently:  
    ```
    COMMIT;
    ```
  - To undo changes, use:  
    ```
    ROLLBACK;
    ```
  - In Squirrel SQL Client, check the **Auto-Commit** setting (under the session toolbar or preferences). If enabled, each statement is committed automatically; if disabled, you must manually commit.

- **Syntax and Data Types**:
  - Use single quotes for strings (e.g., `'Sales'`).
  - Match values to column data types (e.g., integers without quotes).
  - For dates or special types, use DB2-compatible formats (e.g., `'2023-10-25'` for DATE).

- **Safety**:
  - Double-check `WHERE` clauses in `UPDATE` and `DELETE` to avoid unintended changes.
  - Test with `SELECT` first to confirm the rows you’ll affect.

- **DB2 Compatibility**:
  - Basic SQL (as shown) works with DB2. For advanced features, refer to IBM DB2 documentation.

---

### **Summary**
After connecting to an IBM DB2 database with Squirrel SQL Client:
- Use the **SQL Editor** to write and execute:
  - `INSERT` to add data.
  - `SELECT` to retrieve data.
  - `UPDATE` to modify data.
  - `DELETE` to remove data.
- Run queries with the **Run** button or shortcut.
- Check results or affected rows in the interface.
- Manage transactions with `COMMIT` or `ROLLBACK` if auto-commit is off.

This approach lets you perform all CRUD operations efficiently in Squirrel SQL Client with DB2. If you have specific tables or examples, apply these steps accordingly!