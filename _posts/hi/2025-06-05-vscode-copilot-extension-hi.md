---
audio: false
generated: true
lang: hi
layout: post
title: वीएसकोड एक्सटेंशन से गिटहब कोपिलॉट को कैसे कॉल करें
translated: true
type: note
---

GitHub Copilot एक शक्तिशाली AI-संचालित कोडिंग सहायक है जो Visual Studio Code (VSCode) और IntelliJ IDEA में उनके संबंधित प्लगइन्स के माध्यम से एकीकृत है। हालांकि Copilot को सीधे कॉल करने के लिए कोई सार्वजनिक REST API नहीं है, डेवलपर VSCode Chat API, Language Model API, या कमांड-आधारित इंटरैक्शन का उपयोग करके VSCode एक्सटेंशन के भीतर प्रोग्रामेटिक रूप से इसकी क्षमताओं के साथ इंटरैक्ट कर सकते हैं। यह ब्लॉग पोस्ट एक VSCode एक्सटेंशन बनाने के माध्यम से चलती है जो एक कस्टम प्रॉम्प्ट के साथ Copilot की चैट कार्यक्षमता को ट्रिगर करता है, प्रभावी रूप से Copilot के लिए एक "API कॉल" का सिमुलेशन करता है, और विकास को सुव्यवस्थित करने के लिए Copilot का लाभ उठाने का तरीका बताता है।

## VSCode में Copilot के एकीकरण को समझना

GitHub Copilot सीधे प्रोग्रामेटिक एक्सेस के लिए एक पारंपरिक API (जैसे, REST endpoints) एक्सपोज़ नहीं करता है। इसके बजाय, इसकी कार्यक्षमता इनके माध्यम से उपलब्ध है:
- **VSCode Chat API**: एक्सटेंशन को कस्टम चैट प्रतिभागी बनाने में सक्षम बनाता है जो प्राकृतिक भाषा प्रश्नों के लिए Copilot की चैट सिस्टम के साथ इंटरैक्ट करते हैं।
- **VSCode Language Model API**: एक्सटेंशन को कोड जनरेशन या विश्लेषण जैसे कार्यों के लिए Copilot के बड़े भाषा मॉडल (LLM) तक पहुंचने की अनुमति देता है।
- **VSCode Commands**: Copilot की बिल्ट-इन सुविधाओं, जैसे कि पूर्वनिर्धारित प्रॉम्प्ट के साथ चैट विंडो खोलना, को ट्रिगर करने की अनुमति देता है।

यह गाइड Copilot की चैट इंटरफेस को ट्रिगर करने के लिए `workbench.action.chat.open` कमांड का उपयोग करने पर केंद्रित है, क्योंकि यह Copilot की क्षमताओं को एक्सटेंशन में एकीकृत करने का सबसे सरल तरीका है।

## स्टेप-बाय-स्टेप: Copilot चैट को ट्रिगर करने के लिए एक VSCode एक्सटेंशन बनाना

नीचे एक VSCode एक्सटेंशन बनाने के लिए एक स्टेप-बाय-स्टेप गाइड है जो एक कस्टम प्रॉम्प्ट के साथ Copilot की चैट विंडो खोलता है, प्रभावी रूप से उपयोगकर्ता-परिभाषित क्वेरी को प्रोसेस करने के लिए Copilot को "कॉल" करता है।

### 1. VSCode एक्सटेंशन सेट अप करें

1. **प्रोजेक्ट स्कैफोल्ड करें**:
   - Yeoman VSCode एक्सटेंशन जनरेटर इंस्टॉल करें: `npm install -g yo generator-code`.
   - `yo code` चलाएं और "New Extension (TypeScript)" चुनें ताकि TypeScript-आधारित एक्सटेंशन बन सके।
   - एक्सटेंशन का नाम दें, उदाहरण के लिए, `copilot-api-caller`.

2. **`package.json` कॉन्फ़िगर करें**:
   - Copilot की चैट को ट्रिगर करने के लिए एक कमांड परिभाषित करें।
   - उदाहरण `package.json`:

