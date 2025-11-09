---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: إس بي 32 لمشاريع إنترنت الأشهاردوينو
translated: true
type: note
---

ESP32 هو متحكم منخفض التكلفة ومنخفض الطاقة تم تطويره من قبل Espressif Systems، ويتميز بوجود Wi-Fi مدمج وإمكانية الاتصال عبر Bluetooth ثنائي النمط. إنه في الأساس نظام على شريحة (SoC) يُستخدم على نطاق واسع لمشاريع إنترنت الأشياء (IoT)، وأجهزة الاستشعار، والتطبيقات اللاسلكية نظرًا لتعدد استخداماته وأدائه.

في سياق Arduino، فإن ESP32 ليس "داخل" Arduino ولكنه متوافق بالكامل مع نظام Arduino البيئي. يمكنك برمجة لوحات ESP32 (مثل NodeMCU الشهيرة أو Arduino Nano ESP32 الرسمية) باستخدام برنامج Arduino IDE المجاني. يتضمن ذلك تثبيت حزمة لوحة ESP32 عبر Board Manager في بيئة التطوير، ثم كتابة sketches بلغة C/C++ (تمامًا كما هو الحال مع لوحات Arduino التقليدية مثل Uno). تقدم ESP32 مزايا مقارنةً بـ Arduinos الأساسية، مثل معالجة أسرع (نواة مزدوجة تصل إلى 240 ميغاهيرتز)، ومزيد من دبابيس GPIO، وميزات لاسلكية، مما يجعلها مثالية للمشاريع المتصلة دون الحاجة إلى وحدات إضافية (shields).

إذا كنت جديدًا في هذا المجال، ابدأ بتنزيل Arduino IDE وابحث عن "ESP32 board package" في قائمة Tools > Board > Boards Manager.

### المراجع
- [ESP32 - Wikipedia](https://en.wikipedia.org/wiki/ESP32)
- [Arduino Nano ESP32 Documentation](https://docs.arduino.cc/nano-esp32)
- [Arduino Nano ESP32 Product Page](https://store-usa.arduino.cc/products/nano-esp32)