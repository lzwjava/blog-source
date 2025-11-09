---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: वेबस्फीयर एप्लिकेशन सर्वर में जायथन
translated: true
type: note
---

### IBM WebSphere Application Server में Jython का उपयोग

नोट: "jPython" Jython को संदर्भित करता है, जो Python का एक implementation है जो Java Virtual Machine (JVM) पर चलता है। इसका उपयोग आमतौर पर WebSphere में administrative scripting के लिए किया जाता है और इसे deployed applications में भी integrated किया जा सकता है। WebSphere Application Server (WAS) Jython को (`<WAS_HOME>/optionalLibraries/jython` के अंतर्गत) bundle करता है (आमतौर पर WAS version के आधार पर version 2.1 या बाद का), इसलिए आमतौर पर अलग से installation की आवश्यकता नहीं होती है। नीचे, मैं दो प्राथमिक use cases को कवर करूंगा: administrative tasks और applications में runtime use।

#### 1. wsadmin के साथ Administrative Scripting
WebSphere में Jython का उपयोग करने का सबसे आम तरीका server management tasks जैसे applications deploy करना, servers start/stop करना, resources configure करना, और installed apps की सूची बनाना है। यह `wsadmin` टूल के माध्यम से किया जाता है, जो preferred scripting language के रूप में Jython को सपोर्ट करता है (deprecated Jacl पर)।

**पूर्वापेक्षाएँ:**
- सुनिश्चित करें कि WebSphere server चल रहा है।
- `wsadmin` को `<WAS_HOME>/bin/wsadmin.sh` (Linux/Unix) या `wsadmin.bat` (Windows) में locate करें।
- Jython पहले से bundled है; newer features (जैसे, Python 2.5+ syntax) के लिए, आपको custom classpath के माध्यम से upgrade करने की आवश्यकता हो सकती है (नीचे advanced notes देखें)।

**Jython Script चलाने के मूल चरण:**
1. अपने code के साथ एक Jython script file (जैसे, `example.py`) बनाएँ। WebSphere-specific operations के लिए AdminConfig, AdminControl, और AdminApp objects का उपयोग करें।
   
   सभी installed applications की सूची बनाने के लिए example script (`listApps.py`):
   ```
   # सभी applications की सूची बनाएं
   apps = AdminApp.list()
   print("Installed Applications:")
   for app in apps.splitlines():
       if app.strip():
           print(app.strip())
   AdminConfig.save()  # वैकल्पिक: config changes save करें
   ```

2. Script को `wsadmin` का उपयोग करके चलाएँ:
   - SOAP के माध्यम से connect करें (remote के लिए default):  
     ```
     wsadmin.sh -lang jython -f listApps.py -host <hostname> -port <soap_port> -user <admin_user> -password <admin_pass>
     ```
   - local के लिए (कोई host/port नहीं):  
     ```
     wsadmin.sh -lang jython -f listApps.py
     ```
   - Example output: Apps को `DefaultApplication` जैसे list करता है।

3. Interactive mode (REPL) के लिए:  
   ```
   wsadmin.sh -lang jython
   ```
   फिर सीधे Jython commands टाइप करें, जैसे, `print AdminApp.list()`।

**सामान्य उदाहरण:**
- **एक EAR/WAR Deploy करें:** `deployApp.py` बनाएँ:
  ```
  appName = 'MyApp'
  earPath = '/path/to/MyApp.ear'
  AdminApp.install(earPath, '[-appname ' + appName + ' -server server1]')
  AdminConfig.save()
  print('Deployed ' + appName)
  ```
  चलाएँ: `wsadmin.sh -lang jython -f deployApp.py`.

- **Server Start/Stop करें:**  
  ```
  server = AdminControl.completeObjectName('type=Server,process=server1,*')
  AdminControl.invoke(server, 'start')  # या 'stop'
  ```

- **Jython Version निर्दिष्ट करें (यदि आवश्यक हो):** Jython 2.1 के लिए स्पष्ट रूप से:  
  `wsadmin.sh -usejython21 true -f script.py`. Custom versions के लिए, classpath में add करें: `-wsadmin_classpath /path/to/jython.jar`.

**सुझाव:**
- Command help के लिए `AdminConfig.help('object_type')` का उपयोग करें।
- Scripts को CI/CD (जैसे, Jenkins) में automated किया जा सकता है by calling `wsadmin` in batch files।
- Thin client के लिए (पूर्ण WAS install नहीं): IBM से client jars download करें और classpath सेट करें।

