---
audio: false
generated: true
image: false
lang: ar
layout: post
title: أطر اختبار واجهة برمجة تطبيقات بايثون
translated: true
type: note
---

### أطر عمل Python الموصى بها لاختبار نقاط نهاية API

لاختبار نقاط نهاية الخادم المكتوبة بلغة Java (مثل Spring Boot)، يمكنك استخدام أطر عمل Python لإجراء اختبارات التكامل أو اختبارات نقاط النهاية عن طريق إرسال طلبات HTTP مثل GET وPOST وPUT وDELETE، وما إلى ذلك، والتحقق من رموز الاستجابة والرؤوس ومحتوى الجسم. نظرًا لأن الخادم مكتوب بلغة Java، تعامل معه على أنه API صندوق أسود واستخدم مكتبات عميل HTTP في Python (مثل `requests` أو `httpx`) للتفاعل معه. يتضمن الإعداد الأكثر شيوعًا إطار عمل مشغل اختبار مدمج مع مكتبة HTTP.

فيما يلي بعض الخيارات القوية، مُرتبة حسب الشعبية والملاءمة لحالة استخدامك (استنادًا إلى التوصيات الحديثة اعتبارًا من عام 2025). سأركز على تلك التي تدعم تفاعلات HTTP السهلة والتحقق من الاستجابة:

#### 1. **pytest (مع مكتبة requests أو httpx)**
   - **لماذا هو جيد**: pytest هو إطار عمل اختبار Python الأكثر شيوعًا لاختبارات الوحدة والتكامل وAPI. إنه مرن، وله بناء جملة بسيط، ويدعم التركيبات للإعداد/الهدم (مثل بدء خادم اختبار أو الـ Mocking). يمكنك كتابة اختبارات لإرسال طلبات GET/POST والتأكيد على رموز الحالة (مثل 200 OK) واستجابات JSON. وهو قابل للتوسيع مع الإضافات مثل `pytest-httpx` للاختبار غير المتزامن.
   - **كيفية استخدامه في سيناريوهك**:
     - التثبيت: `pip install pytest requests` (أو `pip install pytest httpx` للاختبار غير المتزامن).
     - مثال على الاختبار:
       ```python
       import requests
       import pytest

       @pytest.fixture
       def base_url():
           return "http://your-java-server:8080"

       def test_get_endpoint(base_url):
           response = requests.get(f"{base_url}/api/resource")
           assert response.status_code == 200
           assert "expected_key" in response.json()

       def test_post_endpoint(base_url):
           data = {"key": "value"}
           response = requests.post(f"{base_url}/api/resource", json=data)
           assert response.status_code == 201
           assert response.json()["status"] == "created"
       ```
     - الإيجابيات: سهل القراءة، إضافات المجتمع، تنفيذ متوازي، رائع لـ CI/CD.
     - السلبيات: يتطلب بعض البرمجة؛ ليس تصريفيًا بحتًا.
   - الأفضل لـ: اختبارات التكامل حيث تحتاج إلى منطق مخصص.

#### 2. **Tavern**
   - **لماذا هو جيد**: Tavern هو إضافة لـ pytest مصممة خصيصًا لاختبارات RESTful API. يستخدم ملفات YAML لتعريف الاختبارات بطريقة تصريحية، مما يجعله سهلًا لتحديد طرق HTTP والحِمل المتوقع واستجابات دون الحاجة إلى الكثير من كود Python. مثالي للتحقق من نقاط النهاية، بما في ذلك رموز الحالة وفحوصات مخطط JSON.
   - **كيفية استخدامه في سيناريوهك**:
     - التثبيت: `pip install tavern`.
     - مثال على ملف اختبار YAML:
       ```yaml
       test_name: Test GET endpoint
       stages:
         - name: Get resource
           request:
             url: http://your-java-server:8080/api/resource
             method: GET
           response:
             status_code: 200
             json:
               expected_key: expected_value

       test_name: Test POST endpoint
       stages:
         - name: Post resource
           request:
             url: http://your-java-server:8080/api/resource
             method: POST
             json: { "key": "value" }
           response:
             status_code: 201
             json:
               status: created
       ```
     - التشغيل باستخدام: `pytest your_test.yaml`.
   - الإيجابيات: YAML سهل القراءة للإنسان، يتكامل مع pytest، عمليات إعادة المحاولة والتحقق التلقائية.
   - السلبيات: أقل مرونة للمنطق المعقد مقارنة بـ Python الخالص.
   - الأفضل لـ: اختبارات API سريعة وتصريحية تركز على نقاط النهاية.

