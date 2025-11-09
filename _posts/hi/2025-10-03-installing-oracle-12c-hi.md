---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: उबुन्टू पर ओरेकल 12c की स्थापना
translated: true
type: note
---

### Ubuntu 22.04 x86_64 पर Tarball से Oracle Database 12c Release 1 (12.1.0.2 with patch 12.1.2?) इंस्टॉल करना

फ़ाइल `v12.1.2_linuxx64_server_dec.tar.gz` एक tarball प्रतीत होती है Oracle Database 12c Release 1 के लिए (संभवतः संस्करण 12.1.0.2 जिसमें 12.1.2 पैच बंडल है, सर्वर संस्करण, संभवतः "dec" का मतलब deconfigured है)। यह Oracle Database का एक पुराना संस्करण है (~2013-2014 से), और Oracle **Ubuntu को आधिकारिक रूप से सपोर्ट नहीं करता है**। Ubuntu 22.04 (जो आधुनिक लाइब्रेरीज जैसे glibc 2.35 का उपयोग करता है) पर इंस्टॉलेशन काम कर सकता है लेकिन संगतता समस्याओं के लिए वर्कअराउंड की आवश्यकता हो सकती है, जैसे लाइब्रेरी लिंकिंग या कर्नेल पैरामीटर। निर्भरताओं के साथ संभावित त्रुटियों की अपेक्षा करें—पहले एक VM में टेस्ट करें।

**चेतावनियाँ:**
- Oracle 12c एक्सटेंडेड सपोर्ट के लिए अंतिम समय (end-of-life) में है (2022 तक), इसलिए टेस्टिंग/प्रोडक्शन के लिए इसका उपयोग अपने जोखिम पर करें। प्रोडक्शन के लिए नए संस्करण जैसे 19c या 23ai पर विचार करें।
- आपको root/sudo एक्सेस की आवश्यकता होगी।
- न्यूनतम हार्डवेयर: 2 GB RAM (8 GB की सिफारिश की गई), 2 CPU कोर, सॉफ़्टवेयर के लिए 10 GB खाली डिस्क स्थान (DB के लिए अधिक)।
- आगे बढ़ने से पहले अपने सिस्टम का बैकअप लें।
- यदि यह tarball Oracle के आधिकारिक स्रोत से नहीं है, तो मैलवेयर से बचने के लिए इसकी अखंडता सत्यापित करें (जैसे, checksums)।

#### चरण 1: अपने सिस्टम को तैयार करें
1. **Ubuntu अपडेट करें**:
   ```
   sudo apt update && sudo apt upgrade -y
   ```

2. **आवश्यक निर्भरताएँ इंस्टॉल करें**:
   Oracle 12c को विशिष्ट लाइब्रेरीज की आवश्यकता होती है। उन्हें apt के माध्यम से इंस्टॉल करें:
   ```
   sudo apt install -y oracle-java8-installer bc binutils libaio1 libaio-dev libelf-dev libnuma-dev libstdc++6 unixodbc unixodbc-dev
   ```
   - यदि `oracle-java8-installer` उपलब्ध नहीं है (यह पुराने रेपो में है), तो Oracle का Java PPA जोड़ें या JDK 8 मैन्युअल रूप से डाउनलोड करें:
     ```
     sudo add-apt-repository ppa:webupd8team/java -y
     sudo apt update
     sudo apt install oracle-java8-installer -y
     ```
     इंस्टॉलेशन के दौरान लाइसेंस स्वीकार करें। JAVA_HOME सेट करें:
     ```
     echo 'export JAVA_HOME=/usr/lib/jvm/java-8-oracle' >> ~/.bashrc
     source ~/.bashrc
     ```

3. **Oracle यूजर और ग्रुप बनाएँ**:
   रूट या sudo के साथ रन करें:
   ```
   sudo groupadd -g 54321 oinstall
   sudo groupadd -g 54322 dba
   sudo useradd -u 54321 -g oinstall -G dba -s /bin/bash oracle
   sudo passwd oracle  # oracle यूजर के लिए एक पासवर्ड सेट करें
   ```

