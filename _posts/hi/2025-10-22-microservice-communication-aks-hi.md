---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: एकेएस में माइक्रोसर्विस संचार विन्यास
translated: true
type: note
---

### Azure Kubernetes Service (AKS) में माइक्रोसर्विसेज के बीच कम्युनिकेशन कॉन्फ़िगर करना

Azure Kubernetes Service (AKS) में, माइक्रोसर्विसेज आमतौर पर **Deployments** द्वारा प्रबंधित **Pods** के रूप में तैनात की जाती हैं। उन्हें एक-दूसरे के साथ संचार करने में सक्षम बनाने के लिए (जैसे, सर्विस A द्वारा सर्विस B को कॉल करना), आप Pods के डायनामिक IPs को अमूर्तित करने और स्थिर एंडपॉइंट्स प्रदान करने के लिए **Kubernetes Services** का उपयोग करते हैं। यह आंतरिक नेटवर्किंग के माध्यम से किया जाता है, जो Kubernetes के अंतर्निहित DNS रिज़ॉल्यूशन का लाभ उठाता है। इसे कॉन्फ़िगर और लागू करने के लिए एक चरण-दर-चरण मार्गदर्शिका यहां दी गई है।

#### 1. **अपनी माइक्रोसर्विसेज को Deployments के रूप में तैनात करना**
   प्रत्येक माइक्रोसर्विस एक Pod (या स्केलिंग के लिए Pods के सेट) में चलती है। उन्हें प्रबंधित करने के लिए एक Deployment का उपयोग करें।

   एक सरल माइक्रोसर्विस Deployment के लिए उदाहरण YAML (`service-a-deployment.yaml`):
   ```yaml
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: service-a
     namespace: default  # या आपका कस्टम namespace
   spec:
     replicas: 3  # आवश्यकतानुसार स्केल करें
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
           image: your-registry/service-a:latest  # उदाहरण: ACR या Docker Hub इमेज
           ports:
           - containerPort: 8080  # वह पोर्ट जिस पर आपका ऐप सुनता है
   ```

   इसे लागू करें:
   ```
   kubectl apply -f service-a-deployment.yaml
   ```

   अन्य सेवाओं (जैसे, `service-b`) के लिए दोहराएं।

#### 2. **Services के साथ माइक्रोसर्विसेज को एक्सपोज़ करना**
   प्रत्येक माइक्रोसर्विस के लिए एक **ClusterIP Service** बनाएं। यह प्रकार केवल आंतरिक संचार के लिए है (क्लस्टर के बाहर एक्सपोज़्ड नहीं)। यह Pods पर ट्रैफ़िक को लोड-बैलेंस करता है और एक DNS नाम प्रदान करता है।

   सर्विस A के लिए उदाहरण YAML (`service-a-service.yaml`):
   ```yaml
   apiVersion: v1
   kind: Service
   metadata:
     name: service-a
     namespace: default
   spec:
     selector:
       app: service-a  # Deployment लेबल से मेल खाता है
     ports:
     - protocol: TCP
       port: 80  # सर्विस पोर्ट (कॉलर क्या उपयोग करते हैं)
       targetPort: 8080  # Pod का कंटेनर पोर्ट
     type: ClusterIP  # केवल आंतरिक
   ```

   इसे लागू करें:
   ```
   kubectl apply -f service-a-service.yaml
   ```

   सर्विस B के लिए भी ऐसा ही करें। अब, Pods सर्विस के DNS नाम के माध्यम से एक-दूसरे तक पहुंच सकते हैं।

