---
audio: false
generated: true
image: false
lang: ar
layout: post
title: إصلاح تقدير شحن البطارية
translated: true
type: note
---

يشير الخطأ `Cannot estimate time to full charge (sysfs files not found)` إلى أن البرنامج النصي لم يتمكن من العثور على ملفات معلومات البطارية المتوقعة في `/sys/class/power_supply/BAT0/`. يمكن أن يحدث هذا إذا:
1. كان اسم البطارية مختلفًا عن `BAT0` (مثل `BAT1` أو اسم آخر).
2. لم تكن الملفات المحددة (`charge_now`, `charge_full`, `current_now`) متاحة أو لها أسماء مختلفة على حاسوب لينوفو الخاص بك.
3. لم يكن للمستخدم الذي يشغل البرنامج النصي الإذن اللازم للوصول إلى هذه الملفات.

إليك برنامجًا نصيًا معدلاً بلغة Python يكتشف اسم البطارية ديناميكيًا ويتعامل مع الاختلافات في أسماء ملفات sysfs (مثل `energy_now` بدلاً من `charge_now` في بعض الأنظمة). كما يتضمن معالجة أفضل للأخطاء وفحوصات للأذونات:

```python
import psutil
import os
import glob

def find_battery_path():
    """Find the battery directory in /sys/class/power_supply."""
    battery_paths = glob.glob('/sys/class/power_supply/BAT*')
    if not battery_paths:
        return None
    return battery_paths[0]  # Return the first battery found (e.g., BAT0 or BAT1)

def get_battery_info():
    try:
        # Get battery information using psutil
        battery = psutil.sensors_battery()
        
        if battery is None:
            print("No battery detected.")
            return

        # Battery percentage
        percent = battery.percent
        print(f"Battery Percentage: {percent:.2f}%")

        # Check if battery is charging
        is_charging = battery.power_plugged
        status = "Charging" if is_charging else "Discharging"
        print(f"Status: {status}")

        # Estimate remaining time (only when discharging)
        if not is_charging and battery.secsleft != psutil.POWER_TIME_UNLIMITED:
            remaining_secs = battery.secsleft
            hours = remaining_secs // 3600
            minutes = (remaining_secs % 3600) // 60
            print(f"Estimated Time Remaining: {hours} hours, {minutes} minutes")
        elif is_charging:
            # Try to estimate time to full charge using sysfs
            battery_path = find_battery_path()
            if not battery_path:
                print("Cannot estimate time to full charge (no battery found in sysfs).")
                return

            try:
                # Check for charge or energy-based files
                charge_now_file = os.path.join(battery_path, 'charge_now')
                energy_now_file = os.path.join(battery_path, 'energy_now')
                charge_full_file = os.path.join(battery_path, 'charge_full')
                energy_full_file = os.path.join(battery_path, 'charge_full_design')
                current_now_file = os.path.join(battery_path, 'current_now')

                # Determine which files to use (charge or energy)
                if os.path.exists(charge_now_file) and os.path.exists(charge_full_file):
                    now_file, full_file = charge_now_file, charge_full_file
                elif os.path.exists(energy_now_file) and os.path.exists(energy_full_file):
                    now_file, full_file = energy_now_file, energy_full_file
                else:
                    print("Cannot estimate time to full charge (charge/energy files not found).")
                    return

                # Read battery data
                with open(now_file, 'r') as f:
                    charge_now = int(f.read().strip())
                with open(full_file, 'r') as f:
                    charge_full = int(f.read().strip())
                with open(current_now_file, 'r') as f:
                    current_now = int(f.read().strip())

                if current_now > 0:
                    charge_remaining = charge_full - charge_now
                    seconds_to_full = (charge_remaining / current_now) * 3600
                    hours = int(seconds_to_full // 3600)
                    minutes = int((seconds_to_full % 3600) // 60)
                    print(f"Estimated Time to Full Charge: {hours} hours, {minutes} minutes")
                else:
                    print("Cannot estimate time to full charge (current_now is 0).")
            except PermissionError:
                print("Cannot estimate time to full charge (permission denied). Try running with sudo.")
            except FileNotFoundError:
                print(f"Cannot estimate time to full charge (sysfs files not found in {battery_path}).")
            except Exception as e:
                print(f"Error estimating time to full charge: {e}")
        else:
            print("No remaining time estimate available.")

    except Exception as e:
        print(f"Error retrieving battery information: {e}")

if __name__ == "__main__":
    get_battery_info()
```

