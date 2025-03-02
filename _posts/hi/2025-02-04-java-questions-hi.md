---
audio: false
generated: true
lang: hi
layout: post
title: 'Java Backend Engineer Interview Questions का अनुवाद:


  "Java Backend Engineer Interview Questions" का अनुवाद:


  "जावा बैकएंड इंजीनियर इंटरव्यू प्रश्न"'
translated: true
---

### Java Core

1. Java में OOP के चार मुख्य सिद्धांत क्या हैं? उत्तर: चार मुख्य सिद्धांत हैं Encapsulation, Inheritance, Polymorphism, और Abstraction. Encapsulation एक object की internal state को छुपाता hai, Inheritance class inheritance ko allow karta hai, Polymorphism method overriding aur overloading ko enable karta hai, aur Abstraction background details ko include karne ke bina essential features ko represent karne ka ek tarika provide karta hai.

2. Generics in Java ka uddeshya kya hai aur ek example bataye? उत्तर: Generics types ko parameterize karne ki anumati deta hai, jo code reusability aur type safety ko enable karta hai. For example, `ArrayList<T>` ek type parameter `T` ka use karta hai elements ko store karne ke liye.

3. Java mein ek thread kaise banaya jaata hai, aur uska lifecycle kya hai? उत्तर: Ek thread ko `Thread` extend karke ya `Runnable` implement karke banaya ja sakta hai. Lifecycle mein New, Runnable, Running, Blocked, Waiting, Timed Waiting, aur Terminated states shamil hain.

4. JVM ke dwara manage kiya gaya different memory areas kya hain? उत्तर: JVM Heap, Stack, Method Area, Native Method Stack, aur Program Counter Register ko manage karta hai. Heap objects ko store karta hai, aur har thread apne Stack ko local variables aur method calls ke liye rakhta hai.

5. Java mein checked aur unchecked exceptions mein kya antar hai? उत्तर: Checked exceptions ko declare ya catch karna padta hai, jabki unchecked exceptions compile time par check nahi kiya jaata hai. Examples mein `IOException` checked aur `NullPointerException` unchecked hai.

6. Java mein serialization kaise implement kiya jaata hai, aur iska kya mahatva hai? उत्तर: Serialization ko implement karne ke liye `Serializable` interface ko implement kiya jaata hai. Yeh object ki state ko save aur restore karne ke liye important hai, jo networking aur persistence ke liye useful hai.

7. Java Collections Framework mein ArrayList aur LinkedList ka compare karein. उत्तर: `ArrayList` fast access aur traversal ke liye suitable hai, jabki `LinkedList` insertions aur deletions ke liye better hai. `ArrayList` contiguous memory ka use karta hai, jabki `LinkedList` nodes aur pointers ka use karta hai.

8. Java mein lambda expressions kya hain, aur ye functional interfaces se kaise relate hote hain? उत्तर: Lambda expressions ek concise tarika hai ek method interface (functional interfaces) ko represent karne ke liye. Yeh functional interfaces jaise `Runnable` ya `Comparator` ko implement karne ke liye use hote hain.

9. Java Stream API mein available key operations kya hain? उत्तर: Stream API mein intermediate operations (jaise `map`, `filter`) aur terminal operations (jaise `forEach`, `collect`) shamil hain. Yeh collections par functional-style operations ko allow karte hain.

10. Java mein reflection kaise use kiya jaata hai classes ko runtime par inspect karne ke liye? उत्तर: Reflection classes, methods, aur fields ko inspect karne ke liye `Class.forName()`, `getMethods()`, aur `getField()` ka use karta hai. Yeh dynamic behavior aur frameworks ke liye use hota hai.

---

### Spring Ecosystem

1. Spring IoC container kya hai aur ye kaise kaam karta hai? उत्तर: IoC container beans aur unki lifecycles ko manage karta hai. Yeh dependency injection ka use karta hai dependencies ko manage karne ke liye, jo coupling ko kam karta hai.

2. Spring Boot auto-configuration kya hai? उत्तर: Auto-configuration classpath dependencies ke basis par beans ko automatically configure karta hai, setup ko simplify karte hue aur boilerplate code ko kam karte hue.

