---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-code-fast-1
title: समय सीमा के साथ उपप्रक्रिया आउटपुट की निगरानी करें
translated: true
type: note
---

```python
import subprocess
import threading
import queue
import time
import sys

def read_output(proc, output_queue):
    """थ्रेड फ़ंक्शन जो stdout और stderr को पढ़ता है, कतार में डालता है।"""
    try:
        for line in iter(proc.stdout.readline, b''):
            if not line:
                break
            output_queue.put(line.decode('utf-8', errors='ignore').rstrip())
        # stderr की भी जाँच करें यदि आवश्यक हो
        for line in iter(proc.stderr.readline, b''):
            if not line:
                break
            output_queue.put(line.decode('utf-8', errors='ignore').rstrip())
    except Exception as e:
        output_queue.put(f"Error reading output: {e}")

def main():
    # चलाने के लिए कमांड (उदाहरण के लिए, Windows पर 'mvn clean compile')
    cmd = ['mvn', 'clean', 'compile']  # आवश्यकतानुसार समायोजित करें, उदाहरण के लिए ['cmd', '/c', 'mvn build']
    timeout_seconds = 10

    # सबप्रोसेस शुरू करें
    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        bufsize=1,  # लाइन बफर्ड
        universal_newlines=False,  # बाइट्स को हैंडल करें
        cwd=None  # कार्यशील निर्देशिका सेट करें यदि आवश्यक हो
    )

    # आउटपुट के लिए कतार
    output_queue = queue.Queue()

    # आउटपुट पढ़ने के लिए थ्रेड शुरू करें
    output_thread = threading.Thread(target=read_output, args=(proc, output_queue))
    output_thread.daemon = True
    output_thread.start()

    print("कमांड शुरू की गई। आउटपुट की हर 10 सेकंड में निगरानी की जा रही है...")

    while proc.poll() is None:
        try:
            # टाइमआउट के साथ आउटपुट की प्रतीक्षा करें
            output = output_queue.get(timeout=timeout_seconds)
            print(f"Output: {output}")  # वैकल्पिक: आउटपुट प्रिंट या प्रोसेस करें
        except queue.Empty:
            print(f"{timeout_seconds} सेकंड से कोई आउटपुट नहीं। कमांड समाप्त कर रहा हूं और बाहर निकल रहा हूं।")
            proc.terminate()  # या जबरदस्ती बंद करने के लिए proc.kill()
            try:
                proc.wait(timeout=5)  # सहज शटडाउन के लिए थोड़ी प्रतीक्षा करें
            except subprocess.TimeoutExpired:
                proc.kill()
            sys.exit(1)

    # प्रक्रिया सामान्य रूप से समाप्त हो गई है
    print("कमांड पूरी हो गई।")
    output_thread.join()  # आउटपुट थ्रेड के समाप्त होने की प्रतीक्षा करें

if __name__ == "__main__":
    main()
```

### व्याख्या
- **सबप्रोसेस**: `mvn clean compile` चलाने के लिए `subprocess.Popen` का उपयोग करता है (आवश्यकतानुसार कमांड समायोजित करें; सरल `mvn build` के लिए, यह `['mvn', 'build']` हो सकता है या यदि आवश्यक हो तो `cmd /c` में लपेटा जा सकता है)। इसे stdout और stderr के लिए पाइपों के साथ अतुल्यकालिक रूप से चलाया जाता है।
- **कतार थ्रेडिंग**: एक अलग थ्रेड stdout और stderr से लाइन दर लाइन (एक बार में पूरा आउटपुट पढ़ने से बचने के लिए) पढ़ता है, इसे डिकोड करता है, और लाइनों को `queue.Queue` में डालता है। यह गैर-ब्लॉकिंग रीड की अनुमति देता है।
- **टाइमआउट मॉनिटरिंग**: मुख्य थ्रेड में, `get(timeout=10)` के साथ नए आउटपुट के लिए कतार की जाँच करें। यदि 10 सेकंड में कोई आउटपुट नहीं आता है, तो सबप्रोसेस को समाप्त करें और बाहर निकलें।
- **विंडोज संगतता**: `subprocess` विंडोज पर काम करता है। यदि कमांड को शेल की आवश्यकता होती है (उदाहरण के लिए, `mvn` के लिए यदि PATH में नहीं है), तो आप `shell=True` सेट कर सकते हैं और कमांड को स्ट्रिंग के रूप में पास कर सकते हैं: `proc = subprocess.Popen("mvn clean compile", shell=True, ...)`।
- **एज केस**: यदि प्रक्रिया प्रतीक्षा के दौरान सामान्य रूप से बाहर निकल जाती है, तो लूप रुक जाता है और हम थ्रेड में शामिल हो जाते हैं। थ्रेड डेमोनिक है ताकि बाहर निकलने पर लटकने से बचा जा सके।
- **अनुकूलन**: आप आउटपुट को अलग तरह से प्रोसेस करने के लिए संशोधित कर सकते हैं (उदाहरण के लिए, प्रिंट करने के बजाय फ़ाइल में लॉग करें)। stderr के लिए, इसे एक ही कतार में जोड़ा जाता है; यदि आवश्यक हो तो आप अलग कर सकते हैं। यदि आउटपुट बाइनरी हैं, तो डिकोडिंग समायोजित करें।