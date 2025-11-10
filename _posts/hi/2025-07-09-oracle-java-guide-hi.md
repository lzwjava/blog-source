---
audio: false
generated: true
lang: hi
layout: post
title: जावा डेवलपर्स के लिए ओरेकल डेटाबेस गाइड
translated: true
type: note
---

## विषय सूची
1. [Oracle Database अवलोकन](#oracle-database-अवलोकन)
2. [इंस्टालेशन और सेटअप](#इंस्टालेशन-और-सेटअप)
3. [Oracle Database आर्किटेक्चर](#oracle-database-आर्किटेक्चर)
4. [SQL फंडामेंटल्स](#sql-फंडामेंटल्स)
5. [एडवांस्ड Oracle फीचर्स](#एडवांस्ड-oracle-फीचर्स)
6. [Java Database Connectivity](#java-database-connectivity)
7. [कनेक्शन मैनेजमेंट](#कनेक्शन-मैनेजमेंट)
8. [ORM फ्रेमवर्क्स](#orm-फ्रेमवर्क्स)
9. [परफॉर्मेंस ऑप्टिमाइजेशन](#परफॉर्मेंस-ऑप्टिमाइजेशन)
10. [सिक्योरिटी बेस्ट प्रैक्टिसेज](#सिक्योरिटी-बेस्ट-प्रैक्टिसेज)
11. [मॉनिटरिंग और मेंटेनेंस](#मॉनिटरिंग-और-मेंटेनेंस)

## Oracle Database अवलोकन

Oracle Database एक मल्टी-मॉडल डेटाबेस मैनेजमेंट सिस्टम है जिसे Oracle Corporation द्वारा बनाया गया है। यह एंटरप्राइज वातावरण में सबसे व्यापक रूप से उपयोग किए जाने वाले रिलेशनल डेटाबेस मैनेजमेंट सिस्टम (RDBMS) में से एक है।

### मुख्य विशेषताएं
- **ACID कंप्लायंस**: एटॉमिसिटी, कंसिस्टेंसी, आइसोलेशन और ड्यूरेबिलिटी के माध्यम से डेटा इंटिग्रिटी सुनिश्चित करता है
- **मल्टी-वर्जन कनकरेंसी कंट्रोल (MVCC)**: एक साथ कई यूजर्स को डेटा एक्सेस करने की अनुमति देता है
- **पार्टीशनिंग**: बड़ी टेबल्स को छोटे, प्रबंधनीय टुकड़ों में विभाजित करता है
- **एडवांस्ड सिक्योरिटी**: बिल्ट-इन एन्क्रिप्शन, ऑडिटिंग और एक्सेस कंट्रोल्स
- **हाई अवेलेबिलिटी**: रियल एप्लीकेशन क्लस्टर्स (RAC) और डेटा गार्ड
- **स्केलेबिलिटी**: विशाल डेटाबेस और उच्च ट्रांजैक्शन वॉल्यूम को सपोर्ट करता है

### Oracle Database एडिशन्स
- **एक्सप्रेस एडिशन (XE)**: डेवलपमेंट और छोटे डिप्लॉयमेंट्स के लिए फ्री, सीमित वर्जन
- **स्टैंडर्ड एडिशन**: कोर फीचर्स के साथ मिड-रेंज एडिशन
- **एंटरप्राइज एडिशन**: एडवांस्ड क्षमताओं के साथ फुल-फीचर्ड वर्जन
- **ऑटोनोमस डेटाबेस**: क्लाउड-आधारित, सेल्फ-मैनेजिंग डेटाबेस सर्विस

## इंस्टालेशन और सेटअप

### Oracle Database इंस्टालेशन

#### Oracle Database XE का उपयोग करना (डेवलपमेंट के लिए रिकमेंडेड)
1. Oracle की ऑफिशियल वेबसाइट से Oracle Database XE डाउनलोड करें
2. प्लेटफॉर्म-विशिष्ट निर्देशों का पालन करते हुए इंस्टॉल करें
3. डेटाबेस कॉन्फिगरेशन असिस्टेंट (DBCA) का उपयोग करके डेटाबेस कॉन्फिगर करें

#### Docker इंस्टालेशन (क्विक सेटअप)
```bash
# Oracle Database XE इमेज पुल करें
docker pull container-registry.oracle.com/database/express:21.3.0-xe

# Oracle Database XE कंटेनर रन करें
docker run --name oracle-xe \
  -p 1521:1521 \
  -p 5500:5500 \
  -e ORACLE_PWD=your_password \
  -e ORACLE_CHARACTERSET=AL32UTF8 \
  container-registry.oracle.com/database/express:21.3.0-xe
```

### क्लाइंट टूल्स
- **SQL*Plus**: कमांड-लाइन इंटरफेस
- **SQL डेवलपर**: GUI-आधारित डेवलपमेंट एनवायरनमेंट
- **Oracle एंटरप्राइज मैनेजर**: वेब-आधारित मैनेजमेंट कंसोल
- **DBeaver**: थर्ड-पार्टी डेटाबेस मैनेजमेंट टूल

## Oracle Database आर्किटेक्चर

### फिजिकल आर्किटेक्चर
- **डेटाबेस फाइल्स**: डेटा फाइल्स, कंट्रोल फाइल्स और रीडो लॉग फाइल्स
- **पैरामीटर फाइल्स**: कॉन्फिगरेशन सेटिंग्स (PFILE/SPFILE)
- **आर्काइव लॉग फाइल्स**: रिकवरी के लिए रीडो लॉग फाइल्स का बैकअप

### लॉजिकल आर्किटेक्चर
- **टेबलस्पेस**: लॉजिकल स्टोरेज यूनिट्स जिनमें एक या अधिक डेटा फाइल्स होती हैं
- **स्कीमास**: एक यूजर द्वारा स्वामित्व वाले डेटाबेस ऑब्जेक्ट्स का संग्रह
- **सेगमेंट्स**: डेटाबेस ऑब्जेक्ट्स के लिए आवंटित स्पेस
- **एक्सटेंट्स**: स्टोरेज के सन्निहित ब्लॉक्स
- **ब्लॉक्स**: स्टोरेज की सबसे छोटी इकाई

### मेमोरी आर्किटेक्चर
- **सिस्टम ग्लोबल एरिया (SGA)**: शेयर्ड मेमोरी एरिया
  - डेटाबेस बफर कैश
  - शेयर्ड पूल
  - रीडो लॉग बफर
  - लार्ज पूल
- **प्रोग्राम ग्लोबल एरिया (PGA)**: प्रत्येक प्रोसेस के लिए प्राइवेट मेमोरी

## SQL फंडामेंटल्स

### डेटा डेफिनिशन लैंग्वेज (DDL)

#### टेबल्स बनाना
```sql
-- एक टेबल बनाएं
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

-- कंस्ट्रेंट्स जोड़ें
ALTER TABLE employees 
ADD CONSTRAINT fk_dept_id 
FOREIGN KEY (department_id) 
REFERENCES departments(department_id);

-- इंडेक्स बनाएं
CREATE INDEX idx_emp_dept ON employees(department_id);
```

#### Oracle-विशिष्ट डेटा टाइप्स
- **NUMBER**: प्रिसिजन और स्केल के साथ न्यूमेरिक डेटा
- **VARCHAR2**: वेरिएबल-लेंथ कैरेक्टर स्ट्रिंग्स
- **CHAR**: फिक्स्ड-लेंथ कैरेक्टर स्ट्रिंग्स
- **DATE**: डेट और टाइम
- **TIMESTAMP**: फ्रैक्शनल सेकंड्स के साथ डेट और टाइम
- **CLOB**: कैरेक्टर लार्ज ऑब्जेक्ट
- **BLOB**: बाइनरी लार्ज ऑब्जेक्ट
- **XMLTYPE**: XML डेटा

### डेटा मैनिपुलेशन लैंग्वेज (DML)

#### एडवांस्ड क्वेरीज
```sql
-- विंडो फंक्शन्स
SELECT 
    employee_id,
    first_name,
    last_name,
    salary,
    RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) as salary_rank,
    LAG(salary, 1) OVER (ORDER BY hire_date) as prev_salary
FROM employees;

-- कॉमन टेबल एक्सप्रेशन्स (CTE)
WITH dept_avg_salary AS (
    SELECT department_id, AVG(salary) as avg_salary
    FROM employees
    GROUP BY department_id
)
SELECT e.*, d.avg_salary
FROM employees e
JOIN dept_avg_salary d ON e.department_id = d.department_id;

-- हायरार्किकल क्वेरीज
SELECT employee_id, first_name, last_name, manager_id, LEVEL
FROM employees
START WITH manager_id IS NULL
CONNECT BY PRIOR employee_id = manager_id
ORDER SIBLINGS BY last_name;
```

### PL/SQL प्रोग्रामिंग

#### बेसिक PL/SQL ब्लॉक
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

#### स्टोर्ड प्रोसीजर्स और फंक्शन्स
```sql
-- स्टोर्ड प्रोसीजर
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

-- फंक्शन
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

## एडवांस्ड Oracle फीचर्स

### पार्टीशनिंग
```sql
-- रेंज पार्टीशनिंग
CREATE TABLE sales (
    sale_id NUMBER,
    sale_date DATE,
    amount NUMBER
) PARTITION BY RANGE (sale_date) (
    PARTITION p2023 VALUES LESS THAN (DATE '2024-01-01'),
    PARTITION p2024 VALUES LESS THAN (DATE '2025-01-01'),
    PARTITION p_max VALUES LESS THAN (MAXVALUE)
);

-- हैश पार्टीशनिंग
CREATE TABLE customers (
    customer_id NUMBER,
    name VARCHAR2(100)
) PARTITION BY HASH (customer_id) PARTITIONS 4;
```

### सीक्वेंस
```sql
-- सीक्वेंस बनाएं
CREATE SEQUENCE emp_seq
    START WITH 1000
    INCREMENT BY 1
    MAXVALUE 9999999
    NOCACHE
    NOCYCLE;

-- सीक्वेंस का उपयोग करें
INSERT INTO employees (employee_id, first_name, last_name)
VALUES (emp_seq.NEXTVAL, 'John', 'Doe');
```

### व्यूज और मटीरियलाइज्ड व्यूज
```sql
-- व्यू बनाएं
CREATE VIEW employee_details AS
SELECT e.employee_id, e.first_name, e.last_name, 
       d.department_name, e.salary
FROM employees e
JOIN departments d ON e.department_id = d.department_id;

-- मटीरियलाइज्ड व्यू
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

### JDBC ड्राइवर सेटअप

#### Maven डिपेंडेंसीज
```xml
<dependency>
    <groupId>com.oracle.database.jdbc</groupId>
    <artifactId>ojdbc11</artifactId>
    <version>23.3.0.23.09</version>
</dependency>

<!-- कनेक्शन पूलिंग के लिए -->
<dependency>
    <groupId>com.oracle.database.jdbc</groupId>
    <artifactId>ucp</artifactId>
    <version>23.3.0.23.09</version>
</dependency>
```

#### बेसिक JDBC कनेक्शन
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

### CRUD ऑपरेशन्स

#### डेटा एक्सेस ऑब्जेक्ट (DAO) पैटर्न
```java
public class Employee {
    private int employeeId;
    private String firstName;
    private String lastName;
    private String email;
    private Date hireDate;
    private double salary;
    private int departmentId;
    
    // कंस्ट्रक्टर्स, गेटर्स और सेटर्स
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

### स्टोर्ड प्रोसीजर्स के साथ काम करना
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

## कनेक्शन मैनेजमेंट

### Oracle UCP के साथ कनेक्शन पूलिंग
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
            
            // पूल कॉन्फिगरेशन
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

### ट्रांजैक्शन मैनेजमेंट
```java
public class TransactionExample {
    
    public void transferFunds(int fromAccount, int toAccount, double amount) {
        Connection conn = null;
        try {
            conn = ConnectionPoolManager.getConnection();
            conn.setAutoCommit(false); // ट्रांजैक्शन शुरू करें
            
            // स्रोत अकाउंट से डेबिट करें
            String debitSql = "UPDATE accounts SET balance = balance - ? WHERE account_id = ?";
            try (PreparedStatement debitStmt = conn.prepareStatement(debitSql)) {
                debitStmt.setDouble(1, amount);
                debitStmt.setInt(2, fromAccount);
                debitStmt.executeUpdate();
            }
            
            // डेस्टिनेशन अकाउंट में क्रेडिट करें
            String creditSql = "UPDATE accounts SET balance = balance + ? WHERE account_id = ?";
            try (PreparedStatement creditStmt = conn.prepareStatement(creditSql)) {
                creditStmt.setDouble(1, amount);
                creditStmt.setInt(2, toAccount);
                creditStmt.executeUpdate();
            }
            
            conn.commit(); // ट्रांजैक्शन कमिट करें
            
        } catch (SQLException e) {
            if (conn != null) {
                try {
                    conn.rollback(); // एरर पर रोलबैक करें
                } catch (SQLException ex) {
                    ex.printStackTrace();
                }
            }
            throw new RuntimeException("Error in fund transfer", e);
        } finally {
            if (conn != null) {
                try {
                    conn.setAutoCommit(true); // ऑटो-कमिट रीसेट करें
                    conn.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
```

## ORM फ्रेमवर्क्स

### Hibernate कॉन्फिगरेशन
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
        
        <!-- कनेक्शन पूल -->
        <property name="hibernate.c3p0.min_size">5</property>
        <property name="hibernate.c3p0.max_size">20</property>
        <property name="hibernate.c3p0.timeout">300</property>
        <property name="hibernate.c3p0.max_statements">50</property>
        <property name="hibernate.c3p0.idle_test_period">3000</property>
    </session-factory>
</hibernate-configuration>
```

### Oracle-विशिष्ट फीचर्स के साथ JPA एंटिटी
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
    
    // कंस्ट्रक्टर्स, गेटर्स और सेटर्स
    // ...
}
```

### Oracle के साथ Spring Boot
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

## परफॉर्मेंस ऑप्टिमाइजेशन

### क्वेरी ऑप्टिमाइजेशन
```sql
-- इंडेक्सेज का प्रभावी ढंग से उपयोग करें
CREATE INDEX idx_emp_dept_salary ON employees(department_id, salary);

-- आवश्यकता पड़ने पर हिंट्स का उपयोग करें
SELECT /*+ INDEX(e idx_emp_dept_salary) */ 
       e.employee_id, e.first_name, e.last_name
FROM employees e
WHERE department_id = 10 AND salary > 50000;

-- SQL इंजेक्शन को रोकने और परफॉर्मेंस सुधारने के लिए बाइंड वेरिएबल्स का उपयोग करें
SELECT * FROM employees WHERE employee_id = :employee_id;
```

### Java परफॉर्मेंस टिप्स
```java
// मल्टीपल इंसर्ट्स के लिए बैच प्रोसेसिंग का उपयोग करें
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

// बड़े रिजल्ट सेट्स के लिए उचित फेच साइज का उपयोग करें
public List<Employee> getAllEmployeesOptimized() {
    List<Employee> employees = new ArrayList<>();
    String sql = "SELECT * FROM employees ORDER BY employee_id";
    
    try (Connection conn = ConnectionPoolManager.getConnection();
         PreparedStatement pstmt = conn.prepareStatement(sql)) {
        
        pstmt.setFetchSize(1000); // फेच साइज ऑप्टिमाइज करें
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

## सिक्योरिटी बेस्ट प्रैक्टिसेज

### कनेक्शन सिक्योरिटी
```java
// एन्क्रिप्टेड कनेक्शन्स का उपयोग करें
String url = "jdbc:oracle:thin:@(DESCRIPTION=(ADDRESS=(PROTOCOL=tcps)(HOST=localhost)(PORT=2484))(CONNECT_DATA=(SERVICE_NAME=XE)))" +
            "?oracle.net.ssl_client_authentication=false" +
            "&oracle.net.ssl_server_cert_dn=\"CN=localhost\"";

// सिक्योरिटी के लिए कनेक्शन प्रॉपर्टीज का उपयोग करें
Properties props = new Properties();
props.setProperty("user", username);
props.setProperty("password", password);
props.setProperty("oracle.net.encryption_client", "REQUIRED");
props.setProperty("oracle.net.encryption_types_client", "AES256");
props.setProperty("oracle.net.crypto_checksum_client", "REQUIRED");
props.setProperty("oracle.net.crypto_checksum_types_client", "SHA256");

Connection conn = DriverManager.getConnection(url, props);
```

### SQL इंजेक्शन प्रिवेंशन
```java
// हमेशा पैरामीटराइज्ड क्वेरीज का उपयोग करें
public Employee findEmployeeByEmail(String email) {
    String sql = "SELECT * FROM employees WHERE email = ?"; // सेफ
    // String sql = "SELECT * FROM employees WHERE email = '" + email + "'"; // डेंजरस!
    
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

## मॉनिटरिंग और मेंटेनेंस

### डेटाबेस मॉनिटरिंग क्वेरीज
```sql
-- टेबल साइजेज चेक करें
SELECT table_name, 
       ROUND(((num_rows * avg_row_len) / 1024 / 1024), 2) as size_mb
FROM user_tables
ORDER BY size_mb DESC;

-- एक्टिव सेशन्स मॉनिटर करें
SELECT username, osuser, machine, program, status, logon_time
FROM v$session
WHERE username IS NOT NULL
ORDER BY logon_time;

-- टेबलस्पेस यूसेज चेक करें
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

### एप्लीकेशन मॉनिटरिंग
```java
// कनेक्शन पूल मॉनिटरिंग
public class ConnectionPoolMonitor {
    
    public void printPoolStatistics() {
        try {
            oracle