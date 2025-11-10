---
audio: false
generated: true
image: false
lang: ar
layout: post
title: إتقان أساسيات نظام ريد هات إنتربرايز لينكس
translated: true
type: note
---

## مقدمة عن ريد هات لينكس
ريد هات إنتربرايز لينكس (RHEL) هو نظام تشغيل مفتوح المصدر رائد تم تطويره من قبل شركة Red Hat, Inc. تم تصميمه لبيئات المؤسسات، حيث يقدم الاستقرار، الأمان، ودعمًا قويًا للتطبيقات الحرجة. يُستخدم RHEL على نطاق واسع في الخوادم، وبيئات السحابة، والبنية التحتية لتكنولوجيا المعلومات المؤسسية.

### التاريخ
- **1994**: تم إصدار Red Hat Linux لأول مرة كتوزيعة لينكس تجارية.
- **2002**: قدمت ريد هات Red Hat Enterprise Linux، مركزة على الموثوقية من مستوى المؤسسة.
- **2025**: RHEL 9 هو أحدث إصدار رئيسي، مع RHEL 10 قيد التطوير، ليقدم ميزات متقدمة مثل الأمان المعزز ودعم الحاويات.

### الميزات الرئيسية
- **الاستقرار**: يُعطي RHEL الأولوية للدعم طويل الأمد (LTS) بدورة حياة مدتها 10 سنوات لكل إصدار رئيسي.
- **الأمان**: ميزات مثل SELinux (Security-Enhanced Linux)، و firewalld، وتحديثات الأمان المنتظمة.
- **الأداء**: مُحسّن للحوسبة عالية الأداء، والمحاكاة الافتراضية، والنشر السحابي.
- **نموذج الاشتراك**: يوفر الوصول إلى التحديثات، والدعم، والبرامج المعتمدة من خلال اشتراكات ريد هات.
- **النظام البيئي**: يتكامل مع Red Hat OpenShift، و Ansible، وأدوات أخرى لـ DevOps والأتمتة.

## التثبيت
### متطلبات النظام
- **الحد الأدنى**:
  - 1.5 جيجابايت ذاكرة وصول عشوائي
  - 20 جيجابايت مساحة قرص
  - معالج 1 جيجا هرتز
- **المُوصى به**:
  - 4 جيجابايت ذاكرة وصول عشوائي أو أكثر
  - 40 جيجابايت+ مساحة قرص
  - معالج متعدد النوى

