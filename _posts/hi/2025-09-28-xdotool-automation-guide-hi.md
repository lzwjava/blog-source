---
audio: false
generated: true
image: false
lang: hi
layout: post
model: anthropic/claude-sonnet-4
title: एक्सडोटूल कमांड लाइन ऑटोमेशन गाइड
translated: true
type: note
---

## xdotool क्या है?

xdotool एक कमांड-लाइन ऑटोमेशन टूल है जो X11 (Linux डेस्कटॉप एनवायरनमेंट) के लिए बनाया गया है, जो आपको यह करने की अनुमति देता है:
- माउस की गतिविधियों और क्लिक्स को नियंत्रित करना
- एप्लिकेशन्स को कीस्ट्रोक्स भेजना
- विंडोज़ को मैनिपुलेट करना (मूव, रीसाइज़, फोकस)
- विभिन्न मानदंडों के आधार पर विंडोज़ को खोजना
- डेस्कटॉप इंटरैक्शन को प्रोग्रामेटिक रूप से ऑटोमेट करना

## इंस्टालेशन

```bash
# Ubuntu/Debian
sudo apt install xdotool

# Fedora/RHEL/CentOS
sudo dnf install xdotool

# Arch Linux
sudo pacman -S xdotool

# सोर्स से
git clone https://github.com/jordansissel/xdotool
cd xdotool
make
sudo make install
```

## कोर कमांड्स

### विंडो इनफॉर्मेशन कमांड्स

#### `getactivewindow`
वर्तमान में एक्टिव/फोकस्ड विंडो की विंडो ID प्राप्त करता है।
```bash
xdotool getactivewindow
# आउटपुट: 52428807 (विंडो ID)

# एक्टिव विंडो का टाइटल प्राप्त करें
xdotool getactivewindow getwindowname
```

#### `getwindowfocus`
getactivewindow के समान है, लेकिन कुछ विंडो मैनेजर्स में अलग व्यवहार कर सकता है।
```bash
xdotool getwindowfocus
```

#### `getwindowname`
विंडो का टाइटल/नाम प्राप्त करता है।
```bash
# एक्टिव विंडो का नाम प्राप्त करें
xdotool getactivewindow getwindowname

# विशिष्ट विंडो ID का नाम प्राप्त करें
xdotool getwindowname 52428807
```

#### `getwindowpid`
विंडो से जुड़ी प्रक्रिया ID (PID) प्राप्त करता है।
```bash
xdotool getactivewindow getwindowpid
```

#### `getwindowgeometry`
विंडो की स्थिति और आकार की जानकारी प्राप्त करता है।
```bash
xdotool getactivewindow getwindowgeometry
# आउटपुट: Window 52428807
#   Position: 100,50 (screen: 0)
#   Geometry: 800x600
```

#### `getdisplaygeometry`
स्क्रीन/डिस्प्ले के आयाम प्राप्त करता है।
```bash
xdotool getdisplaygeometry
# आउटपुट: 1920x1080
```

### विंडो सर्च और सिलेक्शन

#### `search`
विभिन्न मानदंडों के आधार पर विंडोज़ को खोजता है।
```bash
# विंडो नाम/टाइटल के आधार पर खोजें
xdotool search --name "Firefox"
xdotool search --name "Terminal"

# क्लास नाम के आधार पर खोजें
xdotool search --class "firefox"

# केस-इनसेंसिटिव खोज
xdotool search --name --onlyvisible --maxdepth 1 "terminal"

# सामान्य सर्च ऑप्शन:
# --name: विंडो टाइटल खोजें
# --class: विंडो क्लास नाम खोजें
# --classname: विंडो क्लास इंस्टेंस नाम खोजें
# --onlyvisible: केवल दृश्यमान विंडोज़
# --maxdepth N: सर्च की गहराई सीमित करें
# --limit N: परिणामों की संख्या सीमित करें
# --desktop N: विशिष्ट डेस्कटॉप/वर्कस्पेस पर खोजें
```

