---
audio: false
generated: true
lang: de
layout: post
title: Oracle-Datenbank-Handbuch für Java-Entwickler
translated: true
type: note
---

## Inhaltsverzeichnis
1. [Oracle Database Überblick](#oracle-database-überblick)
2. [Installation und Einrichtung](#installation-und-einrichtung)
3. [Oracle Database Architektur](#oracle-database-architektur)
4. [SQL Grundlagen](#sql-grundlagen)
5. [Erweiterte Oracle-Funktionen](#erweiterte-oracle-funktionen)
6. [Java Database Connectivity](#java-database-connectivity)
7. [Verbindungsmanagement](#verbindungsmanagement)
8. [ORM-Frameworks](#orm-frameworks)
9. [Leistungsoptimierung](#leistungsoptimierung)
10. [Sicherheits-Best-Practices](#sicherheits-best-practices)
11. [Überwachung und Wartung](#überwachung-und-wartung)

## Oracle Database Überblick

Oracle Database ist ein Multi-Model-Datenbankmanagementsystem, das von der Oracle Corporation entwickelt wird. Es ist eines der am weitesten verbreiteten relationalen Datenbankmanagementsysteme (RDBMS) in Unternehmensumgebungen.

### Wichtige Funktionen
- **ACID-Compliance**: Gewährleistet Datenintegrität durch Atomarität, Konsistenz, Isolation und Dauerhaftigkeit
- **Multi-Version Concurrency Control (MVCC)**: Ermöglicht mehreren Benutzern gleichzeitigen Datenzugriff
- **Partitionierung**: Unterteilt große Tabellen in kleinere, handhabbare Teile
- **Erweiterte Sicherheit**: Integrierte Verschlüsselung, Überwachung und Zugriffskontrollen
- **Hohe Verfügbarkeit**: Real Application Clusters (RAC) und Data Guard
- **Skalierbarkeit**: Unterstützt massive Datenbanken und hohe Transaktionsvolumen

### Oracle Database Editionen
- **Express Edition (XE)**: Kostenlose, eingeschränkte Version für Entwicklung und kleine Bereitstellungen
- **Standard Edition**: Mittelklasse-Edition mit Kernfunktionen
- **Enterprise Edition**: Voll ausgestattete Version mit erweiterten Funktionen
- **Autonomous Database**: Cloud-basierter, selbstverwaltender Datenbankdienst

## Installation und Einrichtung

### Oracle Database Installation

#### Verwendung von Oracle Database XE (Empfohlen für Entwicklung)
1. Laden Sie Oracle Database XE von der offiziellen Oracle-Website herunter
2. Installieren Sie gemäß den plattformspezifischen Anweisungen
3. Konfigurieren Sie die Datenbank mit dem Database Configuration Assistant (DBCA)

#### Docker-Installation (Schnelle Einrichtung)
```bash
# Oracle Database XE-Image abrufen
docker pull container-registry.oracle.com/database/express:21.3.0-xe

# Oracle Database XE-Container ausführen
docker run --name oracle-xe \
  -p 1521:1521 \
  -p 5500:5500 \
  -e ORACLE_PWD=your_password \
  -e ORACLE_CHARACTERSET=AL32UTF8 \
  container-registry.oracle.com/database/express:21.3.0-xe
```

### Client-Tools
- **SQL*Plus**: Befehlszeilenschnittstelle
- **SQL Developer**: GUI-basierte Entwicklungsumgebung
- **Oracle Enterprise Manager**: Web-basierte Management-Konsole
- **DBeaver**: Drittanbieter-Datenbankverwaltungstool

## Oracle Database Architektur

### Physische Architektur
- **Datenbankdateien**: Datenfiles, Steuerdateien und Redo-Log-Dateien
- **Parameterdateien**: Konfigurationseinstellungen (PFILE/SPFILE)
- **Archiv-Log-Dateien**: Sicherung der Redo-Log-Dateien für die Wiederherstellung

### Logische Architektur
- **Tablespaces**: Logische Speichereinheiten, die eine oder mehrere Datenfiles enthalten
- **Schemata**: Sammlung von Datenbankobjekten, die einem Benutzer gehören
- **Segmente**: Für Datenbankobjekte reservierter Speicherplatz
- **Extents**: Zusammenhängende Blöcke von Speicherplatz
- **Blöcke**: Kleinste Speichereinheit

### Speicherarchitektur
- **System Global Area (SGA**: Gemeinsamer Speicherbereich
  - Database Buffer Cache
  - Shared Pool
  - Redo Log Buffer
  - Large Pool
- **Program Global Area (PGA)**: Privater Speicher für jeden Prozess

## SQL Grundlagen

### Data Definition Language (DDL)

#### Tabellen erstellen
```sql
-- Tabelle erstellen
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

-- Constraints hinzufügen
ALTER TABLE employees 
ADD CONSTRAINT fk_dept_id 
FOREIGN KEY (department_id) 
REFERENCES departments(department_id);

-- Index erstellen
CREATE INDEX idx_emp_dept ON employees(department_id);
```

#### Oracle-spezifische Datentypen
- **NUMBER**: Numerische Daten mit Präzision und Skalierung
- **VARCHAR2**: Zeichenketten variabler Länge
- **CHAR**: Zeichenketten fester Länge
- **DATE**: Datum und Uhrzeit
- **TIMESTAMP**: Datum und Uhrzeit mit Sekundenbruchteilen
- **CLOB**: Character Large Object
- **BLOB**: Binary Large Object
- **XMLTYPE**: XML-Daten

### Data Manipulation Language (DML)

#### Erweiterte Abfragen
```sql
-- Fensterfunktionen
SELECT 
    employee_id,
    first_name,
    last_name,
    salary,
    RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) as salary_rank,
    LAG(salary, 1) OVER (ORDER BY hire_date) as prev_salary
FROM employees;

-- Common Table Expressions (CTE)
WITH dept_avg_salary AS (
    SELECT department_id, AVG(salary) as avg_salary
    FROM employees
    GROUP BY department_id
)
SELECT e.*, d.avg_salary
FROM employees e
JOIN dept_avg_salary d ON e.department_id = d.department_id;

-- Hierarchische Abfragen
SELECT employee_id, first_name, last_name, manager_id, LEVEL
FROM employees
START WITH manager_id IS NULL
CONNECT BY PRIOR employee_id = manager_id
ORDER SIBLINGS BY last_name;
```

### PL/SQL Programmierung

#### Grundlegender PL/SQL-Block
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
        
        DBMS_OUTPUT.PUT_LINE('Abteilung: ' || v_department_name || 
                           ' hat ' || v_employee_count || ' Mitarbeiter');
    END IF;
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('Keine Daten gefunden');
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Fehler: ' || SQLERRM);
END;
/
```

#### Gespeicherte Prozeduren und Funktionen
```sql
-- Gespeicherte Prozedur
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
        RAISE_APPLICATION_ERROR(-20001, 'Mitarbeiter nicht gefunden');
END;
/

-- Funktion
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

## Erweiterte Oracle-Funktionen

### Partitionierung
```sql
-- Bereichspartitionierung
CREATE TABLE sales (
    sale_id NUMBER,
    sale_date DATE,
    amount NUMBER
) PARTITION BY RANGE (sale_date) (
    PARTITION p2023 VALUES LESS THAN (DATE '2024-01-01'),
    PARTITION p2024 VALUES LESS THAN (DATE '2025-01-01'),
    PARTITION p_max VALUES LESS THAN (MAXVALUE)
);

-- Hash-Partitionierung
CREATE TABLE customers (
    customer_id NUMBER,
    name VARCHAR2(100)
) PARTITION BY HASH (customer_id) PARTITIONS 4;
```

### Sequenzen
```sql
-- Sequenz erstellen
CREATE SEQUENCE emp_seq
    START WITH 1000
    INCREMENT BY 1
    MAXVALUE 9999999
    NOCACHE
    NOCYCLE;

-- Sequenz verwenden
INSERT INTO employees (employee_id, first_name, last_name)
VALUES (emp_seq.NEXTVAL, 'John', 'Doe');
```

### Views und Materialized Views
```sql
-- View erstellen
CREATE VIEW employee_details AS
SELECT e.employee_id, e.first_name, e.last_name, 
       d.department_name, e.salary
FROM employees e
JOIN departments d ON e.department_id = d.department_id;

-- Materialized View
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

### JDBC-Treibereinrichtung

#### Maven-Abhängigkeiten
```xml
<dependency>
    <groupId>com.oracle.database.jdbc</groupId>
    <artifactId>ojdbc11</artifactId>
    <version>23.3.0.23.09</version>
</dependency>

<!-- Für Verbindungspooling -->
<dependency>
    <groupId>com.oracle.database.jdbc</groupId>
    <artifactId>ucp</artifactId>
    <version>23.3.0.23.09</version>
</dependency>
```

#### Grundlegende JDBC-Verbindung
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
            System.out.println("Mit Oracle Database verbunden!");
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
```

### CRUD-Operationen

#### Data Access Object (DAO) Pattern
```java
public class Employee {
    private int employeeId;
    private String firstName;
    private String lastName;
    private String email;
    private Date hireDate;
    private double salary;
    private int departmentId;
    
    // Konstruktoren, Getter und Setter
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
            throw new RuntimeException("Fehler beim Erstellen des Mitarbeiters", e);
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
            throw new RuntimeException("Fehler beim Abrufen des Mitarbeiters", e);
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
            throw new RuntimeException("Fehler beim Abrufen der Mitarbeiter", e);
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
            throw new RuntimeException("Fehler beim Aktualisieren des Mitarbeiters", e);
        }
    }
    
    @Override
    public void deleteEmployee(int id) {
        String sql = "DELETE FROM employees WHERE employee_id = ?";
        
        try (PreparedStatement pstmt = connection.prepareStatement(sql)) {
            pstmt.setInt(1, id);
            pstmt.executeUpdate();
        } catch (SQLException e) {
            throw new RuntimeException("Fehler beim Löschen des Mitarbeiters", e);
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

### Arbeiten mit gespeicherten Prozeduren
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
            throw new RuntimeException("Fehler beim Aufruf der gespeicherten Prozedur", e);
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
            throw new RuntimeException("Fehler beim Aufruf der Funktion", e);
        }
    }
}
```

## Verbindungsmanagement

### Verbindungspooling mit Oracle UCP
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
            
            // Pool-Konfiguration
            poolDataSource.setInitialPoolSize(5);
            poolDataSource.setMinPoolSize(5);
            poolDataSource.setMaxPoolSize(20);
            poolDataSource.setConnectionWaitTimeout(5);
            poolDataSource.setInactiveConnectionTimeout(300);
            
        } catch (SQLException e) {
            throw new RuntimeException("Fehler beim Initialisieren des Verbindungspools", e);
        }
    }
    
    public static Connection getConnection() throws SQLException {
        return poolDataSource.getConnection();
    }
}
```

### Transaktionsmanagement
```java
public class TransactionExample {
    
    public void transferFunds(int fromAccount, int toAccount, double amount) {
        Connection conn = null;
        try {
            conn = ConnectionPoolManager.getConnection();
            conn.setAutoCommit(false); // Transaktion starten
            
            // Von Quellkonto abbuchen
            String debitSql = "UPDATE accounts SET balance = balance - ? WHERE account_id = ?";
            try (PreparedStatement debitStmt = conn.prepareStatement(debitSql)) {
                debitStmt.setDouble(1, amount);
                debitStmt.setInt(2, fromAccount);
                debitStmt.executeUpdate();
            }
            
            // Auf Zielkonto gutschreiben
            String creditSql = "UPDATE accounts SET balance = balance + ? WHERE account_id = ?";
            try (PreparedStatement creditStmt = conn.prepareStatement(creditSql)) {
                creditStmt.setDouble(1, amount);
                creditStmt.setInt(2, toAccount);
                creditStmt.executeUpdate();
            }
            
            conn.commit(); // Transaktion committen
            
        } catch (SQLException e) {
            if (conn != null) {
                try {
                    conn.rollback(); // Bei Fehler zurücksetzen
                } catch (SQLException ex) {
                    ex.printStackTrace();
                }
            }
            throw new RuntimeException("Fehler bei der Überweisung", e);
        } finally {
            if (conn != null) {
                try {
                    conn.setAutoCommit(true); // Auto-Commit zurücksetzen
                    conn.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
```

## ORM-Frameworks

### Hibernate-Konfiguration
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
        
        <!-- Verbindungspool -->
        <property name="hibernate.c3p0.min_size">5</property>
        <property name="hibernate.c3p0.max_size">20</property>
        <property name="hibernate.c3p0.timeout">300</property>
        <property name="hibernate.c3p0.max_statements">50</property>
        <property name="hibernate.c3p0.idle_test_period">3000</property>
    </session-factory>
</hibernate-configuration>
```

### JPA-Entity mit Oracle-spezifischen Funktionen
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
    
    // Konstruktoren, Getter und Setter
    // ...
}
```

### Spring Boot mit Oracle
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

## Leistungsoptimierung

### Abfrageoptimierung
```sql
-- Verwenden Sie Indizes effektiv
CREATE INDEX idx_emp_dept_salary ON employees(department_id, salary);

-- Verwenden Sie Hints bei Bedarf
SELECT /*+ INDEX(e idx_emp_dept_salary) */ 
       e.employee_id, e.first_name, e.last_name
FROM employees e
WHERE department_id = 10 AND salary > 50000;

-- Verwenden Sie Bind-Variablen zur Verhinderung von SQL-Injection und zur Verbesserung der Leistung
SELECT * FROM employees WHERE employee_id = :employee_id;
```

### Java-Leistungstipps
```java
// Verwenden Sie Batch-Verarbeitung für mehrere Einfügungen
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
        throw new RuntimeException("Fehler beim Batch-Einfügen", e);
    }
}

// Verwenden Sie geeignete Fetch-Größen für große Result Sets
public List<Employee> getAllEmployeesOptimized() {
    List<Employee> employees = new ArrayList<>();
    String sql = "SELECT * FROM employees ORDER BY employee_id";
    
    try (Connection conn = ConnectionPoolManager.getConnection();
         PreparedStatement pstmt = conn.prepareStatement(sql)) {
        
        pstmt.setFetchSize(1000); // Fetch-Größe optimieren
        ResultSet rs = pstmt.executeQuery();
        
        while (rs.next()) {
            employees.add(mapResultSetToEmployee(rs));
        }
        
    } catch (SQLException e) {
        throw new RuntimeException("Fehler beim Abrufen der Mitarbeiter", e);
    }
    return employees;
}
```

## Sicherheits-Best-Practices

### Verbindungssicherheit
```java
// Verwenden Sie verschlüsselte Verbindungen
String url = "jdbc:oracle:thin:@(DESCRIPTION=(ADDRESS=(PROTOCOL=tcps)(HOST=localhost)(PORT=2484))(CONNECT_DATA=(SERVICE_NAME=XE)))" +
            "?oracle.net.ssl_client_authentication=false" +
            "&oracle.net.ssl_server_cert_dn=\"CN=localhost\"";

// Verwenden Sie Verbindungseigenschaften für Sicherheit
Properties props = new Properties();
props.setProperty("user", username);
props.setProperty("password", password);
props.setProperty("oracle.net.encryption_client", "REQUIRED");
props.setProperty("oracle.net.encryption_types_client", "AES256");
props.setProperty("oracle.net.crypto_checksum_client", "REQUIRED");
props.setProperty("oracle.net.crypto_checksum_types_client", "SHA256");

Connection conn = DriverManager.getConnection(url, props);
```

### SQL-Injection-Prävention
```java
// Verwenden Sie immer parametrisierte Abfragen
public Employee findEmployeeByEmail(String email) {
    String sql = "SELECT * FROM employees WHERE email = ?"; // Sicher
    // String sql = "SELECT * FROM employees WHERE email = '" + email + "'"; // GEFÄHRLICH!
    
    try (Connection conn = ConnectionPoolManager.getConnection();
         PreparedStatement pstmt = conn.prepareStatement(sql)) {
        
        pstmt.setString(1, email);
        ResultSet rs = pstmt.executeQuery();
        
        if (rs.next()) {
            return mapResultSetToEmployee(rs);
        }
        
    } catch (SQLException e) {
        throw new RuntimeException("Fehler beim Suchen des Mitarbeiters", e);
    }
    return null;
}
```

## Überwachung und Wartung

### Datenbank-Überwachungsabfragen
```sql
-- Tabellengrößen überprüfen
SELECT table_name, 
       ROUND(((num_rows * avg_row_len) / 1024 / 1024), 2) as size_mb
FROM user_tables
ORDER BY size_mb DESC;

-- Aktive Sitzungen überwachen
SELECT username, osuser, machine, program, status, logon_time
FROM v$session
WHERE username IS NOT NULL
ORDER BY logon_time;

-- Tablespace-Nutzung überprüfen
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

### Anwendungsüberwachung
```java
// Verbindungspool-Überwachung
public class ConnectionPoolMonitor {
    
    public void printPoolStatistics() {
        try {
            oracle.ucp.jdbc.PoolDataSource pds = (oracle.ucp.jdbc.PoolDataSource) poolDataSource;
            
            System.out.println("=== Verbindungspool-Statistiken ===");
            System.out.println("Verfügbare Verbindungen: " + pds.getAvailableConnectionsCount());
            System.out.println("Ausgeliehene Verbindungen: " + pds.getBorrowedConnectionsCount());
            System.out.println("Maximale Pool-Größe: " + pds.getPeakPoolSize());
            System.out.println("Aktuelle Pool-Größe: " + pds.getPoolSize());
            System.out.println("================================");
            
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}

// Abfrageleistungsüberwachung
public class QueryPerformanceMonitor {
    
    public <T> T executeWithTiming(String operationName, Supplier<T> operation) {
        long startTime = System.currentTimeMillis();
        
        try {
            T result = operation.get();
            long duration = System.currentTimeMillis() - startTime;
            
            System.out.println(operationName + " ausgeführt in " + duration + "ms");
            
            if (duration > 1000) { // Langsame Abfragen protokollieren
                System.out.println("LANGSAME ABFRAGE ERKANNT: " + operationName);
            }
            
            return result;
            
        } catch (Exception e) {
            System.err.println("Fehler in " + operationName + ": " + e.getMessage());
            throw e;
        }
    }
}
```

## Best Practices Zusammenfassung

### Datenbankdesign
- Verwenden Sie geeignete Datentypen und Constraints
- Implementieren Sie eine geeignete Indexierungsstrategie
- Erwägen Sie Partitionierung für große Tabellen
- Verwenden Sie Sequenzen für Primärschlüssel
- Normalisieren Sie Daten angemessen

### Java-Entwicklung
- Verwenden Sie immer Verbindungspooling
- Implementieren Sie eine ordnungsgemäße Ausnahmebehandlung
- Verwenden Sie parametrisierte Abfragen zur Verhinderung von SQL-Injection
- Schließen Sie Ressourcen ordnungsgemäß (verwenden Sie try-with-resources)
- Erwägen Sie die Verwendung von ORM-Frameworks für komplexe Anwendungen

### Leistung
- Überwachen und optimieren Sie langsame Abfragen
- Verwenden Sie Batch-Operationen für Massendatenoperationen
- Implementieren Sie geeignete Caching-Strategien
- Überwachen Sie Verbindungspool-Metriken
- Verwenden Sie geeignete Fetch-Größen

### Sicherheit
- Verwenden Sie verschlüsselte Verbindungen in der Produktion
- Implementieren Sie geeignete Authentifizierung und Autorisierung
- Speichern Sie niemals Anmeldedaten im Code
- Verwenden Sie das Prinzip der geringsten Rechte
- Regelmäßige Sicherheitsaudits

Dieser umfassende Leitfaden bietet eine solide Grundlage für die Arbeit mit Oracle Database in Java-Anwendungen. Denken Sie daran, für die aktuellsten Informationen und Best Practices immer auf die offizielle Oracle-Dokumentation zu verweisen.