3. Spring Data JPA data access ko kaise simplify karta hai? उत्तर: Spring Data JPA repositories ke sath CRUD operations aur query methods provide karta hai, database interactions ko abstract karte hue.

4. Spring Security kaise use hota hai? उत्तर: Spring Security authentication aur authorization mechanisms provide karta hai, applications ko unauthorized access se secure karte hue.

5. Spring MVC web applications mein kaunsi role nibhata hai? उत्तर: Spring MVC web requests ko handle karta hai, URLs ko controllers se map karte hue aur web responses ke liye views aur models ko manage karte hue.

6. Spring Cloud kya hai aur uske main components kya hain? उत्तर: Spring Cloud cloud-native applications ke liye tools provide karta hai, jaise service discovery (Eureka), circuit breakers (Hystrix), aur API gateways.

7. Spring AOP application functionality ko kaise enhance karta hai? उत्तर: AOP cross-cutting concerns jaise logging aur transaction management ko business logic se separate karne ke liye aspects aur advice ka use karta hai.

8. Spring Boot Actuator kya hai aur ye kaise kaam karta hai? उत्तर: Actuator endpoints provide karta hai monitoring aur applications ko manage karne ke liye, jaise health checks, metrics, aur environment information.

9. Spring profiles ka use kya hai? उत्तर: Profiles alag-alag environments (jaise development, production) ke liye alag configurations provide karte hain, environment-specific settings ko enable karte hue.

10. Spring Boot starters dependency management ko kaise simplify karte hain? उत्तर: Starters ek specific functionality ke liye sabhi necessary dependencies ko include karte hain, dependencies ko manually manage karne ki zarurat ko kam karte hue.

---

### Microservices Architecture

1. Service discovery kya hai aur ye kaise important hai? उत्तर: Service discovery services ko locate karne ki process ko automate karta hai, dynamic environments aur scaling ke liye essential hai.

2. Microservices mein API gateway ka role kya hai? उत्तर: API gateway ek single entry point ka role nibhata hai, requests ko appropriate services tak route karte hue, security aur protocol translation handle karte hue.

3. Circuit Breaker pattern kya hai aur ye kaise help karta hai? उत्तर: Circuit Breaker cascading failures ko rokta hai failing services ko interrupt karke, unhe recover karne ki anumati deta hai.

4. RESTful API design principles kya hain? उत्तर: REST principles mein statelessness, client-server architecture, cacheability, aur uniform interface shamil hain, scalable aur maintainable APIs ko ensure karte hue.

5. GraphQL kya hai aur ye REST se kaise alag hai? उत्तर: GraphQL ek query language hai APIs ke liye, clients ko exactly jo unhe chahiye wo request karne ki anumati deta hai, over-fetching aur under-fetching ko kam karte hue.

6. Microservices mein API versioning kaise handle kiya jaata hai? उत्तर: Versioning URL paths, headers, ya query parameters ke through kiya ja sakta hai, backward compatibility aur smooth transitions ko ensure karte hue.

7. Microservices mein Saga pattern kya hai? उत्तर: Saga distributed transactions ko services ke beech manage karta hai, ek series of local transactions aur compensations ke sath failures ke liye.

8. Microservices mein health checks kya hain aur ye kaise important hain? उत्तर: Health checks services ke availability aur performance ko verify karte hain, monitoring aur service meshes ko manage karne ke liye crucial hain.

9. Microservices mein contract-first development kya hai? उत्तर: Contract-first development APIs ko define karte hue implementation se pehle, compatibility aur services ke beech decoupling ko ensure karte hue.

10. Microservices mein rate limiting kaise implement kiya jaata hai? उत्तर: Rate limiting middleware ya APIs jaise Spring Cloud Gateway ka use karke implement kiya ja sakta hai, request rates ko control karke abuse ko rokne ke liye.

---

### Databases and Caching

1. SQL joins kya hain aur ye kab use hote hain? उत्तर: SQL joins do ya zyada tables ke records ko ek related column ke basis par combine karte hain, related tables ke beech data ko retrieve karne ke liye use hote hain.

2. Database transactions mein ACID properties kya hain? उत्तर: ACID Atomicity, Consistency, Isolation, aur Durability ko denote karta hai, reliable transaction processing ko ensure karte hue.