### التغييرات التي تم إجراؤها
1. **الكشف الديناميكي عن البطارية**:
   - يستخدم `glob.glob('/sys/class/power_supply/BAT*')` للعثور على دليل البطارية (مثل `BAT0`, `BAT1`) بدلاً من الترميز الثابت لـ `BAT0`.
   - يُرجع أول بطارية يتم العثور عليها أو `None` إذا لم يتم اكتشاف أي بطارية.

2. **دعم لملفات الشحن والطاقة**:
   - يتحقق من كل من ملفات `charge_now`/`charge_full` و `energy_now`/`energy_full`، حيث تستخدم بعض الأنظمة مقاييس قائمة على الطاقة (بالواط/ساعة) بدلاً من المقاييس القائمة على الشحن (بالميكروأمبير/ساعة).
   - يختار الزوج المناسب من الملفات بناءً على التوفر.

3. **معالجة محسنة للأخطاء**:
   - يتعامل مع `PermissionError` بشكل منفصل لاقتراح التشغيل باستخدام `sudo` إذا تم رفض الوصول.
   - يقدم ملاحظات محددة إذا لم يتم العثور على ملفات sysfs أو إذا كانت قيمة `current_now` صفرًا.

4. **إخراج منسق**:
   - يحدد نسبة البطارية بمنزلتين عشريتين (`{percent:.2f}`) للحصول على إخراج أنظف.

### كيفية الاستخدام
1. **تثبيت `psutil` (إذا لم يكن مثبتًا مسبقًا)**:
   ```bash
   sudo pip3 install psutil
   ```

2. **حفظ البرنامج النصي**:
   - احفظ البرنامج النصي المحدث باسم، على سبيل المثال، `battery_info.py`.

3. **تشغيل البرنامج النصي**:
   - نفذه في الطرفية:
     ```bash
     python3 battery_info.py
     ```
   - إذا ظهر خطأ "permission denied"، حاول التشغيل بصلاحيات مرتفعة:
     ```bash
     sudo python3 battery_info.py
     ```

4. **التحقق من مسار البطارية**:
   - للتحقق من اسم البطارية والملفات المتاحة، قم بتشغيل:
     ```bash
     ls /sys/class/power_supply
     ```
     ثم تحقق من محتويات دليل البطارية (مثل `BAT0` أو `BAT1`):
     ```bash
     ls /sys/class/power_supply/BAT0
     ```
   - ابحث عن ملفات مثل `charge_now`, `charge_full`, `energy_now`, `energy_full`, أو `current_now`. إذا كانت مختلفة (مثل `energy_full_design` بدلاً من `charge_full`)، يجب أن يتعامل البرنامج النصي معها، ولكن أخبرني إذا كنت بحاجة إلى مزيد من التعديلات.

### نصائح لتصحيح الأخطاء
- إذا كان البرنامج النصي لا يزال يبلغ عن "لم يتم العثور على ملفات sysfs"، فتحقق من أسماء الملفات الدقيقة في `/sys/class/power_supply/BAT*`. قد تستخدم بعض أجهزة حاسوب لينوفو أسماء غير قياسية أو يكون لها دعم محدود لـ sysfs.
- إذا رأيت "permission denied"، فإن التشغيل باستخدام `sudo` يجب أن يحل المشكلة، لكن كن حذرًا بشأن الصلاحيات المرتفعة.
- إذا تم اكتشاف البطارية ولكن لم يتم تقديم تقدير للوقت، فقد يكون ذلك بسبب أن `current_now` تساوي صفرًا (شائع عندما لا يقدم النظام تيار الشحن بنشاط). في هذه الحالة، سيعود البرنامج النصي إلى الإشارة إلى عدم توفر تقدير.

### مثال على الإخراج
على نظامك (Lenovo XiaoXin-14-IAH8)، قد ترى شيئًا مثل:
```
Battery Percentage: 49.62%
Status: Charging
Estimated Time to Full Charge: 1 hours, 45 minutes
```
أو، إذا كانت الملفات لا تزال مفقودة:
```
Battery Percentage: 49.62%
Status: Charging
Cannot estimate time to full charge (sysfs files not found in /sys/class/power_supply/BAT0).
```

### إذا استمرت المشاكل
إذا فشل البرنامج النصي في العثور على ملفات sysfs، فيرجى مشاركة إخراج:
```bash
ls -l /sys/class/power_supply
ls -l /sys/class/power_supply/BAT*/*
```
سيساعد هذا في تحديد أسماء الملفات الدقيقة والأذونات. بعد ذلك يمكنني تخصيص البرنامج النصي لمطابقة تكوين نظامك.

[psutil Documentation](https://psutil.readthedocs.io/en/latest/)  
[Linux sysfs Power Supply](https://www.kernel.org/doc/html/latest/power/power_supply_class.html)