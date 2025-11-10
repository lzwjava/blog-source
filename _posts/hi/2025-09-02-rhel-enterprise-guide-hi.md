---
audio: false
generated: true
image: false
lang: hi
layout: post
title: आरएचईएल संपूर्ण एंटरप्राइज लिनक्स गाइड
translated: true
type: note
---

यहाँ **Red Hat Enterprise Linux (RHEL) का एक व्यापक मार्गदर्शक** है। मैं इसे चरण दर चरण संरचित करूँगा ताकि आप इसे एक सीखने के मार्ग के रूप में और एक संदर्भ के रूप में उपयोग कर सकें।

---

## 1. Red Hat Linux का परिचय

Red Hat Enterprise Linux (RHEL) **Red Hat, Inc.** द्वारा विकसित एक वाणिज्यिक Linux डिस्ट्रीब्यूशन है, जिसे **स्थिरता, सुरक्षा और एंटरप्राइज़ सपोर्ट** के लिए डिज़ाइन किया गया है। इसके दीर्घकालिक सपोर्ट लाइफसाइकल और प्रमाणित सॉफ़्टवेयर इकोसिस्टम के कारण इसका बैंकिंग, स्वास्थ्य सेवा, सरकार और कॉर्पोरेट आईटी में व्यापक रूप से उपयोग किया जाता है।

मुख्य बिंदु:

* एंटरप्राइज़-ग्रेड सपोर्ट (प्रमुख रिलीज़ के लिए 10+ वर्षों की लाइफसाइकल)।
* प्रमुख हार्डवेयर (Dell, HP, IBM, आदि) पर प्रमाणित।
* क्लाउड (AWS, Azure, GCP), कंटेनर (OpenShift, Kubernetes), और वर्चुअलाइजेशन में व्यापक रूप से उपयोग किया जाता है।

---

## 2. इंस्टालेशन और सेटअप

* **डाउनलोड**: आधिकारिक ISO इमेज Red Hat Customer Portal के माध्यम से उपलब्ध हैं (सब्सक्रिप्शन आवश्यक)।
* **इंस्टॉलर**: ग्राफ़िकल और टेक्स्ट मोड के साथ **Anaconda इंस्टॉलर** का उपयोग करता है।
* **पार्टीशनिंग**: LVM, XFS (डिफ़ॉल्ट फ़ाइलसिस्टम), और एन्क्रिप्टेड डिस्क के लिए विकल्प।
* **पोस्ट-इंस्टालेशन टूल्स**: सिस्टम को रजिस्टर करने के लिए `subscription-manager`।

---

## 3. पैकेज प्रबंधन

* **RPM (Red Hat Package Manager)** – सॉफ़्टवेयर के लिए अंतर्निहित प्रारूप।
* **DNF (Dandified Yum)** – RHEL 8 और बाद में डिफ़ॉल्ट पैकेज मैनेजर।

  * एक पैकेज इंस्टॉल करें:

    ```bash
    sudo dnf install httpd
    ```
  * सिस्टम अपडेट करें:

    ```bash
    sudo dnf update
    ```
  * पैकेज खोजें:

    ```bash
    sudo dnf search nginx
    ```

RHEL सॉफ़्टवेयर के कई संस्करणों (जैसे, Python 3.6 बनाम 3.9) के लिए **AppStreams** का भी समर्थन करता है।

---

## 4. सिस्टम प्रशासन मूल बातें

* **यूज़र प्रबंधन**:
  `useradd`, `passwd`, `usermod`, `/etc/passwd`, `/etc/shadow`
* **प्रोसेस प्रबंधन**:
  `ps`, `top`, `htop`, `kill`, `systemctl`
* **डिस्क प्रबंधन**:
  `lsblk`, `df -h`, `mount`, `umount`, `fdisk`, `parted`
* **सिस्टम सर्विसेज़** (systemd):

  ```bash
  systemctl start nginx
  systemctl enable nginx
  systemctl status nginx
  ```

---

## 5. नेटवर्किंग

* कॉन्फ़िगरेशन `/etc/sysconfig/network-scripts/` में संग्रहीत।
* कमांड:

  * `nmcli` (NetworkManager CLI)
  * `ip addr`, `ip route`, `ping`, `traceroute`
