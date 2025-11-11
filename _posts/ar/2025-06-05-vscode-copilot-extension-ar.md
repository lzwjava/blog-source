---
audio: false
generated: true
lang: ar
layout: post
title: كيفية استدعاء GitHub Copilot من إضافة VSCode
translated: true
type: note
---

GitHub Copilot هو مساعد برمجة قوي يعمل بالذكاء الاصطناعي ومدمج في Visual Studio Code (VSCode) وIntelliJ IDEA من خلال الإضافات الخاصة بهما. بينما لا يوجد واجهة برمجة تطبيقات REST عامة لاستدعاء Copilot مباشرة، يمكن للمطورين التفاعل مع إمكانياته برمجيًا داخل إضافة VSCode باستخدام VSCode Chat API أو Language Model API أو التفاعلات القائمة على الأوامر. تناقش هذه المدونة خطوات إنشاء إضافة VSCode تُطلق وظيفة الدردشة في Copilot باستخدام موجه مخصص، مما يحاكي بشكل فعال "استدعاء واجهة برمجة تطبيقات" لـ Copilot، وتشرح كيفية الاستفادة من Copilot نفسه لتبسيط عملية التطوير.

## فهم تكامل Copilot في VSCode

لا توفر GitHub Copilot واجهة برمجة تطبيقات تقليدية (مثل نقاط نهاية REST) للوصول البرمجي المباشر. بدلاً من ذلك، تتوفر وظيفتها من خلال:
- **VSCode Chat API**: يمكّن الإضافات من إنشاء مشاركين دردشة مخصصين يتفاعلون مع نظام دردشة Copilot للاستعلامات باللغة الطبيعية.
- **VSCode Language Model API**: يسمح للإضافات بالوصول إلى النماذج اللغوية الكبيرة (LLMs) الخاصة بـ Copilot لمهام مثل توليد الكود أو التحليل.
- **VSCode Commands**: يسمح بتشغيل الميزات المضمنة في Copilot، مثل فتح نافذة الدردشة بموجه محدد مسبقًا.

يركز هذا الدليل على استخدام الأمر `workbench.action.chat.open` لتفعيل واجهة دردشة Copilot، حيث إنه أبسط طريقة لدمج إمكانيات Copilot في إضافة.

## خطوة بخطوة: بناء إضافة VSCode لتفعيل دردشة Copilot

أدناه دليل خطوة بخطوة لإنشاء إضافة VSCode تفتح نافذة دردشة Copilot بموجه مخصص، مما "يستدعي" Copilot بشكل فعال لمعالجة استعلام محدد من قبل المستخدم.

### 1. إعداد إضافة VSCode

1. **هيكلة المشروع**:
   - قم بتثبيت منشئ إضافة VSCode Yeoman: `npm install -g yo generator-code`.
   - شغّل `yo code` واختر "New Extension (TypeScript)" لإنشاء إضافة مبنية على TypeScript.
   - قم بتسمية الإضافة، على سبيل المثال، `copilot-api-caller`.

2. **تهيئة `package.json`**:
   - حدد أمرًا لتفعيل دردشة Copilot.
   - مثال `package.json`:

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

   - **باستخدام Copilot**: أثناء تحرير `package.json`، قد يقترح Copilot حقولًا مثل `contributes.commands` أو `activationEvents` أثناء الكتابة. اقبل هذه الاقتراحات باستخدام `Tab` لتسريع الإعداد.

### 2. كتابة كود الإضافة

أنشئ المنطق الخاص بالإضافة لتسجيل أمر يفتح دردشة Copilot بموجه يقدمه المستخدم.

- **الملف**: `src/extension.ts`
- **الكود**:

```typescript
import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
  // Register the command to trigger Copilot Chat
  let disposable = vscode.commands.registerCommand('copilot-api-caller.triggerCopilotChat', async () => {
    // Get user input for the prompt
    const prompt = await vscode.window.showInputBox({
      prompt: 'Enter your query for GitHub Copilot',
      placeHolder: 'e.g., Write a JavaScript function to sort an array'
    });

    if (prompt) {
      try {
        // Execute the command to open Copilot Chat with the prompt
        await vscode.commands.executeCommand('workbench.action.chat.open', prompt);
        vscode.window.showInformationMessage('Sent prompt to Copilot Chat!');
      } catch (error) {
        vscode.window.showErrorMessage(`Failed to trigger Copilot Chat: ${error}`);
      }
    }
  });

  context.subscriptions.push(disposable);
}

export function deactivate() {}
```