```json
{
  "name": "copilot-api-caller",
  "displayName": "Copilot API Caller",
  "description": "Triggers GitHub Copilot Chat with a custom prompt",
  "version": "0.0.1",
  "engines": {
    "vscode": "^1.85.0"
  },
  "categories": ["Other"],
  "activationEvents": [
    "onCommand:copilot-api-caller.triggerCopilotChat"
  ],
  "main": "./out/extension.js",
  "contributes": {
    "commands": [
      {
        "command": "copilot-api-caller.triggerCopilotChat",
        "title": "Trigger Copilot Chat"
      }
    ]
  },
  "scripts": {
    "vscode:prepublish": "npm run compile",
    "compile": "tsc -p ./",
    "watch": "tsc -watch -p ./"
  },
  "devDependencies": {
    "@types/vscode": "^1.85.0",
    "@types/node": "^20.2.5",
    "typescript": "^5.1.3"
  }
}
```

   - **Copilot का उपयोग करते हुए**: `package.json` को एडिट करते समय, जैसे ही आप टाइप करते हैं, Copilot `contributes.commands` या `activationEvents` जैसे फील्ड सुझा सकता है। सेटअप को तेजी से पूरा करने के लिए इन्हें `Tab` से स्वीकार करें।

### 2. एक्सटेंशन कोड लिखें

एक्सटेंशन लॉजिक बनाएं जो एक कमांड रजिस्टर करे जो उपयोगकर्ता-प्रदत्त प्रॉम्प्ट के साथ Copilot की चैट खोलता है।

- **फ़ाइल**: `src/extension.ts`
- **कोड**:

```typescript
import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
  // Copilot Chat को ट्रिगर करने के लिए कमांड रजिस्टर करें
  let disposable = vscode.commands.registerCommand('copilot-api-caller.triggerCopilotChat', async () => {
    // प्रॉम्प्ट के लिए उपयोगकर्ता इनपुट प्राप्त करें
    const prompt = await vscode.window.showInputBox({
      prompt: 'GitHub Copilot के लिए अपनी क्वेरी दर्ज करें',
      placeHolder: 'उदा., एक array को sort करने के लिए एक JavaScript function लिखें'
    });

    if (prompt) {
      try {
        // प्रॉम्प्ट के साथ Copilot Chat खोलने के लिए कमांड execute करें
        await vscode.commands.executeCommand('workbench.action.chat.open', prompt);
        vscode.window.showInformationMessage('प्रॉम्प्ट Copilot Chat को भेज दिया गया!');
      } catch (error) {
        vscode.window.showErrorMessage(`Copilot Chat को ट्रिगर करने में विफल: ${error}`);
      }
    }
  });

  context.subscriptions.push(disposable);
}

export function deactivate() {}
```

- **यह कैसे काम करता है**:
  - एक कमांड `copilot-api-caller.triggerCopilotChat` रजिस्टर करता है।
  - उपयोगकर्ता से एक क्वेरी (जैसे, "एक string को reverse करने के लिए एक Python function लिखें") के लिए प्रॉम्प्ट करता है।
  - प्रॉम्प्ट के साथ Copilot की चैट विंडो खोलने के लिए `vscode.commands.executeCommand('workbench.action.chat.open', prompt)` का उपयोग करता है।
- **Copilot का उपयोग करते हुए**: VSCode में, `import * as vscode` टाइप करें और Copilot पूरा import सुझाएगा। एक कमेंट जोड़ें जैसे `// Copilot Chat खोलने के लिए एक कमांड रजिस्टर करें`, और Copilot `vscode.commands.registerCommand` संरचना प्रस्तावित कर सकता है। कमांड execution के लिए, `// एक प्रॉम्प्ट के साथ Copilot Chat खोलें` टाइप करें, और Copilot `executeCommand` कॉल सुझा सकता है।

### 3. संदर्भ के साथ बढ़ाना (वैकल्पिक)

एक्सटेंशन को और अधिक शक्तिशाली बनाने के लिए, एडिटर से संदर्भ शामिल करें, जैसे कि चयनित कोड, ताकि Copilot को अतिरिक्त जानकारी प्रदान की जा सके।

- **संशोधित कोड** (`src/extension.ts`):

```typescript
import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
  let disposable = vscode.commands.registerCommand('copilot-api-caller.triggerCopilotChat', async () => {
    // सक्रिय एडिटर से चयनित टेक्स्ट प्राप्त करें
    const editor = vscode.window.activeTextEditor;
    let context = '';
    if (editor) {
      const selection = editor.selection;
      context = editor.document.getText(selection);
    }

    // उपयोगकर्ता इनपुट के लिए प्रॉम्प्ट करें
    const prompt = await vscode.window.showInputBox({
      prompt: 'GitHub Copilot के लिए अपनी क्वेरी दर्ज करें',
      placeHolder: 'उदा., इस कोड को समझाएं',
      value: context ? `इस कोड के संबंध में: \n\`\`\`\n${context}\n\`\`\`\n` : ''
    });

    if (prompt) {
      try {
        await vscode.commands.executeCommand('workbench.action.chat.open', prompt);
        vscode.window.showInformationMessage('प्रॉम्प्ट Copilot Chat को भेज दिया गया!');
      } catch (error) {
        vscode.window.showErrorMessage(`Copilot Chat को ट्रिगर करने में विफल: ${error}`);
      }
    }
  });

  context.subscriptions.push(disposable);
}

