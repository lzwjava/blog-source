---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-code-fast-1
title: نظرة عامة على حزم بايثون الأساسية
translated: true
type: note
---

| الترتيب | الحزمة | شرح موجز |
|------|---------|----------------------|
| 1 | requests | مكتبة HTTP بسيطة لإنشاء طلبات لخدمات الويب في Python. |
| 2 | six | أدوات التوافق بين Python 2 و 3. |
| 3 | python-dateutil | إضافات لوحدة datetime القياسية في Python. |
| 4 | setuptools | مكتبة لتنزيل وبناء وتثبيت وترقية وإلغاء تثبيت حزم Python بسهولة. |
| 5 | pip | أداة لتثبيت وإدارة حزم Python من PyPI. |
| 6 | urllib3 | مكتبة HTTP مع تجمع اتصال آمن للخيوط ومنطق إعادة المحاولة. |
| 7 | cryptography | مكتبة توفر وصفات وأساسيات التشفير في Python. |
| 8 | cffi | واجهة الوظيفة الأجنبية لاستدعاء كود C من Python. |
| 9 | wheel | تنسيق حزمة مبني لـ Python، يسمح بتثبيت أسرع. |
| 10 | PyYAML | محلل ومصدر YAML لـ Python. |
| 11 | idna | دعم لأسماء النطاقات الدولية في التطبيقات (IDNA). |
| 12 | certifi | حزمة Python لتوفير حزمة CA الخاصة بـ Mozilla. |
| 13 | chardet | كاشف ترميز الأحرف العالمي لـ Python. |
| 14 | pyparsing | محلل عام وغني بالميزات لـ Python. |
| 15 | packaging | أدوات أساسية لحزم Python. |
| 16 | numpy | الحزمة الأساسية للحوسبة المصفوفية في Python. |
| 17 | argparse | محلل لخيارات وسيطات وأوامر فرعية في سطر الأوامر. |
| 18 | jinja2 | لغة قوالب سريعة وصديقة للمصممين لـ Python. |
| 19 | MarkupSafe | مكتبة للهروب من HTML/XML في Python. |
| 20 | pandas | مكتبة عالية الأداء لتحليل ومعالجة البيانات. |
| 21 | scipy | مكتبة الحوسبة العلمية لـ Python مع وظائف رياضية متقدمة. |
| 22 | matplotlib | مكتبة الرسم لـ Python و PyLab، لإنشاء تصورات ثابتة ومتحركة وتفاعلية. |
| 23 | scikit-learn | مكتبة التعلم الآلي لـ Python مع أدوات بسيطة وفعالة لتنقيب البيانات. |
| 24 | Pillow | نسخة مشتقة من Python Imaging Library (PIL) لمعالجة الصور. |
| 25 | flask | إطار عمل ويب خفيف الوزن من نوع WSGI في Python. |
| 26 | django | إطار عمل ويب Python عالي المستوى للتطوير السريع. |
| 27 | tornado | إطار عمل ويب ومكتبة شبكات غير متزامنة. |
| 28 | sqlalchemy | أدوات SQL ومكتبة تعيين كائنية-علاقية (ORM) لـ Python. |
| 29 | alembic | أداة ترحيل قواعد البيانات لـ SQLAlchemy. |
| 30 | pytest | إطار عمل لكتابة حالات اختبار بسيطة وقابلة للتطوير في Python. |
| 31 | coverage | أداة لقياس تغطية الكود لبرامج Python. |
| 32 | toml | مكتبة Python لتحليل وإنشاء ملفات التكوين TOML. |
| 33 | click | حزمة Python لإنشاء واجهات سطر الأوامر. |
| 34 | attrs | فصول بدون كود متكرر في Python. |
| 35 | more-itertools | المزيد من الروتينات للتعامل مع الكائنات القابلة للتكرار في Python. |
| 36 | zipp | إصدار متوافق مع pathlib للتعامل مع ملفات zip. |
| 37 | importlib-metadata | جلب بيانات وصفية لـ Python متوافقة مع الإصدارات السابقة. |
| 38 | typing-extensions | تلميحات نوع مجلوبة وتجريبية لـ Python. |
| 39 | lxml | مكتبة معالجة XML تجمع بين libxml2 و libxslt مع روابط Python. |
| 40 | beautifulsoup4 | مكتبة لاستخراج البيانات من ملفات HTML و XML. |
| 41 | selenium | أداة لأتمتة متصفحات الويب. |
| 42 | openpyxl | مكتبة لقراءة/كتابة ملفات Excel 2010 xlsx/xlsm. |
| 43 | xlrd | مكتبة لقراءة البيانات من ملفات Excel. |
| 44 | xlwt | مكتبة لكتابة البيانات إلى ملفات Excel. |
| 45 | pycrypto | وحدات التشفير لـ Python. |
| 46 | pyyaml | محلل ومصدر لـ YAML. |
| 47 | bleach | تعقيم HTML. |
| 48 | paramiko | مكتبة بروتوكول SSH2 لـ Python. |
| 49 | pexpect | التحكم في البرامج التفاعلية في طرفية وهمية. |
| 50 | psutil | مكتبة متعددة المنصات لاسترداد المعلومات عن العمليات الجارية. |
| 51 | virtualenv | أداة لإنشاء بيئات Python معزولة. |
| 52 | ujson | مشفر وفك تشفير JSON فائق السرعة في Python. |
| 53 | redis | عميل Python لمخزن المفاتيح والقيم Redis. |
| 54 | flask-wtf | تكامل WTForms مع Flask. |
| 55 | wtforms | مكتبة مرنة للتحقق من النماذج وعرضها لـ Python. |
| 56 | werkzeug | مكتبة أدوات WSGI لـ Python. |
| 57 | gunicorn | خادم HTTP WSGI لـ Python لأنظمة UNIX. |
| 58 | boto3 | حزمة تطوير برمجيات AWS لـ Python. |
| 59 | kafka-python | تنفيذ Python خالص لـ Apache Kafka. |
| 60 | elasticsearch | عميل Python لـ Elasticsearch. |
| 61 | django-rest-framework | مجموعة أدوات قوية ومرنة لبناء واجهات برمجة تطبيقات الويب في Django. |
| 62 | celery | قائمة مهام موزعة. |
| 63 | sqlalchemy-utils | وظائف مساعدة متنوعة لـ SQLAlchemy. |
| 64 | sqlalchemy-migrate | أدوات ترحيل مخطط قاعدة البيانات لـ SQLAlchemy. |
| 65 | alembic | أداة ترحيل قواعد البيانات. |
| 66 | flask-sqlalchemy | تكامل Flask مع SQLAlchemy. |
| 67 | django-cors-headers | تطبيق Django للتعامل مع رؤوس الخادم المطلوبة لمشاركة الموارد بين المصادر (CORS). |
| 68 | django-filter | تطبيق Django قابل لإعادة الاستخدام للسماح للمستخدمين بتصفية مجموعات الاستعلام ديناميكيًا. |
| 69 | djangorestframework-jwt | دعم مصادقة JSON Web Token لإطار عمل Django REST. |
| 70 | django-guardian | أذونات الكائن لـ Django. |
| 71 | django-model-utils | أدوات نموذج Django للمديرين ومجموعات الاستعلام المخصصة. |
| 72 | djangorestframework | واجهات برمجة تطبيقات الويب لـ Django. |
| 73 | graphene-django | تكامل Graphene مع Django. |
| 74 | django-graphql-jwt | تكامل Django للمصادقة GraphQL باستخدام JSON Web Token. |
| 75 | aiohttp | عميل/خادم HTTP غير متزامن لـ asyncio و Python. |
| 76 | httpx | عميل HTTP من الجيل التالي لـ Python. |
| 77 | fastapi | إطار عمل ويب حديث وسريع لبناء واجهات برمجة تطبيقات باستخدام Python 3.7+ بناءً على تلميحات نوع Python القياسية. |
| 78 | uvicorn | تنفيذ خادم ويب ASGI لـ Python. |
| 79 | starlette | إطار عمل/مجموعة أدوات ASGI خفيف الوزن لبناء خدمات asyncio عالية الأداء. |
| 80 | pydantic | التحقق من البيانات وإدارة الإعدادات باستخدام تلميحات نوع Python. |
| 81 | python-multipart | محلل multipart متدفق لـ Python. |
| 82 | sqlalchemy-orm | واجهة وظيفية عالية المستوى لـ SQLAlchemy ORM. |
| 83 | sqlalchemy-pool | تنفيذات تجمع الاتصال لـ SQLAlchemy. |
| 84 | sqlalchemy-connectors | موصلات وبرامج تشغيل لـ SQLAlchemy. |
| 85 | pymongo | برنامج تشغيل Python لـ MongoDB. |
| 86 | motor | برنامج تشغيل Python غير متزامن لـ MongoDB. |
| 87 | influxdb | عميل Python لـ InfluxDB. |
| 88 | peewee | ORM صغير ومعبر لـ Python. |
| 89 | tortoise-orm | ORM غير متزامن سهل الاستخدام لـ Python 3.5 فما فوق مستوحى من Django. |
| 90 | aerich | أداة ترحيل لـ Tortoise ORM، مستوحاة من Alembic. |
| 91 | redis-py | مكتبة عميل Python لـ Redis. |
| 92 | aioredis | مكتبة عميل Redis لـ asyncio. |
| 93 | celery | قائمة مهام موزعة. |
| 94 | django-celery | تكامل Celery مع Django. |
| 95 | rq | قوائم وظائف بسيطة لـ Python. |
| 96 | channels | Django Channels، تطبيق ASGI للويب سوكيت، المهام في الخلفية، إلخ. |
| 97 | django-channels | تكامل Django مع Channels. |
| 98 | daphne | خادم بروتوكول HTTP و HTTP2 و WebSocket لـ ASGI و Django Channels. |
| 99 | mkdocs | توثيق المشروع باستخدام Markdown. |
| 100 | sphinx | مولد توثيق Python. |
| 101 | pdoc3 | إنشاء توثيق واجهة برمجة التطبيقات تلقائيًا لمشاريع Python. |
| 102 | pytest-asyncio | إضافة Pytest لاختبار الكود غير المتزامن. |
| 103 | pytest-cov | إضافة Pittest لإعداد تقارير التغطية. |
| 104 | hypothesis | مكتبة اختبار متقدمة قائمة على الخصائص لـ Python. |
| 105 | faker | إنشاء بيانات وهمية للاختبار. |
| 106 | factory-boy | بديل لأدوات الاختبار لـ Python. |
| 107 | model-mommy | أدوات اختبار ذكية لـ Django. |
| 108 | requests-mock | محاكاة الردود من مكتبة requests للاختبار. |
| 109 | responses | مكتبة أدوات لمحاكاة مكتبة requests في Python. |
| 110 | vcrpy | محاكاة تفاعلات HTTP تلقائيًا لتبسيط وتسريع الاختبار. |
| 111 | httmock | مكتبة محاكاة لـ requests. |
| 112 | freezegun | دع اختبارات Python الخاصة بك تسافر عبر الزمن. |
| 113 | pytest-django | إضافة Pytest لاختبار تطبيقات Django. |
| 114 | pytest-flask | إضافة Pytest لاختبار تطبيقات وإضافات Flask. |
| 115 | pytest-mock | إضافة Pytest لاستخدام unittest.mock. |
| 116 | tox | أتمتة وتوحيد الاختبار في Python. |
| 117 | pre-commit | إطار عمل لإدارة وصيانة خطافات pre-commit متعددة اللغات. |
| 118 | black | منظم كود Python الذي لا يتساهل. |
| 119 | isort | أداة/مكتبة Python لترتيب الواردات أبجديًا. |
| 120 | flake8 | أداة لفرض دليل الأسلوب (pycodestyle, pyflakes, mccabe). |
| 121 | pylint | فاحص لجودة الكود المصدري والأخطاء في لغة برمجة Python. |
| 122 | mypy | كتابة ثابتة اختيارية لـ Python. |
| 123 | bandit | أداة مصممة للعثور على مشكلات أمان شائعة في كود Python. |
| 124 | safety | تحقق من التبعيات المثبتة لديك لمعرفة الثغرات الأمنية المعروفة. |
| 125 | poetry | إدارة تبعيات Python والتعبئة أصبحت سهلة. |
| 126 | pipenv | سير عمل تطوير Python للبشر. |
| 127 | setuptools-scm | إدارة إصداراتك باستخدام علامات scm. |
| 128 | twine | أدوات النشر على PyPI. |
| 129 | build | واجهة أمامية بسيطة وصحيحة لبناء Python. |
| 130 | cibuildwheel | بناء عجلات Python على منصات متعددة. |
| 131 | docker-py | عميل Python لـ Docker. |
| 132 | kubernetes | عميل Python لـ Kubernetes. |
| 133 | pykube | عميل Python خفيف الوزن لـ Kubernetes. |
| 134 | openshift | عميل REST لـ OpenShift. |
| 135 | fabric | تنفيذ أوامر SSH عالية المستوى والنشر. |
| 136 | ansible | أداة أتمتة لمهام تكنولوجيا المعلومات. |
| 137 | molecule | أداة تهدف إلى مساعدة المطورين والمختبرين في العمل مع أدوار ودفاتر تشغيل Ansible. |
| 138 | molecule-docker | دعم Docker لـ Molecule. |
| 139 | vagrant | أداة لبناء وصيانة بيئات تطوير برمجيات افتراضية قابلة للنقل. |
| 140 | virtualbox | واجهة برمجة تطبيقات Python لـ VirtualBox. |
| 141 | pyinstaller | تحويل برامج Python إلى ملفات تنفيذية مستقلة. |
| 142 | cx_Freeze | إنشاء ملفات تنفيذية من نصوص Python، بنفس أداء برامج C++. |
| 143 | nuitka | مترجم Python مع دعم كامل للغة وتوافق مع CPython. |
| 144 | cython | مترجم ثابت محسن لكل من Python و Cython. |
| 145 | numba | مترجم JIT لـ Python يعمل بشكل أفضل على الكود الذي يستخدم مصفوفات ودوال NumPy. |
| 146 | pypy | تنفيذ بديل لـ Python مع مترجم JIT. |
| 147 | micropython | تنفيذ Python خفيف وفعال للأنظمة المدمجة والبيئات المقيدة. |
| 148 | jupyter | الحوسبة التفاعلية عبر عشرات لغات البرمجة. |
| 149 | ipython | غلاف تفاعلي لـ Python. |
| 150 | notebook | دفتر Jupyter التفاعلي. |
| 151 | jupyterlab | JupyterLab هي واجهة المستخدم من الجيل التالي لمشروع Jupyter. |
| 152 | spyder | بيئة تطوير Python العلمية. |
| 153 | vscode | إضافة Visual Studio Code لـ Python. |
| 154 | pycharm | بيئة تطوير متكاملة لـ Python للمطورين. |
| 155 | rope | مكتبة إعادة هيكلة كود Python. |
| 156 | jedi | مكتبة الإكمال التلقائي والتحليل الثابت لـ Python. |
| 157 | python-language-server | خادم لغة Python. |
| 158 | pylsp | خادم Python LSP. |
| 159 | yapf | منظم كود Python آخر. |
| 160 | autopep8 | تنسيق كود Python تلقائيًا للتوافق مع دليل الأسلوب PEP 8. |
| 161 | yapf | منظم كود Python. |
| 162 | black | منظم كود لـ Python. |
| 163 | isort | منظم الواردات لـ Python. |
| 164 | nbconvert | تحويل الدفاتر إلى تنسيقات أخرى متنوعة. |
| 165 | nbformat | مكتبة لقراءة وكتابة ملفات دفتر Jupyter. |
| 166 | ipywidgets | عناصر واجهة HTML تفاعلية لدفاتر Jupyter ونواة IPython. |
| 167 | voila | تحويل دفاتر Jupyter إلى تطبيقات ويب مستقلة. |
| 168 | bokeh | رسوم بيانية وتطبيقات تفاعلية في المتصفح من Python. |
| 169 | plotly | مكتبة مفتوحة المصدر لإنشاء مخططات وخرائط تفاعلية. |
| 170 | altair | تصور إحصائي تصريحي في Python. |
| 171 | seaborn | مكتبة تصور البيانات الإحصائية بناءً على matplotlib. |
| 172 | ggplot | استخدام جماليات ggplot2 الخاصة بـ R لإنشاء رسوم بيانية في Python. |
| 173 | folium | إنشاء خرائط تفاعلية باستخدام Python. |
| 174 | basemap | الرسم على إسقاطات الخرائط في Python. |
| 175 | cartopy | حزمة Python لمعالجة البيانات الجغرافية المكانية لإنتاج الخرائط وتحليلات البيانات الجغرافية المكانية الأخرى. |
| 176 | shapely | معالجة وتحليل الكائنات الهندسية المستوية في Python. |
| 177 | geopandas | توسيع مكتبة تحليل البيانات pandas للعمل مع البيانات الجغرافية المكانية. |
| 178 | rasterio | الوصول إلى البيانات النقطية الجغرافية المكانية في Python. |
| 179 | fiona | واجهة برمجة تطبيقات OGR الأنيقة والرشقة لمبرمجي Python. |
| 180 | pyproj | واجهة Python لـ PROJ (مكتبة إسقاطات الخرائط وتحويلات الإحداثيات). |
| 181 | gdal | روابط مكتبة تجريد البيانات الجغرافية المكانية لـ Python. |
| 182 | opencv-python | روابط Python لمكتبة الرؤية الحاسوبية مفتوحة المصدر. |
| 183 | pillow | مكتبة تصوير Python. |
| 184 | scikit-image | مجموعة خوارزميات لمعالجة الصور في Python. |
| 185 | imageio | مكتبة لقراءة وكتابة مجموعة واسعة من تنسيقات بيانات الصور. |
| 186 | moviepy | تحرير الفيديو باستخدام Python. |
| 187 | vpython | وحدة رسوميات ثلاثية الأبعاد سهلة الاستخدام لـ Python. |
| 188 | mayavi | تصور البيانات العلمية والرسم ثلاثي الأبعاد في Python. |
| 189 | vtk | روابط Visualization Toolkit لـ Python. |
| 190 | pyvista | رسم ثلاثي الأبعاد وتحليل الشبكات من خلال واجهة مبسطة. |
| 191 | trimesh | استيراد وتصدير ومعالجة وتحليل وعرض الشبكات المثلثية. |
| 192 | vedo | وحدة Python للتصور العلمي وتحليل الكائنات ثلاثية الأبعاد والشبكات. |
| 193 | statsmodels | النمذجة الإحصائية والاقتصاد القياسي في Python. |
| 194 | patsy | وصف النماذج الإحصائية في Python باستخدام الصيغ الرمزية. |
| 195 | rpy2 | واجهة Python للغة البرمجة R. |
| 196 | lightgbm | إطار عمل تعزيز متدرج يعتمد على خوارزميات شجرة القرار. |
| 197 | xgboost | مكتبة تعزيز متدرج قابلة للتطوير ومرنة. |
| 198 | catboost | مكتبة تعزيز متدرج على أشجار القرار. |
| 199 | tensorflow | منصة مفتوحة المصدر شاملة للتعلم الآلي. |
| 200 | pytorch | موترات وشبكات عصبية ديناميكية في Python مع تسريع قوي لوحدة معالجة الرسومات. |

هذه القائمة تستند إلى ترتيبات شعبية تقريبية من إحصائيات تنزيل PyPI (اعتبارًا من أوائل عام 2023؛ يمكن أن تختلف البيانات الفعلية في الوقت الحقيقي). للحصول على أحدث الترتيبات، تحقق من إحصائيات PyPI الرسمية أو مستودعات مثل GitHub لأعداد النجوم. إذا كنت بحاجة إلى مزيد من التفاصيل حول أي حزمة، دعني أعلم!