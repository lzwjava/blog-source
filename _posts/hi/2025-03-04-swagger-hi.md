---
audio: false
generated: true
lang: hi
layout: post
title: Swagger Annotations का अनुवाद
translated: true
---

`swagger-annotations` पैकेज को अपने Java प्रोजेक्ट में, विशेष रूप से Spring Boot के साथ बनाए गए REST API को दस्तावेजीकरण करने के लिए, इन चरणों का पालन करें। यह गाइड आपको Swagger 2.0 का उपयोग करने की अनुमति देता है, जो आम तौर पर `springfox` लाइब्रेरी के साथ एकीकृत होता है। `swagger-annotations` पैकेज एनोटेशन प्रदान करता है ताकि आप अपने API एंडपॉइंट्स में मेटाडेटा जोड़ सकें, जिससे API दस्तावेजीकरण का स्वचालित जनरेशन संभव हो जाता है।

---

### चरण 1: आवश्यक निर्भरताओं को जोड़ें

आपको अपने प्रोजेक्ट में `swagger-annotations` पैकेज और एक Swagger एकीकृत लाइब्रेरी (जैसे `springfox`) शामिल करनी होगी। अगर आप Maven का उपयोग कर रहे हैं, तो अपने `pom.xml` में निम्न निर्भरताओं को जोड़ें:

```xml
<!-- Swagger Annotations -->
<dependency>
    <groupId>io.swagger</groupId>
    <artifactId>swagger-annotations</artifactId>
    <version>1.6.2</version>
</dependency>

<!-- Springfox Swagger 2 for Swagger Integration -->
<dependency>
    <groupId>io.springfox</groupId>
    <artifactId>springfox-swagger2</artifactId>
    <version>2.9.2</version>
</dependency>

<!-- Springfox Swagger UI for Interactive Documentation -->
<dependency>
    <groupId>io.springfox</groupId>
    <artifactId>springfox-swagger-ui</artifactId>
    <version>2.9.2</version>
</dependency>
```

- **`io.swagger:swagger-annotations`**: Swagger 2.0 के लिए एनोटेशन प्रदान करता है।
- **`springfox-swagger2`**: Swagger को Spring Boot के साथ एकीकृत करता है और एनोटेशन को प्रोसेस करता है।
- **`springfox-swagger-ui`**: उत्पन्न दस्तावेजीकरण को देखने के लिए वेब इंटरफेस जोड़ता है।