#### 3. **PyRestTest**
   - **لماذا هو جيد**: أداة Python خفيفة الوزن لاختبار REST API باستخدام ملفات تكوين YAML أو JSON. إنه خالٍ من الكود للاختبارات الأساسية، ويدعم المعايير، وهو رائع للتحقق من استجابات HTTP من الخوادم الخارجية مثل نقاط نهاية Java الخاصة بك.
   - **كيفية استخدامه في سيناريوهك**:
     - التثبيت: `pip install pyresttest`.
     - مثال YAML:
       ```yaml
       - config:
           url: http://your-java-server:8080
       - test:
           name: GET test
           url: /api/resource
           method: GET
           expected_status: [200]
           validators:
             - {jsonpath_mini: 'expected_key', expected: 'expected_value'}
       - test:
           name: POST test
           url: /api/resource
           method: POST
           body: '{"key": "value"}'
           expected_status: [201]
           validators:
             - {jsonpath_mini: 'status', expected: 'created'}
       ```
     - التشغيل باستخدام: `pyresttest http://base-url test.yaml`.
   - الإيجابيات: إعداد بسيط، لا حاجة لكود متكرر، محمول.
   - السلبيات: مجتمع محدود مقارنة بـ pytest؛ أداة أقدم ولكنها لا تزال محفوظة.
   - الأفضل لـ: المعايير الدقيقة واختبارات التكامل البسيطة.

#### 4. **Robot Framework (مع RequestsLibrary)**
   - **لماذا هو جيد**: إطار عمل قائم على الكلمات المفتاحية لاختبارات القبول وAPI. مع `RequestsLibrary`، يتعامل مع طلبات HTTP بشكل أصلي وقابل للتوسيع لاختبارات التكامل. جيد للفرق التي تفضل اختبارات قابلة للقراءة بدون كود.
   - **كيفية استخدامه في سيناريوهك**:
     - التثبيت: `pip install robotframework robotframework-requests`.
     - مثال على ملف الاختبار:
       ```
       *** Settings ***
       Library    RequestsLibrary

       *** Test Cases ***
       Test GET Endpoint
           Create Session    mysession    http://your-java-server:8080
           ${response}=    GET On Session    mysession    /api/resource
           Status Should Be    200    ${response}
           ${json}=    To Json    ${response.content}
           Should Be Equal    ${json['expected_key']}    expected_value

       Test POST Endpoint
           Create Session    mysession    http://your-java-server:8080
           ${data}=    Create Dictionary    key=value
           ${response}=    POST On Session    mysession    /api/resource    json=${data}
           Status Should Be    201    ${response}
           ${json}=    To Json    ${response.content}
           Should Be Equal    ${json['status']}    created
       ```
     - التشغيل باستخدام: `robot your_test.robot`.
   - الإيجابيات: قائم على الكلمات المفتاحية (سهل لغير المطورين)، التقارير مدمجة.
   - السلبيات: بناء الجملة مطول؛ منحنى تعلم أكثر حدة لمحبي Python.
   - الأفضل لـ: اختبارات التكامل بأسلوب BDD.

#### نصائح إضافية
- **مكتبة شائعة: requests**:几乎所有几乎 جميع أطر العمل تعمل جيدًا معها لمكالمات HTTP. إنها بسيطة (`response = requests.get(url)`)، وتتعامل مع JSON تلقائيًا، وتم اختبارها جيدًا.
- **بديل لـ requests: httpx**: استخدمه إذا كنت بحاجة إلى دعم غير متزامن (مثل اختبارات الإنتاجية العالية). قم بالتثبيت عبر `pip install httpx`.
- **الإعداد لخادم Java**: تأكد من تشغيل خادم Java محليًا أو عن بُعد. لاختبارات التكامل، فكر في استخدام Docker لتشغيل تطبيق Spring Boot في CI/CD.
- **الاختيار العام الأفضل**: ابدأ بـ pytest + requests للمرونة. إذا كنت تفضل الاختبارات التصريحية، فاختر Tavern أو PyRestTest.
- **اعتبارات**: تعمل هذه الأدوات عبر اللغات لأنها تستخدم HTTP القياسي. للتحقق من المخطط، أضف مكتبات مثل `jsonschema`. قم بالتشغيل في CI/CD باستخدام أدوات مثل Jenkins أو GitHub Actions.

### المراجع
[Top Python Testing Frameworks in 2025 You Should Switch To](https://medium.com/@hadiyolworld007/top-python-testing-frameworks-in-2025-you-should-switch-to-6ddeb679ccd5)  
[10 Best Python Testing Frameworks To Look For In 2025](https://www.lambdatest.com/blog/top-python-testing-frameworks/)  
[Top 14 Best Python Automation Tools for Testing in 2025](https://apidog.com/blog/best-python-testing-tools-2025/)  
[The Best Open Source API Testing Tools for 2025](https://testguild.com/12-open-source-api-testing-tools-rest-soap-services/)