#### 2. Deployed Applications में Jython का उपयोग
WebSphere पर चल रहे Java application (जैसे, servlet या EJB) के भीतर Jython code को execute करने के लिए, application की classpath में Jython runtime (jython.jar) को शामिल करें। यह Python scripts को embed करने या Jython को scripting engine के रूप में उपयोग करने की अनुमति देता है। यदि bundled version outdated है तो official Jython site से latest jython.jar download करें।

दो मुख्य methods हैं: **Classpath** (server-wide) या **Shared Library** (apps में reusable)।

**Method 1: Classpath (JVM में Direct Addition)**
1. WebSphere host पर एक accessible path में `jython.jar` save करें (जैसे, `/opt/IBM/WebSphere/AppServer/profiles/AppSrv01/mylibs/jython.jar`)।
2. WebSphere Admin Console में log in करें।
3. **Servers > Server Types > WebSphere application servers > [आपका Server]** पर navigate करें।
4. **Java and Process Management > Process definition > Java Virtual Machine > Classpath** पर जाएं।
5. `jython.jar` का full path add करें (जैसे, `/opt/.../jython.jar`)।
6. **Generic JVM arguments** में, Python path add करें:  
   `-Dpython.path=/opt/.../jython.jar/Lib` (Jython की standard library की ओर इशारा करता है)।
7. **OK** क्लिक करें, configuration save करें, और server restart करें।
8. यदि clustered environment में है तो nodes synchronize करें (via **System administration > Nodes > Synchronize**)।
9. अपने Java code में, Jython scripts चलाने के लिए `org.python.util.PythonInterpreter` का उपयोग करें:
   ```
   import org.python.util.PythonInterpreter;
   PythonInterpreter interpreter = new PythonInterpreter();
   interpreter.exec("print('Hello from Jython in WebSphere!')");
   ```

**Method 2: Shared Library (Multiple Apps के लिए Recommended)**
1. `jython.jar` को एक shared directory में रखें (जैसे, `/shared/libs/jython.jar`)।
2. Admin Console में: **Environment > Shared libraries > [Scope: Server या Cell] > New**।
3. एक name दर्ज करें (जैसे, `JythonLib`), **Use a native library directory** चेक करें, और **Classpath** को `/shared/libs/jython.jar` पर सेट करें।
4. Save करें।
5. किसी specific application के लिए: **Applications > Application Types > WebSphere enterprise applications > [आपका App] > Reference shared libraries**।
6. **Shared library references** के अंतर्गत, **Add** क्लिक करें, `JythonLib` चुनें, और **Classpath** को match करने के लिए सेट करें।
7. Save करें, app को update करें (यदि आवश्यक हो तो restart करें), और nodes synchronize करें।
8. Code में Classpath method के अनुसार reference करें।

**Apps के लिए सुझाव:**
- Servlet-based Jython apps के लिए, Python handlers के लिए PyServlet (Jython में included) का उपयोग करें।
- Dev environment में test करें; classpath issues के लिए logs monitor करें।
- यदि newer Jython (जैसे, 2.7) का उपयोग कर रहे हैं, तो Java 8+ compatibility सुनिश्चित करें।

#### उन्नत नोट्स
- **Version Compatibility:** WAS 9.x Jython 2.7+ का उपयोग करता है। Upgrades के लिए, bundled jar को replace करें लेकिन thoroughly test करें।
- **Error Handling:** Scripts में, `try: ... except Exception as e: print(e)` का उपयोग करें।
- **IDE Support:** Jython/wsadmin scripts को debug करने के लिए IBM Rational Application Developer (RAD) या Eclipse with WebSphere plugins का उपयोग करें।
- **Resources:** पूर्ण tutorials के लिए, पुस्तक *WebSphere Application Server Administration Using Jython* या IBM के wsadmin docs देखें।

यदि यह आपके exact scenario से मेल नहीं खाता (जैसे, specific WAS version या use case), तो tailored advice के लिए अधिक details प्रदान करें।

**संदर्भ:**  
- [Using wsadmin scripting with Jython (IBM Docs)](https://www.ibm.com/docs/en/was/9.0.5?topic=scripting-using-wsadmin-jython)  
- [Deploying Jython on WebSphere (Oracle Guide)](https://docs.oracle.com/en/applications/jd-edwards/cross-product/9.2/eotos/deploying-jython-on-ais-server-on-ibm-websphere-application.html)  
- [WebSphere Jython Integration (Stack Overflow)](https://stackoverflow.com/questions/25187577/will-the-ibm-websphere-application-server-run-the-python-jython-script-without-p)  
- [Jython Wiki on WebSphere](https://wiki.python.org/jython/WebSphere)  
- [Deploy App with Jython Example](https://jobhunterssite.wordpress.com/2016/05/12/deploy-an-application-in-websphere-using-jython-automation/)