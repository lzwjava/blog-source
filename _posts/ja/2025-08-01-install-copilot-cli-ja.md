---
audio: false
generated: true
image: false
lang: ja
layout: post
title: GitHub Copilot CLI拡張機能のインストール
translated: true
type: note
---

`gh extension install github/gh-copilot` コマンドは、GitHub CLI 用の GitHub Copilot 拡張機能をインストールし、コマンドラインの提案や説明などの Copilot 機能を利用できるようにします。エンタープライズユーザーにとって、このコマンドが適用されるかどうかは特定の条件に依存します：

- **エンタープライズ構成**: エンタープライズユーザーは、自身の組織またはエンタープライズが GitHub Copilot Business または Copilot Enterprise サブスクリプションを保有しており、かつ管理者が CLI 機能を有効にしている場合、Copilot CLI 拡張機能を利用できます。組織のオーナーまたはエンタープライズ管理者が CLI での Copilot を無効にしている場合、拡張機能をインストールしても使用できません。[](https://docs.github.com/fr/enterprise-cloud%40latest/copilot/how-tos/set-up/install-copilot-in-the-cli)[](https://docs.github.com/en/enterprise-cloud%40latest/copilot/how-tos/set-up/install-copilot-in-the-cli)
- **認証**: エンタープライズユーザーは、Copilot のシートが割り当てられている GitHub アカウントで GitHub CLI に認証する必要があります。GitHub Enterprise Cloud (GHE.com) 上のマネージドユーザーアカウントの場合、サインイン前に設定を更新するなどの追加のセットアップが必要になることがあります。[](https://docs.github.com/en/enterprise-cloud%40latest/copilot/how-tos/set-up/install-copilot-extension)
- **インストール要件**: コマンドを実行する前に GitHub CLI がインストールされている必要があります。インストールプロセス自体はエンタープライズユーザーと個人ユーザーで同じですが、エンタープライズポリシーによって使用が制限される場合があります。[](https://docs.github.com/en/enterprise-cloud%40latest/copilot/how-tos/set-up/install-copilot-in-the-cli)

**エンタープライズユーザーの手順**:
1.  GitHub CLI がインストールされていることを確認します（手順については [GitHub CLI リポジトリ](https://github.com/cli/cli)を参照）。
2.  エンタープライズ管理者に、あなたの組織で Copilot CLI が有効になっていることを確認します。
3.  ターミナルで `gh extension install github/gh-copilot` を実行します。
4.  エンタープライズから割り当てられた GitHub アカウントを使用して `gh auth login` で認証します。
5.  GHE.com のマネージドユーザーアカウントを使用している場合は、[GHE.com のアカウントで GitHub Copilot を使用する](https://docs.github.com/en/enterprise-cloud@latest/copilot/configuring-github-copilot-in-your-environment/using-github-copilot-with-an-account-on-ghecom)で概説されている追加のセットアップ手順に従ってください。[](https://docs.github.com/en/enterprise-cloud%40latest/copilot/how-tos/set-up/install-copilot-extension)

お使いのエンタープライズが CLI アクセスを制限している場合、または Copilot を有効にしていない場合、拡張機能はインストールされても機能しません。ポリシーの詳細については管理者に確認してください。

[CLI への GitHub Copilot のインストール](https://docs.github.com/en/enterprise-cloud@latest/copilot/installing-github-copilot-in-the-cli)[](https://docs.github.com/en/enterprise-cloud%40latest/copilot/how-tos/set-up/install-copilot-in-the-cli)
[エンタープライズ向け GitHub Copilot のセットアップ](https://docs.github.com/en/enterprise-cloud@latest/copilot/setting-up-github-copilot-for-your-enterprise)[](https://docs.github.com/en/enterprise-cloud%40latest/copilot/how-tos/set-up/set-up-for-enterprise)