### خطوات التثبيت
1. **تحميل RHEL**:
   - احصل على ملف RHEL ISO من [بوابة عملاء ريد هات](https://access.redhat.com) (يتطلب اشتراكًا أو حساب مطور).
   - بدلاً من ذلك، استخدم اشتراك المطور المجاني للاستخدام غير الإنتاجي.
2. **إنشاء وسائط قابلة للتمهيد**:
   - استخدم أدوات مثل `dd` أو Rufus لإنشاء محرك أقراص USB قابل للتمهيد.
   - أمر مثال: `sudo dd if=rhel-9.3-x86_64.iso of=/dev/sdX bs=4M status=progress`
3. **التمهيد والتثبيت**:
   - قم بالتمهيد من USB أو DVD.
   - اتبع مُثبّت Anaconda:
     - اختر اللغة والمنطقة.
     - قم بتكوين تقسيم القرص (يدوي أو تلقائي).
     - إعداد إعدادات الشبكة.
     - أنشئ كلمة مرور root وحسابات المستخدمين.
4. **تسجيل النظام**:
   - بعد التثبيت، سجل النظام في مدير اشتراكات ريد هات: `subscription-manager register --username <username> --password <password>`.
   - اربط اشتراكًا: `subscription-manager attach --auto`.

## إدارة النظام
### إدارة الحزم
يستخدم RHEL أداة **DNF** (Dandified YUM) لإدارة الحزم.
- تثبيت حزمة: `sudo dnf install <package-name>`
- تحديث النظام: `sudo dnf update`
- البحث عن الحزم: `sudo dnf search <keyword>`
- تمكين المستودعات: `sudo subscription-manager repos --enable <repo-id>`

### إدارة المستخدمين
- إضافة مستخدم: `sudo useradd -m <username>`
- تعيين كلمة المرور: `sudo passwd <username>`
- تعديل مستخدم: `sudo usermod -aG <group> <username>`
- حذف مستخدم: `sudo userdel -r <username>`

### إدارة نظام الملفات
- فحص استخدام القرص: `df -h`
- سرد أنظمة الملفات الموصولة: `lsblk`
- إدارة الأقسام: استخدم `fdisk` أو `parted` لتقسيم القرص.
- تكوين LVM (مدير الوحدات المنطقية):
  - إنشاء وحدة مادية: `pvcreate /dev/sdX`
  - إنشاء مجموعة وحدات: `vgcreate <vg-name> /dev/sdX`
  - إنشاء وحدة منطقية: `lvcreate -L <size> -n <lv-name> <vg-name>`

### الشبكات
- تكوين الشبكة باستخدام `nmcli`:
  - سرد الاتصالات: `nmcli connection show`
  - إضافة IP ثابت: `nmcli con mod <connection-name> ipv4.addresses 192.168.1.100/24 ipv4.gateway 192.168.1.1 ipv4.method manual`
  - تفعيل الاتصال: `nmcli con up <connection-name>`
- إدارة الجدار الناري باستخدام `firewalld`:
  - فتح منفذ: `sudo firewall-cmd --add-port=80/tcp --permanent`
  - إعادة تحميل الجدار الناري: `sudo firewall-cmd --reload`

### الأمان
- **SELinux**:
  - فحص الحالة: `sestatus`
  - تعيين الوضع (تقييد/تساهل): `sudo setenforce 0` (تساهل) أو `sudo setenforce 1` (تقييد)
  - تعديل السياسات: استخدم `semanage` و `audit2allow` للسياسات المخصصة.
- **التحديثات**:
  - تطبيق تصحيحات الأمان: `sudo dnf update --security`
- **SSH**:
  - تأمين SSH: عدّل ملف `/etc/ssh/sshd_config` لتعطيل تسجيل دخول root (`PermitRootLogin no`) وتغيير المنفذ الافتراضي.
  - إعادة تشغيل SSH: `sudo systemctl restart sshd`

## الميزات المتقدمة
### الحاويات والمحاكاة الافتراضية
- **Podman**: أداة الحاويات التي لا تتطلب صلاحيات جذرية في RHEL.
  - تشغيل حاوية: `podman run -it docker.io/library/centos bash`
  - بناء صورة: `podman build -t <image-name> .`
- **المحاكاة الافتراضية**: استخدم `libvirt` و `virt-manager` لإدارة الأجهزة الافتراضية.
  - التثبيت: `sudo dnf install libvirt virt-manager`
  - بدء تشغيل libvirt: `sudo systemctl start libvirtd`

### الأتمتة باستخدام Ansible
- تثبيت Ansible: `sudo dnf install ansible`
- إنشاء دفتر المهام (playbook):
  ```yaml
  - name: Install Apache
    hosts: all
    tasks:
      - name: Install httpd
        dnf:
          name: httpd
          state: present
  ```
- تشغيل دفتر المهام: `ansible-playbook playbook.yml`

### التكامل مع السحابة
- يتكامل RHEL مع AWS، و Azure، و Google Cloud.
- استخدم Red Hat OpenShift لتنسيق الحاويات.
- انشر صور RHEL في بيئات السحابة عبر Red Hat Cloud Access.

## استكشاف الأخطاء وإصلاحها
- **السجلات**: افحص `/var/log` للبحث في سجلات النظام (مثل `/var/log/messages` أو `/var/log/secure`).
- **Systemd**: إدارة الخدمات باستخدام `systemctl`:
  - فحص حالة الخدمة: `systemctl status <service>`
  - إعادة تشغيل الخدمة: `systemctl restart <service>`
- **الأداء**: استخدم `top`، أو `htop`، أو `vmstat` لمراقبة أداء النظام.
- **مشاكل الشبكة**: استخدم `ping`، أو `traceroute`، أو `nslookup` للتشخيص.

## أفضل الممارسات
- قم بتحديث النظام بانتظام لتصحيح الثغرات الأمنية.
- استخدم كلمات مرور قوية وفرض سياسات SELinux.
- احفظ نسخًا احتياطية من البيانات الحرجة باستخدام أدوات مثل `rsync` أو أداة ريد هات `rear`.
- راقب صحة النظام باستخدام أدوات مثل Cockpit (`sudo dnf install cockpit`).

## المصادر
- [بوابة عملاء ريد هات](https://access.redhat.com)
- [توثيق RHEL](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux)
- [برنامج مطوري ريد هات](https://developers.redhat.com)
- منتديات المجتمع مثل [Red Hat Discuss](https://discuss.redhat.com)