> **नोट**: [Maven Repository](https://mvnrepository.com/) पर नवीनतम संस्करणों की जांच करें क्योंकि इन संस्करणों (1.6.2 के लिए `swagger-annotations` और 2.9.2 के लिए `springfox`) में अपडेट हो सकते हैं।

---

### चरण 2: अपने एप्लिकेशन में Swagger को कॉन्फ़िगर करें

Swagger को सक्रिय करने और अपने API को एनोटेशन के लिए स्कैन करने के लिए, एक कॉन्फ़िगरेशन क्लास बनाएं जिसमें एक `Docket` बीन है। इसे अपने Spring Boot एप्लिकेशन में जोड़ें:

```java
import springfox.documentation.builders.PathSelectors;
import springfox.documentation.builders.RequestHandlerSelectors;
import springfox.documentation.spi.DocumentationType;
import springfox.documentation.spring.web.plugins.Docket;
import springfox.documentation.swagger2.annotations.EnableSwagger2;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
@EnableSwagger2
public class SwaggerConfig {
    @Bean
    public Docket api() {
        return new Docket(DocumentationType.SWAGGER_2)
                .select()
                .apis(RequestHandlerSelectors.any()) // सभी कंट्रोलर्स को स्कैन करें
                .paths(PathSelectors.any())          // सभी पथ शामिल करें
                .build();
    }
}
```

- **`@EnableSwagger2`**: Swagger 2.0 समर्थन सक्रिय करता है।
- **`Docket`**: दस्तावेजीकरण करने के लिए एंडपॉइंट्स को कॉन्फ़िगर करता है। ऊपर दिए गए सेटिंग सभी कंट्रोलर्स और पथ को स्कैन करते हैं, लेकिन आप इसे अनुकूलित कर सकते हैं (जैसे, `RequestHandlerSelectors.basePackage("com.example.controllers")`) को सीमित करने के लिए।

---

### चरण 3: अपने कोड में Swagger एनोटेशन का उपयोग करें

`swagger-annotations` पैकेज एनोटेशन प्रदान करता है ताकि आप अपने API को वर्णित कर सकें। इनको अपने कंट्रोलर क्लास, मेथड, पैरामीटर और मॉडल में लागू करें। नीचे आम एनोटेशन के साथ उदाहरण दिए गए हैं:

#### एक कंट्रोलर को एनोटेट करें

`@Api` का उपयोग कंट्रोलर को वर्णित करने के लिए करें:

```java
import io.swagger.annotations.Api;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@Api(value = "User Controller", description = "Users के संबंधित ऑपरेशंस")
@RestController
@RequestMapping("/users")
public class UserController {
    // Methods go here
}
```

- **`value`**: API का एक छोटा नाम।
- **`description`**: कंट्रोलर क्या करता है, इसके बारे में एक संक्षिप्त व्याख्या।

#### API ऑपरेशंस को एनोटेट करें

`@ApiOperation` का उपयोग व्यक्तिगत एंडपॉइंट्स को वर्णित करने के लिए करें:

```java
import io.swagger.annotations.ApiOperation;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;

@ApiOperation(value = "Get a user by ID", response = User.class)
@GetMapping("/{id}")
public ResponseEntity<User> getUserById(@PathVariable Long id) {
    // Implementation
    return ResponseEntity.ok(new User(id, "John Doe"));
}
```

- **`value`**: ऑपरेशन का सारांश।
- **`response`**: अपेक्षित रिटर्न टाइप।

#### पैरामीटर को वर्णित करें

`@ApiParam` का उपयोग मेथड पैरामीटर के लिए करें:

```java
import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiParam;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

@ApiOperation(value = "Create a new user")
@PostMapping
public ResponseEntity<User> createUser(
        @ApiParam(value = "User object to be created", required = true)
        @RequestBody User user) {
    // Implementation
    return ResponseEntity.ok(user);
}
```

- **`value`**: पैरामीटर को वर्णित करता है।
- **`required`**: पैरामीटर अनिवार्य है, यह बताता है।

#### प्रतिक्रियाओं को वर्णित करें

`@ApiResponses` और `@ApiResponse` का उपयोग संभव HTTP प्रतिक्रियाओं को दस्तावेजीकरण करने के लिए करें:

```java
import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiResponses;
import io.swagger.annotations.ApiResponse;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.PathVariable;

@ApiOperation(value = "Delete a user")
@ApiResponses(value = {
    @ApiResponse(code = 200, message = "User deleted successfully"),
    @ApiResponse(code = 404, message = "User not found")
})
@DeleteMapping("/{id}")
public ResponseEntity<Void> deleteUser(@PathVariable Long id) {
    // Implementation
    return ResponseEntity.ok().build();
}
```

- **`code`**: HTTP स्थिति कोड।
- **`message`**: प्रतिक्रिया का वर्णन।

#### मॉडल को वर्णित करें

डेटा ट्रांसफर ऑब्जेक्ट (DTOs) के लिए, `@ApiModel` और `@ApiModelProperty` का उपयोग करें:

```java
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;

@ApiModel(description = "User data transfer object")
public class User {
    @ApiModelProperty(notes = "The user's unique identifier", example = "1")
    private Long id;

    @ApiModelProperty(notes = "The user's name", example = "John Doe")
    private String name;

    // Getters and setters
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    public User(Long id, String name) {
        this.id = id;
        this.name = name;
    }
}
```

- **`@ApiModel`**: मॉडल को वर्णित करता है।
- **`@ApiModelProperty`**: प्रत्येक फील्ड के बारे में विवरण, साथ ही अनिवार्य उदाहरण।

---

### चरण 4: दस्तावेजीकरण को चलाएं और पहुंचें

1. अपने Spring Boot एप्लिकेशन को शुरू करें।
2. ब्राउज़र खोलें और निम्न URL पर जाएं:
   **http://localhost:8080/swagger-ui.html**
   यह URL Swagger UI को प्रदर्शित करता है, जो आपके एनोटेशन पर आधारित API दस्तावेजीकरण का एक इंटरैक्टिव इंटरफेस है।

---

### `swagger-annotations` का उपयोग करने का सारांश

1. **निर्भरताओं को जोड़ें**: `swagger-annotations` और `springfox` को अपने `pom.xml` में शामिल करें।
2. **Swagger को कॉन्फ़िगर करें**: एक `Docket` बीन को सेट अप करें ताकि Swagger स्कैनिंग सक्रिय हो जाए।
3. **अपने कोड को एनोटेट करें**:
   - कंट्रोलर्स के लिए `@Api`।
   - मेथड के लिए `@ApiOperation`।
   - पैरामीटर के लिए `@ApiParam`।
   - प्रतिक्रिया विवरण के लिए `@ApiResponses` और `@ApiResponse`।
   - DTOs के लिए `@ApiModel` और `@ApiModelProperty`।
4. **दस्तावेजीकरण को देखें**: `/swagger-ui.html` पर Swagger UI तक पहुंचें।

---

### अतिरिक्त नोट्स

- **Swagger 2.0 vs. OpenAPI 3.0**: यह गाइड Swagger 2.0 के साथ `io.swagger:swagger-annotations` का उपयोग करता है। OpenAPI 3.0 के लिए, `io.swagger.core.v3:swagger-annotations` और एक लाइब्रेरी जैसे `springdoc-openapi` का उपयोग करें, जो कुछ एनोटेशन नामों को बदल देता है (जैसे, `@Tag` के बजाय `@Api`).
- **कस्टमाइजेशन**: `Docket` कॉन्फ़िगरेशन को अनुकूलित करें ताकि विशेष पैकेज या पथों को फिल्टर करने के लिए अधिक केंद्रित दस्तावेजीकरण हो सके।
- **गुणवत्ता**: एनोटेशन में स्पष्ट, विवरणपूर्ण वर्णन प्रदान करें ताकि उत्पन्न दस्तावेजीकरण का उपयोग करने में आसानी हो सके।

इन चरणों का पालन करके, आप `swagger-annotations` पैकेज का उपयोग करके अपने REST API को दस्तावेजीकरण कर सकते हैं, जिससे डेवलपर्स और उपयोगकर्ताओं को अपने एंडपॉइंट्स को समझने और साथ में काम करने में आसानी हो जाएगी।