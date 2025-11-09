---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: تثبيت أوراكل 12c على أوبونتو
translated: true
type: note
---

### تثبيت Oracle Database 12c الإصدار 1 (12.1.0.2 مع التصحيح 12.1.2؟) من أرشيف Tarball على Ubuntu 22.04 x86_64

يبدو أن الملف `v12.1.2_linuxx64_server_dec.tar.gz` هو أرشيف tarball خاص بـ Oracle Database 12c الإصدار 1 (على الأرجح الإصدار 12.1.0.2 مع حزمة التصحيح 12.1.2، إصدار الخادم، وربما "dec" تشير إلى Deconfigured). هذا إصدار قديم من Oracle Database (من حوالي 2013-2014)، وشركة Oracle **لا تدعم Ubuntu رسميًا**. قد يعمل التثبيت على Ubuntu 22.04 (الذي يستخدم مكتبات حديثة مثل glibc 2.35) ولكنه قد يتطلب حلولاً بديلة لمشاكل التوافق، مثل ربط المكتبات أو معلمات النواة. توقع أخطاء محتملة في التبعيات — اختبر في جهاز ظاهري أولاً.

**تحذيرات:**
- الدعم الممتد لـ Oracle 12c قد انتهى (اعتبارًا من 2022)، لذا استخدمه للاختبار/الإنتاج على مسؤوليتك الخاصة. فكر في استخدام إصدارات أحدث مثل 19c أو 23ai للإنتاج.
- ستحتاج إلى صلاحيات root/sudo.
- الحد الأدنى للأجهزة: 2 جيجابايت من الذاكرة العشوائية (يُوصى بـ 8 جيجابايت)، نواتي معالج، و 10 جيجابايت مساحة حرة على القرص للبرنامج (والمزيد لقاعدة البيانات).
- قم بعمل نسخة احتياطية لنظامك قبل المتابعة.
- إذا لم يكن أرشيف tarball هذا من مصدر Oracle الرسمي، فتحقق من سلامته (على سبيل المثال، باستخدام checksums) لتجنب البرمجيات الخبيثة.

#### الخطوة 1: إعداد نظامك
1. **تحديث Ubuntu**:
   ```
   sudo apt update && sudo apt upgrade -y
   ```

2. **تثبيت التبعيات المطلوبة**:
   تحتاج Oracle 12c إلى مكتبات محددة. قم بتثبيتها عبر apt:
   ```
   sudo apt install -y oracle-java8-installer bc binutils libaio1 libaio-dev libelf-dev libnuma-dev libstdc++6 unixodbc unixodbc-dev
   ```
   - إذا لم يكن `oracle-java8-installer` متاحًا (موجود في مستودعات أقدم)، أضف PPA جافا الخاص بـ Oracle أو قم بتنزيل JDK 8 يدويًا:
     ```
     sudo add-apt-repository ppa:webupd8team/java -y
     sudo apt update
     sudo apt install oracle-java8-installer -y
     ```
     اقبل الترخيص أثناء التثبيت. عيّن `JAVA_HOME`:
     ```
     echo 'export JAVA_HOME=/usr/lib/jvm/java-8-oracle' >> ~/.bashrc
     source ~/.bashrc
     ```

3. **إنشاء مستخدم Oracle والمجموعات**:
   قم بالتشغيل كـ root أو باستخدام sudo:
   ```
   sudo groupadd -g 54321 oinstall
   sudo groupadd -g 54322 dba
   sudo useradd -u 54321 -g oinstall -G dba -s /bin/bash oracle
   sudo passwd oracle  # عيّن كلمة مرور لمستخدم oracle
   ```

4. **تكوين معلمات النواة**:
   قم بتحرير `/etc/sysctl.conf`:
   ```
   sudo nano /etc/sysctl.conf
   ```
   أضف هذه الأسطر (اضبطها بناءً على ذاكرتك العشوائية/القرص؛ هذه هي الحدود الدنيا):
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
   طبق التغييرات:
   ```
   sudo sysctl -p
   ```

5. **تعيين حدود Shell لمستخدم Oracle**:
   قم بتحرير `/etc/security/limits.conf`:
   ```
   sudo nano /etc/security/limits.conf
   ```
   أضف:
   ```
   oracle soft nproc 2047
   oracle hard nproc 16384
   oracle soft nofile 1024
   oracle hard nofile 65536
   oracle soft stack 10240
   oracle hard stack 32768
   ```
   قم بتحرير `/etc/pam.d/login` وأضف:
   ```
   sudo nano /etc/pam.d/login
   ```
   ألحق: `session required pam_limits.so`

6. **إنشاء المجلدات**:
   ```
   sudo mkdir -p /u01/app/oracle/product/12.1.0/dbhome_1
   sudo mkdir -p /u01/app/oraInventory
   sudo chown -R oracle:oinstall /u01
   sudo chmod -R 775 /u01
   ```

7. **مساحة المبادلة** (إذا كانت الذاكرة العشوائية < 8 جيجابايت، أضف مبادلة):
   للذاكرة العشوائية 2 جيجابايت، أنشئ ملف مبادلة بحجم 2 جيجابايت:
   ```
   sudo fallocate -l 2G /swapfile
   sudo chmod 600 /swapfile
   sudo mkswap /swapfile
   sudo swapon /swapfile
   echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
   ```

8. **تعطيل الجدار الناري/SElinux** (إذا كان مفعلًا):
   ```
   sudo ufw disable  # أو قم بتكوين المنافذ 1521, 5500 إذا لزم الأمر
   sudo apt remove apparmor -y  # إذا كان AppArmor يتعارض
   ```

