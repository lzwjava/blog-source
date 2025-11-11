---
audio: false
generated: true
lang: hi
layout: post
title: स्वैगर एनोटेशन्स
translated: true
type: note
---

अपने Java प्रोजेक्ट में, विशेष रूप से Spring Boot के साथ बनाए गए REST API को डॉक्यूमेंट करने के लिए, `swagger-annotations` पैकेज का उपयोग करने के लिए इन चरणों का पालन करें। यह गाइड मानती है कि आप Swagger 2.0 का उपयोग कर रहे हैं, जो आमतौर पर `springfox` लाइब्रेरी के साथ इंटीग्रेट किया जाता है। `swagger-annotations` पैकेज आपके API एंडपॉइंट्स में मेटाडेटा जोड़ने के लिए एनोटेशन प्रदान करता है, जो API डॉक्यूमेंटेशन के स्वचालित जनरेशन को सक्षम बनाता है।

---

### चरण 1: आवश्यक डिपेंडेंसीज जोड़ें

आपको अपने प्रोजेक्ट में `swagger-annotations` पैकेज और एक Swagger इंटीग्रेशन लाइब्रेरी (जैसे `springfox`) को शामिल करने की आवश्यकता है। यदि आप Maven का उपयोग कर रहे हैं, तो अपनी `pom.xml` में निम्नलिखित डिपेंडेंसीज जोड़ें:

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
- **`springfox-swagger2`**: Swagger को Spring Boot के साथ इंटीग्रेट करता है और एनोटेशन को प्रोसेस करता है।
- **`springfox-swagger-ui`**: जनरेट किए गए डॉक्यूमेंटेशन को देखने के लिए एक वेब इंटरफेस जोड़ता है।

