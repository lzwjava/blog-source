---
audio: false
generated: true
lang: hi
layout: post
title: गिट स्टैश
translated: true
type: note
---

यहां बताया गया है कि कैसे `git stash` का प्रभावी ढंग से उपयोग करें और बिना कमिट किए गए बदलावों के साथ बार-बार branches/tags स्विच करें:

## `git stash` का उपयोग करना

`git stash` एक शक्तिशाली कमांड है जो आपको आपके बिना कमिट किए गए बदलावों (staged और unstaged दोनों) को अस्थायी रूप से सहेजने और आपके working directory को अंतिम commit पर वापस लौटाने की अनुमति देता है। यह तब उपयोगी होता है जब आपको अपने वर्तमान, अधूरे काम को कमिट किए बिना किसी दूसरी branch पर स्विच करने या कुछ और काम करने की आवश्यकता होती है।

यहां सामान्य `git stash` ऑपरेशनों का विवरण दिया गया है:

**1. अपने वर्तमान बदलावों को stash करना:**

```bash
git stash
```

यह कमांड आपके बिना कमिट किए गए बदलावों को लेती है, उन्हें एक नए stash के रूप में सहेजती है, और आपके working directory को साफ करती है। आपको इस तरह का एक संदेश दिखाई देगा:

```
Saved working directory and index state WIP on <your_branch>: <commit_hash> <commit_message>
```

**2. एक संदेश के साथ stash करना:**

अपने stashes में एक वर्णनात्मक संदेश जोड़ना मददगार होता है, खासकर यदि आपके पास कई हैं:

```bash
git stash save "आपका वर्णनात्मक संदेश"
# या
git stash push -m "आपका वर्णनात्मक संदेश"
```

**3. अपने stashes की सूची देखना:**

आपके सभी सहेजे गए stashes की सूची देखने के लिए, उपयोग करें:

```bash
git stash list
```

यह stashes की एक सूची प्रदर्शित करेगा, आमतौर पर इस फॉर्मेट में:

```
stash@{0}: On <branch_name>: <commit_hash> <stash_message>
stash@{1}: WIP on <another_branch>: ...
```

`stash@{0}` सबसे हालिया stash है।

**4. एक stash को apply करना:**

किसी stash से बदलावों को वापस लाने के लिए, आप `git stash apply` का उपयोग कर सकते हैं। यह बदलावों को apply करता है लेकिन stash को सूची में रखता है। डिफ़ॉल्ट रूप से, यह नवीनतम stash (`stash@{0}`) apply करता है।

```bash
git stash apply
# या किसी विशिष्ट stash को apply करने के लिए:
git stash apply stash@{1}
```

**5. एक stash को apply करना और हटाना:**

यदि आप बदलावों को apply करना चाहते हैं और तुरंत stash को सूची से हटाना चाहते हैं, तो `git stash pop` का उपयोग करें। यह भी डिफ़ॉल्ट रूप से नवीनतम stash पर काम करता है।

```bash
git stash pop
# या किसी विशिष्ट stash को pop करने के लिए:
git stash pop stash@{1}
```

**6. stash विवरण देखना:**

आप किसी stash में बदलावों का सारांश देख सकते हैं:

```bash
git stash show
# या किसी विशिष्ट stash के लिए:
git stash show stash@{2}
```

किसी stash का पूरा diff देखने के लिए, `-p` या `--patch` फ्लैग जोड़ें:

```bash
git stash show -p stash@{0}
```

**7. untracked files को stash करना:**

डिफ़ॉल्ट रूप से, `git stash` केवल tracked files में बदलावों को stash करता है। untracked files को शामिल करने के लिए, `-u` या `--include-untracked` विकल्प का उपयोग करें:

```bash
git stash -u
git stash save -u "stash with untracked"
```

**8. ignored files को भी stash करना:**

untracked और ignored files दोनों को शामिल करने के लिए, `-a` या `--all` विकल्प का उपयोग करें:

```bash
git stash -a
git stash save -a "stash with all"
```

**9. एक stash से एक branch बनाना:**

यदि आपने कुछ बदलाव stash किए हैं और अब उन पर एक नई branch में काम करना चाहते हैं, तो आप सीधे stash से एक branch बना सकते हैं:

```bash
git stash branch <new_branch_name> stash@{0}
# या नवीनतम stash के लिए:
git stash branch <new_branch_name>
```

यह कमांड उस commit के आधार पर एक नई branch बनाती है जहां stash बनाया गया था, stashed बदलावों को नई branch पर apply करती है, और फिर stash को drop कर देती है।

**10. Stashes को हटाना:**

* किसी विशिष्ट stash को हटाने के लिए:
    ```bash
    git stash drop stash@{1}
    ```
* सभी stashes को हटाने के लिए:
    ```bash
    git stash clear
    ```

