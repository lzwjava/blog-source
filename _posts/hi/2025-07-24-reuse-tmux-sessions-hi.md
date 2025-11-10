---
audio: false
generated: true
lang: hi
layout: post
title: मौजूदा टीमक्स सत्रों का पुनः उपयोग
translated: true
type: note
---

मौजूदा tmux sessions (जैसे आपके मामले में session `1` या `8`) को फिर से इस्तेमाल करने के लिए, आप tmux शुरू करते समय किसी मौजूदा session से attach कर सकते हैं। यहां बताया गया है कि आप यह कैसे कर सकते हैं:

### समाधान
1. **मौजूदा Sessions की सूची देखें**:
   सभी active sessions देखने के लिए `tmux list-sessions` (या `tmux ls`) चलाएं:
   ```
   tmux list-sessions
   ```
   आउटपुट (आपके उदाहरण से):
   ```
   1: 1 windows (created Thu Jul 10 03:03:47 2025)
   8: 1 windows (created Thu Jul 24 02:11:07 2025)
   ```

2. **किसी विशेष Session से Attach करें**:
   `tmux` चलाने (जो एक नया session बनाता है) के बजाय, किसी मौजूदा session से कनेक्ट करने के लिए `attach-session` (या `attach`) कमांड का उपयोग करें। उदाहरण के लिए:
   - Session `1` से attach करने के लिए:
     ```
     tmux attach-session -t 1
     ```
   - Session `8` से attach करने के लिए:
     ```
     tmux attach-session -t 8
     ```

   आप `attach-session` को `attach` छोटा कर सकते हैं:
   ```
   tmux attach -t 1
   ```

3. **जांचें कि क्या tmux पहले से चल रहा है**:
   यदि आप किसी ऐसे session से attach करने का प्रयास करते हैं जो मौजूद नहीं है, तो tmux एक error देगा। गलती से नया session बनाने से बचने के लिए, आप इसे शुरू करने से पहले जांच सकते हैं कि क्या tmux चल रहा है। उदाहरण के लिए, इसे अपने shell script या workflow में जोड़ें:
   ```
   tmux has-session -t 1 && tmux attach -t 1 || tmux new-session -s 1
   ```
   यह जांचता है कि क्या session `1` मौजूद है; यदि हां, तो यह इससे attach करता है, अन्यथा यह `1` नाम का एक नया session बनाता है।

4. **इसे सुविधाजनक बनाएं**:
   - **सुविधा के लिए Alias**: हमेशा किसी विशेष session से attach करने के लिए अपनी shell configuration (जैसे `~/.zshrc` या `~/.bashrc`) में एक alias जोड़ें:
     ```
     alias tmux1='tmux attach -t 1 || tmux new-session -s 1'
     ```
     फिर, `tmux1` चलाने से session `1` से attach होगा यदि यह मौजूद है या इसे बनाएगा यदि यह मौजूद नहीं है।
   - **डिफ़ॉल्ट Session**: यदि आप हमेशा किसी विशेष session (जैसे `1`) का उपयोग करना चाहते हैं, तो आप इसे स्वचालित करने के लिए एक script बना सकते हैं या अपने `.tmux.conf` को configure कर सकते हैं।

5. **नए Sessions को रोकें**:
   डिफ़ॉल्ट रूप से `tmux` चलाने पर नए sessions बनने से बचने के लिए, आप अपने workflow को हमेशा मौजूदा sessions की जांच करने के लिए configure कर सकते हैं। उदाहरण के लिए, अपनी shell को यह चलाने के लिए संशोधित करें:
   ```
   tmux attach -t 1 2>/dev/null || tmux new-session -s 1
   ```
   यह session `1` से attach करने का प्रयास करता है और errors को दबा देता है यदि यह मौजूद नहीं है, इसे केवल तभी बनाता है जब आवश्यक हो।

6. **वैकल्पिक: स्पष्टता के लिए Sessions के नाम दें**:
   संख्यात्मक session IDs (`1`, `8`, आदि) पर भरोसा करने के बजाय, आसान प्रबंधन के लिए sessions के नाम दे सकते हैं। उदाहरण के लिए:
   ```
   tmux new-session -s mywork
   ```
   फिर बाद में इससे इस तरह attach करें:
   ```
   tmux attach -t mywork
   ```

### ऐसा क्यों होता है
जब आप बिना arguments के `tmux` चलाते हैं, तो यह एक auto-incrementing ID (जैसे `1`, `8`) के साथ एक नया session बनाता है। Session number बढ़ने से रोकने के लिए, आपको `tmux attach -t <session>` का उपयोग करके किसी मौजूदा session से स्पष्ट रूप से attach करना होगा।

### उदाहरण Workflow
हमेशा session `1` का उपयोग करने के लिए:
1. जांचें कि क्या session `1` मौजूद है, इसके लिए `tmux list-sessions` चलाएं।
2. यदि यह मौजूद है, तो `tmux attach -t 1` चलाएं।
3. यदि यह मौजूद नहीं है, तो `tmux new-session -s 1` चलाएं।

आप इसे अपनी shell में स्वचालित कर सकते हैं:
```bash
if tmux has-session -t 1 2>/dev/null; then
  tmux attach -t 1
else
  tmux new-session -s 1
fi
```

### नोट्स
- यदि कोई session पहले से ही कहीं और attached है, तो आपको पहले इसे detach करना पड़ सकता है (`tmux detach`) या `tmux attach -t 1 -d` चलाकर force attach करना पड़ सकता है ताकि अन्य clients detach हो जाएं।
- अनचाहे sessions को साफ़ करने के लिए, आप उन्हें `tmux kill-session -t <session>` (जैसे `tmux kill-session -t 8`) से kill कर सकते हैं।

यह दृष्टिकोण सुनिश्चित करता है कि आप session count बढ़ाए बिना sessions जैसे `1` या `2` का पुन: उपयोग करते हैं।

[tmux Man Page](https://man.openbsd.org/tmux.1)