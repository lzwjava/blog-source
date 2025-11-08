---
audio: false
generated: true
image: false
lang: en
layout: post
title: Fix ZBook Brightness Not Working
translated: false
type: note
---

On an **HP ZBook workstation**, screen brightness can usually be adjusted in several ways, but sometimes it doesn’t work due to driver, hardware, or setting conflicts. Here’s a structured guide:

---

### Ways to Adjust Brightness

1. **Keyboard shortcuts**

   * Most ZBook laptops use **Fn + F3/F4** (or keys with a sun icon) to decrease/increase brightness.
   * Make sure **Fn lock** isn’t reversed (some models require pressing just F3/F4 if Fn lock is enabled).

2. **Windows Settings**

   * Go to **Start → Settings → System → Display**.
   * Under *Brightness and color*, drag the **Brightness slider**.

3. **Action Center**

   * Press **Win + A** to open Quick Settings.
   * Use the brightness slider at the bottom.

4. **HP Hotkey Support / HP Command Center**

   * Some ZBooks need the **HP Hotkey Support** driver or HP Command Center app for function keys to work properly.

---

### Why Brightness Control Sometimes Doesn’t Work

1. **Display type differences**

   * If your ZBook is connected to an **external monitor**, brightness is controlled via the monitor’s hardware buttons/OSD menu, not Windows.
   * Some workstation displays (DreamColor panels) use **special drivers** that may override Windows’ default controls.

2. **Driver issues**

   * Outdated or missing **Intel Graphics** or **NVIDIA/AMD drivers** can block brightness control.
   * The “Microsoft Basic Display Adapter” fallback driver will remove brightness options.

3. **Power plan settings**

   * In rare cases, power management or adaptive brightness settings may interfere.
   * Check: **Control Panel → Power Options → Change plan settings → Advanced settings → Display → Enable adaptive brightness**.

4. **BIOS/firmware**

   * Some ZBooks need BIOS updates for brightness hotkeys to function consistently.
   * In BIOS, check that **Action Keys Mode** is enabled (so brightness works without pressing Fn).

---

### Fix Checklist

* Update **HP Hotkey Support** driver from HP Support site.
* Update **Intel/NVIDIA/AMD graphics drivers**.
* Make sure you’re adjusting brightness on the **built-in screen**, not an external monitor.
* Check BIOS settings for **Action Keys Mode**.
* Disable or enable **adaptive brightness** if brightness behaves strangely.
* Restart after driver updates—brightness controls sometimes reappear after reboot.

---

👉 Would you like me to give you **step-by-step driver update instructions for HP ZBook** (Intel/NVIDIA/AMD + HP Hotkey driver), so you can fix it permanently?