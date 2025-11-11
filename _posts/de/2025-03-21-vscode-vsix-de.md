---
audio: false
generated: true
lang: de
layout: post
title: VS Code VSIX-Download
translated: true
type: note
---

Um eine `.vsix`-Datei für eine Visual Studio Code (VS Code)-Erweiterung manuell herunterzuladen, können Sie den Visual Studio Marketplace verwenden, auf dem alle offiziellen Erweiterungen gehostet werden. Die `.vsix`-Datei ist das Paketformat für VS Code-Erweiterungen. Obwohl der Marketplace nicht immer einen direkten Download-Button bietet, können Sie die Download-URL konstruieren oder alternative Methoden nutzen. Hier ist eine Schritt-für-Schritt-Anleitung:

### Schritte zum manuellen Herunterladen einer `.vsix`-Datei

1. **Finden Sie die Erweiterung im Visual Studio Marketplace**  
   - Gehen Sie in Ihrem Webbrowser zum [Visual Studio Marketplace](https://marketplace.visualstudio.com/vscode).
   - Suchen Sie nach der gewünschten Erweiterung (z. B. "Python" von Microsoft, "Prettier - Code formatter" usw.).
   - Öffnen Sie die Seite der Erweiterung. Die URL der Python-Erweiterung könnte beispielsweise so aussehen:  
     `https://marketplace.visualstudio.com/items?itemName=ms-python.python`.

2. **Identifizieren Sie den Publisher und den Erweiterungsnamen**  
   - Notieren Sie sich auf der Seite der Erweiterung den **Publisher** und den **Erweiterungs-Identifier**. Diese sind Teil der URL oder auf der Seite angegeben.
   - In `ms-python.python` ist beispielsweise `ms-python` der Publisher und `python` der Erweiterungsname.

3. **Konstruieren Sie die Download-URL**  
   - Die `.vsix`-Datei kann direkt über ein spezifisches URL-Muster des Marketplaces heruntergeladen werden. Das allgemeine Format lautet:  
     ```
     https://<publisher>.gallery.vsassets.io/_apis/public/gallery/publisher/<publisher>/extension/<extension-name>/latest/assetbyname/Microsoft.VisualStudio.Services.VSIXPackage
     ```
   - Ersetzen Sie `<publisher>` mit dem Namen des Publishers und `<extension-name>` mit dem Erweiterungsnamen.
   - Für die Python-Erweiterung (`ms-python.python`) wäre die URL:  
     ```
     https://ms-python.gallery.vsassets.io/_apis/public/gallery/publisher/ms-python/extension/python/latest/assetbyname/Microsoft.VisualStudio.Services.VSIXPackage
     ```
   - Fügen Sie diese URL in Ihren Browser ein, und der Download der `.vsix`-Datei wird gestartet.

4. **Alternative: Verwenden Sie den Link „Download Extension“ auf der Marketplace-Seite (falls verfügbar)**  
   - Einige Erweiterungsseiten enthalten einen Link „Download Extension“ im Abschnitt **Resources** oder an anderer Stelle. Wenn vorhanden, klicken Sie darauf, um die `.vsix`-Datei direkt herunterzuladen. Dies ist jedoch weniger verbreitet, daher ist die URL-Methode zuverlässiger.

5. **Überprüfen Sie den Download**  
   - Die heruntergeladene Datei hat die Erweiterung `.vsix` (z. B. `ms-python.python-<version>.vsix`).
   - Überprüfen Sie die Dateigröße und den Namen, um sicherzustellen, dass sie mit der erwarteten Erweiterung und Version übereinstimmen.

6. **Installieren Sie die `.vsix`-Datei in VS Code (Optional)**  
   - Öffnen Sie VS Code.
   - Gehen Sie zur Erweiterungsansicht (`Strg+Umschalt+X` oder `Cmd+Umschalt+X` auf macOS).
   - Klicken Sie auf das Drei-Punkte-Menü (`...`) oben rechts im Erweiterungsbereich.
   - Wählen Sie **Install from VSIX**, navigieren Sie zur heruntergeladenen `.vsix`-Datei und wählen Sie sie aus.

### Beispielhafte Vorgehensweise
Angenommen, Sie möchten die **ESLint**-Erweiterung von Dirk Baeumer:
- Marketplace-URL: `https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint`
- Publisher: `dbaeumer`
- Erweiterungsname: `vscode-eslint`
- Download-URL:  
  ```
  https://dbaeumer.gallery.vsassets.io/_apis/public/gallery/publisher/dbaeumer/extension/vscode-eslint/latest/assetbyname/Microsoft.VisualStudio.Services.VSIXPackage
  ```
- Öffnen Sie diese URL in Ihrem Browser, und die `.vsix`-Datei (z. B. `dbaeumer.vscode-eslint-<version>.vsix`) wird heruntergeladen.

### Hinweise
- **Version**: Der Teil `/latest/` in der URL stellt sicher, dass Sie die neueste Version erhalten. Wenn Sie eine bestimmte Version benötigen, benötigen Sie typischerweise die Versionsnummer (sichtbar im Tab „Version History“ des Marketplaces) und müssten die URL anpassen oder ein Tool wie `ovsx` verwenden (siehe unten). Die Marketplace-API macht ältere Versionen jedoch nicht immer einfach über eine direkte URL zugänglich.
- **Blockierte Downloads**: Wenn die URL nicht funktioniert, könnte der Publisher den direkten Zugriff einschränken oder Ihr Browser/Netzwerk könnte ihn blockieren. Versuchen Sie in solchen Fällen einen anderen Browser oder einen Download-Manager.
- **Alternative Tools**: Sie können ein Kommandozeilen-Tool wie `ovsx` (vom Open VSX Registry) verwenden, um Erweiterungen herunterzuladen. Installieren Sie es via npm (`npm install -g ovsx`) und führen Sie dann aus:  
  ```
  ovsx download ms-python.python
  ```
  Dies lädt die `.vsix`-Datei programmgesteuert herunter.

### Zusammenfassung
Um eine `.vsix`-Datei für eine VS Code-Erweiterung manuell herunterzuladen:
1. Gehen Sie zur Seite der Erweiterung auf dem [Visual Studio Marketplace](https://marketplace.visualstudio.com/vscode).
2. Identifizieren Sie den Publisher und den Erweiterungsnamen (z. B. `ms-python.python`).
3. Verwenden Sie dieses URL-Format in Ihrem Browser:  
   ```
   https://<publisher>.gallery.vsassets.io/_apis/public/gallery/publisher/<publisher>/extension/<extension-name>/latest/assetbyname/Microsoft.VisualStudio.Services.VSIXPackage
   ```
4. Laden Sie die `.vsix`-Datei herunter und installieren Sie sie optional in VS Code.