#### `selectwindow`
इंटरएक्टिव विंडो सिलेक्शन (सिलेक्ट करने के लिए क्लिक करें)।
```bash
xdotool selectwindow
# इसकी ID प्राप्त करने के लिए किसी भी विंडो पर क्लिक करें
```

### माउस कंट्रोल

#### `click`
माउस क्लिक्स को सिम्युलेट करता है।
```bash
# वर्तमान स्थिति पर लेफ्ट क्लिक
xdotool click 1

# राइट क्लिक
xdotool click 3

# मिडिल क्लिक
xdotool click 2

# डबल क्लिक
xdotool click --repeat 2 1

# विशिष्ट निर्देशांक पर क्लिक करें
xdotool mousemove 500 300 click 1

# डिले के साथ क्लिक करें
xdotool click --delay 500 1
```

#### `getmouselocation`
वर्तमान माउस कर्सर की स्थिति प्राप्त करता है।
```bash
xdotool getmouselocation
# आउटपुट: x:500 y:300 screen:0 window:52428807

# केवल निर्देशांक प्राप्त करें
xdotool getmouselocation --shell
# आउटपुट: X=500 Y=300 SCREEN=0 WINDOW=52428807
```

#### माउस मूवमेंट
```bash
# माउस को एब्सोल्यूट पोजीशन पर ले जाएँ
xdotool mousemove 500 300

# माउस को वर्तमान स्थिति के सापेक्ष ले जाएँ
xdotool mousemove_relative 10 -20

# एक कमांड में मूव और क्लिक करें
xdotool mousemove 500 300 click 1
```

### कीबोर्ड इनपुट

#### `key`
एक्टिव विंडो को कीस्ट्रोक्स भेजता है।
```bash
# सिंगल की भेजें
xdotool key Return
xdotool key Escape
xdotool key Tab

# की कॉम्बिनेशन भेजें
xdotool key ctrl+c
xdotool key ctrl+alt+t
xdotool key shift+F10

# अनुक्रम में एकाधिक की भेजें
xdotool key ctrl+l type "https://google.com" key Return

# सामान्य की नाम:
# - लेटर्स: a, b, c, ... (लोअरकेस)
# - नंबर्स: 1, 2, 3, ...
# - स्पेशल: Return, Escape, Tab, space, BackSpace, Delete
# - फंक्शन: F1, F2, ... F12
# - मॉडिफायर्स: ctrl, alt, shift, super (Windows key)
# - एरो: Up, Down, Left, Right
```

#### टेक्स्ट इनपुट
```bash
# टेक्स्ट टाइप करें (प्रत्येक कैरेक्टर को टाइप करने का अनुकरण करता है)
xdotool type "Hello World"

# कैरेक्टर्स के बीच डिले के साथ टाइप करें
xdotool type --delay 100 "Slow typing"

# फास्ट टाइपिंग के लिए डिले क्लियर करें
xdotool type --clearmodifiers --delay 0 "Fast text"
```

### विंडो मैनिपुलेशन

```bash
# किसी विंडो पर फोकस/एक्टिवेट करें
xdotool windowactivate WINDOW_ID

# विंडो को मिनिमाइज़ करें
xdotool windowminimize WINDOW_ID

# विंडो को मैक्सिमाइज़ करें
xdotool windowmaximize WINDOW_ID

# विंडो बंद करें
xdotool windowclose WINDOW_ID

# विंडो को पोजीशन पर ले जाएँ
xdotool windowmove WINDOW_ID 100 50

# विंडो का आकार बदलें
xdotool windowsize WINDOW_ID 800 600

# विंडो को विशिष्ट डेस्कटॉप पर ले जाएँ
xdotool set_desktop_for_window WINDOW_ID 2

# विंडो को टॉप पर लाएँ
xdotool windowraise WINDOW_ID

# विंडो को मैप करें (दिखाएँ)
xdotool windowmap WINDOW_ID

# विंडो को अनमैप करें (छिपाएँ)
xdotool windowunmap WINDOW_ID
```

### एडवांस्ड फीचर्स