- **كيفية العمل**:
  - يسجل أمر `copilot-api-caller.triggerCopilotChat`.
  - يطلب من المستخدم إدخال استعلام (مثال: "Write a Python function to reverse a string").
  - يستخدم `vscode.commands.executeCommand('workbench.action.chat.open', prompt)` لفتح نافذة دردشة Copilot مع الموجه.
- **باستخدام Copilot**: في VSCode، اكتب `import * as vscode` وسيقترح Copilot الاستيراد الكامل. أضف تعليقًا مثل `// Register a command to open Copilot Chat`، وقد يقترح Copilot هيكل `vscode.commands.registerCommand`. لتنفيذ الأمر، اكتب `// Open Copilot Chat with a prompt`، وقد يقترح Copilot استدعاء `executeCommand`.

### 3. التحسين بإضافة السياق (اختياري)

لجعل الإضافة أكثر قوة، قم بتضمين السياق من المحرر، مثل الكود المحدد، لتزويد Copilot بمعلومات إضافية.

- **الكود المعدل** (`src/extension.ts`):

```typescript
import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
  let disposable = vscode.commands.registerCommand('copilot-api-caller.triggerCopilotChat', async () => {
    // Get selected text from the active editor
    const editor = vscode.window.activeTextEditor;
    let context = '';
    if (editor) {
      const selection = editor.selection;
      context = editor.document.getText(selection);
    }

    // Prompt for user input
    const prompt = await vscode.window.showInputBox({
      prompt: 'Enter your query for GitHub Copilot',
      placeHolder: 'e.g., Explain this code',
      value: context ? `Regarding this code: \n\`\`\`\n${context}\n\`\`\`\n` : ''
    });

    if (prompt) {
      try {
        await vscode.commands.executeCommand('workbench.action.chat.open', prompt);
        vscode.window.showInformationMessage('Sent prompt to Copilot Chat!');
      } catch (error) {
        vscode.window.showErrorMessage(`Failed to trigger Copilot Chat: ${error}`);
      }
    }
  });

  context.subscriptions.push(disposable);
}

export function deactivate() {}
```

- **كيفية العمل**:
  - يسترجع النص المحدد من المحرر النشط ويضمنه كسياق في الموجه.
  - يملأ مربع الإدخال مسبقًا بالكود المحدد، مُنسقًا ككتلة كود Markdown.
  - يرسل الموجه المدمج إلى واجهة دردشة Copilot.
- **باستخدام Copilot**: علّق `// Get selected text from editor`، وقد يقترح Copilot `vscode.window.activeTextEditor`. للتنسيق، اكتب `// Format code as markdown`، وقد يقترح Copilot بناء الجملة بثلاثة علامات `.

### 4. اختبار الإضافة

1. اضغط `F5` في VSCode لبدء تشغيل Extension Development Host.
2. افتح لوحة الأوامر (`Ctrl+Shift+P` أو `Cmd+Shift+P`) وشغّل `Trigger Copilot Chat`.
3. أدخل موجهًا (مثال: "Generate a REST API client in TypeScript") أو حدد كودًا وشغّل الأمر.
4. تحقق من أن نافذة دردشة Copilot تفتح مع الموجه الخاص بك وتقدم ردًا.
5. **باستخدام Copilot**: إذا حدثت أخطاء، أضف تعليقًا مثل `// Handle errors for command execution`، وقد يقترح Copilot كتل try-catch أو رسائل خطأ.

### 5. متقدم: استخدام VSCode Chat API

لمزيد من التحكم، استخدم VSCode Chat API لإنشاء مشارك دردشة مخصص يتكامل مع النماذج اللغوية لـ Copilot، مما يسمح بمعالجة اللغة الطبيعية داخل إضافتك.

- **كود المثال** (`src/extension.ts`):