3. Redis kya hai aur ye caching mein kaise use hota hai? उत्तर: Redis ek in-memory key-value store hai jo caching ke liye use hota hai, frequently used data ko fast access provide karte hue.

4. Redis aur Memcached ko caching ke liye compare karein. उत्तर: Redis data structures aur persistence ko support karta hai, jabki Memcached basic caching ke liye simpler aur faster hai.

5. Databases mein sharding kya hai aur ye kaise use hota hai? उत्तर: Sharding data ko horizontally multiple databases ke beech partition karte hue, large systems mein scalability aur performance ke liye use hota hai.

6. Hibernate database interactions ko kaise simplify karta hai? उत्तर: Hibernate ek ORM framework hai jo Java classes ko database tables se map karta hai, CRUD operations ko simplify karte hue.

7. JDBC connection pooling kya hai? उत्तर: Connection pooling database connections ko reuse karta hai, performance ko improve karte hue connection creation overhead ko kam karte hue.

8. Time-series database kya hai aur ye kab use hota hai? उत्तर: Time-series databases jaise InfluxDB time-stamped data ko store karte hain, monitoring, IoT, aur sensor data ke liye ideal hain.

9. Databases mein transaction isolation levels kya hain? उत्तर: Isolation levels (Read Uncommitted, Read Committed, Repeatable Read, Serializable) transactions ke beech interactions ko define karte hain.

10. Databases mein indexing strategies ko optimize kaise kiya jaata hai? उत्तर: Query patterns ke basis par indexes ko choose karein, over-indexing se bachen, aur multi-column queries ke liye composite indexes ka use karein.

---

### Concurrency and Multithreading

1. Java mein deadlock kya hai aur ye kaise avoid kiya ja sakta hai? उत्तर: Deadlock tab hota hai jab threads indefinitely ek dusre ke liye wait karte hain. Yeh circular waits ko avoid karke aur timeouts ka use karke avoid kiya ja sakta hai.

2. Java mein Executor Framework kya hai? उत्तर: Executor Framework thread execution ko manage karta hai, thread pools aur task scheduling provide karte hue.

3. Callable aur Runnable mein kya antar hai? उत्तर: Callable result return aur exceptions throw kar sakta hai, jabki Runnable nahi, isliye Callable tasks returning results ke liye zyada flexible hai.

4. Java Memory Model kya hai? उत्तर: Java Memory Model threads ko variables access karne ka tarika define karta hai, visibility aur operations ke ordering ko ensure karte hue across processors.

5. Java mein volatile keyword kya hai aur ye kab use kiya jaana chahiye? उत्तर: Volatile ensure karta hai ki variable changes sab threads ke liye visible hain, multi-threaded environments mein caching issues ko prevent karne ke liye use hota hai.

6. Multi-threaded applications mein race conditions ko kaise prevent kiya jaata hai? उत्तर: Synchronization, locks, ya atomic operations ka use karke shared resources ke liye exclusive access ensure kiya jaata hai.

7. Read-write lock ka concept kya hai? उत्तर: Read-write locks multiple readers ya ek writer ko allow karte hain, concurrency ko improve karte hue shared access ko allow karte hue.

8. CountDownLatch kya hai aur ye kaise use hota hai? उत्तर: CountDownLatch ek thread ko ek set of threads ko complete hone tak wait karne ki anumati deta hai, thread execution ko coordinate karne ke liye use hota hai.

9. Java mein lock striping kya hai? उत्तर: Lock striping ek lock ko multiple parts (stripes) mein divide karta hai, different parts ke liye concurrent access ko allow karte hue, contention ko kam karte hue.

10. Java mein thread interruption kaise handle kiya jaata hai? उत्तर: Threads interrupted status check karte hain aur `InterruptedException` throw karte hain, graceful termination ko allow karte hue.

---

### Web Servers and Load Balancing

1. Nginx kaise commonly use hota hai? उत्तर: Nginx ko web server, reverse proxy, load balancer, aur HTTP cache ke roop mein use kiya jaata hai, high performance aur scalability ke liye jaana jaata hai.

2. Load balancer aur reverse proxy mein kya antar hai? उत्तर: Load balancer traffic ko servers ke beech distribute karta hai, jabki reverse proxy requests ko backend servers tak forward karta hai, often caching aur security provide karte hue.