export function deactivate() {}
```

- **यह कैसे काम करता है**:
  - सक्रिय एडिटर से चयनित टेक्स्ट प्राप्त करता है और इसे प्रॉम्प्ट में संदर्भ के रूप में शामिल करता है।
  - इनपुट बॉक्स को चयनित कोड के साथ प्री-फिल करता है, जिसे Markdown कोड ब्लॉक के रूप में फॉर्मेट किया गया है।
  - संयुक्त प्रॉम्प्ट को Copilot के चैट इंटरफेस पर भेजता है।
- **Copilot का उपयोग करते हुए**: कमेंट करें `// एडिटर से चयनित टेक्स्ट प्राप्त करें`, और Copilot `vscode.window.activeTextEditor` सुझा सकता है। फॉर्मेटिंग के लिए, `// कोड को markdown के रूप में फॉर्मेट करें` टाइप करें, और Copilot ट्रिपल-बैकटिक सिंटैक्स प्रस्तावित कर सकता है।

### 4. एक्सटेंशन का परीक्षण करें

1. VSCode में `F5` दबाएं ताकि Extension Development Host लॉन्च हो।
2. कमांड पैलेट (`Ctrl+Shift+P` या `Cmd+Shift+P`) खोलें और `Trigger Copilot Chat` चलाएं।
3. एक प्रॉम्प्ट दर्ज करें (उदा., "TypeScript में एक REST API क्लाइंट जनरेट करें") या कोड का चयन करें और कमांड चलाएं।
4. सत्यापित करें कि आपके प्रॉम्प्ट के साथ Copilot की चैट विंडो खुलती है और एक प्रतिक्रिया प्रदान करती है।
5. **Copilot का उपयोग करते हुए**: यदि त्रुटियां होती हैं, तो एक कमेंट जोड़ें जैसे `// कमांड execution के लिए त्रुटियों को हैंडल करें`, और Copilot try-catch ब्लॉक या त्रुटि संदेश सुझा सकता है।

### 5. एडवांस्ड: VSCode Chat API का उपयोग करना

अधिक नियंत्रण के लिए, VSCode Chat API का उपयोग करें ताकि एक कस्टम चैट प्रतिभागी बन सके जो Copilot के भाषा मॉडल के साथ एकीकृत हो, जो आपके एक्सटेंशन के भीतर प्राकृतिक भाषा प्रोसेसिंग की अनुमति देता है।

- **उदाहरण कोड** (`src/extension.ts`):

```typescript
import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
  // एक चैट प्रतिभागी रजिस्टर करें
  const participant = vscode.chat.createChatParticipant('copilot-api-caller.myParticipant', async (request, context, stream, token) => {
    stream.markdown('आपकी क्वेरी प्रोसेस हो रही है...\n');
    // प्रतिक्रिया उत्पन्न करने के लिए Language Model API का उपयोग करें
    const model = await vscode.lm.selectChatModels({ family: 'gpt-4' })[0];
    if (model) {
      const response = await model.sendRequest([{ text: request.prompt }], {}, token);
      for await (const chunk of response.stream) {
        stream.markdown(chunk);
      }
    } else {
      stream.markdown('कोई उपयुक्त मॉडल उपलब्ध नहीं है।');
    }
  });

  participant.iconPath = new vscode.ThemeIcon('sparkle');
  context.subscriptions.push(participant);
}

export function deactivate() {}
```

- **यह कैसे काम करता है**:
  - एक चैट प्रतिभागी (`@copilot-api-caller.myParticipant`) बनाता है जिसे Copilot Chat व्यू में इनवोक किया जा सकता है।
  - प्रॉम्प्ट को प्रोसेस करने के लिए Copilot के `gpt-4` मॉडल (या कोई अन्य उपलब्ध मॉडल) तक पहुंचने के लिए Language Model API का उपयोग करता है।
  - प्रतिक्रिया को चैट व्यू पर वापस स्ट्रीम करता है।