```typescript
import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
  // Register a chat participant
  const participant = vscode.chat.createChatParticipant('copilot-api-caller.myParticipant', async (request, context, stream, token) => {
    stream.markdown('Processing your query...\n');
    // Use the Language Model API to generate a response
    const model = await vscode.lm.selectChatModels({ family: 'gpt-4' })[0];
    if (model) {
      const response = await model.sendRequest([{ text: request.prompt }], {}, token);
      for await (const chunk of response.stream) {
        stream.markdown(chunk);
      }
    } else {
      stream.markdown('No suitable model available.');
    }
  });

  participant.iconPath = new vscode.ThemeIcon('sparkle');
  context.subscriptions.push(participant);
}

export function deactivate() {}
```

- **كيفية العمل**:
  - ينشئ مشارك دردشة (`@copilot-api-caller.myParticipant`) يمكن استدعاؤه في عرض دردشة Copilot.
  - يستخدم Language Model API للوصول إلى نموذج `gpt-4` الخاص بـ Copilot (أو أي نموذج متاح آخر) لمعالجة الموجه.
  - يقوم ببث الرد مرة أخرى إلى عرض الدردشة.
- **باستخدام Copilot**: علّق `// Create a chat participant for Copilot`، وقد يقترح Copilot هيكل `vscode.chat.createChatParticipant`. بالنسبة لـ Language Model API، علّق `// Access Copilot’s LLM`، وقد يقترح Copilot `vscode.lm.selectChatModels`.

### 6. التغليف والنشر

1. قم بتثبيت `vsce`: `npm install -g @vscode/vsce`.
2. شغّل `vsce package` لإنشاء ملف `.vsix`.
3. ثبّت الإضافة في VSCode عبر عرض الإضافات أو شارك ملف `.vsix` مع الآخرين.
4. **باستخدام Copilot**: أضف تعليقًا مثل `// Add script to package extension` في `package.json`، وقد يقترح Copilot سكريبت `vscode:prepublish`.

## الاستفادة من Copilot أثناء التطوير

يمكن لـ GitHub Copilot أن يسرع بشكل كبير من تطوير الإضافات:
- **اقتراحات الكود**: أثناء الكتابة في `src/extension.ts`، يقترح Copilot عمليات الاستيراد، وتسجيل الأوامر، ومعالجة الأخطاء. على سبيل المثال، كتابة `vscode.commands.` تظهر اقتراحات مثل `registerCommand`.
- **هندسة الموجهات**: استخدم تعليقات واضحة مثل `// Trigger Copilot Chat with a user prompt` لتوجيه اقتراحات Copilot. قم بتنقيح التعليقات إذا كانت الاقتراحات غير دقيقة.
- **تصحيح الأخطاء**: إذا فشلت الإضافة، أضف تعليقات مثل `// Log error details`، وقد يقترح Copilot `console.log` أو `vscode.window.showErrorMessage`.

## القيود

- **لا يوجد وصول مباشر لواجهة برمجة التطبيقات**: لا توفر Copilot واجهة برمجة تطبيقات REST عامة. تعتبر واجهات VSCode Chat API و Language Model API هي واجهات البرمجة الأساسية.
- **المصادقة**: يجب أن يكون للمستخدمين اشتراك Copilot نشط (مجاني أو مدفوع) وأن يكونوا مسجلين الدخول إلى VSCode بحساب GitHub.
- **نطاق Chat API**: يقتصر Chat API على واجهة الدردشة؛ لا يتوفر وصول برمجي مباشر إلى محرك إكمال الكود في Copilot.
- **البيئة**: تأكد من أن الإضافة تلتزم بأي سياسات تنظيمية فيما يتعلق بإضافات VSCode المخصصة.

## الخلاصة

باستخدام نظام الأوامر في VSCode أو Chat API، يمكن للمطورين "استدعاء" GitHub Copilot بشكل فعال من إضافة مخصصة، مما يمكّن التفاعل البرمجي مع إمكانياتها في الذكاء الاصطناعي. يوضح المثال أعلاه تفعيل دردشة Copilot بموجه مخصص، مع تحسينه بسياق المحرر، ويوفر أساسًا للتكاملات الأكثر تقدمًا باستخدام Language Model API. بمساعدة Copilot أثناء التطوير، يصبح إنشاء مثل هذه الإضافات أسرع وأكثر سهولة.

لمزيد من الاستكشاف، فكر في تجربة Chat API للمشاركين المخصصين أو دمج سياق محرر إضافي للحصول على موجهات أكثر ثراءً.