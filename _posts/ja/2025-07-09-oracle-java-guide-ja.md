---
audio: false
generated: true
lang: ja
layout: post
title: Java開発者のためのOracleデータベースガイド
translated: true
type: note
---

## 目次
1. [Oracle Database概要](#oracle-database概要)
2. [インストールとセットアップ](#インストールとセットアップ)
3. [Oracle Databaseアーキテクチャ](#oracle-databaseアーキテクチャ)
4. [SQL基礎](#sql基礎)
5. [高度なOracle機能](#高度なoracle機能)
6. [Java Database Connectivity](#java-database-connectivity)
7. [接続管理](#接続管理)
8. [ORMフレームワーク](#ormフレームワーク)
9. [パフォーマンス最適化](#パフォーマンス最適化)
10. [セキュリティベストプラクティス](#セキュリティベストプラクティス)
11. [監視とメンテナンス](#監視とメンテナンス)

## Oracle Database概要

Oracle Databaseは、Oracle Corporationが開発するマルチモデルデータベース管理システムです。エンタープライズ環境で最も広く使用されているリレーショナルデータベース管理システム（RDBMS）の一つです。

### 主な機能
- **ACID準拠**: Atomicity、Consistency、Isolation、Durabilityによるデータ整合性の確保
- **Multi-version Concurrency Control (MVCC)**: 複数ユーザーによる同時データアクセスを可能にする
- **パーティショニング**: 大きなテーブルを小さな管理可能な部分に分割
- **高度なセキュリティ**: 組み込みの暗号化、監査、アクセス制御
- **高可用性**: Real Application Clusters (RAC) と Data Guard
- **スケーラビリティ**: 大規模データベースと高トランザクション量をサポート

### Oracle Databaseエディション
- **Express Edition (XE)**: 開発と小規模展開向けの無料限定版
- **Standard Edition**: コア機能を備えた中規模エディション
- **Enterprise Edition**: 高度な機能を備えた完全版
- **Autonomous Database**: クラウドベースの自己管理データベースサービス

## インストールとセットアップ

### Oracle Databaseインストール

#### Oracle Database XEの使用（開発推奨）
1. Oracle公式サイトからOracle Database XEをダウンロード
2. プラットフォーム固有の指示に従ってインストール
3. Database Configuration Assistant (DBCA)を使用してデータベースを設定

#### Dockerインストール（クイックセットアップ）
```bash
# Oracle Database XEイメージをプル
docker pull container-registry.oracle.com/database/express:21.3.0-xe

# Oracle Database XEコンテナを実行
docker run --name oracle-xe \
  -p 1521:1521 \
  -p 5500:5500 \
  -e ORACLE_PWD=your_password \
  -e ORACLE_CHARACTERSET=AL32UTF8 \
  container-registry.oracle.com/database/express:21.3.0-xe
```

### クライアントツール
- **SQL*Plus**: コマンドラインインターフェース
- **SQL Developer**: GUIベースの開発環境
- **Oracle Enterprise Manager**: Webベースの管理コンソール
- **DBeaver**: サードパーティ製データベース管理ツール

## Oracle Databaseアーキテクチャ

### 物理アーキテクチャ
- **データベースファイル**: データファイル、制御ファイル、REDOログファイル
- **パラメータファイル**: 設定ファイル（PFILE/SPFILE）
- **アーカイブログファイル**: リカバリ用のREDOログファイルのバックアップ

### 論理アーキテクチャ
- **表領域**: 1つ以上のデータファイルを含む論理記憶単位
- **スキーマ**: ユーザーが所有するデータベースオブジェクトの集合
- **セグメント**: データベースオブジェクトに割り当てられた領域
- **エクステント**: 連続した記憶ブロック
- **ブロック**: 最小の記憶単位

### メモリアーキテクチャ
- **System Global Area (SGA)**: 共有メモリ領域
  - データベースバッファキャッシュ
  - 共有プール
  - REDOログバッファ
  - ラージプール
- **Program Global Area (PGA)**: 各プロセス用のプライベートメモリ

## SQL基礎

### データ定義言語（DDL）

#### テーブルの作成
```sql
-- テーブル作成
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

-- 制約の追加
ALTER TABLE employees 
ADD CONSTRAINT fk_dept_id 
FOREIGN KEY (department_id) 
REFERENCES departments(department_id);

-- インデックスの作成
CREATE INDEX idx_emp_dept ON employees(department_id);
```

#### Oracle固有のデータ型
- **NUMBER**: 精度とスケールを持つ数値データ
- **VARCHAR2**: 可変長文字列
- **CHAR**: 固定長文字列
- **DATE**: 日付と時刻
- **TIMESTAMP**: 小数秒を含む日付と時刻
- **CLOB**: 文字ラージオブジェクト
- **BLOB**: バイナリラージオブジェクト
- **XMLTYPE**: XMLデータ

### データ操作言語（DML）

#### 高度なクエリ
```sql
-- ウィンドウ関数
SELECT 
    employee_id,
    first_name,
    last_name,
    salary,
    RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) as salary_rank,
    LAG(salary, 1) OVER (ORDER BY hire_date) as prev_salary
FROM employees;

-- 共通テーブル式（CTE）
WITH dept_avg_salary AS (
    SELECT department_id, AVG(salary) as avg_salary
    FROM employees
    GROUP BY department_id
)
SELECT e.*, d.avg_salary
FROM employees e
JOIN dept_avg_salary d ON e.department_id = d.department_id;

-- 階層クエリ
SELECT employee_id, first_name, last_name, manager_id, LEVEL
FROM employees
START WITH manager_id IS NULL
CONNECT BY PRIOR employee_id = manager_id
ORDER SIBLINGS BY last_name;
```

### PL/SQLプログラミング

#### 基本的なPL/SQLブロック
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
        
        DBMS_OUTPUT.PUT_LINE('部署: ' || v_department_name || 
                           ' には ' || v_employee_count || ' 名の従業員がいます');
    END IF;
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('データが見つかりません');
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('エラー: ' || SQLERRM);
END;
/
```

#### ストアドプロシージャと関数
```sql
-- ストアドプロシージャ
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
        RAISE_APPLICATION_ERROR(-20001, '従業員が見つかりません');
END;
/

-- 関数
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

## 高度なOracle機能

### パーティショニング
```sql
-- 範囲パーティショニング
CREATE TABLE sales (
    sale_id NUMBER,
    sale_date DATE,
    amount NUMBER
) PARTITION BY RANGE (sale_date) (
    PARTITION p2023 VALUES LESS THAN (DATE '2024-01-01'),
    PARTITION p2024 VALUES LESS THAN (DATE '2025-01-01'),
    PARTITION p_max VALUES LESS THAN (MAXVALUE)
);

-- ハッシュパーティショニング
CREATE TABLE customers (
    customer_id NUMBER,
    name VARCHAR2(100)
) PARTITION BY HASH (customer_id) PARTITIONS 4;
```

### シーケンス
```sql
-- シーケンス作成
CREATE SEQUENCE emp_seq
    START WITH 1000
    INCREMENT BY 1
    MAXVALUE 9999999
    NOCACHE
    NOCYCLE;

-- シーケンスの使用
INSERT INTO employees (employee_id, first_name, last_name)
VALUES (emp_seq.NEXTVAL, 'John', 'Doe');
```

### ビューと実体化ビュー
```sql
-- ビュー作成
CREATE VIEW employee_details AS
SELECT e.employee_id, e.first_name, e.last_name, 
       d.department_name, e.salary
FROM employees e
JOIN departments d ON e.department_id = d.department_id;

-- 実体化ビュー
CREATE MATERIALIZED VIEW emp_dept_summary
BUILD IMMEDIATE
REFRESH COMPLETE ON DEMAND
AS
SELECT d.department_name, COUNT(*) as employee_count, AVG(salary) as avg_salary
FROM employees e
JOIN departments d ON e.department_id = d.department_id
GROUP BY d.department_name;
```

## Java Database Connectivity

### JDBCドライバーセットアップ

#### Maven依存関係
```xml
<dependency>
    <groupId>com.oracle.database.jdbc</groupId>
    <artifactId>ojdbc11</artifactId>
    <version>23.3.0.23.09</version>
</dependency>

<!-- コネクションプーリング用 -->
<dependency>
    <groupId>com.oracle.database.jdbc</groupId>
    <artifactId>ucp</artifactId>
    <version>23.3.0.23.09</version>
</dependency>
```

#### 基本的なJDBC接続
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
            System.out.println("Oracle Databaseに接続しました！");
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
```

### CRUD操作

#### データアクセスオブジェクト（DAO）パターン
```java
public class Employee {
    private int employeeId;
    private String firstName;
    private String lastName;
    private String email;
    private Date hireDate;
    private double salary;
    private int departmentId;
    
    // コンストラクタ、ゲッター、セッター
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
            throw new RuntimeException("従業員作成エラー", e);
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
            throw new RuntimeException("従業員取得エラー", e);
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
            throw new RuntimeException("従業員一覧取得エラー", e);
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
            throw new RuntimeException("従業員更新エラー", e);
        }
    }
    
    @Override
    public void deleteEmployee(int id) {
        String sql = "DELETE FROM employees WHERE employee_id = ?";
        
        try (PreparedStatement pstmt = connection.prepareStatement(sql)) {
            pstmt.setInt(1, id);
            pstmt.executeUpdate();
        } catch (SQLException e) {
            throw new RuntimeException("従業員削除エラー", e);
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

### ストアドプロシージャの操作
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
            throw new RuntimeException("ストアドプロシージャ呼び出しエラー", e);
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
            throw new RuntimeException("関数呼び出しエラー", e);
        }
    }
}
```

## 接続管理

### Oracle UCPを使用したコネクションプーリング
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
            
            // プール設定
            poolDataSource.setInitialPoolSize(5);
            poolDataSource.setMinPoolSize(5);
            poolDataSource.setMaxPoolSize(20);
            poolDataSource.setConnectionWaitTimeout(5);
            poolDataSource.setInactiveConnectionTimeout(300);
            
        } catch (SQLException e) {
            throw new RuntimeException("コネクションプール初期化エラー", e);
        }
    }
    
    public static Connection getConnection() throws SQLException {
        return poolDataSource.getConnection();
    }
}
```

### トランザクション管理
```java
public class TransactionExample {
    
    public void transferFunds(int fromAccount, int toAccount, double amount) {
        Connection conn = null;
        try {
            conn = ConnectionPoolManager.getConnection();
            conn.setAutoCommit(false); // トランザクション開始
            
            // 送金元口座から引き落とし
            String debitSql = "UPDATE accounts SET balance = balance - ? WHERE account_id = ?";
            try (PreparedStatement debitStmt = conn.prepareStatement(debitSql)) {
                debitStmt.setDouble(1, amount);
                debitStmt.setInt(2, fromAccount);
                debitStmt.executeUpdate();
            }
            
            // 送金先口座に入金
            String creditSql = "UPDATE accounts SET balance = balance + ? WHERE account_id = ?";
            try (PreparedStatement creditStmt = conn.prepareStatement(creditSql)) {
                creditStmt.setDouble(1, amount);
                creditStmt.setInt(2, toAccount);
                creditStmt.executeUpdate();
            }
            
            conn.commit(); // トランザクションコミット
            
        } catch (SQLException e) {
            if (conn != null) {
                try {
                    conn.rollback(); // エラー時ロールバック
                } catch (SQLException ex) {
                    ex.printStackTrace();
                }
            }
            throw new RuntimeException("資金振替エラー", e);
        } finally {
            if (conn != null) {
                try {
                    conn.setAutoCommit(true); // 自動コミットをリセット
                    conn.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
```

## ORMフレームワーク

### Hibernate設定
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
        
        <!-- コネクションプール -->
        <property name="hibernate.c3p0.min_size">5</property>
        <property name="hibernate.c3p0.max_size">20</property>
        <property name="hibernate.c3p0.timeout">300</property>
        <property name="hibernate.c3p0.max_statements">50</property>
        <property name="hibernate.c3p0.idle_test_period">3000</property>
    </session-factory>
</hibernate-configuration>
```

### Oracle固有機能を持つJPAエンティティ
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
    
    // コンストラクタ、ゲッター、セッター
    // ...
}
```

### Spring BootとOracle
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

## パフォーマンス最適化

### クエリ最適化
```sql
-- インデックスを効果的に使用
CREATE INDEX idx_emp_dept_salary ON employees(department_id, salary);

-- 必要に応じてヒントを使用
SELECT /*+ INDEX(e idx_emp_dept_salary) */ 
       e.employee_id, e.first_name, e.last_name
FROM employees e
WHERE department_id = 10 AND salary > 50000;

-- SQLインジェクション防止とパフォーマンス向上のためにバインド変数を使用
SELECT * FROM employees WHERE employee_id = :employee_id;
```

### Javaパフォーマンスのヒント
```java
// 複数挿入にはバッチ処理を使用
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
        throw new RuntimeException("バッチ挿入エラー", e);
    }
}

// 大きな結果セットには適切なフェッチサイズを使用
public List<Employee> getAllEmployeesOptimized() {
    List<Employee> employees = new ArrayList<>();
    String sql = "SELECT * FROM employees ORDER BY employee_id";
    
    try (Connection conn = ConnectionPoolManager.getConnection();
         PreparedStatement pstmt = conn.prepareStatement(sql)) {
        
        pstmt.setFetchSize(1000); // フェッチサイズの最適化
        ResultSet rs = pstmt.executeQuery();
        
        while (rs.next()) {
            employees.add(mapResultSetToEmployee(rs));
        }
        
    } catch (SQLException e) {
        throw new RuntimeException("従業員取得エラー", e);
    }
    return employees;
}
```

## セキュリティベストプラクティス

### 接続セキュリティ
```java
// 暗号化接続を使用
String url = "jdbc:oracle:thin:@(DESCRIPTION=(ADDRESS=(PROTOCOL=tcps)(HOST=localhost)(PORT=2484))(CONNECT_DATA=(SERVICE_NAME=XE)))" +
            "?oracle.net.ssl_client_authentication=false" +
            "&oracle.net.ssl_server_cert_dn=\"CN=localhost\"";

// セキュリティのための接続プロパティを使用
Properties props = new Properties();
props.setProperty("user", username);
props.setProperty("password", password);
props.setProperty("oracle.net.encryption_client", "REQUIRED");
props.setProperty("oracle.net.encryption_types_client", "AES256");
props.setProperty("oracle.net.crypto_checksum_client", "REQUIRED");
props.setProperty("oracle.net.crypto_checksum_types_client", "SHA256");

Connection conn = DriverManager.getConnection(url, props);
```

### SQLインジェクション防止
```java
// 常にパラメータ化クエリを使用
public Employee findEmployeeByEmail(String email) {
    String sql = "SELECT * FROM employees WHERE email = ?"; // 安全
    // String sql = "SELECT * FROM employees WHERE email = '" + email + "'"; // 危険！
    
    try (Connection conn = ConnectionPoolManager.getConnection();
         PreparedStatement pstmt = conn.prepareStatement(sql)) {
        
        pstmt.setString(1, email);
        ResultSet rs = pstmt.executeQuery();
        
        if (rs.next()) {
            return mapResultSetToEmployee(rs);
        }
        
    } catch (SQLException e) {
        throw new RuntimeException("従業員検索エラー", e);
    }
    return null;
}
```

## 監視とメンテナンス

### データベース監視クエリ
```sql
-- テーブルサイズの確認
SELECT table_name, 
       ROUND(((num_rows * avg_row_len) / 1024 / 1024), 2) as size_mb
FROM user_tables
ORDER BY size_mb DESC;

-- アクティブセッションの監視
SELECT username, osuser, machine, program, status, logon_time
FROM v$session
WHERE username IS NOT NULL
ORDER BY logon_time;

-- 表領域使用状況の確認
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

### アプリケーション監視
```java
// コネクションプール監視
public class ConnectionPoolMonitor {
    
    public void printPoolStatistics() {
        try {
            oracle.ucp.jdbc.PoolDataSource pds = (oracle.ucp.jdbc.PoolDataSource) poolDataSource;
            
            System.out.println("=== コネクションプール統計 ===");
            System.out.println("利用可能接続数: " + pds.getAvailableConnectionsCount());
            System.out.println("借用中接続数: " + pds.getBorrowedConnectionsCount());
            System.out.println("ピークプールサイズ: " + pds.getPeakPoolSize());
            System.out.println("接続プールサイズ: " + pds.getPoolSize());
            System.out.println("================================");
            
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}

// クエリパフォーマンス監視
public class QueryPerformanceMonitor {
    
    public <T> T executeWithTiming(String operationName, Supplier<T> operation) {
        long startTime = System.currentTimeMillis();
        
        try {
            T result = operation.get();
            long duration = System.currentTimeMillis() - startTime;
            
            System.out.println(operationName + " は " + duration + "ms で実行されました");
            
            if (duration > 1000) { // 遅いクエリをログ記録
                System.out.println("遅いクエリを検出: " + operationName);
            }
            
            return result;
            
        } catch (Exception e) {
            System.err.println(operationName + " でのエラー: " + e.getMessage());
            throw e;
        }
    }
}
```

## ベストプラクティスまとめ

### データベース設計
- 適切なデータ型と制約を使用
- 適切なインデックス戦略を実装
- 大きなテーブルにはパーティショニングを検討
- 主キーにはシーケンスを使用
- データを適切に正規化

### Java開発
- 常にコネクションプーリングを使用
- 適切な例外処理を実装
- SQLインジェクション防止のためにパラメータ化クエリを使用
- リソースを適切にクローズ（try-with-resourcesを使用）
- 複雑なアプリケーションにはORMフレームワークの使用を検討

### パフォーマンス
- 遅いクエリを監視・最適化
- バルクデータ操作にはバッチ操作を使用
- 適切なキャッシュ戦略を実装
- コネクションプールメトリクスを監視
- 適切なフェッチサイズを使用

### セキュリティ
- 本番環境では暗号化接続を使用
- 適切な認証と認可を実装
- 資格情報をハードコードしない
- 最小権限の原則を使用
- 定期的なセキュリティ監査

この包括的なガイドは、JavaアプリケーションでOracle Databaseを操作するための強固な基盤を提供します。最新の情報とベストプラクティスについては、常に公式Oracleドキュメントを参照してください。