3. HAProxy kya hai aur ye kaise use hota hai? उत्तर: HAProxy ek high availability load balancer aur proxy server hai, network connections ko manage aur distribute karne ke liye use hota hai.

4. Web server par SSL/TLS kaise configure kiya jaata hai? उत्तर: SSL/TLS ko configure karne ke liye certificates obtain karte hain aur HTTPS listeners setup karte hain, data in transit ko encrypt karte hue.

5. Server-side caching kya hai aur ye kaise implement kiya jaata hai? उत्तर: Server-side caching frequently accessed data ko memory mein store karta hai, tools jaise Varnish ya Redis ka use karke implement kiya jaata hai improved performance ke liye.

6. Web servers mein logging ka importance kya hai? उत्तर: Logging server activity ko monitor, issues ko troubleshoot, aur security ko audit karne mein madad karta hai, tools jaise ELK Stack ke sath analysis ke liye.

7. Web servers ko secure karne ke best practices kya hain? उत्तर: Best practices mein security headers ka use, software ko updated rakhna, aur firewalls ko configure karna shamil hain threats ko protect karne ke liye.

8. Load balancing mein session persistence kaise handle kiya jaata hai? उत्तर: Session persistence sticky sessions ya session replication ka use karke achieve kiya ja sakta hai, user sessions ko consistent rakhne ke liye.

9. SSL offloading kya hai aur ye kaise beneficial hai? उत्तर: SSL offloading SSL/TLS traffic ko load balancer par decrypt karta hai, server load ko kam karte hue aur performance ko improve karte hue.

10. Web servers ko horizontally scale karne ka process kya hai? उत्तर: Horizontal scaling mein zyada servers add kiya jaata hai increased load ko handle karne ke liye, load balancers aur auto-scaling groups ke sath manage kiya jaata hai.

---

### CI/CD and DevOps

1. GitOps kya hai aur ye traditional CI/CD se kaise alag hai? उत्तर: GitOps infrastructure ko code ke roop mein treat karta hai, Git repositories ko configurations aur deployments ko manage karne ke liye use karta hai, declarative definitions par emphasis karte hue.

2. Blue/Green deployment strategy kya hai? उत्तर: Blue/Green deployment do identical environments ko run karta hai, successful deployment par traffic ko new environment par switch karte hue.

3. Jenkins pipeline kya hai aur ye kaise configure kiya jaata hai? उत्तर: Jenkins pipeline ek series of steps hai building, testing, aur deploying software ke liye, Jenkinsfile mein declarative ya scripted syntax ke sath define kiya jaata hai.

4. CI/CD pipeline mein continuous integration kaise implement kiya jaata hai? उत्तर: Continuous integration code ko commits par automatically build aur test karta hai, code ko always deployable state mein rakhne ke liye.

5. CI/CD mein Docker ka role kya hai? उत्तर: Docker containers consistent environments provide karte hain building, testing, aur deploying applications ke liye, stages ke beech parity ko ensure karte hue.

6. Infrastructure as Code (IaC) ka concept kya hai? उत्तर: IaC infrastructure ko code ke sath manage karta hai, version control, automation, aur environment setups ke consistency ko allow karte hue.

7. CI/CD mein Kubernetes ka use ke benefits kya hain? उत्तर: Kubernetes containerized applications ko orchestrate karta hai, scalability, self-healing, aur declarative deployment capabilities provide karte hue.

8. CI/CD pipeline mein security scanning kaise handle kiya jaata hai? उत्तर: Security scanning tools jaise SonarQube ya OWASP Dependency Check pipelines mein integrate hote hain vulnerabilities ko early detect karne ke liye.

9. Failed deployment ko rollback karne ka process kya hai? उत्तर: Rollbacks version control ya CI/CD tools ke sath automate kiya ja sakta hai, failure par known stable version par revert karte hue.

10. DevOps mein environment management ka importance kya hai? उत्तर: Environment management development, testing, aur production ke beech consistency ko ensure karta hai, environment-specific issues ko kam karte hue.

---

### Design Patterns and Best Practices