#### `behave`
विंडो इवेंट व्यवहार (ट्रिगर्स) सेट अप करता है।
```bash
# जब विंडो फोकस प्राप्त करे तो कमांड एक्सेक्यूट करें
xdotool behave WINDOW_ID focus exec echo "Window focused"

# जब विंडो बने तो एक्सेक्यूट करें
xdotool behave WINDOW_ID create exec "notify-send 'New window'"

# उपलब्ध इवेंट्स: focus, unfocus, mouse-enter, mouse-leave, create, destroy
```

#### `behave_screen_edge`
माउस के स्क्रीन एज तक पहुँचने पर एक्शन्स ट्रिगर करता है।
```bash
# जब माउस लेफ्ट एज को हिट करे तो कमांड एक्सेक्यूट करें
xdotool behave_screen_edge left exec "echo 'Left edge hit'"

# उपलब्ध एज: left, right, top, bottom
```

## प्रैक्टिकल उदाहरण

### बेसिक ऑटोमेशन स्क्रिप्ट्स

#### टर्मिनल खोलें और कमांड रन करें
```bash
#!/bin/bash
# टर्मिनल खोलें और ls कमांड रन करें
xdotool key ctrl+alt+t
sleep 1
xdotool type "ls -la"
xdotool key Return
```

#### एक्टिव विंडो का स्क्रीनशॉट लें
```bash
#!/bin/bash
WINDOW=$(xdotool getactivewindow)
NAME=$(xdotool getwindowname $WINDOW | sed 's/[^a-zA-Z0-9]/_/g')
import -window $WINDOW "screenshot_${NAME}.png"
```

#### विशिष्ट एप्लिकेशन पर फोकस करें
```bash
#!/bin/bash
# Firefox पर फोकस करें या यदि नहीं चल रहा है तो खोलें
WINDOW=$(xdotool search --onlyvisible --class "firefox" | head -1)
if [ -n "$WINDOW" ]; then
    xdotool windowactivate $WINDOW
else
    firefox &
fi
```

### विंडो मैनेजमेंट स्क्रिप्ट्स

#### विंडोज़ को साइड बाय साइड टाइल करें
```bash
#!/bin/bash
# स्क्रीन ज्योमेट्री प्राप्त करें
eval $(xdotool getdisplaygeometry --shell)
HALF_WIDTH=$((WIDTH / 2))

# दो सबसे रीसेंट विंडोज़ प्राप्त करें
WINDOWS=($(xdotool search --onlyvisible --maxdepth 1 "" | tail -2))

# पहली विंडो को बाईं ओर पोजिशन करें
xdotool windowsize ${WINDOWS[0]} $HALF_WIDTH $HEIGHT
xdotool windowmove ${WINDOWS[0]} 0 0

# दूसरी विंडो को दाईं ओर पोजिशन करें
xdotool windowsize ${WINDOWS[1]} $HALF_WIDTH $HEIGHT
xdotool windowmove ${WINDOWS[1]} $HALF_WIDTH 0
```

#### एक्टिव विंडो को सेंटर करें
```bash
#!/bin/bash
WINDOW=$(xdotool getactivewindow)
eval $(xdotool getdisplaygeometry --shell)
eval $(xdotool getwindowgeometry --shell $WINDOW)

NEW_X=$(((WIDTH - WINDOW_WIDTH) / 2))
NEW_Y=$(((HEIGHT - WINDOW_HEIGHT) / 2))

xdotool windowmove $WINDOW $NEW_X $NEW_Y
```

### एप्लिकेशन-स्पेसिफिक ऑटोमेशन

#### ब्राउज़र ऑटोमेशन
```bash
#!/bin/bash
# नया टैब खोलें और नेविगेट करें
xdotool key ctrl+t
sleep 0.5
xdotool type "github.com"
xdotool key Return
```

#### टेक्स्ट एडिटर ऑटोमेशन
```bash
#!/bin/bash
# सभी सिलेक्ट करें और क्लिपबोर्ड पर कॉपी करें
xdotool key ctrl+a
sleep 0.1
xdotool key ctrl+c
```

## टिप्स और बेस्ट प्रैक्टिसेज़

