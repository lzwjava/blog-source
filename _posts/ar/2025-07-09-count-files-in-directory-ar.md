---
audio: false
generated: true
lang: ar
layout: post
title: عدّد الملفات في مجلد
translated: true
type: note
---

لحساب عدد الملفات في دليل، يمكنك استخدام طرق مختلفة بناءً على نظام التشغيل والأدوات المستخدمة. إليك أكثر الطرق شيوعًا:

### **على Windows (موجه الأوامر)**
```cmd
dir /a-d | find /c /v ""
```
- يعرض جميع الملفات (وليس المجلدات) ويعد الأسطر، مستثنياً الأسطر الفارغة.

### **على Windows (PowerShell)**
```powershell
(Get-ChildItem -File).Count
```
- يسترجع الملفات فقط ويعدها.

### **على Linux/macOS (الطرفية)**
```bash
ls -l | grep ^- | wc -l
```
- يعرض الملفات (`ls -l`)، يرشح الملفات العادية (`grep ^-`)، ويعدها (`wc -l`).

أو، بطريقة أبسط:
```bash
find . -maxdepth 1 -type f | wc -l
```
- يجد الملفات فقط (`-type f`) في الدليل الحالي (`-maxdepth 1`) ويعدها.

### **باستخدام Python**
```python
import os
file_count = len([f for f in os.listdir('.') if os.path.isfile(f)])
print(file_count)
```
- يعرض محتويات الدليل، يتحقق من الملفات، ويعدها.

اختر الطريقة بناءً على بيئتك. إذا كنت تحتاج تفاصيل لنظام تشغيل أو أداة محددة، دعني أعلم!