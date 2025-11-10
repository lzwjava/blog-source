---
audio: false
generated: true
lang: hant
layout: post
title: Java 開發人員 Oracle 數據庫指南
translated: true
type: note
---

## 目錄
1. [Oracle 數據庫概述](#oracle-數據庫概述)
2. [安裝與設定](#安裝與設定)
3. [Oracle 數據庫架構](#oracle-數據庫架構)
4. [SQL 基礎](#sql-基礎)
5. [進階 Oracle 功能](#進階-oracle-功能)
6. [Java 數據庫連接](#java-數據庫連接)
7. [連接管理](#連接管理)
8. [ORM 框架](#orm-框架)
9. [性能優化](#性能優化)
10. [安全最佳實踐](#安全最佳實踐)
11. [監控與維護](#監控與維護)

## Oracle 數據庫概述

Oracle Database 是由 Oracle Corporation 生產的多模型數據庫管理系統。它是企業環境中最廣泛使用的关系型數據庫管理系統 (RDBMS) 之一。

### 主要功能
- **ACID 合規性**：通過原子性、一致性、隔離性和持久性確保數據完整性
- **多版本並發控制 (MVCC)**：允許多個用戶同時訪問數據
- **分區**：將大表劃分為較小、易於管理的部分
- **進階安全性**：內置加密、審計和訪問控制
- **高可用性**：Real Application Clusters (RAC) 和 Data Guard
- **可擴展性**：支持大規模數據庫和高交易量

### Oracle 數據庫版本
- **Express Edition (XE)**：免費、功能有限的開發和小型部署版本
- **Standard Edition**：具有核心功能的中階版本
- **Enterprise Edition**：具有進階功能的完整版本
- **Autonomous Database**：基於雲端、自我管理的數據庫服務

## 安裝與設定

### Oracle 數據庫安裝

#### 使用 Oracle Database XE（推薦用於開發）
1. 從 Oracle 官方網站下載 Oracle Database XE
2. 按照平台特定說明進行安裝
3. 使用 Database Configuration Assistant (DBCA) 配置數據庫

#### Docker 安裝（快速設定）
```bash
# 拉取 Oracle Database XE 映像
docker pull container-registry.oracle.com/database/express:21.3.0-xe

# 運行 Oracle Database XE 容器
docker run --name oracle-xe \
  -p 1521:1521 \
  -p 5500:5500 \
  -e ORACLE_PWD=your_password \
  -e ORACLE_CHARACTERSET=AL32UTF8 \
  container-registry.oracle.com/database/express:21.3.0-xe
```

### 客戶端工具
- **SQL*Plus**：命令行界面
- **SQL Developer**：基於 GUI 的開發環境
- **Oracle Enterprise Manager**：基於 Web 的管理控制台
- **DBeaver**：第三方數據庫管理工具

## Oracle 數據庫架構

### 物理架構
- **數據庫文件**：數據文件、控制文件和重做日誌文件
- **參數文件**：配置設定 (PFILE/SPFILE)
- **歸檔日誌文件**：用於恢復的重做日誌文件備份

### 邏輯架構
- **表空間**：包含一個或多個數據文件的邏輯存儲單元
- **模式**：由用戶擁有的數據庫對象集合
- **段**：為數據庫對象分配的空間
- **區間**：連續的存儲塊
- **塊**：最小的存儲單位

### 記憶體架構
- **系統全局區 (SGA)**：共享記憶體區域
  - 數據庫緩衝區快取
  - 共享池
  - 重做日誌緩衝區
  - 大池
- **程序全局區 (PGA)**：每個進程的私有記憶體

## SQL 基礎

### 數據定義語言 (DDL)

#### 創建表
```sql
-- 創建表
CREATE TABLE employees (
    employee_id NUMBER(6) PRIMARY KEY,
    first_name VARCHAR2(20) NOT NULL,
    last_name VARCHAR2(25) NOT NULL,
    email VARCHAR2(50) UNIQUE,
    hire_date DATE DEFAULT SYSDATE,
    job_id VARCHAR2(10),
    salary NUMBER(8,2),
    department_id NUMBER(4),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 添加約束
ALTER TABLE employees 
ADD CONSTRAINT fk_dept_id 
FOREIGN KEY (department_id) 
REFERENCES departments(department_id);

-- 創建索引
CREATE INDEX idx_emp_dept ON employees(department_id);
```

#### Oracle 特定數據類型
- **NUMBER**：具有精度和小數位數的數值數據
- **VARCHAR2**：可變長度字符串
- **CHAR**：固定長度字符串
- **DATE**：日期和時間
- **TIMESTAMP**：具有小數秒的日期和時間
- **CLOB**：字符大對象
- **BLOB**：二進制大對象
- **XMLTYPE**：XML 數據

### 數據操作語言 (DML)

#### 進階查詢
```sql
-- 窗口函數
SELECT 
    employee_id,
    first_name,
    last_name,
    salary,
    RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) as salary_rank,
    LAG(salary, 1) OVER (ORDER BY hire_date) as prev_salary
FROM employees;

-- 通用表表達式 (CTE)
WITH dept_avg_salary AS (
    SELECT department_id, AVG(salary) as avg_salary
    FROM employees
    GROUP BY department_id
)
SELECT e.*, d.avg_salary
FROM employees e
JOIN dept_avg_salary d ON e.department_id = d.department_id;

-- 層次查詢
SELECT employee_id, first_name, last_name, manager_id, LEVEL
FROM employees
START WITH manager_id IS NULL
CONNECT BY PRIOR employee_id = manager_id
ORDER SIBLINGS BY last_name;
```

### PL/SQL 編程

#### 基本 PL/SQL 塊
```sql
DECLARE
    v_employee_count NUMBER;
    v_department_name VARCHAR2(30);
BEGIN
    SELECT COUNT(*) INTO v_employee_count
    FROM employees
    WHERE department_id = 10;
    
    IF v_employee_count > 0 THEN
        SELECT department_name INTO v_department_name
        FROM departments
        WHERE department_id = 10;
        
        DBMS_OUTPUT.PUT_LINE('Department: ' || v_department_name || 
                           ' has ' || v_employee_count || ' employees');
    END IF;
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('No data found');
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error: ' || SQLERRM);
END;
/
```

#### 存儲過程和函數
```sql
-- 存儲過程
CREATE OR REPLACE PROCEDURE update_employee_salary(
    p_employee_id IN NUMBER,
    p_salary_increase IN NUMBER
) AS
    v_current_salary NUMBER;
BEGIN
    SELECT salary INTO v_current_salary
    FROM employees
    WHERE employee_id = p_employee_id;
    
    UPDATE employees
    SET salary = v_current_salary + p_salary_increase
    WHERE employee_id = p_employee_id;
    
    COMMIT;
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        RAISE_APPLICATION_ERROR(-20001, 'Employee not found');
END;
/

-- 函數
CREATE OR REPLACE FUNCTION calculate_annual_salary(
    p_employee_id IN NUMBER
) RETURN NUMBER AS
    v_monthly_salary NUMBER;
BEGIN
    SELECT salary INTO v_monthly_salary
    FROM employees
    WHERE employee_id = p_employee_id;
    
    RETURN v_monthly_salary * 12;
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        RETURN 0;
END;
/
```

## 進階 Oracle 功能

### 分區
```sql
-- 範圍分區
CREATE TABLE sales (
    sale_id NUMBER,
    sale_date DATE,
    amount NUMBER
) PARTITION BY RANGE (sale_date) (
    PARTITION p2023 VALUES LESS THAN (DATE '2024-01-01'),
    PARTITION p2024 VALUES LESS THAN (DATE '2025-01-01'),
    PARTITION p_max VALUES LESS THAN (MAXVALUE)
);

-- 哈希分區
CREATE TABLE customers (
    customer_id NUMBER,
    name VARCHAR2(100)
) PARTITION BY HASH (customer_id) PARTITIONS 4;
```

### 序列
```sql
-- 創建序列
CREATE SEQUENCE emp_seq
    START WITH 1000
    INCREMENT BY 1
    MAXVALUE 9999999
    NOCACHE
    NOCYCLE;

-- 使用序列
INSERT INTO employees (employee_id, first_name, last_name)
VALUES (emp_seq.NEXTVAL, 'John', 'Doe');
```

### 視圖和物化視圖
```sql
-- 創建視圖
CREATE VIEW employee_details AS
SELECT e.employee_id, e.first_name, e.last_name, 
       d.department_name, e.salary
FROM employees e
JOIN departments d ON e.department_id = d.department_id;

-- 物化視圖
CREATE MATERIALIZED VIEW emp_dept_summary
BUILD IMMEDIATE
REFRESH COMPLETE ON DEMAND
AS
SELECT d.department_name, COUNT(*) as employee_count, AVG(salary) as avg_salary
FROM employees e
JOIN departments d ON e.department_id = d.department_id
GROUP BY d.department_name;
```

## Java 數據庫連接

### JDBC 驅動程式設定

#### Maven 依賴
```xml
<dependency>
    <groupId>com.oracle.database.jdbc</groupId>
    <artifactId>ojdbc11</artifactId>
    <version>23.3.0.23.09</version>
</dependency>

<!-- 用於連接池 -->
<dependency>
    <groupId>com.oracle.database.jdbc</groupId>
    <artifactId>ucp</artifactId>
    <version>23.3.0.23.09</version>
</dependency>
```

#### 基本 JDBC 連接
```java
import java.sql.*;

public class OracleConnection {
    private static final String URL = "jdbc:oracle:thin:@localhost:1521:XE";
    private static final String USERNAME = "your_username";
    private static final String PASSWORD = "your_password";
    
    public static Connection getConnection() throws SQLException {
        return DriverManager.getConnection(URL, USERNAME, PASSWORD);
    }
    
    public static void main(String[] args) {
        try (Connection conn = getConnection()) {
            System.out.println("Connected to Oracle Database!");
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
```

### CRUD 操作

#### 數據訪問對象 (DAO) 模式
```java
public class Employee {
    private int employeeId;
    private String firstName;
    private String lastName;
    private String email;
    private Date hireDate;
    private double salary;
    private int departmentId;
    
    // 構造函數、getter 和 setter
    // ...
}

public interface EmployeeDAO {
    void createEmployee(Employee employee);
    Employee getEmployeeById(int id);
    List<Employee> getAllEmployees();
    void updateEmployee(Employee employee);
    void deleteEmployee(int id);
}

public class EmployeeDAOImpl implements EmployeeDAO {
    private Connection connection;
    
    public EmployeeDAOImpl(Connection connection) {
        this.connection = connection;
    }
    
    @Override
    public void createEmployee(Employee employee) {
        String sql = "INSERT INTO employees (employee_id, first_name, last_name, email, salary, department_id) VALUES (emp_seq.NEXTVAL, ?, ?, ?, ?, ?)";
        
        try (PreparedStatement pstmt = connection.prepareStatement(sql)) {
            pstmt.setString(1, employee.getFirstName());
            pstmt.setString(2, employee.getLastName());
            pstmt.setString(3, employee.getEmail());
            pstmt.setDouble(4, employee.getSalary());
            pstmt.setInt(5, employee.getDepartmentId());
            
            pstmt.executeUpdate();
        } catch (SQLException e) {
            throw new RuntimeException("Error creating employee", e);
        }
    }
    
    @Override
    public Employee getEmployeeById(int id) {
        String sql = "SELECT * FROM employees WHERE employee_id = ?";
        
        try (PreparedStatement pstmt = connection.prepareStatement(sql)) {
            pstmt.setInt(1, id);
            ResultSet rs = pstmt.executeQuery();
            
            if (rs.next()) {
                return mapResultSetToEmployee(rs);
            }
        } catch (SQLException e) {
            throw new RuntimeException("Error retrieving employee", e);
        }
        return null;
    }
    
    @Override
    public List<Employee> getAllEmployees() {
        List<Employee> employees = new ArrayList<>();
        String sql = "SELECT * FROM employees ORDER BY employee_id";
        
        try (Statement stmt = connection.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {
            
            while (rs.next()) {
                employees.add(mapResultSetToEmployee(rs));
            }
        } catch (SQLException e) {
            throw new RuntimeException("Error retrieving employees", e);
        }
        return employees;
    }
    
    @Override
    public void updateEmployee(Employee employee) {
        String sql = "UPDATE employees SET first_name = ?, last_name = ?, email = ?, salary = ?, department_id = ? WHERE employee_id = ?";
        
        try (PreparedStatement pstmt = connection.prepareStatement(sql)) {
            pstmt.setString(1, employee.getFirstName());
            pstmt.setString(2, employee.getLastName());
            pstmt.setString(3, employee.getEmail());
            pstmt.setDouble(4, employee.getSalary());
            pstmt.setInt(5, employee.getDepartmentId());
            pstmt.setInt(6, employee.getEmployeeId());
            
            pstmt.executeUpdate();
        } catch (SQLException e) {
            throw new RuntimeException("Error updating employee", e);
        }
    }
    
    @Override
    public void deleteEmployee(int id) {
        String sql = "DELETE FROM employees WHERE employee_id = ?";
        
        try (PreparedStatement pstmt = connection.prepareStatement(sql)) {
            pstmt.setInt(1, id);
            pstmt.executeUpdate();
        } catch (SQLException e) {
            throw new RuntimeException("Error deleting employee", e);
        }
    }
    
    private Employee mapResultSetToEmployee(ResultSet rs) throws SQLException {
        Employee employee = new Employee();
        employee.setEmployeeId(rs.getInt("employee_id"));
        employee.setFirstName(rs.getString("first_name"));
        employee.setLastName(rs.getString("last_name"));
        employee.setEmail(rs.getString("email"));
        employee.setHireDate(rs.getDate("hire_date"));
        employee.setSalary(rs.getDouble("salary"));
        employee.setDepartmentId(rs.getInt("department_id"));
        return employee;
    }
}
```

### 使用存儲過程
```java
public class StoredProcedureExample {
    
    public void updateEmployeeSalary(int employeeId, double salaryIncrease) {
        String sql = "{call update_employee_salary(?, ?)}";
        
        try (Connection conn = OracleConnection.getConnection();
             CallableStatement cstmt = conn.prepareCall(sql)) {
            
            cstmt.setInt(1, employeeId);
            cstmt.setDouble(2, salaryIncrease);
            cstmt.execute();
            
        } catch (SQLException e) {
            throw new RuntimeException("Error calling stored procedure", e);
        }
    }
    
    public double getAnnualSalary(int employeeId) {
        String sql = "{? = call calculate_annual_salary(?)}";
        
        try (Connection conn = OracleConnection.getConnection();
             CallableStatement cstmt = conn.prepareCall(sql)) {
            
            cstmt.registerOutParameter(1, Types.NUMERIC);
            cstmt.setInt(2, employeeId);
            cstmt.execute();
            
            return cstmt.getDouble(1);
            
        } catch (SQLException e) {
            throw new RuntimeException("Error calling function", e);
        }
    }
}
```

## 連接管理

### 使用 Oracle UCP 的連接池
```java
import oracle.ucp.jdbc.PoolDataSource;
import oracle.ucp.jdbc.PoolDataSourceFactory;

public class ConnectionPoolManager {
    private static PoolDataSource poolDataSource;
    
    static {
        try {
            poolDataSource = PoolDataSourceFactory.getPoolDataSource();
            poolDataSource.setURL("jdbc:oracle:thin:@localhost:1521:XE");
            poolDataSource.setUser("your_username");
            poolDataSource.setPassword("your_password");
            poolDataSource.setConnectionFactoryClassName("oracle.jdbc.pool.OracleDataSource");
            
            // 連接池配置
            poolDataSource.setInitialPoolSize(5);
            poolDataSource.setMinPoolSize(5);
            poolDataSource.setMaxPoolSize(20);
            poolDataSource.setConnectionWaitTimeout(5);
            poolDataSource.setInactiveConnectionTimeout(300);
            
        } catch (SQLException e) {
            throw new RuntimeException("Error initializing connection pool", e);
        }
    }
    
    public static Connection getConnection() throws SQLException {
        return poolDataSource.getConnection();
    }
}
```

### 交易管理
```java
public class TransactionExample {
    
    public void transferFunds(int fromAccount, int toAccount, double amount) {
        Connection conn = null;
        try {
            conn = ConnectionPoolManager.getConnection();
            conn.setAutoCommit(false); // 開始交易
            
            // 從源帳戶扣款
            String debitSql = "UPDATE accounts SET balance = balance - ? WHERE account_id = ?";
            try (PreparedStatement debitStmt = conn.prepareStatement(debitSql)) {
                debitStmt.setDouble(1, amount);
                debitStmt.setInt(2, fromAccount);
                debitStmt.executeUpdate();
            }
            
            // 向目標帳戶存款
            String creditSql = "UPDATE accounts SET balance = balance + ? WHERE account_id = ?";
            try (PreparedStatement creditStmt = conn.prepareStatement(creditSql)) {
                creditStmt.setDouble(1, amount);
                creditStmt.setInt(2, toAccount);
                creditStmt.executeUpdate();
            }
            
            conn.commit(); // 提交交易
            
        } catch (SQLException e) {
            if (conn != null) {
                try {
                    conn.rollback(); // 出錯時回滾
                } catch (SQLException ex) {
                    ex.printStackTrace();
                }
            }
            throw new RuntimeException("Error in fund transfer", e);
        } finally {
            if (conn != null) {
                try {
                    conn.setAutoCommit(true); // 重置自動提交
                    conn.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
```

## ORM 框架

### Hibernate 配置
```xml
<!-- hibernate.cfg.xml -->
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE hibernate-configuration PUBLIC
    "-//Hibernate/Hibernate Configuration DTD 3.0//EN"
    "http://www.hibernate.org/dtd/hibernate-configuration-3.0.dtd">
<hibernate-configuration>
    <session-factory>
        <property name="hibernate.connection.driver_class">oracle.jdbc.OracleDriver</property>
        <property name="hibernate.connection.url">jdbc:oracle:thin:@localhost:1521:XE</property>
        <property name="hibernate.connection.username">your_username</property>
        <property name="hibernate.connection.password">your_password</property>
        <property name="hibernate.dialect">org.hibernate.dialect.Oracle12cDialect</property>
        <property name="hibernate.hbm2ddl.auto">update</property>
        <property name="hibernate.show_sql">true</property>
        <property name="hibernate.format_sql">true</property>
        
        <!-- 連接池 -->
        <property name="hibernate.c3p0.min_size">5</property>
        <property name="hibernate.c3p0.max_size">20</property>
        <property name="hibernate.c3p0.timeout">300</property>
        <property name="hibernate.c3p0.max_statements">50</property>
        <property name="hibernate.c3p0.idle_test_period">3000</property>
    </session-factory>
</hibernate-configuration>
```

### 具有 Oracle 特定功能的 JPA 實體
```java
@Entity
@Table(name = "employees")
@SequenceGenerator(name = "emp_seq", sequenceName = "emp_seq", allocationSize = 1)
public class Employee {
    
    @Id
    @GeneratedValue(strategy = GenerationType.SEQUENCE, generator = "emp_seq")
    @Column(name = "employee_id")
    private Integer employeeId;
    
    @Column(name = "first_name", nullable = false, length = 20)
    private String firstName;
    
    @Column(name = "last_name", nullable = false, length = 25)
    private String lastName;
    
    @Column(name = "email", unique = true, length = 50)
    private String email;
    
    @Column(name = "hire_date")
    @Temporal(TemporalType.DATE)
    private Date hireDate;
    
    @Column(name = "salary", precision = 8, scale = 2)
    private BigDecimal salary;
    
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "department_id")
    private Department department;
    
    @CreationTimestamp
    @Column(name = "created_at")
    private Timestamp createdAt;
    
    @UpdateTimestamp
    @Column(name = "updated_at")
    private Timestamp updatedAt;
    
    // 構造函數、getter 和 setter
    // ...
}
```

### Spring Boot 與 Oracle
```yaml
# application.yml
spring:
  datasource:
    url: jdbc:oracle:thin:@localhost:1521:XE
    username: your_username
    password: your_password
    driver-class-name: oracle.jdbc.OracleDriver
    hikari:
      minimum-idle: 5
      maximum-pool-size: 20
      idle-timeout: 300000
      max-lifetime: 1800000
      connection-timeout: 30000
      
  jpa:
    hibernate:
      ddl-auto: update
    show-sql: true
    properties:
      hibernate:
        dialect: org.hibernate.dialect.Oracle12cDialect
        format_sql: true
        jdbc:
          batch_size: 20
        order_inserts: true
        order_updates: true
```

## 性能優化

### 查詢優化
```sql
-- 有效使用索引
CREATE INDEX idx_emp_dept_salary ON employees(department_id, salary);

-- 必要時使用提示
SELECT /*+ INDEX(e idx_emp_dept_salary) */ 
       e.employee_id, e.first_name, e.last_name
FROM employees e
WHERE department_id = 10 AND salary > 50000;

-- 使用綁定變量防止 SQL 注入並提高性能
SELECT * FROM employees WHERE employee_id = :employee_id;
```

### Java 性能提示
```java
// 對多個插入使用批處理
public void batchInsertEmployees(List<Employee> employees) {
    String sql = "INSERT INTO employees (employee_id, first_name, last_name, email, salary, department_id) VALUES (emp_seq.NEXTVAL, ?, ?, ?, ?, ?)";
    
    try (Connection conn = ConnectionPoolManager.getConnection();
         PreparedStatement pstmt = conn.prepareStatement(sql)) {
        
        conn.setAutoCommit(false);
        
        for (Employee emp : employees) {
            pstmt.setString(1, emp.getFirstName());
            pstmt.setString(2, emp.getLastName());
            pstmt.setString(3, emp.getEmail());
            pstmt.setDouble(4, emp.getSalary());
            pstmt.setInt(5, emp.getDepartmentId());
            pstmt.addBatch();
        }
        
        pstmt.executeBatch();
        conn.commit();
        
    } catch (SQLException e) {
        throw new RuntimeException("Error in batch insert", e);
    }
}

// 對大型結果集使用適當的提取大小
public List<Employee> getAllEmployeesOptimized() {
    List<Employee> employees = new ArrayList<>();
    String sql = "SELECT * FROM employees ORDER BY employee_id";
    
    try (Connection conn = ConnectionPoolManager.getConnection();
         PreparedStatement pstmt = conn.prepareStatement(sql)) {
        
        pstmt.setFetchSize(1000); // 優化提取大小
        ResultSet rs = pstmt.executeQuery();
        
        while (rs.next()) {
            employees.add(mapResultSetToEmployee(rs));
        }
        
    } catch (SQLException e) {
        throw new RuntimeException("Error retrieving employees", e);
    }
    return employees;
}
```

## 安全最佳實踐

### 連接安全
```java
// 使用加密連接
String url = "jdbc:oracle:thin:@(DESCRIPTION=(ADDRESS=(PROTOCOL=tcps)(HOST=localhost)(PORT=2484))(CONNECT_DATA=(SERVICE_NAME=XE)))" +
            "?oracle.net.ssl_client_authentication=false" +
            "&oracle.net.ssl_server_cert_dn=\"CN=localhost\"";

// 使用連接屬性進行安全設定
Properties props = new Properties();
props.setProperty("user", username);
props.setProperty("password", password);
props.setProperty("oracle.net.encryption_client", "REQUIRED");
props.setProperty("oracle.net.encryption_types_client", "AES256");
props.setProperty("oracle.net.crypto_checksum_client", "REQUIRED");
props.setProperty("oracle.net.crypto_checksum_types_client", "SHA256");

Connection conn = DriverManager.getConnection(url, props);
```

### SQL 注入預防
```java
// 始終使用參數化查詢
public Employee findEmployeeByEmail(String email) {
    String sql = "SELECT * FROM employees WHERE email = ?"; // 安全
    // String sql = "SELECT * FROM employees WHERE email = '" + email + "'"; // 危險！
    
    try (Connection conn = ConnectionPoolManager.getConnection();
         PreparedStatement pstmt = conn.prepareStatement(sql)) {
        
        pstmt.setString(1, email);
        ResultSet rs = pstmt.executeQuery();
        
        if (rs.next()) {
            return mapResultSetToEmployee(rs);
        }
        
    } catch (SQLException e) {
        throw new RuntimeException("Error finding employee", e);
    }
    return null;
}
```

## 監控與維護

### 數據庫監控查詢
```sql
-- 檢查表大小
SELECT table_name, 
       ROUND(((num_rows * avg_row_len) / 1024 / 1024), 2) as size_mb
FROM user_tables
ORDER BY size_mb DESC;

-- 監控活動會話
SELECT username, osuser, machine, program, status, logon_time
FROM v$session
WHERE username IS NOT NULL
ORDER BY logon_time;

-- 檢查表空間使用情況
SELECT tablespace_name,
       ROUND(((total_bytes - free_bytes) / 1024 / 1024), 2) as used_mb,
       ROUND((free_bytes / 1024 / 1024), 2) as free_mb,
       ROUND(((total_bytes - free_bytes) / total_bytes * 100), 2) as percent_used
FROM (
    SELECT tablespace_name, SUM(bytes) as total_bytes
    FROM dba_data_files
    GROUP BY tablespace_name
) total,
(
    SELECT tablespace_name, SUM(bytes) as free_bytes
    FROM dba_free_space
    GROUP BY tablespace_name
) free
WHERE total.tablespace_name = free.tablespace_name(+);
```

### 應用程序監控
```java
// 連接池監控
public class ConnectionPoolMonitor {
    
    public void printPoolStatistics() {
        try {
            oracle.ucp.jdbc.PoolDataSource pds = (oracle.ucp.jdbc.PoolDataSource) poolDataSource;
            
            System.out.println("=== 連接池統計 ===");
            System.out.println("可用連接: " + pds.getAvailableConnectionsCount());
            System.out.println("借用連接: " + pds.getBorrowedConnectionsCount());
            System.out.println("峰值池大小: " + pds.getPeakPoolSize());
            System.out.println("連接池大小: " + pds.getPoolSize());
            System.out.println("================================");
            
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}

// 查詢性能監控
public class QueryPerformanceMonitor {
    
    public <T> T executeWithTiming(String operationName, Supplier<T> operation) {
        long startTime = System.currentTimeMillis();
        
        try {
            T result = operation.get();
            long duration = System.currentTimeMillis() - startTime;
            
            System.out.println(operationName + " 在 " + duration + "ms 內執行");
            
            if (duration > 1000) { // 記錄慢查詢
                System.out.println("檢測到慢查詢: " + operationName);
            }
            
            return result;
            
        } catch (Exception e) {
            System.err.println(operationName + " 中的錯誤: " + e.getMessage());
            throw e;
        }
    }
}
```

## 最佳實踐總結

### 數據庫設計
- 使用適當的數據類型和約束
- 實施適當的索引策略
- 考慮對大表進行分區
- 對主鍵使用序列
- 適當規範化數據

### Java 開發
- 始終使用連接池
- 實施適當的異常處理
- 使用參數化查詢防止 SQL 注入
- 正確關閉資源（使用 try-with-resources）
- 對於複雜應用程序考慮使用 ORM 框架

### 性能
- 監控和優化慢查詢
- 對批量數據操作使用批處理操作
- 實施適當的快取策略
- 監控連接池指標
- 使用適當的提取大小

### 安全
- 在生產環境中使用加密連接
- 實施適當的身份驗證和授權
- 切勿硬編碼憑證
- 使用最小權限原則
- 定期安全審計

本綜合指南為在 Java 應用程序中使用 Oracle Database 提供了堅實的基礎。請始終參考官方 Oracle 文檔以獲取最新信息和最佳實踐。