- **Copilot का उपयोग करते हुए**: कमेंट करें `// Copilot के लिए एक चैट प्रतिभागी बनाएं`, और Copilot `vscode.chat.createChatParticipant` संरचना सुझा सकता है। Language Model API के लिए, कमेंट करें `// Copilot के LLM तक पहुंचें`, और Copilot `vscode.lm.selectChatModels` प्रस्तावित कर सकता है।

### 6. पैकेज और डिप्लॉय करें

1. `vsce` इंस्टॉल करें: `npm install -g @vscode/vsce`.
2. `.vsix` फ़ाइल बनाने के लिए `vsce package` चलाएं।
3. VSCode में एक्सटेंशन को Extensions व्यू के माध्यम से इंस्टॉल करें या `.vsix` फ़ाइल दूसरों के साथ साझा करें।
4. **Copilot का उपयोग करते हुए**: `package.json` में एक कमेंट जोड़ें जैसे `// एक्सटेंशन को पैकेज करने के लिए स्क्रिप्ट जोड़ें`, और Copilot `vscode:prepublish` स्क्रिप्ट सुझा सकता है।

## विकास के दौरान Copilot का लाभ उठाना

GitHub Copilot एक्सटेंशन विकास को काफी तेज कर सकता है:
- **कोड सुझाव**: जैसे ही आप `src/extension.ts` में टाइप करते हैं, Copilot imports, कमांड रजिस्ट्रेशन, और त्रुटि हैंडलिंग सुझाता है। उदाहरण के लिए, `vscode.commands.` टाइप करने पर `registerCommand` जैसे सुझाव प्रॉम्प्ट होते हैं।
- **प्रॉम्प्ट इंजीनियरिंग**: Copilot के सुझावों को मार्गदर्शन देने के लिए स्पष्ट कमेंट्स का उपयोग करें जैसे `// उपयोगकर्ता प्रॉम्प्ट के साथ Copilot Chat को ट्रिगर करें`। यदि सुझाव गलत हैं तो कमेंट्स को परिष्कृत करें।
- **डीबगिंग**: यदि एक्सटेंशन विफल हो जाती है, तो कमेंट्स जोड़ें जैसे `// त्रुटि विवरण लॉग करें`, और Copilot `console.log` या `vscode.window.showErrorMessage` सुझा सकता है।

## सीमाएँ

- **कोई सीधी API एक्सेस नहीं**: Copilot कोई सार्वजनिक REST API एक्सपोज़ नहीं करता है। VSCode Chat और Language Model APIs प्राथमिक प्रोग्रामेटिक इंटरफेस हैं।
- **प्रमाणीकरण**: उपयोगकर्ताओं के पास एक सक्रिय Copilot सब्सक्रिप्शन (मुफ्त या भुगतान) होना चाहिए और VSCode में GitHub अकाउंट के साथ साइन इन होना चाहिए।
- **Chat API स्कोप**: Chat API चैट इंटरफेस तक सीमित है; Copilot के कोड कम्प्लीशन इंजन तक सीधी पहुंच प्रोग्रामेटिक रूप से उपलब्ध नहीं है।
- **वातावरण**: सुनिश्चित करें कि एक्सटेंशन कस्टम VSCode एक्सटेंशन से संबंधित किसी भी संगठनात्मक नीति का अनुपालन करती है।

## निष्कर्ष

VSCode की कमांड सिस्टम या Chat API का उपयोग करके, डेवलपर एक कस्टम एक्सटेंशन से GitHub Copilot को प्रभावी ढंग से "कॉल" कर सकते हैं, जिससे इसकी AI क्षमताओं के साथ प्रोग्रामेटिक इंटरैक्शन सक्षम होता है। ऊपर दिया गया उदाहरण एक कस्टम प्रॉम्प्ट के साथ Copilot की चैट को ट्रिगर करना प्रदर्शित करता है, जिसे एडिटर संदर्भ के साथ बढ़ाया गया है, और Language Model API का उपयोग करके अधिक उन्नत एकीकरण के लिए एक आधार प्रदान करता है। विकास के दौरान Copilot की सहायता से, ऐसे एक्सटेंशन बनाना तेज और अधिक सहज हो जाता है।

आगे की खोज के लिए, कस्टम प्रतिभागियों के लिए Chat API के साथ प्रयोग करने पर विचार करें या समृद्ध प्रॉम्प्ट के लिए अतिरिक्त एडिटर संदर्भ को एकीकृत करें। हैप्पी कोडिंग!