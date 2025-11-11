---
audio: false
generated: true
lang: hi
layout: post
title: टॉर्टॉइसगिट को गिट मर्जटूल के रूप में कॉन्फ़िगर करना
translated: true
type: note
---

Git में TortoiseGit को merge टूल के रूप में कॉन्फ़िगर करने के लिए, आपको अपनी Git कॉन्फ़िगरेशन में TortoiseGitMerge (TortoiseGit के साथ शामिल merge टूल) को सेट अप करना होगा। इसे प्राप्त करने के चरण नीचे दिए गए हैं:

### पूर्वापेक्षाएँ
- सुनिश्चित करें कि TortoiseGit आपके सिस्टम पर इंस्टॉल है। आप इसे [tortoisegit.org](https://tortoisegit.org) से डाउनलोड कर सकते हैं।
- सत्यापित करें कि TortoiseGitMerge executable उपलब्ध है (आमतौर पर `C:\Program Files\TortoiseGit\bin\TortoiseGitMerge.exe` पर स्थित होता है)।

### Git Mergetool के रूप में TortoiseGitMerge को कॉन्फ़िगर करने के चरण

1.  **कमांड प्रॉम्प्ट या Git Bash खोलें**
    - आप आवश्यक Git कॉन्फ़िगरेशन कमांड चलाने के लिए Windows Command Prompt, PowerShell, या Git Bash का उपयोग कर सकते हैं।

2.  **Merge टूल के रूप में TortoiseGitMerge सेट करें**
    Git को TortoiseGitMerge का उपयोग करने के लिए कॉन्फ़िगर करने हेतु निम्नलिखित कमांड चलाएँ:

    ```bash
    git config --global merge.tool tortoisegitmerge
    git config --global mergetool.tortoisemerge.cmd "\"C:/Program Files/TortoiseGit/bin/TortoiseGitMerge.exe\" -base:\"$BASE\" -theirs:\"$REMOTE\" -mine:\"$LOCAL\" -merged:\"$MERGED\""
    ```

    **स्पष्टीकरण**:
    - `merge.tool tortoisegitmerge`: merge टूल का नाम `tortoisegitmerge` सेट करता है (आप कोई भी नाम चुन सकते हैं, लेकिन यह एक परंपरा है)।
    - `mergetool.tortoisemerge.cmd`: TortoiseGitMerge को उचित पैरामीटर्स के साथ चलाने का कमांड निर्दिष्ट करता है:
      - `-base:"$BASE"`: सामान्य पूर्वज फ़ाइल।
      - `-theirs:"$REMOTE"`: merge किए जा रहे ब्रांच से फ़ाइल।
      - `-mine:"$LOCAL"`: आपकी वर्तमान ब्रांच से फ़ाइल।
      - `-merged:"$MERGED"`: आउटपुट फ़ाइल जहाँ हल किया गया merge सहेजा जाएगा।
    - पथ में फॉरवर्ड स्लैश (`/`) का उपयोग करें और आवश्यकतानुसार quotes को escape करें, खासकर यदि पथ में स्पेस हैं।

    **नोट**: यदि TortoiseGit किसी भिन्न लोकेशन पर इंस्टॉल है (जैसे, `E:/Program Files/TortoiseGit/bin/TortoiseGitMerge.exe`) तो पथ को समायोजित करें।

3.  **वैकल्पिक: Mergetool प्रॉम्प्ट अक्षम करें**
    हर बार `git mergetool` चलाने पर प्रॉम्प्ट होने से बचने के लिए, आप प्रॉम्प्ट को अक्षम कर सकते हैं:

    ```bash
    git config --global mergetool.prompt false
    ```

4.  **वैकल्पिक: सुनिश्चित करें कि TortoiseGitMerge सिस्टम PATH में है**
    यदि Git TortoiseGitMerge को नहीं ढूंढ पा रहा है, तो सुनिश्चित करें कि इसका डायरेक्टरी आपके सिस्टम के PATH एनवायरनमेंट वेरिएबल में शामिल है:
    - "This PC" या "My Computer" पर राइट-क्लिक करें → Properties → Advanced system settings → Environment Variables.
    - "System Variables" के अंतर्गत, `Path` वेरिएबल को ढूंढें और एडिट करें ताकि इसमें `C:\Program Files\TortoiseGit\bin` शामिल हो।
    - वैकल्पिक रूप से, Git कॉन्फ़िगरेशन में स्पष्ट रूप से पथ सेट करें:

      ```bash
      git config --global mergetool.tortoisemerge.path "C:/Program Files/TortoiseGit/bin/TortoiseGitMerge.exe"
      ```

5.  **कॉन्फ़िगरेशन का परीक्षण करें**
    - एक Git रिपॉजिटरी में merge conflict बनाएँ (जैसे, conflict वाले परिवर्तनों वाली दो ब्रांचेज़ को merge करके)।
    - merge टूल लॉन्च करने के लिए निम्नलिखित कमांड चलाएँ:

      ```bash
      git mergetool
      ```

    - TortoiseGitMerge खुलना चाहिए, जो conflict वाली फ़ाइल के base, theirs, और mine वर्जन के साथ तीन-पेन व्यू दिखाता है। नीचे का पेन merge का परिणाम है।

6.  **TortoiseGitMerge में Conflicts को हल करें**
    - तीन-पेन व्यू में, TortoiseGitMerge दिखाता है:
      - **बायाँ पेन**: "theirs" वर्जन (merge की जा रही ब्रांच से)।
      - **दायाँ पेन**: "mine" वर्जन (आपकी वर्तमान ब्रांच से)।
      - **मध्य पेन**: base (सामान्य पूर्वज) वर्जन।
      - **नीचे का पेन**: merge का परिणाम जहाँ आप conflicts को हल करते हैं।
    - conflict वाले सेक्शन पर राइट-क्लिक करके "Use text block from 'theirs'", "Use text block from 'mine'", या मैन्युअल रूप से merge की गई फ़ाइल को एडिट करने जैसे विकल्प चुनें।
    - एक बार हल हो जाने पर, फ़ाइल को सेव करें (File → Save) और TortoiseGitMerge बंद करें।
    - यदि TortoiseGitMerge सफलतापूर्वक बंद होता है (एग्ज़िट कोड 0) तो Git फ़ाइल को हल किया हुआ मार्क कर देगा। यदि प्रॉम्प्ट किया जाए, त conflict को हल किए जाने की पुष्टि करें।

7.  **हल किए गए Merge को कमिट करें**
    Conflicts को हल करने के बाद, परिवर्तनों को कमिट करें:

    ```bash
    git commit
    ```

    **नोट**: यदि conflict रीबेस या चेरी-पिक के दौरान हुआ था, तो स्टैंडर्ड कमिट डायलॉग के बजाय प्रक्रिया जारी रखने के लिए संबंधित TortoiseGit डायलॉग (Rebase या Cherry-pick) का उपयोग करें।[](https://tortoisegit.org/docs/tortoisegit/tgit-dug-conflicts.html)

### TortoiseGit GUI के माध्यम से TortoiseGitMerge का उपयोग करना
यदि आप conflicts को हल करने के लिए TortoiseGit GUI का उपयोग करना पसंद करते हैं:
1. Windows Explorer में conflict वाली फ़ाइल पर राइट-क्लिक करें।
2. **TortoiseGit → Edit Conflicts** चुनें।
3. TortoiseGitMerge खुलेगा, जिससे आप ऊपर बताए अनुसार conflicts को हल कर सकते हैं।
4. सेव करने के बाद, दोबारा राइट-क्लिक करें और फ़ाइल को हल किया हुआ मार्क करने के लिए **TortoiseGit → Resolved** चुनें।
5. TortoiseGit के Commit डायलॉग का उपयोग करके परिवर्तनों को कमिट करें।

### समस्या निवारण
- **त्रुटि: "Unsupported merge tool 'tortoisemerge'"**
  - सुनिश्चित करें कि `TortoiseGitMerge.exe` का पथ सही और एक्सेसिबल है।
  - सत्यापित करें कि टूल का नाम `merge.tool` और `mergetool.<tool>.cmd` कॉन्फ़िगरेशन में बिल्कुल मेल खाता है।
  - जांचें कि TortoiseGitMerge PATH में है या `mergetool.tortoisemerge.path` का उपयोग करके स्पष्ट रूप से सेट है।[](https://stackoverflow.com/questions/5190188/why-cant-i-use-tortoisemerge-as-my-git-merge-tool-on-windows)
- **फ़ाइल पथों में स्पेस**
  - यदि फ़ाइल पथों में स्पेस हैं, तो escape किए गए quotes के साथ कमांड सिंटैक्स (जैसा ऊपर दिखाया गया है) को उन्हें सही तरीके से हैंडल करना चाहिए।[](https://stackoverflow.com/questions/5190188/why-cant-i-use-tortoisemerge-as-my-git-merge-tool-on-windows)
- **Cygwin उपयोगकर्ता**
  - यदि Cygwin का उपयोग कर रहे हैं, तो Cygwin के माउंट पॉइंट का उपयोग करने के लिए पथ को समायोजित करें, जैसे:

    ```bash
    git config --global mergetool.tortoisemerge.cmd '"/cygdrive/c/Program Files/TortoiseGit/bin/TortoiseGitMerge.exe" -base:"$BASE" -theirs:"$REMOTE" -mine:"$LOCAL" -merged:"$MERGED"'
    ```

    यह Cygwin के `/cygdrive/c/` पथ संरचना को ध्यान में रखता है।[](https://devstuffs.wordpress.com/2013/03/08/setting-tortoisegitmerge-in-msysgit-as-the-git-mergetool/)
- **TortoiseGitMerge नहीं मिल रहा**
  - यदि आपने पहले TortoiseSVN के TortoiseMerge का उपयोग किया था, तो सुनिश्चित करें कि आप `TortoiseGitMerge.exe` की ओर इशारा कर रहे हैं, क्योंकि TortoiseGit वर्जन 1.8 में executable का नाम बदल गया था।[](https://devstuffs.wordpress.com/2013/03/08/setting-tortoisegitmerge-in-msysgit-as-the-git-mergetool/)[](https://stackoverflow.com/questions/15881449/why-doesnt-tortoisemerge-work-as-my-mergetool)

### अतिरिक्त नोट्स
- TortoiseGitMerge merge के लिए conflict रेज़ोल्यूशन हेतु तीन-पेन व्यू को सपोर्ट करता है, जो आदर्श है। यह स्वचालित रूप से non-conflicting परिवर्तनों को merge करता है और मैन्युअल रेज़ोल्यूशन के लिए conflicts को हाइलाइट करता है।[](https://tortoisegit.org/docs/tortoisegitmerge/tmerge-dug.html)[](https://manios.org/2018/05/30/git-merge-conflicts-using-tortoise-git-merge-windows)
- यदि आप TortoiseGitMerge को diff टूल के रूप में भी उपयोग करना चाहते हैं, तो इसे इसी तरह कॉन्फ़िगर करें:

  ```bash
  git config --global diff.tool tortoisediff
  git config --global difftool.tortoisediff.cmd "\"C:/Program Files/TortoiseGit/bin/TortoiseGitMerge.exe\" -mine:\"$REMOTE\" -base:\"$LOCAL\""
  ```

  फिर फ़ाइलों की तुलना करने के लिए `git difftool` का उपयोग करें।[](https://stackoverflow.com/questions/16493368/can-tortoisemerge-be-used-as-a-difftool-with-windows-git-bash)
- उन्नत सेटिंग्स के लिए, आप TortoiseGit को merge टूल के बंद होने की प्रतीक्षा करने और एग्ज़िट कोड के आधार पर स्वचालित रूप से फ़ाइलों को हल किया हुआ मार्क करने के लिए कॉन्फ़िगर कर सकते हैं। TortoiseGit Settings → External Programs → Merge Tool में, "Block TortoiseGit while executing the external merge tool" चुनें और "Trust exit code" सक्षम करें।[](https://tortoisegit.org/docs/tortoisegit/tgit-dug-settings.html)

### स्रोत
- TortoiseGit डॉक्यूमेंटेशन:[](https://tortoisegit.org/docs/tortoisegitmerge/tmerge-dug.html)[](https://tortoisegit.org/docs/tortoisegit/tgit-dug-merge.html)[](https://tortoisegit.org/docs/tortoisegit/tgit-dug-conflicts.html)
- Stack Overflow और अन्य वेब संसाधन:[](https://devstuffs.wordpress.com/2013/03/08/setting-tortoisegitmerge-in-msysgit-as-the-git-mergetool/)[](https://stackoverflow.com/questions/5190188/why-cant-i-use-tortoisemerge-as-my-git-merge-tool-on-windows)[](https://stackoverflow.com/questions/16493368/can-tortoisemerge-be-used-as-a-difftool-with-windows-git-bash)

इन चरणों का पालन करके, आपको TortoiseGitMerge को अपने Git mergetool के रूप में प्रभावी ढंग से उपयोग करने में सक्षम होना चाहिए, चाहे कमांड लाइन से या TortoiseGit GUI के माध्यम से।