4. **कर्नेल पैरामीटर कॉन्फ़िगर करें**:
   `/etc/sysctl.conf` एडिट करें:
   ```
   sudo nano /etc/sysctl.conf
   ```
   ये लाइनें जोड़ें (अपने RAM/डिस्क के लिए एडजस्ट करें; ये न्यूनतम हैं):
   ```
   fs.file-max = 6815744
   kernel.sem = 250 32000 100 128
   kernel.shmmni = 4096
   kernel.shmall = 1073741824
   kernel.shmmax = 4398046511104
   kernel.panic_on_oops = 1
   net.core.rmem_default = 262144
   net.core.rmem_max = 4194304
   net.core.wmem_default = 262144
   net.core.wmem_max = 1048576
   fs.aio-max-nr = 1048576
   vm.swappiness = 0
   ```
   परिवर्तन लागू करें:
   ```
   sudo sysctl -p
   ```

5. **Oracle यूजर के लिए शेल लिमिट सेट करें**:
   `/etc/security/limits.conf` एडिट करें:
   ```
   sudo nano /etc/security/limits.conf
   ```
   जोड़ें:
   ```
   oracle soft nproc 2047
   oracle hard nproc 16384
   oracle soft nofile 1024
   oracle hard nofile 65536
   oracle soft stack 10240
   oracle hard stack 32768
   ```
   `/etc/pam.d/login` एडिट करें और जोड़ें:
   ```
   sudo nano /etc/pam.d/login
   ```
   Append करें: `session required pam_limits.so`

6. **डायरेक्टरीज़ बनाएँ**:
   ```
   sudo mkdir -p /u01/app/oracle/product/12.1.0/dbhome_1
   sudo mkdir -p /u01/app/oraInventory
   sudo chown -R oracle:oinstall /u01
   sudo chmod -R 775 /u01
   ```

7. **स्वैप स्पेस** (यदि RAM < 8 GB, तो स्वैप जोड़ें):
   2 GB RAM के लिए, 2 GB स्वैपफ़ाइल बनाएँ:
   ```
   sudo fallocate -l 2G /swapfile
   sudo chmod 600 /swapfile
   sudo mkswap /swapfile
   sudo swapon /swapfile
   echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
   ```

8. **फ़ायरवॉल/SElinux डिसेबल करें** (यदि सक्षम है):
   ```
   sudo ufw disable  # या पोर्ट 1521, 5500 कॉन्फ़िगर करें यदि आवश्यक हो
   sudo apt remove apparmor -y  # यदि AppArmor हस्तक्षेप करता है
   ```

#### चरण 2: Tarball Extract करें
oracle यूजर पर स्विच करें:
```
su - oracle
cd ~/Downloads  # या जहाँ भी फ़ाइल है
```
Extract करें (यह डेटाबेस होम डायरेक्टरी स्ट्रक्चर बनाता है):
```
tar -xzf v12.1.2_linuxx64_server_dec.tar.gz -C /u01/app/oracle/product/12.1.0/
```
- इससे `/u01/app/oracle/product/12.1.0/dbhome_1` फ़ाइलों जैसे `runInstaller` के साथ बनना चाहिए।
- यदि tarball एक अलग स्ट्रक्चर में एक्सट्रैक्ट होता है, तो पाथ को तदनुसार एडजस्ट करें (जैसे, `database/` डिर)।

#### चरण 3: इंस्टॉलर रन करें
अभी भी oracle यूजर के रूप में:
```
cd /u01/app/oracle/product/12.1.0/dbhome_1
./runInstaller
```
- GUI इंस्टॉलर लॉन्च होगा (यदि SSH है तो X11 फॉरवर्डिंग की आवश्यकता है; `ssh -X` का उपयोग करें या X11 सक्षम करें)।
- **इंस्टॉलेशन विकल्प**:
  - "Create and configure a database software only" या "Single instance database installation" (सर्वर एडिशन के लिए) चुनें।
  - ORACLE_HOME: `/u01/app/oracle/product/12.1.0/dbhome_1`
  - इन्वेंटरी: `/u01/app/oraInventory`
  - यदि यह सिर्फ सॉफ़्टवेयर है (कोई DB क्रिएशन नहीं), तो "Install database software only" चुनें।
- विज़ार्ड का पालन करें: जहाँ संभव हो डिफ़ॉल्ट स्वीकार करें, लेकिन SYS/SYSTEM के लिए पासवर्ड सेट करें।
- शुरुआत में किसी भी "prereq" चेतावनी को नज़रअंदाज़ करें—यदि आवश्यक हो तो पोस्ट-इंस्टॉल ठीक करें।