* फ़ायरवॉल:

  * **firewalld** (`firewall-cmd`) द्वारा प्रबंधित।
  * उदाहरण:

    ```bash
    firewall-cmd --add-service=http --permanent
    firewall-cmd --reload
    ```

---

## 6. सुरक्षा

* **SELinux**: मैंडेटरी एक्सेस कंट्रोल सिस्टम।

  * स्टेटस जांचें: `sestatus`
  * मोड: enforcing, permissive, disabled
* **FirewallD**: नेटवर्क सुरक्षा प्रबंधित करता है।
* **सिस्टम अपडेट**: `dnf update` के माध्यम से सुरक्षा पैच।
* **Auditd**: लॉगिंग और अनुपालन।

---

## 7. लॉगिंग और मॉनिटरिंग

* **सिस्टम लॉग**:
  `/var/log/` के अंतर्गत संग्रहीत।
* **Journald**:
  `journalctl -xe`
* **परफॉर्मेंस टूल्स**:

  * `sar` (sysstat पैकेज)
  * `vmstat`, `iostat`, `dstat`
* **Red Hat Insights**: क्लाउड-आधारित सिस्टम विश्लेषण।

---

## 8. वर्चुअलाइजेशन और कंटेनर्स

* वर्चुअलाइजेशन के लिए **KVM** (Kernel-based Virtual Machine)।
* **Podman** (Docker के बजाय):

  ```bash
  podman run -it centos /bin/bash
  ```
* ऑर्केस्ट्रेशन के लिए **OpenShift** (Kubernetes प्लेटफ़ॉर्म)।

---

## 9. स्टोरेज प्रबंधन

* लचीले डिस्क प्रबंधन के लिए **LVM (Logical Volume Manager)**।
* **XFS**: डिफ़ॉल्ट फ़ाइलसिस्टम।
* **Stratis**: थिन प्रोविज़निंग और स्नैपशॉट के साथ स्टोरेज प्रबंधन।

---

## 10. ऑटोमेशन और कॉन्फ़िगरेशन प्रबंधन

* **Ansible**: Red Hat का ऑटोमेशन प्लेटफ़ॉर्म।
* **Kickstart**: OS इंस्टालेशन को स्वचालित करता है।
* **सिस्टम रोल्स**: RHEL के लिए पूर्वनिर्धारित Ansible रोल।

---

## 11. सब्सक्रिप्शन और सपोर्ट

* Red Hat एक **सब्सक्रिप्शन मॉडल** का उपयोग करता है।
* `subscription-manager` रजिस्टर करने, सब्सक्रिप्शन जोड़ने और रिपॉजिटरी सक्षम करने के लिए।
* RHEL डेवलपर सब्सक्रिप्शन व्यक्तियों के लिए **मुफ़्त** है।

---

## 12. सर्वोत्तम अभ्यास

* सिस्टम को हमेशा सुरक्षा पैच के साथ अपडेट रखें।
* डीबगिंग के अलावा SELinux को enforcing मोड में उपयोग करें।
* `rsyslog` या ELK स्टैक के साथ लॉगिंग केंद्रीकृत करें।
* Ansible के साथ दोहराए जाने वाले कार्यों को स्वचालित करें।
* Red Hat Insights के साथ सिस्टम स्वास्थ्य की निगरानी करें।

---

## 13. सीखने के संसाधन

* [Red Hat Documentation](https://access.redhat.com/documentation)
* [Red Hat Academy](https://www.redhat.com/en/services/training-and-certification/red-hat-academy)
* प्रमाणन:

  * **RHCSA** (Red Hat Certified System Administrator)
  * **RHCE** (Red Hat Certified Engineer)
  * **RHCA** (Red Hat Certified Architect)

---

✅ यही आधारशिला है।
क्या आप चाहेंगे कि मैं इसे **एक व्यावहारिक "हैंड्स-ऑन गाइड"** में विस्तारित करूँ, जिसमें वास्तविक दुनिया के कमांड और वर्कफ़्लो शामिल हों (जैसे वेब सर्वर, डेटाबेस, फ़ायरवॉल आदि सेट अप करना), या इसे अधिक **सैद्धांतिक और वैचारिक** रखूँ?