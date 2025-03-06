---
title: Issues about SQuirrelSQL with IBM DB2 Databases
lang: en
layout: post
audio: false
translated: false
generated: true
---

When using the Squirrel SQL client to connect to your IBM DB2 database named ADB and running the query `SELECT * FROM ADB.EDATA`, you’re encountering an "undefined name" error. This error typically means that the database cannot find the object (in this case, `EDATA`) you’re trying to query. Let’s break down why this might be happening and how to resolve it step by step.

### Why the Error Occurs
The "undefined name" error (often associated with SQLCODE -204 and SQLSTATE 42704 in DB2) suggests one of the following issues:
1. **The table `EDATA` doesn’t exist in the `ADB` schema.**
2. **The schema or table name is misspelled or uses a different case.**
3. **You don’t have sufficient privileges to access the table.**
4. **The connection or configuration in Squirrel SQL isn’t pointing to the right database or schema.**

Since you mentioned that the database `ADB` has "a lot of objects, like EDATA," it implies that `EDATA` should exist, but we need to confirm its exact location and accessibility.

### Steps to Diagnose and Fix the Issue

#### 1. Verify Your Database Connection
First, ensure that Squirrel SQL is connected to the correct database, `ADB`. In DB2, you connect to a database, and within that database, there are multiple schemas. Check your connection settings in Squirrel SQL:
- Open the connection properties for your alias in Squirrel SQL.
- Confirm that the database name specified is indeed `ADB`.

If you’re connected to a different database, update the connection settings and reconnect.

#### 2. Confirm the Schema Name
In your query, `ADB.EDATA` assumes that `ADB` is the schema containing the table `EDATA`. However, `ADB` might be the database name rather than the schema name. In DB2, the schema is a separate namespace within the database. To list all schemas in the `ADB` database, run this query:

```sql
SELECT SCHEMANAME FROM SYSCAT.SCHEMATA
```

- Look for `ADB` in the results. If it’s present, `ADB` is a valid schema.
- If `ADB` isn’t listed, it confirms that `ADB` is the database name, not the schema. In that case, `EDATA` might reside in a different schema (e.g., your default schema, often your username, or another schema like `SYSIBM`).

#### 3. Check for the Table in the `ADB` Schema
Assuming `ADB` is the schema, verify that `EDATA` exists within it. Run this query to list all tables in the `ADB` schema:

```sql
SELECT TABNAME FROM SYSCAT.TABLES WHERE TABSCHEMA = 'ADB'
```

- If `EDATA` appears in the list, the table exists in the `ADB` schema.
- If not, either the table doesn’t exist in that schema, or there’s a typo or case-sensitivity issue (more on this below).

#### 4. Handle Case Sensitivity
In DB2, schema and table names are case-sensitive if created with quotes (e.g., `"EDATA"`). By default, unquoted names are folded to uppercase. Since you wrote `ADB.EDATA`, DB2 interprets it as `ADB.EDATA` (all uppercase). If the table was created with a different case (e.g., `"EData"`), you’ll need to match it exactly. Try this:

```sql
SELECT * FROM "ADB"."EDATA"
```

If that works, the issue is case sensitivity. Alternatively, check the exact name:

```sql
SELECT TABNAME FROM SYSCAT.TABLES WHERE TABSCHEMA = 'ADB'
```

Look at the exact spelling and case of `EDATA` in the results, and adjust your query accordingly (e.g., `SELECT * FROM ADB."EData"` if it’s listed as `EData`).

#### 5. Search Across All Schemas
If `EDATA` isn’t in the `ADB` schema, it might be in another schema. Search the entire database for `EDATA`:

```sql
SELECT TABSCHEMA, TABNAME FROM SYSCAT.TABLES WHERE TABNAME = 'EDATA'
```

- If this returns a row like `SOME_SCHEMA | EDATA`, then `EDATA` exists in `SOME_SCHEMA`, not `ADB`. Update your query to `SELECT * FROM SOME_SCHEMA.EDATA`.
- If no rows are returned, `EDATA` doesn’t exist as a table in the database.

#### 6. Check Object Type
`EDATA` might not be a table but a view, alias, or nickname (e.g., for a remote table). Check these possibilities:
- **Views:**
  ```sql
  SELECT VIEWNAME FROM SYSCAT.VIEWS WHERE VIEWSCHEMA = 'ADB'
  ```
