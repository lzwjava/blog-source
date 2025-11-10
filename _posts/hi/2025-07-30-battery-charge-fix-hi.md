---
audio: false
generated: true
image: false
lang: hi
layout: post
title: बैटरी चार्ज अनुमान सुधार
translated: true
type: note
---

त्रुटि `Cannot estimate time to full charge (sysfs files not found)` यह इंगित करती है कि स्क्रिप्ट को `/sys/class/power_supply/BAT0/` में अपेक्षित बैटरी सूचना फाइलें नहीं मिलीं। ऐसा निम्न कारणों से हो सकता है:
1. बैटरी का नाम `BAT0` के अलावा कुछ और है (जैसे, `BAT1` या कोई अन्य नाम)।
2. विशिष्ट फाइलें (`charge_now`, `charge_full`, `current_now`) आपके लेनोवो लैपटॉप पर उपलब्ध नहीं हैं या उनके अलग नाम हैं।
3. स्क्रिप्ट चलाने वाले उपयोगकर्ता के पास इन फाइलों तक पहुंच की अनुमति नहीं है।

यहां एक ठीक किया गया Python स्क्रिप्ट है जो बैटरी का नाम गतिशील रूप से पता लगाता है और sysfs फाइल नामों में भिन्नताओं को संभालता है (जैसे, कुछ सिस्टम के लिए `charge_now` के बजाय `energy_now`)। इसमें बेहतर त्रुटि प्रबंधन और अनुमति जांच भी शामिल है:

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

### किए गए परिवर्तन
1. **डायनेमिक बैटरी डिटेक्शन**:
   - बैटरी डायरेक्टरी (जैसे `BAT0`, `BAT1`) को खोजने के लिए `glob.glob('/sys/class/power_supply/BAT*')` का उपयोग करता है, न कि `BAT0` को हार्डकोड करता है।
   - पाई गई पहली बैटरी लौटाता है या यदि कोई बैटरी नहीं मिलती है तो `None` लौटाता है।

2. **चार्ज और एनर्जी फाइलों के लिए सपोर्ट**:
   - `charge_now`/`charge_full` और `energy_now`/`energy_full` दोनों प्रकार की फाइलों की जांच करता है, क्योंकि कुछ सिस्टम चार्ज-आधारित (माइक्रोएम्पीयर-घंटे में) के बजाय एनर्जी-आधारित मेट्रिक्स (वाट-घंटे में) का उपयोग करते हैं।
   - उपलब्धता के आधार पर फाइलों की उपयुक्त जोड़ी का चयन करता है।

3. **बेहतर त्रुटि प्रबंधन**:
   - यदि एक्सेस अस्वीकार कर दिया जाता है तो `sudo` के साथ चलाने का सुझाव देने के लिए `PermissionError` को अलग से संभालता है।
   - यदि sysfs फाइलें नहीं मिलती हैं या `current_now` शून्य है तो विशिष्ट फीडबैक प्रदान करता है।

4. **फॉर्मेटेड आउटपुट**:
   - क्लीनर आउटपुट के लिए बैटरी प्रतिशत को दो दशमलव स्थानों (`{percent:.2f}`) तक सीमित करता है।

### उपयोग कैसे करें
1. **`psutil` इंस्टॉल करें (यदि पहले से इंस्टॉल नहीं है)**:
   ```bash
   sudo pip3 install psutil
   ```

2. **स्क्रिप्ट सेव करें**:
   - अपडेटेड स्क्रिप्ट को, उदाहरण के लिए, `battery_info.py` के रूप में सेव करें।

3. **स्क्रिप्ट रन करें**:
   - टर्मिनल में निष्पादित करें:
     ```bash
     python3 battery_info.py
     ```
   - यदि आपको "permission denied" त्रुटि मिलती है, तो उन्नत विशेषाधिकारों के साथ चलाने का प्रयास करें:
     ```bash
     sudo python3 battery_info.py
     ```

4. **बैटरी पथ जांचें**:
   - बैटरी नाम और उपलब्ध फाइलों को सत्यापित करने के लिए, रन करें:
     ```bash
     ls /sys/class/power_supply
     ```
     फिर, बैटरी डायरेक्टरी (जैसे `BAT0` या `BAT1`) की सामग्री की जांच करें:
     ```bash
     ls /sys/class/power_supply/BAT0
     ```
   - `charge_now`, `charge_full`, `energy_now`, `energy_full`, या `current_now` जैसी फाइलों की तलाश करें। यदि वे भिन्न हैं (जैसे `charge_full` के बजाय `energy_full_design`), तो स्क्रिप्ट को इसे संभालना चाहिए, लेकिन यदि आपको आगे ट्वीक्स की आवश्यकता है तो मुझे बताएं।

### डीबगिंग टिप्स
- यदि स्क्रिप्ट अभी भी "sysfs files not found" रिपोर्ट करती है, तो `/sys/class/power_supply/BAT*` में सटीक फाइल नाम जांचें। कुछ लेनोवो लैपटॉप गैर-मानक नामों का उपयोग कर सकते हैं या उनमें सीमित sysfs सपोर्ट हो सकता है।
- यदि आप "permission denied" देखते हैं, तो `sudo` के साथ चलाने से इसे हल करना चाहिए, लेकिन उन्नत विशेषाधिकारों के साथ सावधान रहें।
- यदि बैटरी का पता चल जाता है लेकिन कोई समय अनुमान प्रदान नहीं किया जाता है, तो यह `current_now` के शून्य होने के कारण हो सकता है (आमतौर पर तब जब सिस्टम सक्रिय रूप से चार्जिंग करंट की रिपोर्ट नहीं कर रहा हो)। इस स्थिति में, स्क्रिप्ट यह इंगित करने के लिए वापस आ जाएगी कि कोई अनुमान उपलब्ध नहीं है।

### उदाहरण आउटपुट
आपके सिस्टम (Lenovo XiaoXin-14-IAH8) पर, आप कुछ इस तरह देख सकते हैं:
```
Battery Percentage: 49.62%
Status: Charging
Estimated Time to Full Charge: 1 hours, 45 minutes
```
या, यदि फाइलें अभी भी गायब हैं:
```
Battery Percentage: 49.62%
Status: Charging
Cannot estimate time to full charge (sysfs files not found in /sys/class/power_supply/BAT0).
```

### यदि समस्याएं बनी रहती हैं
यदि स्क्रिप्ट को अभी भी sysfs फाइलें नहीं मिलती हैं, तो कृपया इसका आउटपुट साझा करें:
```bash
ls -l /sys/class/power_supply
ls -l /sys/class/power_supply/BAT*/*
```
इससे सटीक फाइल नामों और अनुमतियों की पहचान करने में मदद मिलेगी। फिर मैं स्क्रिप्ट को आपके सिस्टम कॉन्फ़िगरेशन से मेल खाने के लिए और अनुकूलित कर सकता हूं।

[psutil Documentation](https://psutil.readthedocs.io/en/latest/)  
[Linux sysfs Power Supply](https://www.kernel.org/doc/html/latest/power/power_supply_class.html)