> **नोट**: [Maven Repository](https://mvnrepository.com/) पर नवीनतम वर्जन की जांच करें क्योंकि ये वर्जन (`swagger-annotations` के लिए 1.6.2 और `springfox` के लिए 2.9.2) के अपडेट हो सकते हैं।

---

### चरण 2: अपने एप्लिकेशन में Swagger कॉन्फ़िगर करें

Swagger को सक्षम करने और उसे आपके API को एनोटेशन के लिए स्कैन करने की अनुमति देने के लिए, एक `Docket` बीन के साथ एक कॉन्फ़िगरेशन क्लास बनाएं। इसे अपने Spring Boot एप्लिकेशन में जोड़ें:

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
                .paths(PathSelectors.any())          // सभी पाथ्स को शामिल करें
                .build();
    }
}
```

- **`@EnableSwagger2`**: Swagger 2.0 सपोर्ट को सक्रिय करता है।
- **`Docket`**: कॉन्फ़िगर करता है कि किन एंडपॉइंट्स को डॉक्यूमेंट करना है। उपरोक्त सेटअप सभी कंट्रोलर्स और पाथ्स को स्कैन करता है, लेकिन आप इसे कस्टमाइज़ कर सकते हैं (उदाहरण के लिए, `RequestHandlerSelectors.basePackage("com.example.controllers")`) स्कोप को सीमित करने के लिए।

---

### चरण 3: अपने कोड में Swagger एनोटेशन का उपयोग करें

`swagger-annotations` पैकेज आपके API का वर्णन करने के लिए एनोटेशन प्रदान करता है। इन्हें अपनी कंट्रोलर क्लासेज, मेथड्स, पैरामीटर्स और मॉडल्स पर लागू करें। नीचे उदाहरणों के साथ सामान्य एनोटेशन दिए गए हैं:

#### एक कंट्रोलर को एनोटेट करना

कंट्रोलर का वर्णन करने के लिए `@Api` का उपयोग करें:

```java
import io.swagger.annotations.Api;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@Api(value = "User Controller", description = "Operations pertaining to users")
@RestController
@RequestMapping("/users")
public class UserController {
    // मेथड्स यहाँ जाएंगी
}
```

- **`value`**: API के लिए एक संक्षिप्त नाम।
- **`description`**: कंट्रोलर क्या करता है इसका संक्षिप्त विवरण।

#### API ऑपरेशन्स को एनोटेट करना

अलग-अलग एंडपॉइंट्स का वर्णन करने के लिए `@ApiOperation` का उपयोग करें:

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

#### पैरामीटर्स का वर्णन करना

मेथड पैरामीटर्स के लिए `@ApiParam` का उपयोग करें:

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

- **`value`**: पैरामीटर का वर्णन करता है।
- **`required`**: इंगित करता है कि पैरामीटर अनिवार्य है या नहीं।

#### रिस्पॉन्सेज निर्दिष्ट करना

संभावित HTTP रिस्पॉन्सेज को डॉक्यूमेंट करने के लिए `@ApiResponses` और `@ApiResponse` का उपयोग करें:

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

- **`code`**: HTTP स्टेटस कोड।
- **`message`**: रिस्पॉन्स का विवरण।

#### मॉडल्स का वर्णन करना

डेटा ट्रांसफर ऑब्जेक्ट्स (DTOs) के लिए, `@ApiModel` और `@ApiModelProperty` का उपयोग करें:

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

- **`@ApiModel`**: मॉडल का वर्णन करता है।
- **`@ApiModelProperty`**: प्रत्येक फील्ड का विवरण देता है, वैकल्पिक उदाहरणों के साथ।

---

### चरण 4: डॉक्यूमेंटेशन रन करें और एक्सेस करें

1. अपना Spring Boot एप्लिकेशन स्टार्ट करें।
2. एक ब्राउज़र खोलें और इस URL पर नेविगेट करें:  
   **http://localhost:8080/swagger-ui.html**  
   यह URL Swagger UI को प्रदर्शित करता है, जो एनोटेशन के आधार पर आपके API डॉक्यूमेंटेशन को दिखाने वाला एक इंटरैक्टिव इंटरफेस है।

---

### `swagger-annotations` का उपयोग कैसे करें - सारांश

1.  **डिपेंडेंसीज जोड़ें**: अपनी `pom.xml` में `swagger-annotations` और `springfox` शामिल करें।
2.  **Swagger कॉन्फ़िगर करें**: Swagger स्कैनिंग को सक्षम करने के लिए एक `Docket` बीन सेट अप करें।
3.  **अपने कोड को एनोटेट करें**:
    - कंट्रोलर्स के लिए `@Api`।
    - मेथड्स के लिए `@ApiOperation`।
    - पैरामीटर्स के लिए `@ApiParam`।
    - रिस्पॉन्स विवरण के लिए `@ApiResponses` और `@ApiResponse`।
    - DTOs के लिए `@ApiModel` और `@ApiModelProperty`।
4.  **डॉक्यूमेंटेशन देखें**: Swagger UI को `/swagger-ui.html` पर एक्सेस करें।

---

### अतिरिक्त नोट्स

- **Swagger 2.0 बनाम OpenAPI 3.0**: यह गाइड `io.swagger:swagger-annotations` के साथ Swagger 2.0 का उपयोग करती है। OpenAPI 3.0 के लिए, `io.swagger.core.v3:swagger-annotations` और `springdoc-openapi` जैसी लाइब्रेरी का उपयोग करें, जो कुछ एनोटेशन नाम बदल देती है (उदाहरण के लिए, `@Api` के बजाय `@Tag`)।
- **कस्टमाइज़ेशन**: अधिक केंद्रित डॉक्यूमेंटेशन के लिए विशिष्ट पैकेज या पाथ्स को फ़िल्टर करने के लिए `Docket` कॉन्फ़िगरेशन को एडजस्ट करें।
- **गुणवत्ता**: जनरेट किए गए डॉक्यूमेंटेशन की उपयोगिता को बेहतर बनाने के लिए एनोटेशन में स्पष्ट, विस्तृत विवरण प्रदान करें।

इन चरणों का पालन करके, आप अपने REST API को डॉक्यूमेंट करने के लिए `swagger-annotations` पैकेज का प्रभावी ढंग से उपयोग कर सकते हैं, जिससे डेवलपर्स और उपभोक्ताओं के लिए आपके एंडपॉइंट्स को समझना और उनके साथ इंटरैक्ट करना आसान हो जाता है।