- **Aliases or Nicknames:**
  ```sql
  SELECT TABNAME, TYPE FROM SYSCAT.TABLES WHERE TABSCHEMA = 'ADB' AND TABNAME = 'EDATA'
  ```
  - `TYPE = 'A'` indicates an alias; `TYPE = 'N'` indicates a nickname. If so, query it as is (`ADB.EDATA`), but ensure the underlying object exists and is accessible.

#### 7. Verify Permissions
Although "undefined name" typically indicates the object doesn’t exist, it’s worth checking your privileges:

```sql
SELECT GRANTOR, GRANTEE, SELECTAUTH FROM SYSCAT.TABAUTH WHERE TABSCHEMA = 'ADB' AND TABNAME = 'EDATA'
```

- If your username (or a role you have) is listed with `SELECTAUTH = 'Y'`, you have permission.
- If not, contact your database administrator to grant you `SELECT` privileges:
  ```sql
  GRANT SELECT ON ADB.EDATA TO YOUR_USERNAME
  ```

#### 8. Look for Typos or Similar Names
If `EDATA` isn’t found, there might be a typo. Search for similar table names:

```sql
SELECT TABNAME FROM SYSCAT.TABLES WHERE TABSCHEMA = 'ADB' AND TABNAME LIKE '%EDATA%'
```

If you see something like `E_DATA` or `EDATA1`, use that name instead (e.g., `SELECT * FROM ADB.E_DATA`).

### How to Fix It
Based on the above diagnostics, here’s how to resolve the issue:
- **If `EDATA` exists in `ADB`:** Use the correct case-sensitive name (e.g., `SELECT * FROM "ADB"."EDATA"`).
- **If `EDATA` is in another schema:** Update the schema in your query (e.g., `SELECT * FROM OTHER_SCHEMA.EDATA`).
- **If `EDATA` doesn’t exist:** Confirm with your database administrator or colleagues that the table exists and get its correct name and schema.
- **If it’s a permission issue:** Request `SELECT` privileges from your administrator.
- **If it’s a connection issue:** Fix your Squirrel SQL connection settings to point to the right database.

### Example Resolution
Suppose you run `SELECT TABSCHEMA, TABNAME FROM SYSCAT.TABLES WHERE TABNAME = 'EDATA'` and get:
```
TABSCHEMA | TABNAME
----------|---------
USER1     | EDATA
```
Then, your query should be:
```sql
SELECT * FROM USER1.EDATA
```

If the table doesn’t appear anywhere, it likely doesn’t exist, and you’ll need to clarify its name or location.

### Final Notes
Start by running the diagnostic queries in Squirrel SQL to pinpoint the issue. The most likely cause, given the "undefined name" error, is that `EDATA` isn’t in the `ADB` schema or has a different name/case. Once you identify the correct schema and table name, your query should work. If you’re still stuck, check the detailed error message in Squirrel SQL (e.g., SQLCODE) for more clues or consult your database administrator.

---

When you run the query `SELECT * FROM SYSCAT.TABLES` in Squirrel SQL Client connected to an IBM DB2 database and then commit, seeing only "commit successfully" without any results can be confusing. The `SYSCAT.TABLES` view in DB2 should display a list of all tables in the database, including system tables, so you would expect to see some output. Let’s walk through why this might be happening and how to resolve it.

### Understanding the Behavior
First, it’s worth noting that a `SELECT` statement doesn’t modify data, so committing after running it doesn’t affect the query’s results. The "commit successfully" message likely relates to the transaction state in Squirrel SQL Client (e.g., if "Auto Commit" is off), but it’s unrelated to whether results are displayed. The key issue is that no data appears in the "Results" tab, which suggests a problem with the query execution, permissions, or how the tool is displaying the output.

### Steps to Diagnose and Fix the Issue

