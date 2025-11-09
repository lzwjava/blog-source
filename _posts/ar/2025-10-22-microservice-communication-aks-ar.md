---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: تهيئة اتصال الخدمات المصغرة في خدمة حاويات Azure
translated: true
type: note
---

### تكوين الاتصال بين الخدمات المصغرة في خدمة Azure Kubernetes (AKS)

في خدمة Azure Kubernetes (AKS)، يتم عادةً نشر الخدمات المصغرة كـ **Pods** تُدار بواسطة **Deployments**. لتمكينها من التواصل مع بعضها البعض (مثل قيام الخدمة A باستدعاء الخدمة B)، تستخدم **خدمات Kubernetes** لتجميل عناوين الـ IP الديناميكية للـ Pods وتوفير نقاط نهاية ثابتة. يتم ذلك عبر الشبكة الداخلية، مستفيدًا من دقة DNS المدمجة في Kubernetes. إليك دليل خطوة بخطوة لتكوين وتنفيذ هذا.

#### 1. **نشر الخدمات المصغرة كـ Deployments**
   تعمل كل خدمة مصغرة في Pod (أو مجموعة من Pods للتوسع). استخدم Deployment لإدارتها.

   مثال YAML لنشر خدمة مصغرة بسيطة (`service-a-deployment.yaml`):
   ```yaml
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: service-a
     namespace: default  # أو النطاق المخصص الخاص بك
   spec:
     replicas: 3  # قم بالتوسع حسب الحاجة
     selector:
       matchLabels:
         app: service-a
     template:
       metadata:
         labels:
           app: service-a
       spec:
         containers:
         - name: service-a
           image: your-registry/service-a:latest  # على سبيل المثال، صورة ACR أو Docker Hub
           ports:
           - containerPort: 8080  # المنفذ الذي تستمع عليه التطبيق
   ```

   طبقها:
   ```
   kubectl apply -f service-a-deployment.yaml
   ```

   كرر العملية للخدمات الأخرى (مثل `service-b`).

#### 2. **عرض الخدمات المصغرة باستخدام Services**
   أنشئ **ClusterIP Service** لكل خدمة مصغرة. هذا النوع مخصص للاتصال الداخلي فقط (غير معروض خارج الكتلة). يقوم بموازنة حركة المرور إلى الـ Pods ويوفر اسم DNS.

   مثال YAML للخدمة A (`service-a-service.yaml`):
   ```yaml
   apiVersion: v1
   kind: Service
   metadata:
     name: service-a
     namespace: default
   spec:
     selector:
       app: service-a  # يطابق تسميات الـ Deployment
     ports:
     - protocol: TCP
       port: 80  # منفذ الخدمة (ما يستخدمه المتصلون)
       targetPort: 8080  # منفذ حاوية الـ Pod
     type: ClusterIP  # داخلي فقط
   ```

   طبقها:
   ```
   kubectl apply -f service-a-service.yaml
   ```

   افعل نفس الشيء للخدمة B. الآن، يمكن للـ Pods الوصول إلى بعضها البعض عبر اسم DNS الخاص بالخدمة.

#### 3. **كيف تتصل الخدمات المصغرة ببعضها البعض**
   - **الاكتشاف القائم على DNS**: يحدد DNS الخاص بـ Kubernetes أسماء الخدمات تلقائيًا. من Pod في الخدمة A، استدعِ الخدمة B باستخدام:
     - `<service-name>.<namespace>.svc.cluster.local` (مؤهل بالكامل، مثل `service-b.default.svc.cluster.local`).
     - أو فقط `<service-name>` إذا كان في نفس النطاق (مثل `service-b`).
   - **مكالمات HTTP/gRPC**: في كود التطبيق الخاص بك، قم بطلبات إلى `http://service-b:80/endpoint`. يتعامل Kubernetes مع موازنة الحمل والتعافي من الأعطال.
     - مثال في Python (باستخدام requests):
       ```python
       import requests
       response = requests.get("http://service-b:80/api/data")
       ```
     - بالنسبة لـ gRPC، استخدم نفس اسم المضيف مع منفذ gRPC.
   - **تعيين المنفذ**: يتم تعيين منفذ الخدمة (مثل 80) إلى منفذ الهدف للـ Pod (مثل 8080). لا حاجة لتشفير عناوين IP الـ Pods بصعوبة—فهي تتغير عند إعادة التشغيل.

   اختبر الاتصال من Pod:
   ```
   kubectl exec -it <pod-name-in-service-a> -- curl http://service-b:80/health
   ```

#### 4. **خيارات التكوين المتقدمة**
   - **النطاقات**: انشر الخدمات في نطاقات مختلفة للعزل. استخدم DNS الكامل (مثل `service-b.other-ns.svc.cluster.local`).
   - **سياسات الشبكة**: قم بتأمين الاتصال باستخدام سياسات Calico أو Azure CNI للسماح/منع حركة المرور بين الخدمات.
     مثال على سياسة تسمح للخدمة A باستدعاء الخدمة B:
     ```yaml
     apiVersion: networking.k8s.io/v1
     kind: NetworkPolicy
     metadata:
       name: allow-service-a-to-b
     spec:
       podSelector:
         matchLabels:
           app: service-b
       policyTypes:
       - Ingress
       ingress:
       - from:
         - podSelector:
             matchLabels:
               app: service-a
         ports:
         - protocol: TCP
           port: 80
     ```
   - **شبكة الخدمات (مثل Istio أو Linkerd)**: للإنتاج، أضف شبكة للملاحظة، وmTLS، وإدارة حركة المرور. قم بالتثبيت عبر Helm على AKS، ثم حقن وكلاء sidecar في الـ Pods.
   - **الوصول الخارجي (إذا لزم الأمر)**: استخدم خدمات **LoadBalancer** أو **Ingress** للمكالمات الصادرة، ولكن التزم بـ ClusterIP للداخلية.

#### 5. **أفضل الممارسات**
   - استخدم **متغيرات البيئة** أو **ConfigMaps** لحقن أسماء DNS للخدمة في التطبيقات ديناميكيًا.
   - راقب باستخدام Azure Monitor لـ AKS لتتبع حركة المرور بين الخدمات.
   - قم بالتوسع الأفقي باستخدام Horizontal Pod Autoscaler (HPA) بناءً على وحدة المعالجة المركزية/الذاكرة.
   - للتكاملات المحددة في Azure، استخدم Azure Container Registry (ACR) للصور و Azure AD للمصادقة.

يضمن هذا الإعداد اتصالاً موثوقًا وقابل للتوسع دون اقتران شديد. ابدأ بالخدمات الأساسية، ثم أضف الأمان/شبكة الخدمات حسب الحاجة.

[نظرة عامة على شبكات AKS](https://learn.microsoft.com/en-us/azure/aks/concepts-network)  
[توثيق خدمات Kubernetes](https://kubernetes.io/docs/concepts/services-networking/service/)  
[برنامج تعليمي للخدمات المصغرة في AKS](https://learn.microsoft.com/en-us/azure/aks/tutorial-kubernetes-deploy-cluster)