यदि GUI फेल हो जाता है (जैसे, DISPLAY एरर), साइलेंट इंस्टॉल रन करें:
```
./runInstaller -silent -responseFile /path/to/responsefile.rsp
```
आपको एक रिस्पांस फ़ाइल (नमूना एक्सट्रैक्टेड डिर में, जैसे `db_install.rsp`) तैयार करनी होगी। इसे अपनी सेटिंग्स (ORACLE_HOME, आदि) के साथ एडिट करें और रन करें।

#### चरण 4: पोस्ट-इंस्टॉलेशन
1. **root.sh रन करें** (रूट के रूप में):
   ```
   sudo /u01/app/oraInventory/orainstRoot.sh
   sudo /u01/app/oracle/product/12.1.0/dbhome_1/root.sh
   ```

2. **एनवायरनमेंट वेरिएबल्स सेट करें** (oracle यूजर के लिए, `~/.bash_profile` में जोड़ें):
   ```
   export ORACLE_HOME=/u01/app/oracle/product/12.1.0/dbhome_1
   export PATH=$ORACLE_HOME/bin:$PATH
   export ORACLE_SID=orcl  # अपने SID में बदलें
   export LD_LIBRARY_PATH=$ORACLE_HOME/lib:/lib:/usr/lib
   export CLASSPATH=$ORACLE_HOME/jlib:$ORACLE_HOME/rdbms/jlib
   ```
   ```
   source ~/.bash_profile
   ```

3. **एक डेटाबेस बनाएँ** (यदि इंस्टॉल के दौरान नहीं बनाया गया है):
   ```
   dbca  # Database Configuration Assistant (GUI/silent)
   ```
   या मैनुअल क्रिएशन के लिए SQL*Plus का उपयोग करें।

4. **सर्विसेज़ स्टार्ट/स्टॉप करें**:
   ```
   sqlplus / as sysdba
   STARTUP;  # या shutdown
   ```
   ऑटो-स्टार्ट के लिए systemd में जोड़ें (`/etc/systemd/system/oracle.service` बनाएँ जिसमें `dbstart` के लिए exec हो)।

#### Ubuntu 22.04 पर सामान्य समस्याओं का समाधान
- **Glibc/निर्भरता त्रुटियाँ**: Oracle 12c glibc <=2.17 की अपेक्षा करता है। Ubuntu 22.04 में 2.35 है—चेक करने के लिए `ldd` का उपयोग करें, या कॉम्पैट लिब्स इंस्टॉल करें:
  ```
  sudo apt install libc6:i386 libncurses5:i386 libstdc++6:i386
  ```
  यदि लिंकर एरर हैं, तो `LD_PRELOAD` सेट करें या Oracle Linux वाले Docker कंटेनर का उपयोग करें।
- **Java/Display समस्याएँ**: सुनिश्चित करें कि JDK 8 सेट है (`java -version` को 1.8 दिखाना चाहिए)। हेडलेस के लिए: `export DISPLAY=:0`।
- **मेमोरी खत्म**: ulimit या RAM बढ़ाएँ। यदि आवश्यक हो तो `runInstaller` पैरामीटर एडिट करें।
- **पैच 12.1.2**: यदि बंडल नहीं है, तो My Oracle Support से डाउनलोड करें और इंस्टॉल के बाद `opatch` के साथ अप्लाई करें।
- **लॉग**: त्रुटियों के लिए `/u01/app/oraInventory/logs/installActions*.log` चेक करें।
- **संगतता फिक्स**: कुछ यूजर्स लिब्स को सिमलिंक करते हैं (जैसे, `sudo ln -s /lib/x86_64-linux-gnu/libpthread.so.0 /u01/app/oracle/product/12.1.0/dbhome_1/lib/libpthread_nonshared.a`—प्रति एरर रिसर्च करें)।

#### सत्यापन
- `sqlplus / as sysdba` रन करें और `SELECT * FROM v$version;` एक्ज़िक्यूट करें।
- लिसनर: `lsnrctl start`।

यदि आपको विशिष्ट त्रुटियाँ मिलती हैं, तो अधिक मदद के लिए लॉग आउटपुट प्रदान करें। आधिकारिक (हालाँकि RHEL-केंद्रित) डॉक्स के लिए, Oracle का 12c इंस्टॉल गाइड देखें। यदि यह किसी अलग प्रोडक्ट (DB नहीं) के लिए है, तो tarball की सामग्री स्पष्ट करें!