#### الخطوة 2: استخراج أرشيف Tarball
انتقل إلى مستخدم oracle:
```
su - oracle
cd ~/Downloads  # أو أينما يوجد الملف
```
استخرج (هذا ينشئ هيكل مجلد قاعدة البيانات الرئيسي):
```
tar -xzf v12.1.2_linuxx64_server_dec.tar.gz -C /u01/app/oracle/product/12.1.0/
```
- من المفترض أن ينشئ هذا `/u01/app/oracle/product/12.1.0/dbhome_1` مع ملفات مثل `runInstaller`.
- إذا كان أرشيف tarball يستخرج إلى هيكل مختلف، فاضبط المسارات وفقًا لذلك (مثل مجلد `database/`).

#### الخطوة 3: تشغيل برنامج التثبيت
لا يزال كمستخدم oracle:
```
cd /u01/app/oracle/product/12.1.0/dbhome_1
./runInstaller
```
- سيعمل مثبت واجهة المستخدم الرسومية (يتطلب توجيه X11 إذا كنت تستخدم SSH؛ استخدم `ssh -X` أو فعّل X11).
- **خيارات التثبيت**:
  - اختر "Create and configure a database software only" أو "Single instance database installation" (لإصدار الخادم).
  - ORACLE_HOME: `/u01/app/oracle/product/12.1.0/dbhome_1`
  - Inventory: `/u01/app/oraInventory`
  - إذا كان البرنامج فقط (بدون إنشاء قاعدة بيانات)، اختر "Install database software only".
- اتبع المعالج: اقبل الإعدادات الافتراضية حيثما أمكن، ولكن عيّن كلمات المرور لـ SYS/SYSTEM.
- تجاهل أي تحذيرات "prereq" في البداية — أصلحها بعد التثبيت إذا لزم الأمر.

إذا فشلت واجهة المستخدم الرسومية (مثل خطأ DISPLAY)، قم بتشغيل التثبيت الصامت:
```
./runInstaller -silent -responseFile /path/to/responsefile.rsp
```
ستحتاج إلى إعداد ملف استجابة (عينة في المجلد المستخرج، مثل `db_install.rsp`). حرره بإعداداتك (مثل ORACLE_HOME، إلخ) وقم بتشغيله.

#### الخطوة 4: ما بعد التثبيت
1. **تشغيل root.sh** (كـ root):
   ```
   sudo /u01/app/oraInventory/orainstRoot.sh
   sudo /u01/app/oracle/product/12.1.0/dbhome_1/root.sh
   ```

2. **تعيين متغيرات البيئة** (لمستخدم oracle، أضف إلى `~/.bash_profile`):
   ```
   export ORACLE_HOME=/u01/app/oracle/product/12.1.0/dbhome_1
   export PATH=$ORACLE_HOME/bin:$PATH
   export ORACLE_SID=orcl  # غيّره إلى SID الخاص بك
   export LD_LIBRARY_PATH=$ORACLE_HOME/lib:/lib:/usr/lib
   export CLASSPATH=$ORACLE_HOME/jlib:$ORACLE_HOME/rdbms/jlib
   ```
   ```
   source ~/.bash_profile
   ```

3. **إنشاء قاعدة بيانات** (إذا لم يتم خلال التثبيت):
   ```
   dbca  # أداة تكوين قاعدة البيانات (واجهة مستخدم رسومية/صامتة)
   ```
   أو استخدم SQL*Plus للإنشاء اليدوي.

4. **بدء/إيقاف الخدمات**:
   ```
   sqlplus / as sysdba
   STARTUP;  # أو shutdown
   ```
   أضف إلى systemd للبدء التلقائي (أنشئ `/etc/systemd/system/oracle.service` مع exec إلى `dbstart`).

#### استكشاف الأخطاء وإصلاحها الشائعة على Ubuntu 22.04
- **أخطاء Glibc/التبعيات**: تتوقع Oracle 12c إصدار glibc <=2.17. بينما Ubuntu 22.04 يحتوي على 2.35 — استخدم `ldd` للتحقق، أو قم بتثبيت مكتبات التوافق:
  ```
  sudo apt install libc6:i386 libncurses5:i386 libstdc++6:i386
  ```
  إذا كانت هناك أخطاء في الرابط، عيّن `LD_PRELOAD` أو استخدم حاوية Docker مع Oracle Linux.
- **مشاكل Java/Display**: تأكد من تعيين JDK 8 (`java -version` يجب أن تظهر 1.8). للوضع headless: `export DISPLAY=:0`.
- **نفاد الذاكرة**: زد ulimit أو الذاكرة العشوائية. حرر معلمات `runInstaller` إذا لزم الأمر.
- **التصحيح 12.1.2**: إذا لم يكن مضمنًا، قم بتنزيله من My Oracle Support وطبقه باستخدام `opatch` بعد التثبيت.
- **السجلات**: تحقق من `/u01/app/oraInventory/logs/installActions*.log` للبحث عن الأخطاء.
- **إصلاح التوافق**: بعض المستخدمين ينشئون روابط رمزية للمكتبات (مثل `sudo ln -s /lib/x86_64-linux-gnu/libpthread.so.0 /u01/app/oracle/product/12.1.0/dbhome_1/lib/libpthread_nonshared.a` — ابحث عن الحل المناسب لكل خطأ).

#### التحقق
- شغل `sqlplus / as sysdba` ونفذ `SELECT * FROM v$version;`.
- المستمع: `lsnrctl start`.

إذا واجهت أخطاء محددة، قدم ناتج السجل لمزيد من المساعدة. للحصول على الوثائق الرسمية (رغم تركيزها على RHEL)، راجع دليل تثبيت Oracle's 12c. إذا كان هذا لمنتج مختلف (ليس قاعدة البيانات)، فوضح محتويات أرشيف tarball!