### टाइमिंग और डिलेज़
```bash
# धीमे एप्लिकेशन्स के लिए डिलेज़ जोड़ें
xdotool key ctrl+alt+t
sleep 2  # टर्मिनल के खुलने का इंतज़ार करें
xdotool type "echo hello"

# xdotool के बिल्ट-इन डिलेज़ का उपयोग करें
xdotool key --delay 100 ctrl+alt+t
```

### एरर हैंडलिंग
```bash
#!/bin/bash
# किसी विंडो पर कार्य करने से पहले जांचें कि वह मौजूद है या नहीं
WINDOW=$(xdotool search --name "MyApp" 2>/dev/null)
if [ -n "$WINDOW" ]; then
    xdotool windowactivate $WINDOW
else
    echo "Window not found"
    exit 1
fi
```

### मल्टीपल विंडोज़ के साथ कार्य करना
```bash
#!/bin/bash
# किसी विशिष्ट एप्लिकेशन की सभी विंडोज़ पर कार्य करें
xdotool search --name "Firefox" | while read WINDOW; do
    xdotool windowactivate $WINDOW
    xdotool key F5  # Refresh
    sleep 0.5
done
```

### डीबगिंग
```bash
# वर्बोज़ आउटपुट सक्षम करें
xdotool --verbose key Return

# विस्तृत विंडो जानकारी प्राप्त करें
xdotool search --name "Terminal" getwindowgeometry getwindowname getwindowpid
```

## सामान्य उपयोग के मामले

1. **विंडो मैनेजमेंट**: विंडोज़ को प्रोग्रामेटिक रूप से फोकस, मूव, रीसाइज़ करना
2. **एप्लिकेशन टेस्टिंग**: GUI टेस्टिंग सिनेरियो को ऑटोमेट करना
3. **प्रेजेंटेशन टूल्स**: स्लाइड नेविगेशन और विंडो स्विचिंग को ऑटोमेट करना
4. **गेमिंग मैक्रोज़**: दोहराए जाने वाले गेमिंग टास्क्स को ऑटोमेट करना
5. **एक्सेसिबिलिटी**: विकलांग उपयोगकर्ताओं के लिए कस्टम इनपुट मेथड्स बनाना
6. **सिस्टम एडमिनिस्ट्रेशन**: GUI-आधारित एडमिन टास्क्स को ऑटोमेट करना
7. **डेवलपमेंट टूल्स**: IDE और डेवलपमेंट वर्कफ़्लो के साथ इंटीग्रेट करना

## ट्रबलशूटिंग

### सामान्य समस्याएं

- **कमांड्स काम नहीं कर रही**: सुनिश्चित करें कि X11 चल रहा है (Wayland नहीं)
- **परमिशन इशूज़**: कुछ ऑपरेशन्स के लिए उचित उपयोगकर्ता अनुमतियों की आवश्यकता हो सकती है
- **विंडो नहीं मिली**: सत्यापित करने के लिए `xdotool search` का उपयोग करें कि विंडो मौजूद है और दृश्यमान है
- **टाइमिंग इशूज़**: कमांड्स के बीच उचित डिलेज़ जोड़ें
- **स्पेशल कैरेक्टर्स**: टेक्स्ट इनपुट में स्पेशल कैरेक्टर्स के लिए उचित एस्केपिंग का उपयोग करें

### सुरक्षा संबंधी विचार

- xdotool किसी भी एप्लिकेशन को नियंत्रित कर सकता है, सावधानी से उपयोग करें
- अविश्वसनीय xdotool स्क्रिप्ट्स को रन करने से बचें
- संवेदनशील डेटा को हैंडल करने वाले ऑटोमेशन के साथ सावधान रहें
- `xdotool` का उपयोग केवल नियंत्रित वातावरण में करने पर विचार करें

यह गाइड xdotool की आवश्यक और उन्नत सुविधाओं को कवर करती है। अपनी विशिष्ट आवश्यकताओं के अनुरूप शक्तिशाली डेस्कटॉप ऑटोमेशन स्क्रिप्ट्स बनाने के लिए इन कमांड्स के साथ प्रयोग करें।