#### 3. **माइक्रोसर्विसेज एक-दूसरे को कैसे कॉल करती हैं**
   - **DNS-आधारित डिस्कवरी**: Kubernetes DNS स्वचालित रूप से सर्विस नामों को रिज़ॉल्व करता है। सर्विस A के एक Pod से, सर्विस B को इसका उपयोग करके कॉल करें:
     - `<service-name>.<namespace>.svc.cluster.local` (पूरी तरह से योग्य, उदाहरण: `service-b.default.svc.cluster.local`)।
     - या फिर सिर्फ़ `<service-name>` अगर एक ही namespace में है (उदाहरण: `service-b`)।
   - **HTTP/gRPC कॉल्स**: अपने ऐप कोड में, `http://service-b:80/endpoint` पर अनुरोध करें। Kubernetes लोड बैलेंसिंग और फेलओवर को संभालता है।
     - Python में उदाहरण (requests का उपयोग करके):
       ```python
       import requests
       response = requests.get("http://service-b:80/api/data")
       ```
     - gRPC के लिए, gRPC पोर्ट के साथ उसी होस्टनाम का उपयोग करें।
   - **पोर्ट मैपिंग**: सर्विस पोर्ट (उदाहरण: 80) Pod के टारगेट पोर्ट (उदाहरण: 8080) पर मैप होता है। Pod IPs को हार्डकोड करने की आवश्यकता नहीं है—वे रीस्टार्ट पर बदल जाते हैं।

   एक Pod से कनेक्टिविटी का परीक्षण करें:
   ```
   kubectl exec -it <pod-name-in-service-a> -- curl http://service-b:80/health
   ```

#### 4. **उन्नत कॉन्फ़िगरेशन विकल्प**
   - **Namespaces**: अलगाव के लिए सेवाओं को अलग-अलग namespaces में तैनात करें। पूर्ण DNS (उदाहरण: `service-b.other-ns.svc.cluster.local`) का उपयोग करें।
   - **नेटवर्क पॉलिसीज़**: सेवाओं के बीच ट्रैफ़िक की अनुमति देने/अस्वीकार करने के लिए Calico या Azure CNI पॉलिसीज़ के साथ संचार को सुरक्षित करें।
     सर्विस A को सर्विस B को कॉल करने की अनुमति देने वाली उदाहरण पॉलिसी:
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
   - **सर्विस मेश (जैसे, Istio या Linkerd)**: प्रोडक्शन के लिए, ऑब्ज़र्वेबिलिटी, mTLS, और ट्रैफ़िक मैनेजमेंट के लिए एक मेश जोड़ें। AKS पर Helm के माध्यम से इंस्टॉल करें, फिर Pods में साइडकार प्रॉक्सी इंजेक्ट करें।
   - **एक्सटर्नल एक्सेस (अगर आवश्यक हो)**: आउटबाउंड कॉल्स के लिए **LoadBalancer** या **Ingress** Services का उपयोग करें, लेकिन आंतरिक के लिए ClusterIP पर ही बने रहें।

#### 5. **बेस्ट प्रैक्टिसेज़**
   - सेवा DNS नामों को ऐप्स में डायनामिक रूप से इंजेक्ट करने के लिए **एनवायरनमेंट वेरिएबल्स** या **ConfigMaps** का उपयोग करें।
   - इंटर-सर्विस ट्रैफ़िक को ट्रैक करने के लिए Azure Monitor for AKS के साथ मॉनिटर करें।
   - CPU/मेमोरी के आधार पर Horizontal Pod Autoscaler (HPA) के साथ क्षैतिज रूप से स्केल करें।
   - Azure-विशिष्ट इंटीग्रेशन के लिए, इमेजेज़ के लिए Azure Container Registry (ACR) और ऑथ के लिए Azure AD का उपयोग करें।

यह सेटअप टाइट कपलिंग के बिना विश्वसनीय, स्केलेबल संचार सुनिश्चित करता है। बुनियादी Services से शुरुआत करें, फिर आवश्यकतानुसार सुरक्षा/मेश को लेयर करें।

[AKS नेटवर्किंग अवलोकन](https://learn.microsoft.com/en-us/azure/aks/concepts-network)  
[Kubernetes Services डॉक्यूमेंटेशन](https://kubernetes.io/docs/concepts/services-networking/service/)  
[AKS माइक्रोसर्विसेज ट्यूटोरियल](https://learn.microsoft.com/en-us/azure/aks/tutorial-kubernetes-deploy-cluster)