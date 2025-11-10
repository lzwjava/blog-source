---
audio: false
generated: true
image: false
lang: ar
layout: post
title: دليل RHEL الكامل لنظام لينكس المؤسسي
translated: true
type: note
---

إليك **دليل شامل لنظام Red Hat Enterprise Linux (RHEL)**. سأقوم بتنظيمه خطوة بخطوة حتى تتمكن من استخدامه كمسار تعلم وكمصدر مرجعي.

---

## 1. مقدمة عن Red Hat Linux

Red Hat Enterprise Linux (RHEL) هو توزيعة لينكس تجارية مطورة من قبل **Red Hat, Inc.**، مصممة من أجل **الاستقرار، الأمان، والدعم المؤسسي**. يُستخدم على نطاق واسع في القطاعات المصرفية والرعاية الصحية والحكومية وتقنية المعلومات المؤسسية بسبب دورة دعمه طويلة الأمد ونظامه البيئي للبرمجيات المعتمدة.

أبرز النقاط:

* دعم بمستوى مؤسسي (دورة حياة تزيد عن 10 سنوات لكل إصدار رئيسي).
* معتمد على أجهزة رئيسية (Dell, HP, IBM، إلخ).
* مستخدم على نطاق واسع في السحابة (AWS, Azure, GCP)، والحاويات (OpenShift, Kubernetes)، والمحاكاة الافتراضية.

---

## 2. التثبيت والإعداد

* **التنزيل**: صور ISO الرسمية متاحة عبر بوابة عملاء Red Hat (تتطلب اشتراكًا).
* **برامج التثبيت**: يستخدم **برنامج التثبيت Anaconda** مع الوضعين الرسومي والنصي.
* **التقسيم**: خيارات لـ LVM، وXFS (نظام الملفات الافتراضي)، والأقراص المشفرة.
* **أدوات ما بعد التثبيت**: `subscription-manager` لتسجيل النظام.

---

## 3. إدارة الحزم

* **RPM (مدير حزم Red Hat)** – التنسيق الأساسي للبرمجيات.
* **DNF** – مدير الحزم الافتراضي في RHEL 8 والإصدارات الأحدث.

  * تثبيت حزمة:

    ```bash
    sudo dnf install httpd
    ```
  * تحديث النظام:

    ```bash
    sudo dnf update
    ```
  * البحث عن الحزم:

    ```bash
    sudo dnf search nginx
    ```

يدعم RHEL أيضًا **تيارات التطبيقات (AppStreams)** لإصدارات متعددة من البرمجيات (مثل Python 3.6 مقابل 3.9).

---

## 4. أساسيات إدارة النظام

* **إدارة المستخدمين**:
  `useradd`, `passwd`, `usermod`, `/etc/passwd`, `/etc/shadow`
* **إدارة العمليات**:
  `ps`, `top`, `htop`, `kill`, `systemctl`
* **إدارة الأقراص**:
  `lsblk`, `df -h`, `mount`, `umount`, `fdisk`, `parted`
* **خدمات النظام (systemd)**:

  ```bash
  systemctl start nginx
  systemctl enable nginx
  systemctl status nginx
  ```

---

## 5. الشبكات

* التكوين مخزن في `/etc/sysconfig/network-scripts/`.
* الأوامر:

  * `nmcli` (واجهة سطر أوامر NetworkManager)
  * `ip addr`, `ip route`, `ping`, `traceroute`
* الجدار الناري:

  * يُدار بواسطة **firewalld** (`firewall-cmd`).
  * مثال:

    ```bash
    firewall-cmd --add-service=http --permanent
    firewall-cmd --reload
    ```

---

## 6. الأمان

* **SELinux**: نظام تحكم دخول إلزامي.

  * التحقق من الحالة: `sestatus`
  * الأنماط: enforcing, permissive, disabled
* **FirewallD**: يدير أمان الشبكة.
* **تحديثات النظام**: تصحيحات الأمان عبر `dnf update`.
* **Auditd**: التسجيل والامتثال.

---

## 7. التسجيل والمراقبة

* **سجلات النظام**:
  مخزنة تحت `/var/log/`.
* **Journald**:
  `journalctl -xe`
* **أدوات الأداء**:

  * `sar` (حزمة sysstat)
  * `vmstat`, `iostat`, `dstat`
* **Red Hat Insights**: تحليل النظام القائم على السحابة.

---

## 8. المحاكاة الافتراضية والحاويات

* **KVM** للاستضافة الافتراضية.
* **Podman** (بدلاً من Docker):

  ```bash
  podman run -it centos /bin/bash
  ```
* **OpenShift** (منصة Kubernetes) للتنسيق.

---

## 9. إدارة التخزين

* **LVM** للإدارة المرنة للأقراص.
* **XFS**: نظام الملفات الافتراضي.
* **Stratis**: إدارة التخزين مع التخصيص الرقيق ولقطات النظام.

---

## 10. الأتمتة وإدارة التكوين

* **Ansible**: منصة الأتمتة من Red Hat.
* **Kickstart**: يُؤتمت تثبيت نظام التشغيل.
* **أدوار النظام (System Roles)**: أدوار Ansible محددة مسبقًا لـ RHEL.

---

## 11. الاشتراكات والدعم

* تستخدم Red Hat **نموذج اشتراك**.
* `subscription-manager` للتسجيل وإرفاق الاشتراكات وتمكين المستودعات.
* اشتراك مطور RHEL **مجاني للأفراد**.

---

## 12. أفضل الممارسات

* حافظ دائمًا على تحديث الأنظمة بتصحيحات الأمان.
* استخدم SELinux في وضع `enforcing` ما لم تكن تقوم بتنقيح الأخطاء.
* مرّكز التسجيل باستخدام `rsyslog` أو مجموعة ELK.
* أتمت المهام المتكررة باستخدام Ansible.
* راقب صحة النظام باستخدام Red Hat Insights.

---

## 13. مصادر التعلم

* [Red Hat Documentation](https://access.redhat.com/documentation)
* [Red Hat Academy](https://www.redhat.com/en/services/training-and-certification/red-hat-academy)
* الشهادات:

  * **RHCSA**
  * **RHCE**
  * **RHCA**

---

✅ هذا هو الأساس.
هل تريد مني **توسيع هذا إلى "دليل عملي"** يحتوي على أوامر وسير عمل من العالم الحقيقي (مثل إعداد خادم ويب، قاعدة بيانات، جدار ناري، إلخ)، أم تفضّل الإبقاء عليه **نظريًا ومفاهيميًا** أكثر؟