1. Singleton pattern kya hai aur ye kab use kiya jaana chahiye? उत्तर: Singleton ensure karta hai ki ek class ke sirf ek instance hoga, shared resources jaise databases ya configuration settings ko manage karne ke liye useful hai.

2. Factory pattern aur uske benefits kya hain? उत्तर: Factory pattern ek interface provide karta hai objects ko create karne ke liye unke classes ko specify karne ke bina, loose coupling ko promote karte hue.

3. Strategy pattern kya hai aur ye flexibility ko kaise promote karta hai? उत्तर: Strategy pattern runtime par ek algorithm ko select karne ki anumati deta hai, flexible behavior changes ko allow karte hue code ko modify karne ke bina.

4. SOLID principles kya hain aur unka significance kya hai? उत्तर: SOLID principles (Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion) design ko maintainable aur scalable code ke liye guide karte hain.

5. Dependency injection code quality ko kaise improve karta hai? उत्तर: Dependency injection object creation ko externalize karta hai, code ko modular aur testable banate hue coupling ko kam karte hue.

6. Event sourcing kya hai aur ye traditional data storage se kaise alag hai? उत्तर: Event sourcing ek sequence of events ko store karta hai jo state changes ko describe karte hain, state reconstruction aur audit trails ko allow karte hue.

7. CQRS architecture pattern kya hai? उत्तर: CQRS commands (write operations) aur queries (read operations) ko separate karta hai, write aur read concerns ko alag-alag optimize karte hue.

8. Code refactoring ke best practices kya hain? उत्तर: Best practices mein small, incremental changes, tests ko maintain karna, aur automated refactorings ke tools ka use shamil hain.

9. Clean code practices ko kaise ensure kiya jaata hai? उत्तर: Clean code practices mein meaningful naming, standards ke adherence, aur self-documenting code likhna shamil hain.

10. TDD (Test-Driven Development) ka importance kya hai? उत्तर: TDD code likhne se pehle tests likhne ka process hai, code ko requirements ko meet karne ke liye ensure karte hue aur continuous testing ke sath maintainability ko improve karte hue.

---

### Security

1. OAuth2 kya hai aur ye authorization ke liye kaise use hota hai? उत्तर: OAuth2 ek authorization framework hai jo third-party applications ko resources ko access karne ki anumati deta hai credentials ko share karne ke bina.

2. JWT (JSON Web Tokens) aur unka security mein role kya hai? उत्तर: JWT ek compact aur self-contained tarika provide karta hai information ko securely transmit karne ke liye parties ke beech, authentication aur information exchange ke liye use hota hai.

3. RBAC kya hai aur ye access control ko kaise simplify karta hai? उत्तर: Role-Based Access Control roles ko permissions assign karta hai, user access management ko simplify karte hue roles ko users assign karte hue.

4. SQL injection attacks ko kaise roka ja sakta hai? उत्तर: Prepared statements aur parameterized queries ka use karke code aur data ko separate karke malicious SQL execution ko rokta hai.

5. XSS (Cross-Site Scripting) kya hai aur ye kaise prevent kiya ja sakta hai? उत्तर: XSS attackers ko scripts ko web pages mein inject karne ki anumati deta hai; ye sanitizing inputs aur outputs aur security headers ka use karke prevent kiya ja sakta hai.

6. Data security mein encryption ka importance kya hai? उत्तर: Encryption data confidentiality ko protect karta hai data ko unreadable format mein convert karke, sirf authorized parties ko access karne ki anumati deta hai.

7. Java mein secure coding ke best practices kya hain? उत्तर: Practices mein input validation, secure libraries ka use, aur security guidelines jaise OWASP ka adherence shamil hain.

8. Applications mein audit trails kaise implement kiya jaata hai? उत्तर: Audit trails user actions aur system events ko log karte hain, security aur compliance ke liye visibility aur accountability provide karte hue.

9. Two-factor authentication kya hai aur ye kaise important hai? उत्तर: Two-factor authentication ek extra layer of security provide karta hai do forms of verification ko require karke, unauthorized access risks ko kam karte hue.

10. Web Application Firewall (WAF) ka role kya hai? उत्तर: WAF web applications ko attacks jaise SQL injection aur XSS se protect karta hai HTTP traffic ko filter aur monitor karte hue.