---
audio: false
lang: en
layout: post
title: Enable Word Wrapping Only for Specific File Extensions
translated: false
---

I assume you're asking how to configure Visual Studio Code (VS Code) to enable word wrapping only for specific file extensions. Here's how you can achieve that:

1. **Open VS Code Settings**:
   - Press `Ctrl + ,` (or `Cmd + ,` on macOS) to open the settings, or go to `File > Preferences > Settings`.

2. **Use the JSON Settings File**:
   - In the Settings UI, click the `{}` icon in the top-right corner to open the `settings.json` file. This allows for more granular control.

3. **Configure Word Wrap per File Type**:
   - Add a configuration using the `"[filetype]": {}` syntax to specify settings for specific file extensions. For example, to enable word wrapping only for `.md` (Markdown) and `.txt` (Text) files, you can add something like this:

   ```json
   {
       "editor.wordWrap": "off", // Default: no wrapping for all files
       "[markdown]": {
           "editor.wordWrap": "on" // Wrap only for .md files
       },
       "[plaintext]": {
           "editor.wordWrap": "on" // Wrap only for .txt files
       }
   }
   ```

4. **Explanation**:
   - `"editor.wordWrap": "off"` sets the global default to no wrapping.
   - `"[markdown]"` and `"[plaintext]"` are language identifiers for Markdown and plain text files, respectively. You can replace them with other language identifiers like `[javascript]`, `[python]`, etc., based on the file extensions you want to target.
   - `"editor.wordWrap": "on"` enables wrapping for those specific file types.

5. **Find Language Identifiers**:
   - If you’re unsure of the language identifier for a file extension, open a file of that type in VS Code, click the language mode in the bottom-right corner (e.g., "Plain Text" or "Python"), and note the identifier shown in the command palette when selecting a language.

6. **Save and Test**:
   - Save the `settings.json` file, and VS Code will apply the settings immediately. Open files with different extensions to confirm the behavior.

This approach ensures word wrapping is enabled only for the file types you specify, leaving all others unaffected. Let me know if you need help with specific extensions!