#### 1. **Verify the Query Execution in Squirrel SQL Client**
   - **Check the "Results" Tab**: After running `SELECT * FROM SYSCAT.TABLES`, ensure you’re looking at the "Results" tab in Squirrel SQL Client. If you’re on a different tab (e.g., "Messages"), you might miss the output.
   - **Look at the "Messages" Tab**: This tab may show errors or status messages about the query. If there’s an error (e.g., "access denied"), it will appear here.
   - **Check the Status Bar**: At the bottom of Squirrel SQL Client, the status bar often indicates how many rows were returned (e.g., "Fetched 0 rows"). This can confirm whether the query executed but returned no data.
   - **Row Limit Setting**: Squirrel SQL Client limits the number of rows displayed by default. Go to the **SQL** menu, select **Limit Rows**, and ensure it’s not set to 0 or a very low number. If it is, increase it (e.g., to 1000) and rerun the query.

#### 2. **Test Basic Connectivity and Permissions**
   - **Run a Simple Query**: Try `SELECT * FROM SYSIBM.SYSDUMMY1`. This is a built-in DB2 table that always returns one row with a single column (`IBMREQD`). If this works and shows a result, your connection is active, and the issue is specific to `SYSCAT.TABLES`.
   - **Check the Current Database**: Confirm you’re connected to the intended database (e.g., `ADB`). Run `SELECT CURRENT SERVER FROM SYSIBM.SYSDUMMY1` to display the database name. If it’s not the expected database, reconnect to the correct one via Squirrel SQL Client’s connection settings.

#### 3. **Investigate Permissions on SYSCAT.TABLES**
   - **Why Permissions Matter**: `SYSCAT.TABLES` is a system catalog view in DB2, and accessing it requires at least the `SELECT` privilege on the view or broader `DATAACCESS` authority. If your user account lacks these privileges, the query might execute without errors but return no rows, or it might fail silently depending on the tool’s behavior.
   - **Test Another Catalog View**: Run `SELECT * FROM SYSCAT.SCHEMATA` to see if you can access other system catalog views. If this also returns no rows or an error, it’s a strong indicator of a permissions issue.
   - **Action**: If you suspect permissions are the problem, contact your database administrator to verify your privileges. They can grant you access with a command like:
     ```sql
     GRANT SELECT ON SYSCAT.TABLES TO YOUR_USERNAME;
     ```
     Alternatively, if you’re the administrator, execute this yourself using an account with sufficient authority.

#### 4. **Confirm Database Content**
   - **Are There Tables?**: Although you mentioned there are "a lot of objects" in the database, it’s worth confirming that `SYSCAT.TABLES` should have data. This view includes both user-defined and system tables, so even a new database has entries. If other queries (e.g., on user tables like `MYSCHEMA.MYTABLE`) work, this step may be unnecessary.
   - **Connection Context**: Double-check your connection properties in Squirrel SQL Client (under the "Connections" tab) to ensure you’re not connected to an empty or different database.

#### 5. **Rule Out Tool-Specific Issues**
   - **Filters**: In the "Results" tab, look for a filter icon or setting that might be hiding rows. If a filter is applied, disable it and rerun the query.
   - **Execution Delay**: If the database is large, the query might take time to fetch results. Wait a few seconds after running it, though "commit successfully" suggests execution has completed.
   - **Logs**: Check Squirrel SQL Client’s logs (accessible via the tool’s help or configuration menu) for any errors related to DB2 connectivity.

### Likely Cause and Solution
The most probable reason you’re not seeing results is that your user account lacks the necessary permissions to query `SYSCAT.TABLES`. This is common in DB2 environments where access to system catalog views is restricted. Here’s what to do:

- **Verify Permissions**: Ask your database administrator to confirm whether your user has `SELECT` privilege on `SYSCAT.TABLES` or `DATAACCESS` authority.
- **Test Alternatives**: Run `SELECT * FROM SYSIBM.SYSDUMMY1` and `SELECT * FROM SYSCAT.SCHEMATA` to narrow down the issue.
- **Adjust Privileges**: If permissions are the issue, request or grant the required access as described above.

If permissions are confirmed and the problem persists, focus on Squirrel SQL Client settings (e.g., row limits, tab selection) or verify the database connection.

### Final Notes
By following these steps, you should identify whether the issue is due to permissions, tool configuration, or an unexpected database state. Start with the simple tests (`SYSIBM.SYSDUMMY1`) and escalate to your administrator if needed. Once resolved, `SELECT * FROM SYSCAT.TABLES` should display the expected list of tables.