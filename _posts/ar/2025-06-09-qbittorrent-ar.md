---
audio: false
generated: true
lang: ar
layout: post
title: تثبيت qBittorrent على أوبونتو
translated: true
type: note
---

تثبيت qBittorrent على أوبونتو عملية مباشرة. إليك الخطوات:

### **الطريقة 1: التثبيت عبر APT (موصى بها)**
1. **حدّث قائمة الحزم**:
   ```bash
   sudo apt update
   ```

2. **ثبّت qBittorrent**:
   ```bash
   sudo apt install qbittorrent
   ```

3. **شغّل qBittorrent**:
   - من الطرفية:
     ```bash
     qbittorrent
     ```
   - أو ابحث عن "qBittorrent" في قائمة تطبيقات أوبونتو.

---

### **الطريقة 2: تثبيت أحدث إصدار عبر PPA (اختياري)**
إذا كنت تريد إصدارًا أحدث من الموجود في مستودع أوبونتو الافتراضي، يمكنك استخدام PPA الرسمي:

1. **أضف PPA الخاص بـ qBittorrent**:
   ```bash
   sudo add-apt-repository ppa:qbittorrent-team/qbittorrent-stable
   ```

2. **حدّث قوائم الحزم**:
   ```bash
   sudo apt update
   ```

3. **ثبّت qBittorrent**:
   ```bash
   sudo apt install qbittorrent
   ```

4. **شغّل qBittorrent**:
   ```bash
   qbittorrent
   ```

---

### **الطريقة 3: تثبيت qBittorrent عبر Flatpak (بديل)**
إذا كنت تفضل استخدام Flatpak:

1. **ثبّت Flatpak (إذا لم يكن مثبتًا بالفعل)**:
   ```bash
   sudo apt install flatpak
   ```

2. **أضف مستودع Flathub**:
   ```bash
   flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
   ```

3. **ثبّت qBittorrent**:
   ```bash
   flatpak install flathub org.qbittorrent.qBittorrent
   ```

4. **شغّل qBittorrent**:
   ```bash
   flatpak run org.qbittorrent.qBittorrent
   ```

---

### **إلغاء تثبيت qBittorrent (إذا لزم الأمر)**
- **إذا كان مثبتًا عبر APT أو PPA**:
  ```bash
  sudo apt remove qbittorrent
  ```
- **إذا كان مثبتًا عبر Flatpak**:
  ```bash
  flatpak uninstall org.qbittorrent.qBittorrent
  ```

هذا كل شيء! الآن لديك qBittorrent مثبتًا على أوبونتو. 🚀 دعني أعلم إذا كنت بحاجة إلى أي مساعدة!