## बिना कमिट किए गए बदलावों के साथ बार-बार Branches या Tags स्विच करना

यहां बताया गया है कि कैसे `git stash` का उपयोग branches या tags के बीच बार-बार स्विच करने की सुविधा प्रदान करने के लिए करें, जब आपके पास बिना कमिट किए गए बदलाव हों:

**परिदृश्य 1: किसी दूसरी branch पर स्विच करना**

1.  **अपने वर्तमान बदलावों को stash करें:**
    ```bash
    git stash save "WIP on current branch"
    ```
2.  **Target branch पर स्विच करें:**
    ```bash
    git checkout <target_branch_name>
    # या नए `git switch` कमांड का उपयोग करके:
    git switch <target_branch_name>
    ```
3.  **Target branch पर अपना काम करें।**
4.  **जब आपको अपनी मूल branch पर वापस जाने की आवश्यकता हो:**
    ```bash
    git checkout <original_branch_name>
    # या
    git switch <original_branch_name>
    ```
5.  **अपने stashed बदलावों को फिर से apply करें:**
    ```bash
    git stash pop  # यदि आप stash को apply और remove करना चाहते हैं
    # या
    git stash apply # यदि आप stash को apply करके रखना चाहते हैं
    ```
6.  **किसी भी संभावित merge conflicts को resolve करें** जो तब उत्पन्न हो सकते हैं यदि मूल branch आपके stash बनाने के बाद से काफी हद तक अलग हो गई है।

**परिदृश्य 2: किसी tag पर स्विच करना**

किसी tag पर सीधे स्विच करने से आप एक "detached HEAD" स्थिति में आ जाते हैं, जो आमतौर पर commits बनाने के लिए अनुशंसित नहीं है। यदि आप केवल किसी विशिष्ट tag पर कोड का निरीक्षण करना चाहते हैं:

1.  **अपने वर्तमान बदलावों को stash करें:**
    ```bash
    git stash save "WIP before tag inspection"
    ```
2.  **Tag पर स्विच करें:**
    ```bash
    git checkout <tag_name>
    ```
3.  **कोड का निरीक्षण करें।**
4.  **अपनी branch पर वापस जाने के लिए:**
    ```bash
    git checkout <your_branch_name>
    # या
    git switch <your_branch_name>
    ```
5.  **अपने stashed बदलावों को फिर से apply करें:**
    ```bash
    git stash pop
    # या
    git stash apply
    ```

**परिदृश्य 3: अपने stashed बदलावों के साथ किसी tag से एक नई branch बनाना**

यदि आप किसी विशिष्ट tag के आधार पर एक नई feature या fix पर काम शुरू करना चाहते हैं, और आपके पास पिछले context से stashed बदलाव हैं:

1.  **अपने वर्तमान बदलावों को stash करें (यदि आपने पहले से नहीं किया है):**
    ```bash
    git stash save "WIP"
    ```
2.  **Tag से एक नई branch बनाएं:**
    ```bash
    git checkout -b <new_branch_name> <tag_name>
    # या
    git switch -c <new_branch_name> <tag_name>
    ```
3.  **अपने stashed बदलावों को नई branch पर apply करें:**
    ```bash
    git stash pop # या git stash apply
    ```
4.  **किसी भी संभावित merge conflicts को resolve करें।**

**महत्वपूर्ण विचार:**

* **अपने stashes को व्यवस्थित रखें:** अपने stashes को आसानी से पहचानने के लिए वर्णनात्मक संदेशों का उपयोग करें।
* **Stash स्थानीय होता है:** Stashes आपके repository में स्थानीय रूप से संग्रहीत होते हैं और remote repositories पर push नहीं किए जाते हैं।
* **Conflicts की संभावना:** जब आप किसी stash को फिर से apply करते हैं, तो merge conflicts की संभावना होती है यदि वह branch जिस पर आप apply कर रहे हैं, आपके stash बनाने के बाद से महत्वपूर्ण रूप से बदल गई है। आपको इन conflicts को मैन्युअल रूप से resolve करने की आवश्यकता होगी।
* **अस्थायी branches बनाने पर विचार करें:** दीर्घकालिक काम के लिए जो आप commit करने के लिए तैयार नहीं हैं, stashes पर भारी निर्भरता के बजाय एक अस्थायी branch बनाना बेहतर दृष्टिकोण हो सकता है। आप आसानी से branches के बीच स्विच कर सकते हैं और अपनी प्रगति commit कर सकते हैं।

`git stash` का प्रभावी ढंग से उपयोग करके, आप branches और tags के बीच सहजता से स्विच कर सकते हैं, भले ही आपके पास बिना कमिट किए गए बदलाव हों, जिससे एक अधिक लचीला और कुशल workflow सक्षम होता है। अपने stashes को प्रबंधित करना याद रखें और संभावित merge conflicts को संभालने के लिए तैयार रहें।