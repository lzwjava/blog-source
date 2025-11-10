---
audio: false
generated: true
image: false
lang: de
layout: post
title: Install GitHub Copilot CLI-Erweiterung
translated: true
type: note
---

Der Befehl `gh extension install github/gh-copilot` installiert die GitHub Copilot-Erweiterung für die GitHub CLI und aktiviert Copilot-Funktionen wie Befehlszeilen-Vorschläge und Erklärungen. Für Enterprise-Nutzer gilt, ob dieser Befehl anwendbar ist, unter bestimmten Bedingungen:

- **Enterprise-Konfiguration**: Enterprise-Nutzer können die Copilot CLI-Erweiterung verwenden, wenn ihre Organisation oder ihr Unternehmen über ein GitHub Copilot Business- oder Copilot Enterprise-Abonnement verfügt und die CLI-Funktion von Administratoren aktiviert wurde. Wenn der Organisationsinhaber oder Enterprise-Administrator Copilot in der CLI deaktiviert hat, kann die Erweiterung nicht verwendet werden, selbst wenn sie installiert ist.[](https://docs.github.com/fr/enterprise-cloud%40latest/copilot/how-tos/set-up/install-copilot-in-the-cli)[](https://docs.github.com/en/enterprise-cloud%40latest/copilot/how-tos/set-up/install-copilot-in-the-cli)
- **Authentifizierung**: Enterprise-Nutzer müssen sich bei der GitHub CLI mit einem GitHub-Konto authentifizieren, dem ein Copilot-Sitzplatz zugewiesen ist. Für verwaltete Benutzerkonten auf GitHub Enterprise Cloud (GHE.com) können zusätzliche Einrichtungsschritte erforderlich sein, z. B. das Aktualisieren von Einstellungen vor der Anmeldung.[](https://docs.github.com/en/enterprise-cloud%40latest/copilot/how-tos/set-up/install-copilot-extension)
- **Installationsvoraussetzungen**: Die GitHub CLI muss installiert sein, bevor der Befehl ausgeführt wird. Der Installationsprozess selbst ist für Enterprise- und individuelle Nutzer gleich, aber Unternehmensrichtlinien können die Nutzung einschränken.[](https://docs.github.com/en/enterprise-cloud%40latest/copilot/how-tos/set-up/install-copilot-in-the-cli)

**Schritte für Enterprise-Nutzer**:
1. Stellen Sie sicher, dass die GitHub CLI installiert ist (siehe [GitHub CLI-Repository](https://github.com/cli/cli) für Anleitungen).
2. Verifizieren Sie bei Ihrem Enterprise-Administrator, dass Copilot CLI für Ihre Organisation aktiviert ist.
3. Führen Sie `gh extension install github/gh-copilot` in Ihrem Terminal aus.
4. Authentifizieren Sie sich mit `gh auth login` unter Verwendung Ihres unternehmenszugeordneten GitHub-Kontos.
5. Wenn Sie ein verwaltetes Benutzerkonto auf GHE.com verwenden, befolgen Sie die zusätzlichen Einrichtungsschritte, die unter [Verwenden von GitHub Copilot mit einem Konto auf GHE.com](https://docs.github.com/en/enterprise-cloud@latest/copilot/configuring-github-copilot-in-your-environment/using-github-copilot-with-an-account-on-ghecom) beschrieben sind.[](https://docs.github.com/en/enterprise-cloud%40latest/copilot/how-tos/set-up/install-copilot-extension)

Wenn Ihr Unternehmen den CLI-Zugriff einschränkt oder Copilot nicht aktiviert hat, kann die Erweiterung zwar installiert werden, funktioniert aber nicht. Wenden Sie sich für Details zu den Richtlinien an Ihren Administrator.

[Installieren von GitHub Copilot in der CLI](https://docs.github.com/en/enterprise-cloud@latest/copilot/installing-github-copilot-in-the-cli)[](https://docs.github.com/en/enterprise-cloud%40latest/copilot/how-tos/set-up/install-copilot-in-the-cli)
[Einrichten von GitHub Copilot für Ihr Unternehmen](https://docs.github.com/en/enterprise-cloud@latest/copilot/setting-up-github-copilot-for-your-enterprise)[](https://docs.github.com/en/enterprise-cloud%40latest/copilot/how-tos/set-up/set-up-for-enterprise)