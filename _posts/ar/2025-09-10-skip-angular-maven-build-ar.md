---
audio: false
date: 2025-09-10
generated: true
image: false
lang: ar
layout: post
model: openai/gpt-5
title: تخطي بناء Angular في Maven
translated: true
type: note
---

إجابة قصيرة: نعم—يمكنك تخطي بناء Angular/npm، ولكن ليس باستخدام علامة مدمجة مثل `--skip-web`. استخدم إحدى هذه الطرق.

### ١) استبعاد وحدة الويب في بناء متعدد الوحدات

إذا كان تطبيق Angular الخاص بك عبارة عن وحدة Maven منفصلة (مثل `web`)، فما عليك سوى استبعاده في المفاعل:

```
mvn -pl '!web' -am clean package
```

أو ابنِ فقط وحدة الخلفية:

```
mvn -pl :backend -am clean package
```

(الوسيط `-am` يبني أي تبعيات مطلوبة؛ بناء الجملة `!web` يستبعد تلك الوحدة.)

### ٢) إضافة خاصية "تخطي الواجهة الأمامية" (تعمل مع frontend-maven-plugin أو exec)

احمِ أهداف npm باستخدام خاصية واشغلها من سطر الأوامر.

**ملف POM (وحدة الويب أو الأصل):**

```xml
<properties>
  <skip.frontend>false</skip.frontend>
</properties>

<build>
  <plugins>
    <!-- مثال: com.github.eirslett:frontend-maven-plugin -->
    <plugin>
      <groupId>com.github.eirslett</groupId>
      <artifactId>frontend-maven-plugin</artifactId>
      <version>...your version...</version>
      <configuration>
        <skip>${skip.frontend}</skip>
      </configuration>
      <executions>
        <execution>
          <id>npm-build</id>
          <phase>prepare-package</phase>
          <goals>
            <goal>npm</goal>
          </goals>
          <configuration>
            <arguments>run build</arguments>
          </configuration>
        </execution>
      </executions>
    </plugin>

    <!-- إذا كنت تستخدم exec-maven-plugin لاستدعاء npm -->
    <plugin>
      <groupId>org.codehaus.mojo</groupId>
      <artifactId>exec-maven-plugin</artifactId>
      <version>...your version...</version>
      <executions>
        <execution>
          <id>npm-build</id>
          <phase>prepare-package</phase>
          <goals><goal>exec</goal></goals>
          <configuration>
            <skip>${skip.frontend}</skip>
            <executable>npm</executable>
            <arguments>
              <argument>run</argument>
              <argument>build</argument>
            </arguments>
          </configuration>
        </execution>
      </executions>
    </plugin>
  </plugins>
</build>
```

**سطر الأوامر:**

```
mvn -Dskip.frontend=true clean package
```

### ٣) استخدام ملفات تعريف Maven

اربط بناء الواجهة الأمامية فقط في ملف تعريف "with-frontend" واجعل ملف تعريف "skip-frontend" هو الافتراضي في بيئة التطوير.

**ملف POM:**

```xml
<profiles>
  <profile>
    <id>with-frontend</id>
    <activation>
      <property>
        <name>!skip.frontend</name>
      </property>
    </activation>
    <build>
      <plugins>
        <!-- نفس إعدادات الإضافة كما ورد أعلاه، بدون خاصية skip -->
      </plugins>
    </build>
  </profile>
</profiles>
```

**سطر الأوامر:**

* العادي (تخطي): `mvn -Dskip.frontend clean package`
* الإصدار (بناء واجهة المستخدم): `mvn -Pwith-frontend clean package`

---

## نصائح للسرعة إذا كنت *ستبني* واجهة المستخدم

* تأكد من تشغيل ذاكرة التخزين المؤقت الدائمة لـ Angular (Angular CLI يقوم بالتخزين المؤقت افتراضيًا؛ احتفظ بـ `node_modules` و `.angular/cache` مخبأة في التكامل المستمر).
* شغّل `ng build` فقط للإصدار؛ في بيئة التطوير، قدّم واجهة المستخدم بشكل منفصل (`npm start`) واجعل Spring يخدم الأصول الثابتة المبنية مسبقًا (على سبيل المثال، ضع `dist/` تحت `src/main/resources/static` للبناء المعبأ).
* فكر في تقسيم المستودع بحيث لا يكون تطبيق Angular وحدة Maven على الإطلاق؛ ابنه فقط عندما تتغير ملفات الواجهة الأمامية.
* إذا كنت تستخدم إصدارًا حديثًا من Angular، فاستخدم أداة البناء الافتراضية esbuild/Vite وأبطل عمل خرائط المصدر في بناء إصدار التكامل المستمر.

---

### خلاصة القول

استخدم `-pl '!web'` لاستبعاد وحدة الويب، **أو** أضف خاصية `skip.frontend` وربط تنفيذات الإضافة الخاصة بك لاحترامها. لا توجد علامة قياسية `mvn package --skip-web`، لكن النمطين المذكورين أعلاه موثوقان وشائعان.