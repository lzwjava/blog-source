---
audio: false
generated: true
lang: fr
layout: post
title: Guide Oracle Database pour les développeurs Java
translated: true
type: note
---

## Table des matières
1. [Vue d'ensemble d'Oracle Database](#oracle-database-overview)
2. [Installation et Configuration](#installation-and-setup)
3. [Architecture d'Oracle Database](#oracle-database-architecture)
4. [Fondamentaux SQL](#sql-fundamentals)
5. [Fonctionnalités avancées d'Oracle](#advanced-oracle-features)
6. [Connexion de base de données Java](#java-database-connectivity)
7. [Gestion des connexions](#connection-management)
8. [ORM Frameworks](#orm-frameworks)
9. [Optimisation des performances](#performance-optimization)
10. [Bonnes pratiques de sécurité](#security-best-practices)
11. [Surveillance et maintenance](#monitoring-and-maintenance)

## Vue d'ensemble d'Oracle Database

Oracle Database est un système de gestion de base de données multi-modèle produit par Oracle Corporation. C'est l'un des systèmes de gestion de base de données relationnelle (SGBDR) les plus largement utilisés dans les environnements d'entreprise.

### Fonctionnalités principales
- **Conformité ACID** : Garantit l'intégrité des données via Atomicité, Cohérence, Isolation et Durabilité
- **Contrôle de concurrence multi-version (MVCC)** : Permet à plusieurs utilisateurs d'accéder aux données simultanément
- **Partitionnement** : Divise les grandes tables en parties plus petites et gérables
- **Sécurité avancée** : Chiffrement intégré, audit et contrôles d'accès
- **Haute disponibilité** : Real Application Clusters (RAC) et Data Guard
- **Évolutivité** : Prend en charge les bases de données massives et les volumes de transactions élevés

### Éditions d'Oracle Database
- **Express Edition (XE)** : Version gratuite et limitée pour le développement et les petits déploiements
- **Standard Edition** : Édition milieu de gamme avec les fonctionnalités de base
- **Enterprise Edition** : Version complète avec des capacités avancées
- **Autonomous Database** : Service de base de données cloud et auto-géré

## Installation et Configuration

### Installation d'Oracle Database

#### Utilisation d'Oracle Database XE (Recommandé pour le développement)
1. Téléchargez Oracle Database XE depuis le site web officiel d'Oracle
2. Installez en suivant les instructions spécifiques à la plateforme
3. Configurez la base de données en utilisant Database Configuration Assistant (DBCA)

#### Installation Docker (Configuration rapide)
```bash
# Télécharge l'image Oracle Database XE
docker pull container-registry.oracle.com/database/express:21.3.0-xe

# Exécute le conteneur Oracle Database XE
docker run --name oracle-xe \
  -p 1521:1521 \
  -p 5500:5500 \
  -e ORACLE_PWD=your_password \
  -e ORACLE_CHARACTERSET=AL32UTF8 \
  container-registry.oracle.com/database/express:21.3.0-xe
```

### Outils clients
- **SQL*Plus** : Interface en ligne de commande
- **SQL Developer** : Environnement de développement graphique
- **Oracle Enterprise Manager** : Console de gestion basée sur le web
- **DBeaver** : Outil de gestion de base de données tiers

## Architecture d'Oracle Database

### Architecture physique
- **Fichiers de base de données** : Fichiers de données, fichiers de contrôle et fichiers de redo log
- **Fichiers de paramètres** : Paramètres de configuration (PFILE/SPFILE)
- **Fichiers de journaux d'archivage** : Sauvegarde des fichiers de redo log pour la récupération

### Architecture logique
- **Tablespaces** : Unités de stockage logique contenant un ou plusieurs fichiers de données
- **Schémas** : Collection d'objets de base de données détenus par un utilisateur
- **Segments** : Espace alloué pour les objets de base de données
- **Extensions** : Blocs de stockage contigus
- **Blocs** : Plus petite unité de stockage

### Architecture mémoire
- **System Global Area (SGA)** : Zone mémoire partagée
  - Database Buffer Cache
  - Shared Pool
  - Redo Log Buffer
  - Large Pool
- **Program Global Area (PGA)** : Mémoire privée pour chaque processus

## Fondamentaux SQL

### Langage de définition de données (DDL)

#### Création de tables
```sql
-- Créer une table
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

-- Ajouter des contraintes
ALTER TABLE employees 
ADD CONSTRAINT fk_dept_id 
FOREIGN KEY (department_id) 
REFERENCES departments(department_id);

-- Créer un index
CREATE INDEX idx_emp_dept ON employees(department_id);
```

#### Types de données spécifiques à Oracle
- **NUMBER** : Données numériques avec précision et échelle
- **VARCHAR2** : Chaînes de caractères de longueur variable
- **CHAR** : Chaînes de caractères de longueur fixe
- **DATE** : Date et heure
- **TIMESTAMP** : Date et heure avec fractions de secondes
- **CLOB** : Character Large Object
- **BLOB** : Binary Large Object
- **XMLTYPE** : Données XML

### Langage de manipulation de données (DML)

#### Requêtes avancées
```sql
-- Fonctions de fenêtrage
SELECT 
    employee_id,
    first_name,
    last_name,
    salary,
    RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) as salary_rank,
    LAG(salary, 1) OVER (ORDER BY hire_date) as prev_salary
FROM employees;

-- Expressions de table communes (CTE)
WITH dept_avg_salary AS (
    SELECT department_id, AVG(salary) as avg_salary
    FROM employees
    GROUP BY department_id
)
SELECT e.*, d.avg_salary
FROM employees e
JOIN dept_avg_salary d ON e.department_id = d.department_id;

-- Requêtes hiérarchiques
SELECT employee_id, first_name, last_name, manager_id, LEVEL
FROM employees
START WITH manager_id IS NULL
CONNECT BY PRIOR employee_id = manager_id
ORDER SIBLINGS BY last_name;
```

### Programmation PL/SQL

#### Bloc PL/SQL de base
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

#### Procédures stockées et fonctions
```sql
-- Procédure stockée
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

-- Fonction
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

## Fonctionnalités avancées d'Oracle

### Partitionnement
```sql
-- Partitionnement par plage
CREATE TABLE sales (
    sale_id NUMBER,
    sale_date DATE,
    amount NUMBER
) PARTITION BY RANGE (sale_date) (
    PARTITION p2023 VALUES LESS THAN (DATE '2024-01-01'),
    PARTITION p2024 VALUES LESS THAN (DATE '2025-01-01'),
    PARTITION p_max VALUES LESS THAN (MAXVALUE)
);

-- Partitionnement par hachage
CREATE TABLE customers (
    customer_id NUMBER,
    name VARCHAR2(100)
) PARTITION BY HASH (customer_id) PARTITIONS 4;
```

### Séquences
```sql
-- Créer une séquence
CREATE SEQUENCE emp_seq
    START WITH 1000
    INCREMENT BY 1
    MAXVALUE 9999999
    NOCACHE
    NOCYCLE;

-- Utiliser une séquence
INSERT INTO employees (employee_id, first_name, last_name)
VALUES (emp_seq.NEXTVAL, 'John', 'Doe');
```

### Vues et vues matérialisées
```sql
-- Créer une vue
CREATE VIEW employee_details AS
SELECT e.employee_id, e.first_name, e.last_name, 
       d.department_name, e.salary
FROM employees e
JOIN departments d ON e.department_id = d.department_id;

-- Vue matérialisée
CREATE MATERIALIZED VIEW emp_dept_summary
BUILD IMMEDIATE
REFRESH COMPLETE ON DEMAND
AS
SELECT d.department_name, COUNT(*) as employee_count, AVG(salary) as avg_salary
FROM employees e
JOIN departments d ON e.department_id = d.department_id
GROUP BY d.department_name;
```

## Connexion de base de données Java

### Configuration du pilote JDBC

#### Dépendances Maven
```xml
<dependency>
    <groupId>com.oracle.database.jdbc</groupId>
    <artifactId>ojdbc11</artifactId>
    <version>23.3.0.23.09</version>
</dependency>

<!-- Pour le pool de connexions -->
<dependency>
    <groupId>com.oracle.database.jdbc</groupId>
    <artifactId>ucp</artifactId>
    <version>23.3.0.23.09</version>
</dependency>
```

#### Connexion JDBC de base
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

### Opérations CRUD

#### Modèle Data Access Object (DAO)
```java
public class Employee {
    private int employeeId;
    private String firstName;
    private String lastName;
    private String email;
    private Date hireDate;
    private double salary;
    private int departmentId;
    
    // Constructeurs, getters et setters
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

### Utilisation des procédures stockées
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

## Gestion des connexions

### Pool de connexions avec Oracle UCP
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
            
            // Configuration du pool
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

### Gestion des transactions
```java
public class TransactionExample {
    
    public void transferFunds(int fromAccount, int toAccount, double amount) {
        Connection conn = null;
        try {
            conn = ConnectionPoolManager.getConnection();
            conn.setAutoCommit(false); // Début de la transaction
            
            // Débit du compte source
            String debitSql = "UPDATE accounts SET balance = balance - ? WHERE account_id = ?";
            try (PreparedStatement debitStmt = conn.prepareStatement(debitSql)) {
                debitStmt.setDouble(1, amount);
                debitStmt.setInt(2, fromAccount);
                debitStmt.executeUpdate();
            }
            
            // Crédit du compte destination
            String creditSql = "UPDATE accounts SET balance = balance + ? WHERE account_id = ?";
            try (PreparedStatement creditStmt = conn.prepareStatement(creditSql)) {
                creditStmt.setDouble(1, amount);
                creditStmt.setInt(2, toAccount);
                creditStmt.executeUpdate();
            }
            
            conn.commit(); // Validation de la transaction
            
        } catch (SQLException e) {
            if (conn != null) {
                try {
                    conn.rollback(); // Annulation en cas d'erreur
                } catch (SQLException ex) {
                    ex.printStackTrace();
                }
            }
            throw new RuntimeException("Error in fund transfer", e);
        } finally {
            if (conn != null) {
                try {
                    conn.setAutoCommit(true); // Réinitialisation de l'auto-commit
                    conn.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
```

## ORM Frameworks

### Configuration Hibernate
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
        
        <!-- Pool de connexions -->
        <property name="hibernate.c3p0.min_size">5</property>
        <property name="hibernate.c3p0.max_size">20</property>
        <property name="hibernate.c3p0.timeout">300</property>
        <property name="hibernate.c3p0.max_statements">50</property>
        <property name="hibernate.c3p0.idle_test_period">3000</property>
    </session-factory>
</hibernate-configuration>
```

### Entité JPA avec fonctionnalités spécifiques à Oracle
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
    
    // Constructeurs, getters et setters
    // ...
}
```

### Spring Boot avec Oracle
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

## Optimisation des performances

### Optimisation des requêtes
```sql
-- Utiliser efficacement les index
CREATE INDEX idx_emp_dept_salary ON employees(department_id, salary);

-- Utiliser des indications lorsque nécessaire
SELECT /*+ INDEX(e idx_emp_dept_salary) */ 
       e.employee_id, e.first_name, e.last_name
FROM employees e
WHERE department_id = 10 AND salary > 50000;

-- Utiliser des variables de liaison pour prévenir les injections SQL et améliorer les performances
SELECT * FROM employees WHERE employee_id = :employee_id;
```

### Conseils de performance Java
```java
// Utiliser le traitement par lots pour les insertions multiples
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

// Utiliser des tailles de récupération appropriées pour les grands ensembles de résultats
public List<Employee> getAllEmployeesOptimized() {
    List<Employee> employees = new ArrayList<>();
    String sql = "SELECT * FROM employees ORDER BY employee_id";
    
    try (Connection conn = ConnectionPoolManager.getConnection();
         PreparedStatement pstmt = conn.prepareStatement(sql)) {
        
        pstmt.setFetchSize(1000); // Optimiser la taille de récupération
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

## Bonnes pratiques de sécurité

### Sécurité des connexions
```java
// Utiliser des connexions chiffrées
String url = "jdbc:oracle:thin:@(DESCRIPTION=(ADDRESS=(PROTOCOL=tcps)(HOST=localhost)(PORT=2484))(CONNECT_DATA=(SERVICE_NAME=XE)))" +
            "?oracle.net.ssl_client_authentication=false" +
            "&oracle.net.ssl_server_cert_dn=\"CN=localhost\"";

// Utiliser les propriétés de connexion pour la sécurité
Properties props = new Properties();
props.setProperty("user", username);
props.setProperty("password", password);
props.setProperty("oracle.net.encryption_client", "REQUIRED");
props.setProperty("oracle.net.encryption_types_client", "AES256");
props.setProperty("oracle.net.crypto_checksum_client", "REQUIRED");
props.setProperty("oracle.net.crypto_checksum_types_client", "SHA256");

Connection conn = DriverManager.getConnection(url, props);
```

### Prévention des injections SQL
```java
// Toujours utiliser des requêtes paramétrées
public Employee findEmployeeByEmail(String email) {
    String sql = "SELECT * FROM employees WHERE email = ?"; // Sécurisé
    // String sql = "SELECT * FROM employees WHERE email = '" + email + "'"; // DANGEREUX!
    
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

## Surveillance et maintenance

### Requêtes de surveillance de base de données
```sql
-- Vérifier les tailles des tables
SELECT table_name, 
       ROUND(((num_rows * avg_row_len) / 1024 / 1024), 2) as size_mb
FROM user_tables
ORDER BY size_mb DESC;

-- Surveiller les sessions actives
SELECT username, osuser, machine, program, status, logon_time
FROM v$session
WHERE username IS NOT NULL
ORDER BY logon_time;

-- Vérifier l'utilisation des tablespaces
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

### Surveillance d'application
```java
// Surveillance du pool de connexions
public class ConnectionPoolMonitor {
    
    public void printPoolStatistics() {
        try {
            oracle.ucp.jdbc.PoolDataSource pds = (oracle.ucp.jdbc.PoolDataSource) poolDataSource;
            
            System.out.println("=== Connection Pool Statistics ===");
            System.out.println("Available Connections: " + pds.getAvailableConnectionsCount());
            System.out.println("Borrowed Connections: " + pds.getBorrowedConnectionsCount());
            System.out.println("Peak Pool Size: " + pds.getPeakPoolSize());
            System.out.println("Connection Pool Size: " + pds.getPoolSize());
            System.out.println("================================");
            
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}

// Surveillance des performances des requêtes
public class QueryPerformanceMonitor {
    
    public <T> T executeWithTiming(String operationName, Supplier<T> operation) {
        long startTime = System.currentTimeMillis();
        
        try {
            T result = operation.get();
            long duration = System.currentTimeMillis() - startTime;
            
            System.out.println(operationName + " executed in " + duration + "ms");
            
            if (duration > 1000) { // Journaliser les requêtes lentes
                System.out.println("SLOW QUERY DETECTED: " + operationName);
            }
            
            return result;
            
        } catch (Exception e) {
            System.err.println("Error in " + operationName + ": " + e.getMessage());
            throw e;
        }
    }
}
```

## Récapitulatif des bonnes pratiques

### Conception de base de données
- Utiliser des types de données et des contraintes appropriés
- Implémenter une stratégie d'indexation appropriée
- Envisager le partitionnement pour les grandes tables
- Utiliser des séquences pour les clés primaires
- Normaliser les données de manière appropriée

### Développement Java
- Toujours utiliser le pool de connexions
- Implémenter une gestion appropriée des exceptions
- Utiliser des requêtes paramétrées pour prévenir les injections SQL
- Fermer correctement les ressources (utiliser try-with-resources)
- Envisager d'utiliser des ORM frameworks pour les applications complexes

### Performance
- Surveiller et optimiser les requêtes lentes
- Utiliser des opérations par lots pour les opérations de données en masse
- Implémenter des stratégies de mise en cache appropriées
- Surveiller les métriques du pool de connexions
- Utiliser des tailles de récupération appropriées

### Sécurité
- Utiliser des connexions chiffrées en production
- Implémenter une authentification et une autorisation appropriées
- Ne jamais coder en dur les informations d'identification
- Utiliser le principe du moindre privilège
- Audits de sécurité réguliers

Ce guide complet fournit une base solide pour travailler avec Oracle Database dans les applications Java. N'oubliez pas de toujours vous référer à la documentation officielle d'Oracle pour les informations et les bonnes pratiques les plus récentes.