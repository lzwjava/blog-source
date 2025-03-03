---
audio: false
generated: true
lang: hi
layout: post
title: Spring Data REST Module का अनुवाद
translated: true
---

**spring-data-rest-core** का उपयोग करने के लिए, आप Spring Data REST module का उपयोग करke aap apne Spring Data repositories ko RESTful endpoints ke roop mein apne application mein expose kar sakte hain. Niche ek poore, step-by-step guide hai jo aapko start karne mein madad karega:

---

### 1. Spring Data REST Dependency Add Karein
Spring Data REST ka use karne ke liye, aapko apne project mein uska dependency include karna padta hai. Agar aap **Spring Boot** ka use kar rahe hain (ek common scenario), to aap apne build file mein niche diye gaye dependency ko add karein:

- **Maven**:
  ```xml
  <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-data-rest</artifactId>
  </dependency>
  ```

- **Gradle**:
  ```gradle
  implementation 'org.springframework.boot:spring-boot-starter-data-rest'
  ```

Yeh starter `spring-data-rest-core` ke saath saath aur zaroori components ko lekar aati hai. Non-Spring Boot projects ke liye, aap `spring-data-rest-core` ko directly include kar sakte hain, lekin Spring Boot starter simplicity ke liye recommend kiya jaata hai.

---

### 2. Apne Entities ko Define Karein
Aap apne domain model ko define karke entity classes banayein, ek persistence technology jaise JPA (Java Persistence API) ka use karke. Jaise:

```java
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.GeneratedValue;

@Entity
public class User {
    @Id
    @GeneratedValue
    private Long id;
    private String name;

    // Constructors
    public User() {}
    public User(String name) {
        this.name = name;
    }

    // Getters and Setters
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
}
```

Yeh `User` entity aapke database mein ek simple table ko represent karta hai, ek `id` aur `name` ke saath.

---

### 3. Repository Interfaces Banayein
Apne entity ke liye ek repository interface define karein, ek Spring Data ka repository interface extend karke, jaise `JpaRepository`. Jaise:

```java
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserRepository extends JpaRepository<User, Long> {
}
```

`JpaRepository` ko extend karke, aapko basic CRUD (Create, Read, Update, Delete) operations free mein milte hain. Spring Data REST automatically yeh repository ko ek RESTful endpoint ke roop mein expose karega.

---

### 4. Apne Application ko Run Karein
Dependency add karke aur apne entities aur repositories define karke, aap apne Spring Boot application ko start karein. Spring Data REST automatically aapke repository ke basis par REST endpoints generate karega. Upar diye gaye `UserRepository` ke liye, aap access kar sakte hain:

- **GET /users**: Sabhi users ko retrieve karein.
- **GET /users/{id}**: Ek specific user ko ID ke basis par retrieve karein.
- **POST /users**: Ek naya user create karein (ek JSON payload ke saath, jaise `{"name": "Alice"}`).
- **PUT /users/{id}**: Ek existing user ko update karein.
- **DELETE /users/{id}**: Ek user ko delete karein.

Jaise agar aapka application `localhost:8080` par run ho raha hai, to aap ek tool jaise `curl` ya browser ka use karke test kar sakte hain:

```bash
curl http://localhost:8080/users
```

Response mein HATEOAS links shamil honge, jo clients ko related resources ko dynamically navigate karne mein madad karega.

---

### 5. (Optional) REST Endpoints ko Customize Karein
Aap annotations ya configuration ka use karke apne repositories ko expose karne tarah ko customize kar sakte hain:

- **Endpoint Path ko Badalayein**:
  `@RepositoryRestResource` annotation ka use karke ek custom path specify karein:
  ```java
  import org.springframework.data.rest.core.annotation.RepositoryRestResource;

  @RepositoryRestResource(path = "people")
  public interface UserRepository extends JpaRepository<User, Long> {
  }
  ```
  Ab, endpoint `/people` hoga `/users` ke bade.

- **Global Settings ko Configure Karein**:
  Base path ya aur settings ko customize karke `RepositoryRestConfigurer` implement karein:
  ```java
  import org.springframework.data.rest.webmvc.config.RepositoryRestConfigurer;
  import org.springframework.context.annotation.Configuration;
  import org.springframework.data.rest.core.config.RepositoryRestConfiguration;

  @Configuration
  public class RestConfig implements RepositoryRestConfigurer {
      @Override
      public void configureRepositoryRestConfiguration(RepositoryRestConfiguration config) {
          config.setBasePath("/api"); // Sabhi endpoints `/api` se start honege
      }
  }
  ```
  Isse, aapke users ko `/api/users` par access kiya ja sakta hai.

---

### Spring Data REST ke Key Features
- **HATEOAS Support**: Responses mein related resources ke hypermedia links shamil hote hain.
- **Pagination and Sorting**: Query parameters jaise `?page=0&size=10&sort=name,asc` ka use karke results ko paginate aur sort karein.
- **Filtering**: Apne repository mein custom query methods add karein (jaise `findByName(String name)`) additional endpoints ko expose karne ke liye.

---

### Summary
`spring-data-rest-core` ka use karne ke liye:
1. Spring Data REST dependency ko include karein (jaise `spring-boot-starter-data-rest` Spring Boot ke liye).
2. Appropriate annotations ke saath entities ko define karein (jaise `@Entity` JPA ke liye).
3. Spring Data interfaces (jaise `JpaRepository`) extend karke repository interfaces banayein.
4. Apne application ko run karein automatically generated REST endpoints ko access karne ke liye.
5. Agar zaroori ho, endpoint paths ya behavior ko customize karein.

Yeh approach aapko minimal code ke saath ek RESTful API ko quickly build karne mein madad karta hai, Spring Data REST ke core functionality ko leverage karke.