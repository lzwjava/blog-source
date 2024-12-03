---
layout: post
title: "Developer Mode of iOS and ideviceinstaller"
---

## Developer Mode

I was once an iOS developer for some time. But my career focus has shifted to other technologies. However, it is still very useful to apply iOS development knowledge even though I am not a professional iOS developer now.

Recently, I wanted to share my installed apps. But if I took screenshots of all apps from the home screen or from the app list in settings, it would be a mess. So I needed to find a way to view all installed apps.

Here are the steps to view all installed apps using Xcode:

1. Connect your iPhone to your Mac via USB
2. Open Xcode
3. Go to Window → Devices and Simulators (or press Shift + Cmd + 2)
4. Select your iPhone from the left sidebar
5. In the main panel, scroll down to the "Installed Apps" section

It has other useful functions:

1. Taking screenshots
2. Opening recent logs 
3. Opening the console

## xcrun

```bash
(base) lzwjava@192 Downloads % xcrun devicectl device info apps --device 00008120-xxxx --verbose
Using verbose logging.
2024-12-03 16:24:18.579+0800  Enabling developer disk image services.
2024-12-03 16:24:18.637+0800  Acquired usage assertion.
Apps installed:
  - 0 elements

Command Completed, took 0.120 seconds
```


## ideviceinstaller

```bash
brew install ideviceinstaller
ideviceinstaller -l
```

```bash
(base) lzwjava@192 Downloads % ideviceinstaller -l
CFBundleIdentifier, CFBundleVersion, CFBundleDisplayName
com.huawei.smarthome-ios, "14.1.1.325", "HUAWEI AI Life"
com.sf-express.waybillcn, "9.70.0.1", "顺丰速运"
com.roblox.robloxmobile, "2.652.762", "Roblox"
co.alphaexploration.clubhouse, "3273", "Clubhouse"
com.dbs.mbanking.cn, "11", "DBS digibank"
global.longbridge.ios, "59579", "Longbridge"
imgurmobile, "416", "Imgur"
com.creditkarma.mobile, "17316145", "Credit Karma"
...
```

